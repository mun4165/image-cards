from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-03"
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

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")

# 그리드
for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

draw.rectangle([0, 0, W, 4], fill=RED)
draw.rectangle([0, 0, 4, H], fill=RED)

# ── 헤더 ──
draw.text((32, 14), "$AVGO", font=bold(40), fill=RED)
draw.text((160, 20), "브로드컴  오늘 밤 실적 발표  —  확인할 것들", font=bold(26), fill=WHITE)
draw.text((160, 56), "Q2 FY2026  |  한국시간 6/4(목) 오전 6시 컨콜", font=font(17), fill=GRAY)
draw.line([(32, 88), (W - 32, 88)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 가이던스 수치 ──
COL1_X = 32
draw.text((COL1_X, 100), "Q2 가이던스", font=bold(18), fill=GRAY)
draw.line([(COL1_X, 126), (390, 126)], fill=DARK_GRAY, width=1)

metrics = [
    ("AI 반도체",  "$10.7B",  "+140% YoY", RED),
    ("총 매출",    "$22.0B",  "+47% YoY",  ORANGE),
    ("EBITDA 마진","~68%",    "GP ~77%",   AMBER),
]
y = 134
for label, value, sub, color in metrics:
    draw.text((COL1_X, y), label, font=font(15), fill=GRAY)
    draw.text((COL1_X, y + 18), value, font=bold(28), fill=color)
    draw.text((COL1_X + 4, y + 50), sub, font=font(14), fill=GRAY)
    y += 74

# ── 중앙: XPU 고객 ──
draw.line([(410, 88), (410, H - 44)], fill=DARK_GRAY, width=1)
COL2_X = 426

draw.text((COL2_X, 100), "XPU 고객  —  6곳 중 이름 공개 4곳", font=bold(18), fill=GRAY)
draw.line([(COL2_X, 126), (820, 126)], fill=DARK_GRAY, width=1)

customers = [
    (GREEN,  "Google",    "TPU · 2031년까지 장기계약"),
    (GREEN,  "Meta",      "MTIA · 2027년부터 멀티GW"),
    (GREEN,  "Anthropic", "확인됨"),
    (GREEN,  "OpenAI",    "Q1에서 공개 · $100억+ 추론칩 개발"),
    (GRAY,   "미공개",    "2곳 — 오늘 밤 힌트 나오는지 본다"),
]
y = 134
for color, name, desc in customers:
    draw.rectangle([COL2_X, y + 4, COL2_X + 4, y + 26], fill=color)
    draw.text((COL2_X + 12, y), name, font=bold(19), fill=WHITE if color != GRAY else GRAY)
    draw.text((COL2_X + 12, y + 24), desc, font=font(15), fill=GRAY)
    y += 56

# ── 오른쪽: 오늘 밤 체크 ──
draw.line([(836, 88), (836, H - 44)], fill=DARK_GRAY, width=1)
COL3_X = 852

draw.text((COL3_X, 100), "오늘 밤 체크", font=bold(18), fill=GRAY)
draw.line([(COL3_X, 126), (W - 32, 126)], fill=DARK_GRAY, width=1)

checks = [
    (RED,    "① AI 매출 $10.7B 달성?",
             "분기 $100억 첫 돌파 여부"),
    (ORANGE, "② Q3 가이던스 방향",
             "AI 매출 $120억+\n연간 $600억 언급 여부"),
    (PURPLE, "③ 미공개 고객 힌트?",
             "6곳 중 2곳 미공개\n오늘 이름 나오는지"),
    (CYAN,   "④ 네트워킹 매출",
             "스위치칩 수요 가속\n데이터센터 확장 확인"),
]
y = 134
for color, title, desc in checks:
    draw.rectangle([COL3_X, y + 4, COL3_X + 4, y + 28], fill=color)
    draw.text((COL3_X + 12, y), title, font=bold(18), fill=WHITE)
    for i, line in enumerate(desc.split('\n')):
        draw.text((COL3_X + 12, y + 26 + i * 20), line, font=font(14), fill=GRAY)
    y += 82

# ── Hock Tan 발언 배너 ──
draw.rounded_rectangle([32, H - 78, W - 32, H - 46], radius=6, fill=(30, 20, 10))
draw.text((48, H - 68), '"FY2027 AI 칩 매출 $1,000억 이상, 가시권에 있다"  —  Hock Tan CEO', font=bold(17), fill=AMBER)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.03  |  Broadcom IR 공식 가이던스 · Q1 어닝콜 기준  |  개인 공부 기록", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-03_AVGO_실적체크.png")
img.save(out)
print("Saved:", out)
