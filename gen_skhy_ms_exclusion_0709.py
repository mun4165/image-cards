from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-09"
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

draw.text((32,24), "SK하이닉스 ADR 주관사에 모건스탠리가 없다", font=bold(30), fill=ACCENT)
draw.text((32,80), "2년 전 그 리포트 때문이었다", font=bold(24), fill=GRAY)
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
band(by, bh, BLUE, (10,20,34), "명단",
     "주관사 4곳 골드만·JP모간·BofA·씨티, 모건스탠리 없음",
     "각 사당 평균 10조원가량 수요 확보 부담",
     "글로벌 최상위권 IB가 초대형 딜에서 빠진 이례적 사례")
band(by+step, bh, RED, (40,15,15), "배경",
     "2024.09.15 \"Winter looms\" 목표가 54% 하향",
     "발표 이틀 전 101만주 매도 → 선행매매 의혹, 거래소·금감원 조사",
     "완전한 오류 인정까지 7개월(2025.03.18 중립 상향)")
band(by+step*2, bh, CYAN, (8,28,34), "그런데",
     "7/7 재차 반도체 비중축소, 하이퍼스케일러 추천",
     "AI 투자 확대 전제로 하이퍼스케일러 담으라면서 반도체는 줄이라는 논리",
     "과거 전적 + 이번 모순이 겹치는 지점")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.09  |  SKHY  SK Hynix", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-09_SK하이닉스_모건스탠리배제.png")
img.save(out); print("Saved:", out)
