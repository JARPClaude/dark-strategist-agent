#!/usr/bin/env python3
"""Offline regression for archetype lenses (P2). No API calls. Run from orchestrator/."""
import sys
from archetype_lenses import ARCHETYPE_LENSES, select_lenses, build_lens_directive

CATALOG = len(ARCHETYPE_LENSES)


def _checks():
    """Yields (label, passed_bool)."""
    #--- 1. Catalog integrity: non-empty, every entry has id/label/angle, ids unique.
    ids = [l.get("id") for l in ARCHETYPE_LENSES]
    yield ("catalog integrity (id/label/angle present, ids unique)",
           CATALOG >= 2
           and all(l.get("id") and l.get("label") and l.get("angle") for l in ARCHETYPE_LENSES)
           and len(ids) == len(set(ids)))

    #--- 2. Order contract: first complementary pair is FALSIFIER then FAILURE_MODE_HUNTER.
    yield ("order: first pair = FALSIFIER, FAILURE_MODE_HUNTER",
           ids[:2] == ["FALSIFIER", "FAILURE_MODE_HUNTER"])

    #--- 3. select_lenses(2) returns first 2 in order.
    two = select_lenses(2)
    yield ("select_lenses(2) -> first two in order",
           [l["id"] for l in two] == ["FALSIFIER", "FAILURE_MODE_HUNTER"])

    #--- 4. select_lenses caps at catalog size (no IndexError, no padding).
    yield ("select_lenses(99) caps at catalog size",
           len(select_lenses(99)) == CATALOG)

    #--- 5. Degenerate n -> empty list (0, negative, None, non-numeric).
    yield ("degenerate n (0 / -1 / None / 'x') -> []",
           select_lenses(0) == [] and select_lenses(-1) == []
           and select_lenses(None) == [] and select_lenses("x") == [])

    #--- 6. Numeric-string coercion: "2" -> 2 lenses.
    yield ('select_lenses("2") coerces to 2', len(select_lenses("2")) == 2)

    #--- 7. Determinism: same call twice -> identical ids.
    yield ("determinism: select_lenses(3) stable across calls",
           [l["id"] for l in select_lenses(3)] == [l["id"] for l in select_lenses(3)])

    #--- 8. Isolation: mutating a returned lens must NOT corrupt the frozen catalog.
    snapshot = ARCHETYPE_LENSES[0]["angle"]
    select_lenses(1)[0]["angle"] = "MUTATED"
    yield ("isolation: catalog not mutated by caller", ARCHETYPE_LENSES[0]["angle"] == snapshot)

    #--- 9. build_lens_directive embeds round, label, angle and focus.
    d = build_lens_directive(two[0], 1, "F1 | F2")
    yield ("directive embeds round/label/angle/focus",
           "ROUND 1" in d and two[0]["label"] in d
           and two[0]["angle"][:20] in d and "F1 | F2" in d)

    #--- 10. build_lens_directive degrades gracefully (None lens, empty focus, bad round).
    d2 = build_lens_directive(None, "bad", "")
    yield ("directive graceful on None lens / empty focus / bad round",
           "ROUND 1" in d2 and "low-corroboration verdict" in d2)


def main():
    fails = 0
    total = 0
    for label, ok in _checks():
        total += 1
        print(("PASS" if ok else "FAIL"), "--", label)
        if not ok:
            fails += 1
    print("=" * 40)
    print("RESULT: %d FAIL / %d total" % (fails, total))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
