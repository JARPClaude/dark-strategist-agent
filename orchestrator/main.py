"""
Dark Strategist Agent — Main Orchestrator
Version: 2.8.0

Usage:
    # Single mode (default)
    python main.py --document path/to/doc.txt

    # Tribunal mode (auto-size via Swarm Activation Score)
    python main.py --document path/to/doc.txt --tribunal

    # Tribunal mode (forced size)
    python main.py --document path/to/doc.txt --tribunal --agents 5

    # Domain expansion report
    python main.py --report
"""

import os
import sys
import json
import time
import uuid
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
    """Prints domain expansion report from Google Sheets."""
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
        description="Dark Strategist Agent v2.8.0 — Agente Forense Orquestador"
    )
    parser.add_argument("--document", type=str, help="Path to document to audit")
    parser.add_argument("--config", type=str, default="config.json")
    parser.add_argument("--tribunal", action="store_true",
                        help="Activate Tribunal Adversarial mode")
    parser.add_argument("--agents", type=int, choices=[1, 3, 5, 7],
                        help="Force tribunal size (1/3/5/7). Auto-calculated if omitted.")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--report", action="store_true",
                        help="Print domain expansion report")
    args = parser.parse_args()

    config = load_config(args.config)

    if args.report:
        print_report_mode(config)
        return

    if not args.document:
        parser.print_help()
        sys.exit(1)

    document = Path(args.document).read_text(encoding="utf-8")

    # Forced size: only in tribunal mode
    forced_size = None
    if args.tribunal and args.agents:
        forced_size = args.agents
    elif not args.tribunal:
        forced_size = 1  # Single mode

    print(f"\n{'='*60}")
    print(f"DARK STRATEGIST AGENT v2.8.0")
    mode_label = "TRIBUNAL" if args.tribunal else "SINGLE"
    print(f"Mode: {mode_label} | Agents: {forced_size or 'AUTO'}")
    print(f"{'='*60}\n")

    afo = AgenteForenseOrquestador(config, config["prompts_dir"])
    result = afo.run(document, forced_tribunal_size=forced_size)

    print(f"\n{'='*60}")
    print("VEREDICTO FORENSE UNIFICADO")
    print(f"{'='*60}\n")
    print(result["final_verdict"])

    if args.verbose:
        afo.budget.print_summary()

    print(f"\n{'='*60}")
    print(f"Session: {result['session_id']}")
    print(f"Domain:  {result['domain']}")
    print(f"Mode:    {result['tribunal_mode']}")
    print(f"Agents:  {result['agents_deployed']}")
    print(f"Time:    {result['duration_seconds']}s")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
