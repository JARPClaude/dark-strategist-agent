<#
.SYNOPSIS
  Dark Strategist - atomic version-stamp bump (§4.14.1).
  Bumps version stamps across base + router + 19 domain variants + README + CLAUDE,
  WITHOUT touching prose/content. CHANGELOG is intentionally excluded (history is immutable).

.DESCRIPTION
  Targeted, line-anchored replacement: only lines carrying a real version stamp
  (PROTOCOL_STATUS / BASE_PROTOCOL / CATALOG_VERSION / Version: / -ROUTER / ARCHITECTURAL LAYERS /
  version badge) get OldVersion -> NewVersion. Everything else is left byte-for-byte.
  Dry-run by default; pass -Apply to write. Reusable for future bumps via -OldVersion/-NewVersion.

.EXAMPLE
  # 1) Preview (no writes):
  powershell -ExecutionPolicy Bypass -File .\bump_stamps.ps1
  # 2) Apply after reviewing the preview:
  powershell -ExecutionPolicy Bypass -File .\bump_stamps.ps1 -Apply
#>
param(
    [string]$RepoRoot   = "C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent",
    [string]$OldVersion = "3.8.0",
    [string]$NewVersion = "3.9.0",
    [switch]$Apply
)

#--- Anchors: a line is eligible ONLY if it contains one of these markers.
$anchors = @(
    'PROTOCOL_STATUS',
    'BASE_PROTOCOL',
    'CATALOG_VERSION',
    '-ROUTER',
    'ARCHITECTURAL LAYERS',
    'Version:',
    'version:',
    'VERSION'
)

#--- Scope: prompts/*.md + README.md + CLAUDE.md. CHANGELOG.md excluded by design.
$targets = @()
$targets += Get-ChildItem -Path (Join-Path $RepoRoot 'prompts') -Filter '*.md' -File -ErrorAction SilentlyContinue
foreach ($f in @('README.md','CLAUDE.md')) {
    $p = Join-Path $RepoRoot $f
    if (Test-Path $p) { $targets += Get-Item $p }
}

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$totalChanges = 0
$filesTouched = 0

Write-Host ("=" * 64)
Write-Host "STAMP BUMP  $OldVersion -> $NewVersion   (mode: $(if($Apply){'APPLY'}else{'DRY-RUN'}))"
Write-Host ("=" * 64)

foreach ($file in $targets) {
    if ($file.Name -eq 'CHANGELOG.md') { continue }
    $lines = [System.IO.File]::ReadAllLines($file.FullName)
    $fileChanges = 0
    for ($i = 0; $i -lt $lines.Length; $i++) {
        $line = $lines[$i]
        if (($line -match [regex]::Escape($OldVersion)) -and
            ($anchors | Where-Object { $line -like "*$_*" }).Count -gt 0) {
            $newLine = $line -replace [regex]::Escape($OldVersion), $NewVersion
            if ($newLine -ne $line) {
                Write-Host ("  {0}:{1}" -f $file.Name, ($i + 1))
                Write-Host ("    - {0}" -f $line.Trim())
                Write-Host ("    + {0}" -f $newLine.Trim())
                $lines[$i] = $newLine
                $fileChanges++
            }
        }
    }
    if ($fileChanges -gt 0) {
        $filesTouched++
        $totalChanges += $fileChanges
        if ($Apply) {
            [System.IO.File]::WriteAllLines($file.FullName, $lines, $utf8NoBom)
        }
    }
}

Write-Host ("=" * 64)
Write-Host ("FILES: {0}   STAMP LINES: {1}   {2}" -f $filesTouched, $totalChanges,
            $(if($Apply){'WRITTEN'}else{'(dry-run, nothing written)'}))
Write-Host ("=" * 64)
if (-not $Apply) { Write-Host "Review above. Re-run with -Apply to write." }
