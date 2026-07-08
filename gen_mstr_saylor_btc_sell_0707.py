from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-07"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = ORANGE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "세일러의 Strategy, 비트코인 3,588개 매도", font=bold(32), fill=ACCENT)
draw.text((32,80), "이유는 하락 베팅이 아니라 배당금 방어였다", font=bold(24), fill=GRAY)
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
band(by, bh, ORANGE, (40,24,10), "매도 규모",
     "6월 말~7월 5일 3,588 BTC, 약 2.16억 달러 매도",
     "평균 매도가 6만 달러, 전체 보유의 0.43%",
     "5월 말에도 32개 매도 — 2022년 이후 첫 매도")
band(by+step, bh, AMBER, (40,28,10), "매도 이유",
     "우선주 STRC(연 12% 배당) 지급 방어 목적",
     "6월 29일 Digital Credit Capital Framework 도입",
     "CFO 앤드류 강: \"비트코인은 자본이다\"")
band(by+step*2, bh, CYAN, (8,28,34), "현재 상태",
     "총 보유 843,775 BTC, 평균 매입가 75,476달러",
     "현재가 63,014달러, 2분기 미실현손실 83억 달러",
     "달러 유보금 25.5억 달러, 약 17개월분 커버")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.07  |  MSTR  Strategy Inc.", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-07_MSTR_세일러비트코인매도.png")
img.save(out); print("Saved:", out)
