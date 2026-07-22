from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-12"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "라이트패스·로켓랩 인수설 파다가 정리한 개념", font=bold(20), fill=GRAY)
draw.text((32,58), "ITAR(국제무기거래규정) / non-ITAR / NDAA(국방수권법)", font=bold(26), fill=ACCENT)
draw.line([(32,110),(W-32,110)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(22), fill=color)
    draw.line([(250,y+16),(250,y+h-16)], fill=DARK_GRAY, width=1)
    block_h = 30+14+28+12+26
    ty = y + (h-block_h)//2
    draw.text((276, ty), headline, font=bold(21), fill=WHITE)
    draw.text((276, ty+42), d1, font=font(17), fill=color)
    draw.text((276, ty+76), d2, font=font(16), fill=GRAY)

by = 128
avail = (H-30) - by - 20
step = avail // 3
bh = step - 16

band(by, bh, ORANGE, (40,24,10), "ITAR",
     "미국인만 만들 수 있는 물건 카테고리",
     "라이트패스 열상렌즈=美등록공장, 로켓랩 발사체=美-NZ 조약(TSA)",
     "중국 웨이브렝스는 같은 유리 만들어도 이 카테고리라 배제")
band(by+step, bh, GREEN, (10,28,20), "non-ITAR",
     "그 규칙 자체를 안 받는 설계 전략",
     "세틀로직 NextGen — 美통제부품 빼고 설계, 수출허가 없이 전세계 판매",
     "해외 국방고객과 1,200만달러 위성계약 체결")
band(by+step*2, bh, CYAN, (10,20,34), "NDAA",
     "물건이 아니라 이름 찍힌 회사만 배제",
     "889=화웨이·ZTE(통신) / 5949=SMIC·창신메모리·YMTC(반도체)",
     "정부조달 한정이라 애플 아이폰(민간용) 테스트는 대상 자체가 아님")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.12  |  LPTH  RKLB  SATL  개념정리", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-12_ITARNDAA_X포스팅카드.png")
img.save(out); print("Saved:", out)
