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

for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

draw.rectangle([0, 0, W, 4], fill=GREEN)
draw.rectangle([0, 0, 4, H], fill=GREEN)

# ── 헤더 ──
draw.text((32, 14), "BlackDiamond — 중국 수출통제를 피하는가", font=bold(38), fill=WHITE)
draw.text((32, 62), "2026.06.10  |  LPTH  |  BD6 조성 직접 확인", font=font(18), fill=GREEN)
draw.line([(32, 98), (W - 32, 98)], fill=DARK_GRAY, width=1)

CONTENT_TOP = 114
CONTENT_BOT = H - 52

# ── 왼쪽: BD6 조성 ──
LEFT_W = 520
draw.text((32, CONTENT_TOP), "BD6 조성", font=bold(18), fill=GRAY)

# 핵심 조성 박스
draw.rounded_rectangle([32, CONTENT_TOP + 28, LEFT_W, CONTENT_TOP + 160], radius=10, fill=(18, 30, 22))
draw.rounded_rectangle([32, CONTENT_TOP + 28, LEFT_W, CONTENT_TOP + 160], radius=10, outline=GREEN, width=2)
draw.text((32 + 36, CONTENT_TOP + 44), "As40Se60", font=bold(46), fill=GREEN)
draw.text((32 + 20, CONTENT_TOP + 108), "이진(Binary) 유리  —  원소 단 2개로 구성", font=font(16), fill=GRAY)
draw.text((32 + 20, CONTENT_TOP + 132), "비소(As) 40%  +  셀레늄(Se) 60%", font=font(15), fill=WHITE)

# 원소별 박스
elem_top = CONTENT_TOP + 176
elem_h = (CONTENT_BOT - elem_top) // 2 - 6

elems = [
    (CYAN,  "비소 (As)  40%",  "글로벌 분산 공급  /  중국 통제 비대상"),
    (BLUE,  "셀레늄 (Se)  60%", "주요 생산국 일본·독일·캐나다  /  중국 통제 비대상"),
]
ey = elem_top
for color, title, sub in elems:
    draw.rounded_rectangle([32, ey, LEFT_W, ey + elem_h], radius=8, fill=(20, 24, 34))
    draw.rectangle([32, ey, 38, ey + elem_h], fill=color)
    draw.text((52, ey + 12), title, font=bold(18), fill=color)
    draw.text((52, ey + 44), sub, font=font(14), fill=GRAY)
    ey += elem_h + 8

# ── 세로 구분선 ──
draw.line([(548, 98), (548, CONTENT_BOT)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 수출통제 체크 ──
RX = 568
draw.text((RX, CONTENT_TOP), "중국 수출통제 대상 vs BD6", font=bold(18), fill=GRAY)

controls = [
    ("게르마늄  (Ge)", "중국 수출통제 대상", "BD6 미함유", GREEN),
    ("갈륨  (Ga)",     "중국 수출통제 대상", "BD6 미함유", GREEN),
    ("안티모니  (Sb)", "중국 수출통제 대상", "BD6 미함유", GREEN),
    ("희토류",         "중국 수출통제 대상", "BD6 미함유", GREEN),
]

row_h = (CONTENT_BOT - CONTENT_TOP - 28) // 4 - 4
ry = CONTENT_TOP + 28
for mineral, status, result, color in controls:
    draw.rounded_rectangle([RX, ry, W - 32, ry + row_h], radius=8, fill=(18, 26, 20))
    draw.text((RX + 18, ry + 10), mineral, font=bold(17), fill=WHITE)
    draw.text((RX + 18, ry + 40), status, font=font(14), fill=RED)

    check_x = W - 180
    draw.rounded_rectangle([check_x, ry + 10, W - 42, ry + row_h - 10], radius=6, fill=(20, 40, 28))
    draw.text((check_x + 14, ry + 18), "✓  " + result, font=bold(14), fill=GREEN)
    ry += row_h + 6

# ── 하단 결론 바 ──
draw.line([(32, H - 52), (W - 32, H - 52)], fill=DARK_GRAY, width=1)
draw.rounded_rectangle([32, H - 48, W - 32, H - 8], radius=6, fill=(16, 28, 20))
draw.text((52, H - 38), "BD6는 중국 수출통제 대상 원소를 단 하나도 함유하지 않는다  —  공급망 자립 확인됨", font=bold(16), fill=GREEN)

out = os.path.join(OUT_DIR, "2026-06-10_LPTH_BD6_composition.png")
img.save(out)
print("Saved:", out)
