import streamlit as st
import json
import re
import html as html_lib
import pandas as pd
import altair as alt
from pathlib import Path
from collections import Counter

st.set_page_config(
    page_title="Surveillance Pricing Jurisdiction Tracker",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Auth ---

def check_password():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if st.session_state.authenticated:
        return True
    pwd = st.text_input("Password", type="password", key="pwd_input")
    if pwd:
        if pwd == st.secrets.get("password", ""):
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password")
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
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if text.startswith("---"):
            end = text.find("---", 3)
            if end != -1:
                text = text[end + 3:].strip()
        text = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', r'\2', text)
        text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
        return text
    return None

@st.cache_data
def load_analysis():
    path = Path(__file__).parent / "analysis.md"
    if path.exists():
        text = path.read_text(encoding="utf-8")
        text = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', r'\2', text)
        text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
        return text
    return None

@st.cache_data
def parse_analysis_sections():
    """Parse analysis.md into navigable sections."""
    text = load_analysis()
    if not text:
        return []

    sections = []
    current_h2 = None
    current_h2_body = ""

    for line in text.split("\n"):
        if line.startswith("## "):
            if current_h2:
                sections.append({"level": "h2", "title": current_h2, "body": current_h2_body.strip()})
            current_h2 = line[3:].strip()
            current_h2_body = ""
        elif line.startswith("### "):
            if current_h2_body.strip():
                # flush any h2 intro text before the first h3
                pass
            current_h2_body += line + "\n"
        else:
            current_h2_body += line + "\n"

    if current_h2:
        sections.append({"level": "h2", "title": current_h2, "body": current_h2_body.strip()})

    # Now split each h2 section into h3 subsections
    result = []
    for sec in sections:
        h3_parts = re.split(r'^### ', sec["body"], flags=re.MULTILINE)
        # First part is intro text (before any ###)
        intro = h3_parts[0].strip()
        subsections = []
        for part in h3_parts[1:]:
            lines = part.split("\n", 1)
            title = lines[0].strip()
            body = lines[1].strip() if len(lines) > 1 else ""
            subsections.append({"title": title, "body": body})

        result.append({
            "title": sec["title"],
            "intro": intro,
            "subsections": subsections,
        })

    return result


data = load_data()

# --- Constants ---

STATUS_COLORS = {
    "Operative": "#22c55e",
    "Enacted": "#3b82f6",
    "Proposed": "#eab308",
    "Failed": "#ef4444",
    "Paused": "#6b7280",
    "Active Investigation": "#a855f7",
}

DESIGN_LOGIC_COLORS = {
    "Unified": "#22c55e",
    "Differentiated": "#3b82f6",
    "Accumulated": "#eab308",
}

STRATEGY_ORDER = [
    "Prohibition", "Disclosure", "Competition",
    "Rights & Liabilities", "Code-as-Regulation",
    "Self-Regulation", "Direct Action",
]

STRATEGY_COLORS = {
    "Prohibition": "#ef4444",
    "Disclosure": "#3b82f6",
    "Competition": "#f97316",
    "Rights & Liabilities": "#8b5cf6",
    "Code-as-Regulation": "#06b6d4",
    "Self-Regulation": "#6b7280",
    "Direct Action": "#ec4899",
}

PE_COLORS = {
    "Stalled": "#eab308",
    "Blocked": "#ef4444",
    "Withdrawn": "#6b7280",
    "Passed": "#22c55e",
}

# --- CSS ---

st.markdown("""
<style>
    .block-container { max-width: 1200px; padding-top: 2rem; }
    h1 { font-size: 1.75rem !important; font-weight: 600 !important; margin-bottom: 0.25rem !important; }
    .card-badge {
        font-size: 0.72rem;
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: 500;
    }
    .strategy-chip {
        font-size: 0.7rem;
        padding: 2px 7px;
        border-radius: 3px;
        display: inline-block;
        margin: 1px;
        font-weight: 500;
    }
    .status-pill {
        font-size: 0.72rem;
        padding: 2px 8px;
        border-radius: 10px;
        font-weight: 500;
        display: inline-block;
    }
    .inst-table { width: 100%; border-collapse: collapse; font-size: 0.85rem; margin: 1rem 0; }
    .inst-table th {
        text-align: left;
        padding: 0.6rem 0.75rem;
        border-bottom: 2px solid #2a2a3a;
        color: #6b7280;
        font-weight: 500;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .inst-table td {
        padding: 0.6rem 0.75rem;
        border-bottom: 1px solid #1a1a2a;
        color: #d1d5db;
        vertical-align: top;
    }
    .inst-table tr:hover td { background: rgba(255,255,255,0.02); }
    .inst-name { font-weight: 500; color: #fafafa; }
    .inst-summary { font-size: 0.78rem; color: #9ca3af; margin-top: 2px; }
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        padding-top: 1rem;
    }
    section[data-testid="stSidebar"] .stButton button {
        text-align: left;
        width: 100%;
        border: none;
        background: transparent;
        padding: 0.3rem 0.75rem;
        font-size: 0.85rem;
    }
    section[data-testid="stSidebar"] .stButton button:hover {
        background: rgba(255,255,255,0.05);
    }
    section[data-testid="stSidebar"] .stMarkdown {
        padding-left: 0.25rem;
    }
    section[data-testid="stSidebar"] h3 {
        font-size: 0.9rem !important;
        padding-left: 0.25rem;
        margin-bottom: 0.25rem !important;
    }
</style>
""", unsafe_allow_html=True)


# --- Helpers ---

def esc(text):
    return html_lib.escape(str(text))

def design_logic_badge(logic):
    color = DESIGN_LOGIC_COLORS.get(logic, "#6b7280")
    bg = f"{color}20"
    return f'<span class="card-badge" style="color:{color}; background:{bg};">{esc(logic)}</span>'

def status_pill(status):
    color = STATUS_COLORS.get(status, "#6b7280")
    bg = f"{color}20"
    return f'<span class="status-pill" style="color:{color}; background:{bg};">{esc(status)}</span>'

def status_dot(status):
    color = STATUS_COLORS.get(status, "#6b7280")
    return f'<span style="color:{color};">●</span>'

def strategy_chip(name):
    color = STRATEGY_COLORS.get(name, "#6b7280")
    bg = f"{color}20"
    return f'<span class="strategy-chip" style="color:{color}; background:{bg}; border:1px solid {color}40;">{esc(name)}</span>'

def pe_pill(outcome):
    color = PE_COLORS.get(outcome, "#6b7280")
    bg = f"{color}20"
    return f'<span class="status-pill" style="color:{color}; background:{bg};">{esc(outcome)}</span>'


# --- State ---

if "page" not in st.session_state:
    st.session_state.page = "grid"
if "jurisdiction_id" not in st.session_state:
    st.session_state.jurisdiction_id = None
if "analysis_section" not in st.session_state:
    st.session_state.analysis_section = None


# --- Sidebar Navigation ---

with st.sidebar:
    st.markdown("### Navigation")

    # Overview
    if st.button("All Jurisdictions", key="nav_grid", use_container_width=True):
        st.session_state.page = "grid"
        st.session_state.jurisdiction_id = None
        st.rerun()

    # New views
    st.markdown("**Views**")
    if st.button("Timeline", key="nav_timeline", use_container_width=True):
        st.session_state.page = "timeline"
        st.rerun()
    if st.button("Institution Divergence", key="nav_divergence", use_container_width=True):
        st.session_state.page = "divergence"
        st.rerun()
    if st.button("Strategy × Visibility", key="nav_matrix", use_container_width=True):
        st.session_state.page = "matrix"
        st.rerun()
    if st.button("Political Economy", key="nav_pe", use_container_width=True):
        st.session_state.page = "political_economy"
        st.rerun()

    st.markdown("---")

    # Jurisdictions list
    st.markdown("**Jurisdictions**")
    for j in data["jurisdictions"]:
        label = j["name"]
        if st.button(label, key=f"nav_j_{j['id']}", use_container_width=True):
            st.session_state.page = "detail"
            st.session_state.jurisdiction_id = j["id"]
            st.rerun()

    st.markdown("---")

    # Analysis sections (H2 only, subsections navigable via tabs inside)
    st.markdown("**Analysis**")
    analysis_sections = parse_analysis_sections()
    for sec in analysis_sections:
        if st.button(sec["title"].split("(")[0].strip(), key=f"nav_a_{sec['title'][:20]}", use_container_width=True):
            st.session_state.page = "analysis"
            st.session_state.analysis_section = sec["title"]
            st.rerun()

    st.markdown("---")
    # attribution removed


# --- URL param handling ---

params = st.query_params
if "jurisdiction" in params:
    jid = params["jurisdiction"]
    if any(j["id"] == jid for j in data["jurisdictions"]):
        st.session_state.page = "detail"
        st.session_state.jurisdiction_id = jid


# ============================================================
# GRID VIEW
# ============================================================

def render_grid():
    st.title("Surveillance Pricing Jurisdiction Tracker")
    st.caption("Comparative regulation across 15 jurisdictions. Baldwin's regulatory strategies mapped to instruments")

    # Stats
    total_instruments = sum(j["instrument_count"] for j in data["jurisdictions"])
    operative = sum(1 for j in data["jurisdictions"] for i in j["instruments"] if i["status"] == "Operative")
    reaches = sum(1 for j in data["jurisdictions"] for i in j["instruments"] if i.get("reaches_proprietary_pricing"))

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Jurisdictions", len(data["jurisdictions"]))
    m2.metric("Instruments", total_instruments)
    m3.metric("Operative", operative)
    m4.metric("Reaches Proprietary Pricing", reaches)

    # Proprietary pricing gap chart
    with st.expander("Proprietary pricing gap", expanded=False):
        gap_rows = []
        for j in data["jurisdictions"]:
            r = sum(1 for i in j["instruments"] if i.get("reaches_proprietary_pricing"))
            nr = j["instrument_count"] - r
            gap_rows.append({"jurisdiction": j["name"], "count": r, "type": "Reaches proprietary"})
            gap_rows.append({"jurisdiction": j["name"], "count": nr, "type": "Does not reach"})
        gap_df = pd.DataFrame(gap_rows)
        # Sort by proportion reaching
        j_order = gap_df[gap_df["type"] == "Reaches proprietary"].sort_values("count")["jurisdiction"].tolist()
        gap_chart = alt.Chart(gap_df).mark_bar().encode(
            y=alt.Y("jurisdiction:N", sort=j_order, title=None),
            x=alt.X("count:Q", title="Instruments"),
            color=alt.Color("type:N",
                scale=alt.Scale(domain=["Reaches proprietary", "Does not reach"], range=["#22c55e", "#2a2a3a"]),
                legend=alt.Legend(title=None, orient="top"),
            ),
            tooltip=["jurisdiction:N", "type:N", "count:Q"],
        ).properties(height=400)
        st.altair_chart(gap_chart, use_container_width=True)

    # Filters
    st.markdown("")
    f1, f2, f3, f4 = st.columns(4)
    with f1:
        filter_logic = st.multiselect("Design Logic", ["Unified", "Differentiated", "Accumulated"], default=[], placeholder="All")
    with f2:
        filter_strategy = st.multiselect("Strategy", STRATEGY_ORDER, default=[], placeholder="All")
    with f3:
        filter_status = st.multiselect("Status", list(STATUS_COLORS.keys()), default=[], placeholder="All")
    with f4:
        regions = sorted(set(j.get("region", "Other") for j in data["jurisdictions"]))
        filter_region = st.multiselect("Region", regions, default=[], placeholder="All")

    group_by_region = st.checkbox("Group by region", value=False)

    jurisdictions = data["jurisdictions"]
    if filter_logic:
        jurisdictions = [j for j in jurisdictions if j["design_logic"] in filter_logic]
    if filter_strategy:
        jurisdictions = [j for j in jurisdictions if any(i["strategy"] in filter_strategy for i in j["instruments"])]
    if filter_status:
        jurisdictions = [j for j in jurisdictions if any(i["status"] in filter_status for i in j["instruments"])]
    if filter_region:
        jurisdictions = [j for j in jurisdictions if j.get("region") in filter_region]

    st.caption(f"{len(jurisdictions)} jurisdictions shown")

    # Card grid
    COLS = 3

    def render_jurisdiction_card(j):
        with st.container(border=True):
            st.markdown(
                f"**{esc(j['name'])}** {design_logic_badge(j['design_logic'])}",
                unsafe_allow_html=True,
            )
            st.markdown(f"*{esc(j['key_finding'])}*")

            status_counts = Counter(i["status"] for i in j["instruments"])
            parts = []
            for s in ["Operative", "Enacted", "Proposed", "Active Investigation", "Failed", "Paused"]:
                n = status_counts.get(s, 0)
                if n > 0:
                    parts.append(f"{status_dot(s)} {n} {s.lower()}")
            st.markdown(
                f"**{j['instrument_count']}** instruments: " + " &nbsp; ".join(parts),
                unsafe_allow_html=True,
            )

            # Proprietary pricing fraction + political economy
            reaches = sum(1 for i in j["instruments"] if i.get("reaches_proprietary_pricing"))
            total = j["instrument_count"]
            r_color = "#22c55e" if reaches > 0 else "#6b7280"
            pe_counts = Counter(i.get("political_economy_outcome") for i in j["instruments"] if i.get("political_economy_outcome"))
            pe_html = " &nbsp;".join(f'{pe_pill(k)} {v}' for k, v in pe_counts.items()) if pe_counts else ""
            st.markdown(
                f'<span style="color:{r_color}; font-size:0.78rem;">{reaches}/{total} reach proprietary</span>'
                + (f" &nbsp;&nbsp;{pe_html}" if pe_html else ""),
                unsafe_allow_html=True,
            )

            strategies = sorted(set(i["strategy"] for i in j["instruments"]))
            chips = " ".join(strategy_chip(s) for s in strategies)
            st.markdown(chips, unsafe_allow_html=True)

            if st.button("View detail", key=f"btn_{j['id']}"):
                st.session_state.page = "detail"
                st.session_state.jurisdiction_id = j["id"]
                st.rerun()

    if group_by_region:
        region_groups = {}
        for j in jurisdictions:
            r = j.get("region", "Other")
            region_groups.setdefault(r, []).append(j)
        for region_name in ["North America", "Europe", "Asia-Pacific", "Southeast Asia", "Other"]:
            if region_name not in region_groups:
                continue
            st.markdown(f"### {region_name}")
            group = region_groups[region_name]
            rows = [group[i:i + COLS] for i in range(0, len(group), COLS)]
            for row in rows:
                cols = st.columns(COLS)
                for idx, j in enumerate(row):
                    with cols[idx]:
                        render_jurisdiction_card(j)
    else:
        rows = [jurisdictions[i:i + COLS] for i in range(0, len(jurisdictions), COLS)]
        for row in rows:
            cols = st.columns(COLS)
            for idx, j in enumerate(row):
                with cols[idx]:
                    render_jurisdiction_card(j)


# ============================================================
# DETAIL VIEW
# ============================================================

def render_detail(jurisdiction_id):
    jurisdiction = next((j for j in data["jurisdictions"] if j["id"] == jurisdiction_id), None)
    if not jurisdiction:
        st.error(f"Jurisdiction not found: {jurisdiction_id}")
        return

    # Header
    logic = jurisdiction["design_logic"]
    st.markdown(
        f"# {esc(jurisdiction['name'])} {design_logic_badge(logic)}",
        unsafe_allow_html=True,
    )
    st.caption(jurisdiction["key_finding"])

    c1, c2, c3 = st.columns(3)
    c1.metric("Instruments", jurisdiction["instrument_count"])
    reaches = sum(1 for i in jurisdiction["instruments"] if i.get("reaches_proprietary_pricing"))
    c2.metric("Reaches Proprietary", f"{reaches}/{jurisdiction['instrument_count']}")
    c3.markdown(f"**Design logic:** {esc(logic)}. {esc(jurisdiction['design_logic_detail'])}")

    # Instrument table
    st.markdown("#### Instruments")
    instruments = jurisdiction["instruments"]

    table_html = '''<table class="inst-table">
    <thead><tr>
        <th style="width:24%;">Instrument</th>
        <th>Strategy</th>
        <th>Status</th>
        <th>Target</th>
        <th>Institution</th>
        <th style="width:4%; text-align:center;">Prop.</th>
        <th style="width:4%; text-align:center;">PRA</th>
        <th>Political Economy</th>
    </tr></thead><tbody>'''

    for inst in instruments:
        reaches_icon = "&#10003;" if inst.get("reaches_proprietary_pricing") else "—"
        reaches_color = "#22c55e" if inst.get("reaches_proprietary_pricing") else "#3a3a4a"
        pra_icon = "&#10003;" if inst.get("private_right_of_action") else "—"
        pra_color = "#22c55e" if inst.get("private_right_of_action") else "#3a3a4a"
        # Show institution divergence with arrow
        formal = esc(inst.get("formal_institution", ""))
        operative = esc(inst.get("operative_institution", ""))
        diverges = inst.get("institution_divergence", False)
        arrow_color = "#ef4444" if diverges else "#3a3a4a"
        inst_cell = f'<span style="font-size:0.75rem; color:#9ca3af;">{formal}</span><br><span style="color:{arrow_color};">→</span> <span style="font-size:0.75rem;">{operative}</span>'
        # Target visibility
        vis = inst.get("target_visibility", "")
        vis_color = {"Conspicuous": "#22c55e", "Inconspicuous": "#ef4444", "Mixed": "#eab308"}.get(vis, "#6b7280")
        # Political economy
        pe_out = inst.get("political_economy_outcome")
        pe_detail = inst.get("political_economy_detail", "")
        pe_cell = pe_pill(pe_out) if pe_out else ""
        if pe_detail:
            pe_cell += f'<div class="inst-summary">{esc(pe_detail)}</div>'
        table_html += f'''<tr>
            <td>
                <div class="inst-name">{esc(inst["name"])}</div>
                <div class="inst-summary">{esc(inst["summary"])}</div>
            </td>
            <td>{strategy_chip(inst["strategy"])}</td>
            <td>{status_pill(inst["status"])}</td>
            <td style="font-size:0.78rem; color:{vis_color};">{esc(vis)}</td>
            <td style="font-size:0.75rem;">{inst_cell}</td>
            <td style="text-align:center; color:{reaches_color}; font-weight:600;">{reaches_icon}</td>
            <td style="text-align:center; color:{pra_color}; font-weight:600;">{pra_icon}</td>
            <td style="font-size:0.75rem;">{pe_cell}</td>
        </tr>'''

    table_html += '</tbody></table>'
    st.markdown(table_html, unsafe_allow_html=True)

    # Timeline per instrument
    with st.expander("Timelines"):
        for inst in instruments:
            st.markdown(f"**{inst['name']}**")
            for event in inst.get("timeline", []):
                st.markdown(f"- `{event['date']}` {event['event']}")
            st.markdown("")

    with st.expander("Enforcement details"):
        for inst in instruments:
            st.markdown(f"**{inst['name']}**")
            enforcement = inst.get("enforcement_mechanism", inst.get("enforcement", "—"))
            st.markdown(f"- Enforcement: {enforcement}")
            pra = inst.get("private_right_of_action")
            if pra is not None:
                st.markdown(f"- Private right of action: {'Yes' if pra else 'No'}")
            pe = inst.get("political_economy_outcome")
            if pe:
                detail = inst.get("political_economy_detail", "")
                st.markdown(f"- Political economy: {pe}" + (f". {detail}" if detail else ""))
            st.markdown("")

    # Full molecule, split into collapsible sections
    st.markdown("---")
    st.markdown("#### Full Jurisdiction Profile")
    molecule = load_molecule(jurisdiction["molecule_file"])
    if molecule:
        # Split by ## headings into collapsible expanders
        sections = re.split(r'^(## .+)$', molecule, flags=re.MULTILINE)
        # First chunk is intro (before any ##)
        intro = sections[0].strip()
        if intro:
            st.markdown(intro)
        # Remaining pairs: heading, body
        for i in range(1, len(sections), 2):
            heading = sections[i].replace("## ", "").strip()
            body = sections[i + 1].strip() if i + 1 < len(sections) else ""
            with st.expander(heading):
                st.markdown(body)
    else:
        st.warning(f"Molecule file not found: {jurisdiction['molecule_file']}")


# ============================================================
# TIMELINE VIEW
# ============================================================

def render_timeline():
    st.title("Instrument Timeline")
    st.caption("Every instrument plotted by date. Shows the 2024-2025 acceleration wave")

    # Build dataframe from all instruments with timeline events
    rows = []
    for j in data["jurisdictions"]:
        for inst in j["instruments"]:
            for event in inst.get("timeline", []):
                date_str = event["date"]
                # Normalize to a plottable date
                if len(date_str) == 4:  # YYYY
                    date_str += "-06"
                if len(date_str) == 7:  # YYYY-MM
                    date_str += "-15"
                rows.append({
                    "date": date_str,
                    "jurisdiction": j["name"],
                    "region": j.get("region", "Other"),
                    "instrument": inst["name"],
                    "strategy": inst["strategy"],
                    "status": inst["status"],
                    "event": event["event"],
                    "visibility": inst.get("target_visibility", ""),
                })

    if not rows:
        st.warning("No timeline data available.")
        return

    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])

    # Filters
    f1, f2, f3 = st.columns(3)
    with f1:
        regions = sorted(df["region"].unique())
        sel_regions = st.multiselect("Region", regions, default=[], placeholder="All", key="tl_region")
    with f2:
        sel_strategies = st.multiselect("Strategy", STRATEGY_ORDER, default=[], placeholder="All", key="tl_strategy")
    with f3:
        sel_status = st.multiselect("Status", list(STATUS_COLORS.keys()), default=[], placeholder="All", key="tl_status")

    if sel_regions:
        df = df[df["region"].isin(sel_regions)]
    if sel_strategies:
        df = df[df["strategy"].isin(sel_strategies)]
    if sel_status:
        df = df[df["status"].isin(sel_status)]

    y_field = st.radio("Y-axis", ["Jurisdiction", "Strategy"], horizontal=True, key="tl_yaxis")
    y_col = "jurisdiction" if y_field == "Jurisdiction" else "strategy"

    # Status color scale
    status_domain = list(STATUS_COLORS.keys())
    status_range = list(STATUS_COLORS.values())

    chart = alt.Chart(df).mark_circle(size=60, opacity=0.8).encode(
        x=alt.X("date:T", title="Date", axis=alt.Axis(format="%Y")),
        y=alt.Y(f"{y_col}:N", title=y_field, sort=None),
        color=alt.Color("status:N",
            scale=alt.Scale(domain=status_domain, range=status_range),
            legend=alt.Legend(title="Status"),
        ),
        tooltip=[
            alt.Tooltip("instrument:N", title="Instrument"),
            alt.Tooltip("jurisdiction:N", title="Jurisdiction"),
            alt.Tooltip("strategy:N", title="Strategy"),
            alt.Tooltip("status:N", title="Status"),
            alt.Tooltip("event:N", title="Event"),
            alt.Tooltip("date:T", title="Date", format="%b %Y"),
        ],
    ).properties(
        height=max(400, len(df[y_col].unique()) * 35),
    ).interactive()

    st.altair_chart(chart, use_container_width=True)
    st.caption(f"{len(df)} events across {df['instrument'].nunique()} instruments")


