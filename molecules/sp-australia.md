---
date-created: "202602251800"
aliases:
  - "Australia surveillance pricing profile"
tags:
  - "#molecules"
  - "#jurisdiction-profile"
topic:
  - "[[surveillance pricing]]"
  - "[[Australia]]"
---

# Australia — Surveillance Pricing Regulatory Profile

*Jurisdiction molecule for [[surveillance-pricing-comparative-regulation|Paper 1]].*

Australia's regulatory profile is defined by the gap between analytical recognition and legislative response. The ACCC's five-year Digital Platform Services Inquiry (2020–2025, final report June 2025) produced comprehensive analysis of algorithmic pricing risks and recommended an economy-wide unfair trading practices prohibition — a recommendation now moving toward legislation through the Competition and Consumer Amendment (Unfair Trading Practices) Bill 2026 (exposure draft February 2026, proposed effective date July 2027). In the interim, the operative instruments are general-purpose: the Australian Consumer Law's misleading conduct prohibition (ACL s.18) and the Competition and Consumer Act's anti-competitive agreement provisions (CCA s.45), neither of which was designed for algorithmic personalized pricing. What distinguishes Australia is the enforcement intensity on pricing-adjacent conduct — ACCC and ASIC have pursued drip pricing (Webjet AUD 9M penalty), illusory discounts (Coles/Woolworths proceedings), and insurance loyalty pricing (IAG AUD 40M penalty, QBE proceedings ongoing) — demonstrating institutional capacity and willingness to address pricing practices through existing law, while targeted instruments for personalized pricing remain prospective.

## Instruments

| Instrument | Strategy | Sector | Status | Enforcement |
|-----------|----------|--------|--------|-------------|
| ACL s.18 (misleading or deceptive conduct, eff. Jan 1, 2011) | Disclosure ([[disclosure-regulation]]) | General | Operative | ACCC; penalties up to AUD 50M or 3x benefit or 30% of adjusted turnover per contravention |
| ACL s.21 (unconscionable conduct) | Rights & liabilities ([[rights-and-liabilities-regulation]]) | General | Operative | ACCC; same penalty structure as s.18 |
| CCA s.45 (anti-competitive agreements and concerted practices, as amended 2017) | Competition ([[competition-over-regulation]]) | General | Operative | ACCC; criminal penalties for cartel conduct (10 years imprisonment, AUD 10M individual fine); civil pecuniary penalties |
| CCA s.46 (misuse of market power, as amended 2017) | Competition ([[competition-over-regulation]]) | General | Operative | ACCC; civil pecuniary penalties |
| ACCC Digital Platform Services Inquiry (2020-2025, final report June 2025) | Study / recommendations | Digital platforms | Complete | Non-binding; informs legislative agenda |
| Competition and Consumer Amendment (Unfair Trading Practices) Bill 2026 (exposure draft Feb 2026) | Disclosure / prohibition (hybrid) | General (consumer transactions) | Proposed (consultation closed Feb 23, 2026; proposed eff. July 1, 2027) | ACCC; penalties up to AUD 50M or 3x benefit or 30% of adjusted turnover |
| Privacy Act 1988 — APP 1 reform (ADM transparency, eff. Dec 10, 2026) | Disclosure ([[disclosure-regulation]]) | General | Enacted (not yet operative) | OAIC; infringement notice regime |
| ASIC enforcement on insurance pricing (IAG, QBE, RACQ — 2023-ongoing) | Disclosure (enforcement via misleading conduct) | Insurance | Operative (enforcement actions ongoing) | ASIC; Federal Court penalties (IAG AUD 40M, RACQ AUD 10M, QBE trial April 2026) |
| AI mandatory guardrails consultation (Sept 2024) / National AI Plan (Dec 2025) | Self-regulation (moving toward regulation) | General (high-risk AI settings) | Proposed (consultation complete; no legislation) | AI Safety Institute (established Nov 2025; operational early 2026) |

## Detail

### ACL s.18 — Misleading or Deceptive Conduct (eff. Jan 1, 2011)

Section 18 of the Australian Consumer Law (Schedule 2 of the Competition and Consumer Act 2010) provides a broad prohibition: "A person must not, in trade or commerce, engage in conduct that is misleading or deceptive or is likely to mislead or deceive." This is the workhorse provision of Australian consumer protection — applicable to any pricing practice that creates a false impression, regardless of intent.

**Application to pricing.** Section 18 has been deployed against drip pricing and illusory discounts, establishing an active enforcement pattern on pricing transparency:

