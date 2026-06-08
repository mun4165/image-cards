from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-09"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
RED       = (239, 68, 68)
AMBER     = (245, 158, 11)
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

# 그리드
for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

# 테두리
draw.rectangle([0, 0, W, 4], fill=RED)
draw.rectangle([0, 0, 4, H], fill=RED)

# ── 헤더 ──
draw.text((32, 14), "좋은 회사 ≠ 좋은 주식", font=bold(40), fill=WHITE)
draw.text((32, 64), "2026.06.09  |  자본 구조가 주주 수익률을 결정한다", font=font(18), fill=RED)
draw.line([(32, 98), (W - 32, 98)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 독성 구조 3가지 ──
CONTENT_TOP = 114
CONTENT_BOT = H - 52
LEFT_W = 590

draw.text((32, CONTENT_TOP), "독성 구조", font=bold(17), fill=GRAY)

toxic = [
    (RED,    "ATM 무한 희석",
             "IREN  시총 $22B  →  ATM $6B",
             "SLNH  시총 $250M  →  ATM $500M  (시총의 2배)"),
    (AMBER,  "고금리 부채",
             "CRWV  부채 $17.3B  /  연 이자 $1.2B",
             "Q1 한 분기 이자만 $536M  —  FCF가 채권자에게 간다"),
    (PURPLE, "SBC 희석",
             "SNAP·BKKT 류  —  조정기준 흑자, GAAP 기준 희석",
             "임직원 보수를 주식으로 지급  →  주주 지분 계속 감소"),
]

item_h = (CONTENT_BOT - CONTENT_TOP - 28) // 3
y = CONTENT_TOP + 28
for color, title, line1, line2 in toxic:
    draw.rounded_rectangle([32, y, LEFT_W, y + item_h - 8], radius=8, fill=(20, 24, 34))
    draw.rectangle([32, y, 38, y + item_h - 8], fill=color)
    draw.text((52, y + 10), title, font=bold(19), fill=color)
    draw.text((52, y + 42), line1, font=font(15), fill=WHITE)
    draw.text((52, y + 68), line2, font=font(13), fill=GRAY)
    y += item_h

# ── 세로 구분선 ──
draw.line([(620, 98), (620, CONTENT_BOT)], fill=DARK_GRAY, width=1)

# ── 오른쪽 ──
RX = 640
draw.text((RX, CONTENT_TOP), "좋은 구조 vs 스크리닝", font=bold(17), fill=GRAY)

# NBIS 박스
nbis_h = int((CONTENT_BOT - CONTENT_TOP - 28) * 0.42)
ny = CONTENT_TOP + 28
draw.rounded_rectangle([RX, ny, W - 32, ny + nbis_h], radius=8, fill=(14, 26, 20))
draw.rounded_rectangle([RX, ny, W - 32, ny + nbis_h], radius=8, outline=GREEN, width=1)
draw.text((RX + 18, ny + 10), "NBIS  —  좋은 구조의 기준", font=bold(17), fill=GREEN)
draw.text((RX + 18, ny + 42), "엔비디아 직접 자금 조달  +  전환사채 혼합", font=font(15), fill=WHITE)
draw.text((RX + 18, ny + 68), "희석 압력 최소  /  YTD  +153%", font=bold(18), fill=GREEN)

# 스크리닝 체크리스트
cy = ny + nbis_h + 14
check_h = CONTENT_BOT - cy
draw.rounded_rectangle([RX, cy, W - 32, CONTENT_BOT], radius=8, fill=(18, 22, 32))

draw.text((RX + 18, cy + 10), "스크리닝 체크리스트", font=bold(16), fill=CYAN)

checks = [
    (AMBER, "ATM 규모 / 시총  ≥ 50%"),
    (RED,   "연 이자비용 / 매출  →  FCF 소진 속도"),
    (PURPLE,"SBC / 조정 영업이익  →  진짜 수익성"),
]
chy = cy + 40
row_h = (check_h - 50) // 3
for color, text in checks:
    draw.rounded_rectangle([RX + 14, chy, W - 46, chy + row_h - 6], radius=6, fill=(25, 28, 40))
    draw.rectangle([RX + 14, chy, RX + 20, chy + row_h - 6], fill=color)
    draw.text((RX + 30, chy + (row_h - 6) // 2 - 10), text, font=font(14), fill=WHITE)
    chy += row_h

# ── 하단 바 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.09", font=font(15), fill=GRAY)
draw.text((W - 500, H - 30), "자본 구조  |  ATM · 부채 · SBC · 희석", font=bold(15), fill=RED)

out = os.path.join(OUT_DIR, "2026-06-09_capital_structure.png")
img.save(out)
print("Saved:", out)
