from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-08-02"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

def base_canvas(accent):
    img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    draw.rectangle([0,0,W,4], fill=accent); draw.rectangle([0,0,4,H], fill=accent)
    return img, draw

def band(draw, y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(17), fill=color)
    draw.line([(268,y+14),(268,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((292, y+15), headline, font=bold(18), fill=WHITE)
    draw.text((292, y+45), detail, font=font(14), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

BY, BH, STEP = 122, 98, 110

img, draw = base_canvas(RED)
draw.text((32,22), "레오폴드 펀드, 4배 레버리지가 무너진 구조", font=bold(25), fill=RED)
draw.text((32,74), "방향은 맞았는데 크기에서 청산당한 이유", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, BLUE, (10,20,40), "포지션  |  연산 숏 · 메모리 롱",
     "SMH·엔비디아 등 풋 84.7억달러, 메모리는 롱", "같은 반도체 안에서 편이 갈린 구조")
band(draw, by+step, bh, RED, (40,14,14), "붕괴  |  헤지가 못 막은 낙폭",
     "SMH -24.6%인데 롱 종목은 -39~-55%", "섹터 헤지보다 본진이 두 배 빨리 무너짐")
band(draw, by+step*2, bh, ORANGE, (44,20,10), "마진콜  |  이틀이 모자랐다",
     "추가출자 공지 8/1, 브로커 기한 7/30", "4억 중 3억은 빚, 자기자본 먼저 소각")
band(draw, by+step*3, bh, TEAL, (10,32,30), "블록딜  |  시타델이 통째로 인수",
     "BofA·골드만·JP모건, 장전 단일거래로 이전", "공개매도 대신 소유주만 교체, 물량은 그대로")
band(draw, by+step*4, bh, GREEN, (10,30,22), "다음날  |  던져진 종목만 반등",
     "IREN +30.5% · 마이크론 +18.4% (7/30)", "강제매도 소멸이지 매도압력 소멸 아님")
footer(draw, "2026.08.02  |  레오폴드 애션브레너 펀드 청산 구조")
out = os.path.join(OUT_DIR, "2026-08-02_레오폴드_청산_4배레버리지구조.png")
img.save(out); print("Saved:", out)
