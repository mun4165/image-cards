from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-05"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = BLUE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,22), "세레브라스 롤러코스터", font=bold(36), fill=ACCENT)
draw.text((32,76), "+19% → -7.4%, 진짜 구조는 AWS와의 경쟁이다", font=bold(21), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(196,y+14),(196,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((220, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((220, y+46), detail, font=font(15), fill=color)

by = 136; bh = 92; step = 100
band(by, bh, GREEN, (10,30,20), "급등",
     "6/29 +19.04%, $216", "Morgan Stanley 목표가 $250 + ARK 매수")
band(by+step, bh, RED, (40,14,14), "급락",
     "7/2 -7.42%, $204.86", "섹터 전반 차익실현, 논리 철회 아님")
band(by+step*2, bh, CYAN, (8,28,34), "구조",
     "AWS Inferentia와 경쟁, Marvell 우회", "협력이 아니라 같은 티어의 병렬 경쟁")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.05  |  Cerebras Systems (CBRS)", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-05_CBRS_롤러코스터.png")
img.save(out); print("Saved:", out)
