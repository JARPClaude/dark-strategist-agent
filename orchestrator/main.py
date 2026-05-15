"""
Dark Strategist Agent — Main Orchestrator
Version: 2.9.0

Usage:
    # Single mode
    python main.py --document doc.txt

    # Tribunal auto-size
    python main.py --document doc.txt --tribunal

    # Tribunal forced size
    python main.py --document doc.txt --tribunal --agents 5

    # Tribunal + SSM auto-scale
    python main.py --document doc.txt --tribunal --ssm

    # Tribunal + SSM forced scale
    python main.py --document doc.txt --tribunal --ssm --ssm-scale MACRO

    # Domain expansion report
    python main.py --report
"""

import os
import sys
import json
import argparse
from pathlib import Path

from dotenv import load_dotenv
from tribunal import AgenteForenseOrquestador

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
            "max_calls_total": 30,
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
        print("⚠️  Google Sheets not enabled in config.")


def main():
    parser = argparse.ArgumentParser(
        description="Dark Strategist Agent v2.9.0 — Agente Forense Orquestador"
    )
    parser.add_argument("--document", type=str, help="Path to document to audit")
    parser.add_argument("--config", type=str, default="config.json")
    parser.add_argument("--tribunal", action="store_true",
                        help="Activate Tribunal Adversarial mode")
    parser.add_argument("--agents", type=int, choices=[1, 3, 5, 7],
                        help="Force tribunal size (1/3/5/7). Auto if omitted.")
    parser.add_argument("--ssm", action="store_true",
                        help="Activate Simulación Social Masiva")
    parser.add_argument("--ssm-scale", type=str,
                        choices=["MICRO", "MESO", "MACRO"], default="MESO",
                        help="SSM scale: MICRO(5-10) / MESO(20) / MACRO(50)")
    parser.add_argument("--verbose", action="store_true",
                        help="Show full transparency report")
    parser.add_argument("--report", action="store_true",
                        help="Print domain expansion report from Sheets")
    args = parser.parse_args()

    config = load_config(args.config)

    if args.report:
        print_report_mode(config)
        return

    if not args.document:
        parser.print_help()
        sys.exit(1)

    document = Path(args.document).read_text(encoding="utf-8")

    # Determine forced size
    forced_size = None
    if not args.tribunal:
        forced_size = 1  # Single mode
    elif args.agents:
        forced_size = args.agents  # Forced tribunal size

    # Print header
    mode_label = "SINGLE" if forced_size == 1 else "TRIBUNAL"
    ssm_label = f" + SSM ({args.ssm_scale})" if args.ssm else ""
    print(f"\n{'='*60}")
    print(f"DARK STRATEGIST AGENT v2.9.0")
    print(f"Mode: {mode_label}{ssm_label} | Agents: {forced_size or 'AUTO'}")
    print(f"{'='*60}\n")

    # Run AFO
    afo = AgenteForenseOrquestador(config, config["prompts_dir"])
    result = afo.run(
        document=document,
        forced_tribunal_size=forced_size,
        run_ssm=args.ssm,
        ssm_scale=args.ssm_scale
    )

    # Print outputs
    print(f"\n{'='*60}")
    print("VEREDICTO FORENSE UNIFICADO")
    print(f"{'='*60}\n")
    print(result["final_verdict"])

    if result.get("ssm_report"):
        print(result["ssm_report"])

    print(result["transparency_report"])

    if args.verbose:
        afo.budget.print_summary()

    print(f"\n{'='*60}")
    print(f"Session:  {result['session_id']}")
    print(f"Domain:   {result['domain']}")
    print(f"Tribunal: {result['tribunal_mode']}")
    print(f"Agents:   {result['agents_deployed']}")
    print(f"Duration: {result['duration_seconds']}s")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
