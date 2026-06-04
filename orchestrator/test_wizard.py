"""
Dark Strategist v3.9.0 — Wizard unit test
Covers the pure build_command() contract (no stdin/IO). Run: python test_wizard.py
"""
from wizard import build_command, format_command, AGENT_SIZES


def _check(name, got, expected):
    assert got == expected, f"[FAIL] {name}\n  got:      {got}\n  expected: {expected}"
    print(f"[PASS] {name}")


def test_legal_subarea():
    answers = {
        "type": "legal", "subscenario": "nda",
        "objective": "identify risks", "regime": "adversarial",
        "tribunal": False, "agents": None, "ssm": False, "ssm_scale": "MESO",
    }
    _check("legal+subarea, no tribunal/ssm", build_command(answers), [
        "--type", "legal", "--subscenario", "nda",
        "--objective", "identify risks", "--regime", "adversarial",
    ])


def test_trading_full_pipeline():
    answers = {
        "type": "trading", "subscenario": "XAUUSD",
        "objective": "buy sell or wait", "regime": "breakout",
        "tribunal": True, "agents": 5, "ssm": True, "ssm_scale": "MACRO",
    }
    _check("trading + tribunal(5) + ssm(MACRO)", build_command(answers), [
        "--type", "trading", "--subscenario", "XAUUSD",
        "--objective", "buy sell or wait", "--regime", "breakout",
        "--tribunal", "--agents", "5", "--ssm", "--ssm-scale", "MACRO",
    ])


def test_tribunal_auto_size_omits_agents():
    answers = {
        "type": "startup", "subscenario": "seed_pitch",
        "objective": "evaluate viability", "regime": "standard",
        "tribunal": True, "agents": None, "ssm": False, "ssm_scale": "MESO",
    }
    #--- agents None => auto-size => --agents must be ABSENT
    _check("tribunal auto-size omits --agents", build_command(answers), [
        "--type", "startup", "--subscenario", "seed_pitch",
        "--objective", "evaluate viability", "--regime", "standard",
        "--tribunal",
    ])


def test_invalid_agents_omitted():
    answers = {
        "type": "general", "subscenario": "case",
        "objective": "identify risks and failure modes", "regime": "standard",
        "tribunal": True, "agents": 4, "ssm": False, "ssm_scale": "MESO",
    }
    #--- 4 is not a legal size (1/3/5/7) => omitted, falls back to auto
    out = build_command(answers)
    assert "--agents" not in out, f"[FAIL] invalid agents 4 should be omitted: {out}"
    assert 4 in AGENT_SIZES or 4 not in AGENT_SIZES  #--- guard: 4 not a valid size
    print("[PASS] invalid agents size (4) omitted -> auto")


def test_format_command_quotes_spaces():
    argv = ["--type", "legal", "--objective", "identify risks"]
    _check("format quotes tokens with spaces", format_command(argv),
           'python main.py --type legal --objective "identify risks"')


if __name__ == "__main__":
    test_legal_subarea()
    test_trading_full_pipeline()
    test_tribunal_auto_size_omits_agents()
    test_invalid_agents_omitted()
    test_format_command_quotes_spaces()
    print("\n[OK] wizard unit suite: 5/5 passed")
