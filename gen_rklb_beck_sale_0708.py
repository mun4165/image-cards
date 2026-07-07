from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-08"
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

draw.text((32,24), "RKLB 피터 벡 500만 주 매도 논란", font=bold(32), fill=ACCENT)
draw.text((32,80), "이리디움 인수 노린 고점 정리? 날짜로 다시 놓기", font=bold(24), fill=GRAY)
draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
    draw.line([(240,y+18),(240,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((268, y+20), headline, font=bold(25), fill=WHITE)
    draw.text((268, y+62), d1, font=font(19), fill=color)
    draw.text((268, y+92), d2, font=font(17), fill=GRAY)

by = 146; bh = 148; step = 164
band(by, bh, BLUE, (10,20,34), "3월 27일",
     "10b5-1 플랜 채택 — 최대 500만 주 사전 공시",
     "골드만삭스 창구, 냉각기간 90일 · 만료 7월 8일",
     "목적: 분산투자 · 상속 설계 · 자선 (3/30 13D/A 공개)")
band(by+step, bh, AMBER, (40,28,10), "6월 29일",
     "이리디움 인수 발표 — 당일 +15.9%",
     "84.54 → 98.01달러, 다음 날 101.65달러까지",
     "주당 54달러 현금+주식, 기업가치 80억 달러")
band(by+step*2, bh, CYAN, (8,28,34), "7월 6일",
     "Form 144 — 500만 주 실행, 당일 -7.4%",
     "매도가 93.09달러 < 발표 전 고점 100.29달러(6/22)",
     "체크포인트: S-4 협상 개시일이 3/27 이전인지")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.08  |  RKLB  Rocket Lab", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-08_RKLB_피터벡500만주매도.png")
img.save(out); print("Saved:", out)
