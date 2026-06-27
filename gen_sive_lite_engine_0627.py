from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-27"
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

draw.text((32,22), "SIVE는 '제2의 Lumentum'일까", font=bold(36), fill=ACCENT)
draw.text((32,74), "초기 방향은 닮았는데 엔진이 안 닮은 이유", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

# 핵심 메시지 박스
ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "닮은 건 출발선의 풍경", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "회사를 끌고 간 '엔진'은 아직 점화 안 됐다", font=bold(24), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "닮은 층 (인정)",
     "픽앤셔블 광부품 포지션", "둘 다 과소평가된 광소자 · 카테고리·자세는 운이 맞는다")
band(by+step, bh, BLUE, (12,20,38), "출발선이 다르다",
     "Lumentum = JDSU 스핀오프", "수억$ 매출·현금흐름 인계받고 시작 · SIVE는 사실상 0")
band(by+step*2, bh, ORANGE, (38,24,8), "엔진이 다르다",
     "앵커 윈 + 자가조달 M&A", "LITE는 애플 VCSEL 확정 앵커 · SIVE 앵커는 아직 OSINT 가설")

gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "엔진 점화 신호 (추적 대상)", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "① 확정 하이퍼스케일러 앵커 윈  ② InP 수율·볼륨 램프  ③ 자가조달 현금흐름",
          font=bold(20), fill=CYAN)
draw.text((52,gy+74), "이 중 하나가 가설→사실로 넘어가는 순간이 Lumentum 비유가 작동하는 지점",
          font=font(15), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.27  |  결과론을 떼고 본 SIVE vs Lumentum — '방향'이 아니라 '카테고리'가 닮았을 뿐", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-27_SIVE_루멘텀엔진비교.png")
img.save(out); print("Saved:", out)
