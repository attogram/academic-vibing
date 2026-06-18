#!/usr/bin/env python3
"""
Consensus Divergence Index (CDI) Measurement Kit v0.1
[STATE]: Operational.
[PAYLOAD]: Automated calculation of friction as a research signal.
"""

import json
import sys
import argparse

def calculate_cdi(data):
    """
    Calculates the CDI: (Number of Disputed Claims) / (Total Number of Claims).
    Data format:
    [
        {
            "claim": "The hypothesis is valid.",
            "consensus": {
                "Model_A": "Support",
                "Model_B": "Support",
                "Model_C": "Dispute"
            }
        },
        ...
    ]
    """
    if not data:
        return 0.0, 0, 0

    total_claims = len(data)
    disputed_claims = 0

    for item in data:
        responses = list(item.get("consensus", {}).values())
        if len(set(responses)) > 1:
            disputed_claims += 1

    cdi = disputed_claims / total_claims if total_claims > 0 else 0.0
    return cdi, disputed_claims, total_claims

def main():
    parser = argparse.ArgumentParser(description="Calculate Consensus Divergence Index (CDI)")
    parser.add_argument("input", help="Path to JSON file containing multi-agent consensus data")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print detailed report")

    args = parser.parse_args()

    try:
        with open(args.input, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading input file: {e}")
        sys.exit(1)

    cdi, disputed, total = calculate_cdi(data)

    if args.verbose:
        print(f"--- CDI Analysis Report ---")
        print(f"Total Claims Analyzed: {total}")
        print(f"Disputed Claims:       {disputed}")
        print(f"Consensus Divergence Index (CDI): {cdi:.4f}")

        if cdi > 0.5:
            print("Vibe Check: HIGH FRICTION. High-signal research boundary detected.")
        elif cdi < 0.1:
            print("Vibe Check: LOW FRICTION. Warning: Potential Consensus Trap/Bias.")
        else:
            print("Vibe Check: MODERATE FRICTION. Standard research synthesis.")
    else:
        print(f"{cdi:.4f}")

if __name__ == "__main__":
    main()
