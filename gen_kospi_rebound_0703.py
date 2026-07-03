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

draw.text((32,22), "코스피 하루 만에 +5.76% 급반등", font=bold(38), fill=ACCENT)
draw.text((32,80), "오전에 짚은 그 신호, 진짜 왔다", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

# 핵심 밴드 — 마감 스냅샷
ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "7/3 종가 8,088.34", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "+440.25p (+5.76%)   ·   일중 7,378 → 8,136",
          font=bold(20), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, GREEN, (10,32,24), "반등 주도",
     "삼성전자 +8.22% · SK하이닉스 +10.88%", "반도체 저가매수가 지수 반등을 견인")
band(by+step, bh, BLUE, (12,20,38), "원달러도 되돌림",
     "1,544원 → 1,530원대, 원화 강세", "7/1 장중고점 1,559원 대비 20원 넘게 하락")
band(by+step*2, bh, ORANGE, (40,24,10), "판단은 아직",
     "저가매수 vs 추세전환, 하루로는 구분 안 됨", "다음 확인 지점 — 7/7 삼성전자 잠정실적")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.03  |  KOSPI·환율 종가 기준, 전일종가 7,648.09 · 1,544.07원", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-03_코스피_급반등_5.76퍼.png")
img.save(out); print("Saved:", out)
