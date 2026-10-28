# CPAAD 공개 일정 페이지(wedunited01drc) -> data/fairs.json
# 페이지 구조가 바뀌어 건수가 비정상이면 파일을 덮어쓰지 않고 실패(워크플로 실패 메일)한다.
import re, json, html, sys, urllib.request, datetime, os

URL = 'https://ad.cpaad.co.kr/wedunited01drc/imeji'
OUT = os.path.join(os.path.dirname(__file__), '..', 'data', 'fairs.json')
MIN_COUNT = 50

raw = urllib.request.urlopen(urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read().decode('utf-8', 'replace')
parts = re.split(r"<b>([^<]*?)\s*웨딩박람회 일정</b>", raw[raw.index('id="section01"') if 'id="section01"' in raw else 0:])

def clean(t):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t))).strip()

fairs = []
for k in range(1, len(parts), 2):
    region = parts[k].strip()
    for m in re.finditer(r"<div class='goods01' id='ban_([^']+)'>(.*?)</a></div>", parts[k + 1], re.S):
        fid, c = m.group(1), m.group(2)
        g = lambda cls: (re.search(r"class='%s'>(.*?)</div>" % cls, c, re.S) or [None, ''])[1]
        loc = [clean(x) for x in re.split(r'<br\s*/?>', g('ad_location'))]
        fairs.append({'id': fid, 'region': region, 'title': clean(g('ad_title')), 'info': clean(g('ad_info')),
                      'date': clean(g('ad_date')), 'addr': loc[0] if loc else '', 'venue': loc[-1] if len(loc) > 1 else ''})

print(len(fairs), 'fairs', file=sys.stderr)
if len(fairs) < MIN_COUNT:
    sys.exit('건수가 너무 적어요(%d건). 페이지 구조가 바뀌었는지 확인하세요. 기존 파일은 그대로 둡니다.' % len(fairs))

kst = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=9)
data = {'updated': kst.strftime('%Y-%m-%d'), 'list': fairs}
body = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
if os.path.exists(OUT):
    old = json.load(open(OUT, encoding='utf-8'))
    if old.get('list') == fairs:       # 내용이 같으면 날짜만 바뀐 커밋을 만들지 않는다
        print('변경 없음', file=sys.stderr)
        sys.exit(0)
open(OUT, 'w', encoding='utf-8').write(body)