- **Webjet (2025).** The Federal Court imposed a AUD 9 million penalty for displaying airfares without disclosing compulsory fees (2018-2023) and representing bookings as confirmed when they were not (2019-2024). The Court described the conduct as "serious and wide-reaching." Webjet admitted liability in February 2025.
- **Dendy Cinemas (2025).** The ACCC issued an infringement notice with a AUD 19,800 penalty for failing to prominently display total ticket prices inclusive of booking fees — a classic drip pricing case.
- **Coles and Woolworths (2024-ongoing).** The ACCC commenced separate Federal Court proceedings against both supermarket chains for marketing products as "Prices Dropped" or "Down Down" after temporarily increasing prices — creating illusory discounts on at least 245 products (Coles) and 266 products (Woolworths) between 2021-2023. These are the largest consumer protection enforcement actions in Australian retail history. No penalties imposed yet; Woolworths hearing scheduled April 2026.

**What it does NOT cover.** Section 18 requires that conduct be misleading or deceptive — it does not prohibit unfair conduct that is not misleading. Personalized pricing that is disclosed (or simply not accompanied by false claims) does not violate s.18. There is no obligation to disclose that prices are personalized, no prohibition on algorithmic price discrimination, and no requirement for pricing transparency beyond avoiding affirmatively false representations. This gap — between misleading pricing (reached by s.18) and unfair pricing (not reached by current law) — is precisely what the proposed Unfair Trading Practices Bill seeks to close.

