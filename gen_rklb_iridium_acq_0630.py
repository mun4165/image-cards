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

draw.text((32,22), "RKLB, 이리디움 80억 달러 인수", font=bold(40), fill=ACCENT)
draw.text((32,80), "로켓 회사가 통신사를 산 게 아니라 '발사 고객'을 샀다", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "핵심", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "주당 54달러·현금+주식·브릿지론 36억 달러 / 2027년 중반 종결",
          font=bold(22), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "효과 1 · 화물",
     "위성 보충발사를 자기 로켓으로 내재화", "발사 회사 최대 약점 '쏠 게 있느냐'를 식구로 메움")
band(by+step, bh, BLUE, (12,20,38), "효과 2 · 현금",
     "적자 체질에 캐시카우를 붙임", "2025 매출 8.7억·OEBITDA 4.95억·마진 57%")
band(by+step*2, bh, AMBER, (40,30,8), "효과 3 · 해자",
     "돈 주고 못 사는 L밴드 주파수", "신규 진입자가 새로 못 사는 자원 — 통째로 사는 길뿐")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.30  |  성장의 가속이 아니라 토대의 강화 · 실현은 뉴트론에 달림", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-30_RKLB_이리디움인수효과.png")
img.save(out); print("Saved:", out)
