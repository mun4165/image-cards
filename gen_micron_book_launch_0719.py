from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-19"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "전자책 「마이크론 완전정복」 출간", font=bold(30), fill=ACCENT)
draw.text((32,78), "예측이 아니라, 급락을 해석할 기준을 담았습니다", font=bold(22), fill=GRAY)
draw.line([(32,124),(W-32,124)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(22), fill=color)
    draw.line([(240,y+18),(240,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((268, y+20), headline, font=bold(23), fill=WHITE)
    draw.text((268, y+58), d1, font=font(18), fill=color)
    draw.text((268, y+88), d2, font=font(16), fill=GRAY)

by = 142; bh = 160; step = 178
band(by, bh, RED, (36,14,14), "시장",
     "마이크론 848.95달러(7/17), 고점 대비 -30%",
     "SOX 베어마켓 진입(7/17) · SK하이닉스 서킷(7/13)",
     "검색창에 치게 되는 건 '마이크론 왜 하락'이다")
band(by+step, bh, BLUE, (10,20,34), "구성",
     "3부 14장 + 부록 A·B, 111쪽",
     "디램·낸드·HBM 기초부터 실적발표 해석까지",
     "블로그 16편 + 아티클 14편, 수치 전부 재검증해 재구성")
band(by+step*2, bh, CYAN, (8,28,34), "프레임",
     "'지금 사라'가 아니라 급락을 해석할 기준",
     "런칭가 16,900원, 이후 정가 22,000원 전환",
     "전망·목표가를 파는 책이 아니다 — 판단 순서를 파는 책이다")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.19  |  MU  Micron  |  마이크론 완전정복", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-19_MU_마이크론완전정복출간.png")
img.save(out); print("Saved:", out)