# ============================================================
# INSTITUTION DIVERGENCE VIEW
# ============================================================

def render_divergence():
    st.title("Institution Divergence")
    st.caption("Formal vs operative institutions: where the law says one thing and reality does another")

    # Count divergence
    total_jurisdictions = len(data["jurisdictions"])
    divergent_jurisdictions = 0
    all_rows = []

    for j in data["jurisdictions"]:
        j_has_divergence = False
        for inst in j["instruments"]:
            formal = inst.get("formal_institution", "")
            operative = inst.get("operative_institution", "")
            diverges = inst.get("institution_divergence", False)
            if diverges:
                j_has_divergence = True
            all_rows.append({
                "jurisdiction": j["name"],
                "region": j.get("region", "Other"),
                "instrument": inst["name"],
                "formal": formal,
                "operative": operative,
                "diverges": diverges,
                "strategy": inst["strategy"],
                "status": inst["status"],
            })
        if j_has_divergence:
            divergent_jurisdictions += 1

    m1, m2, m3 = st.columns(3)
    m1.metric("Jurisdictions with Divergence", f"{divergent_jurisdictions}/{total_jurisdictions}")
    divergent_count = sum(1 for r in all_rows if r["diverges"])
    m2.metric("Divergent Instruments", divergent_count)
    m3.metric("Total Instruments", len(all_rows))

    # Filter
    show_divergent_only = st.checkbox("Show only divergent instruments", value=True)
    display_rows = [r for r in all_rows if r["diverges"]] if show_divergent_only else all_rows

    # Render as HTML table grouped by jurisdiction
    current_j = None
    table_html = '''<table class="inst-table">
    <thead><tr>
        <th style="width:20%;">Jurisdiction</th>
        <th style="width:25%;">Instrument</th>
        <th style="width:22%;">Formal Institution</th>
        <th style="width:3%; text-align:center;"></th>
        <th style="width:22%;">Operative Institution</th>
        <th style="width:8%; text-align:center;">Diverges</th>
    </tr></thead><tbody>'''

    for r in display_rows:
        j_cell = f'<strong>{esc(r["jurisdiction"])}</strong>' if r["jurisdiction"] != current_j else ""
        current_j = r["jurisdiction"]
        div_icon = '<span style="color:#ef4444; font-weight:bold;">✗</span>' if r["diverges"] else '<span style="color:#22c55e;">✓</span>'
        arrow_color = "#ef4444" if r["diverges"] else "#3a3a4a"
        table_html += f'''<tr>
            <td style="font-size:0.8rem;">{j_cell}</td>
            <td style="font-size:0.8rem;">{esc(r["instrument"][:60])}</td>
            <td style="font-size:0.78rem; color:#9ca3af;">{esc(r["formal"])}</td>
            <td style="text-align:center; color:{arrow_color}; font-weight:bold;">→</td>
            <td style="font-size:0.78rem;">{esc(r["operative"])}</td>
            <td style="text-align:center;">{div_icon}</td>
        </tr>'''

    table_html += '</tbody></table>'
    st.markdown(table_html, unsafe_allow_html=True)


