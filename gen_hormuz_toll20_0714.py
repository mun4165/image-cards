from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-14"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(239,68,68)
ACCENT = ORANGE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "호르무즈 해협 통행료 20%", font=bold(22), fill=GRAY)
draw.text((32,58), "원래 이란이 매기려던 요금이었다", font=bold(30), fill=ACCENT)
draw.line([(32,110),(W-32,110)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(20), fill=color)
    draw.line([(280,y+16),(280,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((306, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((306, y+56), d1, font=font(16), fill=color)
    draw.text((306, y+84), d2, font=font(15), fill=GRAY)

by = 130; bh = 172; step = 188
band(by, bh, ORANGE, (40,24,10), "통행료",
     "VLCC 한 척당 약 3,000만 달러",
     "원화 약 450억원, 화물가액의 20%",
     "2026.07.13 트럼프 트루스소셜 발표")
band(by+step, bh, RED, (40,14,14), "유가 반응",
     "브렌트유 하루 약 8% 급등, 82달러 돌파",
     "WTI는 9.4% 올라 78달러 근접",
     "물동량은 하루 18~22척에서 6척으로 급감")
band(by+step*2, bh, CYAN, (10,28,32), "법적 문제",
     "IMO, 강제 통행료 법적 근거 없다고 반대",
     "6월 휴전 조건은 오히려 이란의 요금부과 금지였다",
     "미국은 정작 유엔해양법협약(UNCLOS) 비준국 아님")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.14  |  호르무즈 해협  국제유가", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-14_호르무즈_통행료20%_대표이미지.png")
img.save(out); print("Saved:", out)
