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

draw.text((32,22), "LPTH, 러셀2000·3000 동시 편입", font=bold(40), fill=ACCENT)
draw.text((32,80), "적외선 광학 스몰캡에 무슨 의미인가", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "정체", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "FTSE 러셀 6월 정기변경 · 6/29 효력 · 미국 시총 상위 약 4,000대 진입",
          font=bold(20), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "효과",
     "패시브 자금의 기계적 매수 + 유동성", "인덱스 펀드·ETF가 의무적으로 담는 수요 발생")
band(by+step, bh, BLUE, (12,20,38), "본체",
     "적외선 광학·카메라, 미국·동맹 공급", "매출 약 2배 · 1,820만 달러 IR 카메라 수주")
band(by+step*2, bh, AMBER, (40,30,8), "주의",
     "편입은 펀더멘털 개선이 아니다", "패시브 매수는 일회성 · 매출 늘며 손실도 확대")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.01  |  편입이라는 호재와 실적이라는 본질을 갈라서", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-01_LPTH_러셀편입.png")
img.save(out); print("Saved:", out)
