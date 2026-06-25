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

draw.text((32,22), "어닝콜이 작게 말한 숫자 — 묶인 건 20%뿐", font=bold(37), fill=ACCENT)
draw.text((32,74), "'5년 고마진 고정'의 함정, 진짜 승부처는 풀린 80% (2편)", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "계약은 진짜다, 다만 일부다", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "사이클을 없앤 게 아니라 바닥을 절반만 들어올렸다", font=bold(25), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(22), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(21), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, RED, (40,16,16), "빠진 숫자",
     "묶인 건 디램의 20% · 낸드의 1/3뿐", "나머지 80%는 여전히 시장가에 노출")
band(by+step, bh, ORANGE, (40,22,10), "풀린 80%의 위험",
     "AI 고객이 투자 줄이면 물량을 토해낸다", "묶이지 않은 가격이 같이 흔들린다")
band(by+step*2, bh, BLUE, (10,22,40), "그래서 봐야 할 것",
     "마이크론 숫자가 아니라 고객의 capex 계획", "위험을 없앤 게 아니라 고객에게 넘겼다")

gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "한 줄 요약", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "사이클을 계약서로 절반 막았다  →  나머지 절반이 승부처",
          font=bold(22), fill=CYAN)
draw.text((52,gy+74), "박힌 절반은 단단하다 · 좋은 실적일수록 반대편을 먼저 본다",
          font=font(15), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.25  |  MU  Micron · FY3Q26 어닝콜 (2편)", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-25_MU_2편_묶인건20퍼센트.png")
img.save(out); print("Saved:", out)
