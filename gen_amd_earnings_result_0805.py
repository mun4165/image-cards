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

img, draw = base_canvas(RED)
draw.text((32,22), "AMD 실적 다 넘겼는데 주가는 왜 9% 빠졌나", font=bold(25), fill=RED)
draw.text((32,74), "숫자는 좋았고, 문제는 헬리오스 램프업 시점이었다", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, GREEN, (10,30,22), "실적  |  매출·EPS 모두 컨센서스 상회",
     "매출 115.4억달러  ·  EPS 1.66달러(비GAAP)", "데이터센터 매출 67억달러, 전년비 +107%")
band(draw, by+step, bh, BLUE, (10,20,40), "가이던스  |  3분기도 컨센서스 상회",
     "매출 약 130억달러 ±3억, 전분기比 +13%", "총마진 56% 유지, 지난주 체크1 통과")
band(draw, by+step*2, bh, ORANGE, (44,20,10), "그런데  |  헬리오스는 아직 4분기부터",
     "출하는 이제 시작, 물량 램프업은 4분기", "\"이미 기여 중\"이 아니라 \"이제 시작\"")
band(draw, by+step*3, bh, CYAN, (10,28,32), "참고  |  앤트로픽 2GW 계약은 별개",
     "1단계 1GW는 2027년 상반기부터 시작", "이번 2·3분기 실적엔 반영 안 되는 미래")
band(draw, by+step*4, bh, RED, (40,14,14), "결론  |  기대와 정보의 간극이 매도 원인",
     "시간외 -8.8%, \"블로아웃 가이던스\" 기대 못미침", "실적 결함이 아니라 눈높이 문제였다")
footer(draw, "2026.08.05  |  AMD 2분기 실적 결과 (8/4 발표)")
out = os.path.join(OUT_DIR, "2026-08-05_AMD_실적결과분석.png")
img.save(out); print("Saved:", out)
