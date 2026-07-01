from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-01"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,22), "SATL, 왜 분석은 남에게 맡기나", font=bold(40), fill=ACCENT)
draw.text((32,80), "가장 싸게 찍는 회사가 가장 적게 버는 이유", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "핵심", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "돈이 되는 마진은 사진이 아니라, 그 사진을 '읽어낸 판단'에 있다",
          font=bold(20), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, RED, (40,16,16), "세틀로직  매출 $17.7M",
     "가장 싸게(위성 1기 <$100만), 가장 조밀하게 찍는다", "그런데 셋 중 가장 적게 번다 · 픽셀만 팔아서")
band(by+step, bh, GREEN, (10,32,24), "BlackSky  매출 $106.6M",
     "위성은 더 적은데 매출은 6배", "Spectra AI로 '무슨 일인가'를 읽어 국방에 판다")
band(by+step*2, bh, BLUE, (12,20,38), "Planet  매출 $244M",
     "매일 전지구를 통째로 다시 찍는 규모", "픽셀은 흔해지는 중 · 마진은 위쪽(해석)에")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.01  |  FY2025 매출, stockanalysis.com  |  파트너십은 후퇴가 아니라 분업", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-01_SATL_데이터레이어_매출역설.png")
img.save(out); print("Saved:", out)
