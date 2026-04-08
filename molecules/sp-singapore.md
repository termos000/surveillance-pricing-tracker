---
date-created: "202602241800"
aliases:
  - "Singapore surveillance pricing profile"
tags:
  - "#molecules"
  - "#jurisdiction-profile"
topic:
  - "[[surveillance pricing]]"
  - "[[Singapore]]"
---

# Singapore — Surveillance Pricing Regulatory Profile

*Jurisdiction molecule for [[surveillance-pricing-comparative-regulation|Paper 1]].*

Singapore has no instrument that directly targets surveillance pricing or algorithmic personalized pricing. Its regulatory landscape is composed entirely of general-purpose instruments — data protection, competition law, consumer protection — none of which were designed for or have been applied to personalized pricing. What distinguishes Singapore from other jurisdictions with similarly absent targeted regulation is not the gap itself but the deliberate governance architecture around AI that nonetheless leaves pricing unaddressed: the Model AI Governance Framework, the PDPC Advisory Guidelines on AI Systems, the MAS FEAT Principles, and the AI Verify toolkit collectively constitute a sophisticated voluntary governance infrastructure that emphasizes transparency and fairness in AI decision-making but contains no binding obligation relevant to pricing. The absence of regulation is a design choice, not an oversight — Singapore's "pro-innovation, principles-based" approach deliberately avoids sector-specific or practice-specific AI regulation, channeling governance through existing laws supplemented by non-binding frameworks.

## Instruments

| Instrument | Strategy | Sector | Status | Enforcement |
|-----------|----------|--------|--------|-------------|
| PDPA ss. 13-20 (consent and notification, eff. July 2, 2014; amended 2020) | Rights & liabilities ([[rights-and-liabilities-regulation]]) | General | Operative | PDPC; financial penalties up to SGD 1M or 10% of annual turnover (post-2020 amendment); directions to stop, compliance notices |
| PDPC Advisory Guidelines on Use of Personal Data in AI Recommendation and Decision Systems (March 1, 2024) | Self-regulation ([[self-regulation]]) | General (discriminative AI systems only; excludes generative AI) | Operative (non-binding advisory) | PDPC (informational; not independently enforceable but informs enforcement of PDPA) |
| Model AI Governance Framework, 2nd ed. (PDPC/IMDA, Jan 2020) | Self-regulation ([[self-regulation]]) | General | Operative (voluntary) | None (voluntary adoption; no enforcement mechanism) |
| AI Verify Toolkit (IMDA, 2022; ongoing) with CCCS AIM Plugin (2024) | Self-regulation ([[self-regulation]]) | General | Operative (voluntary testing tool) | None (self-assessment; no enforcement) |
| CPFTA (Consumer Protection (Fair Trading) Act 2003) | Disclosure ([[disclosure-regulation]]) | General (B2C) | Operative | CCCS; court-based enforcement via injunctions; no direct administrative fines for CPFTA violations |
| CCCS Guidelines on Price Transparency (eff. Nov 1, 2020) | Disclosure (guidance) | General (originated from online travel sector study) | Operative (non-binding) | CCCS (informs CPFTA enforcement) |
| Competition Act 2004, s. 34 (anti-competitive agreements, eff. Jan 1, 2006) | Competition ([[competition-over-regulation]]) | General | Operative | CCCS; financial penalties up to 10% of turnover for each year of infringement (max 3 years) |
| Competition Act 2004, s. 47 (abuse of dominance, eff. Nov 1, 2007) | Competition ([[competition-over-regulation]]) | General | Operative | CCCS; same penalty structure as s. 34 |
| CCCS Revised Competition Guidelines (eff. Feb 1, 2022) | Competition (guidance) | General (includes digital economy considerations) | Operative (non-binding) | CCCS (informs enforcement of Competition Act) |
| MAS FEAT Principles (Nov 2018) and Veritas Initiative (2019-2022) | Self-regulation ([[self-regulation]]) | Financial services | Operative (voluntary) | MAS (supervisory expectations; not independently enforceable) |
| MAS Proposed Guidelines on AI Risk Management (consultation Nov 2025; consultation closed Jan 31, 2026) | Self-regulation (proposed, moving toward binding guidance) | Financial services | Proposed (consultation completed; final guidelines pending) | MAS (supervisory expectations; proportionate application) |
| MAS Fair Dealing Guidelines (updated May 30, 2024) | Disclosure ([[disclosure-regulation]]) | Financial services | Operative | MAS (supervisory oversight) |

## Detail

### PDPA — Consent and Notification Provisions (ss. 13-20; eff. July 2, 2014; amended 2020)

The Personal Data Protection Act 2012 governs the collection, use, and disclosure of personal data by private sector organisations. The PDPA's consent framework (Part IV) requires organisations to obtain consent for the collection, use, and disclosure of personal data, and to notify individuals of the purposes for such processing (s. 20). The 2020 amendments introduced a "legitimate interests" exception (s. 13(g)), a "business improvement" exception, and increased the maximum financial penalty from SGD 1 million to 10% of annual turnover for organisations exceeding SGD 10 million in annual turnover.

