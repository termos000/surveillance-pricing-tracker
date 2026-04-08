---
date-created: "202602251430"
aliases:
  - "India surveillance pricing profile"
tags:
  - "#molecules"
  - "#jurisdiction-profile"
topic:
  - "[[surveillance pricing]]"
  - "[[India]]"
---

# India — Surveillance Pricing Regulatory Profile

*Jurisdiction molecule for [[surveillance-pricing-comparative-regulation|Paper 1]].*

India has no instrument that directly addresses surveillance pricing or algorithmic personalized pricing. What it has instead is a constellation of general-purpose consumer protection, competition, and data protection instruments — none designed for the problem, but several being stretched toward it. The most significant regulatory activity is enforcement-led rather than legislative: the CCPA's January 2025 notices to Uber and Ola for differential pricing based on operating systems, and the CCI's October 2025 market study warning that pricing algorithms can produce collusion without human intent. The instrument set is fragmented across multiple regulators (CCPA, CCI, IRDAI, RBI, Data Protection Board) with no coordinating mechanism, and the two proposed instruments that could most directly reach algorithmic pricing — the Draft Digital Competition Bill 2024 and the DPDP Rules 2025's algorithmic impact assessments — remain either unintroduced or newly operative. India's regulatory posture toward surveillance pricing is best described as reactive and enforcement-triggered: regulators are responding to specific consumer complaints (iPhone vs. Android fare disparities) rather than addressing the structural practice.

## Instruments

| Instrument | Strategy | Sector | Status | Enforcement |
|-----------|----------|--------|--------|-------------|
| Consumer Protection Act 2019, s. 2(47) (unfair trade practices) | Disclosure ([[disclosure-regulation]]) | General | Operative | CCPA; consumer commissions (District, State, National); penalties up to INR 10 lakh; imprisonment up to 2 years |
| Consumer Protection (E-Commerce) Rules 2020, Rules 4 and 6 | Disclosure | E-commerce (marketplace and inventory models) | Operative | CCPA; consumer commissions |
| CCPA Dark Patterns Guidelines 2023 (13 specified patterns) | Disclosure (guidelines) | E-commerce | Operative | CCPA; advisory-led; self-audit model; penalties up to INR 10 lakh (s. 21 CPA) |
| CCPA Enforcement — Uber/Ola Differential Pricing (Jan 2025) | Disclosure (enforcement) | Ride-hailing | Active (DG Investigation ongoing) | CCPA Investigation Wing; DG (Investigation) |
| Competition Act 2002 (as amended 2023), ss. 3 and 4 | Competition ([[competition-over-regulation]]) | General | Operative | CCI; penalties up to 10% of average turnover for preceding 3 years |
| CCI Market Study on AI and Competition (Oct 2025) | Self-regulation ([[self-regulation]]) (guidance) | General | Complete (study published) | Non-binding; self-audit framework recommended |
| Digital Personal Data Protection Act 2023 (DPDPA) | Rights & liabilities ([[rights-and-liabilities-regulation]]) (limited) | General | Enacted (rules notified Nov 2025; phased implementation) | Data Protection Board of India; penalties up to INR 250 crore |
| DPDP Rules 2025, Rule 13(3) — Algorithmic Impact Assessments for SDFs | Rights & liabilities (compliance obligation) | General (Significant Data Fiduciaries only) | Enacted (Nov 2025; implementation phased) | Data Protection Board of India |
| Draft Digital Competition Bill 2024 (SSDE obligations) | Competition (structural, ex ante) | Digital markets (Core Digital Services only) | Proposed (public consultation closed May 2024; not introduced in Parliament) | CCI (proposed); penalties up to 10% of global turnover |
| IRDAI Insurance Products Regulations 2024 | Disclosure (sector-specific) | Insurance | Operative | IRDAI; product governance and pricing principles |
| RBI Digital Lending Directions 2025 | Disclosure (sector-specific) | Digital lending | Operative (May 2025; phased) | RBI; Key Fact Statement requirements; neutrality obligations for multi-lender apps |
| India AI Governance Guidelines (Nov 2025) | Self-regulation (voluntary principles) | General | Published (non-binding) | None (voluntary; existing sector regulators apply) |

## Detail

### Consumer Protection Act 2019 — Unfair Trade Practices, s. 2(47)

Section 2(47) defines "unfair trade practice" as any trade practice that adopts an "unfair method or unfair or deceptive practice" for the purpose of promoting the sale of goods or provision of services. The definition is illustrative, not exhaustive: it lists specific categories (false representations about quality, grade, or standard; misleading warranties; price misrepresentation; false claims of sponsorship) but opens with the phrase "including any of the following practices, namely" — leaving room for interpretive expansion.

**Relevance to algorithmic pricing.** The Act does not mention algorithmic pricing, personalized pricing, dynamic pricing, or data-driven price differentiation. Its application to these practices depends on whether they can be characterized as "unfair or deceptive." A price that varies based on the consumer's device, browsing history, or willingness-to-pay profile could theoretically constitute a deceptive practice if the consumer is not informed that the price is personalized. This is the theory underlying the CCPA's Uber/Ola investigation. But the statutory text does not specifically require disclosure of pricing methodology, and no court or commission has ruled on whether algorithmic price personalization constitutes an unfair trade practice under s. 2(47).

**CCPA's enforcement powers.** The CCPA, established under s. 10 of the Act and operative since July 24, 2020, has the power to protect consumer rights "as a class" (s. 18), conduct investigations through its Director General (Investigation) wing, recall goods, withdraw services, discontinue unfair trade practices, and impose penalties. For misleading advertisements, penalties reach INR 10 lakh (first offence) and INR 50 lakh (subsequent offences) with imprisonment up to 2 or 5 years respectively (s. 21). For non-compliance with CCPA directions, penalties under s. 88 include imprisonment up to 6 months or fine up to INR 20 lakh.

