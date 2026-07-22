from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-15"
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

draw.text((32,22), "AAOI, 여섯 달 새 다섯 번째 시설 투자", font=bold(36), fill=ACCENT)
draw.text((32,76), "텍사스 펄랜드 40만 sqft 증설 소식에 주가 +12.13%", font=bold(21), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-12), label, font=bold(20), fill=color)
    draw.line([(184,y+16),(184,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((210, y+20), headline, font=bold(21), fill=WHITE)
    draw.text((210, y+56), detail, font=font(16), fill=color)

by = 132; bh = 98; step = 112
band(by, bh, BLUE, (12,20,38), "2월",
     "휴스턴 블루리지 15만3,928sqft 130개월 임대", "매입권 행사가 약 3,026만 달러")
band(by+step, bh, TEAL, (8,28,26), "4월",
     "텍사스 반도체 혁신펀드 보조금 약 2,085만 달러", "슈가랜드 21만sqft 증설, 총 투자 2.79억 달러")
band(by+step*2, bh, ORANGE, (40,24,10), "5월",
     "휴스턴 3개 건물 73만6천sqft 123개월 임대", "매입권 행사가 합계 1억225만 달러")
band(by+step*3, bh, AMBER, (38,28,8), "6월",
     "FAB4 클린룸 설계-시공 계약 9,410만 달러", "ISO Class 6, 19만5,591sqft, 완공목표 2027.1")
band(by+step*4, bh, CYAN, (8,28,34), "7월",
     "펄랜드 인접부지 2곳 약 40만sqft 신규 착공", "800G·1.6T 광트랜시버向, 투자·완공일 비공개")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.15  |  출처: 각 시점 8-K·보도자료  |  금액은 매입권 행사가·계약총액 기준", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-15_AAOI_펄랜드증설_대표이미지.png")
img.save(out); print("Saved:", out)
