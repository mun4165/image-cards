from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-12"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); BLUE=(59,130,246)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "로켓랩-이리디움 인수 파다가 만난", font=bold(22), fill=GRAY)
draw.text((32,58), "국가안보 게이트 6가지", font=bold(30), fill=ACCENT)
draw.line([(32,110),(W-32,110)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(20), fill=color)
    draw.line([(280,y+16),(280,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((306, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((306, y+56), d1, font=font(16), fill=color)
    draw.text((306, y+84), d2, font=font(15), fill=GRAY)

by = 130; bh = 168; step = 184
band(by, bh, ORANGE, (40,24,10), "물건 자체",
     "ITAR / non-ITAR — 미국 전용이냐 자유판매냐",
     "라이트패스·로켓랩(ITAR) vs 세틀로직 NextGen(non-ITAR)",
     "물건 카테고리를 미국인 전용으로 묶느냐, 설계로 피해가느냐")
band(by+step, bh, GREEN, (10,28,20), "회사 이름",
     "NDAA / Entity List — 지정된 회사만 콕 찍어 배제",
     "NDAA889=화웨이·ZTE, NDAA5949=SMIC·CXMT·YMTC(정부조달 한정)",
     "애플-CXMT 진짜 관건은 Entity List 등재 여부")
band(by+step*2, bh, BLUE, (10,20,34), "지분·인수",
     "FOCI / CFIUS — 누가 회사를 쥐고 있는가",
     "로켓랩·세틀로직 지배구조 재편(FOCI) vs 브로드컴-퀄컴 무산(CFIUS)",
     "지배구조 심사냐, 인수거래 승인 여부냐")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.12  |  LPTH  RKLB  국가안보 게이트 개념정리", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-12_LPTH_RKLB_국가안보게이트6가지_대표이미지.png")
img.save(out); print("Saved:", out)
