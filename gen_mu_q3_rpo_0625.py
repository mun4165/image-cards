from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-25"
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

# 헤더
draw.text((32,22), "마이크론 실적 다 좋았다 — 진짜 폭탄은 계약잔고 100조", font=bold(33), fill=ACCENT)
draw.text((32,72), "FY3Q26 — 매출 1년 만에 4.5배, 다음 분기 50조 가이드", font=bold(20), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)

# 테제 박스
ty = 130
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "분기 흥정이 계약으로 바뀌었다", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "RPO 130조 = 사이클이냐 지속 수요냐의 객관적 답", font=bold(26), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(22), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(21), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 246; bh = 84; step = 92
band(by, bh, GREEN, (10,32,24), "실적  컨센 상회",
     "매출 $41.5B · 비GAAP EPS $25.11", "예상 $20 상회 · 총마진 84.6%")
band(by+step, bh, AMBER, (40,22,10), "가이드  더 셌다",
     "다음 분기 매출 $50B · EPS $31", "총마진 약 86% — 메모리 역사상 최고급")
band(by+step*2, bh, BLUE, (10,22,40), "HBM  구조 확인",
     "HBM4 12단 램프 2배 속도 · 누적 10억달러", "디램 한 장 자리에 세 장씩")

# 결론 박스
gy = 522
draw.rounded_rectangle([32,gy,W-32,gy+98], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "그래도 반박을 먼저", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "좋은 실적 ≠ 안전  →  86% 마진은 사이클 정점의 모습이기도",
          font=bold(22), fill=CYAN)
draw.text((52,gy+76), "체크포인트: 다음 분기 capex 가이드 = 다음 다운사이클 씨앗",
          font=font(15), fill=GRAY)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.25  |  MU  Micron · FY3Q26", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-25_MU_실적발표_계약잔고100조.png")
img.save(out); print("Saved:", out)
