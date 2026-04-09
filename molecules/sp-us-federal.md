---
date-created: "202602252100"
aliases:
  - "US Federal surveillance pricing profile"
tags:
  - "#molecules"
  - "#jurisdiction-profile"
topic:
  - "[[surveillance-pricing]]"
  - "[[United States]]"
---

# United States (Federal) — Surveillance Pricing Regulatory Profile


The US federal government has no statute, regulation, or binding rule that directly addresses surveillance pricing or personalized consumer pricing. Instead, federal regulatory activity operates through three channels: antitrust enforcement (DOJ Sherman Act actions against algorithmic collusion), consumer protection authority (FTC Section 5 unfairness/deception, deployed through studies and enforcement actions rather than rulemaking), and proposed but unenacted legislation (two congressional bills targeting algorithmic pricing, neither advancing past committee). The 2025 change of administration produced a sharp discontinuity: the FTC's surveillance pricing study was effectively suspended when Chair Andrew Ferguson closed the public comment period in January 2025, while the DOJ's RealPage prosecution — initiated under Biden — continued to settlement under the Trump DOJ in November 2025. The result is a jurisdiction where the most consequential regulatory action is antitrust enforcement against coordination, while the consumer protection dimension is stalled, and legislative proposals face a hostile congressional environment.

## Instruments

| Instrument | Strategy | Sector | Status | Enforcement |
|-----------|----------|--------|--------|-------------|
| FTC 6(b) Surveillance Pricing Study (P246202, July 2024) | Disclosure ([[disclosure-regulation]]) | General (intermediary companies) | Paused (public comment withdrawn Jan 2025; study findings released Jan 17, 2025 by 3-2 vote) | FTC 6(b) compulsory orders; no enforcement mechanism — informational only |
| DOJ v. RealPage, No. 1:24-cv-00710 (M.D.N.C., filed Aug 23, 2024) | Competition ([[competition-over-regulation]]) | Rental housing (multifamily) | Settled (proposed consent decree Nov 24, 2025; pending Tunney Act court approval) | DOJ Antitrust Division; Sherman Act ss. 1-2; court-appointed monitor for three years; seven-year decree |
| FTC v. Amazon.com, No. 2:23-cv-01495-JHC (W.D. Wash., filed Sept 26, 2023) | Competition | E-commerce (general) | Ongoing (trial set for Feb 9, 2027) | FTC + 19 state AGs; Sherman Act s. 2; FTC Act s. 5 |
| Preventing Algorithmic Collusion Act, S. 232, 119th Cong. (introduced Jan 23, 2025) | Competition (legislative codification) | General | Proposed (referred to Senate Judiciary Committee) | DOJ + FTC joint enforcement; civil penalties min. $10,000/day or total value of products sold; private right of action not included |
| Stop AI Price Gouging and Wage Fixing Act, H.R. 4640, 119th Cong. (introduced July 23, 2025) | Command and control ([[command-and-control]]) + Disclosure | General (pricing and wages) | Proposed (referred to House committees) | FTC + state AGs + private right of action; EEOC for wage provisions |
| EO 14110, Safe, Secure, and Trustworthy AI (Oct 30, 2023) | Disclosure + Code-as-regulation ([[code-as-regulation]]) | General (cross-sector) | Revoked (rescinded by EO 14179, Jan 20, 2025) | Federal agencies under existing authority; no independent enforcement mechanism |
| CEA Issue Brief, "Cost of Anticompetitive Pricing Algorithms in Rental Housing" (Dec 17, 2024) | Direct action (none — informational study) | Rental housing | Complete | No enforcement mechanism; provides evidentiary basis for DOJ prosecution |
| CEA/OSTP, "Big Data and Differential Pricing" (Feb 2015) | Disclosure (informational — recommends transparency) | General | Complete | No enforcement mechanism; recommended enforcement of existing laws |
| FTC Section 5 Authority (15 U.S.C. s. 45) | Rights & liabilities ([[rights-and-liabilities-regulation]]) / Competition | General | Operative (but scope under active contestation; 2022 Policy Statement expanding UMC authority under political threat) | FTC administrative enforcement; consent orders; federal court injunctions; civil penalties for consent order violations |

## Detail

### FTC 6(b) Surveillance Pricing Study (P246202)

