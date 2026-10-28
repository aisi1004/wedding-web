# wedding-web
웨딩박람회 일정 모음(com.imeji.wedding) 앱이 받아 가는 일정 데이터. GitHub Pages(`wedding.imeji.com`)로 공개한다.

- 갱신: 사장님 PC 의 Windows 작업 스케줄러 `wedding-fairs-update` 가 매주 월요일 새벽 3시(KST)에 `scripts/run-update.ps1` 을 실행한다(PC 가 꺼져 있었으면 켜진 뒤 실행). CPAAD 가 GitHub 서버(해외 IP) 접속을 막아서 GitHub Actions 로는 수집할 수 없다.
- 수집 스크립트 `scripts/update.py`: 건수가 50건 미만이면(페이지 구조 변경 의심) 파일을 덮어쓰지 않고 실패한다. 내용이 같으면 커밋하지 않는다.
- 로그: `scripts/update.log`(저장소에는 올리지 않음)
