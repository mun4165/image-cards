from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-04"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = RED

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,22), "SIVE, 증자 다음날 -19%", font=bold(38), fill=ACCENT)
draw.text((32,78), "발행가 57크로나 밑으로 무너진 이유", font=bold(21), fill=GRAY)
draw.line([(32,120),(W-32,120)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(180,y+14),(180,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((204, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((204, y+46), detail, font=font(15), fill=color)

by = 136; bh = 78; step = 86
band(by, bh, RED, (40,14,14), "7/2 주가",
     "-19.34%, 49.00크로나 마감", "발행가 57크로나 대비 -14%, 개장 초반 -15%대 낙폭")
band(by+step, bh, ORANGE, (40,24,10), "증자 조건",
     "700MSEK, 발행가 57크로나(-9.7% 할인)", "여러 배 초과청약, 조달액도 계획보다 100MSEK 이상 증가")
band(by+step*2, bh, CYAN, (8,28,34), "진짜 원인",
     "1분기 매출 6,190만크로나, 전년비 -22%", "미국 국방예산 지연(정부 셧다운 여파) + 환율 역풍")
band(by+step*3, bh, TEAL, (8,28,26), "괴리",
     "수주 파이프라인 5개월간 +77%", "약 7억9,900만달러, 매출 전환 속도가 다음 관전포인트")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.04  |  SIVE  Sivers Semiconductors", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-04_SIVE_증자다음날급락.png")
img.save(out); print("Saved:", out)