In July 2024, the FTC issued compulsory 6(b) orders to eight intermediary companies — Mastercard, Revionics (Aptos), Bloomreach, JPMorgan Chase, Task Software, PROS, Accenture, and McKinsey — seeking information on their surveillance pricing products and services. The study represented the first systematic federal inquiry into the mechanics of personalized pricing intermediaries: how third-party firms use AI and consumer data (location, demographics, browsing history, purchase patterns) to set individualized prices for retailers.

On January 17, 2025, the FTC released initial research summaries in a 3-2 party-line vote, with then-Commissioner Ferguson and Commissioner Holyoak dissenting. Key findings: at least 250 retailers across grocery, apparel, health and beauty, home goods, convenience, and hardware sectors used surveillance pricing; intermediaries had access to direct consumer data, inferred data, and first- and third-party sources; consumer behaviors including mouse movements and abandoned cart items were tracked for pricing purposes. Ferguson and Holyoak accused the outgoing Democratic majority of "slowly dripping out information" rather than issuing a comprehensive final report.

Three days later, on January 20, 2025, Ferguson became FTC Chair. Within the week, he closed the public comment period on the related Request for Information regarding surveillance pricing practices, which had been set to run until April 17, 2025. This effectively suspended the study's public-facing dimension. The closure drew bipartisan congressional pushback: Senator Jacky Rosen (D-NV) wrote to Ferguson in March 2025 urging him to reopen the comment period; in December 2025, a bipartisan group — Senators Warner (D-VA), Hawley (R-MO), Blumenthal (D-CT), and Gallego (D-AZ) — wrote to Ferguson calling on the FTC to reopen its market investigation and take enforcement action.

**What it does not cover.** The 6(b) study is informational, not regulatory. It creates no binding obligations, imposes no disclosure requirements on retailers, and generates no enforcement authority beyond what FTC Section 5 already provides. The study examined intermediaries (pricing software vendors), not the retailers or platforms that deploy surveillance pricing. It provides evidence that could support future enforcement or rulemaking, but under the current FTC leadership, neither appears forthcoming.

### DOJ v. RealPage, No. 1:24-cv-00710 (M.D.N.C.)

On August 23, 2024, the DOJ Antitrust Division, joined by eight state Attorneys General (North Carolina, California, Colorado, Connecticut, Minnesota, Oregon, Tennessee, and Washington), filed suit against RealPage Inc. alleging violations of Sections 1 and 2 of the Sherman Act. The complaint alleged that RealPage operated a hub-and-spoke conspiracy: competing landlords fed nonpublic, competitively sensitive rental data (lease terms, occupancy rates, forward-looking pricing) into RealPage's algorithmic pricing software, which then recommended prices incorporating competitors' data. The DOJ alleged RealPage held approximately 80% of the revenue management software market for multifamily apartments.

On November 24, 2025, the DOJ and RealPage announced a proposed consent decree. Key terms: RealPage must stop using nonpublic competitor data in its revenue management products; model training restricted to backward-looking data at least 12 months old; removal of auto-accept, "governor" guardrails, and "sold-out" guardrails that relied on competitors' data; prohibition on market surveys gathering nonpublic competitive intelligence for pricing; prohibition on discussing nonpublic data or pricing strategies at RealPage-hosted meetings attended by competing property managers; appointment of a court monitor for three years; RealPage becomes a government cooperator in ongoing DOJ cases against landlord defendants. The decree runs seven years, with possible early termination after four years. No financial penalties were imposed and RealPage admitted no liability.

The settlement is pending Tunney Act court approval in the Middle District of North Carolina. The 60-day public comment period must run before the court can enter final judgment.

**What it does not cover.** The case addresses algorithmic collusion (shared data inputs across competitors), not unilateral personalized pricing. A single landlord using its own proprietary data to set individualized rents would fall outside the Sherman Act Section 1 framework. The settlement imposes behavioral remedies on RealPage's software design but does not ban algorithmic pricing as such — it bans the use of competitors' nonpublic data in algorithmic pricing. The Fenwick analysis characterized the settlement as "a blueprint for 'safer' algorithmic pricing," and Duane Morris noted that "DOJ is not treating algorithmic pricing as inherently illegal."

The Biden CEA's December 2024 issue brief quantified the consumer harm: anticompetitive pricing algorithms cost renters in algorithm-utilizing buildings an average of $70 per month, totaling approximately $3.8 billion nationally in 2023. In six major metros, the cost exceeded $100 per month (Atlanta: $181/month, where 68% of multifamily landlords used RealPage).

