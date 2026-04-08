---
date-created: "202602242200"
aliases:
  - "California surveillance pricing profile"
tags:
  - "#molecules"
  - "#jurisdiction-profile"
topic:
  - "[[surveillance pricing]]"
  - "[[California]]"
---

# California — Surveillance Pricing Regulatory Profile

*Jurisdiction molecule for [[surveillance-pricing-comparative-regulation|Paper 1]].*

California's primary position is competition — targeting shared algorithms through antitrust reform (AB 325) and enforcement (RealPage/Greystar) — but the AG is pivoting laterally to privacy law (CCPA) to reach the proprietary personalized pricing that antitrust cannot touch, after the legislature blocked prohibition attempts.

## Instruments

| Instrument | Strategy | Sector | Status | Enforcement |
|-----------|----------|--------|--------|-------------|
| AB 325 (Jan 2026) | [[competition-over-regulation|Competition]] | General (shared algorithms only; proprietary exempt) | Operative | AG (enhanced criminal/civil penalties); private action under [[Cartwright Act]] with treble damages |
| SB 763 (Jan 2026) | Competition | General (pleading standard reform + coercion liability) | Operative | Private action (lowered pleading burden); AG |
| AG v. RealPage / Greystar (Jan 2025-Nov 2025) | Competition | Residential rental | Settlement (Greystar $7M); RealPage pending | AG under UCL; nine-state coalition |
| AG CCPA Surveillance Pricing Sweep (Jan 2026) | Rights & liabilities (deployed as enforcement) | Retail, grocery, hotel | Inquiry phase | AG investigative authority under CCPA |
| AB 446 (Feb 2025) | Prohibition | General (narrowed to grocery; withdrawn) | Failed (Sept 2025) | Would have included private right of action |
| SB 259 (2025) | Prohibition | Online pricing | Failed (inactive file Sept 2025) | Would have included private right of action |
| SB 295 (2025) | Competition (expanded) | Algorithm distributors | Failed; carries over to 2026 | Would have included affirmative defense for due diligence |

## Detail

### AB 325 — Common Pricing Algorithms Act (eff. Jan 1, 2026)

