from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-17"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (60, 70, 82)
CARD      = (20, 27, 36)
AMBER     = (245, 158, 11)
TEAL      = (20, 184, 166)
BLUE      = (59, 130, 246)
CYAN      = (6, 182, 212)
GREEN     = (52, 211, 153)
RED       = (239, 68, 68)

ACCENT = CYAN

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

# ── 헤더 (표지형) ──
draw.text((40, 22), "게르마늄-프리 냉각 MWIR", font=bold(46), fill=ACCENT)
draw.text((40, 84), "중국이 쥔 소재 하나가 미국 국방 광학의 급소가 됐다", font=bold(25), fill=WHITE)
draw.text((40, 122), "MWIR = 중파장 적외선(3~5㎛) · 멀리 있는 표적을 정밀하게 식별하는 전장의 '눈'", font=font(18), fill=GRAY)
draw.line([(40, 156), (W - 40, 156)], fill=DARK_GRAY, width=1)

# ── 2×2 핵심 카드 ──
cells = [
    ("01", CYAN,  "MWIR이 뭔가",
     ["중파장 적외선 3~5㎛ 대역", "파장 짧아 장거리 정밀 식별에 유리"]),
    ("02", BLUE,  "냉각이 장거리의 열쇠",
     ["-196°C로 식혀 광자를 직접 검출", "비냉각식보다 민감도 수십 배"]),
    ("03", RED,   "게르마늄이 급소",
     ["정제 60%가 중국산 · 2023 수출통제", "열 오르면 초점 흔들림(dn/dT 큼)"]),
    ("04", GREEN, "해법 = 게르마늄-프리",
     ["칼코게나이드 유리 · 블랙다이아몬드", "기존 카메라에 그대로 '드롭인 교체'"]),
]

col_x = [40, 662]
row_y = [170, 380]
cw, ch = 578, 198
for i, (num, color, title, descs) in enumerate(cells):
    x = col_x[i % 2]
    y = row_y[i // 2]
    draw.rounded_rectangle([x, y, x + cw, y + ch], radius=12, fill=CARD)
    draw.rectangle([x, y + 12, x + 5, y + ch - 12], fill=color)  # 좌측 컬러바
    draw.text((x + 26, y + 22), num, font=bold(30), fill=color)
    draw.text((x + 80, y + 26), title, font=bold(27), fill=WHITE)
    draw.text((x + 26, y + 92), descs[0], font=font(19), fill=(205, 212, 222))
    draw.text((x + 26, y + 130), descs[1], font=font(19), fill=GRAY)

# ── 하단 한 줄 정리 ──
by = 600
draw.rounded_rectangle([40, by, W - 40, by + 56], radius=10, fill=(6, 30, 36))
draw.rectangle([40, by, 45, by + 56], fill=ACCENT)
draw.text((62, by + 14), "냉각 MWIR(멀리 보는 성능)  ×  게르마늄-프리(적성국 소재 0)  =  지금 미국 방산이 가장 원하는 교집합",
          font=bold(20), fill=CYAN)

# ── 푸터 ──
draw.text((40, H - 32), "2026.06.17  |  적외선 광학 · 게르마늄-프리 냉각 MWIR · LPTH BlackDiamond", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-17_LPTH_게르마늄프리냉각MWIR_네이버.png")
img.save(out)
print("Saved:", out)
