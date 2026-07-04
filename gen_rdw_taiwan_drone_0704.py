from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-04"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = ORANGE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,22), "RDW, 대만 해안경비대가 고른 무인기", font=bold(36), fill=ACCENT)
draw.text((32,76), "레드와이어 Penguin Mk2.5 VTOL 계약 타임라인", font=bold(21), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(180,y+14),(180,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((204, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((204, y+46), detail, font=font(15), fill=color)

by = 136; bh = 78; step = 86
band(by, bh, ORANGE, (40,24,10), "6/30 계약",
     "대만 Taiwan Color Optics 대상 공급 계약", "SemiLux 자회사, 최종수요처 대만 해안경비대, Tranche 1")
band(by+step, bh, CYAN, (8,28,34), "기체 제원",
     "Penguin Mk2.5, VTOL(수직이착륙)", "EO/IR 페이로드, 해상감시·야간정찰(ISR)")
band(by+step*2, bh, BLUE, (12,20,38), "주가 반응",
     "6/30 +4.62% -> 7/1 -2.13% -> 7/2 -5.51%", "발표 당일 반짝, 이틀 만에 상승분 반납")
band(by+step*3, bh, RED, (40,14,14), "남는 질문",
     "계약금액 비공시", "Tranche 1 표현, 후속 물량 확대 여부가 관건")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.04  |  RDW  Redwire Corporation", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-04_RDW_대만해안경비대드론계약.png")
img.save(out); print("Saved:", out)
