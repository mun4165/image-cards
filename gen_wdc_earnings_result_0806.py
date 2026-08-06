from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-08-06"
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
    draw.line([(360,y+14),(360,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((384, y+15), headline, font=bold(18), fill=WHITE)
    draw.text((384, y+45), detail, font=font(14), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

BY, BH, STEP = 122, 98, 110

img, draw = base_canvas(BLUE)
draw.text((32,22), "웨스턴디지털 4분기, GAAP EPS 8.21달러의 진짜 정체", font=bold(25), fill=BLUE)
draw.text((32,74), "비GAAP은 3.56달러 — 차이는 SanDisk 지분 평가이익", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, BLUE, (10,20,40), "매출  |  컨센서스 상회",
     "37억4,700만달러, 전년비 +44% · 전분기比 +12%", "컨센서스 37억달러를 상회")
band(draw, by+step, bh, RED, (40,14,14), "EPS 괴리  |  GAAP 8.21 vs 비GAAP 3.56",
     "차이 4.65달러는 SanDisk 지분 평가이익 20.5억달러", "본업 수익성은 비GAAP EPS 3.56달러 쪽이 더 실질에 가깝다")
band(draw, by+step*2, bh, GREEN, (10,30,22), "마진  |  비GAAP 총마진 54.4%",
     "전년비 +1,310bp · 전분기比 +390bp 개선", "GAAP 기준 54.1%, 출하량 231EB(전년비 +22%)")
band(draw, by+step*3, bh, AMBER, (40,30,8), "출하  |  nearline 209EB, 전체의 90%",
     "데이터센터용 nearline 출하량 전년비 +23%", "40TB급 신제품 출하 시작, 자사주매입 6억7,200만달러")
band(draw, by+step*4, bh, ORANGE, (44,20,10), "watch  |  실적 상회에도 시간외 10%대 하락",
     "FY27 1분기 가이던스 매출 41억달러, 비GAAP EPS 4.00달러", "발표 전 주가가 이미 높은 기대 반영 — nearline 증가율 둔화가 신호")
footer(draw, "2026.08.06  |  Western Digital(WDC) 2026 회계연도 4분기 실적 발표")
out = os.path.join(OUT_DIR, "2026-08-06_WDC_실적결과.png")
img.save(out); print("Saved:", out)
