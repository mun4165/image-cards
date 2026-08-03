from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-31"
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
    draw.text((60, y+14), label, font=bold(17), fill=color)
    draw.line([(268,y+14),(268,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((292, y+15), headline, font=bold(18), fill=WHITE)
    draw.text((292, y+45), detail, font=font(14), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

BY, BH, STEP = 122, 98, 110

img, draw = base_canvas(GREEN)
draw.text((32,22), "AXT 2분기 실적, 매출 컨센서스 40% 상회", font=bold(25), fill=GREEN)
draw.text((32,74), "인듐인화물 역대 최고 매출, 시간외 +30%", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, GREEN, (10,32,22), "매출  |  컨센서스 상회",
     "4760만달러 · 컨센서스 3410만~3480만달러 대비 +37~40%", "전년 동기 대비 +165%, 전분기 대비 +77%")
band(draw, by+step, bh, TEAL, (10,28,30), "수익성  |  총이익률 급등",
     "GAAP 총이익률 44.9% · 1분기 29.6%, 전년동기 8.0%", "비GAAP EPS 0.19달러, 컨센서스 0.07달러 대비 대폭 상회")
band(draw, by+step*2, bh, AMBER, (40,28,10), "InP  |  역대 최고 분기",
     "백로그 1억달러 초과 유지 · 수요가 공급을 초과", "캐파 목표 2026년말 6000만달러 → 2027년말 1억3000만달러")
band(draw, by+step*3, bh, BLUE, (10,20,40), "루멘텀 계약  |  아직 미반영",
     "6년 공급계약, 매출 인식은 2027년부터 시작", "이번 분기 기여는 경영진 표현으로 매우 제한적")
band(draw, by+step*4, bh, RED, (40,14,14), "3분기 가이던스 · 리스크",
     "매출 6600만달러 · 비GAAP EPS 0.30~0.32달러", "2차 증자 6억3250만달러로 희석, 중국 수출허가 불확실성 지속")
footer(draw, "2026.07.31  |  AXTI  AXT Inc.")
out = os.path.join(OUT_DIR, "2026-07-31_AXTI_2분기실적.png")
img.save(out); print("Saved:", out)
