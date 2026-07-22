from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-14"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(239,68,68)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "SIVE  이사회 5인 자사주 매입", font=bold(22), fill=GRAY)
draw.text((32,58), "-9.5% 빠진 날, 원문 대조해보니", font=bold(30), fill=ACCENT)
draw.line([(32,110),(W-32,110)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(20), fill=color)
    draw.line([(280,y+16),(280,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((306, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((306, y+56), d1, font=font(16), fill=color)
    draw.text((306, y+84), d2, font=font(15), fill=GRAY)

by = 130; bh = 150; step = 166
band(by, bh, CYAN, (10,28,32), "공식발표",
     "이사 5명 + CEO 자사주 매입 완료",
     "2026.07.13 보도자료, AGM 승인 프로그램",
     "매입 주식 12개월 의무 보유")
band(by+step, bh, ORANGE, (40,24,10), "대조 결과",
     "CEO 매입분(약 95만 크로나)은 지난주 그 숫자",
     "7/9 개별 공시(24,000주·95만 6,741크로나)와 일치",
     "새 정보는 이사 2명(Bastani·Nideborn) 추가 참여뿐")
band(by+step*2, bh, RED, (40,14,14), "같은 날 주가",
     "SIVE 42.80크로나, 하루 -9.5%",
     "SK Hynix 서울장 -15.4% 발 반도체 섹터 투매",
     "발표 자체는 급락과 무관한 지난주 매입 재확인")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.14  |  SIVE  Sivers Semiconductors", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-14_SIVE_이사회매입_대표이미지.png")
img.save(out); print("Saved:", out)
