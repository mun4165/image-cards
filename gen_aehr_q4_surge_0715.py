from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-15"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(239,68,68)
ACCENT = GREEN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "AEHR  FY2026 4분기 실적", font=bold(22), fill=GRAY)
draw.text((32,58), "실적발표 후 시간외 +29%, 가이던스가 진짜 뇌관", font=bold(28), fill=ACCENT)
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
band(by, bh, GREEN, (10,32,22), "4분기 숫자",
     "매출 $18.8M(+34%), 비GAAP 순이익 $3.6M 흑자",
     "매출총이익률 35%→43%, 컨센서스 상회",
     "분기 수주 $60.7M 사상 최대, 유효 백로그 $100.6M")
band(by+step, bh, CYAN, (10,28,32), "FY2027 가이던스",
     "매출 $130~150M, 전년 $50M 대비 160~200%↑",
     "AI ~70% · 실리콘포토닉스 15~20% 구성",
     "Q2(9~11월) 출하 집중형 — 실행 리스크 존재")
band(by+step*2, bh, ORANGE, (40,26,10), "남은 리스크",
     "고객 집중은 SiC에서 AI로 대상만 이동",
     "10%+ 고객 3곳 중 2곳이 AI 리드고객",
     "특허소송(SemiE·NEXUSTEST) + 부품가 최대 40% 인상")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.15  |  AEHR  Q4 FY2026 Earnings", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-15_AEHR_4분기실적서프라이즈_대표이미지.png")
img.save(out); print("Saved:", out)
