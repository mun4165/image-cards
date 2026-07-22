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

draw.text((32,24), "MU  창신메모리 IPO 급락 — 질문을 바꿔야 한다", font=bold(22), fill=GRAY)
draw.text((32,58), "디램이 부족하냐가 아니라, 계약가의 기울기다", font=bold(30), fill=ACCENT)
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
band(by, bh, RED, (40,14,16), "새 정보는 따로",
     "IPO는 구문 — 사이즈와 규제가 새 뉴스였다",
     "조달액 $8.5B, 당초 목표의 2배로 증액 확정 (7/27 상해 상장)",
     "같은 날 미국 HBM 추가 수출규제 검토 보도가 겹침")
band(by+step, bh, ORANGE, (40,26,10), "마진의 정체",
     "마이크론 마진 확장은 물량이 아니라 가격",
     "매출총이익률 38% → 72.6%, 전부 디램 가격에서 왔다",
     "부족분 채워지는 속도가 빨라지면 가격은 기울기부터 꺾인다")
band(by+step*2, bh, CYAN, (10,28,32), "CXMT의 자리",
     "선도 3사가 HBM으로 빼면서 생긴 커머디티 빈자리",
     "기술 격차와 무관 — 지금 노드로도 채울 수 있는 곳",
     "HBM은 비트당 웨이퍼 3배 잠식, 부족은 견고 · 시험대는 2027년")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.16  |  MU  Micron Technology  |  첫 체크: 7/29 SK하이닉스 어닝콜", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-16_마이크론_계약가의기울기_카드.png")
img.save(out); print("Saved:", out)
