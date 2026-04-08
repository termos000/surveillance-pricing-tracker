---
date-created: "202602242350"
aliases:
  - "EU surveillance pricing profile"
tags:
  - "#molecules"
  - "#jurisdiction-profile"
topic:
  - "[[surveillance pricing]]"
  - "[[European Union]]"
---

# European Union — Surveillance Pricing Regulatory Profile

*Jurisdiction molecule for [[surveillance-pricing-comparative-regulation|Paper 1]].*

The EU occupies every strategy except prohibition — disclosure, rights, competition, and code-as-regulation — but no single instrument was designed for surveillance pricing. The instrument set accumulated across different eras, legal bases, and policy objectives (consumer protection, data protection, competition, platform governance, AI safety), producing a dense regulatory surface with low coherence, no clear hierarchy, and contested operational status on the provision most directly relevant to personalized pricing (GDPR Article 22).

## Instruments

| Instrument | Strategy | Sector | Status | Enforcement |
|-----------|----------|--------|--------|-------------|
| Consumer Rights Directive Art. 6(1)(ea) (Omnibus Directive 2019/2161, eff. May 2022) | Disclosure ([[disclosure-regulation]]) | General (distance and off-premises contracts only; excludes in-store and dynamic pricing not based on personal data) | Operative | National consumer protection authorities; penalties up to 4% of turnover or EUR 2M under Omnibus Directive penalty framework; no private right of action at EU level |
| GDPR Article 22 (eff. May 2018) | Rights & liabilities ([[rights-and-liabilities-regulation]]) | General | Contested | National DPAs; fines up to EUR 20M or 4% of global turnover; individual right to lodge complaint with DPA; no harmonized private right of action |
| TFEU Articles 101/102 + 2023 Horizontal Guidelines | Competition ([[competition-over-regulation]]) | General | Operative (investigations confirmed July 2025) | European Commission (DG Competition); national competition authorities; fines up to 10% of global turnover; private damages actions under Damages Directive |
| Digital Markets Act (eff. May 2023; full application March 2024) | Competition (structural) | Core platform services (gatekeepers only) | Operative | European Commission exclusively; fines up to 10% of global turnover; periodic penalties up to 5%; systemic non-compliance: up to 20% |
| AI Act (Regulation 2024/1689, eff. Aug 2024; high-risk provisions apply Aug 2026) | Code-as-regulation ([[code-as-regulation]]) | Sector-specific (credit scoring and insurance pricing are high-risk under Annex III; general algorithmic pricing not classified) | Enacted (not yet operative for high-risk obligations) | National market surveillance authorities; AI Office (Commission); fines up to EUR 35M or 7% of global turnover for prohibited systems |
| Unfair Commercial Practices Directive (2005/29/EC, amended by Omnibus 2019/2161) | Disclosure | General (B2C) | Operative | National consumer protection authorities; UCPD Annex I (blacklist of prohibited practices); CPC Network for cross-border enforcement |
| Digital Fairness Act (consultation closed Oct 2025; draft expected Q3 2026) | Disclosure (expanded, potentially prohibition of drip pricing) | General (digital B2C) | Proposed | TBD |
| Platform-to-Business Regulation (eff. July 2020; repeal proposed Nov 2025) | Disclosure | Online intermediation services (B2B transparency) | Operative (proposed repeal) | National courts; mediation; observatory function |

## Detail

### Consumer Rights Directive Art. 6(1)(ea) (Omnibus Directive, eff. May 28, 2022)

The Omnibus Directive (2019/2161) inserted Article 6(1)(ea) into the Consumer Rights Directive (2011/83/EU), creating the EU's most directly on-point provision for surveillance pricing. Traders must inform consumers, before a distance or off-premises contract is concluded, when the price has been "personalised on the basis of automated decision-making." The disclosure is triggered by personalisation based on profiling of consumer behavior; it does not apply to dynamic pricing that responds to market demand or supply conditions without using personal data.

**Scope limitations.** The provision applies only to distance and off-premises contracts — it does not cover in-store retail. The information requirement is thin: traders must disclose the fact of personalisation, not the mechanism, the data used, or the magnitude of the price difference. This makes it significantly narrower than New York's A6765, which requires the specific disclosure "THIS PRICE WAS SET BY AN ALGORITHM USING YOUR PERSONAL DATA" across all retail channels. The Omnibus Directive also does not require offering a non-personalised price as a baseline (contrast China's E-Commerce Law Article 18, which requires non-personalised search options).

**Implementation.** EU member states were required to transpose by November 28, 2021, and bring provisions into force by May 28, 2022. Germany transposed via Section 312d BGB and Article 246a EGBGB, which may warrant a separate molecule. National implementation varies in strictness — the Directive allows member states to introduce additional transparency obligations.

**Enforcement.** The Omnibus Directive introduced GDPR-style fines for consumer protection breaches: maximum penalties of at least 4% of turnover or EUR 2 million. Cross-border enforcement is coordinated through the Consumer Protection Cooperation (CPC) Network. No enforcement actions specifically targeting personalised pricing under Art. 6(1)(ea) have been identified as of February 2026.

