#!/usr/bin/env python3
"""
Parse jurisdiction molecules from the vault into structured data.json.

Reads from: ~/exocortex/library/molecules/sp-*.md
Writes to:  ./data.json

The molecule template defines the schema. This parser extracts:
1. Frontmatter (YAML)
2. Key Data block (key-value pairs)
3. Instruments table (9 columns)
4. Section presence and content
5. Computed fields (counts, year range, etc.)
"""
import re
import json
import yaml
from pathlib import Path

VAULT_MOLECULES = Path.home() / "exocortex" / "library" / "molecules"
OUTPUT = Path(__file__).parent / "data.json"

# Slugify jurisdiction name for ID
def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

# Parse YAML frontmatter
def parse_frontmatter(text):
    if text.startswith('---'):
        end = text.find('---', 3)
        if end != -1:
            try:
                return yaml.safe_load(text[3:end]), text[end+3:].strip()
            except yaml.YAMLError:
                pass
    return {}, text

# Parse Key Data block
def parse_key_data(text):
    data = {}
    match = re.search(r'^## Key Data\s*\n(.*?)(?=\n## |\Z)', text, re.DOTALL | re.MULTILINE)
    if match:
        for line in match.group(1).strip().split('\n'):
            line = line.strip()
            if line.startswith('- ') and ':' in line:
                key, val = line[2:].split(':', 1)
                data[key.strip()] = val.strip()
    return data

# Parse markdown table into list of dicts
def parse_table(text, section_name="## Instruments"):
    pattern = rf'^{re.escape(section_name)}\s*\n(.*?)(?=\n## |\Z)'
    match = re.search(pattern, text, re.DOTALL | re.MULTILINE)
    if not match:
        return []

    table_text = match.group(1).strip()
    lines = [l.strip() for l in table_text.split('\n') if l.strip().startswith('|')]

    if len(lines) < 3:  # header + separator + at least one row
        return []

    # Parse header
    headers = [h.strip() for h in lines[0].split('|')[1:-1]]

    # Parse rows (skip separator line)
    rows = []
    for line in lines[2:]:
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if len(cells) == len(headers):
            row = {}
            for h, c in zip(headers, cells):
                # Strip wikilinks
                c = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', r'\2', c)
                c = re.sub(r'\[\[([^\]]+)\]\]', r'\1', c)
                row[h] = c
            rows.append(row)

    return rows

# Parse timeline from Detail section
def parse_timelines(text):
    """Extract timeline lists from ## Detail subsections."""
    timelines = {}
    # Find each ### subsection
    subsections = re.split(r'^### (.+)$', text, flags=re.MULTILINE)
    for i in range(1, len(subsections), 2):
        heading = subsections[i].strip()
        body = subsections[i+1] if i+1 < len(subsections) else ""

        # Find **Timeline.** block
        tl_match = re.search(r'\*\*Timeline\.\*\*\s*\n((?:- .*\n?)+)', body)
        if tl_match:
            events = []
            for line in tl_match.group(1).strip().split('\n'):
                line = line.strip()
                if line.startswith('- '):
                    parts = line[2:].split(':', 1)
                    if len(parts) == 2:
                        events.append({
                            "date": parts[0].strip(),
                            "event": parts[1].strip()
                        })
            if events:
                # Use first word(s) of heading as key
                timelines[heading] = events

    return timelines

# Extract opening paragraph (between Key Data and ## Instruments)
def parse_opening(text):
    # After Key Data block, before ## Instruments
    match = re.search(r'^## Key Data\s*\n.*?\n\n(.+?)(?=\n## Instruments)', text, re.DOTALL | re.MULTILINE)
    if match:
        opening = match.group(1).strip()
        # Strip wikilinks
        opening = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', r'\2', opening)
        opening = re.sub(r'\[\[([^\]]+)\]\]', r'\1', opening)
        return opening
    return ""

# Normalize strategy names from messy old-format molecules
def normalize_strategy(raw):
    raw = re.sub(r'\s*\([^)]*\)', '', raw).strip()  # strip parentheticals
    raw = raw.split('/')[0].strip()  # take first if compound
    raw = raw.split('+')[0].strip()  # take first if compound
    mapping = {
        "command and control": "Prohibition",
        "code-as-regulation": "Direct Action",
        "self-regulation": "Self-Regulation",
        "rights & liabilities": "Rights & Liabilities",
        "institutional coordination": "Direct Action",
    }
    return mapping.get(raw.lower(), raw.title() if raw[0:1].islower() else raw) if raw else ""

