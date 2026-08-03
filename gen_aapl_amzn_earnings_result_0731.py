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
draw.text((32,22), "애플 마진 방어, 아마존 capex 상향", font=bold(25), fill=TEAL)
draw.text((32,74), "같은 메모리 가격 상승, 두 회사엔 정반대로 나타났다", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, GREEN, (10,30,22), "애플  |  총마진 50.1%",
     "가이던스 하단 47.5% 상회 · 관세환급 +2%p 포함", "환급 걷어내면 실질 마진 약 48.1%")
band(draw, by+step, bh, RED, (40,14,14), "애플  |  시간외 -6%대",
     "매출 EPS 모두 컨센서스 상회했지만 급락", "다음분기 공급제약 경고가 가이던스 발목")
band(draw, by+step*2, bh, ORANGE, (44,20,10), "아마존  |  capex 2,200억달러",
     "2,000억→2,200억달러, 예상(2,100억) 웃돎", "메모리 가격 상승 근거, 채권 250억달러 발행")
band(draw, by+step*3, bh, TEAL, (10,32,30), "아마존  |  AWS 37% 성장",
     "18개분기 최고속도 · 영업마진 39.4%", "백로그 4,960억달러, 캐파 증설 압력도 동반")
band(draw, by+step*4, bh, BLUE, (10,20,40), "아마존  |  FCF 마이너스 전환",
     "트레일링12개월 잉여현금흐름 -76억달러", "전년 +182억달러에서 capex 급증으로 역전")
footer(draw, "2026.07.31  |  AAPL 애플 · AMZN 아마존  실적발표 결과")
out = os.path.join(OUT_DIR, "2026-07-31_AAPL_AMZN_실적발표결과_단일변수검증.png")
img.save(out); print("Saved:", out)
