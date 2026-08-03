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
draw.text((32,22), "총마진 50.1%, 관세환급 걷으면 48.1%", font=bold(25), fill=TEAL)
draw.text((32,74), "매출 EPS 다 이겼는데 시간외 6%대 하락한 이유", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, GREEN, (10,30,22), "실적  |  매출 EPS 서프라이즈",
     "매출 1,094억달러 · EPS 2.02달러, 컨센서스 상회", "매출 +16% · EPS +29%, 헤드라인은 완승")
band(draw, by+step, bh, ORANGE, (44,20,10), "마진  |  관세환급 +2%p",
     "총마진 50.1% · 가이던스 하단 47.5%", "환급 걷어내면 실질 마진 약 48.1%")
band(draw, by+step*2, bh, RED, (40,14,14), "부진  |  서비스·아이패드",
     "서비스 307억달러(컨센 314억) · 아이패드 62억(컨센 69억)", "서비스 성장률 12.1%, 아이폰 21.7%보다 낮음")
band(draw, by+step*3, bh, BLUE, (10,20,40), "가이던스  |  공급 제약 경고",
     "다음분기 supply constraints 언급", "아이폰 잘 나온 직후 나온 조심스러운 톤")
band(draw, by+step*4, bh, TEAL, (10,32,30), "주가  |  시간외 -6%대",
     "실적 서프라이즈에도 급락", "가이던스 톤이 헤드라인 숫자를 압도")
footer(draw, "2026.07.31  |  AAPL 애플  FY26 3분기 실적발표")
out = os.path.join(OUT_DIR, "2026-07-31_AAPL_실적발표_총마진관세환급.png")
img.save(out); print("Saved:", out)
