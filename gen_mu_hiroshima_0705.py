from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-05"
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

draw.text((32,24), "마이크론 히로시마 HBM 공장 착공", font=bold(40), fill=ACCENT)
draw.text((32,84), "일본 정부가 7,745억엔을 대는 이유", font=bold(24), fill=GRAY)
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
band(by, bh, BLUE, (14,24,44), "착공",
     "7월 4일 착공식 · 1조5,000억엔 (96억 달러)",
     "기존 히로시마 사업장 내 HBM 신공장 — EUV 이미 가동 중",
     "2025-12 발표 → 2026-05 건설 개시 → 2028년 첫 출하 목표")
band(by+step, bh, GREEN, (10,32,22), "보조금",
     "METI 최대 5,000억엔 — 투자액의 1/3",
     "2023년 EUV 도입 때 1,920억엔 → 누적 최대 7,745억엔",
     "외국 기업 단일 사업장 기준 이례적 규모의 국가 자본")
band(by+step*2, bh, AMBER, (40,28,10), "구도",
     "HBM 3파전, 마이크론 뒤에만 국가 자본",
     "SK하이닉스·삼성전자와 캐파 경쟁 — 자본 부담이 다르다",
     "대만 퉁뤄 · 히로시마 · 인도 3곳 동시 증설 중 히로시마만 보조금")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.05  |  $MU  Micron Technology", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-05_마이크론히로시마착공.png")
img.save(out); print("Saved:", out)
