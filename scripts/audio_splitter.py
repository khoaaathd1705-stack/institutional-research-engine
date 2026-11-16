import os
import sys
import subprocess
import argparse
import math
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import imageio_ffmpeg
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def get_ffmpeg_path() -> str:
    """Retrieve bundled or system ffmpeg executable."""
    return imageio_ffmpeg.get_ffmpeg_exe()

def format_timestamp(seconds: float) -> str:
    """
    Format seconds to mm'm'ss's' format for filename (e.g. 09m45s or 125m30s).
    """
    total_sec = int(round(seconds))
    m = total_sec // 60
    s = total_sec % 60
    return f"{m:02d}m{s:02d}s"

def format_human_time(seconds: float) -> str:
    """Format seconds into HH:MM:SS string."""
    total_sec = int(round(seconds))
    h = total_sec // 3600
    m = (total_sec % 3600) // 60
    s = total_sec % 60
    if h > 0:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"

def get_media_duration(file_path: str, ffmpeg_exe: str) -> float:
    """Get media duration in seconds instantly using ffmpeg header inspection."""
    cmd = [
        ffmpeg_exe,
        "-i", file_path
    ]
    result = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL, text=True, encoding="utf-8", errors="ignore")
    for line in result.stderr.splitlines():
        if "Duration:" in line:
            parts = line.split("Duration:")[1].split(",")[0].strip()
            time_parts = parts.split(":")
            if len(time_parts) == 3:
                h = float(time_parts[0])
                m = float(time_parts[1])
                s = float(time_parts[2])
                return h * 3600 + m * 60 + s
    return 0.0

