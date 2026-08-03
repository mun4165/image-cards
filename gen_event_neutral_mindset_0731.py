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

BY, BH, STEP = 150, 118, 130

img, draw = base_canvas(TEAL)
draw.text((32,22), "사건은 가치중립적이다", font=bold(27), fill=TEAL)
draw.text((32,76), "판단은 감정이 붙이고, 의미는 다음 행동이 결정한다", font=bold(18), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, GRAY, (24,26,30), "출발점  |  동일한 사건",
     "손실 하나가 났다", "뇌는 자동으로 이걸 나쁜 일이라는 감정 라벨부터 붙인다")
band(draw, by+step, bh, RED, (40,14,14), "회피  |  손절 후 외면",
     "충동적으로 정리하고 다시는 안 본다", "복기 없는 손절은 같은 실수를 반복시킨다")
band(draw, by+step*2, bh, ORANGE, (40,26,10), "과신  |  무리한 만회",
     "복구하려고 베팅을 더 키운다", "레버리지가 대표적인 케이스, 작은 손실이 큰 파국이 된다")
band(draw, by+step*3, bh, GREEN, (10,32,22), "복기  |  판단 기준 수정",
     "왜 틀렸는지 다시 뜯어보고 기준을 고친다", "같은 손실이 다음 판단을 더 정교하게 만드는 재료가 된다")
footer(draw, "2026.07.31  |  투자 마인드")
out = os.path.join(OUT_DIR, "2026-07-31_사건은가치중립적이다.png")
img.save(out); print("Saved:", out)
