# -*- coding: utf-8 -*-
"""
Build standardized full_transcript.md and full_transcript.docx for BIDV (BID).
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

TRANSCRIPT_MD = """# BANK FOR INVESTMENT AND DEVELOPMENT OF VIETNAM (BIDV - BID)
# 3Q26 & 9M26 EARNINGS CALL TRANSCRIPT

* **Reporting Period**: 3Q26 & First Nine Months of 2026 (9M26) – 4Q26 Outlook & FY27 Guidance
* **Date**: November 2026 (Call Duration: 42:59)
* **Host**: Joint Stock Commercial Bank for Investment and Development of Vietnam (Ticker: BID / BIDV)
* **Participants & Speakers**:
  - **Management Representative** – Board of Management & Senior Leadership, BIDV
  - **Head of Investor Relations** – Investor Relations Department, BIDV
  - **Institutional Analysts**: MBIS, Horizon Capital, HD Securities, Vietcap, VPBankS, VPS Securities, Shinhan Securities, VCBF, PYN Elite Fund, FPTS, Thien Viet Securities (TVS)
* **Benchmark Source**: `BIDV Presentation 3Q26.pdf` (29 official presentation slides)
* **Editorial & Compliance Standards**:
  - `Spoken Text`: Cleaned verbatim speech standardized into professional institutional English, eliminating conversational hesitations, false starts, and speech-to-text acoustic artifacts.
  - `> *[Editorial Note: Reference Slide X: ...]*`: Cross-reference footnotes linking verbal disclosures directly to official presentation slides (Ground Truth).
  - `Standardized Notation`: Unified quarter notation (`3Q26`, `9M26`, `4Q26`, `3Q25`, `FY26`, `FY27`).
  - `Number Convention`: International standard (dot `.` for decimals, comma `,` for thousands).

---

## 01  |  Opening Remarks and FY26 Full-Year Guidance Outlook

**[Head of Investor Relations – BIDV]**:
"Good afternoon, ladies and gentlemen, and welcome to BIDV's third quarter 2026 earnings conference call. We have received our first group of questions from MBIS, Horizon Capital, and HD Securities: What is your 4Q26 earnings forecast? Could you provide updates on 2027 planning and your sector outlook for 4Q26 and 2027?"

**[Management Representative – BIDV]**:
"Thank you for the questions. Regarding our fourth-quarter earnings outlook: As you are well aware, our bank's operating discipline is strictly focused on delivering our full-year profit targets rather than providing specific quarterly earnings guidance. 

Looking ahead to the remainder of 2026, our 4Q26 earnings performance will primarily depend on three core pillars:

First, credit growth momentum and the net interest income (NII) that we are able to capture across our lending franchises.

Second, net fee and commission income combined with bad debt recoveries. As shared earlier, we are actively targeting full-year debt recoveries written off of approximately 14,000 billion VND. Under favorable macroeconomic and asset resolution conditions, we may exceed this threshold.

Third, the appropriate calibration of credit risk provisions. Our overarching priority is to fully achieve the annual profit before tax target approved by the AGM while maintaining stringent risk management buffers.

Regarding your question on 2027 planning: At this stage, it is still premature for BIDV to disclose finalized business budget figures for 2027. However, at the macro and banking sector level, we forecast system-wide credit growth of approximately 16% in 2027, driven by accelerated public investment disbursement, key national infrastructure projects, manufacturing expansion, and robust FDI inflows.

For BIDV specifically, looking back across previous operating cycles, our assigned credit quota generally matches system-wide credit growth. Consequently, we aim to achieve credit growth in the range of 15% to 16% in 2027. Our operating departments at the Head Office are currently consolidating figures to submit the comprehensive business plan to the Board of Directors and Board of Management for official approval. Once finalized, we will promptly disclose the detailed targets to the investment community."

