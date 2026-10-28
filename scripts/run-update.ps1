# 주 1회(월요일 새벽 3시 KST) 이 PC 의 작업 스케줄러가 실행한다.
# CPAAD 가 해외(GitHub 서버) 접속을 막아서 GitHub Actions 대신 여기서 수집해 push 한다.
$ErrorActionPreference = 'Continue'
Set-Location (Join-Path $PSScriptRoot '..')
$log = Join-Path $PSScriptRoot 'update.log'
function Log($m) { "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') $m" | Add-Content -Path $log -Encoding utf8 }
$py = 'C:\miniconda3\python.exe'
Log '시작'
& $py -X utf8 scripts/update.py 2>&1 | ForEach-Object { Log "$_" }
if ($LASTEXITCODE -ne 0) { Log "수집 실패(exit $LASTEXITCODE) - 기존 파일 유지"; exit 1 }
if (git status --porcelain data/fairs.json) {
  git add data/fairs.json
  git commit -m "update fairs $(Get-Date -Format yyyy-MM-dd)" 2>&1 | ForEach-Object { Log "$_" }
  git push 2>&1 | ForEach-Object { Log "$_" }
  if ($LASTEXITCODE -ne 0) { Log 'push 실패'; exit 1 }
  Log '갱신·push 완료'
} else { Log '변경 없음' }
