"""
Dark Strategist Agent — Main Orchestrator
Pipeline: Router → Prompt Selection → Audit → Notifications → Logging
Version: 2.7.0

Usage:
    python main.py --document path/to/document.txt
    python main.py --document path/to/document.txt --config config.json --verbose
    python main.py --report
"""

import os
import sys
import json
import time
import uuid
import argparse
from pathlib import Path
from datetime import datetime

import anthropic
from dotenv import load_dotenv

from router import DomainRouter
from notifier import SlackNotifier, GitHubNotifier
from sheets_logger import SheetsLogger

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


def run_audit(system_prompt: str, document: str, config: dict) -> str:
    client = anthropic.Anthropic(api_key=config["anthropic"]["api_key"])
    response = client.messages.create(
        model=config["anthropic"]["model"],
        max_tokens=config["anthropic"]["max_tokens"],
        system=system_prompt,
        messages=[{"role": "user", "content": f"Audit the following document:\n\n{document}"}]
    )
    return response.content[0].text


def extract_verdict(text: str) -> str:
    for v in ["INVIABLE", "VIABLE WITH CRITICAL CORRECTIONS", "VIABLE WITH ADJUSTMENTS",
              "SOLID UNDER PRESSURE", "DO NOT DEPLOY", "DEPLOY TO DEMO ONLY",
              "DO NOT EXECUTE", "EXECUTE WITH CRITICAL REVISIONS"]:
        if v in text.upper():
            return v
    return "VERDICT_NOT_EXTRACTED"


def dispatch_notifications(routing: dict, config: dict) -> tuple:
    slack_sent, github_sent = False, False
    if not routing.get("is_unknown"):
        return slack_sent, github_sent
    slack_cfg = config["notifications"]["slack"]
    if slack_cfg.get("enabled") and slack_cfg.get("webhook_url"):
        slack_sent = SlackNotifier(slack_cfg["webhook_url"], slack_cfg["channel"]).send_domain_expansion(routing)
    github_cfg = config["notifications"]["github"]
    if github_cfg.get("enabled") and github_cfg.get("token"):
        github_sent = GitHubNotifier(github_cfg["token"], github_cfg["owner"], github_cfg["repo"]).create_domain_expansion_issue(routing)
    return slack_sent, github_sent


def log_to_sheets(routing, verdict, slack_sent, github_sent, duration, config):
    sheets_cfg = config["logging"]["google_sheets"]
    if not sheets_cfg.get("enabled") or not sheets_cfg.get("spreadsheet_id"):
        return
    try:
        SheetsLogger(sheets_cfg["credentials_file"], sheets_cfg["spreadsheet_id"],
                     sheets_cfg["sheet_name"]).log_execution(routing, verdict, slack_sent, github_sent, duration)
    except Exception as e:
        print(f"⚠️  Sheets skipped: {e}")


def main():
    parser = argparse.ArgumentParser(description="Dark Strategist Agent — Orchestrator v2.7.0")
    parser.add_argument("--document", type=str, help="Path to document")
    parser.add_argument("--config", type=str, default="config.json")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--report", action="store_true", help="Print domain expansion report")
    args = parser.parse_args()

    config = load_config(args.config)

    if args.report:
        sheets_cfg = config["logging"]["google_sheets"]
        if sheets_cfg.get("enabled"):
            SheetsLogger(sheets_cfg["credentials_file"], sheets_cfg["spreadsheet_id"],
                         sheets_cfg["sheet_name"]).print_expansion_report()
        else:
            print("⚠️  Google Sheets not enabled.")
        return

    if not args.document:
        parser.print_help()
        sys.exit(1)

    start_time = time.time()
    session_id = str(uuid.uuid4())[:8].upper()

    print(f"\n{'='*60}\nDARK STRATEGIST AGENT v2.7.0 — Session {session_id}\n{'='*60}\n")

    document = Path(args.document).read_text(encoding="utf-8")

    print("🔍 Detecting domain...")
    router = DomainRouter(config, config["prompts_dir"])
    routing = router.detect_domain(document)
    routing["session_id"] = session_id

    if args.verbose:
        router.print_routing_summary(routing)

    print(f"✅ Domain: {routing['domain']} | Prompt: {routing['prompt_file']} | Confidence: {routing['confidence']}")

    system_prompt = router.load_domain_prompt(routing)

    print(f"⚔️  Running forensic audit...")
    audit_output = run_audit(system_prompt, document, config)
    verdict = extract_verdict(audit_output)
    duration = time.time() - start_time

    print(f"\n{'='*60}\nFORENSIC AUDIT REPORT\n{'='*60}\n")
    print(audit_output)

    if routing.get("is_unknown"):
        print("\n⚠️  DOMAIN_EXPANSION_RECOMMENDED — dispatching notifications...")

    slack_sent, github_sent = dispatch_notifications(routing, config)
    log_to_sheets(routing, verdict, slack_sent, github_sent, duration, config)

    print(f"\n{'='*60}\nSession {session_id} complete in {duration:.1f}s | Verdict: {verdict}\n{'='*60}\n")


if __name__ == "__main__":
    main()