> *[Editorial Note: Reference Slide 04, 06, 08: Vietnam 9M26 GDP grew 9.01% (3Q26: +9.95%), with merchandise exports +24.5% and public investment reaching 658,040 billion VND (+19.0% YoY). BIDV 9M26 PBT reached 29,483 billion VND (+24.8% YoY), completing 88.5% of FY26 guidance (target ~33,300 billion VND). Total operating income reached 67,541 billion VND (+10.5% YoY), with NII reaching 50,594 billion VND (+14.7% YoY) and credit provisions down 5.4% YoY to 15,959 billion VND. System credit growth forecast at +15% to +16% for FY26 and +16% for FY27 (approx. +17% including 18 key national infrastructure projects)]*

---

## 02  |  Credit Growth Drivers, Loan Portfolio Mix & Segment Performance

**[Head of Investor Relations – BIDV]**:
"The next question regarding credit growth and loan portfolio mix comes from Vietcap and VPBankS: Which sectors, customer segments, and loan products drove credit expansion in 9M26? Why did retail lending expand more moderately at 4.0% YTD while SME loans contracted, and what accounted for the wholesale banking segment's growth of 11.5%?"

**[Management Representative – BIDV]**:
"Thank you. Through the end of September 2026, BIDV's credit growth was primarily driven by our Wholesale Banking division, which expanded by 11.5% YTD and contributed approximately 76% of total net loan growth.

Within wholesale banking, the primary growth engines were:
- Large corporate clients (LC), which increased by 12.4% YTD;
- Foreign Direct Investment (FDI) clients, expanding by 54.2% YTD;
- Mid-commercial clients (MIDCOM), which increased by 33.6% YTD.

On the other hand, retail lending grew at a more measured pace of 4.0% YTD. This moderated pace was largely attributable to contractions in residential housing mortgages and business production loans, which partially offset strong double-digit expansions in other consumer lending lines.

From an industry perspective:
- The Services sector led expansion, growing by approximately 30.7% YTD and contributing roughly 72% of the bank's total net loan growth;
- The Manufacturing and processing sector grew solidly by 10.3% YTD, accounting for about 19% of total growth. Together, services and manufacturing represented over 91% of our net credit increase in 9M26."

> *[Editorial Note: Reference Slide 11, 12: Gross customer loans reached 2,561,795 billion VND (+8.0% YTD, +14.5% YoY). Wholesale portfolio reached 1,523 trillion VND (59.4% of total loans), comprising Large Corporates 611 trillion VND (+12.4% YTD, 23.8% share), Mid-commercial 386 trillion VND (+30.3% YTD, 15.1% share), FDI 140 trillion VND (+54.2% YTD, 5.5% share), and SME 387 trillion VND (-6.1% YTD, 15.1% share). Retail loans reached 1,146,805 billion VND (+4.0% YTD, 45.6% total share). In retail by product: Housing loans stood at 334,153 billion VND (-5.8% YTD, 29.1% share), Business production loans stood at 341,234 billion VND (-3.7% YTD, 29.8% share), while Secured consumer loans rose to 225,187 billion VND (+37.3% YTD, 19.6% share). By industry: Services 740 trillion VND (+30.7% YTD, 28.9% share), Manufacturing 580 trillion VND (+10.3% YTD, 22.7% share), Wholesale & Retail 386 trillion VND (-6.0% YTD, 15.1% share)]*

---

## 03  |  Infrastructure Financing & Public Investment Special Credit Mechanism

**[Head of Investor Relations – BIDV]**:
"We have received questions regarding national and public investment projects from VPS Securities, Shinhan Securities, and VCBF: What share of loans goes to public investment projects? Under what conditions does BIDV lend to key national projects outside the standard credit quota, and what are your overall credit growth expectations for 2026 and 2027?"

**[Management Representative – BIDV]**:
"Thank you. For 2026, as you know, BIDV's objective is to fully utilize our approved credit quota of 10.7% assigned by the State Bank of Vietnam (SBV). 

