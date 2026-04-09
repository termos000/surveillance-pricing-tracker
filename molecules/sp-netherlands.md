---
date-created: "202602251900"
aliases:
  - "Netherlands surveillance pricing profile"
tags:
  - "#molecules"
  - "#jurisdiction-profile"
topic:
  - "[[surveillance-pricing]]"
  - "[[Netherlands]]"
---

# Netherlands — Surveillance Pricing Regulatory Profile


The Netherlands layers a distinctive national regulatory architecture on top of the [[sp-eu|EU baseline]]. Where the EU provides the general framework (GDPR, CRD, UCPD, AI Act, DMA), the Netherlands adds three things the EU alone does not: a combined competition-and-consumer-protection authority (ACM) that has launched the first EU national-level market investigation specifically into computer-controlled consumer pricing (aviation sector, 2025); a financial sector regulator (AFM) that has produced the most developed supervisory framework for personalized pricing in insurance anywhere in the EU, including a 2021 exploratory study and a 2025 deep dive finding that almost half of non-life insurers charge loyal customers higher margins; and an institutional coordination infrastructure (the SDT platform and the AP's Department for the Coordination of Algorithmic Oversight) that connects the multiple regulators whose mandates touch algorithmic pricing. The design logic is accumulated but institutionally coordinated: the instruments come from different eras and legal bases, but the Netherlands has invested more than any other EU member state in making its regulators talk to each other about algorithms.

## Instruments

| Instrument | Strategy | Sector | Status | Enforcement |
|-----------|----------|--------|--------|-------------|
| Article 6:230m(1)(ea) BW (Omnibus Directive transposition, eff. May 28, 2022) — personalized pricing disclosure | Disclosure ([[disclosure-regulation]]) | General (distance and off-premises contracts) | Operative | ACM; fines up to EUR 900,000 or 1% of turnover |
| Section 6:193a-j BW (UCPD implementation) — unfair commercial practices | Disclosure | General (B2C) | Operative | ACM; fines; private actions for damages or contract termination |
| ACM Leidraad Bescherming Online Consument (2020, updated May 2024) — online consumer protection guidelines | Disclosure / Self-regulation ([[self-regulation]]) | Digital (B2C online) | Operative (soft law) | ACM (underlying hard law); guidance function |
| ACM Leidraad Prijsweergave en -vergelijkingen (Sept 19, 2025) — price display guidelines | Disclosure | General (B2C retail) | Operative (soft law) | ACM (underlying hard law); fines up to EUR 900,000 or 1% of turnover |
| Besluit prijsaanduiding producten (Price Indication Decree, eff. Jan 1, 2023) — 30-day prior price rule | Disclosure | General (B2C retail) | Operative | ACM; fines up to EUR 900,000 or 1% of turnover |
| Mededingingswet (Mw) — Dutch Competition Act (Articles 6, 24) | Competition ([[competition-over-regulation]]) | General | Operative | ACM; fines up to 10% of global turnover; private damages actions |
| ACM Market Investigation — Computer-Controlled Consumer Prices in Aviation (2025) | Competition / Disclosure (market study) | Aviation (pilot sector) | Ongoing (draft report expected early 2026) | ACM (non-binding recommendations; may trigger enforcement) |
| UAVG (Uitvoeringswet AVG) — GDPR Implementation Act | Rights & liabilities ([[rights-and-liabilities-regulation]]) | General | Operative | AP (Autoriteit Persoonsgegevens); fines per GDPR schedule |
| AFM Exploratory Study on Personalized Pricing in Insurance (June 2021) | Disclosure / Self-regulation (supervisory guidance) | Insurance | Published (soft law) | AFM (underlying Wft obligations) |
| AFM Deep Dive: Margin Personalisation — Fair Premium for Loyal Policyholders (April 8, 2025) | Disclosure / Self-regulation (supervisory guidance) | Insurance (non-life) | Published (soft law, call to action) | AFM (underlying Wft obligations; product governance standards) |
| DNB Sector Update: AI at Insurers (March 2025) | Self-regulation (supervisory expectations) | Insurance | Published (soft law) | DNB (prudential supervision) |
| AP as Coordinating AI Supervisor / DCA (est. 2023) | Code-as-regulation ([[code-as-regulation]]) / institutional coordination | General (algorithms and AI) | Operative (coordination role; AI Act market surveillance pending formal designation) | AP; coordination with ACM, AFM, RDI, CvdM |
| SDT — Samenwerkingsplatform Digitale Toezichthouders (est. Oct 2021) | Institutional coordination | Digital (cross-sectoral) | Operative | Non-binding; participating authorities: ACM, AP, AFM, CvdM |

## Detail

### Article 6:230m(1)(ea) BW — Personalized Pricing Disclosure (eff. May 28, 2022)

The Netherlands transposed the Omnibus Directive's personalized pricing disclosure obligation (CRD Art. 6(1)(ea)) through the Implementatiewet richtlijn modernisering consumentenbescherming (Stb. 2022, 157), which amended Book 6 of the Burgerlijk Wetboek (BW), the Wet handhaving consumentenbescherming (Whc), and the Prijzenwet (Pw). Article 6:230m(1)(ea) BW requires traders to inform consumers, before a distance or off-premises contract is concluded, when the price has been personalized on the basis of automated decision-making.

**Scope and limitations.** The obligation mirrors the Omnibus Directive: it applies only to distance and off-premises contracts, not to in-store retail. Traders must disclose the fact of personalization, not the mechanism, the data used, or the magnitude of the price difference. Dynamic pricing that responds to general market demand or supply conditions without using personal data is not covered. The Netherlands did not exercise the member state option to impose stricter transparency requirements beyond the Directive minimum.

**Enforcement architecture.** The ACM enforces consumer protection provisions under the Whc. Violations can result in fines of up to EUR 900,000 or, if higher, 1% of the trader's annual turnover. This is significantly higher than Germany's PAngV maximum of EUR 25,000 for comparable violations, reflecting the ACM's broader enforcement mandate. Consumers affected by unfair commercial practices can also seek damages or contract termination under Article 6:193j BW.

**No enforcement actions.** As of February 2026, no enforcement action specifically targeting failure to disclose personalized pricing under Article 6:230m(1)(ea) BW has been identified. The provision has been operative for nearly four years.

**Primary**: [Implementatiewet richtlijn modernisering consumentenbescherming (Stb. 2022, 157)](https://zoek.officielebekendmakingen.nl/stb-2022-157.html); [Tweede Kamer dossier 35940](https://www.tweedekamer.nl/kamerstukken/wetsvoorstellen/detail?id=2021Z17824&dossier=35940); [Dutch Civil Code Book 6 (English translation)](http://www.dutchcivillaw.com/civilcodebook066.htm)

**Secondary**: [Bird & Bird, "Netherlands — Omnibus Directive" country page](https://www.twobirds.com/en/trending-topics/omnibus-directive/omnibus-directive-countries/netherlands); [NautaDutilh, "Implementation Bill for Modernising Consumer Protection"](https://www.nautadutilh.com/en/insights/implementation-bill-for-modernising-consumer-protection/); [CMS, "Netherlands to Issue New Rules on Price Reduction Announcements" (2022)](https://cms.law/en/nld/publication/netherlands-to-issue-new-rules-on-price-reduction-announcements); [Fieldfisher, "New Consumer Protection Rules in the Netherlands"](https://www.fieldfisher.com/en/insights/new-consumer-protection-rules-in-the-netherlands); [ICLG, "Consumer Protection 2025-2026: Netherlands"](https://iclg.com/practice-areas/consumer-protection-laws-and-regulations/netherlands)

### Section 6:193a-j BW — Unfair Commercial Practices (UCPD Implementation)

The Unfair Commercial Practices Directive (2005/29/EC) was transposed into Section 3A, Title 3 of Book 6 of the Dutch Civil Code. Article 6:193c BW prohibits misleading commercial practices, and Article 6:193d BW prohibits misleading omissions where material information is withheld from consumers. Non-disclosure of personalized pricing could constitute a misleading omission under Article 6:193d, providing a parallel enforcement pathway to the Article 6:230m disclosure obligation.

**Consumer remedies.** Under Article 6:193j BW, consumers who are affected by unfair commercial practices can demand compensation (damages) or terminate the sales contract, resulting in a refund. This private action right supplements the ACM's public enforcement powers and is structurally stronger than Germany's PAngV fine-only mechanism.

**Relevance.** The UCP provisions function as background law for surveillance pricing rather than a targeted instrument. Their significance lies in the private action right, which creates a decentralized enforcement mechanism available even when the ACM does not act.

**Primary**: [Dutch Civil Code Book 6, Section 3A (English translation)](https://www.g-regs.com/downloads/NLChap6.3.3ADCCUnfairCommPracWRedit.pdf); [Deceptive Design, "Section 6.3.3A of the Dutch Civil Code"](https://www.deceptive.design/laws/section-6-3-3a-of-the-dutch-civil-code-unfair-commercial-practices)

**Secondary**: [Business.gov.nl, "Unfair Trading Practices"](https://business.gov.nl/regulations/unfair-trading-practices/); [ICLG, "Consumer Protection 2025-2026: Netherlands"](https://iclg.com/practice-areas/consumer-protection-laws-and-regulations/netherlands)

### ACM Leidraad Bescherming Online Consument (2020, updated May 2024) — Online Consumer Protection Guidelines

The ACM published the Leidraad Bescherming Online Consument in February 2020, with a substantial update in May 2024 incorporating the Consumer Rights Directive Implementation Act and the Digital Services Act. The guideline explains how the ACM applies consumer legislation to online influence of purchasing decisions.

**Personalized pricing provisions.** The guidelines explicitly address personalized pricing: if prices are personalized, traders must inform consumers about this before the purchase. The 2024 update also addresses dynamic pricing, scarcity indications, nudging, social proof, and dark patterns, defining the boundary between permissible persuasion and prohibited deception in online contexts.

**Legal status.** Soft law. The guidelines do not create new legal obligations but articulate the ACM's interpretation of existing provisions (Articles 6:193a-j and 6:230m BW). They signal enforcement priorities and provide compliance guidance.

**Significance.** The Leidraad is the most detailed Dutch guidance document on how consumer protection rules apply to algorithmic and personalized pricing practices online. Its practical importance exceeds its formal status: businesses use it as a compliance benchmark, and the ACM references it in enforcement actions.

**Primary**: [ACM, Leidraad Bescherming Online Consument (May 2024 version, PDF)](https://www.acm.nl/system/files/documents/leidraad-bescherming-online-consument.pdf); [ACM, "ACM Publishes Update to the Rules Regarding Online Deception"](https://www.acm.nl/en/publications/acm-publishes-update-rules-regarding-online-deception)

**Secondary**: [De Brauw, "Dutch Regulator Guidelines on Online Consumer Protection"](https://www.debrauw.com/articles/dutch-regulator-guidelines-on-online-consumer-protection-what-these-mean-in-practice); [GALA Law Blog, "ACM Issues Guidance on Influencing Online Buying Behavior"](http://blog.galalaw.com/post/102fym4/netherlands-authority-for-consumers-markets-acm-issues-guidance-on-influencin)

### ACM Leidraad Prijsweergave en -vergelijkingen (Sept 19, 2025) — Price Display and Comparison Guidelines

The ACM published the Leidraad Prijsweergave en -vergelijkingen on September 19, 2025, providing rules and practical examples for price display and price comparisons. The guidelines respond to widespread non-compliance with the 30-day prior price rule, evidenced by the ACM's May 2024 fake discount fines.

**Key rules.** Only the lowest previous price in the preceding 30 days may be used as a crossed-out reference price. Price reduction techniques (percentage discounts, euro-amount discounts, "was" prices) are not permitted if the reference price is not the lowest previous price. Discounts lasting longer than three months are considered excessive.

**Personalized pricing.** The guidelines address personalized discounts within loyalty programs and conditional offers but, notably, do not fully elaborate the ACM's position on how the 30-day prior price rule interacts with personalized pricing. The European Commission's guidelines on the Omnibus Directive contain exceptions for personalized discounts that the ACM does not explicitly address, leaving some interpretive ambiguity.

**Legal status.** Soft law. The guidelines interpret the Besluit prijsaanduiding producten (Price Indication Decree), which implements the EU Omnibus Directive's price indication rules.

**Primary**: [ACM, Leidraad Prijsweergave en -vergelijkingen (PDF)](https://www.acm.nl/system/files/documents/acm-leidraad-prijsweergave-en-vergelijkingen.pdf); [ACM, Leidraad Prijsweergave publication page](https://www.acm.nl/nl/publicaties/leidraad-prijsweergave-en-vergelijkingen)

**Secondary**: [Osborne Clarke, "Dutch Consumer Protection Authority Publishes Guidelines on Price Indications and Comparisons"](https://www.osborneclarke.com/insights/dutch-consumer-protection-authority-publishes-guidelines-price-indications-and-comparisons); [CMS, "Nieuwe ACM-Leidraad: Let op Prijsinformatie!" (2025)](https://cms.law/nl/nld/publication/nieuwe-acm-leidraad-let-op-prijsinformatie); [GALA Law Blog, "New Guidelines for Price Indications and Comparisons"](https://blog.galalaw.com/post/102lq09/new-guidelines-for-price-indications-and-comparisons-acm-publishes-guidance); [Maverick Advocaten, "ACM Opts for Stricter Approach"](https://www.maverick-law.com/en/blogs/acm-opts-for-stricter-approach-more-supervision-of-fake-discounts-in-consumer-sales.html)

### Besluit prijsaanduiding producten (Price Indication Decree, eff. Jan 1, 2023)

The Besluit prijsaanduiding producten implements the Omnibus Directive's prior-price requirements, establishing that when a trader announces a price reduction, the reference "from" price must be the lowest price the trader charged in the preceding 30 days. This entered into force on January 1, 2023, after the main Omnibus transposition provisions took effect on May 28, 2022.

**Relevance to surveillance pricing.** The 30-day rule targets a specific dark pattern in dynamic pricing: raising prices before a sale event to create the appearance of a larger discount. It does not directly regulate personalized pricing, but it constrains one practice that algorithmic pricing systems facilitate.

**Primary**: [Besluit prijsaanduiding producten (Overheid.nl)](https://wetten.overheid.nl/BWBR0046582)

**Secondary**: [CMS, "Netherlands to Issue New Rules on Price Reduction Announcements" (2022)](https://cms.law/en/nld/publication/netherlands-to-issue-new-rules-on-price-reduction-announcements); [Kennedy Van der Laan, "Explanation of Price Reductions"](https://kvdl.com/en/articles/uitleg-bij-prijsverlagingen)

### Mededingingswet (Mw) — Dutch Competition Act

The Mededingingswet prohibits anti-competitive agreements (Article 6 Mw, paralleling TFEU Article 101) and abuse of a dominant position (Article 24 Mw, paralleling TFEU Article 102). The ACM enforces these provisions alongside the European Commission.

**Relevance to algorithmic pricing.** Article 6 Mw reaches algorithmic collusion, including the use of shared pricing algorithms by competitors (paralleling the US RealPage theory and the EU Horizontal Guidelines paragraph 379). Article 24 Mw could reach exploitative personalized pricing by a dominant firm. The ACM's combined competition-and-consumer-protection mandate means it can pursue algorithmic pricing practices through whichever channel is most effective, without the institutional fragmentation that constrains enforcement in some other jurisdictions.

**No enforcement actions on algorithmic pricing.** As of February 2026, the ACM has not brought a competition enforcement action specifically targeting algorithmic pricing or personalized pricing. The market investigation into aviation pricing (below) is a market study, not a competition enforcement proceeding.

**Primary**: [Mededingingswet (English summary)](https://www.acm.nl/en/about-acm/mission-vision-strategy/legislation)

**Secondary**: [Simmons & Simmons, "Netherlands Competition Regulator's Strategic Focus for 2025" (2025)](https://www.simmons-simmons.com/en/publications/cm6t6pbzt000ctfm0hbe6gn7i/the-netherlands-competition-regulator-s-strategic-focus-for-2025)

### ACM Market Investigation — Computer-Controlled Consumer Prices in Aviation (2025)

In 2025, the ACM launched a market investigation into computer-controlled consumer prices in the Dutch aviation sector. This is the first EU national-level market investigation specifically examining how algorithmic pricing operates in practice and affects consumers.

**Scope and definitions.** The ACM distinguishes between two forms of computer-controlled pricing: dynamic pricing, where prices change in response to demand and supply conditions (e.g., higher prices during high season) and are the same for every consumer at a given moment; and personalized pricing, where different consumers face different prices for the same product at the same time, achieved through the use of individual consumer data such as search history, location, or device type. This definitional distinction is itself analytically significant, tracking the distinction that matters for surveillance pricing regulation.

**Why aviation.** The ACM selected aviation because plane ticket prices are well-known to vary considerably, data can be easily collected, and the sector is considered socially relevant. The ACM notes that findings may extend beyond aviation to other sectors with computer-controlled consumer prices.

**Research methodology.** The ACM published a research methods and consultation document (ACM/UIT/651935) inviting consumers, businesses, scholars, and other stakeholders to share opinions on the research methods through July 31, 2025. The investigation aims to understand how prices are actually formed in practice and what consequences this has for consumers.

**Timeline.** The ACM planned to publish provisional results and recommendations by the end of 2025, with a draft report expected in early 2026. As of February 2026, the final report has not been publicly released.

**Significance.** This investigation represents the Netherlands' most direct engagement with surveillance pricing as a regulatory concern. Its framing (understanding "how computer-controlled consumer prices are actually formed in practice") signals a fact-finding orientation rather than a presumption of harm, which could lead to either enforcement action or regulatory recommendations depending on findings. The ACM's own emphasis that findings may extend beyond aviation signals an intention to develop a broader analytical framework for computer-controlled pricing.

**Primary**: [ACM, "Market Investigation into Computer-Controlled Consumer Prices in the Airline Sector: Research Methods and Consultation"](https://www.acm.nl/en/publications/acm-market-investigation-computer-controlled-consumer-prices-airline-sector-research-methods-and-consultation); [ACM, Research Methods and Consultation Document (PDF)](https://www.acm.nl/system/files/documents/research-methods-and-consultation-of-market-investigation-into-computer-controlled-consumer-prices-in-the-aviation-sector_1.pdf); [ACM, "ACM in 2025 to Launch Five New Broad Investigations into Market Problems"](https://www.acm.nl/en/publications/acm-2025-launch-five-new-broad-investigations-market-problems)

**Secondary**: [Taylor Wessing, "ACM Investigates Dynamic Pricing of Airline Tickets" (Sept 2025)](https://www.taylorwessing.com/en/insights-and-events/insights/2025/09/acm-investigates-dynamic-pricing-of-airline-tickets); [Wilson Sonsini, "2026 Antitrust Year in Preview: Algorithmic Pricing" (Jan 2026)](https://www.wsgr.com/en/insights/2026-antitrust-year-in-preview-algorithmic-pricing.html); [Cleary Gottlieb, "The Comeback of Sectoral Investigations: Dutch and Belgian Competition Authority Announce Probes" (Feb 2025)](https://www.clearyantitrustwatch.com/2025/02/the-comeback-of-sectoral-investigations-the-dutch-and-belgian-competition-authority-announce-probes/)

### UAVG — Uitvoeringswet Algemene verordening gegevensbescherming (GDPR Implementation Act)

The UAVG implements the GDPR in the Netherlands and exercises national derogations where the GDPR permits member state flexibility. The UAVG extends the scope of automated individual decision-making provisions beyond the GDPR minimum, making the Netherlands one of the EU member states with a broader national implementation of Article 22.

**Extended automated decision-making scope.** The UAVG expands the scope of GDPR Article 22's protections beyond what the Regulation itself requires. The precise extent of this expansion and its application to personalized pricing has not been tested in enforcement or litigation, but the broader national implementation creates a potentially stronger foundation for challenging algorithmic pricing decisions than the GDPR baseline alone.

**Article 41 UAVG.** Implements GDPR Article 23 (restrictions on data subject rights) in the Netherlands, specifying the conditions under which automated decision-making protections may be restricted.

**Enforcement.** The Autoriteit Persoonsgegevens (AP) is the supervisory authority. The AP has not taken enforcement action applying GDPR Article 22 or UAVG provisions to personalized consumer pricing.

**AP's enforcement priorities.** The AP identified four key enforcement areas for 2024: algorithms and AI, Big Tech, freedom and security, and data trading and digital government. Algorithmic pricing falls within the algorithms and AI priority, but the AP's enforcement focus has been on other algorithmic practices (biometric data processing, emotion recognition) rather than pricing.

**Primary**: [UAVG (wetten.nl)](https://wetten.overheid.nl/BWBR0040940); [Autoriteit Persoonsgegevens, "Automated Decision"](https://www.autoriteitpersoonsgegevens.nl/en/themes/algorithms-ai/algorithms-explained/automated-decision)

**Secondary**: [GDPRhub, "Data Protection in the Netherlands"](https://gdprhub.eu/Data_Protection_in_the_Netherlands); [Velotix, "Netherlands Data Protection Act (UAVG): What You Need to Know"](https://www.velotix.ai/privacy-regulations/netherlands-data-protection-act-uavg/); [Linklaters, "Data Protected — Netherlands"](https://www.linklaters.com/en/insights/data-protected/data-protected---netherlands); [CMS, "Data Protection Laws and GDPR Enforcement in the Netherlands"](https://cms.law/en/nld/publication/gdpr-enforcement-tracker-report/netherlands); [ICLG, "Data Protection 2024-2025: Netherlands"](https://iclg.com/practice-areas/data-protection-laws-and-regulations/netherlands)

### AFM Exploratory Study on Personalized Pricing in Insurance (June 2021)

In June 2021, the Autoriteit Financiele Markten (AFM) published an exploratory study on the personalization of prices and conditions in the insurance sector ("Gepersonaliseerde beprijzing"). The study presented nine points of attention for insurers.

**Key findings.** The AFM found that behavioral pricing (using data on actual consumer behavior, such as driving patterns, to set premiums) had begun making inroads in the Dutch insurance market, though adoption was still in its infancy compared to the US and UK. Measuring car speed and braking behavior was one example, but the AFM noted this could expand to include where and when people drive, effectively creating continuous behavioral surveillance for pricing.

**Nine points of attention.** The AFM identified concerns including: personalization and price differentiation are difficult for consumers to recognize; behavioral pricing can lead to lower premiums for safe behavior but also to greater uninsurability and less transparent markets; and the expanding scope of data collection raises questions about proportionality and consumer consent.

**Significance.** This study makes the Netherlands one of the few jurisdictions where a financial regulator has proactively examined personalized pricing before widespread adoption, rather than reacting to complaints or market failures after the fact. The study is soft law (guidance, not regulation), but it established the AFM's supervisory posture and laid the groundwork for the 2025 deep dive.

**Primary**: [AFM, "The Personalisation of Prices and Conditions in the Insurance Sector" (2021, PDF)](https://www.afm.nl/~/profmedia/files/nieuws/2021/gepersonaliseerde-beprijzing.pdf?sc_lang=en); [AFM, "Points of Attention for Personalisation of Premiums and Conditions" (June 2021)](https://www.afm.nl/en/sector/actueel/2021/juni/aandachtspunten-gepersonaliseerde-beprijzing)

**Secondary**: [AFM, "Opportunities and Risks of the Digitalising Insurance Market over the Next Decade" (April 2023)](https://www.afm.nl/en/sector/actueel/2023/april/kansen-risico-digitalisering-verzekeringsmarkt)

### AFM Deep Dive: Margin Personalisation — Fair Premium for Loyal Policyholders (April 8, 2025)

The AFM published an analysis report titled "A Fair Premium for Loyal Policyholders" on April 8, 2025, based on a deep dive into margin personalisation practices among 18 Dutch non-life insurers representing 31 brands across three product groups: private cars (27 brands), home contents (28 brands), and liability insurance (26 brands).

**Definition of margin personalisation.** An insurer personalizes the profit margin when it has a higher margin on certain customers or groups of customers, where the price differences are not explained by differences in risk profile. This is distinct from risk-based price differentiation (where premium differences reflect actuarial risk): margin personalisation means charging more to some customers simply because the insurer can, not because they cost more.

**Key findings.** Almost half of the non-life insurers examined had higher profit margins on loyal customers in at least one product group. For private car insurance, 19-30% of brands showed higher average profit margins for loyal customers than for newer customers. For home contents insurance, 23% of brands showed the same pattern. The increased profit margin was often more than 10% when comparing customer groups with 1-2 years of tenure to those with 9 or more years. News reports indicated the "loyalty penalty" could mean approximately EUR 150 extra per year for car insurance.

**Regulatory implications.** The AFM stated that if loyal customers pay higher premiums without any difference in risk profile, or for no other valid reason, this may represent a violation of the legal standards on product governance under the Wet op het financieel toezicht (Wft). The AFM issued a "call to insurers" to ensure fair premiums for loyal customers.

**Connection to EIOPA.** The AFM's investigation followed EIOPA's supervisory statement on differential pricing practices from February 2023, making the Dutch deep dive one of the most thorough national follow-ups to the European-level concern.

**Significance.** The AFM's margin personalisation findings are directly relevant to surveillance pricing. Margin personalisation in insurance is structurally identical to surveillance pricing in retail: using data about individual consumers (here, tenure and renewal behavior rather than browsing history) to extract higher prices from consumers who are less likely to shop around. The AFM's willingness to characterize this as a potential Wft violation is the strongest regulatory signal in the Netherlands that data-driven price differentiation not justified by cost differences is problematic.

**Primary**: [AFM, "A Fair Premium for Loyal Policyholders" (April 8, 2025, PDF)](https://www.afm.nl/~/profmedia/files/rapporten/2025/deep-dive-margepersonalisatie-en.pdf); [AFM, "Call to Insurers: Ensure a Fair Premium for Loyal Customers" (April 2025)](https://www.afm.nl/en/sector/actueel/2025/apr/sb-margepersonalisatie)

**Secondary**: [WTW, "A Response to AFM's Call to Insurers: Ensuring Fair Premiums for Loyal Customers" (May 2025)](https://www.wtwco.com/en-nl/insights/2025/05/a-response-to-afms-call-to-insurers-ensuring-fair-premiums-for-loyal-customers); [DutchNews.nl, "'Loyalty Penalty' Could Mean EUR 150 Extra for Car Insurance: AFM" (April 2025)](https://www.dutchnews.nl/2025/04/loyalty-penalty-could-mean-e150-extra-for-car-insurance-afm/)

### DNB Sector Update: AI at Insurers (March 2025)

De Nederlandsche Bank (DNB) published a sector update titled "AI at Insurers: Opportunities and Risks" in March 2025, outlining supervisory expectations for AI use in the insurance sector based on a 2024 survey of 36 insurers.

**Key findings.** Of 36 insurers surveyed, 15 were already applying AI in business processes, including for risk assessment, personalized product recommendations, fraud detection, and claims processing. DNB emphasized that AI implementation should not undermine fair treatment of customers or introduce biases into decision-making processes, and that insurers must consider the societal impacts of personalized pricing strategies and maintain appropriate levels of solidarity in insurance risk pooling.

**Fairness framework.** DNB expects insurers to define fairness within their specific context and demonstrate that their AI models adhere to these criteria, which may involve comprehensive bias audits and diverse datasets for model training. The emphasis on maintaining "solidarity in insurance risk pooling" is directly relevant to surveillance pricing: excessive price personalization in insurance can erode the pooling function that makes insurance markets work.

**Significance.** The DNB guidance focuses on prudential supervision (financial soundness) rather than consumer protection, but its emphasis on fairness and solidarity creates an additional supervisory expectation for insurers using algorithmic pricing. Combined with the AFM's consumer-facing work, this means Dutch insurers face algorithmic pricing scrutiny from both their prudential and conduct supervisors.

**Primary**: [DNB, "AI at Insurers" (referenced in Stibbe analysis)](https://www.stibbe.com/publications-and-insights/dnbs-ai-guidance-balancing-innovation-with-prudence)

**Secondary**: [Stibbe, "DNB's AI Guidance: Balancing Innovation with Prudence" (2025)](https://www.stibbe.com/publications-and-insights/dnbs-ai-guidance-balancing-innovation-with-prudence)

### AP as Coordinating AI Supervisor / Department for the Coordination of Algorithmic Oversight (DCA)

Since 2023, the Autoriteit Persoonsgegevens (AP) has served as the coordinating supervisor for algorithms and AI in the Netherlands. The AP houses the Department for the Coordination of Algorithmic Oversight (DCA), which hosts the AI & Algorithm Chamber (Algoritme- en AI-Kamer, AAK) as an administrative consultation body within the Digital Regulation Cooperation Platform (SDT).

**Functions.** The DCA coordinates between Dutch regulators on algorithmic risks, prepares for new supervisory tasks under the EU AI Act, and publishes biannual reports on AI and algorithms in the Netherlands (Rapportage AI & Algoritmes Nederland, RAN). The DCA received EUR 1 million in initial funding in 2023, gradually increasing to EUR 3.6 million by 2026.

**AI Act market surveillance.** In November 2024, the AP and the Rijksinspectie Digitale Infrastructuur (RDI) published joint final advice recommending that the AP, RDI, DNB, and AFM be designated as market surveillance authorities for the EU AI Act. The AP would specifically supervise transparency obligations under the AI Act, given its existing role as coordinating algorithm supervisor and the connection between transparency obligations and personal data processing. Formal designation by the Ministry of Economic Affairs and the Ministry of Legal Protection was due by August 2, 2025.

**Relevance to pricing.** The DCA's mandate covers algorithmic systems broadly, including those used for pricing. However, the DCA's published outputs focus on broader algorithmic governance themes (transparency, non-discrimination, AI literacy) rather than pricing specifically. The coordination infrastructure creates a pathway through which pricing concerns raised by one regulator (e.g., the ACM's aviation investigation or the AFM's insurance findings) could be connected to data protection concerns (the AP's GDPR enforcement) in ways that fragmented regulatory systems cannot achieve.

**Primary**: [AP, "Coordination of Algorithmic and AI Supervision"](https://www.autoriteitpersoonsgegevens.nl/en/themes/algorithms-ai/coordination-of-algorithmic-and-ai-supervision); [AP, "Department for the Coordination of Algorithmic Oversight (DCA)"](https://www.autoriteitpersoonsgegevens.nl/en/themes/algorithms-ai/coordination-of-algorithmic-and-ai-supervision/department-for-the-coordination-of-algorithmic-oversight-dca); [AP/RDI, "Final Advice on the Supervisory Structure for the AI Act" (Nov 2024, PDF)](https://www.rdi.nl/site/binaries/site-content/collections/documenten/2024/11/7/final-advice-on-the-supervisory-structure-for-the-ai-act/Final+advice+supervisory+structure+AI+Act_AP_RDI.pdf); [AP, "Work Plan Oversight of AI and Algorithms 2025"](https://autoriteitpersoonsgegevens.nl/en/documents/work-plan-oversight-of-ai-and-algorithms-2025)

**Secondary**: [Knowledge Centre Data & Society, "Dutch Authorities Publish Final Advice on AI Authorities"](https://data-en-maatschappij.ai/en/publications/nederland-nederlandse-autoriteiten-publiceren-eindadvies-over-toezicht-op-ai); [GLACIS, "EU AI Act Netherlands Implementation Guide 2026"](https://www.glacis.io/guide-eu-ai-act-netherlands); [Chambers, "Artificial Intelligence 2025: Netherlands"](https://practiceguides.chambers.com/practice-guides/artificial-intelligence-2025/netherlands)

### SDT — Samenwerkingsplatform Digitale Toezichthouders (Digital Regulation Cooperation Platform, est. Oct 2021)

The SDT was established in October 2021 as a cooperation platform among four Dutch regulators: the ACM, the AP, the AFM, and the Commissariaat voor de Media (CvdM, Dutch Media Authority). In March 2023, the SDT expanded its collaboration and created two additional chambers: one for DSA enforcement coordination and one for oversight of algorithms and AI (the AAK, hosted by the AP's DCA).

**Focus areas.** The SDT's stated focus areas include artificial intelligence, algorithms and data processing, online design, online personalisation, online manipulation and deception. Online personalisation and online manipulation directly encompass surveillance pricing practices.

**Significance.** The SDT is the institutional innovation that distinguishes the Netherlands from most other jurisdictions in this survey. In many jurisdictions, competition authorities, data protection authorities, and financial regulators operate in institutional silos, each applying their own legal frameworks to algorithmic pricing without coordinating. The SDT creates a formal mechanism for the ACM (competition and consumer protection), the AP (data protection), the AFM (financial conduct), and the CvdM (media) to identify overlaps and coordinate responses. For surveillance pricing, this means the ACM's aviation pricing investigation, the AFM's insurance margin personalisation findings, and the AP's algorithmic governance work can inform each other through a structured coordination platform.

**Primary**: [ACM, "The Digital Regulation Cooperation Platform (SDT)"](https://www.acm.nl/en/about-acm/cooperation/national-cooperation/digital-regulation-cooperation-platform-sdt); [AP, "Cooperation"](https://www.autoriteitpersoonsgegevens.nl/en/about-the-ap/cooperation)

**Secondary**: [Hogan Lovells, "Dutch Regulators Join Forces for Supervision in the Digital Field" (2021)](https://www.hoganlovells.com/en/publications/dutch-regulators-join-forces-for-supervision-in-the-digital-field); [AFM, "SDT Members to Expand Their Collaboration Regarding Digital Regulation" (March 2023)](https://www.afm.nl/en/sector/actueel/2023/maart/uitbreiding-digitaal-toezicht-sdt)

## Analysis

**Hierarchy.** Disclosure dominates in formal terms but investigation leads in practice. The disclosure instruments (Article 6:230m(1)(ea) BW, Leidraad Bescherming Online Consument, Leidraad Prijsweergave) provide the only legally operative obligations specifically addressing personalized pricing, but none has been enforced. The ACM's aviation sector investigation is the most active engagement with algorithmic pricing but has not yet produced findings or recommendations. The AFM's insurance work is the most substantively developed, with empirical findings and a regulatory call to action, but operates in a single sector through soft-law guidance rather than enforcement orders. The hierarchy is therefore: disclosure (operative, unenforced) > investigation/soft law (active, ongoing) > competition (operative, not activated for pricing) > rights (operative, not activated for pricing) > institutional coordination (operative, enabling function).

The Netherlands does not have a Germany-style competition enforcement instrument (no equivalent to GWB Section 19a) that targets digital platform pricing directly. The Dutch instruments are structurally softer: guidelines, market investigations, and supervisory expectations rather than prohibition orders and disgorgement. This reflects a regulatory culture preference for guidance and dialogue over adversarial enforcement, which the ACM has explicitly articulated in its 2025 priorities.

**Design logic.** Accumulated but institutionally coordinated. The instruments come from different eras, legal bases, and institutional mandates: BW consumer protection (2022 Omnibus transposition), Mw competition law (1998/ongoing), UAVG data protection (2018/ongoing), AFM financial supervision (Wft), DNB prudential supervision, and the SDT/DCA coordination infrastructure (2021-2023). No single legislative moment designed these as a set for surveillance pricing. However, unlike most EU member states where the accumulation is uncoordinated, the Netherlands has invested in institutional infrastructure (the SDT and the DCA) specifically designed to connect the regulators whose mandates touch algorithmic systems. The coordination does not eliminate the accumulated character of the instruments, but it creates pathways for information sharing and joint analysis that are absent in most other jurisdictions.

**Institutional divergence.** The most distinctive feature of the Dutch system is the ACM's combined competition-and-consumer-protection mandate. The ACM was created in 2013 through the merger of the Netherlands Competition Authority (NMa), the Consumer Authority (CA), and the telecommunications regulator (OPTA). This means a single institution can pursue algorithmic pricing practices through competition law (Article 6 Mw, cartel prohibition; Article 24 Mw, abuse of dominance), consumer protection law (Articles 6:193a-j, 6:230m BW), and sector-specific regulation (telecommunications, energy, transport), choosing whichever legal basis is most effective without inter-agency coordination costs.

Compare this with Germany, where the Bundeskartellamt handles competition enforcement but consumer protection enforcement depends on state-level authorities (Landesverwaltungen) and private UWG actions, creating a structural gap between the aggressive competition enforcement and the weak consumer protection enforcement for personalized pricing. In the Netherlands, if the ACM's aviation investigation reveals consumer harm from personalized pricing, the same institution that conducted the investigation can bring either a competition enforcement action or a consumer protection enforcement action.

The trade-off is that the ACM must balance multiple mandates with limited resources. The AFM and DNB add sector-specific supervisory capacity for insurance, but general retail and e-commerce pricing falls to the ACM alone.

## Evidence

**ACM v. G-Star, JYSK, Tommy Hilfiger, Leen Bakker, Day Traders — fake discount fines (May 2024).** The ACM imposed fines totaling EUR 621,000 on five online stores for using misleading "was" prices that did not reflect the lowest price in the preceding 30 days. Individual fines: Day Traders (EUR 163,000), Leen Bakker (EUR 130,000), JYSK (EUR 112,500), G-Star (EUR 110,000), Tommy Hilfiger (EUR 105,500). This is not a personalized pricing case, but it demonstrates the ACM's willingness and capacity to enforce pricing transparency rules in e-commerce, and the penalty levels it applies. [ACM, "ACM Has Fined Online Stores for Using Fake Discounts"](https://www.acm.nl/en/publications/acm-has-fined-online-stores-using-fake-discounts); [NL Times, "Retailers Issued Fines for Offering Fake Discount Prices Online" (June 2024)](https://nltimes.nl/2024/06/12/retailers-issued-fines-offering-fake-discount-prices-online-netherlands)

**AFM margin personalisation findings (April 2025).** Almost half of 18 non-life insurers examined had higher profit margins on loyal customers in at least one product group. The profit margin differential was often more than 10%. The AFM characterized this as potentially violating product governance standards under the Wft. This is the strongest empirical evidence of surveillance pricing practices in the Netherlands, though in the insurance sector rather than general retail. [AFM sources cited above]

**AP fine against Clearview AI — EUR 30.5 million (Sept 2024).** The AP fined Clearview AI for processing biometric data without a legal basis and issued four enforcement orders effectively requiring the company to cease EU operations. While this case concerns facial recognition rather than pricing, it demonstrates the AP's enforcement capacity and willingness to impose substantial fines on algorithmic processing of personal data. [AP/EDPB, "Dutch Supervisory Authority Imposes a Fine on Clearview" (Sept 2024)](https://www.edpb.europa.eu/news/national-news/2024/dutch-supervisory-authority-imposes-fine-clearview-because-illegal-data_en)

**Hanspach, Sapi & Wieting — Bol.com algorithmic pricing study (2024).** The most rigorous empirical study of algorithmic pricing in the Dutch market, analyzing two months of high-frequency pricing data for over 2,800 products on Bol.com (the largest Dutch online marketplace). Key findings: algorithmic sellers are more likely to win the Buy Box (the most prominent product listing); prices are particularly high when two algorithms compete with a medium number of sellers; but with sufficient competitors, algorithmic sellers reduce prices and compete fiercely. The study found no robust evidence that algorithmic pricing is associated with higher average Buy Box prices overall, but it found that consumers face inflated prices more often because algorithmic sellers are more likely to win the Buy Box. [Hanspach, Sapi & Wieting, "Algorithms in the Marketplace: An Empirical Analysis of Automated Pricing in E-Commerce," Information Economics and Policy (2024)](https://www.sciencedirect.com/science/article/abs/pii/S0167624524000337)

**Bits of Freedom v. Meta — algorithmic feed ruling (Oct 2025).** A Dutch court ordered Meta to offer Dutch users an algorithm-free feed option, ruling that Meta's current design violates the Digital Services Act. Brought by Bits of Freedom, the Netherlands' leading digital rights organization. While the case concerns algorithmic content curation rather than pricing, it demonstrates the Dutch civil society infrastructure for challenging algorithmic practices and the willingness of Dutch courts to intervene in algorithmic design. [DutchNews.nl, "Court Tells Meta to Give Dutch Users Algorithm-Free Feed Option" (Oct 2025)](https://www.dutchnews.nl/2025/10/court-tells-meta-to-give-dutch-users-algorithm-free-feed-option/)

## Movement

The Netherlands' trajectory shows progressive institutional investment in algorithmic governance infrastructure, with pricing as an emerging focus area building on consumer protection and financial supervision foundations.

1. **2005-2012**: UCPD implemented in Book 6 BW, establishing baseline unfair commercial practices framework
2. **2012**: Dutch government issues "cookie law" requiring website owners to inform users about tracking, profiling, and personalization before the visit — early Dutch engagement with behavioral surveillance
3. **2013 (April 1)**: ACM created through merger of NMa (competition), CA (consumer protection), and OPTA (telecommunications) — establishes combined mandate that defines Dutch institutional architecture
4. **2018 (May 25)**: GDPR/UAVG take effect — UAVG extends automated decision-making scope beyond GDPR minimum
5. **2020 (Feb)**: ACM publishes Leidraad Bescherming Online Consument — first Dutch guidance addressing personalized pricing disclosure for online consumers
6. **2021 (June)**: AFM publishes exploratory study on personalized pricing in insurance — first EU financial regulator to proactively examine personalized pricing before widespread adoption
7. **2021 (Oct)**: SDT established — formal coordination platform connecting ACM, AP, AFM, and CvdM for digital regulation
8. **2022 (May 28)**: Omnibus Directive transposition takes effect — Article 6:230m(1)(ea) BW creates personalized pricing disclosure obligation
9. **2023 (Jan 1)**: Besluit prijsaanduiding producten takes effect — 30-day prior price rule for price reduction announcements
10. **2023**: AP's DCA receives initial funding (EUR 1 million) as coordinating AI supervisor; AAK (AI & Algorithm Chamber) created within SDT
11. **2024 (May)**: ACM fines five online stores EUR 621,000 for fake discounts — demonstrates pricing enforcement capacity
12. **2024 (May)**: ACM publishes updated Leidraad Bescherming Online Consument — incorporates CRD Implementation Act and DSA
13. **2024 (Sept)**: AP fines Clearview AI EUR 30.5 million — demonstrates algorithmic enforcement capacity
14. **2024 (Nov)**: AP and RDI publish joint final advice recommending AI Act market surveillance authority designations
15. **2025 (March)**: DNB publishes "AI at Insurers" sector update — fairness and solidarity expectations for algorithmic insurance pricing
16. **2025 (April)**: AFM publishes margin personalisation deep dive — finds loyalty penalty at nearly half of non-life insurers; issues call to action
17. **2025**: ACM launches market investigation into computer-controlled consumer prices in aviation — first EU national-level investigation specifically into algorithmic consumer pricing; stakeholder consultation closes July 31, 2025
18. **2025 (Sept)**: ACM publishes Leidraad Prijsweergave en -vergelijkingen — comprehensive price display guidelines
19. **2026 (expected)**: ACM aviation investigation draft report and recommendations; AP DCA funding reaches EUR 3.6 million; formal AI Act market surveillance authority designations

The trajectory reveals three concurrent developments. First, a progressive deepening of the ACM's engagement with algorithmic pricing, from general online consumer protection guidance (2020) through pricing enforcement capacity demonstration (2024 fake discount fines) to a dedicated market investigation (2025). Second, the AFM's independent development of insurance-specific personalized pricing supervision, from exploratory study (2021) to empirical deep dive with regulatory consequences (2025). Third, the construction of institutional coordination infrastructure (SDT 2021, DCA 2023, AAK 2023, AI Act designation advice 2024) that positions the Netherlands to connect these parallel streams.

What is absent from the trajectory is enforcement. No Dutch authority has enforced the personalized pricing disclosure obligation, applied GDPR Article 22 to pricing, or brought a competition case against algorithmic pricing. The Netherlands' contribution is institutional and analytical rather than enforcement-based. Whether the ACM's aviation investigation triggers a shift from analysis to enforcement remains the key question.

## Sources

**Primary**:
- [Implementatiewet richtlijn modernisering consumentenbescherming (Stb. 2022, 157)](https://zoek.officielebekendmakingen.nl/stb-2022-157.html)
- [Tweede Kamer dossier 35940 — Implementatiewet](https://www.tweedekamer.nl/kamerstukken/wetsvoorstellen/detail?id=2021Z17824&dossier=35940)
- [Dutch Civil Code Book 6 (English translation)](http://www.dutchcivillaw.com/civilcodebook066.htm)
- [Dutch Civil Code, Section 6:193a-j (Unfair Commercial Practices, English/PDF)](https://www.g-regs.com/downloads/NLChap6.3.3ADCCUnfairCommPracWRedit.pdf)
- [UAVG (wetten.nl)](https://wetten.overheid.nl/BWBR0040940)
- [ACM, Leidraad Bescherming Online Consument (May 2024, PDF)](https://www.acm.nl/system/files/documents/leidraad-bescherming-online-consument.pdf)
- [ACM, Leidraad Prijsweergave en -vergelijkingen (Sept 2025, PDF)](https://www.acm.nl/system/files/documents/acm-leidraad-prijsweergave-en-vergelijkingen.pdf)
- [ACM, "Market Investigation into Computer-Controlled Consumer Prices in the Airline Sector" (2025)](https://www.acm.nl/en/publications/acm-market-investigation-computer-controlled-consumer-prices-airline-sector-research-methods-and-consultation)
- [ACM, Research Methods and Consultation Document (PDF)](https://www.acm.nl/system/files/documents/research-methods-and-consultation-of-market-investigation-into-computer-controlled-consumer-prices-in-the-aviation-sector_1.pdf)
- [ACM, "ACM in 2025 to Launch Five New Broad Investigations into Market Problems"](https://www.acm.nl/en/publications/acm-2025-launch-five-new-broad-investigations-market-problems)
- [ACM, "ACM Has Fined Online Stores for Using Fake Discounts" (2024)](https://www.acm.nl/en/publications/acm-has-fined-online-stores-using-fake-discounts)
- [AFM, "The Personalisation of Prices and Conditions in the Insurance Sector" (2021, PDF)](https://www.afm.nl/~/profmedia/files/nieuws/2021/gepersonaliseerde-beprijzing.pdf?sc_lang=en)
- [AFM, "A Fair Premium for Loyal Policyholders" (April 2025, PDF)](https://www.afm.nl/~/profmedia/files/rapporten/2025/deep-dive-margepersonalisatie-en.pdf)
- [AP, "Coordination of Algorithmic and AI Supervision"](https://www.autoriteitpersoonsgegevens.nl/en/themes/algorithms-ai/coordination-of-algorithmic-and-ai-supervision)
- [AP, "Department for the Coordination of Algorithmic Oversight (DCA)"](https://www.autoriteitpersoonsgegevens.nl/en/themes/algorithms-ai/coordination-of-algorithmic-and-ai-supervision/department-for-the-coordination-of-algorithmic-oversight-dca)
- [AP/RDI, "Final Advice on the Supervisory Structure for the AI Act" (Nov 2024, PDF)](https://www.rdi.nl/site/binaries/site-content/collections/documenten/2024/11/7/final-advice-on-the-supervisory-structure-for-the-ai-act/Final+advice+supervisory+structure+AI+Act_AP_RDI.pdf)
- [ACM, "The Digital Regulation Cooperation Platform (SDT)"](https://www.acm.nl/en/about-acm/cooperation/national-cooperation/digital-regulation-cooperation-platform-sdt)

**Secondary**:
- [Bird & Bird, "Netherlands — Omnibus Directive"](https://www.twobirds.com/en/trending-topics/omnibus-directive/omnibus-directive-countries/netherlands)
- [NautaDutilh, "Implementation Bill for Modernising Consumer Protection"](https://www.nautadutilh.com/en/insights/implementation-bill-for-modernising-consumer-protection/)
- [CMS, "Netherlands to Issue New Rules on Price Reduction Announcements" (2022)](https://cms.law/en/nld/publication/netherlands-to-issue-new-rules-on-price-reduction-announcements)
- [Fieldfisher, "New Consumer Protection Rules in the Netherlands"](https://www.fieldfisher.com/en/insights/new-consumer-protection-rules-in-the-netherlands)
- [ICLG, "Consumer Protection 2025-2026: Netherlands"](https://iclg.com/practice-areas/consumer-protection-laws-and-regulations/netherlands)
- [Osborne Clarke, "Dutch Consumer Protection Authority Publishes Guidelines on Price Indications and Comparisons"](https://www.osborneclarke.com/insights/dutch-consumer-protection-authority-publishes-guidelines-price-indications-and-comparisons)
- [Maverick Advocaten, "ACM Opts for Stricter Approach" (2025)](https://www.maverick-law.com/en/blogs/acm-opts-for-stricter-approach-more-supervision-of-fake-discounts-in-consumer-sales.html)
- [De Brauw, "Dutch Regulator Guidelines on Online Consumer Protection"](https://www.debrauw.com/articles/dutch-regulator-guidelines-on-online-consumer-protection-what-these-mean-in-practice)
- [Taylor Wessing, "ACM Investigates Dynamic Pricing of Airline Tickets" (Sept 2025)](https://www.taylorwessing.com/en/insights-and-events/insights/2025/09/acm-investigates-dynamic-pricing-of-airline-tickets)
- [Wilson Sonsini, "2026 Antitrust Year in Preview: Algorithmic Pricing" (Jan 2026)](https://www.wsgr.com/en/insights/2026-antitrust-year-in-preview-algorithmic-pricing.html)
- [Cleary Gottlieb, "The Comeback of Sectoral Investigations" (Feb 2025)](https://www.clearyantitrustwatch.com/2025/02/the-comeback-of-sectoral-investigations-the-dutch-and-belgian-competition-authority-announce-probes/)
- [Simmons & Simmons, "Netherlands Competition Regulator's Strategic Focus for 2025"](https://www.simmons-simmons.com/en/publications/cm6t6pbzt000ctfm0hbe6gn7i/the-netherlands-competition-regulator-s-strategic-focus-for-2025)
- [GDPRhub, "Data Protection in the Netherlands"](https://gdprhub.eu/Data_Protection_in_the_Netherlands)
- [Velotix, "Netherlands Data Protection Act (UAVG)"](https://www.velotix.ai/privacy-regulations/netherlands-data-protection-act-uavg/)
- [Linklaters, "Data Protected — Netherlands"](https://www.linklaters.com/en/insights/data-protected/data-protected---netherlands)
- [CMS, "Data Protection Laws and GDPR Enforcement in the Netherlands"](https://cms.law/en/nld/publication/gdpr-enforcement-tracker-report/netherlands)
- [WTW, "A Response to AFM's Call to Insurers" (May 2025)](https://www.wtwco.com/en-nl/insights/2025/05/a-response-to-afms-call-to-insurers-ensuring-fair-premiums-for-loyal-customers)
- [DutchNews.nl, "'Loyalty Penalty' Could Mean EUR 150 Extra" (April 2025)](https://www.dutchnews.nl/2025/04/loyalty-penalty-could-mean-e150-extra-for-car-insurance-afm/)
- [Stibbe, "DNB's AI Guidance: Balancing Innovation with Prudence" (2025)](https://www.stibbe.com/publications-and-insights/dnbs-ai-guidance-balancing-innovation-with-prudence)
- [Hogan Lovells, "Dutch Regulators Join Forces for Supervision in the Digital Field" (2021)](https://www.hoganlovells.com/en/publications/dutch-regulators-join-forces-for-supervision-in-the-digital-field)
- [AFM, "SDT Members to Expand Collaboration" (March 2023)](https://www.afm.nl/en/sector/actueel/2023/maart/uitbreiding-digitaal-toezicht-sdt)
- [Knowledge Centre Data & Society, "Dutch Authorities Publish Final Advice on AI Authorities"](https://data-en-maatschappij.ai/en/publications/nederland-nederlandse-autoriteiten-publiceren-eindadvies-over-toezicht-op-ai)
- [GLACIS, "EU AI Act Netherlands Implementation Guide 2026"](https://www.glacis.io/guide-eu-ai-act-netherlands)
- [Chambers, "Artificial Intelligence 2025: Netherlands"](https://practiceguides.chambers.com/practice-guides/artificial-intelligence-2025/netherlands)
- [NL Times, "Retailers Issued Fines for Fake Discount Prices" (June 2024)](https://nltimes.nl/2024/06/12/retailers-issued-fines-offering-fake-discount-prices-online-netherlands)
- [DutchNews.nl, "Court Tells Meta to Give Dutch Users Algorithm-Free Feed Option" (Oct 2025)](https://www.dutchnews.nl/2025/10/court-tells-meta-to-give-dutch-users-algorithm-free-feed-option/)
- [Hanspach, Sapi & Wieting, "Algorithms in the Marketplace," Information Economics and Policy (2024)](https://www.sciencedirect.com/science/article/abs/pii/S0167624524000337)
- [Zuiderveen Borgesius & Poort, "Online Price Discrimination and EU Data Privacy Law," 40 J. Consumer Pol'y 347 (2017)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3009188)
- [Poort & Zuiderveen Borgesius, "Personalised Pricing: The Demise of the Fixed Price?" in Data-Driven Personalisation (CUP, 2021)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3792842)
- [Heidary, "An Empirical Legal Investigation of Online Price Discrimination" (PhD diss., Leiden University, 2025)](https://scholarlypublications.universiteitleiden.nl/access/item:4195837/view)
- [Heidary et al., "Discrimination Grounds and Personalised Pricing," Internet Policy Review (2024)](https://policyreview.info/articles/analysis/discrimination-grounds-and-personalised-pricing)
- [Jones Day, "Netherlands Launches New Consumer and Market Authority — The New Dutch Super Regulator" (April 2013)](https://www.jonesday.com/en/insights/2013/04/antitrust-alert--the-netherlands-launches-new-consumer-and-market-authority--the-new-dutch-super-regulator)
- [Taylor Wessing, "Most Notable Consumer Law Cases ACM 2024" (Feb 2025)](https://www.taylorwessing.com/en/insights-and-events/insights/2025/02/most-notable-consumer-law-cases-acm-2024)
- [Maverick Advocaten, "High Fines for Use of Dark Patterns and ACM Shuts Down Online Store"](https://www.maverick-law.com/en/blogs/high-fines-for-use-of-dark-patterns-and-acm-shuts-down-online-store-due-to-misleading-practices.html)