# ============================================================
# STRATEGY × VISIBILITY MATRIX
# ============================================================

def render_matrix():
    st.title("Strategy × Target Visibility")
    st.caption("Where instruments cluster. Baldwin's strategies against whether the regulated practice is observable")

    visibility_cols = ["Conspicuous", "Inconspicuous", "Mixed"]

    # Build counts
    matrix = {}
    for strategy in STRATEGY_ORDER:
        matrix[strategy] = {v: [] for v in visibility_cols}

    for j in data["jurisdictions"]:
        for inst in j["instruments"]:
            s = inst["strategy"]
            v = inst.get("target_visibility", "Mixed")
            if s in matrix and v in visibility_cols:
                matrix[s][v].append(inst)

    # Render as an HTML grid
    table_html = '''<table class="inst-table">
    <thead><tr>
        <th style="width:25%;">Strategy</th>'''
    for v in visibility_cols:
        table_html += f'<th style="text-align:center;">{esc(v)}</th>'
    table_html += '<th style="text-align:center;">Total</th></tr></thead><tbody>'

    for strategy in STRATEGY_ORDER:
        row_total = sum(len(matrix[strategy][v]) for v in visibility_cols)
        table_html += f'<tr><td><strong>{esc(strategy)}</strong></td>'
        for v in visibility_cols:
            instruments = matrix[strategy][v]
            count = len(instruments)
            if count == 0:
                table_html += '<td style="text-align:center; color:#3a3a4a;">—</td>'
            else:
                # Color intensity by count
                status_counts = Counter(inst["status"] for inst in instruments)
                status_dots = " ".join(f'{status_dot(s)}{n}' for s, n in status_counts.items() if n > 0)
                table_html += f'<td style="text-align:center;"><strong>{count}</strong><br><span style="font-size:0.7rem;">{status_dots}</span></td>'
        table_html += f'<td style="text-align:center; color:#6b7280;">{row_total}</td></tr>'

    # Column totals
    table_html += '<tr style="border-top:2px solid #2a2a3a;"><td style="color:#6b7280;"><em>Total</em></td>'
    for v in visibility_cols:
        col_total = sum(len(matrix[s][v]) for s in STRATEGY_ORDER)
        table_html += f'<td style="text-align:center; color:#6b7280;"><em>{col_total}</em></td>'
    grand_total = sum(len(matrix[s][v]) for s in STRATEGY_ORDER for v in visibility_cols)
    table_html += f'<td style="text-align:center; color:#6b7280;"><em>{grand_total}</em></td></tr>'

    table_html += '</tbody></table>'
    st.markdown(table_html, unsafe_allow_html=True)

    # Detail expander per cell
    st.markdown("#### Drill-down")
    sel_strategy = st.selectbox("Strategy", STRATEGY_ORDER, key="mx_strategy")
    sel_visibility = st.selectbox("Target Visibility", visibility_cols, key="mx_vis")
    instruments = matrix.get(sel_strategy, {}).get(sel_visibility, [])
    if instruments:
        for inst in instruments:
            st.markdown(f"- {status_pill(inst['status'])} **{inst['name']}**", unsafe_allow_html=True)
    else:
        st.caption("No instruments in this cell.")


