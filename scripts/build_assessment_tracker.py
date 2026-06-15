#!/usr/bin/env python3
"""Generate audit/assessment-tracker.csv from the CMMC->AZ-104 mapping CSVs.

The tracker is an auditor-facing worksheet: one row per CMMC practice with
empty columns for an assessor to record implementation status, evidence
location, the assessment method used, and the final finding.

Usage:
    python3 scripts/build_assessment_tracker.py
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = [
    (ROOT / "csv" / "cmmc-level1-az104-mapping.csv", "Level 1"),
    (ROOT / "csv" / "cmmc-level2-az104-mapping.csv", "Level 2"),
]
OUTPUT = ROOT / "audit" / "assessment-tracker.csv"

# Auditor worksheet columns. Mapping context is pre-filled; the assessor
# fills the remaining columns during the engagement.
FIELDS = [
    "Practice ID",
    "Level",
    "CMMC Domain",
    "Practice Name",
    "NIST 800-171 Ref",
    "Azure Service(s)",
    "Implementation Status",        # Implemented / Partially / Planned / Not Implemented
    "Assessment Method",            # Examine / Interview / Test (one or more)
    "Evidence Artifact / Location", # path or system where evidence lives
    "Assessor Notes",
    "Finding",                      # Met / Not Met / N/A
    "POA&M ID",                     # link to Plan of Action if Not Met
]


def load(path, level):
    rows = {}
    with path.open(newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            pid = r["Practice ID"].strip()
            rows[pid] = {
                "Practice ID": pid,
                "Level": level,
                "CMMC Domain": r["CMMC Domain"].strip(),
                "Practice Name": r["Practice Name"].strip(),
                "NIST 800-171 Ref": r["NIST 800-171 Ref"].strip(),
                "Azure Service(s)": r["Azure Service(s)"].strip(),
                "Implementation Status": "",
                "Assessment Method": "",
                "Evidence Artifact / Location": "",
                "Assessor Notes": "",
                "Finding": "",
                "POA&M ID": "",
            }
    return rows


def main():
    merged = {}
    for path, level in SOURCES:
        for pid, row in load(path, level).items():
            # A practice can appear in both levels (L1 carried into L2);
            # keep the lowest level it is introduced at.
            if pid not in merged:
                merged[pid] = row

    def sort_key(item):
        pid = item[0]
        domain = pid.split(".")[0]
        return (domain, pid)

    OUTPUT.parent.mkdir(exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        for _pid, row in sorted(merged.items(), key=sort_key):
            writer.writerow(row)

    print(f"Wrote {len(merged)} practices to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
