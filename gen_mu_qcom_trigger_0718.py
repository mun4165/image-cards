from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-18"
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

draw.text((32,24), "MU  퀄컴 등 7개사와 자동차 메모리 계약", font=bold(22), fill=GRAY)
draw.text((32,58), "그런데 주가는 5.65% 더 빠졌다", font=bold(28), fill=ACCENT)
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
     "7/16 퀄컴·현대모비스 등 7곳과 SCA 체결",
     "인포테인먼트·ADAS향 자동차 메모리 — HBM 아님",
     "계약기간·물량·가격 조건은 비공개")
band(by+step, bh, RED, (36,14,14), "주가 반응",
     "7/16 종가 853.20달러, -5.65%",
     "전날(7/15) 이미 -8.02%, 이틀 연속 하락",
     "같은 날 S&P500은 오히려 +0.4%")
band(by+step*2, bh, CYAN, (10,28,32), "해석",
     "실제 트리거=CXMT $85.5억 IPO + 코어위브 가격헤지설",
     "코어위브=대형 AI클라우드 구매자, 가격하락에 베팅",
     "지수는 오르고 섹터만 빠짐 = 종목·섹터 특이적 신호")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.18  |  MU  Micron x Qualcomm SCA", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-18_MU_퀄컴계약진짜하락원인.png")
img.save(out); print("Saved:", out)
