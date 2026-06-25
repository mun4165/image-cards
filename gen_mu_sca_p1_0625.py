from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-25"
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

draw.text((32,22), "마이크론은 어떻게 다음 불황을 미리 막았나", font=bold(36), fill=ACCENT)
draw.text((32,74), "안 사도 돈 내는 계약 16건 — 구조 편 (1편)", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "가격에 바닥을 깔았다", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "SCA = 가격 하한(Floor)을 계약서에 박은 전략 고객계약", font=bold(25), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(22), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(21), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, GRAY, (26,28,32), "옛날 계약 (LTA)",
     "물량만 보장, 가격은 시장 따라 분기 조정", "값이 빠지면 마이크론도 같이 깎였다")
band(by+step, bh, GREEN, (10,32,24), "이번 계약 (SCA)  Floor",
     "값이 폭락해도 약속한 하한가에 사야 함", "하한만 적용돼도 역대 최고 마진 위라고 밝힘")
band(by+step*2, bh, AMBER, (40,22,10), "못 깨는 장치",
     "Take-or-Pay · 안 사도 돈 낸다", "이미 받은 현금예치만 180억 달러")

gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "여기까지 보면", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "마이크론이 사이클을 죽인 것 같다  →  그런데",
          font=bold(22), fill=CYAN)
draw.text((52,gy+74), "어닝콜이 작게 말한 숫자 하나가 남아 있다 — 2편에서",
          font=font(15), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.25  |  MU  Micron · FY3Q26 어닝콜 (1편)", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-25_MU_1편_안사도돈내는계약16건.png")
img.save(out); print("Saved:", out)
