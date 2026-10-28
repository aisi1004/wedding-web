# wedding-web
웨딩박람회 일정 모음(com.imeji.wedding) 앱이 받아 가는 일정 데이터. GitHub Pages(`wedding.imeji.com`)로 공개한다.

- 수집 스크립트 `scripts/update.py`: CPAAD 공개 일정 페이지를 읽어 `data/fairs.json` 을 만든다. 건수가 50건 미만이면(페이지 구조 변경 의심) 덮어쓰지 않고 실패하고, 내용이 같으면 바뀌지 않는다.
- `scripts/run-update.ps1`: 수집 후 바뀐 때만 commit/push 하는 Windows 용 실행 스크립트.
- 주의: CPAAD 가 해외 IP(GitHub Actions)의 접속을 막는다(연결 시간 초과). 한국 IP 에서 돌려야 한다.
- 정기 실행(월요일 새벽 주 1회)은 아직 설정하지 않았다(PC 는 상시 켜 두지 않으므로 PC 작업 스케줄러는 쓰지 않기로 함).
