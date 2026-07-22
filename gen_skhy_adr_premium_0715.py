from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-15"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(239,68,68)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "SKHY  ADR vs 원주 괴리율", font=bold(22), fill=GRAY)
draw.text((32,58), "하루 만에 프리미엄 51%로 확대", font=bold(30), fill=ACCENT)
draw.line([(32,110),(W-32,110)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(20), fill=color)
    draw.line([(280,y+16),(280,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((306, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((306, y+56), d1, font=font(16), fill=color)
    draw.text((306, y+84), d2, font=font(15), fill=GRAY)

by = 130; bh = 150; step = 166
band(by, bh, CYAN, (10,28,32), "급등",
     "ADR $193.92, 전일比 +27.29%",
     "2026.07.14 나스닥 종가 (전일 $152.35)",
     "예탁비율 1:10, ADR 10주 = 원주 1주")
band(by+step, bh, ORANGE, (40,24,10), "괴리",
     "원주 환산가 대비 프리미엄 51%",
     "공모 당시(7/9) +2.9% → 열흘 만에 급확대",
     "7/13 폭락 당일에도 원주 -15.4% vs ADR -9%로 이미 시작")
band(by+step*2, bh, RED, (40,14,14), "구조",
     "전환 제약 + 거래시간 미중첩",
     "ADR→원주 역전환 제약 가능성, KRX·나스닥 시간 안 겹침",
     "TSMC ADR도 원주 대비 13~16% 프리미엄 구조적 유지")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.15  |  SKHY  SK Hynix ADR", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-15_SKHY_ADR프리미엄.png")
img.save(out); print("Saved:", out)