Our involvement in additional infrastructure project financing depends on three fundamental criteria:
1. Project commercial feasibility and debt service viability;
2. Strict adherence to applicable regulatory limits and credit underwriting standards;
3. Our internal capital adequacy and long-term funding mobilization capacity.

At the end of September 2026, BIDV maintained sound capacity for further infrastructure financing. Our existing infrastructure loan portfolio includes approximately 18,400 billion VND in transport BOT project loans and 4,500 billion VND in deep-water seaport infrastructure financing.

We evaluate all potential infrastructure projects through three distinct and rigorous stages: projects under preliminary consideration, approved credit commitments, and actual investment disbursements. Notably, we have reported a 2,000 billion VND credit commitment to one major national transport project under the special credit mechanism—meaning this financing is eligible to be excluded from the SBV's standard annual credit quota.

Heading into 2027, we will continue our rigorous appraisal of customer dossiers and project sponsors to capture viable financing opportunities while safeguarding credit discipline."

> *[Editorial Note: Reference Slide 04, 06, 11: National public investment disbursement reached 658,040 billion VND (+19.0% YoY) in 9M26. System-wide infrastructure pipeline includes 18 national key transport and logistics projects expected to add ~1.0 ppt to 2027 credit growth. Decision 1743/QD-NHNN allows 50% of term State Treasury deposits to count toward LDR through July 2028 (lowering BIDV LDR by ~1.6 - 1.7 ppt). Circular 25/2026/TT-NHNN raised short-term funds for medium- and long-term lending ceiling to 40% (BIDV comfortably at 24.49%)]*

---

## 04  |  Mortgage Book Dynamics, Interest Rate Floating Migration & Group 2 Loans

**[Head of Investor Relations – BIDV]**:
"The next set of questions concerns mortgages and asset quality from MBS, Shinhan Securities, and VCBF: What share of your residential mortgage portfolio has transitioned from fixed to floating interest rates? What are the NPL ratios across mortgages, retail, and SME, and is NPL formation accelerating? Furthermore, please explain why Group 2 loans increased by 32 bps QoQ to 1.54%, which segments drove this increase, and what is your expectation for migration into NPLs?"

**[Management Representative – BIDV]**:
"Thank you. Based on our portfolio data at the end of September 2026:
- Approximately 35% of our residential mortgage portfolio has transitioned to floating interest rates.
- The remaining 65% continues to benefit from fixed promotional interest rates.
- The total mortgage book stood at approximately 341,000 billion VND, carrying an average floating lending rate of 7.28%.

During 3Q26, new mortgage disbursements reached approximately 14,000 billion VND. However, customer principal repayments totaled approximately 18,000 billion VND, including roughly 14,000 billion VND in early loan prepayments by retail borrowers. Consequently, our outstanding residential mortgage balance contracted by approximately 4,000 billion VND during the quarter.

Regarding the rise in Group 2 loans and 3Q26 NPL formation: Group 2 loans rose by 32 bps QoQ to 1.54%. Three primary factors drove this development:

1. **CIC Cross-Classification Effect**: Under SBV regulations, when a corporate borrower is downgraded or classified as NPL at any other credit institution in the national credit information system (CIC), all outstanding loans of that borrower across the banking system—including at BIDV—must be symmetrically reclassified. This systemic contagion contributed significantly to the rise in our classified debt.
2. **Borrower Operating and Cash Flow Strains**: Given broader macroeconomic headwinds and elevated input costs, certain business borrowers faced temporary cash flow disruptions, leading to payment delays.
3. **Expiration of Circular 02 Restructuring Framework**: With the expiration of Circular 02/2023/TT-NHNN, previously restructured debts that were unable to resume regular debt service were reclassified into their true debt categories.

By customer segment:
- The SME segment experienced the highest stress, with an NPL ratio of approximately 2.2%;
- The Large Corporate segment recorded an NPL ratio of approximately 2.0%;
- The Retail segment remained very well controlled, with an NPL ratio of 1.22% (up 27 bps YTD from 0.95% at year-end 2025). Over 97.5% of our retail loans are secured by high-quality collateral with an average LTV of 59.35%."

