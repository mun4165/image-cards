from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-14"
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

draw.text((32,24), "RKLB  뉴트론 2단 엔진 AVac", font=bold(22), fill=GRAY)
draw.text((32,58), "연소시험 성공, 그런데 주가는 5일째 하락", font=bold(28), fill=ACCENT)
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
band(by, bh, GREEN, (10,32,22), "시험 성공",
     "2단 엔진 AVac 풀듀레이션 연소시험 완료",
     "2026.07.13 밤, 회사 표현 \"a thing of beauty\"",
     "1단 아르키메데스 대비 추력 1.2배, 노즐 2.5m 김")
band(by+step, bh, CYAN, (10,28,32), "남은 일정",
     "뉴트론 첫 발사 목표는 2026년 4분기",
     "1월 탱크 결함으로 초반 발사창 상실, 교체 탱크 생산 중",
     "5월 5회 발사 계약 확보, 연내 데뷔 목표 재확인")
band(by+step*2, bh, RED, (40,14,14), "같은 기간 주가",
     "RKLB 5거래일 누적 -19.3%, 시총 약 120억달러 증발",
     "같은 기간 S&P500은 상승, 종목 고유 압력",
     "7/13 유가급등+우주주 동반하락, 엔진시험과는 별개 트랙")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.14  |  RKLB  Rocket Lab  Neutron", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-14_RKLB_뉴트론엔진시험_대표이미지.png")
img.save(out); print("Saved:", out)
