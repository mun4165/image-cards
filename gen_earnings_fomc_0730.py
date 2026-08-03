from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-30"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

def base_canvas(accent):
    img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    draw.rectangle([0,0,W,4], fill=accent); draw.rectangle([0,0,4,H], fill=accent)
    return img, draw

def band(draw, y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(17), fill=color)
    draw.line([(268,y+14),(268,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((292, y+15), headline, font=bold(18), fill=WHITE)
    draw.text((292, y+45), detail, font=font(14), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# 5개 밴드 배치용 지오메트리 (푸터 라인 H-30 위에서 끝나도록)
BY, BH, STEP = 122, 98, 110


# ── 1. MSFT 현금흐름 격차 ────────────────────────────────
img, draw = base_canvas(AMBER)
draw.text((32,22), "영업현금흐름 +30%인데 잉여현금흐름은 -23%", font=bold(25), fill=AMBER)
draw.text((32,74), "마이크로소프트 FY26 4분기, capex가 만든 격차", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, GREEN, (10,30,22), "손익  |  견조",
     "매출 900억달러(+18%) · 영업이익 406억달러(+18%)", "EPS 4.81달러(+32%), 매출·영업이익 모두 두 자릿수 성장")
band(draw, by+step, bh, RED, (40,14,14), "현금  |  역방향",
     "영업현금흐름 554억달러(+30%) → 잉여현금흐름 196억달러(-23%)", "현금 전환율 약 35%로 하락, 두 지표가 반대로 움직였다")
band(draw, by+step*2, bh, ORANGE, (44,20,10), "원인  |  capex +69%",
     "금융리스 포함 분기 capex 410억달러(순수 capex 358억달러)", "영업현금 554억달러 중 410억달러가 인프라로 유출")
band(draw, by+step*3, bh, AMBER, (40,28,10), "회계  |  표기 변경",
     "감가상각 내용연수 15년 → 25년 · 금융리스 → 운영리스", "capex 표기 1,900억→1,750억달러, 투자 계획 축소 아님")
band(draw, by+step*4, bh, BLUE, (10,20,40), "부외  |  미확정 리스",
     "미확정 리스 약정 3,291억달러(전기 1,966억달러)", "한 분기에 1,300억달러 증가, 아직 부채로 잡히지 않은 의무")
footer(draw, "2026.07.30  |  MSFT  마이크로소프트 FY26 Q4")
out = os.path.join(OUT_DIR, "2026-07-30_MSFT_영업현금흐름과_잉여현금흐름_격차.png")
img.save(out); print("Saved:", out)


# ── 2. MSFT 백로그 오픈AI 집중도 ─────────────────────────
img, draw = base_canvas(CYAN)
draw.text((32,22), "백로그 6,780억달러 +84%, 오픈AI 빼면 +25%", font=bold(25), fill=CYAN)
draw.text((32,74), "마이크로소프트 RPO의 절반은 단일 고객이다", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, GREEN, (10,30,22), "공시  |  전체 수치",
     "상업 RPO 6,780억달러(+84%) · 연매출 3,318억달러의 2배 이상", "평균 듀레이션 2.5년(전분기 2년), 계약 잔액 기준")
band(draw, by+step, bh, RED, (40,14,14), "집중  |  오픈AI 45%",
     "약 3,050억달러가 오픈AI 물량 · 제외 시 증가율 +25%", "84%와 25%, 같은 백로그에서 나오는 두 개의 증가율")
band(draw, by+step*2, bh, ORANGE, (44,20,10), "질  |  지불 능력",
     "오픈AI는 미이익 기업, 연속 펀딩 라운드로 운영자금 조달", "자체 현금흐름이 아닌 외부 조달 의존 구조")
band(draw, by+step*3, bh, AMBER, (40,28,10), "이탈  |  공급자 다변화",
     "AWS와 380억달러 계약 · 브로드컴 자체 칩 2026년 말 배치", "갱신 시점 협상력과 추가 물량 향방에 영향")
band(draw, by+step*4, bh, BLUE, (10,20,40), "채점  |  실제 기준",
     "백로그 확인이 아니라 자체 현금흐름 감당 + 가이던스 유지", "같은 날 MSFT 약 +8%, META 약 -10%가 그 증거")
footer(draw, "2026.07.30  |  MSFT  마이크로소프트 · 오픈AI")
out = os.path.join(OUT_DIR, "2026-07-30_MSFT_백로그_오픈AI집중도.png")
img.save(out); print("Saved:", out)


# ── 3. META 컴퓨팅 임대·부채 ─────────────────────────────
img, draw = base_canvas(RED)
draw.text((32,22), "매출 +28%인데 잉여현금흐름 7억달러, 왜 안 파나", font=bold(25), fill=RED)
draw.text((32,74), "메타 2026년 2분기, 컴퓨팅 프리미엄 제안과 부외 부채", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, RED, (40,14,14), "실적  |  마진 붕괴",
     "매출 608억달러(+28%) · 순이익 158억달러(-14%)", "영업마진 43% → 31%, 시간외 주가 -9.64%")
band(draw, by+step, bh, ORANGE, (44,20,10), "현금  |  사실상 0",
     "영업현금흐름 319억달러 - capex 311억달러 = 7.84억달러", "매출 608억달러를 벌어 잉여현금 7.84억달러가 남았다")
band(draw, by+step*2, bh, AMBER, (40,28,10), "부채  |  의도적 확대",
     "분기 중 장기부채 249억달러 조달 · 분기말 837억달러", "수전 리: 자본비용 낮추려 부채 비중 확대 중")
band(draw, by+step*3, bh, BLUE, (10,20,40), "부외  |  JV 구조",
     "하이페리온(블루아울) · 엘패소(블랙록 80%, 부채 125억달러)", "프로젝트 대상 조달이라 capex 아닌 임차료로 계상")
band(draw, by+step*4, bh, CYAN, (10,28,36), "컴퓨팅  |  팔지 않는다",
     "저커버그: 지불 가격보다 상당한 프리미엄 제안 여러 건", "지능 판매 마진이 더 높다 · 금액·계약 미공시 = 검증 불가")
footer(draw, "2026.07.30  |  META  메타 2026 Q2")
out = os.path.join(OUT_DIR, "2026-07-30_META_잉여현금흐름_컴퓨팅임대.png")
img.save(out); print("Saved:", out)


# ── 4. AAPL·AMZN 관전포인트 ──────────────────────────────
img, draw = base_canvas(TEAL)
draw.text((32,22), "애플·아마존 같은 날 발표, 채점 기준은 다르다", font=bold(25), fill=TEAL)
draw.text((32,74), "7월 30일 장 마감 후 · 한국시간 7월 31일 새벽", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, TEAL, (10,32,30), "일정  |  한 시간 간격",
     "애플 동부 16:00 공개·17:00 콜 · 아마존 동부 17:00 콜", "한국시간 7/31 금요일 오전 5시와 6시")
band(draw, by+step, bh, AMBER, (40,28,10), "애플  |  총마진",
     "컨센서스 매출 1,090억달러 · EPS 1.89달러 · 가이던스 47.5~48.5%", "메모리 원가 전가 후 47.5% 하단 이탈 여부가 핵심")
band(draw, by+step*2, bh, ORANGE, (44,20,10), "애플  |  마지막 콜",
     "팀 쿡의 마지막 어닝콜, 제프 윌리엄스로 승계 예정", "떠나는 CEO는 가이던스를 보수적으로 깔 유인이 있다")
band(draw, by+step*3, bh, RED, (40,14,14), "아마존  |  capex",
     "2월 제시 2,000억달러 → BofA는 2,100억달러 예상", "상향하면 알파벳 반응, 유지하면 MSFT 반응")
band(draw, by+step*4, bh, BLUE, (10,20,40), "아마존  |  AWS",
     "컨센서스 405억달러(+31%) · 마진 33.8% · 백로그 확대 폭", "MSFT Azure +43%가 비교 기준, 오픈AI 380억달러 반영 확인")
footer(draw, "2026.07.30  |  AAPL · AMZN  실적 관전 포인트")
out = os.path.join(OUT_DIR, "2026-07-30_AAPL_AMZN_실적관전포인트.png")
img.save(out); print("Saved:", out)


# ── 5. FOMC·워시 ─────────────────────────────────────────
img, draw = base_canvas(BLUE)
draw.text((32,22), "9대 3 동결인데 30년물은 5.21%까지 뛰었다", font=bold(25), fill=BLUE)
draw.text((32,74), "워시는 긴축을 채권시장에 넘겼다고 직접 말했다", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, BLUE, (10,20,40), "결정  |  9 대 3 동결",
     "연방기금금리 목표범위 3.50~3.75% 유지", "해맥·카시카리·로건 3명 전원 0.25%p 인상 주장")
band(draw, by+step, bh, ORANGE, (44,20,10), "분포  |  인하 주장 0",
     "반대표가 전원 인상 쪽, 완화 방향 표는 한 장도 없었다", "이것이 이번 회의 매파적 신호의 본질")
band(draw, by+step*2, bh, RED, (40,14,14), "시장  |  장기금리 급등",
     "30년물 +10bp → 5.21%(19년래 최고) · 10년물 +7bp → 4.67%", "기자회견 도중 발생, 10년물은 모기지 기준금리")
band(draw, by+step*3, bh, AMBER, (40,28,10), "워시  |  의도된 결과",
     "42일간 명목·실질 금리 상승폭이 20년 내 상위 10분위", "심판이 아니라 공을 보는 법을 배우고 있다 · 아직 시작에 불과")
band(draw, by+step*4, bh, CYAN, (10,28,36), "연결  |  AI capex 의제화",
     "capex 붐이 메모리·로직 칩 가격을 밀어올린다고 위원회 논의", "AI 투자 붐 자체가 긴축 명분을 만드는 구조")
footer(draw, "2026.07.30  |  FOMC  케빈 워시 기자회견 원문 기준")
out = os.path.join(OUT_DIR, "2026-07-30_FOMC_워시_9대3동결_장기금리.png")
img.save(out); print("Saved:", out)
