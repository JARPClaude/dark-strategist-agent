<#
  Dark Strategist v3.9.0 — release-doc finalizer (ASCII-safe, PS 5.1 proof).
  Source is pure ASCII; all non-ASCII (em-dash, check, section, box, arrow) is built
  at RUNTIME via [char] codes via Ex(), so PowerShell's ANSI script-reading cannot
  corrupt search strings. Per-EDIT application with idempotent GUARDS (re-running is
  safe). Dry-run default; -Apply writes.

  Run:  powershell -ExecutionPolicy Bypass -File .\finalize_v3_9_0.ps1
        powershell -ExecutionPolicy Bypass -File .\finalize_v3_9_0.ps1 -Apply
#>
param([switch]$Apply)
$ErrorActionPreference = "Stop"

$DS = "C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent"
$TK = "C:\Users\jrodr\OneDrive\Documentos 1\GitHub\jarp-toolkit"
$enc = New-Object System.Text.UTF8Encoding($false)

# runtime token expansion: keeps the .ps1 source ASCII-only.
function Ex([string]$s) {
    $s.Replace('<<EM>>',  [string][char]0x2014).
       Replace('<<OK>>',  [string][char]0x2705).
       Replace('<<SEC>>', [string][char]0x00A7).
       Replace('<<V>>',   [string][char]0x2502).
       Replace('<<T>>',   [string][char]0x251C).
       Replace('<<H>>',   [string][char]0x2500).
       Replace('<<LA>>',  [string][char]0x2190)
}

$files = [ordered]@{}
function Add-Edit([string]$path,[string]$label,[string]$old,[string]$new,[string]$guard) {
    if (-not $script:files.Contains($path)) { $script:files[$path] = @() }
    $script:files[$path] += [pscustomobject]@{
        Label = $label; Old = (Ex $old); New = (Ex $new); Guard = (Ex $guard)
    }
}

# --- CHANGELOG.md ---
$old = @'
## [3.8.0] <<EM>> 2026-06-03
'@
$new = @'
## [3.9.0] <<EM>> 2026-06-03

### Added <<EM>> Interactive Wizard CLI (roadmap v3.9.0)
- New `orchestrator/wizard.py`: guided interactive flag builder for non-technical operators (closes the KIMI/Copilot gap). Pure `build_command(answers)` (deterministic, unit-tested) + `run_wizard()` (the only I/O). Walks domain (20) -> canonical `--type` token, Legal sub-area drill-down (L01-L12), subscenario, objective, regime (7), Tribunal (auto/1/3/5/7), SSM (MICRO/MESO/MACRO). Emits the equivalent `python main.py ...` command and offers to run it.
- `main.py`: new `--wizard` flag. The wizard SYNTHESIZES argv and re-parses it through the SAME argparse parser, so the guided path is byte-for-byte equivalent to manual flags. No existing path altered.
- New `orchestrator/test_wizard.py`: 5-case unit suite over `build_command`.

### Fixed <<EM>> D-v38-01 (LATENT carried from the v3.8.0 cert)
- `orchestrator/retriever.py`: `build_agent_context` default `doc_top_k` aligned 5 -> 6 to match config/orchestrator (config was authoritative; the "next retriever touch" the v3.8.0 cert flagged). `query(top_k=5)` left untouched (out of scope). Module docstring left at v3.8.0 (content-based).

### Versioning
- Atomic <<SEC>>4.14.1 bump: base + router + 19 domain variants + README + CLAUDE product-face -> v3.9.0 (23 files, 69 stamp lines). No prompt/skill CONTENT changed; no roster/verdict-logic change. Skills 6, domains 20 (unchanged).

### Non-forensic guarantee
- v3.9.0 touches the orchestrator product-face only. The forensic surface (19 variants + 6 skills + base + router CONTENT) is byte-identical except version stamps.

### JARP_CERTIFIED: DS v3.9.0 <<EM>> PA-20260603-004 <<OK>>

