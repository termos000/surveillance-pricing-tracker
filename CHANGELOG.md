# Changelog

## 2026-04-08: Editorial cleanup + redesign

**Editorial (Pass 1)**
- Swept `data.json` for AI-tell patterns: 54 fixes (40 em dashes, 7 superlatives, 7 restructured sentences)
- Cleaned `app.py` of hardcoded em dashes in captions and labels
- Zero hard-rule violations remain in structured data

**Editorial (Pass 2)**
- Voice pass on `analysis.md` and `data.json` text fields
- Applied style guide to key_finding, summary, design_logic_detail, political_economy_detail

**Visualization redesign**
- Color-coded strategy chips (Prohibition red, Disclosure blue, Competition orange, Rights purple, Code-as-Regulation cyan, Self-Regulation gray, Direct Action pink)
- Enriched grid cards: proprietary pricing fraction, political economy outcome pills, prominent key findings
- Sidebar cleanup: removed analysis subsection buttons, added Political Economy view
- Detail table: added PE Outcome and Private Right of Action columns
- Proprietary pricing gap chart (collapsible Altair horizontal stacked bar on grid view)
- Political Economy view: stacked bar by strategy + detail table with political narratives

**Infrastructure**
- Password protection via st.secrets
- Deployed to GitHub and Streamlit Community Cloud

## 2026-03-03: Initial build

- 15 jurisdictions, 142 instruments
- Structured JSON extracted from jurisdiction molecules
- Views: grid, detail, timeline, institution divergence, strategy x visibility, analysis
- Enrichment script for timeline, institution, political economy fields
- Dark theme, Altair timeline chart

---

# Roadmap

## Pending

- Substance review: check data.json against developments since March 3, verify analytical judgments
- Vault molecule sync: diff project copies against source molecules, update if needed

## Future

- Sector normalization (72 sectors don't form clean cross-jurisdiction taxonomy yet)
- Timeline view: add political economy outcome as color/shape layer
- Enforcement comparison view
- Mobile/responsive improvements for sharing
