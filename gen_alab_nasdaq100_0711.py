from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-11"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "ALAB 나스닥100 편입", font=bold(27), fill=ACCENT)
draw.text((32,80), "로켓랩과 같은 날, PER은 279배", font=bold(24), fill=GRAY)
draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
    draw.line([(250,y+18),(250,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((278, y+22), headline, font=bold(23), fill=WHITE)
    draw.text((278, y+64), d1, font=font(18), fill=color)
    draw.text((278, y+96), d2, font=font(17), fill=GRAY)

by = 150; bh = 152; step = 170
band(by, bh, GREEN, (10,28,20), "지수 편입",
     "2026.6.22 나스닥100 편입 (로켓랩·코어위브 동시)",
     "동시에 러셀2500에서는 제외",
     "시가총액 707.9억달러 (7/10 기준)")
band(by+step, bh, CYAN, (10,24,30), "실적",
     "1분기 매출 3.084억달러, 사상 최대",
     "전년비 +93%, 순이익 +152%",
     "2분기 가이던스 3.55~3.65억달러")
band(by+step*2, bh, RED, (40,15,15), "밸류에이션 리스크",
     "PER 279배",
     "5개 고객이 매출 12%+씩 차지",
     "엔비디아·하이퍼스케일러 의존")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.11  |  ALAB  Astera Labs", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-11_ALAB_나스닥100편입.png")
img.save(out); print("Saved:", out)