Level 1 <<EM>> JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.9.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.8.0 baseline (19/19 unchanged). Scope: v3.9.0 delta <<EM>> `wizard.py` (NEW), `test_wizard.py` (NEW), `main.py --wizard`, `retriever.py` doc_top_k alignment (D-v38-01), atomic <<SEC>>4.14.1 stamp barrido. RULE 08 self-audit L0 (PA-20260603-003) PASS first. Functional evidence: `test_wizard.py` 5/5 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, needs live key <<EM>> non-blocking) + interactive wizard flow validated live (correct argv, re-parse parity). Three doc-consistency findings caught and resolved pre-cert <<EM>> D-v39-01 (MODERATE, CLAUDE.md bottom status `ACTIVE <<EM>> v3.8.0` not caught by the anchored stamp pass) + D-v39-02 (MODERATE, CLAUDE.md repo tree missing wizard.py/test_wizard.py) + D-v39-03 (LATENT, README+CLAUDE roadmap tables missing the v3.9.0 row). Prior LATENT D-v38-01 CLOSED. Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT -> `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS`. Non-forensic bump. Supersedes PA-20260603-002 (DS v3.8.0). `JARP_BENCHMARK_LIVE` advances to v3.9.0. Valid until 30/08/2026 or DS v4.0.0.

---

## [3.8.0] <<EM>> 2026-06-03
'@
Add-Edit "$DS\CHANGELOG.md" "CHANGELOG [3.9.0]+cert" $old $new '## [3.9.0] <<EM>> 2026-06-03'

# --- CLAUDE.md ---
Add-Edit "$DS\CLAUDE.md" "C1 status drift" '**ACTIVE <<EM>> v3.8.0**' '**ACTIVE <<EM>> v3.9.0**' '**ACTIVE <<EM>> v3.9.0**'

$old = @'
<<V>>   <<T>><<H>><<H>> main.py
'@
$new = @'
<<V>>   <<T>><<H>><<H>> main.py
<<V>>   <<T>><<H>><<H>> wizard.py                   <<LA>> NEW v3.9.0 (interactive CLI)
<<V>>   <<T>><<H>><<H>> test_wizard.py              <<LA>> NEW v3.9.0 (wizard unit)
'@
Add-Edit "$DS\CLAUDE.md" "C2 repo tree" $old $new 'wizard.py                   <<LA>> NEW v3.9.0'

$old = @'
| v3.8.0 RAG retrieval at doc-feed layer <<EM>> BM25 R1 intra-document + R2 jurisdictional corpus, non-breaking [:N] fallback | <<OK>> |
'@
$new = @'
| v3.8.0 RAG retrieval at doc-feed layer <<EM>> BM25 R1 intra-document + R2 jurisdictional corpus, non-breaking [:N] fallback | <<OK>> |
| v3.9.0 Interactive Wizard CLI (guided flag builder, synthesizes argv into the same parser) + doc_top_k align (D-v38-01) | <<OK>> |
'@
Add-Edit "$DS\CLAUDE.md" "C3 roadmap row" $old $new '| v3.9.0 Interactive Wizard CLI (guided flag builder, synthesizes argv'

# --- README.md ---
$old = @'
| v3.8.0 | RAG retrieval at document-feed layer <<EM>> BM25 (R1 intra-document relevance replaces blind doc_window truncation; R2 optional jurisdictional corpus), non-breaking [:N] fallback | <<OK>> |
'@
$new = @'
| v3.8.0 | RAG retrieval at document-feed layer <<EM>> BM25 (R1 intra-document relevance replaces blind doc_window truncation; R2 optional jurisdictional corpus), non-breaking [:N] fallback | <<OK>> |
| v3.9.0 | Interactive Wizard CLI <<EM>> guided flag builder (synthesizes argv into the same parser); doc_top_k align (D-v38-01) | <<OK>> |
'@
Add-Edit "$DS\README.md" "README roadmap row" $old $new '| v3.9.0 | Interactive Wizard CLI <<EM>> guided flag builder'

