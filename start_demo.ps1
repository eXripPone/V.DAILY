$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
$runtimeCandidate = Join-Path $env:USERPROFILE '.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
if (Test-Path -LiteralPath $runtimeCandidate) {
    & $runtimeCandidate -m app.server --demo
} else {
    python -m app.server --demo
}
