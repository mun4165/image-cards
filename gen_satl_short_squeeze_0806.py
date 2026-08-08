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

img, draw = base_canvas(AMBER)
draw.text((32,22), "SATL 공매도 급증, 숏스퀴즈로 이어질 구조인가", font=bold(25), fill=AMBER)
draw.text((32,74), "조건 3개 중 몇 개를 채웠는지 따져봤다", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, RED, (40,14,14), "잔고  |  5월대비 6월말 거의 두배",
     "1,181만주 → 2,093만주(6/30), float 16~17%", "시장 평균 대비 확연히 높은 숏 비중")
band(draw, by+step, bh, ORANGE, (44,20,10), "커버일수  |  4.28일로 급증",
     "6/15 1.95일 → 7/15 4.28일", "숏 물량 감소에도 거래량 급감이 되사기를 어렵게 함")
band(draw, by+step*2, bh, GREEN, (10,30,22), "트리거 후보  |  실적 서프라이즈",
     "매출 컨센서스 대비 +70%, 첫 영업흑자(8/5)", "숏 데이터는 7/15분까지 — 실적 후 반응 미확인")
band(draw, by+step*3, bh, BLUE, (10,20,40), "반례  |  6월 호재에도 숏은 안 물러남",
     "6/29 국방계약 +22% 급등에도 숏 잔고 더 늘어", "숏 논리=위성 대수, 매출증가로 안 풀리는 의심")
band(draw, by+step*4, bh, TEAL, (10,32,30), "watch  |  다음 결제일 데이터",
     "7/31 결제분 발표, 실적 이후 숏 방향 확인 지점", "10월 멀린 첫 발사가 진짜 트리거일 가능성")
footer(draw, "2026.08.06  |  Satellogic(SATL) 공매도 잔고 구조 분석")
out = os.path.join(OUT_DIR, "2026-08-06_SATL_숏스퀴즈구조.png")
img.save(out); print("Saved:", out)
