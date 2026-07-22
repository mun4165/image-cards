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

draw.text((32,24), "AAOI 월 4.71억달러 매출설", font=bold(27), fill=ACCENT)
draw.text((32,80), "회사가 말한 적 없다", font=bold(24), fill=GRAY)
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
band(by, bh, GREEN, (10,28,20), "회사 발표",
     "2026년 연매출 11억달러 초과 (5/7 실적발표)",
     "비GAAP 영업이익 1.4억달러 이상",
     "1분기 매출 1.51억달러, 전년비 +51%")
band(by+step, bh, ORANGE, (40,24,10), "SNS 주장",
     "\"2027년 하반기 월매출 4.71억달러\"",
     "출처는 시킹알파 기고자의 자체 계산 모델",
     "회사가 낸 가이던스 아님")
band(by+step*2, bh, RED, (40,15,15), "숫자 대조",
     "월 4.71억 연환산 시 약 56.5억달러",
     "회사 가이던스의 5배, 최근 12개월 매출의 11배",
     "가이던스와 추정 모델은 다른 카테고리")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.11  |  AAOI  Applied Optoelectronics", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-11_AAOI_가이던스팩트체크.png")
img.save(out); print("Saved:", out)