# --- JARP_TOOLKIT.md ---
Add-Edit "$TK\JARP_TOOLKIT.md" "T1 header" `
'# Last updated: 03/06/2026 (session 22) <<EM>> DS v3.8.0 JARP_CERTIFIED (PA-20260603-002, RAG document-feed retrieval BM25, 0/0/0/1-LATENT, supersedes PA-20260602-002). Prior: 02/06/2026 (session 21) <<EM>> DS v3.7.0 (PA-20260602-002, context-degradation lens).' `
'# Last updated: 03/06/2026 (session 23) <<EM>> DS v3.9.0 JARP_CERTIFIED (PA-20260603-004, Interactive Wizard CLI + doc_top_k D-v38-01 fix, non-forensic, 0/0/0/0, supersedes PA-20260603-002). Prior: 03/06/2026 (session 22) <<EM>> DS v3.8.0 (PA-20260603-002, RAG document-feed BM25).' `
'(session 23) <<EM>> DS v3.9.0 JARP_CERTIFIED (PA-20260603-004'

Add-Edit "$TK\JARP_TOOLKIT.md" "T2 #30 Version" `
'**Version:** 3.8.0 <<EM>> JARP_CERTIFIED <<OK>> (PA-20260603-002, delta over v3.7.0 baseline 19/19)' `
'**Version:** 3.9.0 <<EM>> JARP_CERTIFIED <<OK>> (PA-20260603-004, Interactive Wizard CLI + doc_top_k align, non-forensic)' `
'**Version:** 3.9.0 <<EM>> JARP_CERTIFIED <<OK>> (PA-20260603-004, Interactive Wizard'

Add-Edit "$TK\JARP_TOOLKIT.md" "T3 #30 CERT STATUS" `
'**CERT STATUS:** repo at v3.8.0 <<EM>> **JARP_CERTIFIED** <<OK>> `PA-20260603-002` (issued 2026-06-03, valid until 2026-08-30 or DS v4.0.0, auditor PA-agent v1.3.0 <<EM>> delta over v3.7.0 baseline 19/19, 0/0/0/1-LATENT D-v38-01 accepted, BIAS_CHECK PASS) certifies **v3.8.0** (RAG document-feed retrieval, BM25). Supersedes PA-20260602-002. JARP_BENCHMARK_LIVE = v3.8.0.' `
'**CERT STATUS:** repo at v3.9.0 <<EM>> **JARP_CERTIFIED** <<OK>> `PA-20260603-004` (issued 2026-06-03, valid until 2026-08-30 or DS v4.0.0, auditor PA-agent v1.3.0 <<EM>> delta over v3.8.0 baseline 19/19, 0/0/0/0, prior LATENT D-v38-01 CLOSED, BIAS_CHECK PASS) certifies **v3.9.0** (Interactive Wizard CLI + doc_top_k align; non-forensic <<EM>> orchestrator product-face only). Supersedes PA-20260603-002. JARP_BENCHMARK_LIVE = v3.9.0.' `
'certifies **v3.9.0** (Interactive Wizard CLI + doc_top_k align'

Add-Edit "$TK\JARP_TOOLKIT.md" "T4 #30 prev certs" `
'**Previous certs (SUPERSEDED):** v3.7.0 <<EM>> PA-20260602-002 (closed at v3.8.0 re-cert);' `
'**Previous certs (SUPERSEDED):** v3.8.0 <<EM>> PA-20260603-002 (closed at v3.9.0 re-cert); v3.7.0 <<EM>> PA-20260602-002 (closed at v3.8.0 re-cert);' `
'v3.8.0 <<EM>> PA-20260603-002 (closed at v3.9.0 re-cert);'

