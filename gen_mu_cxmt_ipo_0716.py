from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-16"
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

draw.text((32,24), "MU  마이크론 하루 -8.02%", font=bold(22), fill=GRAY)
draw.text((32,58), "창신메모리 IPO 때문만이 아니다 — 트리거는 두 개였다", font=bold(28), fill=ACCENT)
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
band(by, bh, RED, (40,14,16), "급락 트리거",
     "7/15 종가 904.28달러, CXMT IPO + HBM 규제 겹침",
     "창신메모리 $8.5B 상해 IPO(7/27) — 전액 DRAM 캐파 확충",
     "같은 날 미국 HBM 추가 수출규제 검토 보도, 하이닉스 ADR -12%")
band(by+step, bh, CYAN, (10,28,32), "창신메모리 캐파",
     "웨이퍼 월 26.5만장 → 올해말 35만장 계획",
     "마이크론 38.5만장에 웨이퍼 기준 근접",
     "DRAM 점유율 2025년 9% → 2027년 12% 전망 (SemiAnalysis)")
band(by+step*2, bh, ORANGE, (40,26,10), "기술 격차",
     "EUV 반입 불가, 노드 G4(1z급) 정체",
     "DDR5 비트당 원가 +30% 열위 · HBM3 8단 수율 25%",
     "이익풀(HBM·서버 DDR5)은 당분간 선도 3사 영역")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.16  |  MU  Micron Technology", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-16_마이크론_창신메모리IPO급락_대표이미지.png")
img.save(out); print("Saved:", out)
