from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-16"
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

draw.text((32,24), "NBIS  리플렉션AI 10억 달러 컴퓨팅 계약", font=bold(22), fill=GRAY)
draw.text((32,58), "그런데 당일 주가는 7.8% 빠졌다", font=bold(28), fill=ACCENT)
draw.line([(32,110),(W-32,110)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(20), fill=color)
    draw.line([(280,y+16),(280,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((306, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((306, y+56), d1, font=font(16), fill=color)
    draw.text((306, y+84), d2, font=font(15), fill=GRAY)

by = 130; bh = 168; step = 186
band(by, bh, GREEN, (10,32,22), "확인된 계약",
     "7/14 리플렉션AI에 2029년까지 컴퓨팅 공급",
     "규모 10억 달러+ · 엔비디아 GB300 기반(블룸버그)",
     "리플렉션AI = 구글딥마인드 출신 창업, 밸류 250억 달러")
band(by+step, bh, RED, (36,14,14), "주가 반응",
     "발표 당일 210.51 → 194.09달러, -7.8%",
     "종가 기준 200달러선 최초 붕괴",
     "7/15 199.51달러로 반등했지만 200달러 미회복")
band(by+step*2, bh, CYAN, (10,28,32), "해석",
     "연환산 2.5~3.3억 달러 vs 연간 capex 200~250억",
     "계약 잔고(메타·MS·리플렉션) 약 500억 달러 중 일부",
     "capex 상향 근거=2027 캐파 선확정 수요, 현금소진과는 결이 다름")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.16  |  NBIS  Reflection AI Compute Deal", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-16_NBIS_리플렉션AI딜.png")
img.save(out); print("Saved:", out)
