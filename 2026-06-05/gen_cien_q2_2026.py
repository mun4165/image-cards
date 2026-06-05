from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-05"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
RED       = (239, 68, 68)
ORANGE    = (249, 115, 22)
AMBER     = (245, 158, 11)
GREEN     = (52, 211, 153)
CYAN      = (6, 182, 212)
PURPLE    = (167, 139, 250)

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)

def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

def make_base(accent):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=GRID, width=1)
    draw.rectangle([0, 0, W, 4], fill=accent)
    draw.rectangle([0, 0, 4, H], fill=accent)
    return img, ImageDraw.Draw(img)

def footer(draw, date_str, source_str):
    draw.line([(60, H - 52), (W - 60, H - 52)], fill=DARK_GRAY, width=1)
    draw.text((60, H - 36), f"{date_str}  |  {source_str}", font=font(17), fill=GRAY)


img, draw = make_base(CYAN)

# ── 헤더 ──
draw.text((60, 18), "CIEN  -13.66%  —  어닝 쇼크 아니다, 공급 쇼크다", font=bold(34), fill=WHITE)
draw.text((60, 62), "EPS +290%·백로그 $7.7B 사상 최대  ·  주가가 빠진 이유는 따로 있다", font=font(19), fill=GRAY)
draw.line([(60, 98), (W - 60, 98)], fill=DARK_GRAY, width=1)

# ── 왼쪽: Q2 실적 ──
lx = 60
draw.text((lx, 112), "FY2026 Q2 실적  (2026.06.04 발표)", font=bold(20), fill=GRAY)

rows = [
    ("매출",      "$1.57B",   "+40% YoY",   CYAN),
    ("조정 EPS",  "$1.64",    "+290% YoY",  GREEN),
    ("조정 GM",   "44.9%",    "확대",        GREEN),
    ("백로그",    "$7.7B",    "사상 최대",   AMBER),
]
y = 144
for label, val, note, color in rows:
    draw.text((lx, y),        label, font=font(17), fill=GRAY)
    draw.text((lx + 200, y),  val,   font=bold(22), fill=color)
    draw.text((lx + 360, y),  note,  font=font(17), fill=GRAY)
    draw.line([(lx, y + 34), (lx + 560, y + 34)], fill=DARK_GRAY, width=1)
    y += 44

# 컨센서스 비교 박스
draw.rounded_rectangle([lx, y + 6, lx + 560, y + 56], radius=8, fill=(10, 35, 40))
draw.text((lx + 16, y + 14), "컨센서스 EPS  $1.45  →  실제  $1.64  (+13% 초과)", font=bold(18), fill=CYAN)
draw.text((lx + 16, y + 36), "백로그 중 $5.1B  향후 12개월 내 인도 예정", font=font(16), fill=GRAY)
y += 70

# ── 왼쪽 아래: 가이던스 ──
y += 8
draw.line([(lx, y), (lx + 560, y)], fill=DARK_GRAY, width=1)
draw.text((lx, y + 10), "가이던스 상향 (3분기 연속)", font=bold(20), fill=GRAY)

guidance = [
    ("Q3 FY2026",    "$1.625B  ±$50M"),
    ("FY2026 전체",  "$6.3B  ±$100M  (+32% YoY)"),
    ("TAM 전망",     "$50B (2029년, 현재 대비 약 2배)"),
]
gy = y + 44
for label, val in guidance:
    draw.text((lx, gy),        label, font=font(16), fill=GRAY)
    draw.text((lx + 200, gy),  val,   font=bold(17), fill=WHITE)
    gy += 30

# ── 세로 구분선 ──
draw.line([(640, 98), (640, H - 60)], fill=DARK_GRAY, width=1)

# ── 오른쪽 위: 주가 하락 이유 ──
rx = 668
draw.text((rx, 112), "주가가 빠진 이유 — 펌프 레이저", font=bold(20), fill=GRAY)

draw.rectangle([rx, 144, rx + 4, 220], fill=RED)
draw.text((rx + 14, 144), "펌프 레이저(pump laser)", font=bold(20), fill=RED)
draw.text((rx + 14, 170), "광증폭기의 핵심 부품", font=font(17), fill=GRAY)
draw.text((rx + 14, 192), "수요 > 공급  →  인도 지연 우려", font=font(17), fill=ORANGE)

draw.rounded_rectangle([rx, 228, W - 60, 292], radius=8, fill=(40, 12, 12))
draw.text((rx + 16, 236), "백로그 $7.7B  ≠  즉시 매출 인식", font=bold(19), fill=RED)
draw.text((rx + 16, 260), "부품 수급이 막히면 인도 타임라인이 밀린다", font=font(17), fill=ORANGE)

# CapEx 대응
draw.line([(rx, 306), (W - 60, 306)], fill=DARK_GRAY, width=1)
draw.text((rx, 318), "대응  :  CapEx $250~275M 투입", font=bold(19), fill=GRAY)
draw.text((rx, 346), "공급망 직접 확보 중  ·  정상화 시점 미명시", font=font(17), fill=GRAY)

# ── 오른쪽 아래: 체크리스트 ──
draw.line([(rx, 384), (W - 60, 384)], fill=DARK_GRAY, width=1)
draw.text((rx, 396), "다음 확인 포인트  (Q3 어닝  ~2026년 9월)", font=bold(19), fill=GRAY)

checks = [
    (GREEN, "Q3 매출 $1.625B 달성 여부"),
    (GREEN, "백로그 $8B 이상 유지 여부"),
    (RED,   "펌프 레이저 제약 반복 언급 시 주의"),
]
cy = 428
for color, text in checks:
    symbol = "✓" if color == GREEN else "▲"
    draw.text((rx, cy), f"{symbol}  {text}", font=font(18), fill=color)
    cy += 30

# S&P 500 편입 메모
draw.rounded_rectangle([rx, cy + 8, W - 60, cy + 60], radius=8, fill=(10, 25, 40))
draw.text((rx + 16, cy + 16), "S&P 500  2026년 2월 편입 완료", font=bold(18), fill=CYAN)
draw.text((rx + 16, cy + 40), "패시브 수급 카탈리스트는 이미 소화됨", font=font(16), fill=GRAY)

footer(draw, "2026.06.05", "Ciena FY2026 Q2 Earnings  |  CIEN 종가 기준")

out = os.path.join(OUT_DIR, "2026-06-05_CIEN_Q2어닝.png")
img.save(out)
print("Saved:", out)
