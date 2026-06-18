from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-19"
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

ACCENT = GREEN  # 메모리·상승 테마

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")

for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

draw.rectangle([0, 0, W, 4], fill=ACCENT)
draw.rectangle([0, 0, 4, H], fill=ACCENT)

# ── 헤더 ──
draw.text((32, 18), "마이크론 +8.7%, 실적이 아니라 목표가였다", font=bold(36), fill=ACCENT)
draw.text((32, 68), "사상 최고가 경신 — 그런데 분기 실적은 6/24에야 나온다", font=bold(23), fill=WHITE)
draw.text((32, 104), "이날 급등은 '사실'이 아니라 실적에 대한 '기대'가 만든 것이다", font=font(18), fill=GRAY)
draw.line([(32, 138), (W - 32, 138)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("6/18 종가",        "$1,133.99",   "+8.70%  /  장중 사상 최고가",          GREEN),
    ("최근 1년",          "+800%↑",      "구조적 AI 메모리 수요",                AMBER),
    ("HBM 생산능력",      "완판",         "판매가, 회사 기대치 상회",              BLUE),
    ("Q3 매출 추정(웨드부시)", "$385억",   "컨센서스 $348.4억 대비 상향",          CYAN),
]
y = 156
for label, value, sub, color in metrics:
    draw.text((32, y), label, font=font(17), fill=GRAY)
    draw.text((32, y + 22), value, font=bold(28), fill=color)
    draw.text((32, y + 56), sub, font=font(16), fill=GRAY)
    draw.line([(32, y + 80), (590, y + 80)], fill=DARK_GRAY, width=1)
    y += 92

draw.line([(620, 136), (620, H - 46)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 목표가 일제 상향 ──
draw.text((644, 156), "방아쇠 — 개장 전 목표가 폭탄 상향", font=bold(22), fill=WHITE)
draw.line([(644, 188), (W - 32, 188)], fill=DARK_GRAY, width=1)

targets = [
    ("스티펠",        "$550 → $1,500"),
    ("도이체방크",     "→ $1,500"),
    ("TD코웬",        "→ $1,500"),
    ("웨드부시",       "$550 → $1,300"),
    ("씨티 · 로젠블랫", "→ $1,200"),
]
y = 202
for name, chg in targets:
    draw.text((656, y), name, font=bold(19), fill=WHITE)
    draw.text((980, y), chg, font=bold(19), fill=GREEN)
    y += 40

# 요약 박스
draw.line([(644, y + 6), (W - 32, y + 6)], fill=DARK_GRAY, width=1)
y += 20
draw.rounded_rectangle([644, y, W - 32, y + 62], radius=8, fill=(6, 36, 24))
draw.text((658, y + 12), "기대 선반영은 양날의 검", font=bold(18), fill=GREEN)
draw.text((658, y + 36), "6/24 실적이 검증 분기점 — 소문에 사고 뉴스에 판다", font=bold(16), fill=GREEN)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.19  |  MU  Micron  ·  stockanalysis · Investing.com", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-19_MU_목표가폭탄상향_핵심요약.png")
img.save(out)
print("Saved:", out)
