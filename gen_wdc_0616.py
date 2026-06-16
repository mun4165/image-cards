from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-16"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (60, 70, 82)
AMBER     = (245, 158, 11)
TEAL      = (20, 184, 166)
BLUE      = (59, 130, 246)
CYAN      = (6, 182, 212)
GREEN     = (52, 211, 153)
RED       = (239, 68, 68)
ORANGE    = (249, 115, 22)

ACCENT = BLUE  # WDC 강조색

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")

# 그리드
for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

# 상단·좌측 강조선
draw.rectangle([0, 0, W, 4], fill=ACCENT)
draw.rectangle([0, 0, 4, H], fill=ACCENT)

# ── 헤더 ──
draw.text((32, 18), "WDC (Western Digital)", font=bold(40), fill=ACCENT)
draw.text((32, 72), "샌디스크 버리고 HDD 전업  —  AI가 살린 하드디스크", font=bold(24), fill=WHITE)
draw.text((32, 108), "2025.02 낸드 분할 후 순수 HDD  ·  매출 89% 하이퍼스케일러 클라우드", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("주가 / 시총 (2026.06.15 종가, ATH)", "$653.53 / $225B", "분할 전 대비 약 9배 리레이팅", GREEN),
    ("Q3 FY2026 매출",                     "$3.34B",          "+45% YoY  /  Q4 가이드 ~$3.65B", BLUE),
    ("매출총이익률",                        "50.5%",           "+440bp QoQ  /  역사상 첫 50%대",  TEAL),
    ("밸류에이션",                          "PE 35.8",         "P/S 약 17배  /  연매출 ~$13B",    AMBER),
]
y = 158
for label, value, sub, color in metrics:
    draw.text((32, y), label, font=font(17), fill=GRAY)
    draw.text((32, y + 22), value, font=bold(28), fill=color)
    draw.text((32, y + 56), sub, font=font(16), fill=GRAY)
    draw.line([(32, y + 80), (590, y + 80)], fill=DARK_GRAY, width=1)
    y += 92

# 세로 구분선
draw.line([(620, 140), (620, H - 46)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 투자 포인트 & 리스크 ──
draw.text((644, 158), "투자 포인트 & 리스크", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (TEAL,  "2026 캐파 완판",
     "장기계약으로 선예약  /  계약 2027~2028 연장  =  매출 가시성"),
    (GREEN, "3사 과점 95%+",
     "WDC·시게이트·도시바  /  캐파 절제가 가격결정력으로"),
    (BLUE,  "TB당 비용 최강자",
     "AI 콜드·웜 데이터 저장  /  SSD 대비 압도적 원가 우위"),
    (RED,   "리스크",
     "시클리컬에 성장주 멀티플  /  capex 89% 의존  /  HAMR 시게이트가 앞섬"),
]
y = 204
for color, title, desc in points:
    draw.rectangle([640, y + 3, 644, y + 30], fill=color)
    draw.text((656, y), title, font=bold(20), fill=WHITE)
    draw.text((656, y + 28), desc, font=font(17), fill=GRAY)
    y += 62

# ── 체크포인트 ──
draw.line([(644, y + 4), (W - 32, y + 4)], fill=DARK_GRAY, width=1)
draw.text((644, y + 14), "다음 체크포인트  ·  8월 5일 Q4 실적", font=bold(20), fill=ORANGE)
y += 46

checks = [
    "① FY2027 가이던스 성장 유지 여부",
    "② 장기계약 가격 상향·고정 vs 변동",
    "③ HAMR qual 완료·양산 일정(CY2027 초)",
]
for line in checks:
    draw.text((644, y), line, font=font(17), fill=GRAY)
    y += 30

# 요약 박스
draw.rounded_rectangle([644, y + 8, W - 32, y + 50], radius=8, fill=(10, 22, 40))
draw.text((658, y + 18), "캐파는 완판  —  관건은 시클리컬에 붙은 성장주 멀티플", font=bold(18), fill=BLUE)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.16  |  stockanalysis · WDC Q3 FY2026 실적 · Motley Fool", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-16_WDC_순수HDD전업_핵심요약.png")
img.save(out)
print("Saved:", out)
