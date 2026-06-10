from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-10"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
GREEN     = (52, 211, 153)
CYAN      = (6, 182, 212)
BLUE      = (59, 130, 246)
PURPLE    = (167, 139, 250)

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

draw.rectangle([0, 0, W, 4], fill=BLUE)
draw.rectangle([0, 0, 4, H], fill=BLUE)

# ── 헤더 ──
draw.text((32, 14), "SIVE — 기관 누적 매집 타임라인", font=bold(38), fill=WHITE)
draw.text((32, 62), "2026.06.10  |  Sivers Semiconductors  |  JPMorgan · Fidelity · BlackRock", font=font(18), fill=CYAN)
draw.line([(32, 98), (W - 32, 98)], fill=DARK_GRAY, width=1)

CONTENT_TOP = 114
CONTENT_BOT = H - 52

# ── 왼쪽: 타임라인 ──
LEFT_W = 500
draw.text((32, CONTENT_TOP), "진입 타임라인", font=bold(18), fill=GRAY)

events = [
    ("5월 29일", "MSCI Sweden Small-Cap 편입 효력",
     "패시브 ETF 의무 매수 시작  —  BlackRock 진입", PURPLE),
    ("6월  1일", "OMXS30 편입 효력",
     "2차 패시브 매수 파동  /  공매도 17% vs 패시브 충돌", CYAN),
    ("6월  2일", "GlobalFoundries AI 포토닉스 파트너십 발표",
     "발표 당일 JPMorgan 5.25% 공시  /  주가 +50%", BLUE),
]

ey = CONTENT_TOP + 30
box_h = (CONTENT_BOT - ey) // 3 - 6

for date, title, sub, color in events:
    draw.rounded_rectangle([32, ey, LEFT_W, ey + box_h], radius=8, fill=(18, 22, 34))
    draw.rectangle([32, ey, 38, ey + box_h], fill=color)
    draw.text((52, ey + 10), date, font=bold(17), fill=color)
    draw.text((52, ey + 40), title, font=bold(16), fill=WHITE)
    draw.text((52, ey + 70), sub, font=font(13), fill=GRAY)
    ey += box_h + 6

# ── 세로 구분선 ──
draw.line([(524, 98), (524, CONTENT_BOT)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 기관별 성격 ──
RX = 544
draw.text((RX, CONTENT_TOP), "기관별 성격", font=bold(18), fill=GRAY)

institutions = [
    (BLUE,   "JPMorgan",        "5.25%  /  ~$1.35억",
     "액티브 — 소규모 선진입 후 6월 2일 대규모 확대",
     "GF 파트너십 당일 공시  /  신념 기반 포지션"),
    (CYAN,   "Fidelity Research", "직접 포지션",
     "액티브 — 자체 리서치 후 직접 매수",
     "미국 기관의 스웨덴 소형주 커버리지 개시 신호"),
    (PURPLE, "BlackRock",       "패시브 오너",
     "패시브 — 인덱스 편입 의무 매수",
     "신념 아닌 의무  /  단, 유동주식 흡수 효과 있음"),
]

iy = CONTENT_TOP + 30
ibox_h = (CONTENT_BOT - iy) // 3 - 6

for color, name, amount, nature, desc in institutions:
    draw.rounded_rectangle([RX, iy, W - 32, iy + ibox_h], radius=8, fill=(18, 22, 34))
    draw.rectangle([RX, iy, RX + 6, iy + ibox_h], fill=color)
    name_w = int(draw.textlength(name, font=bold(18)))
    draw.text((RX + 20, iy + 10), name, font=bold(18), fill=color)
    draw.text((RX + 20 + name_w + 14, iy + 14), amount, font=font(14), fill=GRAY)
    draw.text((RX + 20, iy + 40), nature, font=bold(14), fill=WHITE)
    draw.text((RX + 20, iy + 66), desc, font=font(13), fill=GRAY)
    iy += ibox_h + 6

# ── 하단 결론 바 ──
draw.line([(32, H - 52), (W - 32, H - 52)], fill=DARK_GRAY, width=1)
draw.rounded_rectangle([32, H - 48, W - 32, H - 8], radius=6, fill=(16, 20, 38))
draw.text((52, H - 36), "+1,700% 주가에 대형 기관 3곳 동시 진입  —  현재 가격을 지지 가능하다고 판단한 것", font=bold(16), fill=BLUE)

out = os.path.join(OUT_DIR, "2026-06-10_SIVE_institutional_accumulation.png")
img.save(out)
print("Saved:", out)
