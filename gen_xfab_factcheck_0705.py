from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-05"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = TEAL

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,22), "X-FAB 반토막", font=bold(36), fill=ACCENT)
draw.text((32,76), "보조금 뉴스 vs 베른슈타인 목표가, 팩트체크", font=bold(21), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(196,y+14),(196,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((220, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((220, y+46), detail, font=font(15), fill=color)

by = 136; bh = 92; step = 100
band(by, bh, RED, (40,14,14), "주가",
     "15.88유로 → 7.22유로, 두 달새 반토막", "5/27 사상최고 → 7/2 종가")
band(by+step, bh, AMBER, (40,28,10), "진짜원인",
     "1분기 매출 -4%, 순이익 92% 감소", "최대고객 Melexis 재고조정(destocking)")
band(by+step*2, bh, CYAN, (8,28,34), "루머검증",
     "베른슈타인 목표가 12.8유로 상향설 = 거짓", "실제는 Hold, 목표가 5.0~5.5유로(현재가 밑)")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.05  |  X-FAB Silicon Foundries SE", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-05_XFAB_반토막.png")
img.save(out); print("Saved:", out)
