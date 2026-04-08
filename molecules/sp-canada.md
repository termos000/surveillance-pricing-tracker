---
date-created: "202602251800"
aliases:
  - "Canada surveillance pricing profile"
tags:
  - "#molecules"
  - "#jurisdiction-profile"
topic:
  - "[[surveillance pricing]]"
  - "[[Canada]]"
---

# Canada — Surveillance Pricing Regulatory Profile

*Jurisdiction molecule for [[surveillance-pricing-comparative-regulation|Paper 1]].*

Canada has no instrument specifically designed for surveillance pricing, but its regulatory landscape is in active motion. The Competition Act, substantially amended in 2022 and 2024, provides the most developed enforcement infrastructure through drip pricing prohibition, expanded abuse of dominance provisions, and civil competitor collaboration tools that can reach algorithmic coordination. Federal privacy law (PIPEDA) applies general consent and purpose limitation principles but lacks automated decision-making provisions. The most significant development is the Competition Bureau's June 2025 discussion paper on algorithmic pricing and its January 2026 "What We Heard" report, which represent Canada's most direct institutional engagement with surveillance pricing to date. The death of Bill C-27 in January 2025 left Canada without a federal automated decision-making framework or AI regulation, though Quebec's Law 25 provides provincial-level automated decision-making rights that are directly relevant. The overall design logic is accumulated: instruments from different eras, agencies, and legal bases (competition, privacy, consumer protection, provincial legislation) with no coordination and a growing awareness that the existing framework may not reach the core practice.

## Instruments

| Instrument | Strategy | Sector | Status | Enforcement |
|-----------|----------|--------|--------|-------------|
| Competition Act, s. 74.01(1.1) — Drip Pricing Prohibition (2022, strengthened 2024) | Command and control ([[command-and-control]]) | General (all commercial sectors) | Operative | Competition Bureau (Commissioner); Competition Tribunal; AMPs up to CAD $10M first offence or 3% global turnover; private right of action (eff. June 2025) |
| Competition Act, s. 45 — Criminal Conspiracy (price-fixing) | Command and control ([[command-and-control]]) | General | Operative (untested for algorithmic collusion) | Competition Bureau; criminal prosecution; imprisonment up to 14 years; fines up to CAD $25M |
| Competition Act, s. 90.1 — Civil Competitor Collaboration (amended 2024) | Competition ([[competition-over-regulation]]) | General | Operative | Competition Bureau; Competition Tribunal; expanded to non-competitors if significant purpose is lessening competition |
| Competition Act, ss. 78-79 — Abuse of Dominance (amended 2024) | Competition ([[competition-over-regulation]]) | General | Operative | Competition Bureau; Competition Tribunal; AMPs up to 3% global turnover; excessive pricing now an enumerated anti-competitive act |
| Competition Act, s. 74.01(1) — Deceptive Marketing (false/misleading representations) | Disclosure ([[disclosure-regulation]]) | General | Operative | Competition Bureau; Competition Tribunal; AMPs up to CAD $10M (first) / $15M (subsequent) or 3% global turnover; private right of action (eff. June 2025) |
| PIPEDA — Consent and Purpose Limitation Principles | Rights & liabilities ([[rights-and-liabilities-regulation]]) | Private sector commercial activity (federal) | Operative | Office of the Privacy Commissioner (OPC); findings and recommendations (non-binding); Federal Court enforcement; no direct AMP power |
| Quebec Law 25 — Automated Decision-Making (s. 12.1, eff. Sept 2023) | Rights & liabilities ([[rights-and-liabilities-regulation]]) | Private sector (Quebec) | Operative | Commission d'acces a l'information du Quebec (CAI); AMPs up to CAD $25M or 4% global turnover |
| Treasury Board Directive on Automated Decision-Making (2019, amended 2023) | Code-as-regulation ([[code-as-regulation]]) | Federal government only | Operative (government sector only) | Treasury Board Secretariat; internal compliance; Algorithmic Impact Assessment mandatory |
| Competition Bureau — Algorithmic Pricing Discussion Paper (June 2025) / What We Heard Report (Jan 2026) | Disclosure (soft — consultation) | General | Consultative (no binding effect) | N/A — policy development stage |

## Detail

### Competition Act, s. 74.01(1.1) — Drip Pricing Prohibition (2022, strengthened June 2024)

Canada is one of the first jurisdictions to enact a statutory prohibition on drip pricing. Section 74.01(1.1) was introduced by the 2022 amendments and prohibits making a representation to the public in any form whatever that the price of a product or service is a given amount when the amount is unattainable due to fixed obligatory charges or fees. The June 2024 amendments (Bill C-59) strengthened this by clarifying that the only fees that may be excluded from the upfront price are those "imposed on a purchaser" by federal or provincial statute (e.g., sales tax). All other mandatory charges must be included in the headline price.

**Relevance to surveillance pricing.** Drip pricing and personalized pricing are distinct practices but share an information asymmetry structure: both involve the consumer seeing a price that does not reflect the actual cost they will bear. Where a personalized pricing algorithm adds fees, surcharges, or adjustments that are not disclosed upfront, the drip pricing prohibition could apply. However, a price that is personalized from the outset (i.e., the consumer sees only their individualized price with no incremental additions) would not constitute drip pricing under s. 74.01(1.1). The provision targets price disaggregation, not price individualization.

**Enforcement.** First-time corporate violations carry AMPs up to the greater of CAD $10 million or three times the benefit derived from the conduct; if the benefit cannot be determined, up to 3% of the corporation's annual worldwide gross revenues. The Competition Tribunal ordered CAD $38.9 million against Cineplex (September 2024) for its online booking fee. The Bureau filed actions against Canada's Wonderland (May 2025) and DoorDash (June 2025). Drip pricing is a stated enforcement priority in the Bureau's 2024-2025 Annual Plan.