# ============================================================
# POLITICAL ECONOMY VIEW
# ============================================================

def render_political_economy():
    st.title("Political Economy")
    st.caption("Legislative fate of instruments. Failed instruments are data")

    # Build dataframe
    rows = []
    for j in data["jurisdictions"]:
        for inst in j["instruments"]:
            pe = inst.get("political_economy_outcome")
            if pe:
                rows.append({
                    "jurisdiction": j["name"],
                    "strategy": inst["strategy"],
                    "instrument": inst["name"],
                    "outcome": pe,
                    "detail": inst.get("political_economy_detail", ""),
                    "status": inst["status"],
                })

    if not rows:
        st.warning("No political economy data available.")
        return

    df = pd.DataFrame(rows)

    m1, m2, m3 = st.columns(3)
    m1.metric("Instruments with PE outcome", len(df))
    m2.metric("Stalled or Blocked", len(df[df["outcome"].isin(["Stalled", "Blocked"])]))
    m3.metric("Passed", len(df[df["outcome"] == "Passed"]))

    # Stacked bar: strategy × outcome
    pe_domain = list(PE_COLORS.keys())
    pe_range = list(PE_COLORS.values())

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("strategy:N", sort=STRATEGY_ORDER, title=None),
        y=alt.Y("count():Q", title="Instruments"),
        color=alt.Color("outcome:N",
            scale=alt.Scale(domain=pe_domain, range=pe_range),
            legend=alt.Legend(title="Outcome", orient="top"),
        ),
        tooltip=[
            alt.Tooltip("strategy:N", title="Strategy"),
            alt.Tooltip("outcome:N", title="Outcome"),
            alt.Tooltip("count():Q", title="Count"),
        ],
    ).properties(height=350)

    st.altair_chart(chart, use_container_width=True)

    # Detail table
    st.markdown("#### Detail")
    sel_outcome = st.multiselect("Filter outcome", pe_domain, default=[], placeholder="All", key="pe_outcome")
    display_df = df[df["outcome"].isin(sel_outcome)] if sel_outcome else df

    table_html = '''<table class="inst-table">
    <thead><tr>
        <th>Jurisdiction</th>
        <th style="width:30%;">Instrument</th>
        <th>Strategy</th>
        <th>Outcome</th>
        <th style="width:30%;">Detail</th>
    </tr></thead><tbody>'''

    for _, r in display_df.iterrows():
        table_html += f'''<tr>
            <td style="font-size:0.8rem;">{esc(r["jurisdiction"])}</td>
            <td style="font-size:0.8rem;">{esc(r["instrument"][:60])}</td>
            <td>{strategy_chip(r["strategy"])}</td>
            <td>{pe_pill(r["outcome"])}</td>
            <td style="font-size:0.75rem; color:#9ca3af;">{esc(r["detail"])}</td>
        </tr>'''

    table_html += '</tbody></table>'
    st.markdown(table_html, unsafe_allow_html=True)


