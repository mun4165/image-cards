from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-24"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = ORANGE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "세레브라스 첫 실적, 좋은 숫자가 안 통한 이유", font=bold(37), fill=ACCENT)
draw.text((32,74), "2026.06.23 상장 후 첫 분기 실적 · 마진 가이던스가 핵심", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

# 테제 박스
ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(36,22,8))
draw.rectangle([32,ty,38,ty+96], fill=ORANGE)
draw.text((60,ty+16), "수요는 진짜다", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "오픈AI 750MW·$20B+, AWS 고속추론 — 거대 계약은 확보", font=bold(26), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(23), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(22), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

# 실적 vs 가이던스
by = 248; bh = 86; step = 96
band(by, bh, GREEN, (10,32,24), "지나간 실적은 합격점",
     "매출 $193.4M (+94% YoY)", "핵심 총이익률 47% · 순손실 축소")
band(by+step, bh, RED, (38,14,14), "다음 분기 마진 전망",
     "총이익률 47% → 36~41% 하향", "성장통 비용 선반영 = 시장은 실망")

# 근거 박스
gy = 452
draw.rounded_rectangle([32,gy,W-32,gy+88], radius=10, fill=(40,22,10))
draw.text((52,gy+14), "그래서 봐야 할 것", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "시간외 -11%   ·   RPO $24.6B(대부분 오픈AI)   ·   고객 86% UAE 쏠림", font=bold(22), fill=AMBER)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.24  |  CBRS  Cerebras Systems", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-24_CBRS_첫실적_마진가이던스.png")
img.save(out); print("Saved:", out)
