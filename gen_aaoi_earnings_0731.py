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

img, draw = base_canvas(TEAL)
draw.text((32,22), "가이던스 60~80%인데 컨센서스는 26%", font=bold(25), fill=TEAL)
draw.text((32,74), "AAOI 8월 6일 실적, 관전포인트는 이 간극 하나", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, RED, (40,14,14), "1분기  |  가이던스 미스",
     "매출 1억5,114만달러(컨센 1억5,514만달러) · EPS -0.07달러", "매출·EPS 모두 예상 하회, 이번 실적의 전례")
band(draw, by+step, bh, TEAL, (10,32,30), "간극  |  성장률 차이",
     "경영진 가이던스 QoQ +60~80% · 컨센서스는 QoQ 약 +26%", "1억9,061만달러 컨센서스, 가이던스 하단에도 못 미치는 수준")
band(draw, by+step*2, bh, GREEN, (10,30,22), "근거  |  텍사스 증설",
     "펄랜드 캠퍼스 40만sqft 증설 · 3월 수주 2건 합산 2.5억달러+", "1.6T 2억달러+ · 800G 5,300만달러+, 증설의 직접 트리거")
band(draw, by+step*3, bh, ORANGE, (44,20,10), "자금  |  ATM 6억달러",
     "3월 한도 2.5억→5억→6억달러 증액 · 이미 약 2.48억달러 조달", "CEO 980만달러·임원 다수 6월 중 지분 매도와 같은 시기")
band(draw, by+step*4, bh, BLUE, (10,20,40), "리스크  |  재미스 시",
     "고정비 부담 증가 + ATM 추가 조달 우려 재부상", "가이던스 신뢰 자체가 쟁점으로 넘어가는 두 번째 미스")
footer(draw, "2026.07.31  |  AAOI  어플라이드 옵토일렉트로닉스 · 8/6 실적발표")
out = os.path.join(OUT_DIR, "2026-07-31_AAOI_8월6일실적_관전포인트.png")
img.save(out); print("Saved:", out)
