from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-21"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); RED=(248,113,113); ORANGE=(249,115,22); BLUE=(59,130,246)

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
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(196,y+14),(196,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((220, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((220, y+46), detail, font=font(15), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

img, draw = base_canvas(RED)
draw.text((32,22), "키옥시아 왜 한달만에 반토막 났나", font=bold(32), fill=RED)
draw.text((32,76), "사상 최고실적인데 스톱안 맞은 이유를 짚었다", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, RED, (40,14,14), "낙폭",
     "6/22 112,700엔 → 7/17 스톱안 52,110엔", "고점 대비 -54%, 시가총액 약 30조엔 증발")
band(draw, by+step, bh, AMBER, (40,28,10), "트리거",
     "7/2 SK하이닉스 청주 낸드공장 80조원 발표", "키옥시아 연간 capex의 9~10배 규모")
band(draw, by+step*2, bh, ORANGE, (40,22,10), "증폭",
     "신용매수 강제청산 연쇄 (추가증거금 투매)", "10배 급등 구간에 쌓인 레버리지가 하락서 역작동")
band(draw, by+step*3, bh, BLUE, (10,20,40), "실적",
     "26년 3월기 매출 +37%, 영업이익 +93.4%", "8년만의 최고실적, 펀더멘털 악화 아님")
footer(draw, "2026.07.21  |  285A  Kioxia Holdings")
out = os.path.join(OUT_DIR, "2026-07-21_키옥시아반토막.png")
img.save(out); print("Saved:", out)
