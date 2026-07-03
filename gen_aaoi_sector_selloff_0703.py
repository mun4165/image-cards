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

draw.text((32,22), "AAOI, 하루 만에 -17%", font=bold(40), fill=ACCENT)
draw.text((32,80), "회사 악재 없었다 · 원인은 섹터 전체 밸류에이션 리셋", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

# 핵심 밴드 — 급락 스냅샷
ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "7/2 종가", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "$120.95   -12.99%   ·   장중 저점 $114.93 (-17%)",
          font=bold(20), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, ORANGE, (40,24,10), "함께 빠짐",
     "Coherent -10% · Lumentum -10%, 같은 날 동반 하락", "업종 전체가 맞은 매물, AAOI만의 문제 아님")
band(by+step, bh, RED, (40,16,16), "재료 소멸",
     "AAOI 연초 대비 +233% · 이미 많이 오른 상태", "위험회피 하루에 적자 고성장주부터 팔림")
band(by+step*2, bh, BLUE, (12,20,38), "남는 리스크",
     "GAAP 적자 지속 · 고객 상위 10곳=매출 98%", "급락과 무관하게 이전부터 있던 구조적 리스크")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.03  |  종가 stockanalysis.com  |  캐파·가이던스 확장 로드맵은 하락 이전과 동일", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-03_AAOI_섹터리셋_17퍼급락.png")
img.save(out); print("Saved:", out)