> *[Editorial Note: Reference Slide 12, 13: Bank-only Circular 31 NPL ratio was 1.58%, strictly inside the <=1.60% AGM ceiling. Consolidated BCTC NPL ratio was 1.85% (3Q25: 1.87%, 4Q25: 1.47%, 1Q26: 1.76%, 2Q26: 1.83%). Group 2 loans stood at 1.54% (+32 bps QoQ). Retail NPL was 1.22% with 97.5% secured loans and 59.35% average LTV. Total retail customers reached 27.4 million (+2.4 million YTD), SmartBanking active users reached 9.27 million. Retail deposits reached 1,208,109 billion VND (+8.95% YTD), with online deposits reaching 315 trillion VND (+47% YTD, 26% of retail funding)]*

---

## 05  |  Real Estate Sector Exposure and Developer Credit

**[Head of Investor Relations – BIDV]**:
"We have a question regarding BIDV's credit exposure to real estate developers and residential housing compared to year-end 2025: What is the current outstanding balance and portfolio proportion?"

**[Management Representative – BIDV]**:
"Thank you. For corporate real estate developers, our outstanding credit balance currently stands at approximately 240,000 billion VND, reflecting a modest and controlled increase compared to year-end 2025.

When combining developer corporate credit with our residential mortgage portfolio, total real estate-related exposure accounts for 24.1% of BIDV's total outstanding customer loan book. This proportion has been maintained stably over recent years, consistent with our conservative risk appetite and prudential sector lending ceilings."

> *[Editorial Note: Reference Slide 11, 12: Real estate and construction credit: Corporate real estate and construction loans combined represent approximately 104 trillion VND in construction (4.0% share) and developer financing. Total real estate-linked credit (developer corporate loans ~240 trillion VND plus retail mortgages ~341 trillion VND) constitutes 24.1% of total bank-wide credit of 2,562 trillion VND]*

---

## 06  |  Net Interest Margin (NIM) Evolution and Asset-Liability Optimization

**[Head of Investor Relations – BIDV]**:
"We have received questions regarding Net Interest Margin (NIM): How do you view NIM trends for the remainder of 2026 and 2027? Will NIM remain compressed, and what measures will offset cost of funds pressure?"

**[Management Representative – BIDV]**:
"Thank you. At the end of September 2026, BIDV's annualized NIM stood at 2.07% (reported on slide as ~2.10%), remaining essentially flat compared to 2Q26.

The underlying dynamic is that steady asset yield improvements achieved through loan repricing were largely offset by higher cost of funds (COF) across the banking system, which rose due to deposit competition earlier in the year.

For 4Q26 and throughout 2027, we expect NIM to improve gradually based on key structural levers:

On the liability side: We aim to lower our overall cost of funds by actively mobilizing low-cost customer deposits and rebuilding our CASA ratio, supported by retail digital banking penetration.

On the asset side:
1. We are optimizing our asset mix toward higher-yielding medium- and long-term loans, which currently account for over 40% of our portfolio (long-term loans alone represent 33.4%);
2. We continue to prioritize high-margin retail lending;
3. Most importantly, we maintain substantial repricing upside in our retail book: Over the next 12 months, approximately 62,000 billion VND in residential mortgages will conclude their fixed promotional interest period and reprice upward by 200 to 300 basis points. Furthermore, 65% of our mortgage book is scheduled for rate repricing in upcoming quarters.

These positive structural adjustments provide strong support for NIM expansion in 4Q26 and into 2027."

> *[Editorial Note: Reference Slide 05, 08, 10, 15: 9M26 Net interest income reached 50,594 billion VND (+14.7% YoY), contributing 74.9% of total operating income. 3Q26 NII reached 17,056 billion VND (+12.4% YoY). BIDV NIM was 2.10% (vs listed bank median ~3.08%). Customer deposits reached 2,360,525 billion VND (+6.2% YTD), valuable papers reached 311,000 billion VND (+38.0% YTD). CASA ratio stood at 19.9% (vs system median ~19.5%). 62 trillion VND of mortgages to reprice +200-300 bps over next 12 months]*

