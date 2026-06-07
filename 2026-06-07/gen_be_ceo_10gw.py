from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-07"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
GREEN     = (52, 211, 153)
AMBER     = (245, 158, 11)
CYAN      = (6, 182, 212)
RED       = (239, 68, 68)
PURPLE    = (167, 139, 250)

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

def base_canvas():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=GRID, width=1)
    draw.rectangle([0, 0, W, 4], fill=GREEN)
    draw.rectangle([0, 0, 4, H], fill=GREEN)
    return img, draw

img, draw = base_canvas()

# ── 헤더 ──
draw.text((32, 14), "BE", font=bold(40), fill=GREEN)
draw.text((100, 18), "블룸에너지 CEO — 2030년 10GW 테제, 숫자로 검증", font=bold(25), fill=WHITE)
draw.text((100, 56), "Bloom Energy  |  연료전지·클린에너지  |  2026.06.07", font=font(15), fill=GRAY)
draw.line([(32, 86), (W - 32, 86)], fill=DARK_GRAY, width=1)

# ── 왼쪽 ──
C1 = 32

# CEO 핵심 발언
draw.text((C1, 100), "CEO 핵심 발언", font=bold(18), fill=GREEN)
draw.line([(C1, 124), (590, 124)], fill=DARK_GRAY, width=1)

ceo_items = [
    (GREEN, "증설 비용",   "1GW당  $100 ~ 150M"),
    (GREEN, "공기",        "6개월 이내 완료"),
    (AMBER, "자금 조달",   "외부 조달 없이 자체 현금흐름으로 충당"),
    (AMBER, "이론상 속도", "연 1 ~ 2GW 증설 가능"),
]
y = 132
for color, label, val in ceo_items:
    draw.rectangle([C1, y + 6, C1 + 4, y + 20], fill=color)
    draw.text((C1 + 12, y), label, font=font(13), fill=GRAY)
    draw.text((C1 + 12, y + 20), val, font=bold(17), fill=color)
    y += 52

# 회사 현황
y += 4
draw.text((C1, y), "회사 현황", font=bold(18), fill=GREEN)
y += 24
draw.line([(C1, y), (590, y)], fill=DARK_GRAY, width=1)
y += 10

stats = [
    (CYAN,  "2025 매출",        "$2.02B   (+37% YoY)"),
    (CYAN,  "2026 가이던스",    "$3.4 ~ 3.8B"),
    (GREEN, "수주 잔고",        "$20B  백로그"),
    (AMBER, "Q1 2026 영업 CF",  "$73.6M  →  연환산 ~$295M"),
]
for color, label, val in stats:
    draw.rectangle([C1, y + 6, C1 + 4, y + 19], fill=color)
    draw.text((C1 + 12, y), label, font=font(13), fill=GRAY)
    draw.text((C1 + 12, y + 19), val, font=bold(16), fill=color)
    y += 46

# ── 중앙 구분선 ──
draw.line([(610, 86), (610, H - 46)], fill=DARK_GRAY, width=1)
C2 = 630

# ── 오른쪽 상단: 2030년 10GW 시뮬레이션 ──
draw.text((C2, 100), "2030년 10GW 시뮬레이션", font=bold(18), fill=AMBER)
draw.line([(C2, 124), (W - 32, 124)], fill=DARK_GRAY, width=1)

sim_items = [
    (GRAY,  "2026 말", "2GW", "확장 진행 중 (Fremont 확정)"),
    (AMBER, "2028",    "6GW", "+2GW/년 유지 시"),
    (GREEN, "2030",   "10GW", "CEO 테제 달성 시점"),
]
y2 = 132
for color, year, gw, note in sim_items:
    draw.rounded_rectangle([C2, y2, W - 32, y2 + 46], radius=4, fill=(20, 26, 36))
    draw.text((C2 + 14, y2 + 6), year, font=bold(15), fill=GRAY)
    draw.text((C2 + 90, y2 + 4), gw, font=bold(22), fill=color)
    draw.text((C2 + 170, y2 + 10), note, font=font(14), fill=GRAY)
    y2 += 54

# ── 오른쪽 중단: 재무 검증 ──
y2 += 4
draw.text((C2, y2), "재무 검증 — 자체 조달 가능한가", font=bold(18), fill=CYAN)
y2 += 24
draw.line([(C2, y2), (W - 32, y2)], fill=DARK_GRAY, width=1)
y2 += 10

draw.rounded_rectangle([C2, y2, W - 32, y2 + 62], radius=6, fill=(10, 28, 36))
draw.text((C2 + 14, y2 + 8),  "Q1 2026 영업 CF  $73.6M  →  연환산 ~$295M", font=font(15), fill=WHITE)
draw.text((C2 + 14, y2 + 32), "1GW 증설비 $100~150M  <  연간 CF  →  자체 조달 ✓", font=bold(15), fill=GREEN)
y2 += 74

# ── 오른쪽 하단: 3가지 전제 ──
y2 += 4
draw.text((C2, y2), "10GW가 실현되려면", font=bold(18), fill=PURPLE)
y2 += 24
draw.line([(C2, y2), (W - 32, y2)], fill=DARK_GRAY, width=1)
y2 += 10

prereqs = [
    (PURPLE, "백로그 $20B → $60B+ 수준으로 확대 필요"),
    (AMBER,  "Fremont 외 신규 부지·공장 확보"),
    (RED,    "AI 데이터센터 전력 수요 지속 여부"),
]
for color, text in prereqs:
    draw.rectangle([C2, y2 + 5, C2 + 4, y2 + 19], fill=color)
    draw.text((C2 + 12, y2), text, font=font(16), fill=GRAY)
    y2 += 30

# ── 하단 배너 ──
draw.rounded_rectangle([32, H - 68, W - 32, H - 10], radius=6, fill=(4, 24, 14))
draw.text((52, H - 58), "재무 구조는 검증됨  |  10GW는 Capability — 수요가 따라와야 Commitment가 된다", font=bold(15), fill=GREEN)
draw.text((52, H - 32), "2026.06.07  |  Bloom Energy IR · CEO 발언", font=font(13), fill=GRAY)

out_path = os.path.join(OUT_DIR, "2026-06-07_BE_CEO_10GW테제.png")
img.save(out_path)
print(f"Saved: {out_path}")
