from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-30"
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

draw.text((32,22), "DRAM, 메모리를 한 바구니에 담는 ETF", font=bold(40), fill=ACCENT)
draw.text((32,80), "삼성·하이닉스·키옥시아를 달러 한 번의 매수로", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "정체", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "티커 DRAM · 라운드힐 메모리 ETF · 미국 상장 / 사이클 분산 베팅",
          font=bold(22), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "묶음",
     "한국·일본·미국 메모리 제조사 한 번에", "삼성·SK하이닉스·키옥시아·샌디스크·마이크론")
band(by+step, bh, BLUE, (12,20,38), "이유",
     "AI가 빨아들이는 구조적 메모리 수요", "고대역폭메모리(HBM) 중심 슈퍼사이클 국면")
band(by+step*2, bh, AMBER, (40,30,8), "주의",
     "분산의 대가는 '한 방'을 포기하는 것", "환율·운용보수·내부 종목 비중은 사기 전 확인")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.30  |  사이클 방향엔 도구, 한 종목 폭발엔 안 맞는 옷", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-30_DRAM_메모리ETF.png")
img.save(out); print("Saved:", out)
