from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-16"
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

draw.text((32,24), "ASML  2026년 2분기 실적 — 매출 93.3억 유로, 총마진 54.0%", font=bold(22), fill=GRAY)
draw.text((32,58), "가이던스 상향보다 캐파 30% 증설이 진짜 신호다", font=bold(28), fill=ACCENT)
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
band(by, bh, GREEN, (10,32,24), "2분기 실적",
     "순이익 29.2억 유로 · EPS 7.59유로 · 장비 86대 출하",
     "서비스(설치기반 관리) 매출 27.6억 유로 사상 최대 (+11% QoQ)",
     "컨센서스 상회 — 달러 환산 매출 106.5억 vs 예상 102.8억")
band(by+step, bh, CYAN, (10,28,32), "가이던스 2차 상향",
     "2026년 연간 430억~450억 유로, 총마진 54~56%",
     "연초 340억~390억 → 4월 360억~400억 → 7월 430억~450억",
     "3분기 110억~120억 유로 제시 — 2분기 대비 +18~29% 점프")
band(by+step*2, bh, ORANGE, (40,26,10), "캐파 + High-NA",
     "EUV 65→85대 · DUV 이머전 130→170대 (2027년 +30%)",
     "2028년 추가 30% 증설 검토 — 수주 비공개를 캐파가 대신 말한다",
     "Intel 18A 일부 레이어 High-NA 퀄 완료, 첫 양산 로직 적용")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.16  |  ASML  ASML Holding", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-16_ASML_2분기실적_대표이미지.png")
img.save(out); print("Saved:", out)