**What is absent.** The PDPA does not contain an equivalent to GDPR Article 22. There is no right against solely automated decision-making. There is no requirement for human review of automated decisions. The PDPA does not differentiate between automated and non-automated processing of personal data. An individual's recourse, if they object to algorithmic pricing, is limited to withdrawing consent — but this requires knowing that their data is being used for pricing in the first place, and the PDPA's notification obligations do not specifically require disclosure of algorithmic pricing practices. The PDPA's purpose limitation (s. 18) requires that personal data be used only for purposes the individual was notified of and consented to, which could theoretically constrain personalized pricing if pricing was not a stated purpose at collection — but this depends on how broadly the stated purpose was drafted, and organizations routinely draft purposes broadly enough to encompass pricing optimization.

**Significance for surveillance pricing.** The PDPA provides a general data protection floor — consent, notification, purpose limitation — but no provision specifically addresses or constrains algorithmic pricing. The absence of an automated decision-making right is the most consequential gap: unlike the EU (GDPR Art. 22), the UK (UK GDPR Art. 22, even as weakened by DUAA 2025), or China (PIPL Art. 24), Singapore provides no individual right to challenge an automated pricing decision or to obtain human review.

**Primary**: [PDPA 2012 (Singapore Statutes Online)](https://sso.agc.gov.sg/Act/PDPA2012); [PDPC, Advisory Guidelines on Key Concepts in the PDPA (May 2022)](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/advisory-guidelines/ag-on-key-concepts/advisory-guidelines-on-key-concepts-in-the-pdpa-17-may-2022.pdf)

**Secondary**: [ICLG, "Data Protection Laws and Regulations 2025-2026: Singapore"](https://iclg.com/practice-areas/data-protection-laws-and-regulations/singapore); [DataGuidance, "Comparing Privacy Laws: GDPR v. Singapore's PDPA" (July 2022)](https://www.dataguidance.com/sites/default/files/gdpr_v_singapore_2022_july_update.pdf); [Future of Privacy Forum, "Singapore's PDPA Shifts Away from Consent-Centric Framework"](https://fpf.org/blog/singapores-personal-data-protection-act-shifts-away-from-a-consent-centric-framework/)

### PDPC Advisory Guidelines on Use of Personal Data in AI Recommendation and Decision Systems (March 1, 2024)

The PDPC issued these advisory guidelines after public consultation (July-August 2023). The guidelines clarify how the PDPA applies to organisations that use personal data to develop and deploy AI systems used for recommendations, predictions, or decisions. They apply to discriminative AI (not generative AI).

**Consent and notification.** Organisations deploying AI systems that make recommendations, predictions, or decisions based on personal data must comply with PDPA consent and notification obligations. Notifications should be sufficient but need not be overly technical, and can be "layered" — most relevant information prominently displayed, with details available elsewhere. Organisations are encouraged to provide information at the point of data collection.

**Transparency best practices.** Organisations are encouraged to include in their written policies information about safeguards and practices ensuring AI systems are trustworthy, "especially where the outcome has high impact on consumers." The guidelines recommend disclosure of whether and how AI systems use personal data to make decisions.

**What it does NOT require.** The guidelines do not mandate disclosure of algorithmic pricing specifically. They do not create a right to contest automated decisions. They do not require human review. They do not address pricing as a use case. The guidelines are not legally binding — the PDPC states it is "likely to take positions consistent with" the guidelines when enforcing the PDPA, which creates soft pressure without legal obligation.

**Significance.** These guidelines represent Singapore's closest approach to addressing automated decision-making with personal data. Applied to a personalized pricing scenario, they would suggest (but not require) that an organization using personal data to set individualized prices should notify individuals that AI is being used in pricing decisions and obtain consent for the use of personal data for that purpose. But the guidelines create no disclosure obligation comparable to NY A6765, no opt-out right comparable to GDPR Art. 22, and no prohibition on any pricing practice.

**Primary**: [PDPC, Advisory Guidelines on Use of Personal Data in AI Recommendation and Decision Systems (March 2024)](https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems)

**Secondary**: [Bird & Bird, "PDPC Advisory Guidelines on the Use of Personal Data in AI Recommendation and Decision Systems" (2024)](https://www.twobirds.com/en/insights/2024/singapore/pdpc-advisory-guidelines-on-the-use-of-personal-data-in-ai-recommendation-and-decision-systems); [Norton Rose Fulbright, "Singapore Releases New Guidelines on the Use of Personal Data in AI Systems" (March 2024)](https://www.nortonrosefulbright.com/en/inside-fintech/blog/2024/03/singapore-releases-new-guidelines-on-the-use-of-personal-data-in-ai-systems); [Rajah & Tann, "PDPC Issues Advisory Guidelines on Use of Personal Data in AI Recommendation and Decision Systems"](https://www.rajahtannasia.com/viewpoints/pdpc-issues-advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems/); [IAPP, "Singapore's PDPC Issues Use Guidelines for AI-Powered Automated Decision-Making Systems"](https://iapp.org/news/a/singapores-pdpc-issues-use-guidelines-for-automated-decision-making-systems-powered-by-ai/)

### Model AI Governance Framework, Second Edition (PDPC/IMDA, January 2020)

The Model Framework provides voluntary, accountability-based guidance for private sector organisations deploying AI. Developed by the PDPC and IMDA, it articulates two high-level principles: (1) AI-assisted decision-making should be explainable, transparent, and fair; (2) AI systems should be human-centric and safe. The second edition (January 2020) added considerations for robustness and reproducibility.

**Fairness and transparency.** The Framework requires (as voluntary guidance) that organisations ensure AI decision-making is "fair — ensuring that decisions do not create discriminatory outcomes" — and "explainable — ensuring that the reasons behind the decision can be explained in non-technical terms." These principles could, if operationalized, reach algorithmic pricing that produces discriminatory outcomes. But the Framework provides no specific guidance on pricing, no definition of what constitutes discriminatory pricing, and no enforcement mechanism.

**Significance.** The Model Framework is Singapore's signature contribution to global AI governance — widely cited, internationally recognized, and entirely voluntary. It establishes norms but not obligations. For surveillance pricing, it is relevant as a signal of governance philosophy: Singapore believes AI governance should come from principles and voluntary adoption, not binding rules. This is the same philosophical orientation as the UK's pro-innovation AI framework (2023 White Paper), but Singapore has been more institutionally consistent in this approach — it has maintained voluntarism since 2019 without the sector-specific binding interventions (like the UK's FCA price walking ban) that create tension with the general philosophy.

**Primary**: [PDPC, Model AI Governance Framework (Second Edition, Jan 2020)](https://www.pdpc.gov.sg/help-and-resources/2020/01/model-ai-governance-framework)

**Secondary**: [OECD.AI, "Singapore's Model Framework to Balance Innovation and Trust in AI"](https://oecd.ai/en/wonk/singapores-model-framework-to-balance-innovation-and-trust-in-ai); [Diligent, "Singapore's AI Governance Framework: A Complete Guide"](https://www.diligent.com/resources/blog/Singapore-AI-regulation)

### CPFTA and CCCS Guidelines on Price Transparency (eff. November 1, 2020)

The Consumer Protection (Fair Trading) Act 2003 protects consumers against unfair trade practices. The CCCS administers the CPFTA and published Guidelines on Price Transparency on September 7, 2020 (effective November 1, 2020), following a market study on online travel bookings.

**Price transparency focus.** The Guidelines address four pricing practices: drip pricing, price comparisons, discounts, and the use of the term "free." For drip pricing, suppliers must include unavoidable fees and charges in the headline price, or disclose them clearly and prominently alongside the headline price. Pre-ticked boxes for add-ons must be properly disclosed.

**CPFTA enforcement mechanism.** Unlike the UK's DMCCA 2024, the CCCS cannot impose administrative fines for CPFTA violations. Enforcement is court-based: the CCCS can apply for injunctions, and consumers or the Consumers Association of Singapore (CASE) can seek remedies. This structural limitation constrains enforcement capacity.

**What it does NOT cover.** The Guidelines and the CPFTA do not address personalized pricing. They target drip pricing (hidden mandatory fees) and misleading price comparisons — the disclosure end of the spectrum. There is no equivalent to the EU CRD Art. 6(1)(ea) requirement to disclose personalized pricing, no equivalent to NY A6765, and no prohibition on any form of algorithmic pricing.

**Dark patterns enforcement (2024-2025).** The CCCS has intensified enforcement against dark patterns in e-commerce, including subscription traps, fake reviews, urgency/scarcity claims, and misleading advertising. Notable actions include enforcement against a food delivery platform for misleading "unlimited free delivery" claims (November 2024), fake review investigations (June 2024, July 2025 including an AI-generated fake reviews case), and hair salon price concealment targeting elderly consumers. These enforcement actions target misleading pricing practices but do not address algorithmic personalized pricing.

**Unit pricing pilot (September 2025).** The CCCS launched a unit pricing pilot at major supermarkets (NTUC FairPrice, Sheng Siong, Prime Supermarket, Cold Storage, Giant) across more than 150 outlets, displaying price-per-unit for selected grocery categories. This is a disclosure initiative aimed at enabling price comparison across product sizes — a basic transparency measure that does not touch algorithmic pricing.

**Primary**: [CPFTA 2003 (Singapore Statutes Online)](https://sso.agc.gov.sg/act/cpfta2003); [CCCS, Guidelines on Price Transparency](https://www.cccs.gov.sg/consumer-protection/legislation-and-guidelines/guidelines-on-price-transparency); [CCCS, "Unit Pricing Pilot Launches at Major Supermarkets" (Sept 2025)](https://www.cccs.gov.sg/media-and-events/newsroom/announcements-and-media-releases/unit-pricing-pilot-launches-at-major-supermarkets-from-september-2025)

**Secondary**: [Allen & Gledhill, "CCCS Guidelines on Price Transparency Effective 1 November 2020"](https://www.allenandgledhill.com/sg/publication/articles/16741/cccs-guidelines-on-price-transparency-effective-1-november-2020); [Bird & Bird, "CCCS Publishes New Guidelines on Price Transparency" (2020)](https://www.twobirds.com/en/insights/2020/singapore/competition-and-consumer-commission-of-singapore-cccs-publishes-new-guidelines-on-price-transparency); [SingaporeLegalAdvice.com, "Price Transparency Guidelines by CCCS"](https://singaporelegaladvice.com/law-articles/price-transparency-guidelines-cccs/); [Rajah & Tann, "Consumer Protection Enforcement and Regulatory Updates in Singapore"](https://www.rajahtannasia.com/viewpoints/consumer-protection-enforcement-and-regulatory-updates-in-singapore/); [Rajah & Tann, "Consumer Protection in Singapore: Five Key Observations for Businesses in a Heightened Enforcement Climate"](https://www.rajahtannasia.com/viewpoints/consumer-protection-in-singapore-five-key-observations-for-businesses-in-a-heightened-enforcement-climate/)

### Competition Act 2004 — Sections 34 and 47

Section 34 prohibits anti-competitive agreements between undertakings. Section 47 prohibits abuse of a dominant position. Both are modeled on EU TFEU Articles 101/102 but with notable differences.

**Section 34 and algorithmic collusion.** The CCCS's 2020 E-commerce Platforms Market Study noted that AI or algorithms used to support or facilitate pre-existing or intended anti-competitive agreements would infringe section 34. The revised Competition Guidelines (effective February 1, 2022), informed by the market study, called for "further study and monitoring" of algorithmic collusion — particularly scenarios where algorithms align market behavior without prior communication among competitors. The CCCS has also announced it is developing (with IMDA) an AI Markets (AIM) Toolkit — integrated as a plugin within AI Verify — for organizations to test their AI systems for potential anticompetitive behavior, including algorithms that recommend prices leading to collusive outcomes.

**Section 47 and pricing discrimination.** Section 47 lists "applying dissimilar conditions to equivalent transactions" as a potential abuse. However, unlike TFEU Art. 102, section 47 makes no reference to "unfair prices" or "unfair trading conditions." The CCCS Guidelines clarify that discrimination is not abusive per se — it constitutes abuse only insofar as it results in exclusionary or foreclosure effects. Consumer-facing personalized pricing by a dominant firm would need to demonstrate exclusionary harm to competition, not merely exploitative harm to consumers, for section 47 to apply.

**No enforcement on algorithmic pricing.** As of February 2026, the CCCS has not brought any enforcement action targeting algorithmic pricing, algorithmic collusion, or personalized pricing. The AIM Toolkit and the monitoring commitment in the revised guidelines represent preparatory institutional capacity, not enforcement.

**Primary**: [Competition Act 2004 (Singapore Statutes Online)](https://sso.agc.gov.sg/act/ca2004); [CCCS, "Market Study on E-Commerce Platforms" (Sept 2020)](https://www.cccs.gov.sg/resources/publications/market-studies/market-study-on-e-commerce-platforms); [CCCS, "Revised Competition Guidelines" (eff. Feb 1, 2022)](https://www.cccs.gov.sg/media-and-events/newsroom/announcements-and-media-releases/cccs-revises-competition-guidelines-for-greater-clarity-and-guidance)

**Secondary**: [Lexology, "Prospective Refinements to CCCS' Competition Guidelines in 2021"](https://www.lexology.com/library/detail.aspx?g=7021d3c3-e88a-4271-9535-602223a94168); [Norton Rose Fulbright, "Keeping with the Times: CCCS Updates Competition Guidelines"](https://www.nortonrosefulbright.com/en/knowledge/publications/62221c11/keeping-with-the-times-cccs-updates-competition-guidelines-and-issues-guidance-note-for-businesses); [Chambers, "Cartels 2025 — Singapore"](https://practiceguides.chambers.com/practice-guides/cartels-2025/singapore/trends-and-developments); [Global Legal Insights, "AI, Machine Learning & Big Data Laws 2025: Singapore"](https://www.globallegalinsights.com/practice-areas/ai-machine-learning-and-big-data-laws-and-regulations/singapore/)

### MAS FEAT Principles (November 2018) and Veritas Initiative (2019-2022)

The Monetary Authority of Singapore published the Principles to Promote Fairness, Ethics, Accountability and Transparency (FEAT) in the Use of AI and Data Analytics in Singapore's Financial Sector in November 2018 — among the earliest financial sector-specific AI governance frameworks globally.

**Fairness principles.** FEAT Fairness requires that "individuals or groups of individuals are not systematically disadvantaged through AIDA-driven decisions, unless these decisions can be justified." Data and models must be "regularly reviewed and validated for accuracy and relevance, and to minimize unintentional bias." Applied to insurance pricing or credit decisions, these principles address the risk that algorithmic pricing produces discriminatory outcomes — but as voluntary principles, not binding rules.

**Veritas Initiative.** MAS worked with industry partners to create the Veritas framework (launched 2019), enabling financial institutions to evaluate AI/data analytics solutions against FEAT. In Phase 2 (published January 2022), Swiss Re and Accenture applied the Fairness Assessment Methodology to insurance predictive underwriting — the closest the Singapore framework comes to addressing algorithmic pricing in financial services. The methodology assesses whether underwriting and pricing models systematically disadvantage individuals, but adoption is voluntary.

**MAS Proposed Guidelines on AI Risk Management (consultation Nov 2025).** MAS issued a consultation paper on November 13, 2025 proposing Guidelines on AI Risk Management for all financial institutions. The proposed guidelines set supervisory expectations on AI risk management systems, policies, procedures, and lifecycle controls, with a proportionate approach based on scale and risk. If finalized, these would represent a shift from purely voluntary principles toward supervisory expectations — still not binding rules, but creating regulatory pressure. MAS proposes a 12-month transition period after issuance. The consultation closed January 31, 2026.

**Fair Dealing Guidelines (updated May 30, 2024).** MAS updated its Fair Dealing guidelines to apply to all financial institutions on a proportionate basis. These require fair treatment of customers but do not specifically address algorithmic pricing.

**What none of these instruments require.** No MAS instrument prohibits algorithmic pricing discrimination in insurance or financial services. No instrument requires disclosure of personalized pricing to consumers. No instrument provides consumers a right to challenge algorithmic pricing decisions. The UK's FCA banned price walking in insurance; Singapore's MAS asks financial institutions to voluntarily assess their AI systems for fairness. The contrast is stark.

**Primary**: [MAS, "FEAT Principles" (Nov 2018)](https://www.mas.gov.sg/publications/monographs-or-information-paper/2018/feat); [MAS, Veritas Initiative](https://www.mas.gov.sg/schemes-and-initiatives/veritas); [MAS, "Consultation Paper on Proposed Guidelines on AI Risk Management" (Nov 2025)](https://www.mas.gov.sg/publications/consultations/2025/consultation-paper-on-guidelines-on-artificial-intelligence-risk-management)

**Secondary**: [K&L Gates, "Managing Artificial Intelligence: MAS Recommendations on AI Model Risk Management" (Jan 2025)](https://www.klgates.com/Managing-Artificial-Intelligence-The-Monetary-Authority-of-Singapores-Recommendations-on-AI-Model-Risk-Management-1-22-2025); [Stephenson Harwood, "Understanding the MAS Consultation Paper on AI Risk Management"](https://www.stephensonharwood.com/insights/understanding-the-mas-consultation-paper-on-ai-risk-management-for-financial-institutions/); [Rajah & Tann, "Veritas Phase 2: FEAT Principles"](https://www.rajahtannasia.com/wp-content/uploads/2024/10/2022-02_Veritas_Phase_2-FEAT_principles.pdf); [Genesis Human Experience, "Responsible AI in Insurance: Beyond Compliance to Trust" (Sept 2025)](https://genesishumanexperience.com/2025/09/06/responsible-ai-in-insurance/)

## Analysis

**Hierarchy.** Self-regulation dominates. The Model AI Governance Framework, the PDPC AI Advisory Guidelines, the FEAT Principles, and the Veritas Initiative are all voluntary instruments that establish norms for AI governance without creating binding obligations. The binding instruments — the PDPA, the CPFTA, the Competition Act — are general-purpose laws that were not designed for and have not been applied to algorithmic pricing. The hierarchy is therefore: self-regulation as the primary strategy for AI-related governance, with general-purpose disclosure (CPFTA/price transparency guidelines) and competition law (Competition Act ss. 34, 47) as background instruments that could theoretically reach pricing practices but have not done so. No instrument occupies the prohibition end of the spectrum.

**Design logic.** Unified. Unlike the UK (differentiated — different strategies for different sectors) or the EU (accumulated — different instruments from different eras with different logics), Singapore's approach is philosophically coherent: voluntary, principles-based governance across all sectors, with binding law confined to general-purpose frameworks. This is a deliberate design choice, not an accumulation of instruments. The PDPC, IMDA, MAS, and CCCS all operate within the same philosophical frame — pro-innovation, industry-led governance, with state enforcement reserved for clear violations of general law. The coherence is notable because Singapore has multiple regulators (PDPC for data protection, CCCS for competition and consumer protection, MAS for financial services, IMDA for technology governance) that could have developed divergent approaches — but they have not. The AI governance architecture is coordinated: the Model Framework feeds into the PDPC Advisory Guidelines, which complement the FEAT Principles, which are operationalized through Veritas, which is being connected to AI Verify through the AIM Toolkit. The system is designed as an integrated voluntary architecture rather than a patchwork of binding rules.

**Institution relied on — divergence.** Singapore's self-regulatory instruments theoretically rely on the market — firms voluntarily adopt governance principles, and market trust rewards compliance. But the operative institution is actually the state, acting as convener rather than enforcer. MAS convened the Veritas consortium. IMDA developed AI Verify. PDPC issued the advisory guidelines. CCCS built the AIM Toolkit. The state designs the voluntary frameworks and provides the testing tools; industry adopts them. This is a distinctive institutional model — neither market-led self-regulation (where industry creates its own standards, as in the UK's pro-innovation framework) nor state-led enforcement (where the regulator imposes rules and penalizes violations). It is state-orchestrated voluntary governance — the state sets the parameters and builds the infrastructure, but compliance remains optional. For surveillance pricing specifically, this means the institutional actor with the most capacity to address algorithmic pricing (the state) has chosen to provide tools and principles rather than rules and enforcement.

## Evidence

**No enforcement on algorithmic pricing.** As of February 2026, no Singapore regulator has brought any enforcement action, investigation, or inquiry specifically targeting algorithmic personalized pricing. The PDPC has not enforced the PDPA against personalized pricing. The CCCS has not applied the CPFTA or Competition Act to algorithmic pricing. MAS has not taken supervisory action against algorithmic pricing in financial services. The enforcement record is entirely blank for this specific practice.

**CCCS consumer protection enforcement (2024-2025) — pricing-adjacent but not personalized pricing.** The CCCS has intensified consumer protection enforcement under its new Chief Executive (April 2024), targeting dark patterns, fake reviews, subscription traps, and misleading pricing practices. Notable actions include enforcement against a food delivery platform for misleading "unlimited free delivery" claims (November 2024), fake review investigations (including an AI-generated reviews case, July 2025), and hair salon price concealment. These demonstrate operational capacity and willingness to address pricing transparency, but none targets personalized pricing specifically. [Rajah & Tann, "Consumer Protection in Singapore: Five Key Observations for Businesses in a Heightened Enforcement Climate"](https://www.rajahtannasia.com/viewpoints/consumer-protection-in-singapore-five-key-observations-for-businesses-in-a-heightened-enforcement-climate/)

**CCCS E-commerce Market Study (September 2020) — no major concerns found.** The CCCS market study on e-commerce platforms identified "personalised pricing that is discriminatory" as a potential theory of harm but concluded that it "did not identify any current major competition concerns involving e-commerce platforms in Singapore." This finding — no current problem — may partly explain the absence of targeted regulation. [CCCS, "Market Study on E-Commerce Platforms" (Sept 2020)](https://www.cccs.gov.sg/resources/publications/market-studies/market-study-on-e-commerce-platforms)

**MAS Veritas Phase 2 — insurance underwriting tested, not pricing.** The Veritas Initiative's Phase 2 applied the FEAT Fairness Assessment Methodology to insurance predictive underwriting (with Swiss Re). This represents the most proximate evidence of Singapore's voluntary governance architecture being applied to an area adjacent to algorithmic pricing. But underwriting risk assessment is not the same as personalized pricing; the Veritas exercise did not test insurer pricing algorithms for discriminatory outcomes. [MAS, Veritas Initiative](https://www.mas.gov.sg/schemes-and-initiatives/veritas)

**AI Verify and AIM Toolkit — infrastructure built, usage data unavailable.** The CCCS AIM Toolkit, integrated as a plugin in AI Verify, enables businesses to self-assess AI models for anticompetitive risks including pricing algorithms that may lead to collusive outcomes. No public data is available on adoption rates, number of firms using the toolkit, or outcomes of self-assessments. The tool exists; its impact is unknown. [Global Legal Insights, "AI, Machine Learning & Big Data Laws 2025: Singapore"](https://www.globallegalinsights.com/practice-areas/ai-machine-learning-and-big-data-laws-and-regulations/singapore/)

## Movement

Singapore's trajectory is steady-state: it has progressively built out its voluntary AI governance infrastructure without crossing into binding regulation for any AI application, including pricing.

1. **November 2018**: MAS publishes FEAT Principles — among the earliest financial sector AI governance frameworks globally
2. **January 2019**: PDPC/IMDA publish Model AI Governance Framework (first edition)
3. **January 2020**: Model AI Governance Framework second edition — adds robustness and reproducibility considerations
4. **September 2020**: CCCS publishes E-commerce Platforms Market Study — identifies personalized pricing as potential theory of harm but finds no current concerns; recommends update to competition guidelines
5. **November 2020**: CCCS Guidelines on Price Transparency take effect — addresses drip pricing, not personalized pricing
6. **2019-2022**: MAS Veritas Initiative Phases 1-3 — develops assessment methodologies for FEAT Principles in financial services
7. **May 2022**: IMDA launches AI Verify — open-source testing toolkit for AI governance principles
8. **February 2022**: CCCS revised Competition Guidelines take effect — notes need for monitoring of algorithmic collusion, calls for further study
9. **March 2024**: PDPC issues Advisory Guidelines on Use of Personal Data in AI Recommendation and Decision Systems — clarifies PDPA application to AI, but non-binding and does not address pricing
10. **June/September 2024**: CCCS announces development of AIM Toolkit (with IMDA) for testing AI systems for anticompetitive behavior, integrated into AI Verify
11. **May 2024**: MAS updates Fair Dealing Guidelines — applicable to all financial institutions
12. **November 2025**: MAS issues consultation paper on proposed Guidelines on AI Risk Management for financial institutions — closest approach to binding AI governance (supervisory expectations, not rules)
13. **July 2025**: CCCS expands consumer protection mandate under Competition (Amendment) Act 2025

The trajectory is notably linear and consistent. There is no inflection point, no sector-specific intervention, no legislative proposal targeting algorithmic pricing. Singapore has built more voluntary governance infrastructure than almost any other jurisdiction in the survey, but has moved less toward binding regulation. The contrast with the UK is instructive: the UK started with a similar pro-innovation voluntary philosophy (2023 White Paper) but produced a sector-specific binding prohibition (FCA price walking ban, 2022 — actually preceding the White Paper) and new direct enforcement powers (DMCCA 2024). Singapore has maintained philosophical consistency: voluntary governance throughout, with no sector-specific departure.

The MAS proposed AI Risk Management Guidelines (November 2025 consultation) represent the most significant potential shift — from voluntary principles to supervisory expectations. If finalized, this would not create binding rules but would move the financial sector closer to enforceable governance. Whether this presages a broader shift from voluntarism remains to be seen.

## Open Questions

1. **Will MAS finalize the AI Risk Management Guidelines, and will they address pricing?** The consultation closed January 31, 2026. If the final guidelines include supervisory expectations on AI-driven pricing in financial services, this would be Singapore's first instrument with regulatory pressure on algorithmic pricing — even if it remains below the threshold of binding law.
2. **Will the CCCS extend its enforcement focus to personalized pricing?** The CCCS has intensified consumer protection enforcement (2024-2025), but exclusively against drip pricing, dark patterns, and misleading practices. The 2020 market study found no major concerns about personalized pricing in e-commerce. Has the landscape changed? Will the CCCS revisit?
3. **What is the adoption rate of voluntary frameworks?** Singapore's governance architecture is built on voluntary adoption, but no public data exists on how many firms have adopted the Model AI Governance Framework, used AI Verify for fairness testing, or applied FEAT Principles to pricing algorithms. Without adoption data, the effectiveness of the voluntary strategy is unknown.
4. **How does the AIM Toolkit work in practice?** The CCCS AIM Toolkit tests for anticompetitive pricing behavior, but no public information exists on its methodology, test results, or adoption. Is it used by firms operating pricing algorithms? Has it detected anticompetitive pricing patterns?
5. **Will Singapore's approach diverge from or converge with regional peers?** South Korea has enacted dark pattern regulation (E-Commerce Act, February 2025) and is considering the Online Platform Fairness Act. China has prohibited algorithmic price discrimination (Rules for Price Behavior, effective April 2026). Singapore's ASEAN neighbors Indonesia and Thailand are strengthening platform regulation. Will regional movement create pressure for Singapore to move beyond voluntarism?
6. **Does the PDPA's consent framework provide an adequate check on surveillance pricing?** The PDPA requires consent for data use, but organizations draft purpose statements broadly. Does "personalization of services" or "improvement of customer experience" as a stated purpose effectively consent individuals to personalized pricing? The PDPC has not clarified.
7. **Insurance pricing fairness gap.** MAS FEAT Principles address fairness in AI-driven financial decisions, but no binding rule prevents discriminatory algorithmic pricing in insurance. Unlike the UK's FCA price walking ban, Singapore has no sector-specific prohibition. Is there evidence of insurance price walking or algorithmic discrimination in Singapore's market?

## Sources

**Primary**:
- [PDPA 2012 (Singapore Statutes Online)](https://sso.agc.gov.sg/Act/PDPA2012)
- [Competition Act 2004 (Singapore Statutes Online)](https://sso.agc.gov.sg/act/ca2004)
- [CPFTA 2003 (Singapore Statutes Online)](https://sso.agc.gov.sg/act/cpfta2003)
- [PDPC, Advisory Guidelines on Use of Personal Data in AI Recommendation and Decision Systems (March 2024)](https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems)
- [PDPC, Model AI Governance Framework (Second Edition, Jan 2020)](https://www.pdpc.gov.sg/help-and-resources/2020/01/model-ai-governance-framework)
- [CCCS, Guidelines on Price Transparency (eff. Nov 2020)](https://www.cccs.gov.sg/consumer-protection/legislation-and-guidelines/guidelines-on-price-transparency)
- [CCCS, "Market Study on E-Commerce Platforms" (Sept 2020)](https://www.cccs.gov.sg/resources/publications/market-studies/market-study-on-e-commerce-platforms)
- [CCCS, Revised Competition Guidelines (eff. Feb 2022)](https://www.cccs.gov.sg/media-and-events/newsroom/announcements-and-media-releases/cccs-revises-competition-guidelines-for-greater-clarity-and-guidance)
- [MAS, FEAT Principles (Nov 2018)](https://www.mas.gov.sg/publications/monographs-or-information-paper/2018/feat)
- [MAS, Veritas Initiative](https://www.mas.gov.sg/schemes-and-initiatives/veritas)
- [MAS, "Consultation Paper on Proposed Guidelines on AI Risk Management" (Nov 2025)](https://www.mas.gov.sg/publications/consultations/2025/consultation-paper-on-guidelines-on-artificial-intelligence-risk-management)
- [MAS, "Guidelines on Fair Dealing" (updated May 2024)](https://www.mas.gov.sg/regulation/regulations-and-guidance)
- [IMDA, AI Verify](https://www.imda.gov.sg/about-imda/emerging-technologies-and-research/artificial-intelligence)
- [CCCS, "Unit Pricing Pilot Launches at Major Supermarkets" (Sept 2025)](https://www.cccs.gov.sg/media-and-events/newsroom/announcements-and-media-releases/unit-pricing-pilot-launches-at-major-supermarkets-from-september-2025)

**Secondary**:
- [Bird & Bird, "PDPC Advisory Guidelines on the Use of Personal Data in AI Recommendation and Decision Systems" (2024)](https://www.twobirds.com/en/insights/2024/singapore/pdpc-advisory-guidelines-on-the-use-of-personal-data-in-ai-recommendation-and-decision-systems)
- [Norton Rose Fulbright, "Singapore Releases New Guidelines on the Use of Personal Data in AI Systems" (March 2024)](https://www.nortonrosefulbright.com/en/inside-fintech/blog/2024/03/singapore-releases-new-guidelines-on-the-use-of-personal-data-in-ai-systems)
- [Rajah & Tann, "PDPC Issues Advisory Guidelines on Use of Personal Data in AI Recommendation and Decision Systems"](https://www.rajahtannasia.com/viewpoints/pdpc-issues-advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems/)
- [Rajah & Tann, "Consumer Protection in Singapore: Five Key Observations for Businesses in a Heightened Enforcement Climate"](https://www.rajahtannasia.com/viewpoints/consumer-protection-in-singapore-five-key-observations-for-businesses-in-a-heightened-enforcement-climate/)
- [Rajah & Tann, "Consumer Protection Enforcement and Regulatory Updates in Singapore"](https://www.rajahtannasia.com/viewpoints/consumer-protection-enforcement-and-regulatory-updates-in-singapore/)
- [Allen & Gledhill, "CCCS Guidelines on Price Transparency Effective 1 November 2020"](https://www.allenandgledhill.com/sg/publication/articles/16741/cccs-guidelines-on-price-transparency-effective-1-november-2020)
- [Bird & Bird, "CCCS Publishes New Guidelines on Price Transparency" (2020)](https://www.twobirds.com/en/insights/2020/singapore/competition-and-consumer-commission-of-singapore-cccs-publishes-new-guidelines-on-price-transparency)
- [Lexology, "Prospective Refinements to CCCS' Competition Guidelines in 2021"](https://www.lexology.com/library/detail.aspx?g=7021d3c3-e88a-4271-9535-602223a94168)
- [Norton Rose Fulbright, "Keeping with the Times: CCCS Updates Competition Guidelines"](https://www.nortonrosefulbright.com/en/knowledge/publications/62221c11/keeping-with-the-times-cccs-updates-competition-guidelines-and-issues-guidance-note-for-businesses)
- [K&L Gates, "Managing Artificial Intelligence: MAS Recommendations on AI Model Risk Management" (Jan 2025)](https://www.klgates.com/Managing-Artificial-Intelligence-The-Monetary-Authority-of-Singapores-Recommendations-on-AI-Model-Risk-Management-1-22-2025)
- [Stephenson Harwood, "Understanding the MAS Consultation Paper on AI Risk Management"](https://www.stephensonharwood.com/insights/understanding-the-mas-consultation-paper-on-ai-risk-management-for-financial-institutions/)
- [Global Legal Insights, "AI, Machine Learning & Big Data Laws 2025: Singapore"](https://www.globallegalinsights.com/practice-areas/ai-machine-learning-and-big-data-laws-and-regulations/singapore/)
- [Chambers, "Artificial Intelligence 2025 — Singapore"](https://practiceguides.chambers.com/practice-guides/artificial-intelligence-2025/singapore/trends-and-developments)
- [ICLG, "Data Protection Laws and Regulations 2025-2026: Singapore"](https://iclg.com/practice-areas/data-protection-laws-and-regulations/singapore)
- [ICLG, "Consumer Protection Laws and Regulations 2025-2026: Singapore"](https://iclg.com/practice-areas/consumer-protection-laws-and-regulations/singapore)
- [IAPP, "Global AI Governance Law and Policy: Singapore"](https://iapp.org/resources/article/global-ai-governance-singapore)
- [Future of Privacy Forum, "AI Verify: Singapore's AI Governance Testing Initiative Explained"](https://fpf.org/blog/ai-verify-singapores-ai-governance-testing-initiative-explained/)
- [Turing Institute, "AI Governance Around the World: Singapore" (Aug 2025)](https://www.turing.ac.uk/sites/default/files/2025-09/ai_governance_around_the_world_singapore.pdf)
- [Osborne Clarke, "Singapore's Competition Regulator Sets Out New Guidelines on Price Transparency"](https://www.osborneclarke.com/insights/singapores-competition-regulator-sets-new-guidelines-price-transparency)
- [Genesis Human Experience, "Responsible AI in Insurance: Beyond Compliance to Trust" (Sept 2025)](https://genesishumanexperience.com/2025/09/06/responsible-ai-in-insurance/)

**Library**:
- [[intel-comparative-regulation]]
- [[surveillance-pricing-comparative-regulation]]
- [[baldwin-regulatory-strategies]]
- [[disclosure-regulation]]
- [[self-regulation]]
- [[competition-over-regulation]]
- [[rights-and-liabilities-regulation]]
- [[regulatory-topology-not-ladder]]
- [[government-capacities-regulation]]
- [[sp-uk]]
- [[sp-eu]]
- [[sp-china]]
- [[sp-new-york]]
- [[sp-california]]