---

## 07  |  SOE Credit Quota Allocation and Policy Alignment

**[Head of Investor Relations – BIDV]**:
"We have a question from PYN Elite Fund: On a year-to-date basis, net loan disbursement in absolute value among the top three state-owned commercial banks appeared to fall behind certain private commercial banks such as MBB and VPBank. Is this acceptable to the government, and does it fall short of state expectations?"

**[Management Representative – BIDV]**:
"Thank you. As a commercial banking institution, BIDV extends credit strictly based on our internal credit criteria, risk management guidelines, and capital optimization framework.

Whenever a customer approaches BIDV for credit facilities, we thoroughly evaluate project feasibility, debt service capacity, and collateral quality against our institutional standards. We do not face administrative pressure or directives from the State Bank of Vietnam to pursue volume growth at the expense of underwriting quality. 

BIDV assumes full institutional responsibility for every credit facility extended to ensure capital preservation and sustainable returns for our shareholders. We manage our loan book to achieve our own strategic milestones and balance sheet health rather than engaging in absolute volume competition with other institutions."

> *[Editorial Note: Reference Slide 05, 08, 20: BIDV loan growth reached +8.0% YTD to 2,561,795 billion VND, deliberately pacing disbursements to balance liquidity, capital ratios, and asset quality. Total assets reached 3,493,271 billion VND (+4.9% YTD, +13.7% YoY), maintaining BIDV's undisputed position as Vietnam's largest commercial bank by total assets]*

---

## 08  |  Capital Adequacy Ratio (CAR), Tier 2 Bonds & Private Placement Progress

**[Head of Investor Relations – BIDV]**:
"Next, we have questions regarding capital structure from Vietcap, FPTS, and other institutional investors: What is BIDV's current CAR? How will BIDV raise capital through 2027, and what is the latest status of your private equity placement?"

**[Management Representative – BIDV]**:
"Thank you. According to our latest figures at 30 September 2026:
- BIDV's consolidated Capital Adequacy Ratio (CAR) reached 10.13%, improving by approximately 80 basis points YTD (compared to 9.3% - 9.4% in 2025). Tier 1 capital ratio rose to 7.14% (+65 bps YTD).

Regarding the private placement roadmap:
- The approved capital increase plan for 2026–2027 includes the issuance of up to 780,000,000 new ordinary shares (representing approximately 10.71% of outstanding shares as of March 2026).
- Upon completion, BIDV's charter capital will expand from 77,782 billion VND to 107,517 billion VND (+47.68% increase).
- We have selected additional international financial advisors to support execution. We are currently engaged in active discussions with potential institutional and strategic investors. We aim to complete this transaction within the projected roadmap.

In addition to equity expansion, we have an active Tier 2 capital bond issuance program. Over the next two years (2026–2027), we plan to issue approximately 25,000 to 28,000 billion VND in senior and Tier 2 capital bonds to augment regulatory capital and support medium- and long-term asset growth."

> *[Editorial Note: Reference Slide 20: Consolidated CAR reached 10.13% (+80 bps YTD); Tier 1 capital ratio at 7.14% (+65 bps YTD). Charter capital reached 77,782 billion VND (+10.8% YTD); capital bonds balance stood at 67,524 billion VND (+16.6% YTD). Private placement roadmap: 780m shares (~10.71% stake) to lift charter capital to 107,517 billion VND (+47.68%). New equity capital target: +10,063 billion VND in 2026 and +30,342 billion VND in 2027. Basel III Standardised Approach targeted for 1Q27; IRB method targeted by 2030]*

---

## 09  |  Asset Quality Breakdown, Sectoral Strains & Full-Year NPL Ceiling

