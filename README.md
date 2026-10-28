# wedding-web
웨딩박람회 일정 모음(com.imeji.wedding) 앱이 받아 가는 일정 데이터. GitHub Pages(`wedding.imeji.com`)로 공개한다.

- 일정 갱신은 앱이 **사용자 폰에서 직접** CPAAD 공개 일정 페이지를 읽는 방식이 기본이다(마지막으로 읽은 지 7일 지나 앱을 열 때 한 번). CPAAD 가 해외 IP(GitHub Actions 등)의 접속을 막아서(연결 시간 초과) 서버에서는 수집할 수 없다. 파서는 앱의 `www/parse.js`.
- 이 저장소의 `data/fairs.json` 은 앱이 받아 쓰는 보조 데이터(앱에 내장된 것과 같은 규칙, 가장 최신 날짜가 쓰인다). 필요할 때 `scripts/update.py`(또는 `run-update.ps1`)를 한국 IP 환경에서 실행해 갱신하고 push 한다.
