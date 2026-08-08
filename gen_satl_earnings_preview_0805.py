from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-08-05"
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

img, draw = base_canvas(CYAN)
draw.text((32,22), "SATL 8월 5일 실적, 봐야 할 건 매출이 아니다", font=bold(25), fill=CYAN)
draw.text((32,74), "1분기 첫 플러스 현금흐름이 이어지는지가 관건", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, CYAN, (10,28,32), "컨센서스  |  매출 성장은 이미 알려진 방향",
     "매출 933만달러  ·  전년비 약 110%", "EPS -0.03달러, 전년 -0.06달러에서 개선")
band(draw, by+step, bh, GREEN, (10,30,22), "1분기  |  창사 첫 영업현금흐름 플러스",
     "매출 610만달러(+80%)  ·  현금 1.22억달러", "조정 EBITDA 손실 420만달러, 32% 개선")
band(draw, by+step*2, bh, ORANGE, (44,20,10), "경영진 경고  |  \"touch and go\"",
     "향후 2~3분기 현금흐름 아슬아슬 예고", "멀린 위성군 자본지출 본격화 구간")
band(draw, by+step*3, bh, AMBER, (40,30,8), "주의  |  순손실 헤드라인 함정",
     "1분기 순손실 1.18억달러 중 1.13억 비현금", "금융상품 공정가치 변동, 영업과 무관")
band(draw, by+step*4, bh, BLUE, (10,20,40), "분기점  |  매출 넘겨도 현금 마이너스면",
     "성장은 맞지만 자금조달 재필요 신호", "영업현금흐름 부호가 매출보다 중요")
footer(draw, "2026.08.05  |  SATL 새틀로직 2분기 실적 발표 (장 마감 후)")
out = os.path.join(OUT_DIR, "2026-08-05_SATL_실적프리뷰.png")
img.save(out); print("Saved:", out)
