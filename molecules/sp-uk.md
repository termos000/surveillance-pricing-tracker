---
date-created: "202602250030"
aliases:
  - "UK surveillance pricing profile"
tags:
  - "#molecules"
  - "#jurisdiction-profile"
topic:
  - "[[surveillance pricing]]"
  - "[[United Kingdom]]"
---

# United Kingdom — Surveillance Pricing Regulatory Profile

*Jurisdiction molecule for [[surveillance-pricing-comparative-regulation|Paper 1]].*

The UK occupies a distinctive position on the topology: the only jurisdiction to have enacted a sector-specific prohibition on algorithmic price discrimination (the FCA price walking ban in home and motor insurance, operative since January 2022), while relying on disclosure-adjacent enforcement and competition powers for general commerce. The instrument set is institutionally concentrated — the CMA and FCA together hold the enforcement architecture — and is reinforced by the DMCCA 2024, which gave the CMA direct consumer enforcement powers (effective April 2025) that it is already deploying against pricing practices. Post-Brexit regulatory divergence from the EU is emerging: the Data (Use and Access) Act 2025 loosens the UK GDPR's automated decision-making restrictions, moving away from the EU's rights-based approach toward a lighter-touch framework that facilitates rather than constrains algorithmic pricing.

## Instruments

| Instrument | Strategy | Sector | Status | Enforcement |
|-----------|----------|--------|--------|-------------|
| DMCCA 2024 Part 4 (consumer provisions, eff. April 6, 2025) | Disclosure ([[disclosure-regulation]]) | General (B2C; drip pricing and misleading omissions focus) | Operative | CMA direct enforcement; fines up to 10% of global turnover; enhanced consumer measures (compensation orders) |
| CMA Dynamic Pricing Project (Nov 2024-June 2025) | Disclosure (guidance) | General (travel, hospitality, entertainment, e-commerce focus) | Complete (guidance published June 2025) | Non-binding; informs future enforcement priorities |
| CMA Consumer Protection Enforcement Sweep (Nov 2025) | Disclosure (enforcement) | Sector-specific (ticketing, driving schools, gyms, homeware) | Operative (investigations ongoing) | CMA direct enforcement under DMCCA; eight investigations opened; advisory letters to 100 firms |
| FCA General Insurance Pricing Practices (PS21/5, eff. Jan 1, 2022) | Prohibition ([[command-and-control]]) | Insurance (home and motor only) | Operative | FCA; annual senior manager attestation; pricing information reports; supervisory review |
| UK GDPR Article 22 (retained EU law, eff. May 25, 2018; amended by DUAA 2025) | Rights & liabilities ([[rights-and-liabilities-regulation]]) | General | Enacted (amended; operative status weakened by DUAA 2025) | ICO; fines up to GBP 17.5M or 4% of global turnover; individual right to lodge complaint |
| Data (Use and Access) Act 2025 (DUAA, Royal Assent May 2025; data provisions eff. late 2025) | Rights & liabilities (relaxation) | General | Enacted | ICO |
| Competition Act 1998 (Chapter I and II prohibitions) | Competition ([[competition-over-regulation]]) | General | Operative | CMA; fines up to 10% of worldwide turnover for each year of infringement (max 3 years) |
| DMCCA 2024 Part 1 — Strategic Market Status (SMS) regime (eff. Jan 1, 2025) | Competition (structural) | Digital markets (designated SMS firms only) | Operative (first designations June 2025: Google, Apple) | CMA Digital Markets Unit; fines up to 10% of global turnover |
| UK pro-innovation AI regulatory framework (2023 White Paper; no legislation) | Self-regulation ([[self-regulation]]) | General | Proposed (principles only; no binding obligations) | Sector regulators (existing); no dedicated AI regulator |

## Detail

### DMCCA 2024 Part 4 — Consumer Protection Provisions (eff. April 6, 2025)

Part 4 of the Digital Markets, Competition and Consumers Act 2024 replaces and updates the Consumer Protection from Unfair Trading Regulations 2008 (CPRs), which were the UK's transposition of the EU Unfair Commercial Practices Directive. The DMCCA modernizes the consumer protection framework and, critically, grants the CMA direct administrative enforcement powers for the first time.

**Drip pricing prohibition — Section 230.** The total price of a product, including all mandatory fees, taxes, charges, or other payments, must be included in any invitation to purchase. Partitioned pricing (displaying components separately without a total) no longer suffices. This targets practices prevalent in ticketing (93% of businesses reviewed by the Department for Business and Trade engaged in drip pricing), cinema (69%), and gym membership (60%).

**Misleading omissions — Section 228.** A commercial practice is unfair if it omits or hides material information that the average consumer needs to make an informed transactional decision. This provision could theoretically reach personalized pricing if failing to disclose price personalization constitutes a misleading omission, though no enforcement has tested this theory.

**Direct CMA enforcement.** Prior to the DMCCA, the CMA could not directly enforce consumer law — it had to seek enforcement orders through the courts. The DMCCA grants the CMA administrative enforcement powers: it can investigate, find infringement, impose fines up to 10% of global turnover, and order enhanced consumer measures (including compensation). This institutional shift is significant — it transforms the CMA from a body that could merely threaten litigation into one that can impose penalties directly.

**What it does NOT cover.** The DMCCA's consumer provisions do not specifically address personalized pricing. Section 230's total price requirement targets drip pricing (sequential disclosure of mandatory fees), not algorithmic price personalization. There is no equivalent to New York's A6765 disclosure mandate ("THIS PRICE WAS SET BY AN ALGORITHM USING YOUR PERSONAL DATA") or the EU's CRD Art. 6(1)(ea) (pre-contractual disclosure of personalized pricing). The UK post-Brexit chose not to replicate the Omnibus Directive's personalized pricing disclosure.

