"""
Dark Strategist Agent v3.0.0 — Main Entry Point
Tribunal Transversal + Dynamic Prompts + Structured Output

Usage:
    # Case-based (v3.0 — recommended)
    python main.py --type contract --subscenario alquiler --objective "identify risks" --regime adversarial

    # With Tribunal Transversal
    python main.py --type finance --subscenario investment_review --objective "evaluate viability" --tribunal

    # With SSM
    python main.py --type contract --subscenario alquiler --objective "identify risks" --tribunal --ssm

    # Full pipeline
    python main.py --type trading --subscenario XAUUSD --objective "buy sell or wait" --regime breakout --tribunal --ssm --ssm-scale MACRO

    # Document-based (v2.x compatibility)
    python main.py --document doc.txt --tribunal --ssm

    # Domain expansion report
    python main.py --report
"""

import os
import sys
import json
import argparse
from pathlib import Path

from dotenv import load_dotenv
from context_builder import ContextBuilder
from tribunal_transversal import TribunalTransversal

load_dotenv()


def load_config(config_path: str = "config.json") -> dict:
    path = Path(config_path)
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {
        "anthropic": {
            "api_key": os.getenv("ANTHROPIC_API_KEY", ""),
            "model": os.getenv("DS_MODEL", "claude-opus-4-6"),
            "max_tokens": int(os.getenv("DS_MAX_TOKENS", "8192"))
        },
        "prompts_dir": os.getenv("DS_PROMPTS_DIR", "./prompts"),
        "tribunal": {
            "max_agents": 7,
            "max_calls_total": 40,
            "max_n2_per_n1": 3,
            "alert_at_percent": 80
        },
        "ssm": {
            "max_personas": 20,
            "max_rounds": 4,
            "max_parallel_personas": 5,
            "alert_at_percent": 80
        },
        "notifications": {
            "slack": {
                "enabled": os.getenv("SLACK_ENABLED", "false").lower() == "true",
                "webhook_url": os.getenv("SLACK_WEBHOOK_URL", ""),
                "channel": os.getenv("SLACK_CHANNEL", "#dark-strategist-alerts")
            },
            "github": {
                "enabled": os.getenv("GITHUB_ENABLED", "false").lower() == "true",
                "token": os.getenv("GITHUB_TOKEN", ""),
                "owner": os.getenv("GITHUB_OWNER", "JARPClaude"),
                "repo": os.getenv("GITHUB_REPO", "dark-strategist-agent")
            }
        },
        "logging": {
            "google_sheets": {
                "enabled": os.getenv("SHEETS_ENABLED", "false").lower() == "true",
                "credentials_file": os.getenv("SHEETS_CREDENTIALS", "credentials.json"),
                "spreadsheet_id": os.getenv("SHEETS_ID", ""),
                "sheet_name": os.getenv("SHEETS_NAME", "DomainExpansionLog")
            }
        }
    }


def print_report_mode(config: dict):
    from sheets_logger import SheetsLogger
    sheets_cfg = config["logging"]["google_sheets"]
    if sheets_cfg.get("enabled") and sheets_cfg.get("spreadsheet_id"):
        SheetsLogger(
            sheets_cfg["credentials_file"],
            sheets_cfg["spreadsheet_id"],
            sheets_cfg["sheet_name"]
        ).print_expansion_report()
    else:
        print("⚠️  Google Sheets not enabled.")


def calculate_tribunal_size(tribunal: bool, agents: int) -> tuple:
    """Returns (tribunal_size, tribunal_label)."""
    labels = {1: "SINGLE", 3: "TRIBUNAL_LIGHT", 5: "TRIBUNAL_FULL", 7: "TRIBUNAL_MAX"}
    if not tribunal:
        return 1, "SINGLE"
    if agents:
        return agents, labels.get(agents, "TRIBUNAL_FULL")
    return None, "AUTO"  # Auto-sized by Swarm Activation Score


