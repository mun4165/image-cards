from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-07"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = BLUE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "TSMC 코워스 병목, Amkor·ASE로 번진다", font=bold(32), fill=ACCENT)
draw.text((32,80), "진짜 체크포인트는 따로 있다", font=bold(24), fill=GRAY)
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
band(by, bh, BLUE, (10,20,34), "TSMC",
     "코워스 웨이퍼 수요 2024년 37만장 → 2026년 100만장",
     "TrendForce: 수급 갭 20% → 연말 10%로 완화 전망(6/15)",
     "엔비디아 비중 약 60%, 26~27년 증설분 절반 예약")
band(by+step, bh, AMBER, (40,28,10), "Amkor·ASE",
     "TSMC, 코워스 서브스텝 일부를 OSAT로 위탁",
     "Amkor 2026 캐펙스 최대 3조원, 65~70% 애리조나행",
     "ASE는 올해 신규 팹 6곳 착공")
band(by+step*2, bh, CYAN, (8,28,34), "다음 레이어",
     "유리기판(Corning)·하이브리드본딩(Kulicke & Soffa) 대기",
     "볼륨 램프는 2027~2028년",
     "리스크: 엔비디아 집중 60%는 밸류체인 전체의 리스크")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.07  |  AMKR  Amkor Technology", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-07_TSMC코워스아웃소싱.png")
img.save(out); print("Saved:", out)