**Primary**: [Directive 2019/2161 (EUR-Lex)](https://eur-lex.europa.eu/eli/dir/2019/2161/oj/eng); [Consumer Rights Directive (European Commission)](https://commission.europa.eu/law/law-topic/consumer-protection-law/consumer-contract-law/consumer-rights-directive_en)

**Secondary**: [EY, "The Omnibus Directive" (2022)](https://www.ey.com/en_pl/insights/law/omnibus-directive); [7Learnings, "EU Omnibus Directive — What Retailers Need to Know"](https://7learnings.com/blog/what-retailers-need-to-know-about-the-new-eu-consumer-protection-directive/); [Library of Congress, "European Union: New Directive Amends Consumer Protection Rules" (Feb 2020)](https://www.loc.gov/item/global-legal-monitor/2020-02-10/european-union-new-directive-amends-consumer-protection-rules/); [European Parliament, "Personalised Pricing" (Study, Nov 2022)](https://www.europarl.europa.eu/RegData/etudes/STUD/2022/734008/IPOL_STU(2022)734008_EN.pdf)

### GDPR Article 22 — Automated Decision-Making (eff. May 25, 2018)

Article 22(1) provides that data subjects "shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her." The provision is the most debated EU instrument in the personalized pricing context. Whether algorithmic pricing constitutes a "decision" that "significantly affects" a consumer is the central contested question.

**The "significant effects" threshold.** The Article 29 Working Party (now EDPB) Guidelines on Automated Decision-Making state that automated differential pricing "could... have a significant effect if, for example, prohibitively high prices effectively bar someone from certain goods or services." This suggests Article 22 could reach extreme cases of personalised pricing but leaves ordinary price differences (e.g., a 10-15% variance) in uncertain territory. No DPA has issued binding guidance specifying when personalised pricing crosses the "significant effects" threshold.

**Scholarly debate.** [[Benjamin Wong]] (2020) argues Article 22 should not be relied upon to constrain personalized pricing, preferring transparency-centric approaches. His skeptical view rests on two grounds: (1) Article 22 does not in fact pose a significant obstacle to online personalised pricing under current interpretation; and (2) there are good reasons not to adopt a prohibitory stance, with transparency being preferred. The European Parliament's 2022 study on personalised pricing reached a different conclusion, noting that "given general consumer rejection of personalized pricing and likelihood of overall detriment, one could consider prohibiting personalised prices" in certain forms. [[Gianclaudio Malgieri]] and [[Giovanni Comande]] argue for a "right to legibility" of automated decision-making that would encompass pricing discrimination.

**CJEU case law — *SCHUFA Holding (Scoring)*, Case C-634/21 (Dec 7, 2023).** The CJEU's first ruling on Article 22 held that credit scoring by an agency constitutes automated individual decision-making when a third party "draws strongly" on the score to make decisions with legal or similarly significant effects. The court found SCHUFA's credit score played a "determining role" in the lender's decision. This ruling is significant for pricing because it establishes that preparatory algorithmic outputs — not just final contractual decisions — can trigger Article 22 when downstream actors rely heavily on them. Whether a personalized price generated by an algorithm occupies the same position as a credit score remains untested but is now more plausible after *SCHUFA*. The subsequent *Dun & Bradstreet Austria* case (C-203/22, Feb 27, 2025) addressed the balance between algorithmic transparency rights and trade secret protection, holding that DPAs or courts must weigh competing interests when controllers claim algorithmic outputs are trade secrets.

**Operational status.** No enforcement action or judicial decision has applied Article 22 specifically to personalised pricing as of February 2026. The provision is "enacted but contested" — it exists as law, the CJEU has interpreted it expansively in the credit scoring context, but its application to pricing remains theoretical.

**Primary**: [GDPR Article 22 text](https://gdpr-info.eu/art-22-gdpr/); [Art. 29 Working Party Guidelines on Automated Decision-Making (WP251rev.01)](https://ec.europa.eu/newsroom/article29/items/612053); *SCHUFA Holding (Scoring)*, Case C-634/21, ECLI:EU:C:2023:957 (Dec 7, 2023); *Dun & Bradstreet Austria*, Case C-203/22, ECLI:EU:C:2025:131 (Feb 27, 2025)

**Secondary**: [Wong, "Online Personalised Pricing as Prohibited Automated Decision-Making Under Article 22 GDPR: A Sceptical View," 30 Info. & Commc'ns Tech. L. 2 (2021)](https://www.tandfonline.com/doi/abs/10.1080/13600834.2020.1860460); [IAPP, "Key Takeaways from the CJEU's Recent Automated Decision-Making Rulings"](https://iapp.org/news/a/key-takeaways-from-the-cjeus-recent-automated-decision-making-rulings); [Bird & Bird, "CJEU Confirms Preparatory Acts Can Be Automated Individual Decisions: The SCHUFA Cases"](https://www.twobirds.com/en/insights/2023/global/key-takeaways-from-the-schufa-case-of-the-cjeu); [A&O Shearman, "CJEU Rules That a Credit Score Constitutes Automated Decision Making"](https://www.aoshearman.com/en/insights/ao-shearman-on-data/cjeu-rules-that-a-credit-score-constitutes-automated-decision-making-under-the-gdpr); [Fasken, "Algorithmic Scoring and the CJEU Decision on SCHUFA: Has the Pandora's Box Been Unleashed?"](https://www.fasken.com/en/knowledge/2024/03/algorithmic-scoring-and-the-cjeu-decision-on-shufa); [FPF, "Automated Decision-Making Under the GDPR: Practical Cases from Courts" (2022)](https://fpf.org/wp-content/uploads/2022/05/FPF-ADM-Report-R2-singles.pdf); [European Parliament, "Personalised Pricing" (Study, Nov 2022)](https://www.europarl.europa.eu/RegData/etudes/STUD/2022/734008/IPOL_STU(2022)734008_EN.pdf)

### TFEU Articles 101/102 and EU Competition Enforcement (ongoing)

EU competition law reaches algorithmic pricing through two channels: Article 101 TFEU (agreements, including algorithmic collusion) and Article 102 TFEU (abuse of dominance, including exploitative pricing by dominant firms).

**Article 101 — algorithmic collusion.** The Commission's 2023 Horizontal Guidelines explicitly address algorithms as collusion facilitators, with paragraph 379 warning that "algorithms then become a device to facilitate collusion (collusion by code)." Software providers can be liable if they knowingly enable price coordination between competitors. In July 2025, Deputy Director-General for Antitrust Linsey McCallum confirmed that the Commission is conducting multiple active investigations into algorithmic pricing, without specifying sectors. This was the Commission's first public confirmation of live algorithmic pricing cases.

**Article 102 — exploitative pricing.** For dominant firms, algorithmic personalised pricing may constitute an abuse under Article 102(c), which prohibits "applying dissimilar conditions to equivalent transactions with other trading parties, thereby placing them at a competitive disadvantage." However, the CJEU has indicated that exploitative abuse enforcement requires an elevated burden of proof. Academic commentary identifies a five-step assessment framework: establishing dominance, identifying non-cost-related price differences, analyzing consumer welfare impact, confirming persistence of harm, and identifying the source of discrimination.

**Significance.** Unlike the disclosure and rights instruments above, the competition channel reaches algorithmic pricing conduct directly, but it requires either horizontal coordination (Article 101) or market dominance (Article 102). Unilateral personalised pricing by non-dominant firms falls outside its reach entirely — the same structural gap as California's AB 325.

**Primary**: [TFEU Articles 101, 102](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A12016ME%2FTXT); [European Commission 2023 Horizontal Guidelines, para 379](https://competition-policy.ec.europa.eu/antitrust-and-cartels/legislation/horizontal-agreements_en)

**Secondary**: [Morgan Lewis, "Algorithmic Pricing Emerges as Enforcement Priority for EU & UK Antitrust Regulators" (Oct 2025)](https://www.morganlewis.com/pubs/2025/10/algorithmic-pricing-emerges-as-enforcement-priority-for-eu-and-uk-antitrust-regulators); [Freshfields, "EU Steps Up on Algorithmic Pricing Cartels" (2025)](https://riskandcompliance.freshfields.com/post/102kt76/eu-steps-up-on-algorithmic-pricing-cartels-joining-the-us-and-other-jurisdiction); [Hogan Lovells, "Update on Algorithmic Pricing in Competition Law"](https://www.hoganlovells.com/en/publications/update-on-algorithmic-pricing-in-competition-law-what-you-need-to-know); [CeCo, "Algorithmic Price Discrimination as Exploitative Abuse under Article 102 TFEU"](https://centrocompetencia.com/algorithmic-pricing-discrimination/); [Steptoe, "Unlawful Unilateral Use of AI: When Algorithms Become Instruments of Anticompetitive Conduct"](https://www.steptoe.com/en/news-publications/stepahead-antitrust-and-competition-insights/unlawful-unilateral-use-of-ai-when-algorithms-become-instruments-of-anticompetitive-conduct.html)

### Digital Markets Act (eff. May 2, 2023; full application from March 2024)

The DMA imposes obligations on designated "gatekeepers" — large platforms providing core platform services — that are relevant to, but not specifically designed for, surveillance pricing.

**Data combination restrictions.** Article 5(2) prohibits gatekeepers from combining personal data from their core platform service with personal data from other services offered by the gatekeeper or third-party services, or from signing in end users to other services in order to combine personal data, unless the end user has given consent. This restricts the data aggregation infrastructure that enables personalised pricing by gatekeepers — if a gatekeeper cannot combine browsing data from its search engine with purchase data from its marketplace without consent, the data inputs for price personalisation are curtailed.

**Anti-self-preferencing and parity.** Article 5(3) prohibits gatekeepers from preventing business users from offering different prices or conditions through other channels. This addresses the merchant-facing dimension of algorithmic pricing — platforms cannot force sellers to maintain price parity across channels.

**Profiling audit.** Article 15 requires gatekeepers to submit an independently audited description of any techniques used to profile consumers across their core platform services.

**Limitations.** The DMA is a competition-adjacent structural regulation, not a consumer protection instrument. It does not prohibit personalised pricing by gatekeepers; it restricts the data infrastructure and self-preferencing practices that enable it. Non-gatekeeper platforms are entirely outside scope.

**Primary**: [Digital Markets Act (Regulation 2022/1925)](https://digital-markets-act.ec.europa.eu/index_en)

**Secondary**: [SecurePrivacy, "Digital Markets Act Explained (2025)"](https://secureprivacy.ai/blog/digital-markets-act-dma-explained-2025); [Covington, "Digital Fairness Act Series — Topic 3: Personalized Advertising and Pricing"](https://www.insideprivacy.com/consumer-protection/digital-fairness-act-series-topic-3-personalized-advertising-and-pricing/)

### AI Act (Regulation 2024/1689, eff. Aug 2024; high-risk provisions apply Aug 2026)

The AI Act classifies AI systems by risk tier (unacceptable, high, limited, minimal). Its relevance to surveillance pricing is partial and indirect.

**High-risk classification — Annex III.** Two categories in Annex III capture algorithmic pricing in specific sectors: (1) "AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score" (credit and insurance pricing); and (2) "AI systems intended to be used for risk assessment and pricing in relation to natural persons in the case of life and health insurance." These high-risk designations impose conformity assessment, transparency, human oversight, and documentation obligations.

**General algorithmic pricing — not classified.** Algorithmic pricing for consumer goods and services (retail, e-commerce, travel, hospitality) is not listed in Annex III and does not fall within the prohibited practices of Article 5 (which target subliminal manipulation, social scoring, and real-time biometric identification). General surveillance pricing is therefore "minimal risk" under the AI Act and subject to no specific obligations beyond voluntary codes of conduct.

**Significance.** The AI Act creates a sector-specific code-as-regulation instrument for credit scoring and insurance pricing algorithms, but leaves the vast majority of surveillance pricing — retail, e-commerce, travel, hospitality — unregulated. The Commission was required to publish guidelines on high-risk classification, including practical examples, by February 2, 2026. In November 2025, the Commission proposed a Digital Omnibus on AI Regulation that would simplify the AI Act and potentially delay the high-risk application date.

**Primary**: [AI Act (Regulation 2024/1689)](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai); [Annex III](https://artificialintelligenceact.eu/annex/3/)

**Secondary**: [LegalNodes, "EU AI Act 2026 Updates: Compliance Requirements and Business Risks"](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks); [Goodwin, "EU AI Act: Key Points for Financial Services"](https://www.goodwinlaw.com/en/insights/publications/2024/08/alerts-practices-pif-key-points-for-financial-services-businesses); [Trilateral Research, "EU AI Act Compliance Timeline"](https://trilateralresearch.com/responsible-ai/eu-ai-act-implementation-timeline-mapping-your-models-to-the-new-risk-tiers); [Harvard Data Science Review, "The Future of Credit Underwriting and Insurance Under the EU AI Act"](https://hdsr.mitpress.mit.edu/pub/19cwd6qx)

### Unfair Commercial Practices Directive (2005/29/EC, amended 2019/2161)

The UCPD provides the baseline consumer protection framework against misleading and aggressive commercial practices. Its application to personalised pricing operates through general provisions rather than pricing-specific rules.

**Article 7(1) — misleading omissions.** A commercial practice is misleading if it omits material information that the average consumer needs to make an informed transactional decision. An equivalent information obligation regarding automated pricing can be derived from this provision — failing to disclose personalisation could constitute a misleading omission. However, this theory is untested in case law.

**Omnibus Directive amendments.** The 2019/2161 amendments added new items to the UCPD's "blacklist" (Annex I) of always-prohibited practices, including manipulative online reviews. The amendments did not add personalised pricing to the blacklist. The amendments also strengthened enforcement penalties (harmonized minimum of 4% turnover or EUR 2 million) and strengthened the CPC Network's cross-border enforcement powers.

**Significance.** The UCPD provides a theoretical catch-all for deceptive pricing practices but has not been deployed specifically against personalised pricing. Its value in the regulatory profile is as background law — present but not operative for this specific practice.

**Primary**: [UCPD (European Commission)](https://commission.europa.eu/law/law-topic/consumer-protection-law/unfair-commercial-practices-and-price-indication/unfair-commercial-practices-directive_en)

**Secondary**: [Springer, "The Silent Death of EU Consumer Law and Its Resilient Revival" (2025)](https://link.springer.com/article/10.1007/s10603-025-09590-5)

### Digital Fairness Act (consultation closed Oct 2025; draft expected Q3 2026)

The DFA is the Commission's forthcoming legislative initiative to address digital-era consumer protection gaps. Its consultation explicitly covers personalized pricing.

**Scope.** The consultation addressed three unfair pricing practices: drip pricing (showing a low headline price then incrementally adding mandatory charges), dynamic pricing (real-time price adjustments based on demand), and personalised pricing (tailoring prices to individual consumers based on profiling). The consultation asked whether existing EU rules are sufficient or whether new obligations are needed.

**Significance for the regulatory profile.** The DFA represents the EU's recognition that the existing accumulated instrument set — CRD Art. 6(1)(ea), GDPR Art. 22, UCPD — is insufficient to address personalised pricing. Whether the DFA will propose disclosure enhancements, prohibition of specific practices (drip pricing appears most likely), or a broader framework remains open until the draft is published (expected Q3 2026).

**Status.** Proposed only. The public consultation ran from July to October 2025. The Commission's impact assessment and formal legislative proposal are expected Q2-Q3 2026.

**Primary**: [Digital Fairness Act consultation (European Commission)](https://commission.europa.eu/document/download/84cfc60e-f264-4f31-9f79-9ec83dce064d_en)

**Secondary**: [Osborne Clarke, "Digital Fairness Act Unpacked: Unfair Pricing Practices"](https://www.osborneclarke.com/insights/digital-fairness-act-unpacked-unfair-pricing-practices); [Sidley Austin, "EU Consults on Digital Fairness Act" (July 2025)](https://www.sidley.com/en/insights/newsupdates/2025/07/eu-consults-on-digital-fairness-act-big-changes-ahead-for-consumer-facing-platforms); [Bird & Bird, "EU Consultation on the Digital Fairness Act" (2025)](https://www.twobirds.com/en/insights/2025/eu-%E2%80%93-consultation-on-the-digital-fairness-act); [Taylor Wessing, "Digital Fairness Act and Digital Omnibus: Clarity or Complexity for Businesses in 2026?"](https://www.taylorwessing.com/en/interface/2025/predictions-2026/digital-fairness-act-and-digital-omnibus)

### Platform-to-Business Regulation (eff. July 12, 2020; repeal proposed Nov 2025)

Regulation 2019/1150 requires online intermediation services to provide transparency to business users regarding ranking parameters, differentiated treatment, and data access. It does not address consumer-facing pricing.

**Significance.** Tangential. The P2B Regulation addresses platform-merchant transparency (algorithmic ranking disclosure, parity clause transparency), not consumer-facing personalised pricing. The Commission proposed repeal in November 2025 as part of the Digital Omnibus simplification package, suggesting its obligations will be absorbed into the DMA or DFA frameworks.

**Primary**: [P2B Regulation (European Commission)](https://digital-strategy.ec.europa.eu/en/policies/platform-business-trading-practices)

## Analysis

**Hierarchy.** No single strategy dominates. Disclosure (CRD Art. 6(1)(ea)) is the only instrument designed specifically for personalised pricing — but it is narrow (distance selling only, fact-of-personalisation only). Rights (GDPR Art. 22) is theoretically the most powerful instrument but is contested for this application and has never been enforced against pricing. Competition (Articles 101/102) is now actively being enforced but requires either coordination or dominance. Code-as-regulation (AI Act) reaches only sector-specific pricing (credit, insurance). The instruments operate in parallel without an explicit statutory relationship between them. This is not an intentional design — it is an absence of hierarchy that reflects the accumulated, uncoordinated character of the instrument set.

**Design logic.** Accumulated. The EU's surveillance pricing instruments were not designed as a set. They emerged from different legislative eras, different legal bases, and different policy objectives:

- CRD Art. 6(1)(ea) — consumer protection, internal market harmonisation (2019/2022)
- GDPR Art. 22 — data protection, fundamental rights (2016/2018)
- TFEU Arts. 101/102 — competition, Treaty-level (1957/ongoing)
- DMA — digital market contestability (2022/2024)
- AI Act — AI safety, risk governance (2024/2026)
- UCPD — consumer protection baseline (2005/2022)
- DFA — digital consumer fairness (proposed Q3 2026)

Each instrument was enacted for broader purposes and incidentally touches surveillance pricing. None was designed with the practice as its primary target. CRD Art. 6(1)(ea) comes closest, but even it was one provision among many in the Omnibus Directive, which primarily addressed prior-price disclosure, fake reviews, and dual quality products. The result is a dense regulatory surface with multiple instruments from different eras, each applying different strategies with different legal bases and different enforcement institutions. This is the opposite of China's unified design: where China deployed multiple strategies in a single direction (escalating toward prohibition), the EU deployed multiple strategies in no coordinated direction.

**Institution relied on — divergence.** Two notable divergences:

First, GDPR Article 22 is a rights-based instrument that theoretically trusts individuals to exercise data protection rights (objecting to automated decisions, demanding human intervention, requesting explanations). But the institutional reality is that individuals almost never exercise these rights against pricing decisions. The *SCHUFA* litigation was brought by a data subject, but the case was a credit denial with clear adverse effects — a price difference of 10% on a consumer product is unlikely to motivate equivalent litigation. The operational institution for GDPR enforcement is the DPA, not the individual — and no DPA has taken action on personalised pricing. The rights-based strategy thus depends on an institution (individual litigants) that does not activate for this practice, while the alternative institution (DPAs) has not prioritised it.

Second, the competition enforcement channel (Articles 101/102) theoretically trusts market structure — breaking collusion restores competitive discipline. But the Commission's July 2025 confirmation of active investigations signals that the state, not the market, is the operative institution. This is consistent with the competition strategy as deployed: the Commission acts as enforcer, not as facilitator of market self-correction. The divergence is less sharp than the GDPR case because competition enforcement always relies significantly on state action, but the absence of private damages litigation on algorithmic pricing in the EU (unlike the US RealPage class actions) means the state-dependence is even more pronounced.

## Evidence

**No enforcement under CRD Art. 6(1)(ea) for personalised pricing.** No national consumer protection authority has brought an enforcement action specifically for failure to disclose personalised pricing under Art. 6(1)(ea) as of February 2026. The provision has been operative since May 2022 — nearly four years. Whether this reflects compliance, non-detection, or non-prioritisation is unknown. The European Commission confirmed in July 2025 that it is investigating algorithmic pricing, but through competition channels, not consumer protection channels.

**No enforcement under GDPR Art. 22 for personalised pricing.** No DPA enforcement action has applied Article 22 to personalised consumer pricing as of February 2026. The *SCHUFA* ruling (Dec 2023) expanded Article 22's scope to preparatory algorithmic outputs relied upon by downstream actors, but no DPA has extended this logic to pricing. The *Dun & Bradstreet Austria* ruling (Feb 2025) addressed algorithmic transparency versus trade secret protection, creating a framework for balancing competing interests when data subjects seek explanation of automated outputs — but again, not in a pricing context.

**European Commission — multiple active competition investigations (July 2025).** Deputy Director-General Linsey McCallum confirmed that the Commission is conducting "multiple inquiries" into algorithmic pricing, without identifying sectors. This is the strongest signal of enforcement activity in the EU landscape, but it operates through competition channels (requiring either coordination under Art. 101 or dominance under Art. 102), not through the consumer protection or data protection instruments. No formal decisions, statements of objections, or settlement outcomes have been published as of February 2026. [Morgan Lewis, "Algorithmic Pricing Emerges as Enforcement Priority" (Oct 2025)](https://www.morganlewis.com/pubs/2025/10/algorithmic-pricing-emerges-as-enforcement-priority-for-eu-and-uk-antitrust-regulators); [GCR, "EU Reveals Existence of Algorithmic Pricing Cases"](https://globalcompetitionreview.com/article/eu-reveals-existence-of-algorithmic-pricing-cases)

**Netherlands ACM — airline pricing investigation (2025).** The ACM launched a market investigation into computer-controlled consumer prices in the Dutch aviation sector, making it the first EU national authority to conduct a sector-specific investigation into algorithmic pricing. The investigation examines how prices are actually formed in practice and consulted stakeholders through July 2025, with provisional results expected by end of 2025. Results had not been published as of February 2026. [ACM, "Market Investigation into Computer-Controlled Consumer Prices in the Airline Sector"](https://www.acm.nl/en/publications/acm-market-investigation-computer-controlled-consumer-prices-airline-sector-research-methods-and-consultation); [Taylor Wessing, "ACM Investigates Dynamic Pricing of Airline Tickets" (Sept 2025)](https://www.taylorwessing.com/en/insights-and-events/insights/2025/09/acm-investigates-dynamic-pricing-of-airline-tickets)

**European Parliament — personalised pricing study (Nov 2022).** The IMCO Committee commissioned a study that found personalised pricing is "in principle allowed under EU law" but identified regulatory gaps and legal uncertainty. The study concluded that "given general consumer rejection of personalized pricing and likelihood of overall detriment, one could consider prohibiting personalised prices" — particularly first-degree price discrimination. The study also recommended facilitated enforcement through burden-of-proof reversal and authority access to algorithms. This study did not trigger legislative action but informed the Digital Fairness Act consultation. [European Parliament, "Personalised Pricing" (Study, 2022)](https://www.europarl.europa.eu/RegData/etudes/STUD/2022/734008/IPOL_STU(2022)734008_EN.pdf)

## Movement

The EU's trajectory is slow accumulation rather than deliberate escalation. The instruments arrived in the following sequence:

1. **2005**: UCPD establishes consumer protection baseline against misleading commercial practices — no pricing-specific provisions
2. **2018**: GDPR takes effect — Article 22 creates rights-based instrument for automated decision-making; applicability to pricing immediately contested
3. **2019**: Omnibus Directive adopted — Art. 6(1)(ea) creates first disclosure obligation specifically for personalised pricing
4. **2020**: P2B Regulation takes effect — transparency for business users of platforms (tangential to consumer pricing)
5. **2022**: CRD Art. 6(1)(ea) becomes operative — personalized pricing disclosure required for distance/off-premises contracts
6. **2022**: European Parliament publishes study recommending potential prohibition — no legislative follow-up
7. **2023**: CJEU rules in *SCHUFA* — expands Article 22 scope to preparatory algorithmic outputs; Commission's Horizontal Guidelines address algorithmic collusion
8. **2024**: DMA fully applies to gatekeepers — data combination and self-preferencing restrictions; AI Act enters into force — credit/insurance pricing classified as high-risk
9. **July 2025**: Commission confirms multiple active competition investigations into algorithmic pricing; DFA consultation opens
10. **Oct 2025**: DFA consultation closes
11. **Q3 2026 (expected)**: DFA draft legislative proposal — first instrument designed primarily for digital pricing fairness

The trajectory is one of accumulation without convergence. Each new instrument adds a layer — disclosure, then rights, then competition, then platform structure, then AI governance — but the layers are not coordinated. There has been no legislative moment where the EU deliberately chose between strategies or designed a coherent instrument set for surveillance pricing. The DFA may represent the first such moment, but it remains proposed.

Critically, the EU has never adopted prohibition as a strategy for surveillance pricing (contrast China, which escalated from disclosure to prohibition over seven years). The European Parliament study floated prohibition in 2022 but it generated no legislative follow-through. The EU's movement has been exclusively within the disclosure-rights-competition range of the topology.

The Netherlands ACM investigation (2025) represents a national-level initiative that could become a leading edge: if the ACM finds consumer harm from airline pricing algorithms, it could trigger either national enforcement or EU-level legislative action.

## Open Questions

1. **Will the DFA include a prohibition on any form of personalised pricing?** The European Parliament's 2022 study recommended considering prohibition. The consultation asked whether new action is necessary. Drip pricing prohibition appears most likely; personalised pricing prohibition is less certain. The DFA draft (expected Q3 2026) will determine whether the EU stays in the disclosure-rights range or moves toward prohibition.
2. **GDPR Art. 22 — will a DPA test the personalised pricing theory?** The *SCHUFA* ruling expanded Article 22's scope but no DPA has extended it to pricing. If a DPA issues guidance or brings an enforcement action applying Article 22 to personalised consumer pricing, this would activate an instrument that currently exists only on paper for this practice.
3. **What sectors are the Commission's competition investigations targeting?** McCallum confirmed investigations but not sectors. Are they targeting algorithmic collusion (shared pricing tools, paralleling the US RealPage model) or exploitative pricing by dominant platforms? The enforcement theory matters: Article 101 (coordination) has a lower threshold than Article 102 (dominance).
4. **Netherlands ACM airline investigation outcomes.** Provisional results were expected by end of 2025 but have not been published. If the ACM finds consumer harm, does it recommend national enforcement, EU-level legislation, or sector-specific codes?
5. **AI Act high-risk classification — scope creep?** The Commission was due to publish guidance on high-risk classification by February 2026. Could general algorithmic pricing systems be brought within scope through interpretive guidance, or is Annex III amendment required?
6. **National transposition variation.** Germany (Section 312d BGB) and potentially other member states have transposed the CRD with stricter requirements. How much variation exists across member states, and does this create a fragmented regulatory surface within the EU?
7. **Digital Omnibus simplification.** The November 2025 Digital Omnibus proposes to simplify the AI Act and repeal the P2B Regulation. How will this consolidation affect the already-accumulated instrument set? Will it reduce or increase coherence?
8. **Interaction between GDPR Art. 22 and CRD Art. 6(1)(ea).** If a DPA finds personalised pricing violates Article 22, does this override the CRD's approach of permitting pricing with disclosure? The instruments have different legal bases (data protection vs consumer protection) and could produce contradictory regulatory signals.

## Sources

**Primary**:
- [Consumer Rights Directive 2011/83/EU, as amended by Omnibus Directive 2019/2161 (EUR-Lex)](https://eur-lex.europa.eu/eli/dir/2019/2161/oj/eng)
- [GDPR Article 22 text](https://gdpr-info.eu/art-22-gdpr/)
- [Art. 29 Working Party Guidelines on Automated Decision-Making (WP251rev.01)](https://ec.europa.eu/newsroom/article29/items/612053)
- *SCHUFA Holding (Scoring)*, Case C-634/21, ECLI:EU:C:2023:957 (CJEU, Dec 7, 2023)
- *Dun & Bradstreet Austria*, Case C-203/22, ECLI:EU:C:2025:131 (CJEU, Feb 27, 2025)
- [TFEU Articles 101, 102](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A12016ME%2FTXT)
- [European Commission 2023 Horizontal Guidelines](https://competition-policy.ec.europa.eu/antitrust-and-cartels/legislation/horizontal-agreements_en)
- [Digital Markets Act (Regulation 2022/1925)](https://digital-markets-act.ec.europa.eu/index_en)
- [AI Act (Regulation 2024/1689)](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [AI Act Annex III](https://artificialintelligenceact.eu/annex/3/)
- [UCPD (Directive 2005/29/EC)](https://commission.europa.eu/law/law-topic/consumer-protection-law/unfair-commercial-practices-and-price-indication/unfair-commercial-practices-directive_en)
- [P2B Regulation (Regulation 2019/1150)](https://digital-strategy.ec.europa.eu/en/policies/platform-business-trading-practices)
- [ACM, "Market Investigation into Computer-Controlled Consumer Prices in the Airline Sector" (2025)](https://www.acm.nl/en/publications/acm-market-investigation-computer-controlled-consumer-prices-airline-sector-research-methods-and-consultation)

**Secondary**:
- [European Parliament, "Personalised Pricing" (Study, Nov 2022)](https://www.europarl.europa.eu/RegData/etudes/STUD/2022/734008/IPOL_STU(2022)734008_EN.pdf)
- [Wong, "Online Personalised Pricing as Prohibited Automated Decision-Making Under Article 22 GDPR: A Sceptical View," 30 Info. & Commc'ns Tech. L. 2 (2021)](https://www.tandfonline.com/doi/abs/10.1080/13600834.2020.1860460)
- [Malgieri & Comande, "Why a Right to Legibility of Automated Decision-Making Exists in the GDPR," 7 Int'l Data Privacy L. 243 (2017)](https://academic.oup.com/idpl/article-abstract/7/4/243/4626991)
- [Morgan Lewis, "Algorithmic Pricing Emerges as Enforcement Priority for EU & UK Antitrust Regulators" (Oct 2025)](https://www.morganlewis.com/pubs/2025/10/algorithmic-pricing-emerges-as-enforcement-priority-for-eu-and-uk-antitrust-regulators)
- [Freshfields, "EU Steps Up on Algorithmic Pricing Cartels" (2025)](https://riskandcompliance.freshfields.com/post/102kt76/eu-steps-up-on-algorithmic-pricing-cartels-joining-the-us-and-other-jurisdiction)
- [Hogan Lovells, "Update on Algorithmic Pricing in Competition Law"](https://www.hoganlovells.com/en/publications/update-on-algorithmic-pricing-in-competition-law-what-you-need-to-know)
- [CeCo, "Algorithmic Price Discrimination as Exploitative Abuse under Article 102 TFEU"](https://centrocompetencia.com/algorithmic-pricing-discrimination/)
- [Steptoe, "Unlawful Unilateral Use of AI: When Algorithms Become Instruments of Anticompetitive Conduct"](https://www.steptoe.com/en/news-publications/stepahead-antitrust-and-competition-insights/unlawful-unilateral-use-of-ai-when-algorithms-become-instruments-of-anticompetitive-conduct.html)
- [EY, "The Omnibus Directive" (2022)](https://www.ey.com/en_pl/insights/law/omnibus-directive)
- [Library of Congress, "EU: New Directive Amends Consumer Protection Rules" (Feb 2020)](https://www.loc.gov/item/global-legal-monitor/2020-02-10/european-union-new-directive-amends-consumer-protection-rules/)
- [IAPP, "Key Takeaways from the CJEU's Recent ADM Rulings"](https://iapp.org/news/a/key-takeaways-from-the-cjeus-recent-automated-decision-making-rulings)
- [Bird & Bird, "CJEU Confirms Preparatory Acts Can Be Automated Individual Decisions"](https://www.twobirds.com/en/insights/2023/global/key-takeaways-from-the-schufa-case-of-the-cjeu)
- [A&O Shearman, "CJEU Rules That a Credit Score Constitutes ADM"](https://www.aoshearman.com/en/insights/ao-shearman-on-data/cjeu-rules-that-a-credit-score-constitutes-automated-decision-making-under-the-gdpr)
- [Fasken, "Algorithmic Scoring and the CJEU Decision on SCHUFA" (2024)](https://www.fasken.com/en/knowledge/2024/03/algorithmic-scoring-and-the-cjeu-decision-on-shufa)
- [FPF, "Automated Decision-Making Under the GDPR: Practical Cases from Courts" (2022)](https://fpf.org/wp-content/uploads/2022/05/FPF-ADM-Report-R2-singles.pdf)
- [Osborne Clarke, "Digital Fairness Act Unpacked: Unfair Pricing Practices"](https://www.osborneclarke.com/insights/digital-fairness-act-unpacked-unfair-pricing-practices)
- [Sidley Austin, "EU Consults on Digital Fairness Act" (July 2025)](https://www.sidley.com/en/insights/newsupdates/2025/07/eu-consults-on-digital-fairness-act-big-changes-ahead-for-consumer-facing-platforms)
- [Bird & Bird, "EU Consultation on the Digital Fairness Act" (2025)](https://www.twobirds.com/en/insights/2025/eu-%E2%80%93-consultation-on-the-digital-fairness-act)
- [Taylor Wessing, "ACM Investigates Dynamic Pricing of Airline Tickets" (Sept 2025)](https://www.taylorwessing.com/en/insights-and-events/insights/2025/09/acm-investigates-dynamic-pricing-of-airline-tickets)
- [SecurePrivacy, "Digital Markets Act Explained (2025)"](https://secureprivacy.ai/blog/digital-markets-act-dma-explained-2025)
- [LegalNodes, "EU AI Act 2026 Updates"](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)
- [Goodwin, "EU AI Act: Key Points for Financial Services"](https://www.goodwinlaw.com/en/insights/publications/2024/08/alerts-practices-pif-key-points-for-financial-services-businesses)
- [Trilateral Research, "EU AI Act Compliance Timeline"](https://trilateralresearch.com/responsible-ai/eu-ai-act-implementation-timeline-mapping-your-models-to-the-new-risk-tiers)
- [Covington, "Digital Fairness Act Series — Topic 3: Personalized Advertising and Pricing"](https://www.insideprivacy.com/consumer-protection/digital-fairness-act-series-topic-3-personalized-advertising-and-pricing/)
- [Springer, "The Silent Death of EU Consumer Law and Its Resilient Revival" (2025)](https://link.springer.com/article/10.1007/s10603-025-09590-5)
- [ICLG, "Consumer Protection 2025-2026: Everyone Has a Price"](https://iclg.com/practice-areas/consumer-protection-laws-and-regulations/01-everyone-has-a-price-the-impact-of-consumer-law-on-pricing-practices)

**Library**:
- [[intel-comparative-regulation]]
- [[surveillance-pricing-comparative-regulation]]
- [[baldwin-regulatory-strategies]]
- [[disclosure-regulation]]
- [[rights-and-liabilities-regulation]]
- [[competition-over-regulation]]
- [[code-as-regulation]]
- [[regulatory-topology-not-ladder]]
- [[government-capacities-regulation]]
- [[creative-compliance]]
- [[sp-new-york]]
- [[sp-california]]
- [[sp-china]]
