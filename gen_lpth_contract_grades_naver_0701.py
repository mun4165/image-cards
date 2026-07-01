from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-01"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = CYAN

def font(s, i=0): return ImageFont.truetype(FONT_PATH, s, index=i)
def bold(s): return ImageFont.truetype(FONT_PATH, s, index=4)

img = Image.new("RGB",(W,H),BG); d = ImageDraw.Draw(img,"RGBA")
for x in range(0,W,80): d.line([(x,0),(x,H)],fill=GRID,width=1)
for y in range(0,H,80): d.line([(0,y),(W,y)],fill=GRID,width=1)
d.rectangle([0,0,W,4],fill=ACCENT); d.rectangle([0,0,4,H],fill=ACCENT)

d.text((32,26),"계약이라고 다 같은 계약이 아니다",font=bold(42),fill=ACCENT)
d.text((32,84),"LPTH 라이트패스로 배우는 '계약 등급' 읽는 눈",font=bold(21),fill=GRAY)
d.line([(32,124),(W-32,124)],fill=DARK_GRAY,width=1)

rungs = [
    (GREEN,  "인수",              "계약·고객 통째 확보",  "가장 강함"),
    (TEAL,   "후속 주문",         "검증된 관계의 재주문",  "확정 매출"),
    (BLUE,   "EDM 개발 주문",     "프로그램 통합·시험",    "돈이 붙음"),
    (ORANGE, "퀄리피케이션 오더", "신규 고객 첫 유상 관문","돈이 붙음"),
    (RED,    "MOU 양해각서",      "'같이 해보자' 비구속",  "매출 0 · 말뿐"),
]
y0=142; h=98; gap=12
for i,(c,name,desc,tag) in enumerate(rungs):
    y=y0+i*(h+gap)
    d.rounded_rectangle([120,y,W-40,y+h],radius=12,fill=(c[0]//7,c[1]//7,c[2]//7))
    d.rectangle([120,y,128,y+h],fill=c)
    d.text((150,y+18),name,font=bold(28),fill=WHITE)
    d.text((150,y+58),desc,font=font(18),fill=GRAY)
    d.text((W-70-d.textlength(tag,font=bold(18)),y+20),tag,font=bold(18),fill=c)
d.text((44,150),"강",font=bold(24),fill=GREEN)
d.text((44,H-92),"약",font=bold(24),fill=RED)
d.line([(60,190),(60,H-96)],fill=DARK_GRAY,width=2)
d.polygon([(56,196),(64,196),(60,182)],fill=GREEN)

out = os.path.join(OUT_DIR,"2026-07-01_LPTH_계약등급사다리.png")
img.save(out); print("Saved:",out)
