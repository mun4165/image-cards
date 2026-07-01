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

draw.text((32,22), "국민연금 리밸런싱, 72조 매도 폭탄?", font=bold(40), fill=ACCENT)
draw.text((32,80), "목표비중이 아니라 '허용상단'을 넘는 부분이 진짜 매도다", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "72조의 정체", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "목표비중 20.8%에 '딱 맞춘다'는 가정의 초과액 · 실제 매도액 아님",
          font=bold(20), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "허용상단",
     "8,500선 매도 필요액은 14.7조 ~ 51조 범위", "기준(28.8 / 27.8 / 26.8%)에 따라 달라짐")
band(by+step, bh, BLUE, (12,20,38), "진짜 변수",
     "코스피 레벨이 아니라 국내·해외 상대강도", "동반 상승장이면 분모가 매도 부담을 흡수")
band(by+step*2, bh, AMBER, (40,30,8), "결론",
     "매도 폭탄 아닌 '조건부 수급 브레이크'", "국내 독주 구간에서만 8,500 위가 무거워진다")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.01  |  시장을 누르는 기관이 아니라, 상승에서 초과비중을 더는 공급자", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-01_국민연금_리밸런싱_브레이크.png")
img.save(out); print("Saved:", out)