# Map table row to instrument dict
def row_to_instrument(row, timelines):
    name = row.get("Instrument", "")
    strategy = normalize_strategy(row.get("Strategy", ""))
    subtype = row.get("Sub-type", "")
    sector = row.get("Sector", "")
    status = row.get("Status", "")
    enforcement = row.get("Enforcement", "")
    target_species = row.get("Target Species", "")
    reaches_core = row.get("Reaches Core", "").strip().lower() == "yes"
    pe_outcome = row.get("PE Outcome", "").strip() or None

    # Map PRA from enforcement text
    has_pra = "PRA" in enforcement or "private right of action" in enforcement.lower()

    # Find matching timeline
    timeline = []
    for heading, events in timelines.items():
        # Match by first few chars of instrument name
        name_prefix = name.split('(')[0].strip()[:15]
        if name_prefix and name_prefix.lower() in heading.lower():
            timeline = events
            break

    inst = {
        "name": name,
        "strategy": strategy,
        "sub_type": subtype if subtype else None,
        "sector": sector,
        "status": status,
        "enforcement_mechanism": enforcement,
        "target_species": target_species,
        "reaches_core": reaches_core,
        "pe_outcome": pe_outcome,
        "private_right_of_action": has_pra,
        "timeline": timeline,
    }

    return inst

# Parse a single molecule file
def parse_molecule(filepath):
    text = filepath.read_text(encoding='utf-8')

    # Frontmatter
    frontmatter, body = parse_frontmatter(text)

    # Title
    title_match = re.search(r'^# (.+)', body, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else filepath.stem

    # Key Data
    key_data = parse_key_data(body)

    # Opening paragraph
    opening = parse_opening(body)

    # Instruments table
    rows = parse_table(body)

    # Timelines from Detail
    timelines = parse_timelines(body)

    # Build instruments
    instruments = [row_to_instrument(r, timelines) for r in rows]

    # Compute fields
    instrument_count = len(instruments)
    operative_count = sum(1 for i in instruments if i["status"].startswith("Operative"))
    reaches_core_count = sum(1 for i in instruments if i["reaches_core"])
    failed_count = sum(1 for i in instruments if i["status"] == "Failed")
    strategy_set = sorted(set(i["strategy"] for i in instruments if i["strategy"]))
    species_set = sorted(set(i["target_species"] for i in instruments if i["target_species"]))

    # Year range from timelines
    all_years = []
    for inst in instruments:
        for event in inst.get("timeline", []):
            year_match = re.match(r'(\d{4})', event.get("date", ""))
            if year_match:
                all_years.append(int(year_match.group(1)))
    year_first = min(all_years) if all_years else None
    year_latest = max(all_years) if all_years else None

    # Region mapping
    region = key_data.get("region", "Other")

    # Jurisdiction name from title
    name = re.sub(r'\s*—.*$', '', title).strip()
    # Clean up prefix patterns
    name = re.sub(r'Surveillance Pricing Regulatory Profile$', '', name).strip()
    name = re.sub(r'Regulatory Profile$', '', name).strip()
    name = name.strip(' —-')

    jid = slugify(name)

    jurisdiction = {
        "id": jid,
        "name": name,
        "design_logic": key_data.get("design-logic", ""),
        "key_finding": key_data.get("key-finding", ""),
        "instrument_count": instrument_count,
        "operative_count": operative_count,
        "reaches_core_count": reaches_core_count,
        "failed_count": failed_count,
        "strategy_set": strategy_set,
        "species_set": species_set,
        "year_first": year_first,
        "year_latest": year_latest,
        "region": region,
        "molecule_file": filepath.name,
        "opening": opening,
        "instruments": instruments,
    }

    return jurisdiction

# Main
def main():
    molecules = sorted(VAULT_MOLECULES.glob("sp-*.md"))
    print(f"Found {len(molecules)} molecules in {VAULT_MOLECULES}")

    jurisdictions = []
    for f in molecules:
        print(f"  Parsing: {f.name}")
        try:
            j = parse_molecule(f)
            print(f"    → {j['name']}: {j['instrument_count']} instruments, "
                  f"{j['reaches_core_count']} reach core, "
                  f"years {j['year_first']}-{j['year_latest']}")
            jurisdictions.append(j)
        except Exception as e:
            print(f"    ✗ ERROR: {e}")

    # Build output
    output = {
        "jurisdictions": jurisdictions,
        "strategy_types": [
            "Prohibition", "Competition", "Disclosure",
            "Rights & Liabilities", "Direct Action",
            "Self-Regulation", "Incentive-Based",
        ],
        "status_types": [
            "Operative", "Operative, unenforced", "Enacted",
            "Proposed", "Failed", "Paused", "Contested", "Settled", "Study",
        ],
        "species_types": [
            "Core Species", "Collusion", "Drip Pricing",
            "Surge Pricing", "Price Walking", "General",
        ],
    }

    OUTPUT.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote {len(jurisdictions)} jurisdictions to {OUTPUT}")
    print(f"Total instruments: {sum(j['instrument_count'] for j in jurisdictions)}")
    print(f"Total reaching core: {sum(j['reaches_core_count'] for j in jurisdictions)}")

if __name__ == "__main__":
    main()
