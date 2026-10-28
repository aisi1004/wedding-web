# wedding-web
웨딩박람회 일정 모음(com.imeji.wedding) 앱이 받아 가는 일정 데이터. 매주 월요일 새벽 3시(KST)에 GitHub Actions 가 CPAAD 공개 일정 페이지를 읽어 `data/fairs.json` 을 갱신하고, GitHub Pages(`wedding.imeji.com`)로 공개한다.
- 수동 실행: Actions 탭 → update-fairs → Run workflow
- 건수가 50건 미만이면(페이지 구조 변경 의심) 파일을 덮어쓰지 않고 실패한다.
