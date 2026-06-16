from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-14"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 2560, 1440
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
CYAN      = (6, 182, 212)

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")

# 그리드
for x in range(0, W, 160):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 160):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

# 테두리 바
draw.rectangle([0, 0, W, 8], fill=CYAN)
draw.rectangle([0, H - 8, W, H], fill=CYAN)
draw.rectangle([0, 0, 8, H], fill=CYAN)

# 유튜브 안전 영역 중심 (모든 기기에서 보이는 구간)
# x: 507~2053 / y: 509~932
SAFE_CX = W // 2   # 1280
SAFE_CY = H // 2   # 720

# 구분선
draw.line([(507, SAFE_CY - 175), (2053, SAFE_CY - 175)], fill=DARK_GRAY, width=1)
draw.line([(507, SAFE_CY + 175), (2053, SAFE_CY + 175)], fill=DARK_GRAY, width=1)

# 제목
title = "조용한 간호사"
tf = bold(148)
tb = draw.textbbox((0, 0), title, font=tf)
tw = tb[2] - tb[0]
th = tb[3] - tb[1]
draw.text((SAFE_CX - tw // 2, SAFE_CY - th - 28), title, font=tf, fill=WHITE)

# 태그라인
tagline = "공시 뜯고, 공급망 추적하고, 스몰캡 공부합니다"
sf = font(54)
sb = draw.textbbox((0, 0), tagline, font=sf)
sw = sb[2] - sb[0]
draw.text((SAFE_CX - sw // 2, SAFE_CY + 28), tagline, font=sf, fill=CYAN)

out = os.path.join(OUT_DIR, "2026-06-14_조용한간호사_유튜브배너.png")
img.save(out)
print("Saved:", out)
