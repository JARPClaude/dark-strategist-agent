#!/usr/bin/env python3
"""Offline regression for compute_confidence (P3, v3.11.0). No API calls. Run from orchestrator/."""
import sys
from schema import compute_confidence

CASES = [
    # (n, driver_corroborated, driver_count, unresolved) -> expected
    ((1, False, 0, 0), "LOW"),     # <2 agents
    ((1, True, 3, 0),  "LOW"),     # <2 agents dominates
    ((5, True, 3, 2),  "LOW"),     # >=2 unresolved clashes
    ((3, False, 1, 0), "LOW"),     # verdict hinges on single uncorroborated finding
    ((3, True, 2, 0),  "HIGH"),    # corroborated driver, n>=3, 0 conflicts
    ((4, False, 0, 0), "HIGH"),    # clean verdict (no findings), n>=3
    ((3, True, 1, 0),  "HIGH"),    # single corroborated finding
    ((2, True, 2, 0),  "MODERATE"),# n=2 (<3) cannot be HIGH
    ((3, True, 2, 1),  "MODERATE"),# 1 conflict (not >=2) blocks HIGH
    ((3, False, 2, 0), "MODERATE"),# multi-finding driver, none corroborated
]

def main():
    fails = 0
    for args, expected in CASES:
        got = compute_confidence(*args)
        ok = got == expected
        print(("PASS" if ok else "FAIL"), args, "->", got, "(expected %s)" % expected)
        if not ok:
            fails += 1
    print("=" * 40)
    print("RESULT: %d FAIL / %d total" % (fails, len(CASES)))
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
