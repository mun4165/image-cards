from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-18"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

def new_canvas():
    img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)
    return img, draw

def header(draw, t1, t2):
    draw.text((32,24), t1, font=bold(30), fill=ACCENT)
    draw.text((32,78), t2, font=bold(22), fill=GRAY)
    draw.line([(32,124),(W-32,124)], fill=DARK_GRAY, width=1)

def footer(draw, label):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), label, font=font(15), fill=GRAY)

def band(draw, y, h, color, fillbg, label, headline, d1, d2, lx=240):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(22), fill=color)
    draw.line([(lx,y+16),(lx,y+h-16)], fill=DARK_GRAY, width=1)
    tx = lx+28
    if d2:
        draw.text((tx, y+16), headline, font=bold(23), fill=WHITE)
        draw.text((tx, y+54), d1, font=font(18), fill=color)
        draw.text((tx, y+82), d2, font=font(16), fill=GRAY)
    else:
        draw.text((tx, y+h//2-32), headline, font=bold(23), fill=WHITE)
        draw.text((tx, y+h//2+6), d1, font=font(18), fill=color)

FOOT = "2026.07.18  |  SATL  Satellogic"

# ── 표지 ──────────────────────────────────────────
img, draw = new_canvas()
header(draw, "세틀로직 -68%, 하락이 과한가는 절반의 질문이었다",
       "52주 고점 12달러 → 3.82달러, 질문을 바꿔야 했다")
by=142; bh=160; step=178
band(draw, by, bh, RED, (36,14,14), "사흘 가격",
     "-8.12% → -9.85% → +7.00%, 3.82달러 마감",
     "7/15 3.96 · 7/16 3.57 · 7/17 3.82달러",
     "사흘간 회사 뉴스 없음 — 가격만 움직였다")
band(draw, by+step, bh, AMBER, (40,28,10), "핵심 변수",
     "궤도 위성 19기 vs 목표 200기·5분 재방문",
     "멀린(Merlin) 컨스텔레이션 첫 발사 2026년 10월",
     "EO 사업은 재방문 빈도가 곧 서비스 품질")
band(draw, by+step*2, bh, CYAN, (8,28,34), "바뀐 질문",
     "하락이 과한가 → 핵심 변수가 풀렸는가",
     "하락폭은 감정을 흔들지만, 변수는 그대로다",
     "고점 대비 -68%는 급등 꼭대기를 기준으로 삼은 숫자")
footer(draw, FOOT)
img.save(os.path.join(OUT_DIR, "2026-07-18_SATL_21편_표지.png"))

# ── 중간삽입1: 가격 이력 타임라인 ──────────────────
img, draw = new_canvas()
header(draw, "반복되는 급등락 — 이번이 처음이 아니다",
       "저점 대비 고점이 열 배 가까운 종목")
by=142; bh=118; step=132
band(draw, by, bh, BLUE, (10,20,34), "2022년",
     "5.5~6.5달러 구간", "스팩 상장 직후의 고점 구간", "")
band(draw, by+step, bh, RED, (36,14,14), "2024년 초",
     "1.2~1.35달러 구간", "고점 대비 -80% 수준까지 하락", "")
band(draw, by+step*2, bh, AMBER, (40,28,10), "2026년 5월",
     "12.00달러 고점 (5/26)", "연초 1달러 후반에서 다섯 배 급등의 꼭대기", "")
band(draw, by+step*3, bh, CYAN, (8,28,34), "2026년 7월",
     "3.82달러 (7/17)", "반복 이력 = 안심 근거가 아니라 변동성의 증거", "")
footer(draw, FOOT)
img.save(os.path.join(OUT_DIR, "2026-07-18_SATL_21편_가격이력.png"))

# ── 중간삽입2: 19기 vs 200기 ──────────────────────
img, draw = new_canvas()
header(draw, "위성 19기 vs 목표 200기",
       "원가우위를 매출로 바꾸는 통로는 위성 수뿐이다")
by=142; bh=160; step=178
band(draw, by, bh, AMBER, (40,28,10), "현재",
     "궤도 위성 19기 (운영 18기)",
     "특정 지역을 며칠에 한 번 지나가는 수준",
     "상시감시가 필요한 국방·정부 수요엔 부족")
band(draw, by+step, bh, CYAN, (8,28,34), "목표",
     "200기 규모 · 5분 재방문",
     "위성 1기당 100만 달러 미만(회사 주장)",
     "200기 구축 비용 2억 달러 미만 제시")
band(draw, by+step*2, bh, GREEN, (10,32,22), "실행분",
     "멀린(Merlin) 1m급 신형 위성군",
     "첫 발사 2026년 10월 · 완전 운영 2027년 상반기",
     "이 간극을 메우는 첫 단추이자 리레이팅 트리거")
footer(draw, FOOT)
img.save(os.path.join(OUT_DIR, "2026-07-18_SATL_21편_19기vs200기.png"))

# ── 중간삽입3: 스와스 트레이드오프 ─────────────────
img, draw = new_canvas()
header(draw, "넓게 찍으면 되지 않나 — 스웹의 맞교환",
       "찍는 폭과 해상도는 같이 못 가진다")
by=142; bh=160; step=178
band(draw, by, bh, RED, (36,14,14), "폭을 넓히면",
     "화각이 커질수록 해상도가 떨어진다",
     "픽셀 하나가 커버하는 지상 면적이 커지기 때문",
     "서브미터 해상도라는 셀링포인트와 충돌")
band(draw, by+step, bh, AMBER, (40,28,10), "해상도 유지",
     "렌즈·센서를 키우면 위성이 무겁고 비싸진다",
     "저가 소형위성이라는 정체성 자체가 무너짐",
     "경쟁 상대로 지목한 진영(크고 비싼 위성)의 스펙이 됨")
band(draw, by+step*2, bh, CYAN, (8,28,34), "선례",
     "플래닛 도브 — 3~5m급인데도 100기 이상 운영",
     "해상도를 양보한 진영조차 물량이 필요했다",
     "폭으로 물량을 대체한 서브미터 사례는 확인 안 됨")
footer(draw, FOOT)
img.save(os.path.join(OUT_DIR, "2026-07-18_SATL_21편_스웹맞교환.png"))

# ── 중간삽입4: 저마진 전략 성립조건 ────────────────
img, draw = new_canvas()
header(draw, "저마진 물량 전략이 성립하려면",
       "TSMC가 증명한 두 조건에 대입해봤다")
by=142; bh=160; step=178
band(draw, by, bh, BLUE, (10,20,34), "조건 ①",
     "복제 불가능한 원가우위",
     "TSMC: 수십조 원 진입장벽 — 아무도 못 따라옴",
     "SATL: 셀링포인트가 '저비용' — 낮은 장벽은 난입을 부른다")
band(draw, by+step, bh, BLUE, (10,20,34), "조건 ②",
     "고객 락인",
     "TSMC: 공정 전용 설계자산에 수십억 달러 묶임",
     "SATL: 분석 파트너의 배타적 의존 증거 아직 없음")
band(draw, by+step*2, bh, CYAN, (8,28,34), "결론",
     "전략이라는 해석은 유효, 증명은 아직",
     "두 조건 없이 물량만 늘면 마진이 더 눌릴 위험",
     "볼 지표 = 스케일업 이후 위성당 매출 유지 여부")
footer(draw, FOOT)
img.save(os.path.join(OUT_DIR, "2026-07-18_SATL_21편_저마진전략조건.png"))

# ── 중간삽입5: 매출 비교 ──────────────────────────
img, draw = new_canvas()
header(draw, "가장 싸게 찍는 회사가 가장 적게 번다",
       "FY2025 매출 — 마진은 픽셀이 아니라 해석 레이어에 있다")
by=142; bh=160; step=178
band(draw, by, bh, RED, (36,14,14), "Satellogic",
     "1,770만 달러",
     "위성 19기 — 가장 싸게, 가장 조밀하게 찍는데",
     "해석 레이어는 SynMax·SpaceKnow 파트너 외주")
band(draw, by+step, bh, AMBER, (40,28,10), "BlackSky",
     "1억 660만 달러 — SATL의 6배",
     "위성은 더 적은데 자체 분석(Spectra AI)으로 해석 판매",
     "마진이 어느 층에 있는지 보여주는 대조군")
band(draw, by+step*2, bh, CYAN, (8,28,34), "Planet",
     "2억 4,400만 달러",
     "해상도를 양보하고 커버리지·구독으로 확장",
     "픽셀은 커모디티화 — 판단을 팔아야 마진이 남는다")
footer(draw, FOOT)
img.save(os.path.join(OUT_DIR, "2026-07-18_SATL_21편_매출비교.png"))

print("Saved 6 cards to", OUT_DIR)