### FTC v. Amazon.com, No. 2:23-cv-01495 (W.D. Wash.)

Filed September 26, 2023 by the FTC and initially 17 (now 19) state Attorneys General, this case alleges Amazon violated Section 2 of the Sherman Act and Section 5 of the FTC Act through monopolistic practices in the online marketplace. The pricing dimension centers on "Project Nessie," an internal Amazon algorithm that identified products for which Amazon predicted competing online stores would follow Amazon's price increases, raised prices on those products, monitored whether competitors followed, and kept the higher prices when they did. The FTC alleged Project Nessie generated over $1.4 billion in excess revenue, with $334 million in additional profit in 2018 alone.

In October 2024, the court denied Amazon's motion to dismiss the Section 2 and Section 5 claims, notably upholding the standalone Section 5 claim — the first such standalone Section 5 claim upheld in federal court in over 40 years. Some state-law claims (New Jersey, Pennsylvania) were subsequently dismissed. Trial is currently set for February 9, 2027.

**What it does not cover.** The case is primarily a monopolization case, not a surveillance pricing case. Project Nessie is an algorithmic pricing strategy (predatory price leadership/signaling), but it is not personalized pricing — it does not set different prices for different consumers based on their personal data. Its relevance to the surveillance pricing landscape is indirect: it establishes that algorithmic pricing strategies can constitute standalone Section 5 violations, which could provide an enforcement theory for future personalized pricing cases. The case also demonstrates that FTC enforcement against major platform algorithmic pricing practices has survived the change of administration — the case is proceeding to trial under the Ferguson FTC.

### Preventing Algorithmic Collusion Act, S. 232

Introduced January 23, 2025 by Senator Amy Klobuchar (D-MN) with eight co-sponsors (Wyden, Durbin, Blumenthal, Hirono, Lujan, Murphy, Shaheen, Welch), this bill is a reintroduction of S. 3686 from the 118th Congress (introduced January 30, 2024, which did not advance). The bill would make it unlawful for any person to "use or distribute any pricing algorithm that uses, incorporates, or was trained with nonpublic competitor data." It creates a rebuttable presumption of agreement under federal antitrust law when competitors share competitively sensitive information through a pricing algorithm. Civil penalties of at least $10,000 per day of violation or the total value of products sold using the algorithm. Requires pricing algorithm users to disclose to customers and employees when algorithms are used. Requires the FTC to conduct a comprehensive study on pricing algorithms within two years. Provides DOJ and FTC with audit authority: 30-day written response required upon request.

**What it does not cover.** The bill targets algorithmic collusion — the sharing of nonpublic competitor data through pricing algorithms. It does not address unilateral personalized pricing using a firm's own first-party consumer data. A retailer using its own customer browsing history to set individualized prices would fall outside scope. The bill codifies the enforcement theory of the RealPage case but does not extend beyond it.

### Stop AI Price Gouging and Wage Fixing Act, H.R. 4640

Introduced July 23, 2025 by Representative Greg Casar (D-TX) with Representative Rashida Tlaib (D-MI), this is the first federal proposal to directly ban the use of AI to set prices or wages based on personal data. The bill prohibits certain uses of "algorithmic decision systems" to inform individualized prices and wages. It requires companies to publish data accuracy procedures, allow consumers to correct or challenge data used in pricing, and disclose what data is considered and how automated systems set prices. Enforcement through FTC, state AGs, and a private right of action; EEOC for wage provisions. It exempts loyalty program discounts and group discounts (veterans, seniors).

**What it does not cover.** The bill is the only federal proposal that reaches unilateral personalized pricing based on consumer data (not just competitor data sharing). However, it has near-zero prospect of passage in the 119th Congress: introduced by progressive Democrats, referred to committee, no Republican co-sponsors, and the current administration has signaled a deregulatory approach to AI. Its significance is as a marker of maximum legislative ambition at the federal level — a ceiling against which other instruments can be measured.

### Executive Order 14110 (Revoked)

Signed October 30, 2023, EO 14110 ("Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence") was the Biden administration's omnibus AI governance instrument. Section 8 directed federal agencies to use existing consumer protection laws to enforce against fraud, bias, discrimination, and privacy infringements arising from AI, including in commercial settings. The order did not specifically address algorithmic pricing but created a general mandate for agencies to apply existing authority to AI-mediated consumer harms.

