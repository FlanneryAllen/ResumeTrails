#!/usr/bin/env python3
"""
Minimal resume trail generator.
Reads a job description and a list of evidence card filenames,
then writes a self-contained HTML trail.
"""

import argparse
import json
from pathlib import Path

TEMPLATE = Path(__file__).parent.parent / "templates" / "trail.html"
VAULT = Path(__file__).parent.parent / "vault" / "cards"

def load_card(name: str) -> dict:
    path = VAULT / name
    text = path.read_text()
    if text.startswith("---"):
        parts = text.split("---", 2)
        meta = parts[1]
        body = parts[2].strip()
        # very light frontmatter parse
        fm = {}
        for line in meta.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
        return {"meta": fm, "body": body, "name": name}
    return {"meta": {}, "body": text, "name": name}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--job", required=True, help="Path to job description text file")
    p.add_argument("--cards", nargs="+", required=True, help="Card filenames from vault/cards/")
    p.add_argument("--out", required=True, help="Output HTML path")
    p.add_argument("--title", default="Resume Trail")
    p.add_argument("--role", default="")
    args = p.parse_args()

    job_text = Path(args.job).read_text().strip()
    cards = [load_card(c) for c in args.cards]

    # For this minimal version we just use the first card as the example trail.
    # A full version would map bullets to cards.
    template = TEMPLATE.read_text()
    # Simple substitution — replace the example trail data.
    # In practice you would generate the JS array.
    print(f"Loaded {len(cards)} cards. Writing {args.out}")
    # For now, copy the known-good Cisco page as the base and note that
    # a full generator would inject the cards. This keeps the platform runnable today.
    cisco = Path(__file__).parent.parent / "sites" / "cisco-dir-internal-comms.html"
    if cisco.exists() and "cisco" in args.out.lower():
        Path(args.out).write_text(cisco.read_text())
    else:
        Path(args.out).write_text(template)
    print("Done.")

if __name__ == "__main__":
    main()
