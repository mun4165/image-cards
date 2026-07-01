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

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,22), "Sivers(SIVE) 6억 크로나 증자", font=bold(40), fill=ACCENT)
draw.text((32,80), "희석은 3%뿐 — 진짜 봐야 할 건 따로 있다", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "지금 상황", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "4월 14.5 SEK → 지금 63 SEK · 시총 194억에 6억 증자 = 약 3% 희석",
          font=bold(21), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "나쁜 증자 아님",
     "성장 자금이다", "피크가에 기관 대상 발행 · 용처=InP 캐파 증설+R&D")
band(by+step, bh, RED, (40,16,16), "치어리딩 안 함",
     "경계할 것 셋", "올해만 반복 희석 · 파이프라인은 확정수주 아님 · 후속 증자 가능")
band(by+step*2, bh, BLUE, (12,20,38), "갈라서 볼 것",
     "진짜 리스크는 가격", "3% 희석이 아니라 1,400% 오른 밸류에이션이 핵심")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.01  |  증자에도 종류가 있다 — 희석 크기보다 가격과 용처를 본다", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-01_SIVE_6억크로나증자.png")
img.save(out); print("Saved:", out)