President Trump revoked EO 14110 on January 20, 2025, through Executive Order 14148 ("Initial Rescissions of Harmful Executive Orders and Actions"). On January 23, 2025, Trump signed EO 14179 ("Removing Barriers to American Leadership in Artificial Intelligence"), which replaced EO 14110's regulatory orientation with a pro-innovation framework emphasizing AI development "free from ideological bias or social agendas." No consumer protection or pricing-specific provisions were included in the replacement order.

### FTC Section 5 Authority — Background Law

FTC Act Section 5 (15 U.S.C. s. 45) prohibits "unfair or deceptive acts or practices" (UDAP) and "unfair methods of competition" (UMC). This is the FTC's general-purpose enforcement authority and the legal basis for both the surveillance pricing study and the Amazon litigation. The authority is not surveillance-pricing-specific but provides the enforcement theory under which the FTC could act.

The November 2022 Policy Statement expanded the FTC's interpretation of UMC to reach conduct that is "coercive, exploitative, collusive, abusive, deceptive, predatory, or involves the use of economic power of a similar nature" — even without proof of antitrust harm or market power. The standalone Section 5 claim in the Amazon case was upheld under this expanded interpretation. Whether the Ferguson FTC will rescind or narrow the 2022 Policy Statement remains an open question; the U.S. Chamber of Commerce and industry groups have urged withdrawal.

**Operation AI Comply** (launched September 2024) represented the FTC's enforcement sweep against deceptive AI claims, resulting in five initial enforcement actions. While none directly targeted algorithmic pricing, the initiative signaled willingness to use Section 5 against AI-mediated commercial practices. The sweep has continued under Ferguson, suggesting bipartisan enforcement support for the deception prong — though not necessarily for the unfairness or competition prongs as applied to pricing.

## Analysis

**Hierarchy.** Competition dominates. The most consequential federal action is antitrust enforcement — DOJ v. RealPage produced a consent decree that will reshape algorithmic pricing software design in rental housing for seven years, and FTC v. Amazon is proceeding to trial. Disclosure (the 6(b) study) was the next most active channel but has been paused. Proposed legislation occupies two positions — S. 232 codifies the competition strategy (algorithmic collusion), while H.R. 4640 attempts command and control (prohibition of personalized pricing) — but neither has advanced. Rights and self-regulation are absent as affirmative strategies; code-as-regulation is absent; nudge is absent; incentive-based approaches are absent. The hierarchy is: competition (operative) > disclosure (stalled) > command and control (proposed, no prospect) > everything else (absent).

**Design logic.** Accumulated (enforcement-driven subtype). The federal instruments emerged from different institutional actors (DOJ Antitrust, FTC, Congress, White House), different legal bases (Sherman Act, FTC Act, legislative proposals, executive authority), and different eras (2015 OSTP study, 2022 Section 5 Policy Statement, 2023 executive order, 2024 enforcement actions, 2025 legislative proposals). There is no unified federal strategy for surveillance pricing. The DOJ prosecutes collusion under antitrust law; the FTC studied the practice under consumer protection authority; Congress proposed legislation under different theories (competition, prohibition); the White House issued and then revoked an executive order. The accumulation is compounded by partisan discontinuity: the 2025 change of administration effectively severed the consumer protection track while preserving the antitrust track. This produces a fractured landscape where the only operative instruments are antitrust enforcement actions inherited from the prior administration.

**Institution relied on — divergence.** Two significant divergences. First, the FTC 6(b) study is formally a disclosure instrument — it gathers and publishes information to enable informed regulatory and consumer action. But the institution the study actually relied on was the FTC Commission itself (specifically, the Democratic majority that authorized and released the study). When the institution changed (Ferguson replaced Khan as Chair), the disclosure instrument was effectively neutralized — not because the information became less relevant, but because the institution controlling its production changed political orientation. Disclosure here depends not on markets disciplining firms after receiving information, but on a politically contingent regulatory body choosing to produce information at all.

Second, the DOJ RealPage settlement deploys competition strategy — breaking algorithmic collusion to restore competitive discipline. But the settlement's detailed behavioral requirements (software redesign, data age restrictions, meeting conduct rules, monitor appointment) function more like command-and-control regulation than traditional antitrust remedy. The institution relied on is the DOJ Antitrust Division and a court-appointed monitor, not market forces. The settlement creates a de facto regulatory code for algorithmic pricing software in rental housing, achieved through litigation rather than legislation.