**Primary**: [Competition and Consumer Act 2010, Schedule 2 (Australian Consumer Law)](https://www.legislation.gov.au/C2004A01468/latest/text); [ACCC v Webjet (Federal Court, 2025)](https://www.accc.gov.au/media-release/webjet-penalty); [ACCC v Coles/Woolworths (Federal Court, proceedings commenced Sept 2024)](https://www.accc.gov.au/media-release/accc-takes-woolworths-and-coles-to-court-over-alleged-misleading-prices-dropped-and-down-down-claims)

**Secondary**: [King & Wood Mallesons, "Hidden Fares and Hollow Confirmations: ACCC Grounds Webjet" (2025)](https://pulse.kwm.com/in-competition/hidden-fares-and-hollow-confirmations-accc-grounds-webjet/); [King & Wood Mallesons, "Fee-ling Misled: ACCC Cracks Down on Dendy Cinema Drip Pricing" (2025)](https://pulse.kwm.com/in-competition/fee-ling-misled-accc-cracks-down-on-dendy-cinema-drip-pricing/); [Holding Redlich, "Down, Down… to Court We Go: Coles and Woolworths in Hot Water over 'Price Drops'" (2024)](https://www.holdingredlich.com/down-down-to-court-we-go-coles-and-woolworths-in-hot-water-over-price-drops)

### ACCC Digital Platform Services Inquiry (2020–2025)

The ACCC conducted a five-year inquiry into the supply of digital platform services, producing interim reports on specific topics (search, social media, app stores, ad tech, online marketplaces) and a final report released on 23 June 2025.

**Final report findings.** The final report examined competition and consumer issues across digital platform services and identified algorithmic pricing as an area of emerging concern. The report flagged that generative AI tools could enable collusive or anti-competitive behaviours including algorithmic price-fixing, and noted risks from algorithmic coordination, access to data, and lack of transparency in automated decision-making as AI tools become integrated into commercial operations.

**Six key recommendations.** (1) Introduce an economy-wide prohibition on unfair trading practices and strengthen unfair contract terms laws. (2) Introduce digital platform-specific consumer protections. (3) Empower the ACCC to create mandatory, targeted, service-specific codes of conduct for designated digital platforms. (4) Include targeted competition obligations in those codes to address anti-competitive conduct. (5) Enable the ACCC to have an ongoing monitoring function for emerging digital technologies. (6) Establish and resource the Digital Platform Regulators Forum (DP-REG) as a permanent forum.

**Significance for surveillance pricing.** The DPSI's primary contribution to the topology is the unfair trading practices recommendation — which has now progressed to the exposure draft stage (February 2026). The inquiry also informed the ACCC's enforcement priorities: drip pricing was designated as an enforcement and compliance priority for 2025-26. The inquiry represents the most comprehensive study of digital platform pricing practices by any regulator in the dataset, but its five-year duration also illustrates the gap between regulatory analysis and legislative action.

**Primary**: [ACCC, Digital Platform Services Inquiry Final Report (March 2025)](https://www.accc.gov.au/about-us/publications/serial-publications/digital-platform-services-inquiry-2020-25-reports/digital-platform-services-inquiry-final-report-march-2025)

**Secondary**: [Clifford Chance, "From Inquiry to Action: The Final DPSI Report and the Future for Digital Platforms in Australia" (July 2025)](https://www.cliffordchance.com/insights/resources/blogs/antitrust-fdi-insights/2025/07/final-dpsi-report-and-future-for-digital-platforms-in-australia.html); [Bird & Bird, "Six Key Recommendations from Australia's Final Digital Platform Services Inquiry Report" (2025)](https://www.twobirds.com/en/insights/2025/australia/six-key-recommendations-from-australias-final-digital-platform-services-inquiry-report)

### Competition and Consumer Amendment (Unfair Trading Practices) Bill 2026

On 9 February 2026, Treasury released an exposure draft of the Competition and Consumer Amendment (Unfair Trading Practices) Bill 2026, proposing amendments to the ACL. Consultation closed on 23 February 2026. If passed, the changes are proposed to take effect from 1 July 2027.

**General prohibition on unfair trading practices.** The Bill proposes a broad prohibition: a contravention arises where conduct does (or is likely to) unreasonably manipulate a consumer, or unreasonably distort the environment in which a consumer makes a decision, and causes or is likely to cause detriment (financial or otherwise) to the consumer. This is a significant expansion of the ACL — s.18 requires conduct to be misleading; the proposed prohibition reaches conduct that is merely unfair.

**Drip pricing.** The Bill includes specific protections against drip pricing — requiring display of total prices inclusive of mandatory fees. This codifies what the ACCC has been pursuing through s.18 enforcement.

**Unfair subscription practices.** The Bill targets hidden renewals, cancellation obstruction, and other subscription traps — paralleling the EU's unfair commercial practices approach and South Korea's E-Commerce Act dark pattern provisions.

**Scope.** Limited to consumer transactions (B2C). Does not extend to business-to-business conduct, though the Government has foreshadowed considering B2B extension.

**Penalties.** For body corporates: the greater of AUD 50 million, 3x the value of any benefit, or 30% of adjusted turnover during the breach period. For individuals: AUD 2.5 million.

**Application to personalized pricing.** The critical question is whether algorithmic personalized pricing could constitute "unreasonably manipulating a consumer" or "unreasonably distorting the environment" in which a pricing decision is made. The Bill does not specifically address personalized pricing, but the broad language — particularly "unreasonably distort the environment" — could theoretically reach personalized pricing if it is characterized as environmental distortion (the consumer sees a price environment shaped by their data, not the actual market). This interpretation is untested and depends on how courts construe the provision. The exposure draft materials do not discuss personalized pricing specifically.

**Primary**: [Treasury, Competition and Consumer Amendment (Unfair Trading Practices) Bill 2026 (Exposure Draft)](https://treasury.gov.au/consultation/c2026-t-unfair-trading-practices)

**Secondary**: [Allens, "Unfair Trading Practices: Treasury Unveils Blueprint for New Regime" (Feb 2026)](https://www.allens.com.au/insights-news/insights/2026/02/unfair-trading-practices-treasury-unveils-blueprint-for-new-regime/); [Baker McKenzie, "Australia: Proposed ACL Unfair Trading Reforms" (Feb 2026)](https://www.bakermckenzie.com/en/insight/publications/2026/02/australia-proposed-acl-unfair-trading-reforms); [Ashurst, "Play Fair: Unfair Trading Practices Ban Coming in 2026" (2026)](https://www.ashurst.com/en/insights/play-fair-unfair-trading-practices-ban-coming-in-2026/); [Gilbert + Tobin, "Dark Patterns to Face the Light of Day: Unfair Trading Practices Targeted in Proposed ACL Reforms" (2026)](https://www.gtlaw.com.au/insights/dark-patterns-to-face-the-light-of-day-unfair-trading-practices-targeted-in-proposed-acl-reforms)

### CCA s.45 — Anti-Competitive Agreements and Concerted Practices

Section 45 of the Competition and Consumer Act 2010 prohibits contracts, arrangements, or understandings that have the purpose or likely effect of substantially lessening competition. The 2017 Harper Reforms added a concerted practices prohibition (s.45(1)(c)), intended to address conduct falling short of an agreement — including algorithmic coordination.

**Concerted practices and algorithmic collusion.** A concerted practice "may exist even if none of the parties is obliged, either legally or morally, to act in any particular way." This was designed to capture tacit coordination that does not rise to the level of an agreement. Academic analysis (Balasingham 2020, Chan 2021) has examined whether this prohibition reaches algorithmic collusion. The prevailing view is that s.45(1)(c) likely still requires some form of communication between competitors — meaning tacit algorithmic collusion (where algorithms independently converge on supra-competitive prices without prior communication) likely falls outside the prohibition. The hub-and-spoke scenario (shared pricing algorithm) would likely be captured; autonomous algorithmic collusion would not.

**No enforcement on algorithmic pricing.** As of February 2026, the ACCC has not brought any enforcement action specifically targeting algorithmic pricing or algorithmic collusion. The concerted practices prohibition has not been tested in court in any context.

**Primary**: [Competition and Consumer Act 2010, s.45](https://www.legislation.gov.au/C2004A01468/latest/text)

**Secondary**: [Balasingham, "The Australian Competition and Consumer Act 2.0: Is the New Concerted Practices Prohibition an Effective Patch to Address Algorithmic Collusion?" (2020)](https://www.competitionpolicyinternational.com/wp-content/uploads/2020/07/9-The-Australian-Competition-and-Consumer-Act-2.0-Is-the-New-Concerted-Practices-Prohibition-an-Effective-Patch-to-Address-Algorithmic-Collusion-Baskaran-Balasingham.pdf); [Chan, "Algorithmic Collusion and Australian Competition Law" (2021) 44(4) UNSW Law Journal 1365](http://classic.austlii.edu.au/au/journals/UNSWLawJl/2021/47.html)

### Privacy Act 1988 — APP 1 Reform: ADM Transparency (eff. Dec 10, 2026)

The first tranche of Privacy Act reforms (passed 2025) amends APP 1 to require organisations to disclose in their privacy policies the use of automated decision-making that could "reasonably be expected to significantly affect the rights or interests of an individual."

**Scope.** The reform applies to any "computer program" — a broad term encompassing rule-based processes, AI, and machine learning — that makes decisions using personal information. "Making a decision" includes refusing or failing to make a decision, and the obligation applies regardless of whether the decision is beneficial or adverse.

**What is required.** Privacy policies must disclose: the kinds of personal information used in automated decisions, and the kinds of decisions made solely by computer programs. This is a transparency/disclosure obligation — it requires organisations to be transparent about the existence and nature of automated decision-making.

**What is NOT required.** There is no right to refuse automated decisions (contrast GDPR Art. 22, PIPA Art. 37-2). There is no right to human review. There is no right to contest an automated decision. There is no obligation to explain the logic of individual decisions. The reform requires disclosure in privacy policies — a systemic transparency measure — not individual-level rights against automated decisions. This positions the Australian reform as the weakest automated decision-making provision in the dataset: weaker than the EU (GDPR Art. 22 — right to refuse), weaker than South Korea (PIPA Art. 37-2 — right to refuse, though undermined by prior-consent exception), and weaker than the UK (UK GDPR Art. 22, even as narrowed by DUAA 2025).

**Commencement.** The ADM transparency obligation takes effect on 10 December 2026, providing organisations a 24-month compliance window. The OAIC has indicated that non-compliance could attract enforcement under its new infringement notice regime, given that privacy policy reviews are straightforward for the regulator.

**Primary**: [Privacy Act 1988 (as amended)](https://www.legislation.gov.au/C2004A03712/latest/text); [OAIC, APP 1 Guidelines (updated)](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-1-app-1-open-and-transparent-management-of-personal-information)

**Secondary**: [Helios Salinger, "How to Get Ahead of the New ADM Rules Before They Rule You" (July 2025)](https://www.heliossalinger.com.au/2025/07/01/how-to-get-ahead-of-the-new-adm-rules-before-they-rule-you/); [Jackson Whittle Saunders, "Practical Implications of the New Transparency Requirements for Automated Decision Making" (2025)](https://jws.com.au/what-we-think/practical-implications-of-new-transparency-requirements-for-automated-decision-making/); [Norton Rose Fulbright, "Australian Privacy Alert: Parliament Passes Major and Meaningful Privacy Law Reform" (2025)](https://www.nortonrosefulbright.com/en/knowledge/publications/be98b0ff/australian-privacy-alert-parliament-passes-major-and-meaningful-privacy-law-reform)

### ASIC Enforcement — Insurance Pricing (2023–ongoing)

ASIC has pursued a series of enforcement actions against insurers for misleading consumers about loyalty discounts — conduct functionally analogous to the "price walking" that the UK's FCA banned through PS21/5.

**IAG (AUD 40M penalty, 2024).** The Federal Court ordered Insurance Australia Group (IAG) to pay AUD 40 million for misleading home insurance customers about pricing discounts. Between January 2017 and December 2022, IAG renewed over one million home insurance policies under the SGIO, SGIC, and RACV brands, offering loyalty discounts that were eroded or eliminated by prior premium increases — customers were told they were receiving a discount when the net effect was a higher price.

**QBE (proceedings commenced October 2024, trial April 2026).** ASIC alleges QBE made misleading representations about discounts on general insurance products, affecting over 500,000 renewal notices to retirees, loyalty customers, shareholders, and multi-policy holders (July 2017 – September 2022). ASIC alleges QBE's pricing model eroded the stated discounts, in some cases to nil.

**RACQ (AUD 10M penalty).** RACQ paid AUD 10 million for similar misleading discount practices.

**Class actions.** IAG also faces a class action over loyalty pricing practices, launched in January 2025.

**Significance for surveillance pricing.** The ASIC enforcement actions target the same underlying problem as the UK's FCA price walking ban — insurers using data (tenure, switching propensity) to extract surplus from loyal customers — but through a fundamentally different regulatory strategy. The FCA prohibited the practice directly (command and control). ASIC uses the existing misleading conduct prohibition (ACL s.12DA, mirror of ACL s.18 for financial services) — the practice itself is not prohibited, but making false claims about discounts while price-walking is. This is disclosure-as-enforcement: the instrument doesn't prohibit algorithmic pricing, it prohibits lying about it. An insurer that price-walks without claiming to offer loyalty discounts would not violate current law.

**Primary**: [ASIC, "23-228MR: ASIC Alleges IAG Misled Home Insurance Customers on Pricing Discounts" (2023)](https://www.asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-228mr-asic-alleges-iag-misled-home-insurance-customers-on-pricing-discounts/); [ASIC, "24-234MR: ASIC Alleges QBE Misled Customers Over Pricing Discounts" (2024)](https://www.asic.gov.au/about-asic/news-centre/find-a-media-release/2024-releases/24-234mr-asic-alleges-qbe-misled-customers-over-pricing-discounts/)

**Secondary**: [Business Insurance Consulting, "IAG Faces New Class Action Over Loyalty Pricing" (Jan 2025)](https://businessinsuranceconsulting.com.au/2025/01/07/iag-faces-new-class-action-over-loyalty-pricing-what-australian-policyholders-need-to-know/); [Bastion Legal, "IAG Ordered to Pay $40 Million Penalty for Misleading Discount Promises" (2024)](https://www.bastionlegal.com.au/articles/iag-ordered-to-pay-40-million-penalty-for-misleading-discount-promises)

### AI Governance — Mandatory Guardrails Consultation and National AI Plan

**Mandatory guardrails proposals paper (September 2024).** The Department of Industry, Science and Resources released a proposals paper on mandatory guardrails for AI in high-risk settings. Ten proposed guardrails include accountability, risk management, data governance, testing, human control, user information, challenge mechanisms, and supply chain transparency. The consultation received 275 submissions. No binding legislation has resulted as of February 2026.

**National AI Plan (December 2025).** The Government launched the National AI Plan on 2 December 2025, focused on building AI capability and infrastructure while establishing safety frameworks.

**AI Safety Institute (November 2025).** The Australian AI Safety Institute was announced on 25 November 2025 and will become operational in early 2026. It will assess upstream risks and downstream harms, support specialist regulators, and coordinate incident responses.

**Significance for surveillance pricing.** None of these instruments addresses algorithmic pricing. The mandatory guardrails are focused on safety, accountability, and transparency for high-risk AI — they do not regulate pricing practices. The AI Safety Institute is a monitoring body, not an enforcement body. The proposals paper does not identify algorithmic pricing as a high-risk setting. Australia's AI governance trajectory mirrors the UK's pro-innovation approach (principles first, sector regulators apply existing law) and Singapore's voluntary governance model (tools and frameworks, not rules). Whether the mandatory guardrails will eventually produce binding legislation that reaches pricing depends on forthcoming policy decisions.

**Primary**: [Department of Industry, Science and Resources, "Introducing Mandatory Guardrails for AI in High-Risk Settings" (Sept 2024)](https://consult.industry.gov.au/ai-mandatory-guardrails); [Department of Industry, Science and Resources, "National AI Plan" (Dec 2025)](https://www.industry.gov.au/publications/national-ai-plan)

**Secondary**: [Corrs Chambers Westgarth, "Australia Releases Proposed Mandatory Guardrails for AI Regulation" (2024)](https://www.corrs.com.au/insights/australia-releases-proposed-mandatory-guardrails-for-ai-regulation); [White & Case, "Australia's National AI Plan: Big Ambitions, But Light on Details" (2025)](https://www.whitecase.com/insight-alert/australias-national-ai-plan-big-ambitions-light-details); [Bird & Bird, "A New Era for AI Governance in Australia" (2025)](https://www.twobirds.com/en/insights/2025/australia/a-new-era-for-ai-governance-in-australia-what-the-national-ai-plan-means-for-industry)

## Analysis

**Hierarchy.** Disclosure dominates, deployed through enforcement rather than targeted legislation. The ACL s.18 misleading conduct prohibition is the operative instrument — it has produced the Webjet, Dendy, Coles/Woolworths, IAG, and RACQ enforcement outcomes. But s.18 can only reach pricing practices that involve affirmative misrepresentations; it cannot reach algorithmic personalized pricing that is simply undisclosed (as opposed to falsely described). The proposed Unfair Trading Practices Bill would expand the ACL beyond misleading conduct to unfair conduct — potentially closing this gap. Competition law (CCA ss.45-46) is present but has not been deployed against pricing. Self-regulation (AI guardrails) is embryonic. No instrument occupies the prohibition end of the spectrum.

**Design logic.** Accumulated — but with a distinctive feature. Like the EU and South Korea, Australia's instrument set accumulated from different regulatory eras and problem framings: the ACL (2011), the Harper Reforms to competition law (2017), the DPSI inquiry (2020-2025), Privacy Act reform (2025), the Unfair Trading Practices Bill (2026), and AI governance (2024-ongoing). Each responded to a different stimulus. But unlike the EU's structural accumulation or South Korea's responsive accumulation, Australia's accumulation follows a study-to-legislation pipeline: the DPSI inquiry produced the recommendation, which produced the exposure draft bill. This gives the accumulated instruments a sequential logic — study → recommendation → legislation — even though the instruments themselves were not designed as a coordinated response to surveillance pricing.

**Institution relied on — divergence.** The ACCC and ASIC operate as enforcement-led regulators deploying general-purpose misleading conduct provisions against pricing practices. The formal strategy is disclosure (s.18 requires truthful representations), but the operative institution is the state enforcing prohibitions on false claims — functionally closer to command and control than to market-disciplining disclosure. The ASIC insurance pricing cases are particularly striking: the same underlying conduct that the UK's FCA addressed through a sector-specific prohibition (price walking ban), Australia addresses through misleading conduct enforcement. The strategy is formally different (disclosure vs. prohibition), but the institutional mechanism is functionally equivalent — the state identifies harmful pricing practices and acts to stop them. The difference is that the UK's prohibition prevents the practice entirely; Australia's misleading conduct enforcement only prevents firms from lying about it.

## Evidence

**Webjet penalty (AUD 9M, 2025).** Drip pricing — displaying airfares without disclosing compulsory fees. Federal Court described conduct as "serious and wide-reaching." [ACCC media release](https://www.accc.gov.au/media-release/webjet-penalty)

**Dendy Cinemas (AUD 19.8K, 2025).** Infringement notice for failing to prominently display total ticket prices inclusive of booking fees. [ACCC, "Dendy Pays Penalties for Alleged 'Drip Pricing' Practices"](https://www.accc.gov.au/media-release/dendy-pays-penalties-for-alleged-drip-pricing-practices)

**Coles and Woolworths (proceedings, 2024–ongoing).** Illusory discounts — temporarily increasing prices before marketing products as "Prices Dropped" or "Down Down." At least 245 products (Coles) and 266 products (Woolworths). Largest consumer protection enforcement action in Australian retail history. Woolworths hearing scheduled April 2026. [ACCC media release (Sept 2024)](https://www.accc.gov.au/media-release/accc-takes-woolworths-and-coles-to-court-over-alleged-misleading-prices-dropped-and-down-down-claims)

**IAG insurance (AUD 40M penalty, 2024).** Misleading loyalty discount representations on over one million home insurance policy renewals (2017-2022). The discounts were eroded by prior premium increases — functionally equivalent to price walking. [ASIC, "23-228MR"](https://www.asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-228mr-asic-alleges-iag-misled-home-insurance-customers-on-pricing-discounts/)

**QBE insurance (proceedings, October 2024; trial April 2026).** Misleading discount representations on over 500,000 renewal notices (2017-2022). [ASIC, "24-234MR"](https://www.asic.gov.au/about-asic/news-centre/find-a-media-release/2024-releases/24-234mr-asic-alleges-qbe-misled-customers-over-pricing-discounts/)

**RACQ insurance (AUD 10M penalty).** Similar misleading discount practices.

**No enforcement on personalized pricing.** No Australian regulator has brought enforcement action specifically targeting algorithmic personalized pricing, algorithmic collusion, or surveillance pricing. All enforcement has targeted misleading representations about pricing (drip pricing, illusory discounts, misleading loyalty discounts) — not the algorithmic logic behind the price.

## Movement

Australia's trajectory follows a study-to-legislation pipeline: comprehensive inquiry → recommendations → exposure draft → (pending) legislation.

1. **January 2011**: Australian Consumer Law takes effect — s.18 misleading conduct prohibition becomes primary consumer protection instrument
2. **November 2017**: Harper Reforms to CCA take effect — concerted practices prohibition (s.45(1)(c)) and effects-based misuse of market power test (s.46) added
3. **March 2020**: ACCC Digital Platform Services Inquiry begins (five-year ministerial direction)
4. **September 2022–2023**: ASIC commences proceedings against IAG (2023) for misleading insurance loyalty discounts
5. **September 2024**: Department of Industry releases mandatory AI guardrails proposals paper
6. **September 2024**: ACCC commences proceedings against Coles and Woolworths for illusory discounts
7. **October 2024**: ASIC commences proceedings against QBE for misleading insurance discounts
8. **February 2025**: Webjet admits liability for drip pricing; AUD 9M penalty imposed
9. **2025**: ACCC designates drip pricing as enforcement and compliance priority for 2025-26
10. **June 2025**: ACCC releases final report of Digital Platform Services Inquiry — recommends economy-wide unfair trading practices prohibition
11. **November 2025**: Australian AI Safety Institute announced
12. **December 2025**: National AI Plan launched; Privacy Act reforms (first tranche) — ADM transparency requirement passed (effective December 2026)
13. **February 2026**: Treasury releases exposure draft of Unfair Trading Practices Bill (consultation closes Feb 23; proposed effective date July 2027)

The trajectory is notable for the gap between recognition and response. The ACCC has studied digital platform pricing since 2020 and recognized algorithmic pricing risks throughout. But the legislative response (the Unfair Trading Practices Bill) arrives in 2026 — six years after the inquiry began — and if passed, takes effect in 2027. In the interim, the ACCC has used existing tools (s.18 misleading conduct) with increasing intensity, creating an enforcement pattern that addresses pricing transparency without waiting for legislative reform. This enforcement-led approach is distinctive: the regulator acts within existing law while simultaneously advocating for new law.

## Open Questions

1. **Will the Unfair Trading Practices Bill reach personalized pricing?** The "unreasonably manipulates" and "unreasonably distorts the environment" language is broad. Could algorithmic personalized pricing — where the price environment a consumer sees is shaped by their data — constitute environmental distortion? The exposure draft does not address this. If courts construe the provision broadly, it could become the most significant instrument for surveillance pricing in the Common Law world.
2. **Will the concerted practices prohibition be tested against algorithmic collusion?** Section 45(1)(c) has not been tested in court. Academic analysis suggests it likely requires communication, limiting its reach to autonomous algorithmic collusion. Will the ACCC bring a test case?
3. **Will the Privacy Act ADM transparency obligation affect pricing practices?** The December 2026 requirement to disclose automated decision-making in privacy policies is systemic transparency — not individual rights. Will firms that use algorithmic pricing disclose this in privacy policies? Will the OAIC enforce? Will disclosure create public pressure for further regulation?
4. **Will ASIC enforcement on insurance loyalty pricing extend to algorithmic pricing?** The IAG/QBE/RACQ enforcement targets misleading discount claims — not the underlying algorithmic pricing logic. Will ASIC move from "you lied about the discount" to "the pricing algorithm itself is unfair"? The Unfair Trading Practices Bill could provide this pathway.
5. **Will the AI guardrails produce binding legislation?** The September 2024 consultation and December 2025 National AI Plan have not yet produced binding rules. If mandatory guardrails are enacted for high-risk AI settings, will pricing algorithms be designated as high-risk?
6. **Is there a gap between ACCC drip pricing enforcement and personalized pricing?** The ACCC has made drip pricing an enforcement priority (2025-26) but has not signaled intent to address personalized pricing through s.18 or any other instrument. Will the ACCC extend its pricing enforcement focus from how prices are displayed to how they are set?

## Sources

**Primary**:
- [Competition and Consumer Act 2010 / Australian Consumer Law](https://www.legislation.gov.au/C2004A01468/latest/text)
- [Privacy Act 1988 (as amended)](https://www.legislation.gov.au/C2004A03712/latest/text)
- [ACCC, Digital Platform Services Inquiry Final Report (March 2025)](https://www.accc.gov.au/about-us/publications/serial-publications/digital-platform-services-inquiry-2020-25-reports/digital-platform-services-inquiry-final-report-march-2025)
- [Treasury, Competition and Consumer Amendment (Unfair Trading Practices) Bill 2026 (Exposure Draft)](https://treasury.gov.au/consultation/c2026-t-unfair-trading-practices)
- [ACCC v Coles / Woolworths (Federal Court, commenced Sept 2024)](https://www.accc.gov.au/media-release/accc-takes-woolworths-and-coles-to-court-over-alleged-misleading-prices-dropped-and-down-down-claims)
- [ASIC, "23-228MR: IAG Misleading Loyalty Discounts" (2023)](https://www.asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-228mr-asic-alleges-iag-misled-home-insurance-customers-on-pricing-discounts/)
- [ASIC, "24-234MR: QBE Misleading Discounts" (2024)](https://www.asic.gov.au/about-asic/news-centre/find-a-media-release/2024-releases/24-234mr-asic-alleges-qbe-misled-customers-over-pricing-discounts/)
- [ACCC, "Dendy Pays Penalties for Drip Pricing" (2025)](https://www.accc.gov.au/media-release/dendy-pays-penalties-for-alleged-drip-pricing-practices)
- [Department of Industry, "Mandatory Guardrails for AI in High-Risk Settings" (Sept 2024)](https://consult.industry.gov.au/ai-mandatory-guardrails)
- [Department of Industry, "National AI Plan" (Dec 2025)](https://www.industry.gov.au/publications/national-ai-plan)

**Secondary**:
- [Clifford Chance, "From Inquiry to Action: The Final DPSI Report" (July 2025)](https://www.cliffordchance.com/insights/resources/blogs/antitrust-fdi-insights/2025/07/final-dpsi-report-and-future-for-digital-platforms-in-australia.html)
- [Bird & Bird, "Six Key Recommendations from Australia's Final DPSI Report" (2025)](https://www.twobirds.com/en/insights/2025/australia/six-key-recommendations-from-australias-final-digital-platform-services-inquiry-report)
- [Allens, "Unfair Trading Practices: Treasury Unveils Blueprint for New Regime" (Feb 2026)](https://www.allens.com.au/insights-news/insights/2026/02/unfair-trading-practices-treasury-unveils-blueprint-for-new-regime/)
- [Baker McKenzie, "Australia: Proposed ACL Unfair Trading Reforms" (Feb 2026)](https://www.bakermckenzie.com/en/insight/publications/2026/02/australia-proposed-acl-unfair-trading-reforms)
- [Ashurst, "Play Fair: Unfair Trading Practices Ban Coming in 2026" (2026)](https://www.ashurst.com/en/insights/play-fair-unfair-trading-practices-ban-coming-in-2026/)
- [Gilbert + Tobin, "Dark Patterns to Face the Light of Day" (2026)](https://www.gtlaw.com.au/insights/dark-patterns-to-face-the-light-of-day-unfair-trading-practices-targeted-in-proposed-acl-reforms)
- [King & Wood Mallesons, "Hidden Fares and Hollow Confirmations: ACCC Grounds Webjet" (2025)](https://pulse.kwm.com/in-competition/hidden-fares-and-hollow-confirmations-accc-grounds-webjet/)
- [King & Wood Mallesons, "Fee-ling Misled: ACCC Cracks Down on Dendy Cinema Drip Pricing" (2025)](https://pulse.kwm.com/in-competition/fee-ling-misled-accc-cracks-down-on-dendy-cinema-drip-pricing/)
- [Holding Redlich, "What Retailers Can Learn from Webjet's $9 Million Penalty" (2025)](https://www.holdingredlich.com/what-retailers-can-learn-from-webjet-s-9-million-penalty-for-misleading-airfare-pricing)
- [Balasingham, "The Australian CCA 2.0: Is the New Concerted Practices Prohibition an Effective Patch?" (2020)](https://www.competitionpolicyinternational.com/wp-content/uploads/2020/07/9-The-Australian-Competition-and-Consumer-Act-2.0-Is-the-New-Concerted-Practices-Prohibition-an-Effective-Patch-to-Address-Algorithmic-Collusion-Baskaran-Balasingham.pdf)
- [Chan, "Algorithmic Collusion and Australian Competition Law" (2021) 44(4) UNSW Law Journal 1365](http://classic.austlii.edu.au/au/journals/UNSWLawJl/2021/47.html)
- [Helios Salinger, "How to Get Ahead of the New ADM Rules" (July 2025)](https://www.heliossalinger.com.au/2025/07/01/how-to-get-ahead-of-the-new-adm-rules-before-they-rule-you/)
- [Norton Rose Fulbright, "Parliament Passes Major and Meaningful Privacy Law Reform" (2025)](https://www.nortonrosefulbright.com/en/knowledge/publications/be98b0ff/australian-privacy-alert-parliament-passes-major-and-meaningful-privacy-law-reform)
- [Corrs Chambers Westgarth, "Australia Releases Proposed Mandatory Guardrails for AI Regulation" (2024)](https://www.corrs.com.au/insights/australia-releases-proposed-mandatory-guardrails-for-ai-regulation)
- [White & Case, "Australia's National AI Plan: Big Ambitions, But Light on Details" (2025)](https://www.whitecase.com/insight-alert/australias-national-ai-plan-big-ambitions-light-details)
- [Business Insurance Consulting, "IAG Faces New Class Action Over Loyalty Pricing" (Jan 2025)](https://businessinsuranceconsulting.com.au/2025/01/07/iag-faces-new-class-action-over-loyalty-pricing-what-australian-policyholders-need-to-know/)

**Library**:
- [[intel-comparative-regulation]]
- [[surveillance-pricing-comparative-regulation]]
- [[baldwin-regulatory-strategies]]
- [[disclosure-regulation]]
- [[rights-and-liabilities-regulation]]
- [[competition-over-regulation]]
- [[self-regulation]]
- [[command-and-control]]
- [[regulatory-topology-not-ladder]]
- [[government-capacities-regulation]]
- [[sp-uk]]
- [[sp-eu]]
- [[sp-china]]
- [[sp-singapore]]
- [[sp-south-korea]]
- [[sp-new-york]]
- [[sp-california]]