# ============================================================
# ANALYSIS VIEW
# ============================================================

def render_analysis(section_title=None, subsection_title=None):
    sections = parse_analysis_sections()
    if not sections:
        st.warning("Analysis file not found.")
        return

    # If a specific subsection was requested, show just that
    if subsection_title:
        for sec in sections:
            for sub in sec["subsections"]:
                if sub["title"] == subsection_title:
                    st.markdown(
                        f'<span style="color:#6b7280; font-size:0.8rem;">'
                        f'{esc(sec["title"].split("(")[0].strip())}</span>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(f"## {sub['title']}")
                    st.markdown(sub["body"])

                    # Prev/next navigation
                    all_subs = [(sec, sub) for sec in sections for sub in sec["subsections"]]
                    current_idx = next(
                        (i for i, (s, su) in enumerate(all_subs) if su["title"] == subsection_title),
                        None,
                    )
                    if current_idx is not None:
                        nav_cols = st.columns(2)
                        if current_idx > 0:
                            prev_sec, prev_sub = all_subs[current_idx - 1]
                            with nav_cols[0]:
                                if st.button(f"← {prev_sub['title'][:40]}", key="prev_sub"):
                                    st.session_state.page = "analysis_sub"
                                    st.session_state.analysis_section = prev_sec["title"]
                                    st.session_state.analysis_subsection = prev_sub["title"]
                                    st.rerun()
                        if current_idx < len(all_subs) - 1:
                            next_sec, next_sub = all_subs[current_idx + 1]
                            with nav_cols[1]:
                                if st.button(f"{next_sub['title'][:40]} →", key="next_sub"):
                                    st.session_state.page = "analysis_sub"
                                    st.session_state.analysis_section = next_sec["title"]
                                    st.session_state.analysis_subsection = next_sub["title"]
                                    st.rerun()
                    return

    # If a specific H2 section was requested, show it with sub-tabs
    if section_title:
        sec = next((s for s in sections if s["title"] == section_title), None)
        if sec:
            st.markdown(f"## {sec['title']}")
            if sec["intro"]:
                st.markdown(sec["intro"])

            if sec["subsections"]:
                tab_names = [sub["title"] for sub in sec["subsections"]]
                # Truncate tab names for display
                short_names = []
                for name in tab_names:
                    # Extract just the key part
                    clean = re.sub(r'^\d+\.\s*', '', name)  # strip leading numbers
                    if len(clean) > 35:
                        clean = clean[:32] + "..."
                    short_names.append(clean)

                tabs = st.tabs(short_names)
                for tab, sub in zip(tabs, sec["subsections"]):
                    with tab:
                        st.markdown(f"### {sub['title']}")
                        st.markdown(sub["body"])
            return

    # Default: show overview of all sections
    st.title("Cross-Cutting Analysis")
    st.caption("Patterns, findings, and theoretical framework emerging from 15 jurisdictions")

    for sec in sections:
        st.markdown(f"### {sec['title'].split('(')[0].strip()}")
        if sec["intro"]:
            st.caption(sec["intro"][:200] + "..." if len(sec["intro"]) > 200 else sec["intro"])
        st.markdown(f"**{len(sec['subsections'])} sections**")
        for sub in sec["subsections"]:
            preview = sub["body"][:120].replace("\n", " ") + "..." if len(sub["body"]) > 120 else sub["body"].replace("\n", " ")
            if st.button(f"{sub['title']}", key=f"aov_{sub['title'][:25]}"):
                st.session_state.page = "analysis_sub"
                st.session_state.analysis_section = sec["title"]
                st.session_state.analysis_subsection = sub["title"]
                st.rerun()
            st.caption(preview)

        st.markdown("---")


# ============================================================
# ROUTING
# ============================================================

page = st.session_state.page

if page == "detail" and st.session_state.jurisdiction_id:
    render_detail(st.session_state.jurisdiction_id)
elif page == "timeline":
    render_timeline()
elif page == "divergence":
    render_divergence()
elif page == "matrix":
    render_matrix()
elif page == "political_economy":
    render_political_economy()
elif page == "analysis":
    render_analysis(section_title=st.session_state.get("analysis_section"))
elif page == "analysis_sub":
    render_analysis(
        section_title=st.session_state.get("analysis_section"),
        subsection_title=st.session_state.get("analysis_subsection"),
    )
else:
    render_grid()
