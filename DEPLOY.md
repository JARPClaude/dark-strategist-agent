# Dark Strategist Agent v2.7.0 — Deployment Guide

## Architecture

```
Document → Cloud Function → Router Agent → Domain Prompt → Audit
                                ↓ (unknown domain)
                    Slack + GitHub Issues + Google Sheets
```

---

## Step 1 — Local Setup

```bash
cd orchestrator
pip install -r requirements.txt
cp config.example.json config.json
# Fill in ANTHROPIC_API_KEY and optional integrations
python main.py --document path/to/document.txt --verbose
```

---

## Step 2 — Google Sheets (Opción D)

1. Create Google Sheet named `DomainExpansionLog`
2. Enable Google Sheets API in Google Cloud Console
3. Create Service Account → Download credentials JSON
4. Share sheet with service account email
5. Update `config.json` with `spreadsheet_id`

View expansion report:
```bash
python main.py --report
```

---

## Step 3 — Slack Webhook (Opción C)

1. Slack workspace → Apps → Incoming Webhooks
2. Create webhook for `#dark-strategist-alerts`
3. Update `config.json` with `webhook_url`

---

## Step 4 — GitHub Issues (Opción C)

1. GitHub → Settings → Developer Settings → Personal Access Tokens
2. Create token with `repo` scope for `JARPClaude/dark-strategist-agent`
3. Update `config.json` with `token`

---

## Step 5 — Google Cloud Function (Production)

```bash
cd infrastructure/cloud_function

# Copy required files
cp ../../orchestrator/router.py .
cp ../../orchestrator/notifier.py .
cp ../../orchestrator/sheets_logger.py .
cp -r ../../prompts ./prompts

gcloud functions deploy dark-strategist \
    --runtime python311 \
    --trigger-http \
    --allow-unauthenticated \
    --entry-point audit \
    --memory 512MB \
    --timeout 300s \
    --region us-central1 \
    --set-env-vars \
        ANTHROPIC_API_KEY=your_key,\
        SLACK_ENABLED=true,\
        SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...,\
        GITHUB_ENABLED=true,\
        GITHUB_TOKEN=ghp_...,\
        SHEETS_ENABLED=true,\
        SHEETS_ID=your_sheet_id
```

Test:
```bash
curl -X POST https://us-central1-YOUR_PROJECT.cloudfunctions.net/dark-strategist \
    -H "Content-Type: application/json" \
    -d '{"document": "Your document text here"}'
```

---

## Step 6 — Looker Studio Dashboard (Opción D)

1. lookerstudio.google.com → Create Report
2. Data source: Google Sheets → `DomainExpansionLog`
3. Build: Bar chart (domain frequency), Time series (executions/day),
   Table (unknown domains + key points), Scorecard (total expansions)

---

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ANTHROPIC_API_KEY` | Claude API key | ✅ |
| `DS_MODEL` | Model (default: claude-opus-4-6) | Optional |
| `SLACK_ENABLED` | Enable Slack | Optional |
| `SLACK_WEBHOOK_URL` | Slack webhook URL | If Slack |
| `GITHUB_ENABLED` | Enable GitHub Issues | Optional |
| `GITHUB_TOKEN` | GitHub PAT (repo scope) | If GitHub |
| `SHEETS_ENABLED` | Enable Sheets logging | Optional |
| `SHEETS_ID` | Spreadsheet ID | If Sheets |

---

## Cost Estimate

| Component | Cost |
|-----------|------|
| Google Cloud Functions | ~$0 (2M req/month free) |
| Google Sheets API | $0 |
| Slack / GitHub | $0 |
| Claude API | ~$0.015 per audit |

**Infrastructure: ~$0. Only pay for Claude API tokens.**
