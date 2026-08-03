from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-23"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

def base_canvas(accent):
    img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    draw.rectangle([0,0,W,4], fill=accent); draw.rectangle([0,0,4,H], fill=accent)
    return img, draw

def band(draw, y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(18), fill=color)
    draw.line([(228,y+14),(228,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((252, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((252, y+46), detail, font=font(15), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# ── INTC 2분기 실적: GAAP 적자의 정체 ──────────────────────────
img, draw = base_canvas(CYAN)
draw.text((32,22), "인텔 110억 달러 적자, 그런데 주가는 12% 뛰었다", font=bold(26), fill=CYAN)
draw.text((32,76), "GAAP 순손실의 정체와 파운드리 외부고객의 진실", font=bold(18), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, RED, (40,16,14), "GAAP 적자",
     "순손실 110억 달러, 주당 -2.16달러", "CHIPS Act 에스크로 주식 평가손실 125억 달러가 원인")
band(draw, by+step, bh, GREEN, (10,32,24), "실제 수익성",
     "비GAAP EPS 0.42달러, 예상의 2배", "영업이익률 17.2%, 전년 -3.9%에서 반전")
band(draw, by+step*2, bh, AMBER, (40,28,10), "매출 성장",
     "161억 달러, 전년비 +25%", "데이터센터·AI 부문 +59%가 견인, 2011년 이후 최고 성장률")
band(draw, by+step*3, bh, CYAN, (8,28,34), "파운드리",
     "첫 외부고객 Fortinet 공개, Intel 4 공정", "18A는 아직 이름 밝힌 외부고객 없음")
footer(draw, "2026.07.23  |  Intel Q2 2026 Earnings")
out = os.path.join(OUT_DIR, "2026-07-23_INTC_2분기실적적자정체.png")
img.save(out); print("Saved:", out)
