import streamlit as st
import json
import re
import html as html_lib
import pandas as pd
import altair as alt
from pathlib import Path
from collections import Counter

st.set_page_config(
    page_title="Surveillance Pricing Tracker",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Landing + Auth ---

LANDING_BODY = """In 2024, the FTC defined the practice: firms using your personal data to set the price they think you'll pay. This dataset maps over 150 instruments across fifteen jurisdictions to find out what reaches it. The answer: almost everything regulators have built reaches the visible forms of algorithmic pricing, coordination, drip pricing, surge pricing. Almost nothing reaches surveillance pricing itself."""

def check_password():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if st.session_state.authenticated:
        return True
    st.markdown("""
    <style>
        .block-container { max-width: 560px !important; padding-top: 8rem !important; }
        /* Hide sidebar on landing page */
        section[data-testid="stSidebar"] { display: none !important; }
        [data-testid="collapsedControl"] { display: none !important; }
        /* Hide all Streamlit chrome on landing */
        header, [role="banner"] { display: none !important; }
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        [data-testid="stDeployButton"], .stDeployButton { display: none !important; }
        [data-testid="stToolbar"] { display: none !important; }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("# Surveillance Pricing Tracker")
    st.markdown("## How is the world trying to regulate surveillance pricing?")
    st.markdown(f"<p style='font-size:0.92rem; color:#57534e; line-height:1.7;'>{LANDING_BODY}</p>", unsafe_allow_html=True)
    pwd = st.text_input("Password", type="password", key="pwd_input", label_visibility="collapsed", placeholder="Password")
    if pwd:
        if pwd == st.secrets.get("password", ""):
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password")
    st.caption("Comparative regulation research, 2026")
    return False

if not check_password():
    st.stop()

# --- Data loading ---

@st.cache_data
def load_data():
    with open(Path(__file__).parent / "data.json", "r") as f:
        return json.load(f)

@st.cache_data
def load_molecule(filename):
    path = Path(__file__).parent / "molecules" / filename
    if not path.exists():
        path = Path.home() / "exocortex" / "library" / "molecules" / filename
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if text.startswith("---"):
            end = text.find("---", 3)
            if end != -1:
                text = text[end + 3:].strip()
        # Strip Key Data block
        text = re.sub(r'^## Key Data\s*\n.*?\n(?=\n)', '', text, flags=re.DOTALL | re.MULTILINE)
        # Strip wikilinks
        text = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', r'\2', text)
        text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
        # Strip "Jurisdiction molecule for..." line
        text = re.sub(r'\n\*Jurisdiction molecule for[^\n]*\n', '\n', text)
        # Strip em dashes
        text = text.replace(' — ', ', ')
        return text.strip()
    return None

data = load_data()

# --- Constants ---

STRATEGY_ORDER = [
    "Prohibition", "Competition", "Disclosure",
    "Rights & Liabilities", "Direct Action",
    "Self-Regulation", "Incentive-Based",
]

STRATEGY_COLORS = {
    "Prohibition": "#dc2626",
    "Disclosure": "#2563eb",
    "Competition": "#ea580c",
    "Rights & Liabilities": "#7c3aed",
    "Direct Action": "#db2777",
    "Code-as-Regulation": "#0891b2",
    "Self-Regulation": "#78716c",
    "Incentive-Based": "#059669",
}

STATUS_COLORS = {
    "Operative": "#166534",
    "Operative, unenforced": "#854d0e",
    "Enacted": "#1e40af",
    "Proposed": "#854d0e",
    "Failed": "#dc2626",
    "Paused": "#78716c",
    "Contested": "#dc2626",
    "Settled": "#166534",
    "Study": "#57534e",
}

PE_COLORS = {
    "Stalled": "#854d0e",
    "Blocked": "#dc2626",
    "Withdrawn": "#78716c",
    "Passed": "#166534",
    "Contested": "#dc2626",
    "Settled": "#166534",
}

DESIGN_LOGIC_COLORS = {
    "Unified": "#166534",
    "Differentiated": "#1e40af",
    "Accumulated": "#854d0e",
}

SPECIES_ORDER = [
    "Core Species", "Collusion", "Drip Pricing",
    "Surge Pricing", "Price Walking", "General",
]

# Display labels: schema value → audience-facing label
def display_species(s):
    return "Surveillance Pricing" if s == "Core Species" else (s or "")

# --- CSS (Light Theme) ---

st.markdown("""
<style>
    /* Light theme base */
    .stApp { background-color: #fafaf9; }
    .block-container { max-width: 1100px; padding-top: 1.5rem; }

    /* Typography */
    h1, h2, h3 { font-family: 'Georgia', 'Source Serif 4', serif !important; color: #1c1917 !important; }
    h1 { font-size: 1.5rem !important; font-weight: 700 !important; margin-bottom: 0.25rem !important; }
    h2 { font-size: 1.2rem !important; font-weight: 600 !important; }

    /* Hide ALL Streamlit chrome */
    #MainMenu { visibility: hidden !important; }
    header[data-testid="stHeader"],
    .stAppHeader,
    header:has(button),
    [role="banner"] {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        min-height: 0 !important;
        max-height: 0 !important;
        overflow: hidden !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    footer, .stAppFooter { visibility: hidden !important; }
    [data-testid="stDeployButton"],
    .stDeployButton,
    [data-testid="stToolbar"],
    .stToolbar,
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"] {
        display: none !important;
    }

    /* Sidebar - always visible, no collapse */
    section[data-testid="stSidebar"] {
        background: #fff;
        border-right: 1px solid #e7e5e4;
        min-width: 220px !important;
        width: 220px !important;
        transform: none !important;
    }
    section[data-testid="stSidebar"] button[kind="header"] {
        display: none;
    }
    [data-testid="collapsedControl"] {
        display: none;
    }
    section[data-testid="stSidebar"] .stButton button {
        text-align: left;
        width: 100%;
        border: none;
        background: transparent;
        padding: 6px 12px;
        font-size: 0.82rem;
        color: #57534e;
        border-radius: 4px;
    }
    section[data-testid="stSidebar"] .stButton button:hover {
        background: #f5f5f4;
    }

    /* Cards */
    [data-testid="stExpander"] {
        border: 1px solid #e7e5e4 !important;
        border-radius: 8px !important;
        background: #fff;
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        background: #fff;
        border: 1px solid #e7e5e4;
        border-radius: 8px;
        padding: 12px 16px;
    }
    [data-testid="stMetricValue"] { color: #1c1917 !important; }
    [data-testid="stMetricLabel"] {
        color: #a8a29e !important;
        text-transform: uppercase;
        font-size: 0.72rem !important;
        letter-spacing: 0.05em;
    }

    /* Strategy chips */
    .chip {
        font-size: 0.7rem;
        padding: 2px 8px;
        border-radius: 3px;
        display: inline-block;
        margin: 1px;
        font-weight: 500;
    }

    /* Status pills */
    .pill {
        font-size: 0.72rem;
        padding: 2px 8px;
        border-radius: 10px;
        font-weight: 500;
        display: inline-block;
    }

    /* Tables */
    .inst-table { width: 100%; border-collapse: collapse; font-size: 0.82rem; margin: 1rem 0; }
    .inst-table th {
        text-align: left;
        padding: 10px 12px;
        border-bottom: 2px solid #e7e5e4;
        color: #a8a29e;
        font-weight: 500;
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .inst-table td {
        padding: 10px 12px;
        border-bottom: 1px solid #f5f5f4;
        color: #44403c;
        vertical-align: top;
    }
    .inst-table tr:hover td { background: #fafaf9; }
    .inst-name { font-weight: 500; color: #1c1917; }
    .inst-summary { font-size: 0.75rem; color: #a8a29e; margin-top: 2px; }

    /* Core callout */
    .core-callout {
        background: #fef2f2;
        border: 1px solid #fecaca;
        border-radius: 8px;
        padding: 14px 20px;
        margin-bottom: 20px;
        font-size: 0.88rem;
        color: #991b1b;
    }

    /* Section labels */
    .section-label {
        font-size: 0.68rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #a8a29e;
        font-weight: 600;
        margin-bottom: 4px;
    }

    /* Tooltip style */
    .has-tip {
        border-bottom: 1px dotted #a8a29e;
        cursor: help;
    }
</style>
""", unsafe_allow_html=True)


# --- Tooltip copy (from Kim) ---

STRATEGY_TIPS = {
    "Prohibition": "The state bans the practice and attaches penalties.",
    "Competition": "The state breaks coordination or constrains market power. Requires agreement or dominance.",
    "Disclosure": "The state requires the firm to inform the consumer or regulator.",
    "Rights & Liabilities": "The state confers a right on the individual to object, opt out, or receive an explanation.",
    "Direct Action": "The state intervenes directly: price caps, software mandates, algorithmic audits.",
    "Self-Regulation": "Industry designs its own voluntary governance. No independent enforcement.",
    "Incentive-Based": "Financial incentives to shape firm behavior. Zero instances in the dataset.",
}

STATUS_TIPS = {
    "Operative": "In force, with at least one enforcement action on algorithmic pricing.",
    "Operative, unenforced": "In force, zero enforcement on algorithmic pricing in any jurisdiction.",
    "Enacted": "Passed into law, not yet in force.",
    "Proposed": "Bill introduced or regulation drafted, not enacted.",
    "Failed": "Introduced and died (withdrawn, voted down, or inactive).",
    "Paused": "Previously active, now suspended. Could resume.",
    "Contested": "Operative, but under active legal challenge.",
    "Settled": "Resolved through consent decree or settlement.",
    "Study": "Formal investigation or consultation, no binding obligations.",
}

SPECIES_TIPS = {
    "Surveillance Pricing": "Unilateral, proprietary, individual-level pricing using behavioral data. The practice the dataset tracks.",
    "Core Species": "Unilateral, proprietary, individual-level pricing using behavioral data. The practice the dataset tracks.",
    "Collusion": "Coordinated pricing through a shared algorithm or intermediary. Reachable by competition law.",
    "Drip Pricing": "Mandatory fees revealed incrementally during checkout. Visible in the interface.",
    "Surge Pricing": "Real-time price spikes in response to demand. Observable to multiple consumers.",
    "Price Walking": "Raising prices for renewing customers relative to new ones. Sector-specific.",
    "General": "Addresses algorithmic pricing broadly without targeting a specific species.",
}

PE_TIPS = {
    "Passed": "Enacted. Industry opposition insufficient or absent.",
    "Blocked": "Actively defeated by organized opposition.",
    "Stalled": "Not advancing, not formally defeated. Sitting in committee or delayed indefinitely.",
    "Withdrawn": "Sponsor voluntarily pulled the instrument.",
    "Contested": "Under legal challenge after enactment.",
    "Settled": "Resolved through consent decree or settlement agreement.",
}

# --- Helpers ---

def esc(text):
    return html_lib.escape(str(text)) if text else ""

def strategy_chip(name):
    color = STRATEGY_COLORS.get(name, "#78716c")
    bg = f"{color}25"
    tip = esc(STRATEGY_TIPS.get(name, ""))
    return f'<span class="chip" title="{tip}" style="color:{color}; background:{bg}; border:1px solid {color}30;">{esc(name)}</span>'

def status_pill(status):
    color = STATUS_COLORS.get(status, "#78716c")
    bg = f"{color}25"
    tip = esc(STATUS_TIPS.get(status, ""))
    return f'<span class="pill" title="{tip}" style="color:{color}; background:{bg};">{esc(status)}</span>'

def pe_pill(outcome):
    color = PE_COLORS.get(outcome, "#78716c")
    bg = f"{color}25"
    tip = esc(PE_TIPS.get(outcome, ""))
    return f'<span class="pill" title="{tip}" style="color:{color}; background:{bg};">{esc(outcome)}</span>'

def design_badge(logic):
    color = DESIGN_LOGIC_COLORS.get(logic, "#78716c")
    bg = f"{color}25"
    return f'<span class="chip" style="color:{color}; background:{bg}; border:1px solid {color}30;">{esc(logic)}</span>'


# --- State ---

if "page" not in st.session_state:
    st.session_state.page = "species"  # default: "Does it reach surveillance pricing?"
if "jurisdiction_id" not in st.session_state:
    st.session_state.jurisdiction_id = None


# --- Sidebar ---

with st.sidebar:
    st.markdown('<div class="section-label">Views</div>', unsafe_allow_html=True)

    views = [
        ("Does it reach surveillance pricing?", "species"),
        ("What have regulators built?", "landscape"),
        ("How did each jurisdiction get here?", "jurisdictions"),
        ("What keeps failing?", "political_economy"),
        ("What does the pattern show?", "analysis"),
        ("How was this built?", "methodology"),
    ]

    for label, key in views:
        if st.button(label, key=f"nav_{key}", use_container_width=True):
            st.session_state.page = key
            st.session_state.jurisdiction_id = None
            st.rerun()

    st.markdown("---")
    st.markdown('<div class="section-label">Jurisdictions</div>', unsafe_allow_html=True)

    for j in data["jurisdictions"]:
        if st.button(j["name"], key=f"nav_j_{j['id']}", use_container_width=True):
            st.session_state.page = "detail"
            st.session_state.jurisdiction_id = j["id"]
            st.rerun()


# ============================================================
# VIEW 1: Does it reach surveillance pricing? (Target Species)
# ============================================================

def render_species():
    st.markdown("## Does it reach surveillance pricing?")
    st.markdown("<p style='color:#57534e; font-size:0.88rem;'>Each row is a species of algorithmic pricing. Each column is a regulatory strategy. The bottom row is surveillance pricing. Filter to see what reaches it.</p>", unsafe_allow_html=True)

    # Scaffolding: "Reading the dataset"
    with st.expander("Reading the dataset", expanded=False):
        st.markdown("**The practice.** Surveillance pricing is when a firm uses your personal data to set the price it thinks you'll pay. The term comes from the FTC's 2024 study. It is one species within a broader genus of algorithmic pricing that includes collusion (firms coordinating through shared algorithms), drip pricing (fees added during checkout), surge pricing (demand-driven spikes), and price walking (raising prices on loyal customers). Each species has different structural characteristics. Each is reachable by different regulatory instruments. Surveillance pricing is the species that almost nothing reaches.")
        st.markdown("**The framework.** This dataset organizes regulatory instruments by what they do, not where they sit. Seven strategies, adapted from Baldwin, Cave, and Lodge (2012): Prohibition, Competition, Disclosure, Rights and Liabilities, Direct Action, Self-Regulation, and Incentive-Based. Each column in the heatmap is one strategy. Each row is one species. The pattern shows where the instruments cluster and where they don't.")
        st.markdown("**The key question.** \"Reaches surveillance pricing\" is the filter that reveals the gap. An instrument is marked Yes if its legal text covers unilateral personalized pricing using proprietary behavioral data. Many instruments formally cover the practice. Almost none produce enforcement. The Status column tells you the difference: \"Operative\" means enforced; \"Operative, unenforced\" means it exists in law and has never been applied. That distinction is the dataset's central finding.")

    # Build species x strategy matrix
    all_instruments = [(j, i) for j in data["jurisdictions"] for i in j["instruments"]]
    total = len(all_instruments)
    reaches = sum(1 for _, i in all_instruments if i.get("reaches_core"))
    gap = total - reaches

    # Core callout
    st.markdown(f'<div class="core-callout"><strong>{reaches} of {total}</strong> instruments reach surveillance pricing. The rest ({gap}) target coordination, drip pricing, surge pricing, or general consumer protection.</div>', unsafe_allow_html=True)

    # Matrix: species (rows) x strategy (columns)
    species_list = SPECIES_ORDER
    strategy_list = [s for s in STRATEGY_ORDER if any(i.get("strategy") == s for _, i in all_instruments)]

    matrix_data = []
    for sp in species_list:
        for st_name in strategy_list:
            count = sum(1 for _, i in all_instruments
                       if i.get("target_species") == sp and i.get("strategy") == st_name)
            matrix_data.append({"Species": display_species(sp), "Strategy": st_name, "count": count})

    df = pd.DataFrame(matrix_data)

    chart = alt.Chart(df).mark_rect().encode(
        x=alt.X("Strategy:N", sort=strategy_list, title=None,
                axis=alt.Axis(labelAngle=-45, labelFontSize=11)),
        y=alt.Y("Species:N", sort=[display_species(s) for s in species_list], title=None,
                axis=alt.Axis(labelFontSize=11)),
        color=alt.condition(
            alt.datum.count > 0,
            alt.Color("count:Q",
                      scale=alt.Scale(scheme="orangered", domain=[0, 20]),
                      legend=alt.Legend(title="Instruments")),
            alt.value("#f5f5f4")
        ),
        tooltip=["Species:N", "Strategy:N", "count:Q"],
    ).properties(height=300).configure_axis(
        grid=False,
    ).configure_view(
        strokeWidth=0,
    )

    st.altair_chart(chart, use_container_width=True)

    # Reaches surveillance pricing filter
    st.markdown("### Instruments that reach surveillance pricing")
    reaches_instruments = [(j, i) for j, i in all_instruments if i.get("reaches_core")]
    if reaches_instruments:
        table_html = '<table class="inst-table"><thead><tr><th>Jurisdiction</th><th>Instrument</th><th><span class="has-tip" title="Baldwin regulatory strategy">Strategy</span></th><th><span class="has-tip" title="Current state of the instrument">Status</span></th><th><span class="has-tip" title="The specific pricing practice this instrument was designed to reach">Species</span></th></tr></thead><tbody>'
        for j, i in reaches_instruments:
            table_html += f'<tr><td style="font-size:0.82rem;">{esc(j["name"])}</td><td><span class="inst-name">{esc(i["name"])}</span></td><td>{strategy_chip(i["strategy"])}</td><td>{status_pill(i["status"])}</td><td style="font-size:0.78rem;">{esc(display_species(i.get("target_species","")))}</td></tr>'
        table_html += '</tbody></table>'
        st.markdown(table_html, unsafe_allow_html=True)
    else:
        st.info("No instruments with 'Reaches Core' data yet. Molecules still being updated.")


# ============================================================
# VIEW 2: What have regulators built? (Landscape)
# ============================================================

def render_landscape():
    st.markdown("## What have regulators built?")
    st.markdown("<p style='color:#57534e; font-size:0.88rem;'>Fifteen jurisdictions, seven regulatory strategies. Every cell shows instrument count by status.</p>", unsafe_allow_html=True)

    all_instruments = [(j, i) for j in data["jurisdictions"] for i in j["instruments"]]

    # Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Jurisdictions", len(data["jurisdictions"]))
    m2.metric("Instruments", len(all_instruments))
    operative = sum(1 for _, i in all_instruments if i["status"].startswith("Operative"))
    m3.metric("Operative", operative)
    reaches = sum(1 for _, i in all_instruments if i.get("reaches_core"))
    m4.metric("Reaches SP", reaches)

    # Jurisdiction x Strategy heatmap
    rows = []
    for j in data["jurisdictions"]:
        for i in j["instruments"]:
            rows.append({
                "Jurisdiction": j["name"],
                "Strategy": i["strategy"],
                "Status": i["status"],
            })
    df = pd.DataFrame(rows)

    if not df.empty:
        count_df = df.groupby(["Jurisdiction", "Strategy"]).size().reset_index(name="count")
        j_order = [j["name"] for j in data["jurisdictions"]]
        s_order = [s for s in STRATEGY_ORDER if s in df["Strategy"].unique()]

        chart = alt.Chart(count_df).mark_rect().encode(
            x=alt.X("Strategy:N", sort=s_order, title=None,
                    axis=alt.Axis(labelAngle=-45, labelFontSize=11)),
            y=alt.Y("Jurisdiction:N", sort=j_order, title=None,
                    axis=alt.Axis(labelFontSize=11)),
            color=alt.Color("count:Q",
                           scale=alt.Scale(scheme="blues", domain=[0, 12]),
                           legend=alt.Legend(title="Instruments")),
            tooltip=["Jurisdiction:N", "Strategy:N", "count:Q"],
        ).properties(height=450).configure_axis(
            grid=False,
        ).configure_view(
            strokeWidth=0,
        )

        st.altair_chart(chart, use_container_width=True)


# ============================================================
# VIEW 3: How did each jurisdiction get here? (Cards)
# ============================================================

def render_jurisdictions():
    st.markdown("## How did each jurisdiction get here?")
    st.markdown("<p style='color:#57534e; font-size:0.88rem;'>Jurisdiction cards. Key finding, instrument count, strategy mix.</p>", unsafe_allow_html=True)

    # Filters
    f1, f2, f3 = st.columns(3)
    with f1:
        filter_logic = st.multiselect("Design Logic", ["Unified", "Differentiated", "Accumulated"], default=[], placeholder="All")
    with f2:
        filter_region = st.multiselect("Region", sorted(set(j.get("region", "Other") for j in data["jurisdictions"])), default=[], placeholder="All")
    with f3:
        filter_core = st.selectbox("Reaches surveillance pricing", ["All", "Has instruments that reach", "None reach"], index=0)

    jurisdictions = data["jurisdictions"]
    if filter_logic:
        jurisdictions = [j for j in jurisdictions if j.get("design_logic") in filter_logic]
    if filter_region:
        jurisdictions = [j for j in jurisdictions if j.get("region") in filter_region]
    if filter_core == "Has instruments that reach":
        jurisdictions = [j for j in jurisdictions if j.get("reaches_core_count", 0) > 0]
    elif filter_core == "None reach":
        jurisdictions = [j for j in jurisdictions if j.get("reaches_core_count", 0) == 0]

    COLS = 3
    def render_card(j):
        with st.container(border=True):
            st.markdown(f"**{esc(j['name'])}** {design_badge(j.get('design_logic',''))}", unsafe_allow_html=True)

            finding = j.get("key_finding", "")
            if finding:
                st.markdown(f"*{esc(finding)}*")

            # Stats line
            inst_count = j.get("instrument_count", 0)
            op_count = j.get("operative_count", 0)
            st.caption(f"{inst_count} instruments, {op_count} operative")

            # Reaches core
            rc = j.get("reaches_core_count", 0)
            rc_color = "#16a34a" if rc > 0 else "#dc2626"
            pe_counts = Counter(i.get("pe_outcome") for i in j.get("instruments", []) if i.get("pe_outcome"))
            pe_html = " ".join(f'{pe_pill(k)}&nbsp;{v}' for k, v in pe_counts.items()) if pe_counts else ""
            st.markdown(
                f'<span style="color:{rc_color}; font-size:0.78rem; font-weight:500;">{rc}/{inst_count} reach surveillance pricing</span>'
                + (f" &nbsp;{pe_html}" if pe_html else ""),
                unsafe_allow_html=True,
            )

            # Strategy chips
            strategies = sorted(set(i["strategy"] for i in j.get("instruments", []) if i.get("strategy")))
            chips = " ".join(strategy_chip(s) for s in strategies)
            st.markdown(chips, unsafe_allow_html=True)

            if st.button("View detail", key=f"btn_{j['id']}"):
                st.session_state.page = "detail"
                st.session_state.jurisdiction_id = j["id"]
                st.rerun()

    rows_data = [jurisdictions[i:i+COLS] for i in range(0, len(jurisdictions), COLS)]
    for row in rows_data:
        cols = st.columns(COLS)
        for idx, j in enumerate(row):
            with cols[idx]:
                render_card(j)


# ============================================================
# VIEW 4: What keeps failing? (Political Economy)
# ============================================================

def render_political_economy():
    st.markdown("## What keeps failing?")
    st.markdown("<p style='color:#57534e; font-size:0.88rem;'>Political economy. Which instruments passed, stalled, were blocked, or are contested. Where industry opposition shapes what survives.</p>", unsafe_allow_html=True)

    rows = []
    for j in data["jurisdictions"]:
        for inst in j["instruments"]:
            pe = inst.get("pe_outcome")
            if pe:
                rows.append({
                    "jurisdiction": j["name"],
                    "strategy": inst["strategy"],
                    "instrument": inst["name"],
                    "outcome": pe,
                    "status": inst["status"],
                    "target_species": inst.get("target_species", ""),
                    "reaches_core": inst.get("reaches_core", False),
                })

    if not rows:
        st.info("No political economy data available yet.")
        return

    df = pd.DataFrame(rows)

    m1, m2, m3 = st.columns(3)
    m1.metric("Instruments with PE outcome", len(df))
    m2.metric("Stalled or Blocked", len(df[df["outcome"].isin(["Stalled", "Blocked"])]))
    m3.metric("Contested", len(df[df["outcome"] == "Contested"]))

    pe_domain = [k for k in PE_COLORS.keys() if k in df["outcome"].values]
    pe_range = [PE_COLORS[k] for k in pe_domain]

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("strategy:N", sort=STRATEGY_ORDER, title=None),
        y=alt.Y("count():Q", title="Instruments"),
        color=alt.Color("outcome:N",
            scale=alt.Scale(domain=pe_domain, range=pe_range),
            legend=alt.Legend(title="Outcome", orient="top")),
        tooltip=["strategy:N", "outcome:N", "count():Q"],
    ).properties(height=300)

    st.altair_chart(chart, use_container_width=True)

    # Table
    st.markdown("### Detail")
    table_html = '<table class="inst-table"><thead><tr><th>Jurisdiction</th><th style="width:30%;">Instrument</th><th><span class="has-tip" title="Baldwin regulatory strategy">Strategy</span></th><th><span class="has-tip" title="Political economy fate">Outcome</span></th><th style="text-align:center;"><span class="has-tip" title="Individual-level pricing set unilaterally using proprietary data">Reaches SP</span></th></tr></thead><tbody>'
    for _, r in df.iterrows():
        core_icon = '<span style="color:#16a34a; font-weight:600;">&#10003;</span>' if r["reaches_core"] else '<span style="color:#d6d3d1;">-</span>'
        table_html += f'<tr><td style="font-size:0.82rem;">{esc(r["jurisdiction"])}</td><td style="font-size:0.82rem;">{esc(r["instrument"][:60])}</td><td>{strategy_chip(r["strategy"])}</td><td>{pe_pill(r["outcome"])}</td><td style="text-align:center;">{core_icon}</td></tr>'
    table_html += '</tbody></table>'
    st.markdown(table_html, unsafe_allow_html=True)


# ============================================================
# VIEW 5: What does the pattern show? (Analysis)
# ============================================================

def render_analysis():
    st.markdown("## What does the pattern show?")
    st.markdown("<p style='color:#57534e; font-size:0.88rem;'>Four findings from reading across fifteen jurisdictions.</p>", unsafe_allow_html=True)

    findings = [
        ("Surveillance pricing is unreached.",
         "Enforcement actions in the dataset reach collusion, drip pricing, surge pricing, and price walking. All involve practices whose structural characteristics match what the instruments were designed to detect. No jurisdiction in the dataset has an operative instrument that has been enforced against surveillance pricing. Fifteen out of fifteen."),
        ("Formal coverage produces no enforcement.",
         "A small number of instruments do address the right practice. GDPR Article 22 has been operative since 2018. The Omnibus Directive's disclosure obligation since 2022. New York's A6765 since November 2025. None has produced enforcement on personalized pricing. The structural characteristics explain why: the consumer does not know the right has been triggered, and the regulator cannot observe the practice from outside."),
        ("Enforcement follows the instrument's original design.",
         "Each institution enforces what its instrument was designed for. Competition authorities find coordination. Consumer protection finds deception visible in the interface. Sector regulators find practices that are already politically salient. The instruments carry the institutional fingerprint of the problems they were originally built to solve."),
        ("The enforcing institution was solving a different problem.",
         "In fourteen of fifteen jurisdictions, the institution that actually enforces diverges from what the regulatory strategy theoretically implies. Competition authorities have become the de facto enforcers because they had the tools for a related problem. The instruments were designed for adjacent practices and stretched toward surveillance pricing. The stretch does not reach."),
    ]

    for title, body in findings:
        with st.expander(title):
            st.markdown(body)


# ============================================================
# VIEW 6: How was this built? (Methodology)
# ============================================================

def render_methodology():
    st.markdown("## How was this built?")
    st.markdown("<p style='color:#57534e; font-size:0.88rem;'>Methodology, scope, and boundaries.</p>", unsafe_allow_html=True)

    with st.expander("What's in the dataset"):
        st.markdown("Over 150 regulatory instruments across fifteen jurisdictions, identified through a three-pass process: legal databases and secondary literature to compile candidates, primary-source verification against the statute or enforcement filing itself, and a cross-check against recent enforcement records and practitioner analyses. Each instrument is coded along nine dimensions: regulatory strategy, sub-type, sector, status, enforcement mechanism, target species, whether it reaches surveillance pricing, and political economy outcome. The jurisdictions span North America (US Federal, New York, California, US States composite, Canada), Europe (EU, UK, Germany, Netherlands), and Asia-Pacific (China, South Korea, Singapore, Australia, India, Indonesia).")

    with st.expander("How it's organized"):
        st.markdown("The dataset uses a seven-position topology adapted from Baldwin, Cave, and Lodge's taxonomy of regulatory strategies (*Understanding Regulation*, 2d ed. 2012): Prohibition, Competition, Disclosure, Rights and Liabilities, Direct Action, Self-Regulation, and Incentive-Based. Each position describes a different relationship between the state, the firm, and the consumer. The topology maps strategies as positions, not as steps on a ladder. One-way escalation from disclosure to prohibition holds only for China. Every other jurisdiction moves laterally, gets blocked, or accumulates instruments without escalating.")

    with st.expander("What's not included"):
        st.markdown("Japan, Brazil, Israel, and the Global South are absent. Selection was based on the presence of active regulatory responses in 2024-2026 and primary-source accessibility. The paper names this boundary rather than claiming comprehensiveness. The dataset is weighted toward jurisdictions with English-language or translated primary sources, supplemented by jurisdiction-specific academic literature for China, South Korea, and Indonesia.")


# ============================================================
# DETAIL VIEW
# ============================================================

def render_detail(jurisdiction_id):
    jurisdiction = next((j for j in data["jurisdictions"] if j["id"] == jurisdiction_id), None)
    if not jurisdiction:
        st.error(f"Jurisdiction not found: {jurisdiction_id}")
        return

    # Header
    st.markdown(
        f"## {esc(jurisdiction['name'])} {design_badge(jurisdiction.get('design_logic',''))}",
        unsafe_allow_html=True,
    )

    finding = jurisdiction.get("key_finding", "")
    if finding:
        st.markdown(f"*{esc(finding)}*")

    # Metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Instruments", jurisdiction.get("instrument_count", 0))
    rc = jurisdiction.get("reaches_core_count", 0)
    total = jurisdiction.get("instrument_count", 0)
    c2.metric("Reaches SP", f"{rc}/{total}")
    c3.metric("Year range", f"{jurisdiction.get('year_first', '?')}-{jurisdiction.get('year_latest', '?')}")
    c4.metric("Design logic", jurisdiction.get("design_logic", ""))

    # Instrument table
    st.markdown("### Instruments")
    instruments = jurisdiction.get("instruments", [])

    table_html = '''<table class="inst-table">
    <thead><tr>
        <th style="width:24%;">Instrument</th>
        <th>Strategy</th>
        <th>Status</th>
        <th><span class="has-tip" title="The specific pricing practice this instrument was designed to reach">Species</span></th>
        <th style="text-align:center;"><span class="has-tip" title="Individual-level pricing set unilaterally using proprietary data">Reaches SP</span></th>
        <th>PE Outcome</th>
    </tr></thead><tbody>'''

    for inst in instruments:
        core_icon = '<span style="color:#16a34a; font-weight:600;">&#10003;</span>' if inst.get("reaches_core") else '<span style="color:#d6d3d1;">-</span>'
        pe = pe_pill(inst["pe_outcome"]) if inst.get("pe_outcome") else ""
        species = esc(display_species(inst.get("target_species", "")))

        table_html += f'''<tr>
            <td><span class="inst-name">{esc(inst["name"])}</span></td>
            <td>{strategy_chip(inst["strategy"])}</td>
            <td>{status_pill(inst["status"])}</td>
            <td style="font-size:0.78rem;">{species}</td>
            <td style="text-align:center;">{core_icon}</td>
            <td>{pe}</td>
        </tr>'''

    table_html += '</tbody></table>'
    st.markdown(table_html, unsafe_allow_html=True)

    # Timeline
    has_timeline = any(inst.get("timeline") for inst in instruments)
    if has_timeline:
        with st.expander("Timelines"):
            for inst in instruments:
                if inst.get("timeline"):
                    st.markdown(f"**{inst['name']}**")
                    for event in inst["timeline"]:
                        st.markdown(f"- `{event['date']}` {event['event']}")
                    st.markdown("")

    # Full molecule profile (collapsible sections)
    st.markdown("---")
    molecule = load_molecule(jurisdiction.get("molecule_file", ""))
    if molecule:
        # Remove title (already shown above)
        molecule = re.sub(r'^# .+\n', '', molecule).strip()
        # Remove ## Instruments section (already shown in table)
        molecule = re.sub(r'^## Instruments\n.*?(?=\n## |\Z)', '', molecule, flags=re.DOTALL | re.MULTILINE).strip()

        # Split by ## headings into collapsible expanders
        sections = re.split(r'^(## .+)$', molecule, flags=re.MULTILINE)
        intro = sections[0].strip()
        if intro:
            st.markdown(intro)

        for i in range(1, len(sections), 2):
            heading = sections[i].replace("## ", "").strip()
            body = sections[i+1].strip() if i+1 < len(sections) else ""
            if heading.lower() in ("open questions", "library"):
                continue
            with st.expander(heading):
                st.markdown(body)


# ============================================================
# ROUTING
# ============================================================

page = st.session_state.page

if page == "detail" and st.session_state.jurisdiction_id:
    render_detail(st.session_state.jurisdiction_id)
elif page == "species":
    render_species()
elif page == "landscape":
    render_landscape()
elif page == "jurisdictions":
    render_jurisdictions()
elif page == "political_economy":
    render_political_economy()
elif page == "analysis":
    render_analysis()
elif page == "methodology":
    render_methodology()
else:
    render_species()
