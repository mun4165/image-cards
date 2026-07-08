from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-06"
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

draw.text((32,24), "SIVE, 사흘 새 두 번째 희석", font=bold(36), fill=ACCENT)
draw.text((32,80), "전환가 4.77크로나의 정체", font=bold(24), fill=GRAY)
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
band(by, bh, AMBER, (40,28,10), "7월 1일",
     "유상증자 — 1,228만주 발행",
     "발행가 57크로나 (6/30 종가 대비 -9.7% 할인) · 약 7억 크로나 조달",
     "다음날 주가 -19.34%, 발행가 밑으로 붕괴")
band(by+step, bh, ORANGE, (40,20,10), "7월 3일",
     "전환사채 전환 — 2,285만주 발행",
     "Bootstrap Europe, 2월 리파이낸싱 조건 그대로 전환 행사",
     "전환가 4.77크로나 — 시가 대비 90%+ 할인")
band(by+step*2, bh, CYAN, (8,28,34), "사흘 합산",
     "발행주식 약 11% 증가, 시장 반응은 정반대",
     "증자엔 -19% 벌 · 전환엔 +11.73% 반등",
     "다음 체크포인트: 7/16 락업 해제 · 2분기 매출 전환 여부")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.06  |  SIVE  Sivers Semiconductors", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-06_SIVE_사흘새두번째희석.png")
img.save(out); print("Saved:", out)