## Evidence

- **DOJ v. RealPage**: Proposed consent decree filed November 24, 2025. No financial penalties; behavioral remedies only. Seven-year decree with three-year monitor. Pending Tunney Act approval. *United States et al. v. RealPage, Inc.*, No. 1:24-cv-00710 (M.D.N.C.). [DOJ Press Release (Nov 2025)](https://www.justice.gov/opa/pr/justice-department-requires-realpage-end-sharing-competitively-sensitive-information-and)
- **CEA consumer harm quantification**: $3.8 billion annual cost to renters nationally (2023); $70/month average increase for renters in algorithm-utilizing buildings; $181/month in Atlanta (68% adoption rate). [CEA Issue Brief (Dec 17, 2024)](https://bidenwhitehouse.archives.gov/cea/written-materials/2024/12/17/the-cost-of-anticompetitive-pricing-algorithms-in-rental-housing/)
- **FTC v. Amazon**: Project Nessie generated over $1.4 billion in excess revenue; $334 million in additional profit in 2018. Standalone Section 5 claim upheld — first in over 40 years. Trial set for February 9, 2027. *FTC et al. v. Amazon.com, Inc.*, No. 2:23-cv-01495-JHC (W.D. Wash.). [BCLP Analysis](https://www.bclplaw.com/en-US/events-insights-news/the-ftc-and-state-case-against-amazon-highlights-risks-and-impacts-from-using-pricing-algorithms.html)
- **FTC 6(b) study**: 250+ retailers identified as using surveillance pricing across grocery, apparel, health/beauty, home goods, convenience, hardware sectors. Eight intermediary companies ordered to produce documents (Mastercard, Revionics, Bloomreach, JPMorgan Chase, Task Software, PROS, Accenture, McKinsey). 3-2 vote to release findings (Jan 17, 2025); public comment period closed by Ferguson (Jan 24, 2025). [FTC Press Release (Jan 2025)](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-surveillance-pricing-study-indicates-wide-range-personal-data-used-set-individualized-consumer); [Ferguson-Holyoak Dissent](https://www.ftc.gov/system/files/ftc_gov/pdf/surveillance-pricing-6b-research-summaries-ferguson-dissent-final.pdf)
- **Bipartisan congressional pressure**: Warner-Hawley-Blumenthal-Gallego letter to Ferguson (Dec 17, 2025) urging FTC to reopen surveillance pricing investigation; Rosen letter (Mar 25, 2025) urging reopening of public comment period. [Warner Press Release (Dec 2025)](https://www.warner.senate.gov/public/index.cfm/2025/12/warner-leads-bipartisan-effort-to-push-ftc-to-crack-down-on-surveillance-pricing-with-holiday-shopping-season-underway)

## Movement

1. **February 2015**: White House CEA/OSTP releases "Big Data and Differential Pricing" report — first federal acknowledgment of algorithmic pricing as a policy concern. Concludes existing laws are largely adequate; recommends transparency. No legislative or regulatory follow-through.
2. **November 2022**: FTC issues expanded Section 5 Policy Statement — broadens UMC enforcement authority beyond Sherman Act standards.
3. **September 2023**: FTC files suit against Amazon (including Project Nessie algorithmic pricing claims).
4. **October 2023**: Biden signs EO 14110 — directs agencies to use existing authority against AI-mediated consumer harms, including in commercial settings. No pricing-specific provisions.
5. **January 2024**: Senator Klobuchar introduces S. 3686 (Preventing Algorithmic Collusion Act) in 118th Congress. Does not advance.
6. **July 2024**: FTC issues 6(b) orders to eight surveillance pricing intermediaries — first systematic federal investigation of the practice.
7. **August 2024**: DOJ files suit against RealPage — first federal antitrust case directly challenging algorithmic pricing software as facilitating collusion.
8. **September 2024**: FTC launches Operation AI Comply — enforcement sweep against deceptive AI claims (not pricing-specific).
9. **October 2024**: Court denies Amazon's motion to dismiss Section 2 and Section 5 claims, including standalone Section 5 (first in 40+ years).
10. **December 2024**: CEA publishes issue brief quantifying $3.8 billion annual renter harm from algorithmic pricing.
11. **January 17, 2025**: FTC releases surveillance pricing study findings (3-2 vote, Ferguson-Holyoak dissent).
12. **January 20, 2025**: Trump inaugurated; revokes EO 14110; Ferguson becomes FTC Chair.
13. **January 23, 2025**: Klobuchar reintroduces Preventing Algorithmic Collusion Act as S. 232 (119th Congress).
14. **January 24, 2025**: Ferguson closes surveillance pricing RFI public comment period.
15. **July 23, 2025**: Casar introduces Stop AI Price Gouging and Wage Fixing Act (H.R. 4640) — first federal prohibition proposal.
16. **November 24, 2025**: DOJ and RealPage announce proposed consent decree — landmark algorithmic pricing settlement.
17. **December 2025**: Bipartisan Senate group (Warner, Hawley, Blumenthal, Gallego) writes to Ferguson urging FTC to reopen surveillance pricing investigation.

## Sources

**Primary**:
- *United States et al. v. RealPage, Inc.*, No. 1:24-cv-00710 (M.D.N.C. 2024). [DOJ Complaint](https://www.justice.gov/opa/media/1410741/dl); [Proposed Final Judgment (Nov 2025)](https://www.justice.gov/opa/pr/justice-department-requires-realpage-end-sharing-competitively-sensitive-information-and)
- *FTC et al. v. Amazon.com, Inc.*, No. 2:23-cv-01495-JHC (W.D. Wash. 2023). [Revised Redacted Complaint](https://www.ftc.gov/system/files/ftc_gov/pdf/1910134amazonecommercecomplaintrevisedredactions.pdf)
- [FTC 6(b) Surveillance Pricing Orders (July 2024)](https://www.ftc.gov/news-events/news/press-releases/2024/07/ftc-issues-orders-eight-companies-seeking-information-surveillance-pricing)
- [FTC Surveillance Pricing Study Research Summaries (Jan 2025)](https://www.ftc.gov/system/files/ftc_gov/pdf/p246202_surveillancepricing6bstudy_researchsummaries_redacted.pdf)
- [Ferguson-Holyoak Dissent on Surveillance Pricing Study (Jan 2025)](https://www.ftc.gov/system/files/ftc_gov/pdf/surveillance-pricing-6b-research-summaries-ferguson-dissent-final.pdf)
- [Preventing Algorithmic Collusion Act of 2025, S. 232](https://www.congress.gov/bill/119th-congress/senate-bill/232/text)
- [Stop AI Price Gouging and Wage Fixing Act of 2025, H.R. 4640](https://www.congress.gov/bill/119th-congress/house-bill/4640/text/ih)
- [EO 14110, Safe, Secure, and Trustworthy AI (Oct 2023)](https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence)
- [EO 14179, Removing Barriers to American Leadership in AI (Jan 2025)](https://www.whitehouse.gov/presidential-actions/2025/01/removing-barriers-to-american-leadership-in-artificial-intelligence/)
- [CEA Issue Brief, "Cost of Anticompetitive Pricing Algorithms in Rental Housing" (Dec 2024)](https://bidenwhitehouse.archives.gov/cea/written-materials/2024/12/17/the-cost-of-anticompetitive-pricing-algorithms-in-rental-housing/)
- [CEA/OSTP, "Big Data and Differential Pricing" (Feb 2015)](https://obamawhitehouse.archives.gov/blog/2015/02/06/economics-big-data-and-differential-pricing)
- [FTC Section 5 Policy Statement (Nov 2022)](https://www.ftc.gov/system/files/ftc_gov/pdf/P221202Section5PolicyStatement.pdf)
- [Warner-Hawley-Blumenthal-Gallego Letter to Ferguson (Dec 17, 2025)](https://www.warner.senate.gov/public/_cache/files/f/2/f2a2d4c9-fcd8-4657-a975-bbb44f355352/247826215C0FDEB472CAD25C116BE9F9C7FA4EB79AE462CDD70D6225A30442F0.251217.ferguson-warner-hawley-blumenthal-gallego-re-surveilliance-pricing.final.sign.pdf)
- [Rosen Letter to Ferguson (Mar 25, 2025)](https://www.rosen.senate.gov/wp-content/uploads/2025/03/3.25.2025.-Letter-to-Chair-on-Surveillance-Pricing-RFI.pdf)

**Secondary**:
- [Paul, Weiss, "Practical Takeaways From the DOJ's Algorithmic Pricing Settlement" (Dec 2025)](https://www.paulweiss.com/insights/client-memos/practical-takeaways-from-the-doj-s-algorithmic-pricing-settlement)
- [Wilson Sonsini, "DOJ Settles Its Algorithmic Price-Fixing Case Against RealPage" (Dec 2025)](https://www.wsgr.com/en/insights/doj-settles-its-algorithmic-price-fixing-case-against-realpage.html)
- [Fenwick, "DOJ's RealPage Settlement: A Blueprint for 'Safer' Algorithmic Pricing" (Dec 2025)](https://www.fenwick.com/insights/publications/dojs-realpage-settlement-a-blueprint-for-safer-algorithmic-pricing)
- [Duane Morris, "RealPage Settlement Shows DOJ Is Not Treating Algorithmic Pricing as Inherently Illegal" (Dec 2025)](https://www.duanemorris.com/articles/realpage_settlement_shows_doj_not_treating_algorithmic_pricing_as_inherently_illegal_1225.html)
- [Hogan Lovells, "Proposed DOJ Settlement Provides Guidance on Use of Competitive Information" (Dec 2025)](https://www.hoganlovells.com/en/publications/proposed-doj-settlement-provides-guidance-on-use-of-competitive-information)
- [Reed Smith, "Algorithmic Pricing Under Pressure: DOJ's RealPage Settlement" (Dec 2025)](https://www.reedsmith.com/our-insights/blogs/viewpoints/102lwqx/algorithmic-pricing-under-pressure-dojs-realpage-settlement-changes-the-rules-f/)
- [BCLP, "FTC and State Case Against Amazon Highlights Risks from Pricing Algorithms" (2023)](https://www.bclplaw.com/en-US/events-insights-news/the-ftc-and-state-case-against-amazon-highlights-risks-and-impacts-from-using-pricing-algorithms.html)
- [DLA Piper, "The Preventing Algorithmic Collusion Act: Strike Two" (Feb 2025)](https://www.dlapiper.com/en-us/insights/publications/2025/02/the-preventing-algorithmic-collusion-act-2025)
- [Klobuchar Press Release, S. 232 (Jan 2025)](https://www.klobuchar.senate.gov/public/index.cfm/2025/2/klobuchar-colleagues-introduce-antitrust-legislation-to-take-on-algorithmic-price-fixing-bring-down-costs)
- [Casar Press Release, H.R. 4640 (July 2025)](https://casar.house.gov/media/press-releases/news-congressman-greg-casar-introduces-new-stop-ai-price-gouging-and-wage)
- [Future of Privacy Forum, "A Price to Pay: U.S. Lawmaker Efforts to Regulate Algorithmic Pricing" (2025)](https://fpf.org/blog/a-price-to-pay-u-s-lawmaker-efforts-to-regulate-algorithmic-and-data-driven-pricing/)
- [ProPublica, "DOJ and RealPage Agree to Settle Rental Price-Fixing Case" (Nov 2025)](https://www.propublica.org/article/doj-realpage-settlement-rental-price-fixing-case)
- [McCarter & English, "FTC Surveillance Pricing Study Finds Personal Data Used to Set Individualized Prices" (Jan 2025)](https://www.mccarter.com/insights/ftc-surveillance-pricing-study-finds-personal-data-is-used-to-set-individualized-consumer-prices-and-generate-higher-profits-for-companies/)
- [Retail Brew, "New FTC Chair Shuts Down Public Comment on Surveillance Pricing" (Jan 2025)](https://www.retailbrew.com/stories/2025/01/24/new-ftc-chair-shuts-down-public-comment-on-retailers-surveillance-pricing)
- [Wiley, "President Trump Revokes Biden Administration's AI EO: What To Know" (Jan 2025)](https://www.wiley.law/alert-President-Trump-Revokes-Biden-Administrations-AI-EO-What-To-Know)
- [Alston & Bird, "First 100 Days: Federal Privacy and Cybersecurity Under Trump" (May 2025)](https://www.alston.com/en/insights/publications/2025/05/federal-privacy-cybersecurity-trump-administration)
- [Consumer Reports Innovation, "How U.S. States Are Tackling Algorithmic Pricing" (2025)](https://innovation.consumerreports.org/how-u-s-states-are-tackling-algorithmic-pricing-2025-bill-tracker-and-analysis/)
