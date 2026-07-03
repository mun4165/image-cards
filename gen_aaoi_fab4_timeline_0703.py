from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-03"
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

draw.text((32,22), "AAOI, 넉 달 새 네 번째 시설 투자", font=bold(38), fill=ACCENT)
draw.text((32,78), "2월~6월 대형 임대·보조금·클린룸 계약 타임라인", font=bold(21), fill=GRAY)
draw.line([(32,120),(W-32,120)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(180,y+14),(180,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((204, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((204, y+46), detail, font=font(15), fill=color)

by = 136; bh = 78; step = 86
band(by, bh, BLUE, (12,20,38), "2월",
     "휴스턴 블루리지 15만3,928sqft 130개월 임대", "매입권 행사가 약 3,026만 달러")
band(by+step, bh, TEAL, (8,28,26), "4월",
     "텍사스 반도체 혁신펀드 보조금 약 2,085만 달러", "슈가랜드 21만sqft 증설, 총 투자 2.79억 달러")
band(by+step*2, bh, ORANGE, (40,24,10), "5월",
     "휴스턴 3개 건물 73만6천sqft 123개월 임대", "매입권 행사가 합계 1억225만 달러")
band(by+step*3, bh, CYAN, (8,28,34), "6월",
     "FAB4 클린룸 설계-시공 계약 9,410만 달러", "ISO Class 6, 19만5,591sqft, 완공목표 2027.1")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.03  |  출처: 각 시점 8-K·보도자료  |  금액은 매입권 행사가·계약총액 기준", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-03_AAOI_FAB4_시설투자타임라인.png")
img.save(out); print("Saved:", out)