Add-Edit "$TK\JARP_TOOLKIT.md" "T5 Note #16" `
'16. **dark-strategist-agent REPORT_ID** <<EM>> Format `DS-AAAAMMDD-NNN`. Current version: **v3.8.0 <<EM>> JARP_CERTIFIED** (`PA-20260603-002`, delta over v3.7.0 baseline 19/19, 0/0/0/1-LATENT, supersedes PA-20260602-002) <<EM>> MIT Open Source. Default model: `claude-opus-4-7`. <<SEC>>4.14.1 Domain Variant Contract governs all 19 domain variants. v3.8.0 landed RAG document-feed retrieval (BM25 embedded: R1 intra-document + R2 jurisdictional corpus empty; infinity/Docker rejected, zero-infra; RAG re-scoped <<EM>> ContextBuilder document-free, retrieval at feed layer). All TOP 7 incorporations now closed. Backlog: corpus R2 content curation + Wizard CLI (v3.9.0). v3.7.0 landed the context-degradation forensic lens; v3.6.0 the legal+finance matrix.' `
'16. **dark-strategist-agent REPORT_ID** <<EM>> Format `DS-AAAAMMDD-NNN`. Current version: **v3.9.0 <<EM>> JARP_CERTIFIED** (`PA-20260603-004`, delta over v3.8.0 baseline 19/19, 0/0/0/0, supersedes PA-20260603-002) <<EM>> MIT Open Source. Default model: `claude-opus-4-7`. <<SEC>>4.14.1 Domain Variant Contract governs all 19 domain variants. v3.9.0 landed the Interactive Wizard CLI (`orchestrator/wizard.py` + `main.py --wizard`; synthesizes argv into the same argparse parser) and closed D-v38-01 (retriever `doc_top_k` 5->6). Non-forensic bump (orchestrator product-face only). All TOP 7 incorporations closed. Backlog (sole remaining roadmap item): corpus R2 content curation (data, not code). v3.8.0 landed RAG document-feed retrieval (BM25; infinity/Docker rejected, zero-infra). v3.7.0 the context-degradation lens; v3.6.0 the legal+finance matrix.' `
'Current version: **v3.9.0 <<EM>> JARP_CERTIFIED** (`PA-20260603-004`'

# --- ENGINE ---
Write-Host ("=" * 64)
Write-Host "FINALIZE v3.9.0  (mode: $(if($Apply){'APPLY'}else{'DRY-RUN'}))"
Write-Host ("=" * 64)

$totApplied = 0; $totAlready = 0; $totFail = 0
foreach ($path in $files.Keys) {
    $leaf = Split-Path $path -Leaf
    if (-not (Test-Path $path)) { Write-Host "  [MISS] $leaf not found"; $totFail++; continue }
    $content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
    $working = $content
    foreach ($e in $files[$path]) {
        if ($working.Contains($e.Guard)) {
            Write-Host ("  [SKIP-DONE] {0} :: {1}" -f $leaf, $e.Label); $totAlready++
            continue
        }
        $hits = ([regex]::Matches($working, [regex]::Escape($e.Old))).Count
        if ($hits -eq 1) {
            $working = $working.Replace($e.Old, $e.New)
            Write-Host ("  [APPLY] {0} :: {1}" -f $leaf, $e.Label); $totApplied++
        } else {
            Write-Host ("  [FAIL]  {0} :: {1}  (anchor found {2}x, need 1)" -f $leaf, $e.Label, $hits)
            $totFail++
        }
    }
    if (($working -ne $content) -and $Apply) {
        [System.IO.File]::WriteAllText($path, $working, $enc)
        Write-Host ("  -> WRITTEN: {0}" -f $leaf)
    }
}

Write-Host ("=" * 64)
Write-Host ("APPLIED: {0}   ALREADY-DONE: {1}   FAILED: {2}   {3}" -f `
            $totApplied, $totAlready, $totFail, $(if($Apply){'(written)'}else{'(dry-run)'}))
Write-Host ("=" * 64)
if (-not $Apply) { Write-Host "Review above. Re-run with -Apply to write. Guards make re-runs idempotent." }
if ($totFail -gt 0) { Write-Host ("WARNING: {0} edit(s) failed anchor match. Paste those lines to me." -f $totFail) }
