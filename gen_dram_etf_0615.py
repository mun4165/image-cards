from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-15"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 10)
WHITE     = (255, 255, 255)
GRAY      = (130, 145, 165)
DARK_GRAY = (45, 58, 72)
BLUE      = (74, 144, 217)
BLUE_DIM  = (28, 65, 120)
BLUE_BG   = (16, 32, 58)
GREEN     = (72, 200, 140)
AMBER     = (245, 180, 50)
CYAN      = (6, 190, 220)
PURPLE    = (167, 139, 250)

def font(size):
    return ImageFont.truetype(FONT_PATH, size, index=0)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")

# 배경 그리드
for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

# 상단 강조선
draw.rectangle([0, 0, W, 4], fill=CYAN)

# ── 태그 ──
draw.rounded_rectangle([32, 22, 310, 52], radius=15, fill=BLUE_BG)
draw.rounded_rectangle([32, 22, 310, 52], radius=15, outline=BLUE_DIM, width=1)
draw.text((50, 30), "MEMORY ETF · 2026.04 출시", font=font(14), fill=CYAN)

# ── 타이틀 ──
draw.text((32, 66), "$DRAM", font=bold(62), fill=CYAN)
draw.text((32, 138), "Roundhill Memory ETF", font=bold(28), fill=WHITE)
draw.text((32, 178), "삼전 · 하닉 · MU  —  메모리 3강을 달러 계좌 하나로", font=font(18), fill=GRAY)

# 세로 구분선
draw.line([(530, 22), (530, H - 50)], fill=DARK_GRAY, width=1)

# ── 왼쪽 하단: 왜 이 ETF인가 ──
LX = 32
LY = 222
draw.text((LX, LY), "왜 이 ETF인가", font=bold(17), fill=GRAY)
draw.line([(LX, LY + 28), (498, LY + 28)], fill=DARK_GRAY, width=1)

points = [
    (CYAN,   "미국 계좌로 삼전·하닉 동시 접근",   "ADR·환전 없이 달러 계좌 하나로 해결"),
    (GREEN,  "메모리 사이클 전체에 베팅",          "누가 이기든 상관없다. 셋 다 담겨 있다"),
    (AMBER,  "단일 종목 25% 캡 자동 분산",         "쏠림 없이 분기마다 리밸런싱"),
]

py = LY + 44
for color, title, sub in points:
    draw.rounded_rectangle([LX, py, 498, py + 64], radius=8, fill=(20, 26, 36))
    draw.rectangle([LX, py, LX + 4, py + 64], fill=color)
    draw.text((LX + 18, py + 10), title, font=bold(17), fill=color)
    draw.text((LX + 18, py + 38), sub, font=font(14), fill=GRAY)
    py += 74

# ── 오른쪽: 구성종목 ──
RX = 558
RY = 22

draw.text((RX, RY), "주요 구성종목", font=bold(17), fill=GRAY)
draw.line([(RX, RY + 28), (W - 32, RY + 28)], fill=DARK_GRAY, width=1)

holdings = [
    ("SK하이닉스",   "17.7%", CYAN),
    ("삼성전자",     "12.9%", BLUE),
    ("Micron (MU)", "12.0%", PURPLE),
    ("Kioxia",       " 7.7%", AMBER),
    ("Sandisk",      " 5.8%", GREEN),
]

hy = RY + 44
ROW = (H - 100 - hy) // len(holdings)
for i, (name, pct, color) in enumerate(holdings):
    draw.rounded_rectangle([RX, hy, W - 32, hy + ROW - 6], radius=8, fill=(18, 24, 34))
    draw.rectangle([RX, hy, RX + 4, hy + ROW - 6], fill=color)

    # 비중 바
    bar_w = int(float(pct.strip().replace('%','')) / 20 * 360)
    draw.rounded_rectangle([RX + 18, hy + ROW - 20, RX + 18 + bar_w, hy + ROW - 10],
                            radius=3, fill=(*color[:3], 60))
    draw.rounded_rectangle([RX + 18, hy + ROW - 20, RX + 18 + bar_w, hy + ROW - 10],
                            radius=3, fill=color)

    draw.text((RX + 18, hy + 10), name, font=bold(18), fill=WHITE)
    draw.text((W - 100, hy + 10), pct, font=bold(22), fill=color)
    hy += ROW

# ── 하단 ──
draw.line([(32, H - 46), (W - 32, H - 46)], fill=DARK_GRAY, width=1)
draw.text((32, H - 32), "2026.06.15  ·  Roundhill Investments", font=font(15), fill=(50, 68, 90))
draw.text((W - 340, H - 32), "#DRAM #메모리ETF #반도체 #미국주식", font=font(15), fill=(50, 68, 90))

out = os.path.join(OUT_DIR, "2026-06-15_DRAM_ETF.png")
img.save(out, "PNG")
print("Saved:", out)
