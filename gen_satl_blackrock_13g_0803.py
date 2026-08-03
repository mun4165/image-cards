from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-08-03"
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

img, draw = base_canvas(CYAN)
draw.text((32,22), "세틀로직에 블랙록 5.2%, 뭐가 다른가", font=bold(25), fill=CYAN)
draw.text((32,74), "13G 지분공시로 보는 지구관측 위성 3사 비교", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, CYAN, (10,28,32), "공시  |  7/30 신규 13G",
     "블랙록 SATL 721.8만주 보유, 5.2%", "발행주식 1.39억주 기준 문턱 694만주")
band(draw, by+step, bh, BLUE, (10,20,40), "비교  |  3사 블랙록 지분율",
     "SATL 5.2%  ·  PL 4.3%  ·  BKSY 없음", "PL은 문턱 아래, BKSY는 13G 자체 없음")
band(draw, by+step*2, bh, GREEN, (10,30,22), "시가총액  |  같은 업종 다른 체급",
     "SATL 5.3억달러  ·  BKSY 9.4억달러  ·  PL 73억달러", "PL이 SATL보다 10배 이상 큰 규모")
band(draw, by+step*3, bh, ORANGE, (44,20,10), "의미  |  13G는 수동적 보유",
     "경영개입 아닌 인덱스·ETF 편입 신호", "13D(경영참여)와 다른 문턱 통과 지표")
band(draw, by+step*4, bh, AMBER, (40,30,8), "체크  |  다음 확인 지점",
     "다음 13G/A에서 비중 증감, PL 5% 돌파여부", "숫자 하나로 펀더멘털 안 바뀜")
footer(draw, "2026.08.03  |  SATL 세틀로직  블랙록 13G 지분공시")
out = os.path.join(OUT_DIR, "2026-08-03_SATL_블랙록13G공시비교.png")
img.save(out); print("Saved:", out)