**Primary**: [DMCCA 2024 (legislation.gov.uk)](https://www.legislation.gov.uk/ukpga/2024/13/contents); [CMA, "Unfair Commercial Practices" guidance (CMA207)](https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices); [CMA, "Price Transparency" guidance (CMA209)](https://www.gov.uk/government/publications/price-transparency-cma209)

**Secondary**: [Lewis Silkin, "Our Guide to the DMCCA 2024 — Consumer Law" (Sept 2024)](https://www.lewissilkin.com/en/insights/2024/09/12/our-guide-digital-markets-competition-consumers-bill-focusing-consumer-law); [Charles Russell Speechlys, "DMCCA: What the UK's New Consumer Rules Mean" (2025)](https://www.charlesrussellspeechlys.com/en/insights/expert-insights/commercial/2025/digital-markets-competition-and-consumers-act-2024-dmcca-what-the-uks-new-consumer-rules-now-mean-for-consumer-facing-businesses/); [Mayer Brown, "CMA Unleashes New Consumer Powers" (Nov 2025)](https://www.mayerbrown.com/en/insights/publications/2025/11/cma-unleashes-new-consumer-powers-with-online-pricing-blitz-whats-new-and-whats-next)

### CMA Dynamic Pricing Project (Nov 2024 — June 2025)

The CMA launched a dedicated project on dynamic pricing in November 2024, examining how dynamic pricing is used across travel, hospitality, live entertainment, and e-commerce. The project published its update and findings on June 20, 2025.

**Definition.** The CMA defines dynamic pricing as situations where "businesses adjust prices rapidly and frequently in response to changing demand conditions." This definition is narrower than "personalized pricing" (setting different prices for different consumers based on personal data) and the CMA explicitly distinguishes the two. Some high-profile incidents in the entertainment sector (notably the Oasis ticket controversy in 2024) that were publicly characterized as "dynamic pricing" did not meet the CMA's definition because prices were not "rapidly and frequently adjusted in response to demand."

**Findings.** The CMA found that dynamic pricing can be "consistent with effective competition and good outcomes for consumers" — including better capacity utilization and efficiency — but identified four risk scenarios: (1) consumers unaware that dynamic pricing is being used; (2) consumers pressured to make quick decisions because prices may rise suddenly; (3) vulnerable consumers disproportionately disadvantaged; (4) dynamic pricing used to obtain or maintain market power.

**Practical guidance.** The CMA published "top tips" for businesses: be upfront about price variability; explain what drives price changes; provide the range of prices (minimum and maximum); keep records sufficient to explain pricing models if challenged by the CMA.

**Significance for personalized pricing.** The CMA's project focused on dynamic pricing (demand-responsive), not personalized pricing (data-based, individual-specific). The project acknowledged that personalized pricing raises additional concerns but did not address it directly. The CMA noted that "challenges remain regarding markets where prices are 'personalised' or set by complex, 'intelligent' algorithms" — signaling awareness without action.

**Primary**: [CMA, "Dynamic Pricing Project" case page](https://www.gov.uk/cma-cases/dynamic-pricing-project); [CMA, "Dynamic Pricing: Project Update" (June 2025)](https://www.gov.uk/government/publications/dynamic-pricing-project-update)

**Secondary**: [Pinsent Masons, "Dynamic Pricing Update Demonstrates CMA's Proactive Stance" (2025)](https://www.pinsentmasons.com/out-law/news/dynamic-pricing-update-cmas-proactive-stance); [CMS, "Dynamic Pricing in the UK — Here to Stay" (June 2025)](https://cms-lawnow.com/en/ealerts/2025/06/dynamic-pricing-in-the-uk-here-to-stay); [IP Tech Blog, "UK Regulator Publishes Update on Dynamic Pricing Project" (July 2025)](https://www.iptechblog.com/2025/07/uk-regulator-publishes-update-on-dynamic-pricing-project-and-top-tips-for-businesses-using-dynamic-pricing/); [Lexology, "Dynamic Pricing: CMA Findings and Guidance for the Travel Sector"](https://www.lexology.com/library/detail.aspx?g=b6709c31-ca66-49fb-8684-d318663f053d)

### CMA Consumer Protection Enforcement Sweep (Nov 18, 2025)

On November 18, 2025, the CMA launched its first enforcement actions under the DMCCA's new direct consumer enforcement powers, targeting online pricing practices across multiple sectors.

**Investigations opened.** Eight businesses: StubHub (ticketing), viagogo (ticketing), AA Driving School, BSM Driving School, Gold's Gym, Wayfair (homeware), Appliances Direct, and Marks Electrical. The investigations focus on drip pricing (mandatory fees not included in headline prices), default opt-ins, and alleged pressure selling tactics.

**Advisory letters.** 100 firms received advisory letters across 14 sectors: holidays, driving schools, homeware retailers, rail travel, parking, bus and coach travel, luggage storage, cinemas, live event tickets, food and drink delivery, letter and parcel delivery, gyms and fitness, fashion, and online vouchers.

**Cross-economy review.** The CMA reviewed more than 400 businesses across 19 sectors, finding concerns in 14.

**CMA Chairman statement.** Douglas Gurr stated that "pricing strategies which obscure the true cost of a product or service, or which manipulate consumer behaviour through opaque algorithms, may infringe consumer protection law." This language — "opaque algorithms" — signals that the CMA views algorithmic pricing practices as within its enforcement remit, even though the current investigations target drip pricing rather than personalized pricing.

**Significance.** This enforcement sweep demonstrates operational capacity under the new DMCCA powers but does not yet target personalized or algorithmic pricing specifically. The targets are drip pricing and hidden fees — the disclosure end of the spectrum. The Gurr quote signals intent to address algorithmic opacity, but this remains prospective.

**Primary**: [CMA, "CMA Launches Major Consumer Protection Drive" press release (Nov 18, 2025)](https://www.gov.uk/government/news/cma-launches-major-consumer-protection-drive-focused-on-online-pricing-practices)

**Secondary**: [Baker Botts, "CMA Launches Consumer Protection Drive" (Nov 2025)](https://www.bakerbotts.com/thought-leadership/publications/2025/november/cma-launches-consumer-protection-drive); [Sidley Austin, "CMA Opens Investigations into Online Pricing Practices" (Nov 2025)](https://www.sidley.com/en/insights/newsupdates/2025/11/uk--competition-and-markets-authority-opens-investigations-into-online-pricing-practices); [Bird & Bird, "CMA Launches Major Consumer Enforcement Drive" (2025)](https://www.twobirds.com/en/insights/2025/uk/cma-launches-major-consumer-enforcement-drive-focused-on-online-pricing-practices); [Taylor Wessing, "CMA Announces First Eight Investigations" (Dec 2025)](https://www.taylorwessing.com/en/insights-and-events/insights/2025/12/aq-cma-announces-first-eight-investigations-into-consumer-law-breaches-using-new-enforcement-powers); [Baker McKenzie, "CMA Commences Enforcement Action Under the DMCCA 2024" (2025)](https://connectontech.bakermckenzie.com/united-kingdom-cma-commences-enforcement-action-under-the-digital-markets-competition-and-consumers-act-2024-focusing-on-online-pricing-practices/); [Wilson Sonsini, "Price Check: The UK's New Consumer Protection Push" (2025)](https://www.wsgr.com/en/insights/price-check-the-uks-new-consumer-protection-push.html)

### FCA General Insurance Pricing Practices — Price Walking Ban (PS21/5, eff. Jan 1, 2022)

The Financial Conduct Authority's General Insurance Pricing Practices (GIPP) rules, published as PS21/5 in May 2021 and effective January 1, 2022, constitute the UK's only sector-specific prohibition directly targeting algorithmic price discrimination.

**What it prohibits.** Home and motor insurers must offer renewing customers a price no higher than the equivalent new business price (ENBP) — the price they would quote to a new customer with the same risk profile, through the same sales channel, at the same time. This directly targets "price walking" — the practice of incrementally increasing premiums for loyal customers year-on-year. Price walking is a form of algorithmic price discrimination: insurers used tenure data (how long a customer had been with the firm) combined with behavioral data (low propensity to switch) to identify customers who would absorb price increases without leaving. The algorithms identified the least price-sensitive customers and extracted surplus from them — a first-degree price discrimination practice enabled by data and computation.

**Scale of the problem.** The FCA's market study (MS18/1.3) found that 6 million policyholders were paying over 50% more than those with a similar risk profile. If they had paid the average price for their risk, they would have saved GBP 1.2 billion collectively. The FCA estimated its reforms would save consumers GBP 4.2 billion over 10 years.

**Compliance mechanism.** ICOBS 6B requires firms to: not systematically discriminate against customers based on tenure; provide annual senior manager attestation of compliance; submit annual pricing information reports; maintain written records of how they satisfy the non-discrimination requirement.

**Scope limitation.** The price walking ban applies only to home and motor insurance. Travel insurance, health insurance, commercial insurance, and other lines are excluded. No other UK sector has adopted an equivalent prohibition on tenure-based algorithmic price discrimination.

**Primary**: [FCA, PS21/5: General Insurance Pricing Practices (May 2021)](https://www.fca.org.uk/publication/policy/ps21-5.pdf); [FCA, PS21/11: Amendments (Aug 2021)](https://www.fca.org.uk/publications/policy-statements/ps21-11-general-insurance-pricing-practices-amendments); [FCA, "FCA Confirms Measures to Protect Customers from the Loyalty Penalty" press release](https://www.fca.org.uk/news/press-releases/fca-confirms-measures-protect-customers-loyalty-penalty-home-motor-insurance-markets)

**Secondary**: [PwC, "The Loyalty Penalty Ban — Where Are We Now?" (2024)](https://www.pwc.co.uk/industries/financial-services/insights/loyalty-penalty-ban-where-are-we-now.html); [Clifford Chance, "FCA Indicates Response to Rising Retail Market Insurance Premiums" (Feb 2024)](https://www.cliffordchance.com/insights/resources/blogs/insurance-insights/2024/02/fca-indicates-response-to-rising-retail-market-insurance-premiums.html); [Akur8, "FCA Price Walking Ban in the UK: Expected Impacts for Insurers" (white paper)](https://www.akur8.com/white-papers/fca-price-walking-ban)

### UK GDPR Article 22 — Automated Decision-Making (retained EU law; amended by DUAA 2025)

UK GDPR Article 22 mirrors the EU provision: individuals have the right not to be subject to a decision based solely on automated processing, including profiling, that produces legal effects or similarly significantly affects them. The ICO has issued guidance on AI and data protection that addresses Article 22's scope.

**ICO guidance.** The ICO states that Article 22 applies when three conditions are met: (1) a decision is made; (2) the decision is based solely on automated processing, including profiling; (3) the decision produces legal effects or similarly significantly affects the individual. The ICO's guidance on AI and data protection notes that the "significant effects" threshold could encompass decisions that "affect the circumstances, behaviour or choices of the individuals concerned" and gives examples including "an online advert that is significantly discriminatory." Whether personalized pricing meets this threshold is not specifically addressed.

**Data (Use and Access) Act 2025 — narrowing.** The DUAA significantly amends UK GDPR Article 22, representing the most important post-Brexit divergence from the EU in this domain. The Act narrows the general restriction on automated decision-making so that it applies only when special category data (health, racial or ethnic origin, political beliefs, religious views, biometric, genetic information) is involved. For all other personal data — including the browsing history, purchase behavior, location data, and income proxies that power algorithmic pricing — controllers can now rely on "legitimate interests" as a lawful basis for solely automated decision-making. The Act maintains safeguards: controllers must inform data subjects of significant automated decisions, provide a right to contest, and enable human intervention. But the substantive restriction is loosened: automated pricing decisions based on non-sensitive personal data will no longer trigger the Article 22 prohibition; they will only need to comply with the safeguard requirements.

**Significance.** The DUAA moves the UK away from the EU's rights-based approach to automated decision-making. In the EU, GDPR Article 22 remains a general prohibition (contested but intact) that at least theoretically constrains personalized pricing. In the UK, the equivalent provision now applies only to special category data — meaning a retailer using browsing history and purchase patterns to set personalized prices will not trigger the Article 22 restriction at all, provided it does not process health data, racial data, or other special categories. This is a deliberate regulatory choice: the UK is facilitating algorithmic decision-making as part of its pro-innovation agenda, explicitly diverging from the EU's more cautious posture.

**Primary**: [UK GDPR Article 22](https://www.legislation.gov.uk/eur/2016/679/article/22); [ICO, "Automated Decision-Making and Profiling" guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/automated-decision-making-and-profiling/); [DUAA 2025 s.80](https://www.legislation.gov.uk/ukpga/2025/18/section/80)

**Secondary**: [Debevoise, "The UK's New Automated Decision-Making Rules — And How They Compare to the EU GDPR" (Nov 2025)](https://www.debevoisedatablog.com/2025/11/19/the-uks-new-automated-decision-making-rules-and-how-they-compare-to-the-eu-gdpr/); [Freshfields, "UK Data Reforms Unpacked: Implications for AI and Other Automated Decision-Making" (2025)](https://technologyquotient.freshfields.com/post/102krow/uk-data-reforms-unpacked-implications-for-ai-and-other-automated-decision-making); [Alston & Bird, "UK's Data (Use and Access) Act 2025 — What Does It Change?" (Jan 2026)](https://www.alston.com/en/insights/publications/2026/01/uk-data-use-and-access-act-2025); [Barrister Group, "Data Use and Access Act 2025: Regulating Automated Decision-Making" (2025)](https://thebarristergroup.co.uk/blog/data-use-and-access-act-2025)

### Competition Act 1998 — Chapter I and II Prohibitions

The Competition Act 1998 provides the UK's substantive competition law framework, mirroring EU TFEU Articles 101/102.

**Chapter I (equivalent to Article 101).** Prohibits agreements between undertakings that prevent, restrict, or distort competition. This reaches algorithmic collusion: the CMA's 2018 working paper on pricing algorithms identified the "hub-and-spoke" scenario (multiple firms using the same pricing algorithm) as the "most immediate risk." Algorithmic price coordination implemented through shared software falls within the Chapter I prohibition.

**Chapter II (equivalent to Article 102).** Prohibits abuse of a dominant position. Algorithmic personalized pricing by a dominant firm could constitute an exploitative abuse if it involves applying dissimilar conditions to equivalent transactions.

**CMA 2018 working paper.** In October 2018, the CMA published an economic working paper on "Pricing Algorithms: Economic Working Paper on the Use of Algorithms to Facilitate Collusion and Personalised Pricing." This identified three algorithmic collusion scenarios — hub-and-spoke (shared algorithm), predictable agent (parallel algorithms that learn to coordinate), autonomous machine (unsupervised algorithms that independently discover collusion). The CMA found that hub-and-spoke posed the most immediate risk, with predictable agent and autonomous machine scenarios being longer-term. On personalized pricing, the CMA found that tacit coordination and personalized pricing are "very unlikely to occur in the same market" because price opacity undermines the mutual monitoring required for collusion.

**No enforcement actions on algorithmic pricing.** As of February 2026, the CMA has not brought any competition enforcement action specifically targeting algorithmic pricing or algorithmic collusion. The 2018 working paper remains the CMA's primary analytical contribution, but it has not translated into enforcement.

**Primary**: [Competition Act 1998 (legislation.gov.uk)](https://www.legislation.gov.uk/ukpga/1998/41/contents); [CMA, "Pricing Algorithms: Economic Working Paper" (Oct 2018)](https://www.gov.uk/government/publications/pricing-algorithms-research-collusion-and-personalised-pricing)

**Secondary**: [Covington, "The CMA's Paper on Pricing Algorithms, Collusion and Personalised Pricing" (Nov 2018)](https://www.covcompetition.com/2018/11/the-cmas-paper-on-pricing-algorithms-collusion-and-personalised-pricing/); [Morgan Lewis, "Algorithmic Pricing Emerges as Enforcement Priority for EU & UK Antitrust Regulators" (Oct 2025)](https://www.morganlewis.com/pubs/2025/10/algorithmic-pricing-emerges-as-enforcement-priority-for-eu-and-uk-antitrust-regulators)

### DMCCA 2024 Part 1 — Strategic Market Status (SMS) Regime (eff. Jan 1, 2025)

The DMCCA's digital markets provisions create a regime for firms designated with Strategic Market Status (SMS) — those with "substantial and entrenched market power" and a "position of strategic significance" in a digital activity. The CMA's Digital Markets Unit (DMU) administers the regime.

**First designations.** In June 2025, the CMA designated Google (general search and search advertising) and both Apple and Google (mobile platforms) with SMS. Conduct requirements are being phased: Category 1 (2025) includes choice screens and data portability; Category 2 (2026) includes fair treatment of specialist search services and transparency in search advertising auctions; Category 3 (2027+) includes restrictions on data sharing within Google's ecosystem and further controls on ad pricing.

**Relevance to surveillance pricing.** The SMS regime is structurally analogous to the EU's DMA — it targets platform gatekeepers rather than consumer-facing pricing. However, the conduct requirements around data sharing, fair ranking, and advertising transparency restrict the data infrastructure that enables personalized pricing by designated firms. The regime is competition-adjacent, not consumer protection.

**Primary**: [CMA, "How the UK's Digital Markets Competition Regime Works"](https://www.gov.uk/guidance/how-the-uks-digital-markets-competition-regime-works); [CMA, "CMA Confirms Google Has Strategic Market Status" (June 2025)](https://www.gov.uk/government/news/cma-confirms-google-has-strategic-market-status-in-search-services)

**Secondary**: [Macfarlanes, "Key Takeaways from the CMA's First Round of SMS Designations" (2025)](https://www.macfarlanes.com/insights/102lwtj/key-takeaways-from-the-cmas-first-round-of-sms-designations/); [DWF Group, "CMA's First SMS Designation" (July 2025)](https://dwfgroup.com/en/news-and-insights/insights/2025/7/cmas-first-sms-designation)

### UK Pro-Innovation AI Regulatory Framework (2023 White Paper; no legislation)

The UK's approach to AI regulation is deliberately non-legislative. The 2023 White Paper "A Pro-Innovation Approach to AI Regulation" established five cross-sector principles (safety, transparency, fairness, accountability, contestability) but did not propose binding rules. Instead, existing sector regulators (FCA, CMA, ICO, Ofcom, etc.) are expected to apply these principles within their existing mandates.

**No AI-specific pricing obligations.** Unlike the EU AI Act, which classifies credit scoring and insurance pricing algorithms as high-risk under Annex III, the UK framework imposes no specific obligations on algorithmic pricing systems. There is no risk classification, no conformity assessment, no mandatory audit for pricing algorithms.

**Significance.** The absence of AI-specific regulation for pricing is itself a regulatory choice. The UK has opted for the lightest possible approach to AI governance — sector regulators apply existing rules, supplemented by voluntary principles. For surveillance pricing, this means the CMA's consumer protection powers and the FCA's sector-specific rules are the operative instruments, not any AI-specific framework. A comprehensive AI Bill has been indicated for possible introduction in 2026, with anticipated priorities including accountability mechanisms for foundation models and enhanced consumer redress, but this remains prospective.

**Primary**: [UK Government, "A Pro-Innovation Approach to AI Regulation" White Paper (March 2023)](https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach/white-paper)

**Secondary**: [Slaughter and May, "AI Update for 2026" (horizon scanning)](https://www.slaughterandmay.com/horizon-scanning/2026/digital/ai-update-for-2026/); [Chambers, "Artificial Intelligence 2025 — UK"](https://practiceguides.chambers.com/practice-guides/artificial-intelligence-2025/uk/trends-and-developments)

## Analysis

**Hierarchy.** No single strategy dominates across all sectors. The FCA price walking ban is the most interventionist instrument — a direct prohibition on tenure-based price discrimination in home and motor insurance — but it is sector-specific and does not extend beyond its narrow scope. For general commerce, disclosure is the only operative strategy, deployed through the DMCCA's total price requirements and the CMA's enforcement sweep. Competition powers exist (Competition Act 1998, SMS regime) but have not been used against algorithmic pricing. Rights instruments (UK GDPR Article 22) have been weakened by the DUAA 2025. The hierarchy is therefore sector-dependent: prohibition dominates in insurance; disclosure dominates in general commerce; competition and rights are present but inoperative for pricing specifically.

**Design logic.** Differentiated. The UK has deliberately chosen different strategies for different sectors, in a pattern that resembles New York's differentiated approach (disclosure for general commerce, prohibition for rental housing) but with a critical difference: the differentiation is institutional rather than legislative. New York enacted two statutes in the same legislative session; the UK's differentiation emerged from different regulators acting in different eras under different mandates. The FCA banned price walking in insurance based on a market study finding specific consumer harm. The CMA is addressing drip pricing in general commerce under the DMCCA's new powers. The ICO administers the UK GDPR's weakened automated decision-making rules. Each regulator operates in its lane. The differentiation is not the result of a unified policy design — it reflects the UK's distributed regulatory architecture, where sector regulators act independently rather than a single legislature choosing strategies for different sectors.

**Institution relied on — divergence.** Two notable divergences:

First, the DMCCA's consumer protection provisions are disclosure-based instruments that theoretically trust the market — informed consumers discipline sellers by avoiding businesses with hidden fees. But the CMA's new direct enforcement powers shift the operative institution from the market to the state. The CMA is not waiting for consumers to exercise informed choice; it is launching investigations, sending advisory letters, and threatening fines up to 10% of global turnover. The disclosure strategy is deployed through state enforcement rather than market discipline — the same divergence observed in New York's A6765 (disclosure enforced by the AG, not by consumer market behavior).

Second, the DUAA 2025's weakening of UK GDPR Article 22 is a deliberate institutional choice. By narrowing the automated decision-making restriction to special category data, the UK is choosing to trust the market to govern algorithmic pricing rather than empowering individuals with rights against automated decisions. The EU retains the rights-based approach (however contested); the UK has effectively removed it for non-sensitive personal data. This is a bet on market discipline and innovation incentives over individual data rights — a distinctive institutional position on the topology.

## Evidence

**FCA price walking ban — evaluation (2025).** The FCA published an evaluation of the GIPP reforms (EP25/2) finding that the remedies have "significantly reduced premium disparities between new and renewing customers" and that price walking has been "largely eliminated." However, the ban had unintended consequences: overall motor insurance prices rose approximately 40% compared to pre-ban levels, and home insurance prices rose approximately 30% by the end of 2023. The mechanism: insurers were cross-subsidizing new customer acquisition with profits from price-walked renewals. When the ban eliminated price walking, insurers raised new customer prices to compensate. The FCA estimated that the reforms would still save consumers GBP 4.2 billion over 10 years, but those savings come from not paying more at renewal rather than from lower prices overall. This is significant evidence for the topology: prohibition achieved its specific objective (eliminating tenure-based discrimination) but produced a market-wide price increase as firms adjusted their business models. [FCA, EP25/2: Evaluation of General Insurance Pricing Practices Remedies (2025)](https://www.fca.org.uk/publication/corporate/ep25-2.pdf); [PwC, "The Loyalty Penalty Ban — Where Are We Now?"](https://www.pwc.co.uk/industries/financial-services/insights/loyalty-penalty-ban-where-are-we-now.html)

**CMA November 2025 enforcement — drip pricing, not personalized pricing.** The CMA's first eight investigations target drip pricing and misleading fees, not algorithmic personalized pricing. The cross-economy review found concerns in 14 of 19 sectors, but these are transparency-related (hidden fees, default opt-ins) rather than data-driven pricing. No enforcement action has targeted personalized pricing in the UK as of February 2026. [CMA press release (Nov 18, 2025)](https://www.gov.uk/government/news/cma-launches-major-consumer-protection-drive-focused-on-online-pricing-practices)

**CMA 2018 working paper — analytical contribution, no enforcement.** The CMA's 2018 economic working paper on pricing algorithms remains its primary analytical contribution on algorithmic collusion and personalized pricing. The paper identified hub-and-spoke algorithmic coordination as the most immediate risk. Seven years later, no competition enforcement action targeting algorithmic pricing has been brought. The gap between analytical recognition and enforcement action is notable. [CMA, "Pricing Algorithms: Economic Working Paper" (Oct 2018)](https://www.gov.uk/government/publications/pricing-algorithms-research-collusion-and-personalised-pricing)

**No ICO enforcement on automated pricing decisions.** No enforcement action by the ICO has applied UK GDPR Article 22 to personalized pricing. The DUAA 2025 makes future enforcement less likely by narrowing the restriction to special category data. The rights-based channel for challenging algorithmic pricing is weaker in the UK than in the EU.

**SMS regime — early stage, no pricing-relevant enforcement.** The first SMS designations were made in June 2025. Conduct requirements are being phased over 2025-2027. No pricing-specific conduct requirement has been imposed, and no enforcement action under the SMS regime relates to pricing as of February 2026.

## Movement

The UK's trajectory shows two distinct arcs: sector-specific prohibition arriving early (2022), followed by a slow build-up of general enforcement capacity (2024-2025), with a simultaneous loosening of data protection constraints (2025).

1. **October 2018**: CMA publishes economic working paper on pricing algorithms — analytical recognition of algorithmic collusion and personalized pricing risks; no enforcement action follows
2. **July 2020**: CMA publishes Online Platforms and Digital Advertising market study final report — recommends pro-competition regime for digital markets; leads eventually to DMCCA
3. **May 2021**: FCA publishes PS21/5 (GIPP rules) — prohibition on price walking in home and motor insurance
4. **January 2022**: FCA price walking ban takes effect — first and only prohibition on algorithmic price discrimination in the UK
5. **May 2024**: DMCCA receives Royal Assent
6. **January 2025**: DMCCA digital markets provisions (SMS regime) take effect
7. **March 2023 / ongoing**: UK Government publishes pro-innovation AI White Paper — no binding AI regulation for pricing
8. **April 2025**: DMCCA consumer provisions take effect — CMA gains direct enforcement powers
9. **May 2025**: Data (Use and Access) Act receives Royal Assent — weakens UK GDPR Article 22 for non-sensitive data
10. **June 2025**: CMA publishes dynamic pricing project findings — guidance, not enforcement; personalized pricing noted as unaddressed
11. **June 2025**: First SMS designations (Google, Apple)
12. **November 2025**: CMA launches first consumer enforcement actions — eight investigations into drip pricing, 100 advisory letters; Chairman Gurr signals concern about "opaque algorithms"

The trajectory is notable for what it includes and what it omits. The UK moved first on sector-specific prohibition (FCA price walking ban, 2022) — earlier than any other jurisdiction in the survey adopted a prohibition strategy for algorithmic price discrimination. But the UK has not adopted any general disclosure requirement for personalized pricing (contrast NY A6765, EU CRD Art. 6(1)(ea)), any general prohibition on algorithmic pricing (contrast China), or any rights-based instrument specifically addressing pricing (UK GDPR Art. 22 is being weakened, not strengthened). The general commerce regulatory landscape consists of transparency obligations for fees (drip pricing) and emerging competition enforcement capacity (SMS), but personalized pricing specifically remains in the "analytical recognition without regulatory response" zone.

The post-Brexit divergence is accelerating. While the EU is consulting on the Digital Fairness Act (potentially adding personalized pricing obligations), the UK is loosening automated decision-making restrictions through the DUAA 2025. The trajectories are moving in opposite directions: the EU toward greater constraint, the UK toward facilitation. This divergence may be the most analytically significant feature of the UK's profile for Paper 1.

## Open Questions

1. **Will the CMA extend its enforcement focus from drip pricing to personalized pricing?** Chairman Gurr's reference to "opaque algorithms" signals awareness, but the current enforcement actions target only fee transparency. The dynamic pricing project explicitly distinguished personalized pricing and did not address it. Will the CMA open a dedicated investigation into personalized pricing, or will it remain in the guidance-and-study phase?
2. **Will other sectors adopt FCA-style price walking bans?** The FCA's prohibition applies only to home and motor insurance. Other insurance lines, telecoms, energy, and subscription services all exhibit similar loyalty penalty dynamics. Will the FCA extend the ban, or will other regulators adopt equivalent sector-specific prohibitions?
3. **How will the DUAA 2025 affect algorithmic pricing in practice?** The narrowing of UK GDPR Article 22 to special category data removes a theoretical constraint on algorithmic pricing. Will firms expand personalized pricing practices in response? Will the ICO develop new guidance addressing algorithmic pricing under the relaxed framework?
4. **UK-EU regulatory divergence — how far will it go?** The EU is consulting on the DFA (potentially adding personalized pricing obligations); the UK is loosening ADM restrictions. How will this divergence affect businesses operating in both markets? Will the UK become a more permissive environment for algorithmic pricing than the EU?
5. **CMA competition enforcement on algorithmic collusion.** The CMA's 2018 working paper identified hub-and-spoke algorithmic collusion as an immediate risk. Seven years later, no enforcement action has followed. Will the CMA bring an algorithmic collusion case, and will it parallel the EU Commission's confirmed investigations?
6. **FCA price walking ban — unintended consequences.** The 40% increase in motor insurance prices post-ban is significant. Will the FCA adjust the GIPP rules, or will the market stabilize? Does the unintended price increase undermine the case for prohibition in other sectors?
7. **AI Bill.** A comprehensive AI Bill has been indicated for possible introduction in 2026. If enacted, will it impose any obligations on algorithmic pricing systems? Will it create a risk classification that captures pricing, similar to the EU AI Act's high-risk designation for credit scoring?
8. **Personalized pricing and the DMCCA's misleading omissions prohibition.** Could a failure to disclose personalized pricing constitute a "misleading omission" under DMCCA Section 228? This theory is untested. If the CMA pursued it, it would create a de facto disclosure obligation for personalized pricing without explicit legislative mandate.

## Sources

**Primary**:
- [DMCCA 2024 (legislation.gov.uk)](https://www.legislation.gov.uk/ukpga/2024/13/contents)
- [CMA, "Unfair Commercial Practices" guidance (CMA207)](https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices)
- [CMA, "Price Transparency" guidance (CMA209)](https://www.gov.uk/government/publications/price-transparency-cma209)
- [CMA, "Dynamic Pricing Project" case page](https://www.gov.uk/cma-cases/dynamic-pricing-project)
- [CMA, "Dynamic Pricing: Project Update" (June 2025)](https://www.gov.uk/government/publications/dynamic-pricing-project-update)
- [CMA, "CMA Launches Major Consumer Protection Drive" press release (Nov 18, 2025)](https://www.gov.uk/government/news/cma-launches-major-consumer-protection-drive-focused-on-online-pricing-practices)
- [CMA, "Pricing Algorithms: Economic Working Paper" (Oct 2018)](https://www.gov.uk/government/publications/pricing-algorithms-research-collusion-and-personalised-pricing)
- [CMA, "How the UK's Digital Markets Competition Regime Works"](https://www.gov.uk/guidance/how-the-uks-digital-markets-competition-regime-works)
- [CMA, "CMA Confirms Google Has SMS" press release (June 2025)](https://www.gov.uk/government/news/cma-confirms-google-has-strategic-market-status-in-search-services)
- [FCA, PS21/5: General Insurance Pricing Practices (May 2021)](https://www.fca.org.uk/publication/policy/ps21-5.pdf)
- [FCA, PS21/11: Amendments (Aug 2021)](https://www.fca.org.uk/publications/policy-statements/ps21-11-general-insurance-pricing-practices-amendments)
- [FCA, EP25/2: Evaluation of GIPP Remedies (2025)](https://www.fca.org.uk/publication/corporate/ep25-2.pdf)
- [FCA, "FCA Confirms Measures to Protect Customers from the Loyalty Penalty" press release](https://www.fca.org.uk/news/press-releases/fca-confirms-measures-protect-customers-loyalty-penalty-home-motor-insurance-markets)
- [Competition Act 1998 (legislation.gov.uk)](https://www.legislation.gov.uk/ukpga/1998/41/contents)
- [UK GDPR Article 22 (legislation.gov.uk)](https://www.legislation.gov.uk/eur/2016/679/article/22)
- [DUAA 2025 s.80 (legislation.gov.uk)](https://www.legislation.gov.uk/ukpga/2025/18/section/80)
- [ICO, "Automated Decision-Making and Profiling" guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/automated-decision-making-and-profiling/)
- [UK Government, "A Pro-Innovation Approach to AI Regulation" White Paper (March 2023)](https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach/white-paper)
- [CMA, "Online Platforms and Digital Advertising Market Study" (July 2020)](https://www.gov.uk/cma-cases/online-platforms-and-digital-advertising-market-study)

**Secondary**:
- [Morgan Lewis, "Algorithmic Pricing Emerges as Enforcement Priority for EU & UK Antitrust Regulators" (Oct 2025)](https://www.morganlewis.com/pubs/2025/10/algorithmic-pricing-emerges-as-enforcement-priority-for-eu-and-uk-antitrust-regulators)
- [Mayer Brown, "CMA Unleashes New Consumer Powers" (Nov 2025)](https://www.mayerbrown.com/en/insights/publications/2025/11/cma-unleashes-new-consumer-powers-with-online-pricing-blitz-whats-new-and-whats-next)
- [Baker Botts, "CMA Launches Consumer Protection Drive" (Nov 2025)](https://www.bakerbotts.com/thought-leadership/publications/2025/november/cma-launches-consumer-protection-drive)
- [Sidley Austin, "CMA Opens Investigations into Online Pricing Practices" (Nov 2025)](https://www.sidley.com/en/insights/newsupdates/2025/11/uk--competition-and-markets-authority-opens-investigations-into-online-pricing-practices)
- [Bird & Bird, "CMA Launches Major Consumer Enforcement Drive" (2025)](https://www.twobirds.com/en/insights/2025/uk/cma-launches-major-consumer-enforcement-drive-focused-on-online-pricing-practices)
- [Taylor Wessing, "CMA Announces First Eight Investigations" (Dec 2025)](https://www.taylorwessing.com/en/insights-and-events/insights/2025/12/aq-cma-announces-first-eight-investigations-into-consumer-law-breaches-using-new-enforcement-powers)
- [Wilson Sonsini, "Price Check: The UK's New Consumer Protection Push" (2025)](https://www.wsgr.com/en/insights/price-check-the-uks-new-consumer-protection-push.html)
- [Baker McKenzie, "CMA Commences Enforcement Action Under the DMCCA 2024" (2025)](https://connectontech.bakermckenzie.com/united-kingdom-cma-commences-enforcement-action-under-the-digital-markets-competition-and-consumers-act-2024-focusing-on-online-pricing-practices/)
- [Lewis Silkin, "Our Guide to the DMCCA 2024 — Consumer Law" (Sept 2024)](https://www.lewissilkin.com/en/insights/2024/09/12/our-guide-digital-markets-competition-consumers-bill-focusing-consumer-law)
- [Charles Russell Speechlys, "DMCCA: What the UK's New Consumer Rules Mean" (2025)](https://www.charlesrussellspeechlys.com/en/insights/expert-insights/commercial/2025/digital-markets-competition-and-consumers-act-2024-dmcca-what-the-uks-new-consumer-rules-now-mean-for-consumer-facing-businesses/)
- [Womble Bond Dickinson, "DMCCA 2024 Explained: The CMA's New Enforcement Toolkit"](https://www.womblebonddickinson.com/uk/insights/articles-and-briefings/digital-markets-competition-and-consumers-act-2024-explained-cmas)
- [Osborne Clarke, "UK CMA Finalises Guidance on Price Transparency Under DMCCA" (2025)](https://www.osborneclarke.com/insights/uk-cma-finalises-guidance-price-transparency-under-dmcca-and-begins-enforcement-action)
- [CMS, "Price Transparency Guidance Lands" (Dec 2025)](https://cms-lawnow.com/en/ealerts/2025/12/price-transparency-guidance-lands-as-cma-launches-first-consumer-law-investigations-using-its-new-dmcc-act-powers)
- [Pinsent Masons, "Dynamic Pricing Update Demonstrates CMA's Proactive Stance" (2025)](https://www.pinsentmasons.com/out-law/news/dynamic-pricing-update-cmas-proactive-stance)
- [CMS, "Dynamic Pricing in the UK — Here to Stay" (June 2025)](https://cms-lawnow.com/en/ealerts/2025/06/dynamic-pricing-in-the-uk-here-to-stay)
- [Covington, "The CMA's Paper on Pricing Algorithms, Collusion and Personalised Pricing" (Nov 2018)](https://www.covcompetition.com/2018/11/the-cmas-paper-on-pricing-algorithms-collusion-and-personalised-pricing/)
- [PwC, "The Loyalty Penalty Ban — Where Are We Now?" (2024)](https://www.pwc.co.uk/industries/financial-services/insights/loyalty-penalty-ban-where-are-we-now.html)
- [Clifford Chance, "FCA Indicates Response to Rising Retail Market Insurance Premiums" (Feb 2024)](https://www.cliffordchance.com/insights/resources/blogs/insurance-insights/2024/02/fca-indicates-response-to-rising-retail-market-insurance-premiums.html)
- [Akur8, "FCA Price Walking Ban in the UK" (white paper)](https://www.akur8.com/white-papers/fca-price-walking-ban)
- [Debevoise, "The UK's New Automated Decision-Making Rules — And How They Compare to the EU GDPR" (Nov 2025)](https://www.debevoisedatablog.com/2025/11/19/the-uks-new-automated-decision-making-rules-and-how-they-compare-to-the-eu-gdpr/)
- [Freshfields, "UK Data Reforms Unpacked: Implications for AI and Other Automated Decision-Making" (2025)](https://technologyquotient.freshfields.com/post/102krow/uk-data-reforms-unpacked-implications-for-ai-and-other-automated-decision-making)
- [Alston & Bird, "UK's Data (Use and Access) Act 2025 — What Does It Change?" (Jan 2026)](https://www.alston.com/en/insights/publications/2026/01/uk-data-use-and-access-act-2025)
- [Macfarlanes, "Key Takeaways from CMA's First Round of SMS Designations" (2025)](https://www.macfarlanes.com/insights/102lwtj/key-takeaways-from-the-cmas-first-round-of-sms-designations/)
- [Slaughter and May, "AI Update for 2026"](https://www.slaughterandmay.com/horizon-scanning/2026/digital/ai-update-for-2026/)
- [Hogan Lovells, "The Price Isn't Right: CMA Review of Online Pricing Practices" (2025)](https://www.hoganlovells.com/en/publications/the-price-isnt-right-cma-review-of-online-pricing-practices)
- [Freshfields, "CMA Steps Up Enforcement Relating to Online Pricing Practices" (2025)](https://riskandcompliance.freshfields.com/post/102lvf8/cma-steps-up-enforcement-relating-to-online-pricing-practices)
- [HSF Kramer, "UK Consumer Protection Round-Up 2025"](https://www.hsfkramer.com/insights/2025-12/uk-consumer-protection-round-up-2025)
- [ICLG, "Consumer Protection 2025-2026: Everyone Has a Price"](https://iclg.com/practice-areas/consumer-protection-laws-and-regulations/01-everyone-has-a-price-the-impact-of-consumer-law-on-pricing-practices)

**Library**:
- [[intel-comparative-regulation]]
- [[surveillance-pricing-comparative-regulation]]
- [[baldwin-regulatory-strategies]]
- [[disclosure-regulation]]
- [[command-and-control]]
- [[competition-over-regulation]]
- [[rights-and-liabilities-regulation]]
- [[self-regulation]]
- [[code-as-regulation]]
- [[regulatory-topology-not-ladder]]
- [[government-capacities-regulation]]
- [[creative-compliance]]
- [[sp-new-york]]
- [[sp-california]]
- [[sp-eu]]
- [[sp-china]]