**Primary**: [Competition Act, s. 74.01(1.1)](https://laws-lois.justice.gc.ca/eng/acts/c-34/page-11.html); [Competition Bureau, Guide to the June 2024 Amendments](https://competition-bureau.canada.ca/en/how-we-foster-competition/education-and-outreach/guide-june-2024-amendments-competition-act); [Competition Bureau, Drip Pricing](https://competition-bureau.canada.ca/en/deceptive-marketing-practices/drip-pricing)

**Secondary**: [Canadian Advertising/Marketing Lawyer, "Competition Bureau Sues DoorDash and Canada's Wonderland" (June 2025)](https://www.canadianadvertisinglaw.com/canadas-competition-bureau-sues-doordash-and-canadas-wonderland-drip-pricing-continues-to-be-a-top-deceptive-marketing-priority/); [Canadian Advertising/Marketing Lawyer, "Cineplex $38.9 Million Decision" (Sept 2024)](https://www.canadianadvertisinglaw.com/canadian-competition-tribunal-releases-full-decision-in-38-9-million-cineplex-drip-pricing-case/); [McMillan, "From Cineplex to Wonderland: The Drip Pricing Rollercoaster" (2025)](https://mcmillan.ca/insights/from-cineplex-to-wonderland-the-drip-pricing-rollercoaster/); [Canadian Advertising/Marketing Lawyer, "2024 Competition Act Amendments: Increased Risks for Advertisers"](https://www.canadianadvertisinglaw.com/2024-competition-act-amendments-bill-c-59-increased-risks-for-advertisers-for-false-or-misleading-price-regular-price-and-sale-claims/)

### Competition Act, s. 45 — Criminal Conspiracy (Price-Fixing)

Section 45(1) makes it a criminal offence for any person to conspire, agree, or arrange with a competitor to fix, maintain, increase, or control the price for the supply of a product; to allocate sales, territories, customers, or markets; or to fix, maintain, control, prevent, lessen, or eliminate the production or supply of a product. The offence requires proof beyond a reasonable doubt of an agreement or arrangement.

**Relevance to surveillance pricing.** Section 45 is the primary instrument against algorithmic collusion, where competitors use shared pricing algorithms or common data sources to coordinate prices. The key enforcement challenge is the "meeting of the minds" requirement: where algorithms autonomously converge on supra-competitive prices without explicit human coordination, proving an "agreement" under s. 45 becomes difficult. The Competition Bureau's discussion paper explicitly identifies this as a gap. Hub-and-spoke arrangements, where multiple competitors feed data into a common algorithm operated by a third party, present a more tractable enforcement theory because the common algorithm evidences coordination. The section 90.1(1.01) amendment (extending civil agreements provisions to non-competitors) creates an alternative civil pathway for hub-and-spoke scenarios.

**Primary**: [Competition Act, s. 45](https://laws-lois.justice.gc.ca/eng/acts/C-34/section-45.html)

**Secondary**: [CanLII Connects, "A Focusing and Widening Lens: Algorithmic Collusion and AI Agents under the Competition Act" (2025)](https://canliiconnects.org/en/commentaries/98434); [McCarthy Tetrault, "ChatCCB: The Competition Bureau Invites Discussion on Algorithmic Pricing" (2025)](https://www.mccarthy.ca/en/insights/publications/chatccb-the-competition-bureau-invites-discussion-on-algorithmic-pricing)

### Competition Act, s. 90.1 — Civil Competitor Collaboration (amended 2024)

Section 90.1 allows the Tribunal to prohibit agreements or arrangements between competitors that prevent or lessen competition substantially. The 2024 amendments significantly expanded its reach in three ways: (1) the Tribunal can now make orders even where none of the parties are competitors, if a "significant purpose" of the agreement is to prevent or lessen competition; (2) past conduct is now reviewable, not only current or prospective; (3) the efficiencies exception was repealed effective December 15, 2024.

**Relevance to surveillance pricing.** The expansion to non-competitor agreements is directly relevant to algorithmic pricing. Where a third-party pricing algorithm provider facilitates coordination among nominally independent firms (the hub-and-spoke model), the provider is not a "competitor" of its clients in the relevant market. Before the 2024 amendment, s. 90.1 could not reach the hub. After the amendment, the Tribunal can make an order against any party to the arrangement if a significant purpose is to prevent or lessen competition, regardless of whether the parties compete. This closes a structural gap that the criminal conspiracy provision (s. 45) leaves open for tacit algorithmic coordination.

**Primary**: [Competition Act, s. 90.1](https://laws.justice.gc.ca/eng/acts/C-34/section-90.1.html); [Competition Bureau, Guide to the June 2024 Amendments](https://competition-bureau.canada.ca/en/how-we-foster-competition/education-and-outreach/guide-june-2024-amendments-competition-act)

**Secondary**: [Norton Rose Fulbright, "Navigating the New Landscape: Competition Act Amendments on Collaborations" (2024)](https://www.nortonrosefulbright.com/en/knowledge/publications/ef5815f0/navigating-the-new-landscape-competition-act-amendments); [Fasken, "Amendments To The Competition Act Only One Step" (Sept 2024)](https://www.fasken.com/en/knowledge/2024/09/amendments-to-the-competition-act-only-one-step-towards-a-truly-competitive-economy)

### Competition Act, ss. 78-79 — Abuse of Dominance (amended 2024)

The abuse of dominance provisions were substantially amended in 2024. The amendments: (1) added "directly or indirectly imposing excessive and unfair selling prices" to the enumerated list of anti-competitive acts in s. 78; (2) removed the requirement to prove both anti-competitive intent and anti-competitive effect — the Tribunal can now issue orders on either ground; (3) lowered the threshold by allowing orders where conduct "has had, is having, or is likely to have" the effect of substantially lessening or preventing competition, provided the effect is not attributable to "superior competitive performance."

**Relevance to surveillance pricing.** A dominant firm using algorithmic pricing to extract supra-competitive personalized prices could, in principle, face an abuse of dominance challenge. The new "excessive and unfair selling prices" provision (s. 78) is the most direct hook. However, the Bureau has indicated it will focus on the anti-competitive conduct that "enables" excessive pricing, not the high prices themselves. This means the provision targets algorithmic pricing as a practice of dominance, not as a standalone harm. The "superior competitive performance" safe harbor also creates ambiguity: a firm might argue that sophisticated algorithmic pricing reflects competitive merit. No enforcement action has applied the amended abuse of dominance provisions to algorithmic pricing as of February 2026.

**Primary**: [Competition Act, ss. 78-79](https://laws-lois.justice.gc.ca/eng/acts/C-34/section-79.html); [Competition Bureau, Abuse of Dominance Enforcement Guidelines](https://competition-bureau.canada.ca/en/how-we-foster-competition/education-and-outreach/abuse-dominance-enforcement-guidelines); [Competition Bureau, Bulletin on Amendments to the Abuse of Dominance Provisions](https://competition-bureau.canada.ca/en/how-we-foster-competition/consultations/bulletin-amendments-abuse-dominance-provisions)

**Secondary**: [ABA, "Making Sense of the New Excessive and Unfair Pricing Provision in Canada's Competition Act" (Aug 2024)](https://www.americanbar.org/groups/antitrust_law/resources/source/2024-aug/making-sense-new-pricing-provision-canada/); [Fasken, "The Evolving Competition Law Landscape: Part 1 — Abuse of Dominance" (June 2024)](https://www.fasken.com/en/knowledge/2024/06/the-evolving-competition-law-landscape-in-canada); [Norton Rose Fulbright, "Navigating the New Landscape: Substantive Amendments to the Abuse of Dominance Regime" (2024)](https://www.nortonrosefulbright.com/en/knowledge/publications/c8df209b/navigating-the-new-landscape-substantive-amendments-to-the-abuse)

### Competition Act, s. 74.01(1) — Deceptive Marketing (False or Misleading Representations)

Section 74.01(1) prohibits making a representation to the public that is false or misleading in a material respect. This is a general provision, not pricing-specific, but it could apply where personalized pricing involves representations about price that are materially misleading.

**Relevance to surveillance pricing.** If a firm displays a "regular price" or "sale price" that is algorithmically personalized without disclosure, and the consumer reasonably believes the price applies generally, this could constitute a materially misleading representation. The 2024 amendments strengthened the ordinary selling price provisions (s. 74.01(3)) and reversed the burden for sellers to prove that discount claims are genuine. The private right of action provisions (effective June 20, 2025) allow private parties to bring deceptive marketing claims directly before the Competition Tribunal if they demonstrate a public interest, which could enable class action-adjacent litigation against personalized pricing. However, no enforcement action or private application has tested this theory as of February 2026.

**Primary**: [Competition Act, s. 74.01](https://laws-lois.justice.gc.ca/eng/acts/c-34/page-11.html)

**Secondary**: [Fasken, "The Evolving Competition Law Landscape: Part 4 — Deceptive Marketing Practices" (July 2024)](https://www.fasken.com/en/knowledge/2024/07/the-evolving-competition-law-landscape-in-ca-4); [Canadian Advertising/Marketing Lawyer, "2024 Amendments: Significantly Increased Penalties" (2024)](https://www.canadianadvertisinglaw.com/2024-competition-act-amendments-bill-c-59-significantly-increased-penalties-and-enforcement-options-across-key-areas-of-canadian-competition-law/); [BLG, "False Advertising and Greenwashing: Bill C-59 Changes" (July 2024)](https://www.blg.com/en/insights/2024/07/false-advertising-and-greenwashing-bill-c-59-changes-to-competition-act)

### PIPEDA — Consent and Purpose Limitation Principles (eff. 2000/2004)

The Personal Information Protection and Electronic Documents Act governs the collection, use, and disclosure of personal information in the course of commercial activity by private sector organizations. PIPEDA is principle-based and technology-neutral. Its ten fair information principles include consent (Principle 3), purpose limitation (Principle 2), and limiting collection (Principle 4). Personal information may only be collected for purposes that "a reasonable person would consider appropriate in the circumstances" (s. 5(3)), and may only be used or disclosed for the purposes for which it was collected unless the individual consents to a new purpose.

**Relevance to surveillance pricing.** PIPEDA constrains the data infrastructure underlying personalized pricing. If an e-commerce platform collects browsing history and purchase data for one purpose (e.g., order fulfillment, recommendations) and uses it for price individualization without consent for that purpose, this violates the purpose limitation principle. The OPC's guidance on meaningful consent requires that consent be informed, and that organizations not use "blanket consent" clauses to authorize novel data uses. The OPC's guidance on "inappropriate data practices" under s. 5(3) identifies "no-go zones" where data use is inappropriate regardless of consent; algorithmic pricing that results in "profiling or categorization that leads to unfair, unethical or discriminatory treatment contrary to human rights law" could fall within this. However, PIPEDA has critical structural limitations for surveillance pricing: (1) it has no specific automated decision-making provisions; (2) the OPC cannot issue binding orders or levy penalties directly (it makes findings and recommendations; enforcement requires Federal Court application); (3) it does not apply in provinces with "substantially similar" legislation (Quebec, Alberta, British Columbia), creating jurisdictional gaps.

**Primary**: [PIPEDA (full text)](https://laws-lois.justice.gc.ca/eng/acts/p-8.6/); [OPC, PIPEDA Requirements in Brief](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda_brief/); [OPC, Guidelines for Obtaining Meaningful Consent](https://www.priv.gc.ca/en/privacy-topics/collecting-personal-information/consent/gl_omc_201805/); [OPC, Guidance on Inappropriate Data Practices: Subsection 5(3)](https://www.priv.gc.ca/en/privacy-topics/collecting-personal-information/consent/gd_53_201805/)

**Secondary**: [OPC, A Regulatory Framework for AI: Recommendations for PIPEDA Reform (Nov 2020)](https://www.priv.gc.ca/en/about-the-opc/what-we-do/consultations/completed-consultations/consultation-ai/reg-fw_202011/); [McCarthy Tetrault, "Using Privacy Laws to Regulate Automated Decision Making" (2021)](https://www.mccarthy.ca/en/insights/blogs/techlex/using-privacy-laws-to-regulate-automated-decision-making); [Baker McKenzie, "AI, Profiling and ADM — Canada" (2025)](https://resourcehub.bakermckenzie.com/en/resources/global-data-and-cyber-handbook/north-america/canada/topics/artificial-intelligence-profiling-and-automated-decision-making)

### Quebec Law 25 — Automated Decision-Making Provisions (s. 12.1, eff. Sept 22, 2023)

Quebec's Act respecting the protection of personal information in the private sector, as amended by Law 25 (Bill 64), includes the most advanced automated decision-making provisions in Canada. Section 12.1 requires that any enterprise using personal information to render a decision based exclusively on automated processing must: (1) inform the person concerned at the time of the decision; (2) on request, provide the personal information used, the reasons and principal factors and parameters that led to the decision; and (3) provide an opportunity to submit observations to a person in a position to review the decision. Law 25 defines profiling as "the collection and use of personal information to assess certain characteristics of a natural person, in particular for the purpose of analyzing that person's work performance, economic situation, health, personal preferences, interests or behaviour."

**Relevance to surveillance pricing.** Section 12.1 applies to any decision based exclusively on automated processing, with no sector exceptions and no significance threshold (unlike GDPR Article 22). If a Quebec-operating firm uses personal data to set an individualized price through a fully automated system, s. 12.1 is triggered. The consumer would have the right to: know the price was set by automated processing, know the data inputs and parameters, and request human review. This is the closest any Canadian instrument comes to directly regulating surveillance pricing. However, the provision applies only to decisions based "exclusively" on automated processing; a firm that introduces a nominal human checkpoint could argue the section does not apply. The provision also does not prohibit the practice — it imposes transparency, explanation, and review obligations. It operates as a rights-based instrument, not as prohibition.

**Limitations.** Quebec's law applies only to commercial activities within Quebec. It does not preempt federal law (PIPEDA) for federally regulated sectors (banking, telecommunications, transportation). No enforcement action has applied s. 12.1 to personalized pricing as of February 2026.

**Primary**: [Act respecting the protection of personal information in the private sector, s. 12.1 (CanLII)](https://www.canlii.org/en/qc/laws/stat/cqlr-c-p-39.1/latest/); [CAI Quebec](https://www.cai.gouv.qc.ca/english/)

**Secondary**: [Torys, "Automated Decision-Making: What Quebec's Bill 64 Reforms Mean for Business" (April 2022)](https://www.torys.com/en/our-latest-thinking/publications/2022/04/automated-decision-making); [Fasken, "New Rules for Automated Decision Making" (Law 25 Series)](https://www.fasken.com/en/knowledge/loi-25/5-new-rules-for-automated-decision-making); [RCGT, "Law 25: The Issue of Automated Decisions"](https://www.rcgt.com/en/insights/expert-advice/law-25-issue-automated-decisions/); [National Magazine, "Privacy Experts Grappling with Automated AI Decision-Making" (2025)](https://nationalmagazine.ca/en-ca/articles/law/in-depth/2025/privacy-experts%C2%A0grappling-with%C2%A0automated-ai-decision-making)

### Treasury Board Directive on Automated Decision-Making (2019, amended 2023)

The Directive sets requirements for federal government institutions using automated decision systems in administrative decision-making. It mandates an Algorithmic Impact Assessment (AIA), transparency requirements scaled to impact level, human oversight, and recourse mechanisms. The 2023 amendments expanded the AIA to include questions about institutional reasons for automation and impacts on persons with disabilities.

**Relevance to surveillance pricing.** The Directive applies only to federal government institutions, not to private sector organizations. It therefore has no direct application to commercial surveillance pricing. Its significance is indirect: it represents Canada's most developed framework for algorithmic governance and has been cited as a model for potential private-sector regulation. The AIA tool has been recognized internationally (OECD) as a leading impact assessment methodology. If Canada eventually adopts a private-sector AI governance framework (following the death of AIDA), the Directive's architecture may inform its design.

**Primary**: [Treasury Board, Directive on Automated Decision-Making](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592); [Algorithmic Impact Assessment Tool](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/algorithmic-impact-assessment.html); [Amendments to the Directive (2023)](https://www.canada.ca/en/government/system/digital-government/policies-standards/policy-service-digital-announcements/amendments-directive-automated-decision-making.html)

### Competition Bureau — Algorithmic Pricing Discussion Paper and What We Heard Report (2025-2026)

In June 2025, the Competition Bureau published a discussion paper on algorithmic pricing and competition, explicitly distinguishing between dynamic pricing algorithms (responding to market conditions) and personalized pricing algorithms (responding to individual consumer data). The Bureau consulted from June 10 to August 4, 2025, and received 103 responses (77 from individuals, 26 from stakeholders). The "What We Heard" report was published January 22, 2026.

**Key findings from the consultation.** Four themes emerged: (1) algorithmic pricing can create market efficiencies; (2) algorithmic pricing can lead to anti-competitive behaviour; (3) lack of data transparency could harm consumers, workers, and competition; (4) regulations should address anti-competitive conduct without stifling innovation. Most individual submissions raised concerns about misuse and the need for regulation, while stakeholder submissions were more balanced. The Bureau's discussion paper identified specific risks: hub-and-spoke conspiracies facilitated by shared algorithms, personalized pricing enabling cross-subsidized discrimination against consumers with fewer outside options, and the evidentiary challenge of proving algorithmic collusion under the "agreement" requirement.

**Relevance to surveillance pricing.** The discussion paper and report represent the most significant direct engagement by a Canadian institution with the specific practice of surveillance pricing. The Bureau explicitly distinguished personalized pricing from dynamic pricing, identified consumer data exploitation as a competition concern, and acknowledged gaps in the existing Competition Act framework. However, the consultation is not intended to produce policy recommendations — it is framed as building the Bureau's understanding. No enforcement guidance, enforcement actions, or legislative recommendations have followed as of February 2026.

**Primary**: [Competition Bureau, Algorithmic Pricing and Competition: Discussion Paper (June 2025)](https://competition-bureau.canada.ca/en/how-we-foster-competition/education-and-outreach/publications/algorithmic-pricing-and-competition-discussion-paper); [Competition Bureau, Consultation on Algorithmic Pricing: What We Heard (Jan 2026)](https://competition-bureau.canada.ca/en/how-we-foster-competition/education-and-outreach/publications/consultation-algorithmic-pricing-and-competition-what-we-heard); [Canada.ca, "Competition Bureau Report Highlights Public Feedback" (Jan 2026)](https://www.canada.ca/en/competition-bureau/news/2026/01/competition-bureau-report-highlights-public-feedback-on-algorithmic-pricing-and-competition.html)

**Secondary**: [ICLE, Comments to Canadian Competition Bureau on Algorithmic Pricing (Aug 2025)](https://laweconcenter.org/resources/icle-comments-to-the-canadian-competition-bureau-on-algorithmic-pricing-and-competition/); [CCIA, Comments on Canadian Algorithmic Pricing Regulations (Aug 2025)](https://ccianet.org/news/2025/08/ccia-files-comments-on-canadian-algorithmic-pricing-regulations); [ITIF, Comments to Competition Bureau on Algorithmic Pricing (Aug 2025)](https://itif.org/publications/2025/08/08/comments-competition-bureau-of-canada-regarding-algorithmic-pricing-competition/); [Chapdelaine, Larouche & Quaid, "The Anti-Competitive Effects of Algorithmic Personalized Pricing and the Big Data Economy" (SSRN, Aug 2025)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5399219)

## Analysis

**Hierarchy.** Competition is the dominant strategy. The Competition Act provides the broadest instrument set (drip pricing prohibition, criminal conspiracy, civil competitor collaboration, abuse of dominance, deceptive marketing), the strongest enforcement institution (Competition Bureau with Tribunal adjudication), the highest penalties (up to 3% of global turnover or criminal imprisonment), and the most active enforcement record (Cineplex, Wonderland, DoorDash). The Bureau is also the institutional actor most directly engaging with algorithmic pricing through its 2025 discussion paper. Privacy law (PIPEDA) operates as secondary infrastructure, constraining the data collection and use that enables pricing but not reaching the pricing decision itself. Quebec's Law 25 is the only instrument that directly imposes obligations on the automated pricing decision, but its geographic scope is limited to one province.

**Design logic.** Accumulated. Canada's instruments addressing surveillance pricing were not designed as a set. They emerged from different eras, different legal bases, and different institutional actors:

- Competition Act drip pricing prohibition — consumer protection via competition law (2022/2024)
- Competition Act conspiracy/abuse provisions — competition law, criminal and civil (1985, amended 2022/2024)
- PIPEDA consent and purpose limitation — privacy law (2000/2004)
- Quebec Law 25 ADM provisions — provincial privacy law (2021, effective 2023)
- Treasury Board Directive — government administrative law (2019/2023)
- Competition Bureau discussion paper — policy development (2025/2026)

The instruments lack a coordinating framework. The Competition Bureau engages with algorithmic pricing as a competition issue. The OPC engages with data-driven profiling as a privacy issue. Quebec engages with automated decision-making as a rights issue. There is no mechanism linking these perspectives, no statutory provision establishing their relationship, and no interagency coordination structure specifically for algorithmic pricing. The Competition Bureau's September 2024 Summit called for "cross-sector collaboration among regulators," but no formal mechanism has been established.

**Institutional divergence.** Two notable patterns:

First, the Competition Bureau is the most active institution, but competition law structurally cannot reach unilateral personalized pricing by non-dominant firms. The criminal conspiracy provision (s. 45) requires an agreement; the abuse of dominance provision (ss. 78-79) requires dominance; the civil competitor collaboration provision (s. 90.1) requires an agreement or arrangement. A single firm that unilaterally deploys an algorithmic pricing system to extract personalized surplus from consumers, without coordinating with competitors and without holding a dominant position, falls outside all four competition instruments. This is the same structural gap identified in the EU and US federal competition frameworks.

Second, the privacy enforcement institution (OPC) has the most relevant legal principles (consent, purpose limitation, inappropriate data practices) but the weakest enforcement powers. The OPC cannot levy administrative monetary penalties and cannot issue binding orders; it makes findings and recommendations, and enforcement requires application to the Federal Court. The OPC has identified automated decision-making as a reform priority but has not issued guidance specific to algorithmic pricing. Quebec's CAI has stronger enforcement powers (AMPs up to CAD $25M or 4% of global turnover under Law 25), but its jurisdiction is provincial. The enforcement gap is structural: the institution with the strongest powers (Competition Bureau) cannot reach unilateral personalized pricing; the institution with the most relevant principles (OPC) cannot enforce them effectively.

## Evidence

**Cineplex drip pricing — Competition Tribunal, September 2024.** The Tribunal ordered Cineplex to pay CAD $38.9 million (equivalent to the amount collected through the undisclosed online booking fee from June 2022 to December 2023). The Tribunal found the online booking fee constituted drip pricing because it was not disclosed until after ticket selection. This is the largest drip pricing penalty in Canadian history and the first major enforcement action under s. 74.01(1.1). While not a personalized pricing case, it establishes the Competition Tribunal's willingness to impose substantial penalties for pricing opacity. [Competition Tribunal decision; Canadian Advertising/Marketing Lawyer, "Cineplex $38.9 Million Decision" (Sept 2024)](https://www.canadianadvertisinglaw.com/canadian-competition-tribunal-releases-full-decision-in-38-9-million-cineplex-drip-pricing-case/)

**Canada's Wonderland drip pricing — filed May 2025.** The Commissioner filed an application alleging Wonderland advertised ticket and season pass prices that were unattainable due to mandatory "processing fees." Pending before the Competition Tribunal as of February 2026. [Competition Bureau; Canadian Advertising/Marketing Lawyer (June 2025)](https://www.canadianadvertisinglaw.com/canadas-competition-bureau-sues-doordash-and-canadas-wonderland-drip-pricing-continues-to-be-a-top-deceptive-marketing-priority/)

**DoorDash drip pricing — filed June 2025.** The Bureau sued DoorDash and its Canadian subsidiary for allegedly engaging in drip pricing in violation of s. 74.01(1.1). Pending as of February 2026. [Competition Bureau (June 2025)](https://www.canadianadvertisinglaw.com/canadas-competition-bureau-sues-doordash-and-canadas-wonderland-drip-pricing-continues-to-be-a-top-deceptive-marketing-priority/)

**Competition Bureau algorithmic pricing consultation — 103 submissions (2025-2026).** The Bureau received 77 individual comments (mostly expressing concern about algorithmic pricing) and 26 stakeholder submissions. Key stakeholder submissions include ICLE (cautioning against regulation that stifles innovation), CCIA (warning against premature regulation), ITIF (emphasizing benefits of algorithmic pricing), and Chapdelaine, Larouche & Quaid (arguing the Competition Act requires "creative interpretations" and refined enforcement strategies to address algorithmic personalized pricing). The plurality of individual submissions called for regulation; the plurality of stakeholder submissions cautioned against premature intervention. [Competition Bureau, What We Heard (Jan 2026)](https://competition-bureau.canada.ca/en/how-we-foster-competition/education-and-outreach/publications/consultation-algorithmic-pricing-and-competition-what-we-heard)

**No enforcement actions on personalized pricing.** As of February 2026, no Canadian authority (Competition Bureau, OPC, Quebec CAI, or any provincial regulator) has brought an enforcement action specifically targeting personalized or algorithmic pricing (as distinct from drip pricing). The enforcement record is entirely in the drip pricing subcategory.

## Movement

1. **2000**: PIPEDA enacted — principle-based privacy framework for commercial activity; no automated decision-making provisions
2. **2004**: PIPEDA fully in force for all provincial commercial activity (except provinces with substantially similar legislation)
3. **2019**: Treasury Board Directive on Automated Decision-Making — first Canadian automated decision-making governance framework (government sector only)
4. **2021**: Quebec Law 25 (Bill 64) adopted — automated decision-making provisions, profiling definition, transparency and explanation rights (phased implementation)
5. **2022 (June)**: Competition Act amendments (Bill C-19) — drip pricing prohibition enacted (s. 74.01(1.1)); new deceptive marketing tools; expanded private enforcement
6. **2022 (Nov)**: Bill C-27 introduced — would have enacted CPPA (with ADM provisions), AIDA (AI governance), and data protection tribunal
7. **2023 (April)**: Treasury Board Directive amended — expanded Algorithmic Impact Assessment scope
8. **2023 (Sept)**: Quebec Law 25 automated decision-making provisions take effect (s. 12.1)
9. **2024 (June)**: Competition Act amendments (Bill C-59) — drip pricing strengthened; abuse of dominance expanded (excessive pricing); s. 90.1 expanded to non-competitors; private right of action expanded; penalty thresholds raised
10. **2024 (Sept)**: Competition Bureau Summit 2024: "Market Dynamics in the AI Era" — algorithmic pricing, collusion, and enforcement challenges discussed
11. **2024 (Sept)**: Cineplex drip pricing decision — CAD $38.9 million penalty
12. **2024 (Oct)**: Competition Bureau AI and Competition What We Heard report (first consultation, focused on AI broadly)
13. **2025 (Jan)**: Parliament prorogued — Bill C-27 dies; CPPA, AIDA, and data protection tribunal all fail
14. **2025 (April)**: Federal election called
15. **2025 (May)**: Wonderland drip pricing action filed
16. **2025 (June)**: DoorDash drip pricing action filed; Competition Bureau publishes algorithmic pricing discussion paper; consultation opens (June 10 - Aug 4, 2025); Minister Solomon confirms AIDA "off the table," signals "light, tight, right" AI regulation and separate privacy bill
17. **2025 (June)**: Private right of action for deceptive marketing and civil competitor collaboration takes effect (Competition Tribunal)
18. **2026 (Jan)**: Competition Bureau publishes What We Heard report on algorithmic pricing consultation
19. **2026 (expected)**: New federal privacy legislation expected (PIPEDA successor); AI regulation to be considered separately

## Open Questions

1. **Will the Competition Bureau issue enforcement guidance on algorithmic pricing?** The discussion paper and What We Heard report are explicitly non-prescriptive. The Bureau has not indicated whether it will issue enforcement guidelines, compliance frameworks, or formal policy positions on algorithmic personalized pricing. Without guidance, the boundary between lawful dynamic pricing and unlawful personalized pricing under the Competition Act remains undefined.

2. **Can section 45 reach algorithmic collusion?** The "agreement" requirement demands proof beyond a reasonable doubt of a meeting of the minds. Where pricing algorithms autonomously converge without explicit communication, the evidentiary burden may be insurmountable. The Bureau's discussion paper acknowledges this gap but does not propose a solution. Whether Canadian courts will adopt a broad interpretation of "agreement" (encompassing algorithm-mediated tacit coordination) or a narrow one (requiring explicit or inferrable human agreement) is untested.

3. **What will replace Bill C-27?** The government has signalled that new federal privacy legislation is expected in 2026, with AI regulation proceeding separately. The key questions for surveillance pricing: Will the new privacy law include automated decision-making provisions comparable to Quebec Law 25 or the defunct CPPA? Will it give the OPC (or a successor tribunal) administrative monetary penalty power? Will the AI regulation framework cover commercial pricing algorithms, or will it focus on higher-risk applications?

4. **Will Quebec's Law 25 produce enforcement precedent?** Section 12.1 has been operative since September 2023 — over two years. No enforcement action has tested its application to algorithmic pricing. The CAI's approach to interpreting the "exclusively automated" threshold and the scope of the explanation right will determine whether the provision has practical force against surveillance pricing.

5. **Will the private right of action generate personalized pricing litigation?** As of June 2025, private parties can bring deceptive marketing claims before the Competition Tribunal. Could a consumer group or advocacy organization file a private application challenging undisclosed personalized pricing as a false or misleading representation under s. 74.01(1)? The "public interest" threshold for leave is untested.

6. **How will federal-provincial interaction evolve?** Quebec has the strongest automated decision-making provisions; PIPEDA does not apply in Quebec for provincially regulated matters. If federal privacy reform includes ADM provisions, how will they interact with Quebec's (potentially stronger) existing law? And will other provinces (British Columbia, Alberta, Ontario) develop their own provisions?

7. **What is the OPC's position on surveillance pricing?** The OPC has published general guidance on AI and profiling (2020 recommendations for PIPEDA reform) and on inappropriate data practices (s. 5(3) guidance), but has not issued a specific position on algorithmic or personalized pricing. The OPC's 2024-2025 annual report identifies "technological advancements such as generative AI" as a strategic priority, but algorithmic pricing does not appear as a named focus area.

8. **Will Canada coordinate with international enforcement?** The Competition Bureau's Summit 2024 called for "cross-sector collaboration." Canada participates in the International Competition Network and has bilateral cooperation agreements. Whether the Bureau will coordinate with the US FTC (which launched a surveillance pricing inquiry in 2024), the EU Commission (which confirmed active algorithmic pricing investigations in 2025), or the UK CMA on enforcement strategy remains to be seen.

## Sources

**Primary**:
- [Competition Act (RSC 1985, c. C-34) — full text](https://laws-lois.justice.gc.ca/eng/acts/c-34/)
- [Competition Act, s. 45 (Criminal Conspiracy)](https://laws-lois.justice.gc.ca/eng/acts/C-34/section-45.html)
- [Competition Act, s. 74.01 (Deceptive Marketing / Drip Pricing)](https://laws-lois.justice.gc.ca/eng/acts/c-34/page-11.html)
- [Competition Act, ss. 78-79 (Abuse of Dominance)](https://laws-lois.justice.gc.ca/eng/acts/C-34/section-79.html)
- [Competition Act, s. 90.1 (Civil Agreements)](https://laws.justice.gc.ca/eng/acts/C-34/section-90.1.html)
- [Competition Bureau, Guide to the June 2024 Amendments](https://competition-bureau.canada.ca/en/how-we-foster-competition/education-and-outreach/guide-june-2024-amendments-competition-act)
- [Competition Bureau, Drip Pricing](https://competition-bureau.canada.ca/en/deceptive-marketing-practices/drip-pricing)
- [Competition Bureau, Abuse of Dominance Enforcement Guidelines](https://competition-bureau.canada.ca/en/how-we-foster-competition/education-and-outreach/abuse-dominance-enforcement-guidelines)
- [Competition Bureau, Algorithmic Pricing and Competition: Discussion Paper (June 2025)](https://competition-bureau.canada.ca/en/how-we-foster-competition/education-and-outreach/publications/algorithmic-pricing-and-competition-discussion-paper)
- [Competition Bureau, Consultation on Algorithmic Pricing: What We Heard (Jan 2026)](https://competition-bureau.canada.ca/en/how-we-foster-competition/education-and-outreach/publications/consultation-algorithmic-pricing-and-competition-what-we-heard)
- [Competition Bureau, Report on Summit 2024: Competition in the AI Era](https://competition-bureau.canada.ca/en/how-we-foster-competition/education-and-outreach/report-summit-2024-competition-ai-era)
- [PIPEDA (full text)](https://laws-lois.justice.gc.ca/eng/acts/p-8.6/)
- [OPC, PIPEDA Requirements in Brief](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda_brief/)
- [OPC, PIPEDA Fair Information Principles](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/p_principle/)
- [OPC, Guidelines for Obtaining Meaningful Consent](https://www.priv.gc.ca/en/privacy-topics/collecting-personal-information/consent/gl_omc_201805/)
- [OPC, Guidance on Inappropriate Data Practices: Subsection 5(3)](https://www.priv.gc.ca/en/privacy-topics/collecting-personal-information/consent/gd_53_201805/)
- [OPC, A Regulatory Framework for AI: Recommendations for PIPEDA Reform (Nov 2020)](https://www.priv.gc.ca/en/about-the-opc/what-we-do/consultations/completed-consultations/consultation-ai/reg-fw_202011/)
- [Quebec, Act respecting the protection of personal information in the private sector (Law 25)](https://www.canlii.org/en/qc/laws/stat/cqlr-c-p-39.1/latest/)
- [Treasury Board, Directive on Automated Decision-Making](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592)
- [Algorithmic Impact Assessment Tool](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/algorithmic-impact-assessment.html)
- [Bill C-27 (44th Parliament) — LEGISinfo](https://www.parl.ca/legisinfo/en/bill/44-1/c-27)

**Secondary**:
- [McCarthy Tetrault, "ChatCCB: The Competition Bureau Invites Discussion on Algorithmic Pricing" (2025)](https://www.mccarthy.ca/en/insights/publications/chatccb-the-competition-bureau-invites-discussion-on-algorithmic-pricing)
- [CanLII Connects, "A Focusing and Widening Lens: Algorithmic Collusion and AI Agents under the Competition Act" (2025)](https://canliiconnects.org/en/commentaries/98434)
- [Chapdelaine, Larouche & Quaid, "The Anti-Competitive Effects of Algorithmic Personalized Pricing and the Big Data Economy" (SSRN, Aug 2025)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5399219)
- [Chapdelaine, "Algorithmic Price Personalization and the Limits of Anti-Discrimination Law" (SSRN, 2024)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4963875)
- [Norton Rose Fulbright, "Three Years and Three Sets of Amendments Later: The State of Canada's Competition Act" (2025)](https://www.nortonrosefulbright.com/en/knowledge/publications/6ab48b44/three-years-and-three-sets-of-amendments-later-the-state-of-canadas-competition-act)
- [Norton Rose Fulbright, "Navigating the New Landscape: Abuse of Dominance" (2024)](https://www.nortonrosefulbright.com/en/knowledge/publications/c8df209b/navigating-the-new-landscape-substantive-amendments-to-the-abuse)
- [ABA, "Making Sense of the New Excessive and Unfair Pricing Provision" (Aug 2024)](https://www.americanbar.org/groups/antitrust_law/resources/source/2024-aug/making-sense-new-pricing-provision-canada/)
- [Fasken, "The Evolving Competition Law Landscape — Part 1: Abuse of Dominance" (June 2024)](https://www.fasken.com/en/knowledge/2024/06/the-evolving-competition-law-landscape-in-canada)
- [Fasken, "The Evolving Competition Law Landscape — Part 4: Deceptive Marketing" (July 2024)](https://www.fasken.com/en/knowledge/2024/07/the-evolving-competition-law-landscape-in-ca-4)
- [Baker McKenzie, "A New Dawn for Competition Law as Bill C-59 Passes" (June 2024)](https://canada-insights.bakermckenzie.com/2024/06/21/a-new-dawn-for-competition-law-and-enforcement-as-bill-c-59-passes/)
- [Canadian Advertising/Marketing Lawyer, "Cineplex $38.9 Million Decision" (Sept 2024)](https://www.canadianadvertisinglaw.com/canadian-competition-tribunal-releases-full-decision-in-38-9-million-cineplex-drip-pricing-case/)
- [Canadian Advertising/Marketing Lawyer, "Competition Bureau Sues DoorDash and Canada's Wonderland" (June 2025)](https://www.canadianadvertisinglaw.com/canadas-competition-bureau-sues-doordash-and-canadas-wonderland-drip-pricing-continues-to-be-a-top-deceptive-marketing-priority/)
- [ICLE, Comments to Canadian Competition Bureau on Algorithmic Pricing (Aug 2025)](https://laweconcenter.org/resources/icle-comments-to-the-canadian-competition-bureau-on-algorithmic-pricing-and-competition/)
- [ITIF, Comments to Competition Bureau on Algorithmic Pricing (Aug 2025)](https://itif.org/publications/2025/08/08/comments-competition-bureau-of-canada-regarding-algorithmic-pricing-competition/)
- [Torys, "Automated Decision-Making: What Quebec's Bill 64 Reforms Mean for Business" (April 2022)](https://www.torys.com/en/our-latest-thinking/publications/2022/04/automated-decision-making)
- [Fasken, "New Rules for Automated Decision Making" (Law 25 Series)](https://www.fasken.com/en/knowledge/loi-25/5-new-rules-for-automated-decision-making)
- [McCarthy Tetrault, "Using Privacy Laws to Regulate Automated Decision Making" (2021)](https://www.mccarthy.ca/en/insights/blogs/techlex/using-privacy-laws-to-regulate-automated-decision-making)
- [Gowling WLG, "Federal Privacy Reform: Where We Left Off and What's Next" (2025)](https://gowlingwlg.com/en/insights-resources/articles/2025/federal-privacy-reform)
- [IAPP, "Ahead of 2025 Federal Election, Will Canada Pass Bill C-27?" (2025)](https://iapp.org/news/a/ahead-of-2025-federal-election-will-canada-pass-bill-c-27-)
- [IAPP, "Notes from IAPP Canada: Loss of Bill C-27 Presents an Opportunity" (2025)](https://iapp.org/news/a/notes-from-the-iapp-canada-loss-of-bill-c-27-presents-an-opportunity)
- [McInnes Cooper, "The Demise of AIDA: 5 Key Lessons" (2025)](https://www.mcinnescooper.com/publications/the-demise-of-the-artificial-intelligence-and-data-act-aida-5-key-lessons/)
- [Osler, "Canada's 2026 Privacy Priorities: Data Sovereignty, Open Banking and AI" (2025)](https://www.osler.com/en/insights/reports/2025-legal-outlook/canadas-2026-privacy-priorities-data-sovereignty-open-banking-and-ai/)
- [Gowling WLG, "Year in Review 2025: Canadian Digital Policy" (2026)](https://gowlingwlg.com/en/insights-resources/articles/2026/year-in-review-2025-canadian-digital-policy)
- [Torys, "Consumer Protection in Canada: Where We Are and Where We're Going" (Q4 2025)](https://www.torys.com/our-latest-thinking/torys-quarterly/q4-2025/consumer-protection-in-canada)
- [Baker McKenzie, "AI, Profiling and ADM — Canada" (2025)](https://resourcehub.bakermckenzie.com/en/resources/global-data-and-cyber-handbook/north-america/canada/topics/artificial-intelligence-profiling-and-automated-decision-making)
- [HillNotes, "Privacy and Artificial Intelligence in Canada" (May 2025)](https://hillnotes.ca/2025/05/27/privacy-and-artificial-intelligence-in-canada/)

**Library**:
- [[surveillance-pricing-comparative-regulation]]
- [[baldwin-regulatory-strategies]]
- [[command-and-control]]
- [[competition-over-regulation]]
- [[disclosure-regulation]]
- [[rights-and-liabilities-regulation]]
- [[code-as-regulation]]
- [[regulatory-topology-not-ladder]]
- [[government-capacities-regulation]]
- [[creative-compliance]]
- [[algorithmic-coordination]]
- [[algorithmic-coordination-agreement-doctrine]]
- [[algorithmic-coordination-evidence]]
- [[market-power-precondition-algorithmic-harm]]
- [[privacy-data-wtp-aggregation]]
- [[sp-eu]]
- [[sp-us-federal]]
- [[sp-uk]]