AB 325 amends the [[Cartwright Act]] (California's antitrust statute) to add Business and Professions Code section 16729, creating two new forms of liability for algorithmic pricing coordination.

**Section 16729(a) — shared algorithm liability.** Makes it unlawful for two or more persons to share, combine, or exchange competitively sensitive nonpublic information through a common pricing algorithm, where the algorithm recommends or sets a price for goods or services. This captures the RealPage model: multiple competitors feed data into a shared system that outputs pricing recommendations.

**Section 16729(b) — coercion liability.** Makes it unlawful to coerce, compel, or incentivize any person to adopt or adhere to a price recommended by a common pricing algorithm. The term "coerce" is not defined — a significant interpretive gap.

**What it does NOT reach.** AB 325 explicitly does not reach proprietary, internally developed algorithms used by a single firm. A company that uses only its own data to personalize prices is not covered. This is the critical gap that distinguishes California's competition strategy from a prohibition strategy.

**Primary**: [AB 325 text (California Legislature)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB325)

**Secondary**: [Alston & Bird, "California's AB 325 Prohibits Shared Pricing Algorithms" (Nov 2025)](https://www.alston.com/en/insights/publications/2025/11/california-ab-325-antitrust-standards); [Cleary Gottlieb, "California's Antitrust Law Amendments Kick In" (Jan 2026)](https://www.clearygottlieb.com/news-and-insights/publication-listing/californias-antitrust-law-amendments-kick-in-targeting-algorithmic-pricing); [Morgan Lewis, "Algorithmic Pricing Antitrust Amendments Take Effect" (Jan 2026)](https://www.morganlewis.com/pubs/2026/01/californias-algorithmic-pricing-antitrust-amendments-to-the-cartwright-act-take-effect); [Pillsbury, "New California Laws Target Shared Pricing Algorithms and Coercion"](https://www.pillsburylaw.com/en/news-and-insights/ab-325-shared-pricing-algorithms-liability-california.html); [WilmerHale, "California Zeroes in on Common Pricing Algorithms" (Nov 2025)](https://www.wilmerhale.com/en/insights/client-alerts/20251114-california-zeroes-in-on-common-pricing-algorithms); [Paul Weiss, "California Restricts Use of Common Pricing Algorithms"](https://www.paulweiss.com/insights/client-memos/california-restricts-use-of-common-pricing-algorithms); [Davis Polk, "New Laws Regulating Algorithmic Pricing Enacted in New York and California"](https://www.davispolk.com/insights/client-update/new-laws-regulating-algorithmic-pricing-enacted-new-york-and-california); [Arnold & Porter, "Algorithmic Pricing Bans Go Coast to Coast" (Oct 2025)](https://www.arnoldporter.com/en/perspectives/advisories/2025/10/algorithmic-pricing-bans-go-coast-to-coast)

### SB 763 — Antitrust Pleading Standard Reform (eff. Jan 1, 2026)

SB 763 amends California's antitrust pleading standard, reversing the prior requirement that plaintiffs allege specific facts establishing an antitrust conspiracy at the pleading stage. Under SB 763, antitrust claims need only meet the general federal pleading standard (plausibility under *Twombly*/*Iqbal*), rather than the heightened specificity California courts had previously required.

**Significance for algorithmic pricing.** The lowered pleading standard makes it easier for private plaintiffs to survive a motion to dismiss in algorithmic pricing cases — where direct evidence of agreement is often unavailable because the algorithm itself mediates the coordination. Several law firm analyses describe this as a "game-changer" for private antitrust litigation targeting algorithmic pricing.

**Primary**: [SB 763 text (California Legislature)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB763)

**Secondary**: [Morgan Lewis, "California Clarifies Antitrust Pleading Standard" (Oct 2025)](https://www.morganlewis.com/pubs/2025/10/california-clarifies-antitrust-pleading-standard-creates-uncertainty-on-coercive-uses-of-algorithmic-software); [Vinson & Elkins, "California Boosts Antitrust Enforcement With Two New Laws"](https://www.velaw.com/insights/california-boosts-antitrust-enforcement-with-two-new-laws/)

### AG v. RealPage / Greystar Settlement (complaint Jan 2025; settlement Nov 2025)

California AG Bonta, alongside the DOJ and a coalition of nine attorneys general (North Carolina, Colorado, Connecticut, Illinois, Massachusetts, Minnesota, Oregon, Tennessee), filed a complaint in January 2025 against RealPage and five property management companies — Camden, Cushman & Wakefield/Pinnacle, LivCor, Willow Bridge, and Greystar.

**The allegations.** RealPage's revenue management software collected competitively sensitive data from competing landlords — real-time pricing, supply levels, lease terms — and used algorithmic models to generate uniform pricing recommendations. The AG alleged this constituted an illegal pricing alignment scheme that artificially raised rents.

**Greystar settlement (Nov 2025).** Greystar, the largest landlord in the United States (managing nearly 950,000 rental units), settled for $7 million. Key terms: stop using software from any company, including RealPage, that uses competitively sensitive information to align rent prices; accept a court-appointed monitor if using a third-party pricing algorithm; cooperate with the states' monopolization claims against RealPage.

**RealPage litigation continues.** The case against RealPage itself remains pending. The federal DOJ settlement with RealPage (November 2025, seven-year term) is a separate action; California's state-level claims under the Unfair Competition Law provide an independent enforcement pathway.

**Primary**: [CA AG Greystar settlement press release (Nov 2025)](https://oag.ca.gov/news/press-releases/attorney-general-bonta-announces-7-million-settlement-greystar-participating); [CA AG amended complaint press release](https://oag.ca.gov/news/press-releases/attorney-general-bonta-files-amended-complaint-realpage-lawsuit-seeks-hold)

**Secondary**: [Wilson Sonsini, "DOJ Settles Algorithmic Price-Fixing Case Against RealPage"](https://www.wsgr.com/en/insights/doj-settles-its-algorithmic-price-fixing-case-against-realpage.html); [Mintz, "Greystar Reaches Settlement Agreement" (Aug 2025)](https://www.mintz.com/insights-center/viewpoints/2025-08-13-no-day-today-greystar-reaches-settlement-agreement-department); [Multifamily Dive, "9 States Reach $7M Settlement with Greystar"](https://www.multifamilydive.com/news/greystar-settlement-rent-setting-algorithms/806095/)

### AG Surveillance Pricing Investigative Sweep (Jan 28, 2026)

On Data Privacy Day (January 28, 2026), AG Bonta announced a new investigative sweep targeting surveillance pricing — the use of consumers' personal information to set individualized prices. This action is significant because it operates under CCPA authority, not antitrust, reaching conduct that AB 325 cannot touch: proprietary, single-firm personalized pricing.

**Legal theory.** The AG frames surveillance pricing as a potential CCPA violation under the statute's purpose limitation principle — businesses may only use personal information for purposes consistent with consumers' reasonable expectations. Using browsing history, demographics, location, and shopping patterns to set individualized prices may violate this standard if consumers do not reasonably expect their data to be used for pricing.

**Scope.** Inquiry letters directed at businesses with "significant online presence" in retail, grocery, and hotel sectors.

**Significance for the regulatory profile.** This is the first enforcement action in California that reaches proprietary personalized pricing. AB 325 catches shared algorithms; the CCPA sweep catches individualized pricing by single firms. Together, they theoretically cover both coordination and personalization — but the CCPA theory is untested and rests on an interpretive stretch of "purpose limitation" rather than explicit statutory text addressing pricing.

**Primary**: [CA AG press release (Jan 28, 2026)](https://oag.ca.gov/news/press-releases/data-privacy-day-attorney-general-bonta-focuses-surveillance-pricing-compliance)

**Secondary**: [Alston & Bird, "California Attorney General Announces Investigative Sweep" (Jan 2026)](https://www.alstonprivacy.com/california-attorney-general-announces-investigative-sweep-into-surveillance-pricing/); [Troutman Pepper, "Is Individualized Pricing the Next Big Privacy Enforcement Issue?" (Feb 2026)](https://www.troutmanprivacy.com/2026/02/is-individualized-pricing-the-next-big-privacy-enforcement-issue-california-ag-announces-investigative-sweep-around-surveillance-pricing-practices/); [Reed Smith, "California Launches Investigative Sweep on Surveillance Pricing"](https://www.reedsmith.com/articles/california-launches-investigative-sweep-on-surveillance-pricing-to-enforce-ccpa-compliance/); [Fenwick, "California AG Launches Investigative Sweep"](https://www.fenwick.com/insights/publications/california-ag-launches-investigative-sweep-on-surveillance-pricing-practices)

### Failed and Pending Bills — AB 446, SB 259, SB 295

Three additional bills attempted broader surveillance pricing regulation in 2025. All failed or stalled, but the pattern is informative.

**AB 446 — Surveillance Pricing Protection Act (Feb 2025).** Assemblymember Ward introduced a comprehensive prohibition on surveillance pricing — making it unlawful for any business to set prices based on personally identifiable information gathered through electronic surveillance. In August 2025, the Senate Appropriations Committee dramatically narrowed the bill to cover only grocery prices. Ward withdrew the bill in September 2025 rather than advance the gutted version. Consumer Watchdog attributed the failure to "industry disinformation."

**SB 259 — Fair Online Pricing Act (2025).** Senator Wahab's bill would have prohibited businesses from setting online prices based on device-specific data and geolocation. Passed the Senate 30-9 and cleared Assembly Privacy and Consumer Protection Committee, but was ordered to inactive file in September 2025.

**SB 295 — Preventing Algorithmic Collusion Act (2025).** Would have prohibited distributing or making recommendations based on a pricing algorithm to two or more competitors if the distributor knows or should know the algorithm processes competitor data. Failed on third reading but was granted reconsideration and carries over to the 2026 session.

**Pattern.** The legislature attempted to move from competition (AB 325, which passed) to prohibition (AB 446, SB 259) and was blocked. The competition strategy succeeded; the prohibition strategy did not. This is a meaningful finding for the topology: California's political economy permits antitrust intervention against coordination but resists direct prohibition of personalized pricing.

**Primary**: [AB 446 text](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB446); [SB 259 text](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB259); [SB 295 text](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB295)

**Secondary**: [National Law Review, "California Largely Strikes Down Surveillance Pricing Bill" (2025)](https://natlawreview.com/article/price-you-pay-california-largely-strikes-down-bill-banning-surveillance-pricing); [Consumer Reports, "AB 446 Fails to Advance" (2025)](https://advocacy.consumerreports.org/press_release/californias-surveillance-pricing-protection-act-ab-446-fails-to-advance-california-legislature/); [Consumer Watchdog, "Industry Disinformation Kills Surveillance Pricing Bill" (Sept 2025)](https://www.prnewswire.com/news-releases/industry-disinformation-kills-surveillance-pricing-bill-as-a-result-ab-446-is-withdrawn-says-consumer-watchdog-302548071.html)

## Analysis

**Hierarchy.** Competition dominates. AB 325 is the only enacted statute. The Greystar/RealPage litigation predates it but operates on the same competition logic — targeting coordination via shared algorithms. The AG's CCPA surveillance pricing sweep operates on a different strategy (using privacy law as enforcement) but is in its inquiry phase, not yet a formal enforcement action, and relies on an untested legal theory. The enacted law and the settled enforcement actions are all competition; the privacy angle is emergent and unproven.

**Design logic.** Accumulated. California did not design its current instrument set in a single legislative moment. AB 325 was enacted in October 2025 as a Cartwright Act amendment targeting algorithmic coordination. The RealPage litigation began in January 2025 under the existing Unfair Competition Law. The CCPA surveillance pricing sweep launched in January 2026 under privacy authority. Each instrument has a different legal basis (antitrust statute, unfair competition law, privacy law) and targets different conduct (shared algorithms, rental coordination, proprietary personalized pricing). The failed prohibition bills (AB 446, SB 259) show that the legislature attempted to unify the approach under a prohibition strategy and was blocked. The resulting instrument set is accumulated rather than designed — different legal tools deployed at different moments by different institutional actors (legislature, AG) under different legal authorities.

This is the opposite of New York's differentiated approach. New York deliberately chose different strategies for different sectors in the same legislative session. California's competition strategy was legislated; its privacy enforcement strategy was improvised by the AG when the prohibition strategy failed legislatively.

**Institution relied on — divergence.** AB 325 is a competition strategy, which theoretically relies on market structure — breaking algorithmic coordination restores competitive discipline. The enforcement mechanism is consistent: both public enforcement (AG with enhanced criminal/civil penalties) and private enforcement (Cartwright Act treble damages). The pleading standard reform (SB 763) amplifies the institution that competition strategy relies on — market participants suing competitors.

The CCPA sweep introduces a divergence. Privacy law is a rights-based instrument (consumers control their data), but the AG is deploying it as an enforcement tool — not empowering consumers to exercise opt-out rights, but using state investigative authority to probe pricing practices. The institution relied on is the state, not individuals. This is similar to the divergence observed in New York's A6765 (disclosure strategy relying on state enforcement rather than market discipline), though here the pivot is from rights to state enforcement rather than from disclosure to state enforcement.

## Evidence

**No AB 325 enforcement actions yet.** The law took effect January 1, 2026. No cases have been filed under the new provisions as of February 2026. The lowered pleading standard, however, is expected to increase private litigation — several law firm analyses describe AB 325 as a "game-changer" for algorithmic pricing litigation. [Vega Economics analysis](https://vegaeconomics.com/california-ab-325-is-effective-january-1-2026-a-game-changer-for-algorithmic-pricing-litigation); [Jones Walker analysis](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/algorithmic-pricing-risk-business-implications-from-californias-new-law-and-bey.html)

**Greystar settlement as precedent.** The $7M settlement with Greystar is the only completed enforcement action in California's surveillance pricing landscape. Its significance: it establishes that using a shared pricing algorithm with competitors' nonpublic data constitutes an actionable antitrust violation under California law; the consent decree's terms (stop using RealPage software, court-appointed monitor, cooperation obligations) provide a behavioral template for future settlements; and the nine-state coalition model demonstrates coordinated state-level enforcement as a substitute for federal action. [CA AG press release](https://oag.ca.gov/news/press-releases/attorney-general-bonta-announces-7-million-settlement-greystar-participating)

**CCPA sweep — no outcomes yet.** The January 2026 investigative sweep is in its inquiry phase. No enforcement actions, settlements, or formal charges have resulted as of February 2026. If the AG successfully applies CCPA purpose limitation to surveillance pricing, it would establish privacy law as a viable enforcement mechanism for personalized pricing — filling the gap that AB 325 leaves for proprietary algorithms. [CA AG press release](https://oag.ca.gov/news/press-releases/data-privacy-day-attorney-general-bonta-focuses-surveillance-pricing-compliance)

**Legislative defeat of prohibition bills.** AB 446's failure is itself evidence. The bill was introduced broadly, narrowed under industry pressure (the Senate Appropriations Committee limited it to grocery prices only), and ultimately withdrawn by its own author. Consumer Watchdog and Consumer Reports both attributed the failure to industry lobbying. This demonstrates the political economy constraint on prohibition in California: the legislature can target coordination (AB 325 passed) but not personalization (AB 446, SB 259 failed). [Consumer Reports](https://advocacy.consumerreports.org/press_release/californias-surveillance-pricing-protection-act-ab-446-fails-to-advance-california-legislature/); [Consumer Watchdog (Sept 2025)](https://www.prnewswire.com/news-releases/industry-disinformation-kills-surveillance-pricing-bill-as-a-result-ab-446-is-withdrawn-says-consumer-watchdog-302548071.html)

## Movement

California's movement is rapid but directionally constrained. In twelve months (January 2025 to January 2026):

1. **January 2025**: AG files RealPage/Greystar complaint (competition under existing law)
2. **February 2025**: AB 446, SB 259, SB 295 introduced (prohibition and expanded competition strategies)
3. **September 2025**: AB 446 withdrawn, SB 259 inactive (prohibition strategy defeated)
4. **October 2025**: AB 325 and SB 763 signed (competition — new statutory authority)
5. **November 2025**: Greystar settlement ($7M, nine-state coalition)
6. **January 2026**: AB 325 takes effect; AG launches CCPA surveillance pricing sweep (privacy-based enforcement)

The trajectory: California tried to move from competition to prohibition and was blocked. The AG then pivoted laterally — from antitrust to privacy — to reach the conduct that AB 325 cannot touch (proprietary personalized pricing). This lateral move is notable: rather than escalating on the intervention ladder (from competition to prohibition), the AG found an alternative legal basis (CCPA) to reach the same conduct through a different institutional pathway. Whether this lateral move succeeds depends entirely on whether the CCPA purpose limitation theory holds.

The failed bills are as informative as the enacted ones. They reveal that California's political economy draws a line: coordination between competitors is targetable (antitrust frame, bipartisan legitimacy); personalization by individual firms is not (industry opposition, appropriations committee gatekeeping).

## Open Questions

1. **Will the CCPA purpose limitation theory hold?** The AG's surveillance pricing sweep relies on interpreting "consistent with reasonable expectations" to prohibit personalized pricing. No court has tested this theory. If it fails, California has no statutory instrument reaching proprietary personalized pricing.
2. **AB 325 litigation trajectory.** Will plaintiffs target software vendors (algorithm distributors) or their clients (algorithm users), or both?
3. **What does "coerce" mean?** Section 16729(b) creates liability for coercing adoption of algorithm-recommended prices but does not define "coerce." Does a software vendor's default setting constitute coercion? Does a contractual penalty for deviating?
4. **SB 295 carryover.** The Preventing Algorithmic Collusion Act carries over to the 2026 session. Would it complement or redundantly overlap AB 325?
5. **Proprietary algorithm migration.** AB 325's shared-algorithm prohibition creates an incentive for firms to develop proprietary algorithms using only internal data. Does this migration undermine the statute's effectiveness, or is restoring competitive pricing (even if personalized) the intended policy outcome?
6. **Interaction with federal DOJ RealPage settlement.** Can conduct that complies with the DOJ settlement still violate California law?
7. **Industry response to CCPA sweep.** Will targeted businesses preemptively modify pricing practices, or contest the AG's authority?

## Sources

**Primary**:
- [AB 325 text (California Legislature)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB325)
- [SB 763 text (California Legislature)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB763)
- [AB 446 text (California Legislature)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB446)
- [SB 259 text (California Legislature)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB259)
- [SB 295 text (California Legislature)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB295)
- [CA AG Greystar settlement press release (Nov 2025)](https://oag.ca.gov/news/press-releases/attorney-general-bonta-announces-7-million-settlement-greystar-participating)
- [CA AG amended complaint press release — RealPage](https://oag.ca.gov/news/press-releases/attorney-general-bonta-files-amended-complaint-realpage-lawsuit-seeks-hold)
- [CA AG surveillance pricing investigative sweep press release (Jan 28, 2026)](https://oag.ca.gov/news/press-releases/data-privacy-day-attorney-general-bonta-focuses-surveillance-pricing-compliance)

**Secondary**:
- [Alston & Bird, "California's AB 325" (Nov 2025)](https://www.alston.com/en/insights/publications/2025/11/california-ab-325-antitrust-standards)
- [Cleary Gottlieb, "California's Antitrust Law Amendments" (Jan 2026)](https://www.clearygottlieb.com/news-and-insights/publication-listing/californias-antitrust-law-amendments-kick-in-targeting-algorithmic-pricing)
- [Morgan Lewis, "Algorithmic Pricing Antitrust Amendments" (Jan 2026)](https://www.morganlewis.com/pubs/2026/01/californias-algorithmic-pricing-antitrust-amendments-to-the-cartwright-act-take-effect)
- [Morgan Lewis, "California Clarifies Antitrust Pleading Standard" (Oct 2025)](https://www.morganlewis.com/pubs/2025/10/california-clarifies-antitrust-pleading-standard-creates-uncertainty-on-coercive-uses-of-algorithmic-software)
- [Pillsbury, "New California Laws Target Shared Pricing Algorithms"](https://www.pillsburylaw.com/en/news-and-insights/ab-325-shared-pricing-algorithms-liability-california.html)
- [Pillsbury, "Enforcement Landscape Heightens Risk"](https://www.pillsburylaw.com/en/news-and-insights/enforcement-landscape-heightened-risk-surveillance-pricing-california-federal-level.html)
- [WilmerHale, "California Zeroes in on Common Pricing Algorithms" (Nov 2025)](https://www.wilmerhale.com/en/insights/client-alerts/20251114-california-zeroes-in-on-common-pricing-algorithms)
- [Paul Weiss, "California Restricts Use of Common Pricing Algorithms"](https://www.paulweiss.com/insights/client-memos/california-restricts-use-of-common-pricing-algorithms)
- [Davis Polk, "New Laws Regulating Algorithmic Pricing" (2025)](https://www.davispolk.com/insights/client-update/new-laws-regulating-algorithmic-pricing-enacted-new-york-and-california)
- [Arnold & Porter, "Algorithmic Pricing Bans Go Coast to Coast" (Oct 2025)](https://www.arnoldporter.com/en/perspectives/advisories/2025/10/algorithmic-pricing-bans-go-coast-to-coast)
- [Vinson & Elkins, "California Boosts Antitrust Enforcement"](https://www.velaw.com/insights/california-boosts-antitrust-enforcement-with-two-new-laws/)
- [Vega Economics, "AB 325 — A Game-Changer" (2026)](https://vegaeconomics.com/california-ab-325-is-effective-january-1-2026-a-game-changer-for-algorithmic-pricing-litigation)
- [Jones Walker, "Algorithmic Pricing Risk" (2026)](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/algorithmic-pricing-risk-business-implications-from-californias-new-law-and-bey.html)
- [Troutman Pepper, "Is Individualized Pricing the Next Big Privacy Issue?" (Feb 2026)](https://www.troutmanprivacy.com/2026/02/is-individualized-pricing-the-next-big-privacy-enforcement-issue-california-ag-announces-investigative-sweep-around-surveillance-pricing-practices/)
- [Alston & Bird, "AG Announces Investigative Sweep" (Jan 2026)](https://www.alstonprivacy.com/california-attorney-general-announces-investigative-sweep-into-surveillance-pricing/)
- [Reed Smith, "California Launches Investigative Sweep"](https://www.reedsmith.com/articles/california-launches-investigative-sweep-on-surveillance-pricing-to-enforce-ccpa-compliance/)
- [Fenwick, "California AG Launches Investigative Sweep"](https://www.fenwick.com/insights/publications/california-ag-launches-investigative-sweep-on-surveillance-pricing-practices)
- [Wilson Sonsini, "DOJ Settles Against RealPage"](https://www.wsgr.com/en/insights/doj-settles-its-algorithmic-price-fixing-case-against-realpage.html)
- [Mintz, "Greystar Reaches Settlement" (Aug 2025)](https://www.mintz.com/insights-center/viewpoints/2025-08-13-no-day-today-greystar-reaches-settlement-agreement-department)
- [Consumer Reports, "AB 446 Fails to Advance" (2025)](https://advocacy.consumerreports.org/press_release/californias-surveillance-pricing-protection-act-ab-446-fails-to-advance-california-legislature/)
- [Consumer Watchdog, "Industry Disinformation Kills Surveillance Pricing Bill" (Sept 2025)](https://www.prnewswire.com/news-releases/industry-disinformation-kills-surveillance-pricing-bill-as-a-result-ab-446-is-withdrawn-says-consumer-watchdog-302548071.html)

**Library**:
- [[intel-comparative-regulation]]
- [[surveillance-pricing-comparative-regulation]]
- [[baldwin-regulatory-strategies]]
- [[competition-over-regulation]]
- [[disclosure-regulation]]
- [[regulatory-topology-not-ladder]]
- [[government-capacities-regulation]]
- [[market-power-precondition-algorithmic-harm]]
- [[sp-new-york]]
