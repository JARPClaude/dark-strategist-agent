"""
Dark Strategist Agent — Sheets Logger
Logs executions and DOMAIN_EXPANSION_RECOMMENDED to Google Sheets.
Version: 2.7.0
"""

from datetime import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

HEADERS = [
    "Timestamp", "Session ID", "Domain Detected", "Prompt Used",
    "Confidence", "Is Unknown Domain", "Domain Expansion Recommended",
    "Key Verification Points", "Suggested New Prompt",
    "Notification Sent (Slack)", "Notification Sent (GitHub)",
    "Audit Verdict", "Execution Duration (s)"
]


class SheetsLogger:
    def __init__(self, credentials_file: str, spreadsheet_id: str, sheet_name: str):
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = sheet_name
        self.service = self._build_service(credentials_file)
        self._ensure_headers()

    def _build_service(self, credentials_file: str):
        creds = Credentials.from_service_account_file(credentials_file, scopes=SCOPES)
        return build("sheets", "v4", credentials=creds)

    def _ensure_headers(self):
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=f"{self.sheet_name}!A1:Z1"
            ).execute()
            if not result.get("values"):
                self.service.spreadsheets().values().update(
                    spreadsheetId=self.spreadsheet_id,
                    range=f"{self.sheet_name}!A1",
                    valueInputOption="RAW",
                    body={"values": [HEADERS]}
                ).execute()
                print("✅ Sheet headers initialized")
        except Exception as e:
            print(f"⚠️  Headers check failed: {e}")

    def log_execution(self, routing: dict, verdict: str = "",
                      slack_sent: bool = False, github_sent: bool = False,
                      duration_seconds: float = 0.0):
        domain = routing.get("domain", "Unknown")
        key_points = routing.get("key_verification_points", [])
        suggested_file = f"system_prompt_{domain.lower().replace(' ', '_')}.md"

        row = [
            routing.get("timestamp", datetime.utcnow().isoformat()),
            routing.get("session_id", ""),
            domain,
            routing.get("prompt_file", ""),
            routing.get("confidence", ""),
            "YES" if routing.get("is_unknown") else "NO",
            "YES" if routing.get("is_unknown") else "NO",
            " | ".join(key_points),
            suggested_file if routing.get("is_unknown") else "",
            "YES" if slack_sent else "NO",
            "YES" if github_sent else "NO",
            verdict,
            str(round(duration_seconds, 2))
        ]

        try:
            self.service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range=f"{self.sheet_name}!A:M",
                valueInputOption="RAW",
                insertDataOption="INSERT_ROWS",
                body={"values": [row]}
            ).execute()
            print("✅ Execution logged to Google Sheets")
        except Exception as e:
            print(f"⚠️  Sheets logging failed: {e}")

    def print_expansion_report(self):
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=f"{self.sheet_name}!A:M"
            ).execute()
            rows = result.get("values", [])
            if len(rows) < 2:
                print("No DOMAIN_EXPANSION_RECOMMENDED events found.")
                return
            headers = rows[0]
            data = rows[1:]
            expansions = []
            for row in data:
                d = dict(zip(headers, row + [""] * (len(headers) - len(row))))
                if d.get("Domain Expansion Recommended") == "YES":
                    expansions.append(d)
            if not expansions:
                print("No expansion events found.")
                return
            domain_counts = {}
            for row in expansions:
                domain = row.get("Domain Detected", "Unknown")
                domain_counts[domain] = domain_counts.get(domain, 0) + 1
            print(f"\n{'='*60}\nDOMAIN EXPANSION REPORT — Dark Strategist v2.7.0\n{'='*60}")
            print(f"Total events: {len(expansions)}\n")
            for domain, count in sorted(domain_counts.items(), key=lambda x: -x[1]):
                suggested = f"system_prompt_{domain.lower().replace(' ', '_')}.md"
                print(f"  {count:3}x  {domain:<25}  → {suggested}")
            print("="*60)
        except Exception as e:
            print(f"⚠️  Could not fetch report: {e}")
