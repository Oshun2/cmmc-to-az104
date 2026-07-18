#!/usr/bin/env python3
"""Validate internal consistency of the CMMC -> Azure mapping data.

Run locally or in CI. Exits non-zero on any failure.

Checks:
  1. Level 1 CSV contains exactly 15 practices (FAR 52.204-21, items i-xv).
  2. Level 2 CSV contains exactly 110 practices (NIST SP 800-171 Rev 2).
  3. No duplicate Practice IDs within either CSV.
  4. Every practice has a non-empty NIST 800-171 Ref and Azure Service(s).
  5. Practice IDs are well formed (e.g. AC.L1-3.1.1 / SC.L2-3.13.16).
  6. The committed assessment tracker matches a freshly generated one
     (guards against the tracker drifting out of sync with the CSVs).

Usage:
    python3 scripts/validate.py
"""
import csv
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
L1 = ROOT / "csv" / "cmmc-level1-az104-mapping.csv"
L2 = ROOT / "csv" / "cmmc-level2-az104-mapping.csv"
TRACKER = ROOT / "audit" / "assessment-tracker.csv"

EXPECTED_L1 = 15
EXPECTED_L2 = 110

# e.g. AC.L1-3.1.1, SC.L2-3.13.16
PRACTICE_ID = re.compile(r"^[A-Z]{2}\.L[123]-3\.\d{1,2}\.\d{1,2}$")

failures = []
notes = []


def check(condition, message, hint=None):
    """Record a passing note, or a failure (with an optional remediation hint)."""
    if condition:
        notes.append(f"  ok   {message}")
    else:
        failures.append(message if not hint else f"{message}\n       -> {hint}")


def load(path):
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def validate_csv(path, expected_count, label):
    rows = load(path)
    ids = [r["Practice ID"].strip() for r in rows]

    check(
        len(rows) == expected_count,
        f"{label}: expected {expected_count} practices, found {len(rows)}",
    )

    dupes = {i for i in ids if ids.count(i) > 1}
    check(not dupes, f"{label}: duplicate Practice IDs: {sorted(dupes) or 'none'}")

    malformed = [i for i in ids if not PRACTICE_ID.match(i)]
    check(not malformed, f"{label}: malformed Practice IDs: {malformed or 'none'}")

    missing_nist = [
        r["Practice ID"] for r in rows if not r.get("NIST 800-171 Ref", "").strip()
    ]
    check(
        not missing_nist,
        f"{label}: practices missing NIST 800-171 Ref: {missing_nist or 'none'}",
    )

    missing_svc = [
        r["Practice ID"] for r in rows if not r.get("Azure Service(s)", "").strip()
    ]
    check(
        not missing_svc,
        f"{label}: practices missing Azure Service(s): {missing_svc or 'none'}",
    )

    return set(ids)


def validate_tracker():
    """Regenerate the tracker into a temp copy and compare to the committed file."""
    if not TRACKER.exists():
        failures.append("tracker: audit/assessment-tracker.csv is missing")
        return

    # Use byte-exact I/O: read_text()/write_text() normalize newlines, which
    # would silently rewrite the file's line endings on restore.
    committed = TRACKER.read_bytes()

    try:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "build_assessment_tracker.py")],
            check=True,
            capture_output=True,
            cwd=ROOT,
        )
        regenerated = TRACKER.read_bytes()
    finally:
        # Always restore the committed content so validation is side-effect free.
        TRACKER.write_bytes(committed)

    check(
        committed == regenerated,
        "tracker: assessment-tracker.csv is in sync with the CSVs",
        hint="regenerate it: python3 scripts/build_assessment_tracker.py",
    )


def main():
    l1_ids = validate_csv(L1, EXPECTED_L1, "Level 1 CSV")
    l2_ids = validate_csv(L2, EXPECTED_L2, "Level 2 CSV")

    # Level 1 practices also carry forward into Level 2.
    missing_in_l2 = l1_ids - l2_ids
    check(
        not missing_in_l2,
        f"Level 1 practices absent from Level 2 CSV: {sorted(missing_in_l2) or 'none'}",
    )

    validate_tracker()

    print("\n".join(notes))
    if failures:
        print("\nFAILED:")
        for f in failures:
            print(f"  x  {f}")
        sys.exit(1)
    print(f"\nAll checks passed ({EXPECTED_L1} L1 / {EXPECTED_L2} L2 practices).")


if __name__ == "__main__":
    main()
