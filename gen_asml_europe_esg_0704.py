from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-04"
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

draw.text((32,22), "ASML 중국매출 42%→19%, 반토막", font=bold(36), fill=ACCENT)
draw.text((32,76), "유럽이 ESG를 버린 진짜 이유", font=bold(21), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(196,y+14),(196,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((220, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((220, y+46), detail, font=font(15), fill=color)

by = 136; bh = 92; step = 100
band(by, bh, RED, (40,14,14), "멈춤",
     "그린 데이터센터 라벨 연기", "원자력 인정 여부, EU 10개국 내부 정치 — 미국과 무관")
band(by+step, bh, GREEN, (10,30,20), "가속",
     "데이터센터 인허가 2년 → 12개월", "CADA 명문화, 반도체 자국화 속도전")
band(by+step*2, bh, CYAN, (8,28,34), "증거",
     "ASML 중국향 시스템 매출 42%→36%→19%", "네덜란드 기업 기술, 수출은 미국 통제하에")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.04  |  ASML Holding N.V.", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-04_ASML_유럽ESG포기.png")
img.save(out); print("Saved:", out)
