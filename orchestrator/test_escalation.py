#!/usr/bin/env python3
"""Offline regression for should_escalate (P1, v3.12.0). No API calls. Run from orchestrator/."""
import sys
from schema import should_escalate

CASES = [
    # (confidence, rounds_done, max_rounds, remaining_agents, enabled) -> expected
    (("LOW", 0, 1, 3, True), True),       # canonical: LOW, budget, room
    (("HIGH", 0, 1, 3, True), False),     # not LOW
    (("MODERATE", 0, 1, 3, True), False), # not LOW
    (("LOW", 1, 1, 3, True), False),      # round cap reached
    (("LOW", 0, 1, 0, True), False),      # no agent budget
    (("LOW", 0, 1, 3, False), False),     # disabled
    (("LOW", 0, 2, 3, True), True),       # room for round 1 of 2
    (("LOW", 1, 2, 3, True), True),       # room for round 2 of 2
    (("LOW", 2, 2, 3, True), False),      # cap reached (2 of 2)
    (("LOW", 0, 0, 3, True), False),      # max_rounds=0 disables
]

def main():
    fails = 0
    for args, expected in CASES:
        got = should_escalate(*args)
        ok = got == expected
        print(("PASS" if ok else "FAIL"), args, "->", got, "(expected %s)" % expected)
        if not ok:
            fails += 1
    print("=" * 40)
    print("RESULT: %d FAIL / %d total" % (fails, len(CASES)))
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
