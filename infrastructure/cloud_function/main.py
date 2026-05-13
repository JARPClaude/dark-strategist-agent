"""
Dark Strategist Agent — Google Cloud Function
HTTP endpoint for remote document auditing.
Version: 2.7.0

Deploy:
    gcloud functions deploy dark-strategist \
        --runtime python311 \
        --trigger-http \
        --allow-unauthenticated \
        --entry-point audit \
        --memory 512MB \
        --timeout 300s \
        --set-env-vars ANTHROPIC_API_KEY=your_key,...
"""

import os
import sys
import json
import uuid
import time
import functions_framework

sys.path.insert(0, os.path.dirname(__file__))

from router import DomainRouter
from notifier import SlackNotifier, GitHubNotifier
from sheets_logger import SheetsLogger
import anthropic as anthropic_lib


def get_config_from_env() -> dict:
    return {
        "anthropic": {
            "api_key": os.environ.get("ANTHROPIC_API_KEY", ""),
            "model": os.environ.get("DS_MODEL", "claude-opus-4-6"),
            "max_tokens": int(os.environ.get("DS_MAX_TOKENS", "8192"))
        },
        "prompts_dir": os.environ.get("DS_PROMPTS_DIR", "./prompts"),
        "notifications": {
            "slack": {
                "enabled": os.environ.get("SLACK_ENABLED", "false").lower() == "true",
                "webhook_url": os.environ.get("SLACK_WEBHOOK_URL", ""),
                "channel": os.environ.get("SLACK_CHANNEL", "#dark-strategist-alerts")
            },
            "github": {
                "enabled": os.environ.get("GITHUB_ENABLED", "false").lower() == "true",
                "token": os.environ.get("GITHUB_TOKEN", ""),
                "owner": os.environ.get("GITHUB_OWNER", "JARPClaude"),
                "repo": os.environ.get("GITHUB_REPO", "dark-strategist-agent")
            }
        },
        "logging": {
            "google_sheets": {
                "enabled": os.environ.get("SHEETS_ENABLED", "false").lower() == "true",
                "credentials_file": "/tmp/credentials.json",
                "spreadsheet_id": os.environ.get("SHEETS_ID", ""),
                "sheet_name": os.environ.get("SHEETS_NAME", "DomainExpansionLog")
            }
        }
    }


def run_audit_cf(system_prompt: str, document: str, config: dict) -> str:
    client = anthropic_lib.Anthropic(api_key=config["anthropic"]["api_key"])
    response = client.messages.create(
        model=config["anthropic"]["model"],
        max_tokens=config["anthropic"]["max_tokens"],
        system=system_prompt,
        messages=[{"role": "user", "content": f"Audit:\n\n{document}"}]
    )
    return response.content[0].text


def extract_verdict(text: str) -> str:
    for v in ["INVIABLE", "VIABLE WITH CRITICAL CORRECTIONS", "VIABLE WITH ADJUSTMENTS",
              "SOLID UNDER PRESSURE", "DO NOT DEPLOY", "DEPLOY TO DEMO ONLY"]:
        if v in text.upper():
            return v
    return "VERDICT_NOT_EXTRACTED"


@functions_framework.http
def audit(request):
    """
    POST {"document": "full text"}
    Returns JSON with routing, verdict, report, and domain expansion flag.
    """
    if request.method == "OPTIONS":
        return ("", 204, {"Access-Control-Allow-Origin": "*",
                          "Access-Control-Allow-Methods": "POST",
                          "Access-Control-Allow-Headers": "Content-Type"})

    headers = {"Access-Control-Allow-Origin": "*", "Content-Type": "application/json"}

    try:
        body = request.get_json(silent=True) or {}
        document = body.get("document", "").strip()
        if not document:
            return (json.dumps({"error": "Missing 'document' field"}), 400, headers)
    except Exception as e:
        return (json.dumps({"error": str(e)}), 400, headers)

    start_time = time.time()
    session_id = str(uuid.uuid4())[:8].upper()
    config = get_config_from_env()

    try:
        router = DomainRouter(config, config["prompts_dir"])
        routing = router.detect_domain(document)
        routing["session_id"] = session_id

        system_prompt = router.load_domain_prompt(routing)
        audit_output = run_audit_cf(system_prompt, document, config)
        verdict = extract_verdict(audit_output)
        duration = time.time() - start_time

        slack_sent, github_sent = False, False
        if routing.get("is_unknown"):
            slack_cfg = config["notifications"]["slack"]
            if slack_cfg.get("enabled") and slack_cfg.get("webhook_url"):
                slack_sent = SlackNotifier(slack_cfg["webhook_url"], slack_cfg["channel"]).send_domain_expansion(routing)
            github_cfg = config["notifications"]["github"]
            if github_cfg.get("enabled") and github_cfg.get("token"):
                github_sent = GitHubNotifier(github_cfg["token"], github_cfg["owner"], github_cfg["repo"]).create_domain_expansion_issue(routing)

        sheets_cfg = config["logging"]["google_sheets"]
        if sheets_cfg.get("enabled") and sheets_cfg.get("spreadsheet_id"):
            try:
                SheetsLogger(sheets_cfg["credentials_file"], sheets_cfg["spreadsheet_id"],
                             sheets_cfg["sheet_name"]).log_execution(routing, verdict, slack_sent, github_sent, duration)
            except Exception as e:
                print(f"Sheets skipped: {e}")

        return (json.dumps({
            "session_id": session_id,
            "domain": routing["domain"],
            "prompt_used": routing["prompt_file"],
            "confidence": routing["confidence"],
            "is_unknown_domain": routing.get("is_unknown", False),
            "verdict": verdict,
            "report": audit_output,
            "domain_expansion_recommended": routing.get("is_unknown", False),
            "key_verification_points": routing.get("key_verification_points", []),
            "duration_seconds": round(duration, 2)
        }, ensure_ascii=False), 200, headers)

    except Exception as e:
        return (json.dumps({"error": str(e), "session_id": session_id}), 500, headers)
