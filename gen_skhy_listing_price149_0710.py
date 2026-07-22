from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-10"
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

draw.text((32,24), "SKHY 나스닥 상장 오늘, 공모가 149달러 확정", font=bold(29), fill=ACCENT)
draw.text((32,80), "잠정가보다 9달러 낮아진 이유", font=bold(24), fill=GRAY)
draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
    draw.line([(250,y+18),(250,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((278, y+22), headline, font=bold(25), fill=WHITE)
    draw.text((278, y+64), d1, font=font(19), fill=color)
    draw.text((278, y+96), d2, font=font(17), fill=GRAY)

by = 150; bh = 152; step = 170
band(by, bh, BLUE, (10,20,34), "오늘",
     "SKHYV 임시 티커로 나스닥 데뷔, 13일 SKHY 정식 전환",
     "시총 약 1조달러, ADR 1억7,790만주 발행",
     "외국기업 미국 상장 사상 최대 265억달러 조달")
band(by+step, bh, CYAN, (8,28,34), "공모가",
     "149달러 확정, 국내 종가 대비 프리미엄 약 2.9%",
     "7/9 코스피 종가 218만6,000원 환산가 1,448달러 기준",
     "청약 수요는 물량의 7배 초과")
band(by+step*2, bh, RED, (40,15,15), "왜 낮아졌나",
     "잠정가 158.14달러 → 확정가 149달러",
     "기준이 된 국내 주가가 일주일새 242.5만→218.6만원, 9.9% 하락",
     "공모 구조가 아니라 국내가 자체 하락분이 반영된 것")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.10  |  SKHY  SK Hynix", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-10_SKHY_공모가149달러확정.png")
img.save(out); print("Saved:", out)
