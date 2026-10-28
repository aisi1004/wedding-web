# wedding-web
웨딩박람회 일정 결혼준비 체크리스트(com.imeji.wedding) 앱이 받아 가는 일정 데이터. GitHub Pages(`wedding.imeji.com`)로 공개한다.

- 일정 갱신은 앱이 **사용자 폰에서 직접** CPAAD 공개 일정 페이지를 읽는 방식이 기본이다(마지막으로 읽은 지 7일 지나 앱을 열 때 한 번). CPAAD 가 해외 IP(GitHub Actions 등)의 접속을 막아서(연결 시간 초과) 서버에서는 수집할 수 없다. 파서는 앱의 `www/parse.js`.
- 이 저장소의 `data/fairs.json` 은 앱이 받아 쓰는 보조 데이터(앱에 내장된 것과 같은 규칙, 가장 최신 날짜가 쓰인다). 필요할 때 `scripts/update.py`(또는 `run-update.ps1`)를 한국 IP 환경에서 실행해 갱신하고 push 한다.

## 앱 안 자체 배너 (앱 업데이트 없이 교체)

앱은 `https://wedding.imeji.com/data/banners.json` 을 6시간에 한 번 받아 각 탭 맨 위에 배너를 보여준다. 이 저장소의 `data/banners.json` 을 고쳐 올리면 된다. 예시는 `data/banners.sample.json`, 이미지는 `img/banners/` 에 넣는다.

| 칸 | 설명 |
|---|---|
| `id` | 배너 고유 이름(영문·숫자). 사용자가 ✕ 로 닫으면 24시간 동안 이 id 는 안 보인다 |
| `img` | 이미지 주소(**https 만**). 권장 크기 1080×300 (3.6:1), 가로로 꽉 채워 보인다 |
| `link` | 눌렀을 때 이동. `https://…` 외부 주소(Play 스토어 링크 가능) / `tab:home` `tab:list` `tab:budget` `tab:quote` `tab:fair` 앱 안 탭 / `settings` 설정 화면 |
| `alt` | 이미지 설명(접근성) |
| `label` | 배너 왼쪽 위 작은 글자(기본 "홍보") |
| `tabs` | 보여줄 탭 목록. 생략하면 모든 탭 |
| `start`, `end` | `YYYY-MM-DD`. 이 기간에만 표시(둘 다 생략 가능) |
| `weight` | 같은 탭에 여러 배너가 겹칠 때 뽑힐 확률 가중치(기본 1) |

- 배너가 없으면 `"banners": []` 로 둔다.
- 한 번에 최대 10개까지 읽는다. 이미지가 안 열리면 그 배너는 자동으로 숨는다.
- 허용되지 않는 링크(`http://`, `javascript:` 등)가 들어간 배너는 무시된다.
- 사용자 정보는 보내지 않고 클릭 수도 세지 않는다. 클릭을 세고 싶으면 `link` 주소에 직접 추적용 문구(예: `?utm_source=wedding_app`)를 붙인다.
