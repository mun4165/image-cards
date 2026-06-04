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

for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

draw.rectangle([0, 0, W, 4], fill=RED)
draw.rectangle([0, 0, 4, H], fill=RED)

# ── 헤더 ──
draw.text((32, 14), "$AVGO  Q2 FY2026 실적 정리", font=bold(38), fill=WHITE)
draw.text((32, 62), "2026.06.03 장 마감 후 발표  |  시간외 -8%", font=font(19), fill=RED)
draw.line([(32, 94), (W - 32, 94)], fill=DARK_GRAY, width=1)

# ── 왼쪽: Q2 실적 ──
draw.text((32, 106), "Q2 실적", font=bold(20), fill=GRAY)

q2 = [
    ("총 매출",         "$22.19B",  "+48% YoY",    "컨센 $22.27B — 소폭 미달",  ORANGE),
    ("AI 반도체",       "$10.8B",   "+143% YoY",   "가이던스 $10.7B 상회 ✅",   GREEN),
    ("소프트웨어",      "$7.18B",   "+9% YoY",     "컨센 $7.32B — 미달 ⚠️",    RED),
    ("Non-GAAP EPS",   "$2.44",    "+54% YoY",    "컨센 $2.40 상회 ✅",        GREEN),
]
y = 136
for label, value, yoy, sub, color in q2:
    draw.text((32, y), label, font=font(15), fill=GRAY)
    draw.text((32, y + 18), value, font=bold(26), fill=color)
    draw.text((200, y + 24), yoy, font=font(14), fill=color)
    draw.text((32, y + 48), sub, font=font(14), fill=GRAY)
    draw.line([(32, y + 68), (580, y + 68)], fill=DARK_GRAY, width=1)
    y += 76

# ── 세로 구분선 ──
draw.line([(608, 94), (608, H - 44)], fill=DARK_GRAY, width=1)

# ── 오른쪽: Q3 가이던스 ──
draw.text((628, 106), "Q3 가이던스  —  시장 예상 대폭 상회", font=bold(20), fill=GRAY)
draw.line([(628, 134), (W - 32, 134)], fill=DARK_GRAY, width=1)

q3 = [
    ("총 매출",       "$29.4B",  "+84% YoY",  "컨센서스 $23B 대폭 초과",   CYAN),
    ("AI 반도체",     "$16.0B",  "+200%+ YoY","QoQ +48%  /  Q2 $10.8B →", PURPLE),
    ("EBITDA 마진",   "~68%",    "유지",       "수익성 견조",               AMBER),
]
y = 148
for label, value, yoy, sub, color in q3:
    draw.text((628, y), label, font=font(15), fill=GRAY)
    draw.text((628, y + 18), value, font=bold(30), fill=color)
    draw.text((628, y + 52), f"{yoy}  ·  {sub}", font=font(15), fill=GRAY)
    draw.line([(628, y + 76), (W - 32, y + 76)], fill=DARK_GRAY, width=1)
    y += 88

# 수주잔고 강조
draw.rounded_rectangle([628, y + 4, W - 32, y + 54], radius=8, fill=(20, 40, 20))
draw.text((644, y + 14), "AI 수주잔고(Bookings)  $30B+  —  출하 $10.8B의 2.8배", font=bold(18), fill=GREEN)

# ── 하락 이유 배너 ──
draw.rounded_rectangle([32, H - 78, W - 32, H - 46], radius=6, fill=(40, 15, 15))
draw.text((48, H - 68), "시간외 하락 이유 :  ① VMware 소프트웨어 미스  ② 연간 AI 가이던스 미상향  ③ YTD +40% 고점 매도", font=bold(16), fill=RED)

draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.03  |  Broadcom IR 공식 발표 기준  |  개인 공부 기록", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-03_AVGO_실적정리.png")
img.save(out)
print("Saved:", out)