**[Head of Investor Relations – BIDV]**:
"We have a follow-up question regarding asset quality: Which sectors are experiencing significant increases in NPLs, and what is BIDV's view on new NPL formation over the next six months?"

**[Management Representative – BIDV]**:
"Thank you. In terms of sector-specific asset quality:
- We observe localized debt servicing difficulties concentrated in the Construction sector, Building Materials manufacturing, and Wholesale/Retail trade (specifically automobile dealerships and repairs).
- By client segment, SME borrowers remain the most vulnerable segment due to their sensitivity to borrowing costs and domestic consumption demand.

Looking ahead over the next six months: We anticipate operating conditions for SMEs will improve progressively. The SBV's recent policy directives urging lower lending rates, combined with targeted concessionary financing packages introduced by commercial banks, should help viable SMEs restore operational cash flow.

For BIDV as a whole, our AGM-approved target is to keep our bank-only NPL ratio strictly below 1.60% by year-end 2026 under Circular 31. At 1.58% as of 3Q26, we remain firmly on track and are confident in our ability to achieve this objective."

> *[Editorial Note: Reference Slide 13: Bank-only Circular 31 NPL ratio was 1.58% at 30/09/2026, within the <=1.60% AGM ceiling. Credit cost annualized in 3Q26 declined to 0.73% (from 0.94% in 2Q26 and 1.12% in 3Q25; 9M26 credit cost was 0.92%). Consolidated NPL was 1.85% (down 2 bps YoY from 1.87% in 3Q25). Overdue loan ratio stood at 2.43%]*

---

## 10  |  Liquidity Gap Between Credit and Deposit Growth

**[Head of Investor Relations – BIDV]**:
"We have a question from Thien Viet Securities (TVS) regarding system liquidity: What is BIDV's perspective on the gap between credit growth and deposit growth in 2026 and 2027?"

**[Management Representative – BIDV]**:
"Thank you. Earlier in 2026, the gap between credit growth and customer deposit mobilization across the domestic banking system was quite wide—at its peak, credit outpaced deposits by roughly 2.5 percentage points, creating funding tension in the interbank market.

However, recent data demonstrates that this gap has narrowed meaningfully. For BIDV specifically, 3Q26 marked an inflection point: For the first time this year, our customer deposit mobilization outpaced loan disbursement (+9.2% YTD for gross deposits vs +8.0% YTD for gross loans).

This strong deposit accumulation significantly enhances our liquidity buffers, positioning BIDV favorably to accelerate credit deployment in 4Q26 while maintaining comfortable regulatory liquidity ratios."

> *[Editorial Note: Reference Slide 05, 10: System-wide credit growth (+11.7% at 30/9) outpaced deposits by ~1.0 ppt (down from >2.5 ppt earlier in the year). Overnight interbank rates fell from 4.25% in August to 3.41% in September and 0.7% - 4.9% in late October. OMO outstanding plunged from peak ~490 trillion VND in February to ~150.5 trillion VND at end-September. BIDV gross deposits grew 9.2% YTD to 2,680,223 billion VND, surpassing loan growth of 8.0% YTD]*

---

## 11  |  Loan Loss Reserve (LLR) Target and 4Q26 Provisioning Budget

**[Head of Investor Relations – BIDV]**:
"We have a question regarding provision coverage: Given that BIDV's NPL coverage ratio (LLR) dropped to 73.4% at the end of 3Q26, could you please share your target LLR and provision expense budget for 4Q26 and full-year 2026?"

**[Management Representative – BIDV]**:
"Thank you. Our year-end 2026 target for the loan loss reserve coverage ratio (LLR) is to restore coverage to approximately 85%. 

To achieve this, we are allocating substantial provisioning resources in the fourth quarter. We expect our LLR ratio to recover from the current level of ~73.4% to around 85% by 31 December 2026.

