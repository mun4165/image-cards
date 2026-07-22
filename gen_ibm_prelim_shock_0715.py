from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-15"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(239,68,68)
ACCENT = RED

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "IBM  2분기 잠정 실적 공개", font=bold(22), fill=GRAY)
draw.text((32,58), "하루 만에 -25.21%, 정식 발표는 아직 7/22", font=bold(28), fill=ACCENT)
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
band(by, bh, RED, (40,14,14), "주가 반응",
     "7/14 하루 -25.21%, $217.07 마감",
     "시총 약 $204B로 -24.8%, 50년래 최대 낙폭이라는 보도",
     "정식 실적 발표는 7/22 예정, 이번은 잠정치 선공개")
band(by+step, bh, ORANGE, (40,26,10), "숫자",
     "매출 $172억(+1%), 컨센서스 $178.6억 미스",
     "인프라 -7% vs 소프트웨어 +5%, 인프라만 역성장",
     "EPS: GAAP $2.27 / Non-GAAP $2.93(컨센서스 $3.01 미스)")
band(by+step*2, bh, CYAN, (10,28,32), "크리슈나가 짚은 원인",
     "매크로 요인과 자체 실행 문제, 두 갈래",
     "고객사 메모리·서버 선매입으로 SW·컨설팅 예산 축소",
     "\"we faltered\" — 대형 계약 다수 예정 시점에 못 닫힘")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.15  |  IBM  Preliminary Q2 2026", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-15_IBM_잠정실적쇼크_대표이미지.png")
img.save(out); print("Saved:", out)