def process_sliding_window_chunks(
    input_path: str,
    output_dir: str = None,
    chunk_duration: int = 1500,   # 25 phút (1500 giây)
    overlap_duration: int = 20,   # 20 giây gối đầu
    sample_rate: int = 16000,     # 16000 Hz
    bitrate: str = "64k"          # 64 kbps Mono
) -> list[dict]:
    """
    Extracts audio directly from video, converts to 16kHz Mono 64kbps MP3,
    and splits into sliding window overlapping chunks.
    """
    input_file = Path(input_path).resolve()
    if not input_file.exists():
        console.print(f"[bold red]Lỗi: Không tìm thấy file nguồn: {input_file}[/bold red]")
        sys.exit(1)

    step_size = chunk_duration - overlap_duration
    if step_size <= 0:
        console.print("[bold red]Lỗi: chunk_duration phải lớn hơn overlap_duration![/bold red]")
        sys.exit(1)

    if output_dir is None:
        output_dir = input_file.parent / f"{input_file.stem}_chunks"
    else:
        output_dir = Path(output_dir).resolve()

    output_dir.mkdir(parents=True, exist_ok=True)
    ffmpeg_exe = get_ffmpeg_path()

    console.print(Panel(
        f"[bold cyan]File Đầu Vào:[/bold cyan] {input_file.name}\n"
        f"[bold cyan]Dung Lượng Gốc:[/bold cyan] {input_file.stat().st_size / (1024 * 1024):.2f} MB\n"
        f"[bold cyan]Thư Mục Lưu Chunks:[/bold cyan] {output_dir}\n"
        f"[bold cyan]Độ dài mỗi đoạn (chunk_duration):[/bold cyan] {chunk_duration} giây ({chunk_duration // 60} phút)\n"
        f"[bold cyan]Thời gian gối đầu (overlap):[/bold cyan] {overlap_duration} giây\n"
        f"[bold cyan]Bước nhảy (step_size):[/bold cyan] {step_size} giây\n"
        f"[bold cyan]Chuẩn âm thanh:[/bold cyan] Mono (-ac 1), {sample_rate}Hz, Bitrate {bitrate}",
        title="[bold green]Cấu Hình Cắt Gối Đầu (Sliding Window Chunker)[/bold green]"
    ))

    console.print("[yellow]Đang đo tổng thời lượng file media...[/yellow]")
    total_duration = get_media_duration(str(input_file), ffmpeg_exe)
    if total_duration <= 0:
        console.print("[bold red]Lỗi: Không thể xác định thời lượng của file![/bold red]")
        sys.exit(1)

    console.print(f"[green]Tổng thời lượng: {format_human_time(total_duration)} ({total_duration:.1f} giây)[/green]\n")

    # Bước 1: Trích xuất và nén thành master audio tối ưu trước để tránh đọc lặp file video 2-3GB nhiều lần
    temp_master_audio = output_dir / f"__temp_master_{input_file.stem}.mp3"
    console.print("[bold blue]Bước 1/2: Đang trích xuất luồng audio và nén chuẩn giọng nói (16kHz, Mono, 64kbps)...[/bold blue]")

    extract_cmd = [
        ffmpeg_exe,
        "-y",
        "-i", str(input_file),
        "-vn",
        "-ac", "1",
        "-ar", str(sample_rate),
        "-b:a", bitrate,
        str(temp_master_audio)
    ]

    extract_res = subprocess.run(extract_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="ignore")
    if extract_res.returncode != 0:
        console.print("[bold red]Lỗi khi trích xuất audio:[/bold red]")
        console.print(extract_res.stderr[-1000:])
        sys.exit(1)

    master_size_mb = temp_master_audio.stat().st_size / (1024 * 1024)
    console.print(f"[green]Đã tạo audio tổng hợp thành công: {master_size_mb:.2f} MB (Giảm từ {input_file.stat().st_size / (1024 * 1024):.2f} MB)[/green]\n")

    # Bước 2: Cắt các đoạn theo cơ chế gối đầu
    console.print("[bold blue]Bước 2/2: Đang cắt các đoạn gối đầu (Sliding Window)...[/bold blue]")

    chunks_info = []
    chunk_index = 1
    current_start = 0.0

    while current_start < total_duration:
        # Thời lượng thực tế của đoạn này
        current_chunk_len = min(float(chunk_duration), total_duration - current_start)
        current_end = current_start + current_chunk_len

        # Nếu đoạn cuối cùng quá ngắn (dưới 5 giây) và không phải là đoạn duy nhất, bỏ qua vì đã được bao phủ bởi overlap của đoạn trước
        if chunk_index > 1 and current_chunk_len < 5.0:
            break

        start_str = format_timestamp(current_start)
        end_str = format_timestamp(current_end)
        file_name = f"part_{chunk_index:02d}_{start_str}_{end_str}.mp3"
        out_chunk_path = output_dir / file_name

        # Cắt chính xác bằng copy codec (cực nhanh vì master đã là mp3 chuẩn)
        cut_cmd = [
            ffmpeg_exe,
            "-y",
            "-ss", str(current_start),
            "-t", str(current_chunk_len),
            "-i", str(temp_master_audio),
            "-c", "copy",
            str(out_chunk_path)
        ]

        cut_res = subprocess.run(cut_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="ignore")
        if cut_res.returncode != 0:
            # Fallback nếu copy stream có issue
            cut_cmd_reencode = [
                ffmpeg_exe,
                "-y",
                "-ss", str(current_start),
                "-t", str(current_chunk_len),
                "-i", str(temp_master_audio),
                "-ac", "1",
                "-ar", str(sample_rate),
                "-b:a", bitrate,
                str(out_chunk_path)
            ]
            subprocess.run(cut_cmd_reencode, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        chunk_size_mb = out_chunk_path.stat().st_size / (1024 * 1024)
        chunks_info.append({
            "index": chunk_index,
            "filename": file_name,
            "path": str(out_chunk_path),
            "start_time": current_start,
            "end_time": current_end,
            "start_human": format_human_time(current_start),
            "end_human": format_human_time(current_end),
            "duration": current_chunk_len,
            "size_mb": chunk_size_mb
        })

        # Dừng nếu đã chạm đến cuối file
        if current_end >= total_duration:
            break

        current_start += step_size
        chunk_index += 1

    # Dọn dẹp file tạm
    if temp_master_audio.exists():
        temp_master_audio.unlink()

    # Hiển thị bảng kết quả
    table = Table(title="[bold green]Danh Sách Chunks Gối Đầu (Overlapping Chunks)[/bold green]")
    table.add_column("Phần", justify="center", style="cyan")
    table.add_column("Tên File Xuất Ra", style="bold white")
    table.add_column("Khoảng Thời Gian", justify="center", style="yellow")
    table.add_column("Thời Lượng", justify="center", style="blue")
    table.add_column("Dung Lượng", justify="right", style="green")

    total_chunks_size = 0.0
    for info in chunks_info:
        total_chunks_size += info["size_mb"]
        table.add_row(
            f"Part {info['index']:02d}",
            info["filename"],
            f"{info['start_human']} -> {info['end_human']}",
            f"{info['duration']:.0f}s ({info['duration']/60:.1f}p)",
            f"{info['size_mb']:.2f} MB"
        )

    console.print(table)
    console.print(Panel(
        f"[bold green]Hoàn tất cắt gối đầu cho NotebookLM![/bold green]\n"
        f"Tổng số chunk: [bold cyan]{len(chunks_info)} files[/bold cyan]\n"
        f"Gối đầu (Overlap): [bold yellow]{overlap_duration} giây[/bold yellow] (đảm bảo không bị đứt câu nói)\n"
        f"Thư mục lưu: [underline]{output_dir}[/underline]\n\n"
        f"[bold yellow]👉 Tiếp theo:[/bold yellow] Bạn có thể kéo thả trực tiếp các file trong thư mục trên vào NotebookLM!",
        title="[bold green]Giai Đoạn 1 Thành Công[/bold green]"
    ))

    return chunks_info

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tách và cắt video theo cơ chế gối đầu (Sliding Window Overlap) cho NotebookLM")
    parser.add_argument("input", help="Đường dẫn đến file video nguồn (MP4, MKV...) hoặc audio nguồn")
    parser.add_argument("--out", "-o", default=None, help="Thư mục xuất các file MP3 con")
    parser.add_argument("--duration", "-d", type=int, default=1500, help="Độ dài tối đa mỗi đoạn (giây, mặc định 1500s = 25 phút)")
    parser.add_argument("--overlap", "-v", type=int, default=20, help="Thời gian gối đầu giữa 2 đoạn liền kề (giây, mặc định 20s)")
    parser.add_argument("--samplerate", "-r", type=int, default=16000, help="Tần số lấy mẫu âm thanh (Hz, mặc định 16000Hz)")
    parser.add_argument("--bitrate", "-b", default="64k", help="Bitrate âm thanh (mặc định 64k)")

    args = parser.parse_args()
    process_sliding_window_chunks(
        input_path=args.input,
        output_dir=args.out,
        chunk_duration=args.duration,
        overlap_duration=args.overlap,
        sample_rate=args.samplerate,
        bitrate=args.bitrate
    )