For full-year 2026 provision expenses, we have budgeted approximately 24,000 to 25,000 billion VND in credit loss provisions (in line with the 25,240 billion VND booked in FY25). Having already recognized 15,959 billion VND in 9M26, this leaves an estimated 8,500 to 9,000 billion VND in provision expense for 4Q26, providing ample flexibility to absorb write-offs while reaching our 85% coverage objective."

> *[Editorial Note: Reference Slide 13: 9M26 credit loss provision expense reached 15,959 billion VND (-5.4% YoY from 16,862 billion VND in 9M25; 3Q26 provision charge was 4,640 billion VND, down -25.0% YoY). Loan-loss reserve balance stood at 34,871 billion VND (-0.2% YoY from 34,946 billion VND at FY25). NPL coverage ratio stood at 73.4% (vs 99.9% at FY25 and 95.0% at 3Q25). Full-year FY26 provision expense budget is ~25,240 billion VND]*

---

## 12  |  Large Corporate NPLs and Collateral Coverage

**[Head of Investor Relations – BIDV]**:
"The next question comes from Vietcap: Could you please provide more details regarding NPLs in the Large Corporate segment? Which specific industries accounted for the majority of these NPLs, what is the collateral coverage for these facilities, and what is your expectation for loan performance over coming quarters?"

**[Management Representative – BIDV]**:
"Thank you. Within the Large Corporate segment, impaired loans are primarily concentrated among contractors and enterprises operating in the Construction and Construction Materials sectors.

These corporate exposures are supported by robust real estate and asset collateral, giving us strong recovery backing. For coming quarters, our credit management teams are actively restructuring viable obligations and expediting asset resolution. We aim to bring the Large Corporate NPL ratio down toward 2.0% (from currently elevated levels), supporting our bank-wide target of keeping overall NPLs below 1.60% under Circular 31."

> *[Editorial Note: Reference Slide 11, 13: Large corporate loans reached 611 trillion VND (+12.4% YTD, 23.8% of total credit). Construction sector credit stood at 103 trillion VND (-0.4% YTD). Bank-wide 9M26 loan recoveries written off reached 8,266 billion VND (+14.1% YoY), contributing to Other income of 7,789 billion VND (+16.8% YoY)]*

---

## 13  |  Mortgage Book NPLs, Prepayments and Long-Term Real Estate Outlook

**[Head of Investor Relations – BIDV]**:
"We have a follow-up question on retail mortgages: What drove the rise in the mortgage NPL ratio in 3Q26, and how do you expect this book to trend in upcoming quarters?"

**[Management Representative – BIDV]**:
"Thank you. In our mortgage portfolio, borrower stress emerged primarily because preferential interest rate packages granted during the 2023–2025 period have concluded, transitioning borrowers to higher floating rates. This adjustment prompted some borrowers to prepay their debt (~14,000 billion VND in prepayments), which mathematically raised the delinquency ratio on the remaining smaller base.

However, the recent SBV guidance urging lower lending rates is already having an effect. For new residential mortgages, BIDV has reduced lending rates to approximately 9.5%. 

Over the long term, we view these headwinds as transitory. As major public infrastructure developments are completed across Vietnam, connectivity and property market liquidity will rebound, strengthening retail borrowers' debt servicing capacity. Because the vast majority of our mortgage facilities are long-term loans secured by established residential collateral, our long-term asset recovery outlook remains fundamentally sound."

> *[Editorial Note: Reference Slide 12: Retail loan balance stood at 1,146,805 billion VND (+4.0% YTD). Housing loans reached 334,153 billion VND (-5.8% YTD, 29.1% share of retail book). Retail NPL ratio was 1.22% (+27 bps YTD). Preferential / floating rate split in housing book was 65% / 35%, with average floating housing rate at 7.28%. 97.5% of retail loans are secured with average LTV of 59.35%]*

---

## 14  |  Non-Interest Income, Fee Growth & Foreign Exchange (FX) Outlook

