from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-28"
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

draw.text((32,22), "안보 매출의 보이지 않는 관세 · FOCI", font=bold(36), fill=ACCENT)
draw.text((32,74), "RKLB·SATL이 본사를 미국으로 옮긴 진짜 이유", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "입장권은 기술·가격이 아니다", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "좋은 위성이 아니라 '통과 가능한 소유구조'가 입장권", font=bold(24), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "들어오는 문 · RKLB",
     "뉴질랜드 창업 → 2013 미국 법인·델라웨어", "짐 가벼움: 파이브 아이즈 동맹 → 도장만 바꾸면 됨")
band(by+step, bh, ORANGE, (38,24,8), "들어오는 문 · SATL",
     "아르헨 창업 + 텐센트(중국) 지분 이력", "짐 무거움: 적성국 자본 털어내야 통과 (2025 이전)")
band(by+step*2, bh, BLUE, (12,20,38), "나가는 문 · CHIPS",
     "보조금 받으면 10년 우려국 확장 금지", "TSMC·삼성·SK하이닉스가 같은 줄에 묶임")

gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "원리는 하나, 작동은 양방향", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "돈·시장 접근을 미끼로 안보 통제를 지배구조에 심는다",
          font=bold(22), fill=CYAN)
draw.text((52,gy+76), "국적 통과는 입장권일 뿐 — 실제 수주는 발사 실적·케이던스로 따로 증명",
          font=font(15), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.28  |  같은 게이트, 다른 통관 비용 — 한 번 이해하면 외국 출신 안보기업 뉴스가 같은 격자로 읽힌다", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-28_RKLB_SATL_FOCI_안보관세.png")
img.save(out); print("Saved:", out)