**Primary**: [Consumer Protection Act, 2019 (indiacode.nic.in)](https://www.indiacode.nic.in/handle/123456789/15256?locale=en); [Section 2(47) text (Indian Kanoon)](https://indiankanoon.org/doc/117738049/)

**Secondary**: [Mondaq, "Consumer Protection Act 2019: Key Takeaways"](https://www.mondaq.com/india/dodd-frank-consumer-protection-act/1020458/consumer-protection-act-2019-key-takeaways); [Legal Service India, "E-Commerce and Consumer Rights under the Consumer Protection Act, 2019"](https://www.legalserviceindia.com/Legal-Articles/e-commerce-consumer-rights-under-the-consumer-protection-act-2019/)

### Consumer Protection (E-Commerce) Rules 2020 — Pricing Provisions

The E-Commerce Rules 2020, framed under s. 94 of the CPA 2019, impose specific duties on e-commerce entities (both marketplace and inventory models) that are relevant to pricing transparency.

**Rule 4 — Non-discrimination.** E-commerce entities must not "discriminate between consumers of the same class or mak[e] any arbitrary classification of consumers affecting their rights under the Act." This is the closest Indian regulatory provision to a prohibition on price discrimination. However, its operative scope is narrow: it prohibits "arbitrary classification" rather than data-driven price differentiation per se, and it is framed as a duty of the platform rather than a right of the consumer. Whether algorithmically determined price variations between consumers constitute "arbitrary classification" has not been tested.

**Rule 4 — Preferential treatment disclosure.** Marketplace entities must describe "any differential treatment" given to goods, services, or sellers of the same category, and must disclose the basis for preferential treatment, including sponsored listings and ranking criteria.

**Rule 6 — Price manipulation prohibition.** E-commerce entities must not "manipulate the price of the goods or services offered on its platform in such a manner as to gain unreasonable profit by imposing on consumers any unjustified price having regard to the prevailing market conditions." This provision targets exploitative pricing but requires proof of "unreasonable profit" and "unjustified price" relative to market conditions — a high threshold that is difficult to apply to personalized pricing, where the same product is offered at different (but individually "justified") prices to different consumers.

**Rule 4 — Total price disclosure.** Sellers must disclose "the total price in single figure of any goods or services offered for sale, along with a breakup price for the goods or services, showing all the compulsory and voluntary charges."

**Primary**: [Consumer Protection (E-Commerce) Rules, 2020 (ICSI text)](https://www.icsi.edu/media/webmodules/Consumer_Protection_E-Commerce_Rules_2020.pdf)

**Secondary**: [TeamLease RegTech, "E-Commerce Compliance in India"](https://www.teamleaseregtech.com/blogs/134/e-commerce-compliance-in-india-understanding-the-consumer-protection-e-commerce-rules-2020/); [S&R Law, "The E-Commerce Rules for 2020"](https://www.snrlaw.in/e-commerce-rules-2020/)

### CCPA Dark Patterns Guidelines 2023 (Nov 30, 2023)

The CCPA issued the "Guidelines for Prevention and Regulation of Dark Patterns, 2023" on November 30, 2023, identifying 13 specified dark patterns in e-commerce: false urgency, basket sneaking, confirm shaming, forced action, subscription trap, interface interference, bait and switch, drip pricing, disguised advertisements, nagging, trick question, SaaS billing, and rogue malware.

**Definition.** Dark patterns are defined as "deceptive patterns or practices deployed in the user interface or user experience (UI/UX) interactions that are designed to mislead or trick users into doing an action they did not originally intend to do."

**What the Guidelines cover.** The Guidelines are applicable to all platforms offering goods or services in India, to advertisers, and to sellers. Of the 13 listed patterns, drip pricing (gradually adding mandatory fees during checkout) and bait and switch (advertising one product/price and substituting another) are the most pricing-adjacent. The CCPA has enforced drip pricing violations — imposing a penalty of INR 7 lakh on Zepto in December 2025 for checkout-stage pricing practices that caused consumers to pay above MRP.

**What the Guidelines do NOT cover.** Personalized pricing is not among the 13 specified patterns. The Guidelines address manipulative interface design, not data-driven price differentiation. A platform that shows the same interface to all consumers but sets different prices based on personal data does not violate the dark patterns framework as currently drafted. This gap is significant: the most common manifestation of surveillance pricing (algorithmic personalization invisible in the UI) falls outside the Guidelines' scope.

**Enforcement trajectory.** In June 2025, the CCPA issued an advisory requiring e-commerce platforms to conduct self-audits to identify and eliminate dark patterns within three months. On May 28, 2025, formal notices were sent to eleven companies. By November 2025, 26 leading platforms submitted self-declaration letters confirming completion of audits. Despite this activity, compliance reviews identified drip pricing violations on 11 of 26 audited companies, including Flipkart, Myntra, Cleartrip, MakeMyTrip, BigBasket, Zomato, and Blinkit.

**Primary**: [CCPA Guidelines for Prevention and Regulation of Dark Patterns, 2023 (PIB)](https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1983994); [CCPA Advisory on Self-Audits (June 2025, PIB)](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2134765)

**Secondary**: [AZB Partners, "Regulatory Crackdown on Dark Patterns: CCPA's Enforcement Actions"](https://www.azbpartners.com/bank/regulatory-crackdown-on-dark-patterns-ccpas-enforcement-actions-and-emerging-compliance-landscape-in-indian-e-commerce/); [IAPP, "India's CCPA Guidelines on Dark Patterns: Welcome Signal, But Law Is Still Soft"](https://iapp.org/news/a/india-s-ccpa-guidelines-on-dark-patterns-welcome-signal-but-law-is-still-soft)

### CCPA Enforcement — Uber/Ola Differential Pricing (Jan–Mar 2025)

In December 2024, reports surfaced that ride-hailing platforms Uber and Ola were charging different fares for the same route depending on whether the consumer used an iPhone or an Android device. Indian entrepreneur Sudhir Kalra shared screenshots showing Uber fares of INR 290.79 on Android versus INR 342.47 on iPhone for the same route. Similar discrepancies of 15-20% were reported in Chennai. Reports also emerged of differential pricing on quick-commerce platforms (Zepto: capsicum at INR 107 on iPhone vs. INR 21 on Android for 500g).

**CCPA notices.** On January 23, 2025, Consumer Affairs Minister Pralhad Joshi announced that the CCPA had issued notices to Ola and Uber demanding clarification of their pricing algorithms and the factors influencing fare variations. Notices were also sent to Apple regarding potential role in enabling OS-based discrimination.

**Company response.** Both companies denied differential pricing. Uber stated: "We do not set prices based on a rider's phone manufacturer. We look forward to working with the Central Consumer Protection Authority to clear up any misunderstanding."

**Escalation to DG Investigation.** After both companies denied differential pricing, the matter was referred to the CCPA's Director General (Investigation) for a detailed investigation, as reported in March 2025 in a Lok Sabha response. The investigation is ongoing as of February 2026. No findings or orders have been issued.

**Significance.** This is the first regulatory action in India explicitly targeting algorithmic differential pricing. The trigger was consumer complaints about observable price differences (iPhone vs. Android), not the more opaque forms of personalized pricing based on behavioral profiling. The enforcement pathway is reactive — consumer complaint triggers CCPA notice, company denial triggers investigation — rather than systematic or proactive. The investigation's outcome will be a significant marker for India's regulatory posture: if the CCPA finds differential pricing and issues orders, it will establish that OS-based price differentiation constitutes an unfair trade practice under s. 2(47) of the CPA 2019.

**Primary**: [DDNews, "CCPA Issues Notices to Ola, Uber over Differential Pricing" (Jan 2025)](https://ddnews.gov.in/en/ccpa-issues-notices-to-ola-uber-over-differential-pricing-apple-also-under-scrutiny/); [Business Standard, "CCPA Notices Sent to Ola, Uber over Android-iOS Fare Differences" (Jan 2025)](https://www.business-standard.com/industry/news/ccpa-ola-uber-flipkart-differential-pricing-android-ios-users-prahlad-joshi-125012300757_1.html)

**Secondary**: [Medianama, "India Targets Differential Pricing — But Is It Missing the Big Picture?" (Jan 2025)](https://www.medianama.com/2025/01/223-views-algorithmic-pricing-ios-android-differential-pricing/); [Medianama, "Ola, Uber Deny Differential Pricing for iPhone Users, Govt Probes" (Mar 2025)](https://www.medianama.com/2025/03/223-ola-uber-deny-differential-pricing-for-iphone-users-as-govt-investigates/); [The Register, "India Investigates Whether Uber Makes iPhone Users Pay More" (Mar 2025)](https://www.theregister.com/2025/03/14/india_rideshare_differential_pricing_investigation/)

### Competition Act 2002 (as amended 2023) — ss. 3 and 4

The Competition Act 2002, as amended by the Competition (Amendment) Act 2023 (effective September 10, 2024), provides two channels relevant to algorithmic pricing.

**Section 3 — Anti-competitive agreements, including hub-and-spoke.** The 2023 amendment added a proviso to s. 3(3) explicitly recognizing hub-and-spoke arrangements. Entities that "participate or intend to participate in the furtherance of" anti-competitive agreements are now liable even if they are not direct competitors. This captures a scenario central to algorithmic collusion: a platform or pricing software provider acting as the "hub" that coordinates pricing among competing "spoke" sellers. The amendment closes an earlier gap where only direct agreements among competitors were clearly captured. A platform that provides dashboards suggesting "recommended prices," imposes most-favored-nation clauses, or facilitates cross-seller communication may now be treated as a hub enabling cartel conduct.

**Section 4 — Abuse of dominant position.** Algorithmic personalized pricing by a dominant firm could constitute an exploitative abuse under s. 4(2)(a)(ii) (imposing unfair or discriminatory conditions or prices). However, the CCI has been conservative in finding dominance in two-sided platform markets. In the Uber/Ola surge pricing cases (Cases 96/2015, 37/2018, and Samir Agrawal v. CCI), the CCI dismissed allegations of abuse, finding that Ola and Uber impose "significant competitive constraint" on each other and therefore neither is dominant. The Supreme Court upheld an investigation order against Uber but the CCI ultimately found no abuse. On surge pricing specifically, Ola argued its algorithm was "complex, taking into account various factors such as time, distance, weather, and availability of cabs, making it impossible for prices to be fixed artificially" — an argument the CCI accepted in dismissing the information.

**No enforcement action on algorithmic pricing or collusion.** As of February 2026, the CCI has not brought any competition enforcement action specifically targeting algorithmic pricing or algorithmic collusion.

**Primary**: [Competition Act, 2002 (cci.gov.in)](https://www.cci.gov.in/legal-framwork/act); [CCI Case No. 96 of 2015 (Meru v. Uber)](https://www.cci.gov.in/images/antitrustorder/en/9620151652247696.pdf)

**Secondary**: [Kluwer Competition Law Blog, "Supreme Court of India Upholds Investigation against Uber"](https://legalblogs.wolterskluwer.com/competition-blog/supreme-court-of-india-upholds-investigation-against-uber/); [AZB Partners, "Pricing Algorithms: CCI's First Major Encounter with Assessing New-Age Collusions"](https://www.azbpartners.com/bank/pricing-algorithms-ccis-first-major-encounter-with-assessing-new-age-collusions/); [Kluwer Competition Law Blog, "2023 Amendments to Indian Competition Law: Bringing Down The Hammer on Anti-Competitive Conduct (Part 2)"](https://competitionlawblog.kluwercompetitionlaw.com/2023/05/04/2023-amendments-to-indian-competition-law-bringing-down-the-hammer-on-anti-competitive-conduct-part-2/)

### CCI Market Study on AI and Competition (Oct 2025)

On October 6, 2025, the CCI released its Market Study on Artificial Intelligence and Competition — India's first comprehensive analysis of how AI affects market structures and competitive behavior. The study was conducted with the Management Development Institute, Gurgaon (MDI), based on secondary data, stakeholder surveys (106 entities), and focused group discussions.

**Pricing algorithms.** The study identifies four categories of pricing algorithms that raise competition concerns: monitoring algorithms (tracking competitor prices), hub-and-spoke algorithms (coordinating through shared service providers), signaling algorithms (responding dynamically to rivals' pricing), and self-learning algorithms (using reinforcement learning to maximize profits). The CCI warns that "widespread use of algorithmic software could cause collusion in markets previously not susceptible to it" and that algorithmic tools "make collusion more stable and rewarding."

**Personalized pricing.** The study acknowledges that "AI-driven dynamic pricing allows firms to offer different prices to different consumers based on behavioural or demographic data" and that such personalized pricing "risks consumer harm when used to exploit vulnerable users or suppress price transparency."

**Self-audit recommendation.** The study's most tangible output is a proposed self-audit framework: enterprises should document AI-based decision-making processes, conduct periodic reviews of algorithmic outputs to detect inadvertent collusion, and review AI-driven pricing strategies to detect unintended discriminatory practices. The framework is non-binding — guidance, not regulation.

**Significance.** The CCI market study parallels the UK CMA's 2018 working paper on pricing algorithms — analytical recognition of risks without enforcement action. The self-audit recommendation places the study in the [[self-regulation]] category on the topology: the CCI is asking firms to monitor themselves rather than imposing state-administered obligations.

**Primary**: [CCI, "Market Study on Artificial Intelligence and Competition" (Oct 2025)](https://www.cci.gov.in/images/marketstudie/en/market-study-on-artificial-intelligence-and-competition1759752172.pdf); [CCI Market Studies page](https://www.cci.gov.in/economics-research/market-studies/details/45/0)

**Secondary**: [Medianama, "AI Algorithms Can Cause Price Collusion Without Intent, Says CCI" (Oct 2025)](https://www.medianama.com/2025/10/223-ai-algorithms-price-collusion-human-intent-cci/); [K&S Partners, "CCI's Market Study and the Architecture of Digital Competition"](https://ksandk.com/competition/cci-issues-landmark-study-on-ai-and-competition/); [Mondaq, "Artificial Intelligence and Competition Law: CCI's Analysis"](https://www.mondaq.com/india/antitrust-eu-competition/1690052/artificial-intelligence-and-competition-law-ccis-analysis-of-the-market-study-on-ai-and-competition-report)

### Digital Personal Data Protection Act 2023 (DPDPA) and DPDP Rules 2025

The DPDPA received Presidential assent on August 11, 2023. The implementing rules — the Digital Personal Data Protection Rules, 2025 — were notified on November 14, 2025, marking the full operationalization of the Act.

**No right to opt out of automated decision-making.** Unlike GDPR Article 22, which provides a right not to be subject to solely automated decisions producing legal or significant effects, the DPDPA contains no equivalent right. Data principals have rights of access, correction, erasure, and grievance redressal, but not a right to object to automated processing or a right to human intervention in automated decisions. This is a deliberate design choice: the DPDPA follows a consent-and-purpose-limitation model rather than a rights-against-processing model. For algorithmic pricing, this means Indian consumers have no statutory right to challenge a price set by an automated system, contest the logic of an algorithmic pricing decision, or demand human review of an algorithmically determined price.

**Accuracy obligation.** The DPDPA requires data fiduciaries to ensure the "completeness, accuracy and consistency" of personal data when it is "likely to be used to make a decision that affects" the data principal (s. 8). This is an accuracy-of-inputs obligation, not a fairness-of-outputs obligation. It requires that the data feeding into a pricing algorithm be accurate, but does not address whether the algorithmic output (the personalized price) is fair, non-discriminatory, or transparent.

**Rule 13(3) — Algorithmic Impact Assessments for Significant Data Fiduciaries.** The DPDP Rules 2025 impose enhanced obligations on Significant Data Fiduciaries (SDFs) — entities designated by the government based on volume and sensitivity of data processed. SDFs must conduct algorithmic impact assessments examining fairness, transparency, accuracy, and rights implications of AI/ML systems used for processing personal data. This obligation applies when personal data is used in automated decision-making, profiling, or algorithmic systems. SDFs must embed these assessments into product development lifecycles and conduct annual Data Protection Impact Assessments and audits.

**Significance.** Rule 13(3)'s algorithmic impact assessments are the closest Indian instrument to a regulatory obligation that reaches algorithmic pricing. But the obligation has three significant limitations: (1) it applies only to SDFs, not all data fiduciaries — smaller platforms may escape; (2) it is a process obligation (conduct an assessment) rather than a substantive obligation (do not discriminate); and (3) it has not been tested in enforcement. The SDF designation process itself was still emerging as of February 2026.

**Primary**: [DPDPA 2023 full text (MeitY)](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf); [DPDP Rules 2025 notification (PIB)](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190655)

**Secondary**: [Future of Privacy Forum, "The Digital Personal Data Protection Act of India, Explained"](https://fpf.org/blog/the-digital-personal-data-protection-act-of-india-explained/); [India-Briefing, "DPDP Rules 2025: India Notifies Digital Privacy Law"](https://www.india-briefing.com/news/dpdp-rules-2025-india-data-protection-law-compliance-40769.html/); [EY, "DPDP Rules 2025 Notified by MeitY: Complete Guide"](https://www.ey.com/en_in/insights/cybersecurity/transforming-data-privacy-digital-personal-data-protection-rules-2025)

### Draft Digital Competition Bill 2024 (Proposed)

On March 12, 2024, the Ministry of Corporate Affairs released a draft report of the Committee on Digital Competition Law along with a Draft Digital Competition Bill 2024 for public consultation (consultation period: March 12 to May 15, 2024). The bill proposes an ex ante regulatory framework modeled on the EU's Digital Markets Act.

**Systematically Significant Digital Enterprises (SSDEs).** The bill introduces quantitative and qualitative criteria for identifying SSDEs offering "Core Digital Services" (online search, social networking, video-sharing, communications, operating systems, browsers, cloud services, advertising, and online intermediation). Quantitative thresholds include India turnover of at least INR 4,000 crore (approximately USD 480 million), global turnover of at least USD 30 billion, India GMV of at least INR 16,000 crore, or global market capitalization of at least USD 75 billion.

**Relevant obligations.** SSDEs are prohibited from: self-preferencing their own products over third-party offerings (s. 9(1)(a)); restricting business users from communicating offers to end users or directing them to third-party services (anti-steering, s. 9); and data misuse across services. Compliance with self-preferencing prohibitions mandates "a complete audit and, likely, a redesign of algorithmic decision-making to ensure neutral and transparent ranking, steering, and display processes."

**No direct pricing provision.** The bill does not include a provision specifically addressing personalized pricing, dynamic pricing, or algorithmic price discrimination. Its relevance to surveillance pricing is indirect: by restricting data sharing within SSDE ecosystems and requiring algorithmic neutrality in ranking and display, the bill constrains some of the data infrastructure that enables personalized pricing on designated platforms.

**Status.** The bill has not been introduced in Parliament. Inter-ministerial consultations were ongoing as of early 2025, with parliamentary introduction anticipated later in 2025. Given India's legislative calendar, enactment remains uncertain.

**Primary**: [Draft Digital Competition Bill, 2024 (Medianama hosted text)](https://www.medianama.com/wp-content/uploads/2024/03/DRAFT-DIGITAL-COMPETITION-BILL-2024.pdf); [PRS India, "Report of the Committee on Digital Competition Law"](https://prsindia.org/policy/report-summaries/digital-competition-law)

**Secondary**: [GW Competition & Innovation Lab, "Overview of India's Digital Competition Bill, 2024"](https://competitionlab.gwu.edu/overview-indias-digital-competition-bill-2024); [Mondaq, "The Draft Digital Competition Bill 2024 & Challenges for Big-Tech"](https://www.mondaq.com/india/antitrust-eu-competition/1575982/the-draft-digital-competition-bill-2024-challenges-for-big-tech); [ITIF, "India's Digital Competition Bill" (policy brief)](https://www2.itif.org/2024-india-digital-competition-bill.pdf)

### IRDAI Insurance Products Regulations 2024 (Sector-Specific)

The Insurance Regulatory and Development Authority of India (IRDAI) replaced 37 existing regulations with 7 consolidated regulations in 2024, including the IRDAI (Insurance Products) Regulations 2024 (effective April 1, 2024).

**Pricing governance.** The regulations mandate that insurers establish a Board-approved Product Management Committee and pricing policies that consider evolving risk coverage needs and ensure transparency. IRDAI has moved toward a "Use and File" system enabling insurers to introduce new products without prior regulatory approval, accelerating innovation cycles including telematics-based and usage-based insurance models (pay-as-you-drive, pay-how-you-drive).

**Algorithmic underwriting.** IRDAI has requested greater disclosure regarding algorithmic underwriting and has indicated that model documentation and Algorithmic Impact Assessments may be required to ensure transparency in claims decisions. Indian motor insurers are shifting toward behavior-based pricing using telematics data — a form of algorithmic pricing that personalizes premiums based on driving behavior.

**No price walking ban or equivalent.** Unlike the UK's FCA, which banned price walking in home and motor insurance (PS21/5, eff. Jan 2022), IRDAI has not imposed any prohibition on tenure-based or behavioral price discrimination. The regulatory posture is facilitative — encouraging algorithmic pricing innovation rather than constraining it.

**Primary**: [IRDAI (Insurance Products) Regulations, 2024 (IRDAI)](https://irdai.gov.in/consolidated-gazette-notified-regulations)

**Secondary**: [Mondaq, "IRDAI (Insurance Products) Regulations, 2024"](https://www.mondaq.com/india/insurance-laws-and-products/1512658/irdai-insurance-products-regulations-2024); [Insurance Business Magazine, "India Motor Insurance Carriers Shift to Behaviour-Based Pricing"](https://www.insurancebusinessmag.com/asia/news/auto-motor/india-motor-insurance-carriers-shift-to-behaviourbased-pricing-557327.aspx)

### RBI Digital Lending Directions 2025 (Sector-Specific)

The Reserve Bank of India issued the Digital Lending Directions 2025 on May 8, 2025, updating the regulatory framework for digital lending.

**Pricing transparency.** Regulated entities must issue a digitally signed Key Fact Statement (KFS) showing the Annual Percentage Rate, all fees, and a minimum cooling-off window. This is a disclosure obligation targeting lending pricing opacity, not algorithmic personalization.

**Algorithmic neutrality.** Fintechs operating multi-lender Digital Lending Apps face new neutrality requirements: unbiased offer display, consistent matching logic, mandatory listing of unmatched lenders, and a ban on dark patterns. This is the only Indian regulatory provision that explicitly requires algorithmic neutrality in a pricing-adjacent context — though it applies to loan offer display rather than consumer product pricing.

**Primary**: [RBI, Digital Lending Directions 2025](https://rbidocs.rbi.org.in/rdocs/notification/PDFs/GUIDELINESDIGITALLENDINGD5C35A71D8124A0E92AEB940A7D25BB3.PDF)

**Secondary**: [Synergia Legal, "An Overview of the RBI's Digital Lending Directions, 2025"](https://synergialegal.com/an-overview-of-the-rbis-digital-lending-direction-2025/); [Legal 500, "Reserve Bank of India (Digital Lending) Directions, 2025"](https://www.legal500.com/developments/thought-leadership/reserve-bank-of-india-digital-lending-directions-2025-brief-overview-analysis/)

### India AI Governance Guidelines (Nov 2025)

Released by the Ministry of Electronics & Information Technology (MeitY) in November 2025, the India AI Governance Guidelines establish seven foundational principles (the "Seven Sutras"): trust, people first, fairness and equity, accountability, understandability by design, safety and resilience, and sustainability.

**Non-binding.** The guidelines are voluntary — "a foundational reference for responsible AI adoption," not enforceable law. They recommend that industry adopt voluntary frameworks, publish transparency reports, provide grievance redressal mechanisms, and mitigate risks with "techno-legal solutions." They propose establishing an AI Governance Group and an AI Safety Institute. They recommend developing "an India-specific risk assessment framework that reflects real-world evidence of harm."

**Relevance to algorithmic pricing.** The guidelines address algorithmic transparency, fairness, and risk classification in general terms but do not specifically address pricing. For surveillance pricing, the guidelines occupy the lightest possible position on the topology — voluntary principles without enforcement, paralleling the UK's 2023 pro-innovation AI White Paper.

**Primary**: [India AI Governance Guidelines (Nov 2025, PIB hosted)](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc2025115685601.pdf)

**Secondary**: [IndiaAI, "India AI Governance Guidelines: Empowering Ethical and Responsible AI"](https://indiaai.gov.in/article/india-ai-governance-guidelines-empowering-ethical-and-responsible-ai); [Carnegie Endowment, "India's Advance on AI Regulation" (Nov 2024)](https://carnegieendowment.org/research/2024/11/indias-advance-on-ai-regulation?lang=en)

## Analysis

**Hierarchy.** No single strategy dominates. The operative instruments are consumer protection provisions (CPA 2019, E-Commerce Rules 2020, Dark Patterns Guidelines 2023) that function as [[disclosure-regulation]] — requiring transparency about pricing without prohibiting any specific pricing practice. Competition instruments (Competition Act 2002 as amended, CCI market study) exist but have not been deployed against algorithmic pricing. Data protection instruments (DPDPA, DPDP Rules 2025) provide process obligations (algorithmic impact assessments for SDFs) but no substantive rights against automated pricing decisions. The proposed Digital Competition Bill would add structural competition obligations but remains unintroduced. The hierarchy, if one exists, is disclosure first — but disclosure of a narrow kind: total price transparency and non-discrimination within same-class consumers, not disclosure of algorithmic methodology or data-driven personalization.

**Design logic.** Accumulated. India's instrument set for surveillance pricing was not designed as a coherent response to algorithmic pricing. It accumulated from different legislative and regulatory moments with different purposes: the CPA 2019 modernized 1986-era consumer protection law; the E-Commerce Rules 2020 responded to the growth of marketplace platforms; the Dark Patterns Guidelines 2023 responded to global momentum on deceptive design; the Competition Amendment 2023 modernized cartel law for digital markets; the DPDPA 2023 established India's first comprehensive data protection framework. None was designed with surveillance pricing as its target. The result is a set of instruments that each partially touches the problem — price transparency here, non-discrimination there, algorithmic fairness obligations elsewhere — without any instrument squarely addressing the practice of using personal data to set individualized prices.

**Institutional fragmentation.** The instruments are distributed across multiple regulators with no coordination mechanism: the CCPA (consumer protection), the CCI (competition), the Data Protection Board of India (data protection), IRDAI (insurance), and the RBI (lending). Each operates within its statutory mandate. The CCPA investigates Uber/Ola's differential pricing as an unfair trade practice; the CCI studies algorithmic collusion as a competition concern; the DPDP Rules require algorithmic impact assessments as a data protection obligation. No regulator has a mandate that spans all three dimensions — consumer protection, competition, and data protection — as they apply to algorithmic pricing. This is not unique to India (the UK's distributed regulatory architecture shows similar institutional separation), but India lacks an equivalent to the UK's CMA, which holds both competition and consumer protection powers in the same institution.

**Institution relied on — divergence from theory.** Two notable divergences. First, the DPDP Rules 2025's algorithmic impact assessment obligation for SDFs is formally a rights-based instrument (protecting data principals), but operationally relies on the state-designated SDF category and process compliance (conduct assessments, file reports) rather than on individual data principals exercising rights against automated decisions. The DPDPA provides no individual right to challenge an algorithmic pricing decision — the enforcement pathway runs through the Data Protection Board, not through individual action. This is a rights instrument that functions through state administration.

Second, the CCI's market study recommends self-regulation (self-audits by firms), but the CCI itself holds enforcement powers under the Competition Act — it could investigate algorithmic pricing under s. 3 (hub-and-spoke) or s. 4 (abuse of dominance) but has chosen guidance over enforcement. The self-regulation recommendation is a deliberate institutional choice to defer enforcement, not a reflection of limited powers. Whether this represents strategic patience or regulatory hesitancy is an open question.

## Evidence

**CCPA Uber/Ola investigation — ongoing, no findings.** The CCPA's January 2025 notices to Uber and Ola for OS-based differential pricing were referred to the DG (Investigation) after both companies denied the practice. No findings, orders, or penalties have been issued as of February 2026. The investigation's outcome is unknown. [Business Standard (Jan 2025)](https://www.business-standard.com/industry/news/ccpa-ola-uber-flipkart-differential-pricing-android-ios-users-prahlad-joshi-125012300757_1.html); [Medianama (Mar 2025)](https://www.medianama.com/2025/03/223-ola-uber-deny-differential-pricing-for-iphone-users-as-govt-investigates/)

**Dark patterns enforcement — limited penalties, ongoing compliance gaps.** The CCPA has imposed penalties on specific companies for dark pattern violations: INR 7 lakh on Zepto (Dec 2025) for drip pricing and basket sneaking. 26 platforms completed self-audits, but drip pricing was identified on 11 of 26 companies. No dark pattern enforcement action has addressed personalized or algorithmic pricing. [Medianama, "Zepto Fined Rs 7 Lakh for Dark Patterns" (Dec 2025)](https://www.medianama.com/2025/12/223-zepto-fined-7-lakh-dark-patterns-ahead-ipo/)

**CCI — no enforcement action on algorithmic pricing or collusion.** The CCI dismissed the Uber/Ola surge pricing complaints (Cases 96/2015, 37/2018) on the ground that neither firm was dominant. No competition enforcement action targeting algorithmic collusion has been brought. The October 2025 market study acknowledged the risks but recommended self-audits rather than enforcement. [CCI Case No. 96 of 2015](https://www.cci.gov.in/images/antitrustorder/en/9620151652247696.pdf); [CCI Market Study (Oct 2025)](https://www.cci.gov.in/images/marketstudie/en/market-study-on-artificial-intelligence-and-competition1759752172.pdf)

**DPDP Rules 2025 — no enforcement data.** The Rules were notified in November 2025 with phased implementation. No Significant Data Fiduciaries have been designated, no algorithmic impact assessments have been filed, and no enforcement actions under the Rules have been reported as of February 2026. The instrument is too new for implementation evidence.

**Consumer complaint data — differential pricing widespread.** Viral reports, journalistic investigations, and consumer complaints document differential pricing across multiple platforms: Uber, Ola, Zepto, Flipkart (iPhone vs. Android); Uber (battery level correlated with surge acceptance, per Keith Chen's 2016 admission and Rishabh Singh's 2025 replication showing 8-12% fare increases when batteries dip below 20%). This consumer-facing evidence drives regulatory attention but does not constitute systematic measurement. [BusinessToday (Jan 2025)](https://www.businesstoday.in/technology/news/story/delhi-mans-experiments-reveal-ubers-pricing-algorithm-disparities-461386-2025-01-20)

## Movement

India's trajectory is recent and enforcement-triggered rather than legislative.

1. **August 2019**: Consumer Protection Act 2019 enacted — modernizes 1986 law; introduces CCPA; broadens unfair trade practice definition
2. **July 2020**: CCPA becomes operative
3. **July 2020**: Consumer Protection (E-Commerce) Rules 2020 notified — total price disclosure, non-discrimination, price manipulation prohibition
4. **2015–2018**: CCI dismisses Uber/Ola surge pricing complaints — no dominance found, no abuse examined
5. **April 2023**: Competition (Amendment) Act 2023 enacted — hub-and-spoke cartel recognition; facilitator liability under s. 3(3)
6. **August 2023**: DPDPA 2023 receives Presidential assent — no right to opt out of automated decision-making
7. **November 2023**: CCPA Dark Patterns Guidelines — 13 specified patterns; personalized pricing not among them
8. **March 2024**: Draft Digital Competition Bill released for consultation — ex ante framework for SSDEs; not introduced in Parliament
9. **April 2024**: IRDAI Insurance Products Regulations 2024 — facilitative approach to algorithmic pricing in insurance
10. **September 2024**: Competition Amendment Act 2023 takes effect
11. **December 2024**: Consumer complaints about Uber/Ola OS-based differential pricing go viral
12. **January 2025**: CCPA issues notices to Uber, Ola, and Apple — first Indian regulatory action targeting algorithmic differential pricing
13. **March 2025**: Investigation escalated to DG (Investigation) after company denials
14. **May 2025**: RBI Digital Lending Directions 2025 — algorithmic neutrality for multi-lender apps
15. **June 2025**: CCPA advisory requiring e-commerce self-audits for dark patterns within 3 months
16. **October 2025**: CCI publishes Market Study on AI and Competition — identifies algorithmic pricing risks; recommends self-audits
17. **November 2025**: DPDP Rules 2025 notified — algorithmic impact assessments for SDFs; 26 platforms complete dark pattern self-audits
18. **November 2025**: India AI Governance Guidelines published (non-binding)
19. **December 2025**: CCPA fines Zepto INR 7 lakh for dark patterns (drip pricing)

The trajectory shows India moving from general-purpose consumer protection and competition law toward recognition of algorithmic pricing as a distinct regulatory concern — but only reaching that recognition in 2025, and only through enforcement activity rather than legislation. There is no legislative instrument in India that specifically addresses surveillance pricing. The movement is from below: consumer complaints surface the problem, regulators respond with investigation and guidance, and legislative proposals (the Digital Competition Bill) remain unintroduced. India is approximately where the UK was in 2018 (analytical recognition through market studies) combined with enforcement-led discovery of specific practices (analogous to but earlier-stage than the CMA's November 2025 enforcement sweep).

## Open Questions

1. **Will the CCPA's Uber/Ola investigation produce a finding?** If the DG (Investigation) finds that OS-based differential pricing constitutes an unfair trade practice under s. 2(47), it would establish the first Indian regulatory precedent that algorithmic price differentiation based on device data violates consumer protection law. If the investigation finds no violation, it may signal that the existing legal framework cannot reach this practice without legislative amendment.
2. **Will the Digital Competition Bill be introduced?** The bill has been in consultation since March 2024 with parliamentary introduction anticipated in 2025. Its enactment would add an ex ante structural competition instrument for digital markets. Its non-enactment would leave India relying solely on the CCI's ex post enforcement powers, which commentators have described as "ill-suited to cope with the challenges of algorithmic pricing and platform-based collusion."
3. **Will SDFs be designated under the DPDP Rules 2025?** The algorithmic impact assessment obligation (Rule 13(3)) applies only to designated Significant Data Fiduciaries. Until SDFs are designated, the obligation is inoperative. Which firms will be designated, and whether the assessment obligation will be applied to pricing algorithms, remains unknown.
4. **Will the CCI move from market study to enforcement?** The October 2025 market study identified algorithmic collusion risks and recommended self-audits. Will the CCI open investigations, or will the self-audit recommendation remain the ceiling of its engagement with algorithmic pricing — as the UK CMA's 2018 working paper was for seven years?
5. **IRDAI — facilitative or regulatory?** IRDAI is encouraging telematics-based algorithmic insurance pricing. Will it introduce constraints (algorithmic transparency requirements, non-discrimination obligations) as the practice scales, or will the facilitative posture persist?
6. **Scope of consumer complaint-driven enforcement.** The Uber/Ola investigation was triggered by consumer complaints about visible price differences (iPhone vs. Android). What about personalized pricing that is not visibly tied to device type — pricing based on behavioral profiles, browsing history, or location data? The complaint-driven model may systematically miss the less observable forms of algorithmic pricing.
7. **E-Commerce Rules 2020 — "arbitrary classification" untested.** Rule 4's prohibition on discriminating between consumers of the same class or making "arbitrary classification" has not been applied to algorithmic pricing. Whether algorithmically segmented pricing constitutes "arbitrary classification" is an unresolved interpretive question.
8. **RBI algorithmic neutrality — model for other sectors?** The RBI's 2025 requirement of algorithmic neutrality for multi-lender digital lending apps is the most specific Indian regulatory obligation for algorithmic fairness in a pricing-adjacent context. Could this serve as a model for CCPA or sector regulators in other domains?

## Sources

**Primary**:
- [Consumer Protection Act, 2019 (indiacode.nic.in)](https://www.indiacode.nic.in/handle/123456789/15256?locale=en)
- [Consumer Protection (E-Commerce) Rules, 2020 (ICSI text)](https://www.icsi.edu/media/webmodules/Consumer_Protection_E-Commerce_Rules_2020.pdf)
- [CCPA Guidelines for Prevention and Regulation of Dark Patterns, 2023 (PIB)](https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1983994)
- [Competition Act, 2002 (cci.gov.in)](https://www.cci.gov.in/legal-framwork/act)
- [Competition (Amendment) Act, 2023 (cci.gov.in)](https://www.cci.gov.in/legal-framwork/act)
- [CCI, "Market Study on Artificial Intelligence and Competition" (Oct 2025)](https://www.cci.gov.in/images/marketstudie/en/market-study-on-artificial-intelligence-and-competition1759752172.pdf)
- [Digital Personal Data Protection Act, 2023 (MeitY)](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf)
- [DPDP Rules, 2025 notification (PIB)](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190655)
- [Draft Digital Competition Bill, 2024 (Medianama hosted text)](https://www.medianama.com/wp-content/uploads/2024/03/DRAFT-DIGITAL-COMPETITION-BILL-2024.pdf)
- [IRDAI (Insurance Products) Regulations, 2024 (IRDAI)](https://irdai.gov.in/consolidated-gazette-notified-regulations)
- [RBI Digital Lending Directions, 2025](https://rbidocs.rbi.org.in/rdocs/notification/PDFs/GUIDELINESDIGITALLENDINGD5C35A71D8124A0E92AEB940A7D25BB3.PDF)
- [India AI Governance Guidelines (Nov 2025, PIB)](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc2025115685601.pdf)
- [CCI Case No. 96 of 2015 (Meru v. Uber)](https://www.cci.gov.in/images/antitrustorder/en/9620151652247696.pdf)
- [CCPA Advisory on Self-Audits (June 2025, PIB)](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2134765)
- [PRS India, "Report of the Committee on Digital Competition Law"](https://prsindia.org/policy/report-summaries/digital-competition-law)

**Secondary**:
- [Medianama, "India Targets Differential Pricing — But Is It Missing the Big Picture?" (Jan 2025)](https://www.medianama.com/2025/01/223-views-algorithmic-pricing-ios-android-differential-pricing/)
- [Medianama, "Ola, Uber Deny Differential Pricing for iPhone Users, Govt Probes" (Mar 2025)](https://www.medianama.com/2025/03/223-ola-uber-deny-differential-pricing-for-iphone-users-as-govt-investigates/)
- [Medianama, "AI Algorithms Can Cause Price Collusion Without Intent, Says CCI" (Oct 2025)](https://www.medianama.com/2025/10/223-ai-algorithms-price-collusion-human-intent-cci/)
- [Medianama, "Zepto Fined Rs 7 Lakh for Dark Patterns" (Dec 2025)](https://www.medianama.com/2025/12/223-zepto-fined-7-lakh-dark-patterns-ahead-ipo/)
- [Business Standard, "CCPA Notices Sent to Ola, Uber" (Jan 2025)](https://www.business-standard.com/industry/news/ccpa-ola-uber-flipkart-differential-pricing-android-ios-users-prahlad-joshi-125012300757_1.html)
- [The Register, "India Investigates Whether Uber Makes iPhone Users Pay More" (Mar 2025)](https://www.theregister.com/2025/03/14/india_rideshare_differential_pricing_investigation/)
- [AZB Partners, "Pricing Algorithms: CCI's First Major Encounter with Assessing New-Age Collusions"](https://www.azbpartners.com/bank/pricing-algorithms-ccis-first-major-encounter-with-assessing-new-age-collusions/)
- [AZB Partners, "Regulatory Crackdown on Dark Patterns"](https://www.azbpartners.com/bank/regulatory-crackdown-on-dark-patterns-ccpas-enforcement-actions-and-emerging-compliance-landscape-in-indian-e-commerce/)
- [IAPP, "India's CCPA Guidelines on Dark Patterns: Welcome Signal, But Law Is Still Soft"](https://iapp.org/news/a/india-s-ccpa-guidelines-on-dark-patterns-welcome-signal-but-law-is-still-soft)
- [K&S Partners, "CCI's Market Study and the Architecture of Digital Competition"](https://ksandk.com/competition/cci-issues-landmark-study-on-ai-and-competition/)
- [Kluwer Competition Law Blog, "Supreme Court of India Upholds Investigation against Uber"](https://legalblogs.wolterskluwer.com/competition-blog/supreme-court-of-india-upholds-investigation-against-uber/)
- [Kluwer Competition Law Blog, "2023 Amendments: Bringing Down The Hammer (Part 2)"](https://competitionlawblog.kluwercompetitionlaw.com/2023/05/04/2023-amendments-to-indian-competition-law-bringing-down-the-hammer-on-anti-competitive-conduct-part-2/)
- [GW Competition & Innovation Lab, "Overview of India's Digital Competition Bill, 2024"](https://competitionlab.gwu.edu/overview-indias-digital-competition-bill-2024)
- [Mondaq, "The Draft Digital Competition Bill 2024 & Challenges for Big-Tech"](https://www.mondaq.com/india/antitrust-eu-competition/1575982/the-draft-digital-competition-bill-2024-challenges-for-big-tech)
- [Mondaq, "Consumer Protection Act 2019: Key Takeaways"](https://www.mondaq.com/india/dodd-frank-consumer-protection-act/1020458/consumer-protection-act-2019-key-takeaways)
- [Future of Privacy Forum, "The DPDP Act of India, Explained"](https://fpf.org/blog/the-digital-personal-data-protection-act-of-india-explained/)
- [India-Briefing, "DPDP Rules 2025"](https://www.india-briefing.com/news/dpdp-rules-2025-india-data-protection-law-compliance-40769.html/)
- [Carnegie Endowment, "India's Advance on AI Regulation"](https://carnegieendowment.org/research/2024/11/indias-advance-on-ai-regulation?lang=en)
- [Insurance Business Magazine, "India Motor Insurance Carriers Shift to Behaviour-Based Pricing"](https://www.insurancebusinessmag.com/asia/news/auto-motor/india-motor-insurance-carriers-shift-to-behaviourbased-pricing-557327.aspx)
- [Synergia Legal, "Overview of the RBI's Digital Lending Directions, 2025"](https://synergialegal.com/an-overview-of-the-rbis-digital-lending-direction-2025/)

**Library**:
- [[intel-comparative-regulation]]
- [[surveillance-pricing-comparative-regulation]]
- [[baldwin-regulatory-strategies]]
- [[disclosure-regulation]]
- [[command-and-control]]
- [[competition-over-regulation]]
- [[rights-and-liabilities-regulation]]
- [[self-regulation]]
- [[regulatory-topology-not-ladder]]
- [[government-capacities-regulation]]
- [[creative-compliance]]
- [[algorithmic-coordination]]
- [[algorithmic-agnosticism-wtp]]
- [[market-power-precondition-algorithmic-harm]]
- [[sp-uk]]
- [[sp-eu]]
- [[sp-china]]
- [[sp-new-york]]