**[Head of Investor Relations – BIDV]**:
"Due to time constraints, we have time for two final questions. Could you please discuss the outlook for non-interest income, including net fee income and foreign exchange (FX) trading gains?"

**[Management Representative – BIDV]**:
"Thank you. In 9M26, BIDV's net fee and commission income reached 5,442 billion VND, up 5.5% YoY (with 3Q26 fee income up 7.2% YoY to 1,858 billion VND).

Traditional fee categories delivered strong growth—most notably, Trade Finance and Payments increased by 14.9% YoY to 2,576 billion VND. Furthermore, digital banking fees turned from a loss to a net profit of 82.9 billion VND (vs -6.5 billion VND in 9M25). Excluding treasury advisory, underlying net fee income grew 22.5% YoY.

Regarding foreign exchange (FX) trading: The banking industry is navigating compressed FX margins because central bank reference rates and commercial transaction rates have traded within very narrow bands, limiting arbitrage spreads. Nonetheless, customer-driven FX transaction volume remains strong, supported by robust import-export activity. As global trade conditions expand in 2027, BIDV's premier position in trade finance and corporate FX will capture meaningful fee volume.

Our strategic goal is to continually increase the proportion of net fee income to total operating income toward double digits, reinforcing our non-interest earnings pillar."

> *[Editorial Note: Reference Slide 15, 17, 18: 9M26 Non-interest income reached 16,947 billion VND (-0.5% YoY; 3Q26: 6,150 billion VND, +2.8% YoY). Net fee income reached 5,442 billion VND (+5.5% YoY; fee ratio 8.1% of TOI). Payments & Trade Finance reached 2,576 billion VND (+14.9% YoY). FX trading income reached 2,955 billion VND (-7.2% YoY). Other income (including loan recoveries) reached 7,789 billion VND (+16.8% YoY). Digital banking delivered 11,152 billion VND in net income (~17.3% of bank-wide net income)]*

---

## 15  |  Closing Remarks and Liquidity Equilibrium

**[Head of Investor Relations – BIDV]**:
"We have our final question: How do you expect the gap between credit growth and deposit growth to evolve in 2027—will it widen or narrow?"

**[Management Representative – BIDV]**:
"Thank you. As noted earlier, the liquidity gap between credit and deposit growth has narrowed significantly over recent months and will remain balanced through the remainder of 2026.

Heading into 2027, we expect this balanced equilibrium to persist. Corporate entities and retail depositors are increasingly recycling liquidity through the formal banking system. With deposit growth keeping pace with credit demand, the banking system will maintain stable funding conditions without recurring liquidity crunches.

On behalf of BIDV's Board of Management and Investor Relations team, we would like to sincerely thank all analysts, institutional investors, and fund managers for joining our earnings call today. We look forward to updating you on our progress in upcoming quarters. Thank you very much."

> *[Editorial Note: Reference Slide 21, 23, 25: BIDV Strategy to 2030 targets Asia Top 100 Bank status, annual asset growth >=8%, NPL <1.0% by 2030, and ROE >=15%. In 9M26, SmartBanking transacting users reached 10.6 million (+29% YoY), with 97.6% of retail transactions conducted on digital channels. AI applications generated 65.7 billion VND in revenue, with 54.17% of business units adopting AI]*
"""

def main():
    out_dir = PROJECT_ROOT / "workspace/Bank/BID/output"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    md_path = out_dir / "full_transcript.md"
    docx_path = out_dir / "full_transcript.docx"
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(TRANSCRIPT_MD)
    print(f"[✓] Đã tạo file Markdown Transcript: {md_path} ({len(TRANSCRIPT_MD)} bytes)")
    
    from scripts.document_formatter import DocumentFormatter
    DocumentFormatter.markdown_to_transcript_docx(str(md_path), str(docx_path))
    print(f"[✓] Đã biên dịch file DOCX Corporate Transcript: {docx_path} ({docx_path.stat().st_size / 1024:.1f} KB)")

if __name__ == "__main__":
    main()