def main():
    parser = argparse.ArgumentParser(
        description="Dark Strategist Agent v3.0.0 — Tribunal Transversal"
    )

    # Case-based args (v3.0 — recommended)
    parser.add_argument("--type", type=str,
                        help="Case type: contract | finance | trading | code | medical | etc.")
    parser.add_argument("--subscenario", type=str,
                        help="Specific subscenario: XAUUSD | alquiler | investment_review | etc.")
    parser.add_argument("--objective", type=str,
                        help="Analysis objective: 'identify risks' | 'buy sell or wait' | etc.")
    parser.add_argument("--regime", type=str, default="standard",
                        choices=["standard", "adversarial", "breakout",
                                 "crisis", "regulatory", "fast_track", "comparative"],
                        help="Analysis regime (default: standard)")

    # Document-based args (v2.x compatibility)
    parser.add_argument("--document", type=str,
                        help="Path to document file (v2.x compatibility mode)")

    # Tribunal args
    parser.add_argument("--tribunal", action="store_true",
                        help="Activate Tribunal Transversal")
    parser.add_argument("--agents", type=int, choices=[1, 3, 5, 7],
                        help="Force tribunal size (auto if omitted)")

    # SSM args
    parser.add_argument("--ssm", action="store_true",
                        help="Activate Simulación Social Masiva")
    parser.add_argument("--ssm-scale", type=str,
                        choices=["MICRO", "MESO", "MACRO"], default="MESO",
                        help="SSM scale: MICRO(5-10) / MESO(20) / MACRO(50)")

    # Utility args
    parser.add_argument("--config", type=str, default="config.json")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--report", action="store_true",
                        help="Print domain expansion report")

    args = parser.parse_args()
    config = load_config(args.config)

    if args.report:
        print_report_mode(config)
        return

    # Build case
    if args.type and args.subscenario and args.objective:
        # v3.0 case-based mode
        case = {
            "type": args.type,
            "subscenario": args.subscenario,
            "objective": args.objective,
            "regime": args.regime,
            "run_ssm": args.ssm,
            "ssm_scale": args.ssm_scale,
        }
        document = f"[Document type: {args.type} | Subscenario: {args.subscenario}]"
    elif args.document:
        # v2.x document-based compatibility
        doc_path = Path(args.document)
        if not doc_path.exists():
            print(f"❌ Document not found: {args.document}")
            sys.exit(1)
        document = doc_path.read_text(encoding="utf-8")
        # Auto-infer case from document
        case = {
            "type": "general",
            "subscenario": doc_path.stem,
            "objective": "identify risks and failure modes",
            "regime": args.regime,
            "run_ssm": args.ssm,
            "ssm_scale": args.ssm_scale,
        }
    else:
        parser.print_help()
        sys.exit(1)

    # Build runtime context
    builder = ContextBuilder()
    ctx = builder.build(case)

    # Set tribunal size
    tribunal_size, tribunal_label = calculate_tribunal_size(args.tribunal, args.agents)
    if tribunal_size:
        ctx.tribunal_size = tribunal_size
    ctx.tribunal_label = tribunal_label

    if args.verbose:
        print(builder.describe(ctx))

    # Print header
    mode_label = tribunal_label if args.tribunal else "SINGLE"
    ssm_label = f" + SSM ({args.ssm_scale})" if args.ssm else ""
    print(f"\n{'='*60}")
    print(f"DARK STRATEGIST v3.0.0 — Tribunal Transversal")
    print(f"Domain: {ctx.domain} | Regime: {ctx.regime}")
    print(f"Mode: {mode_label}{ssm_label}")
    print(f"{'='*60}\n")

    # Run Tribunal Transversal
    tt = TribunalTransversal(config)
    result = tt.run(document=document, ctx=ctx)

    # Output
    print(result["final_verdict_text"])
    if result.get("ssm_report"):
        print(result["ssm_report"])
    print(result["transparency_report"])

    if args.verbose:
        tt.budget.print_summary()

    print(f"\n[Session: {result['session_id']} | "
          f"Duration: {result['duration_seconds']}s | "
          f"Domain: {result['domain']}]\n")


if __name__ == "__main__":
    main()
