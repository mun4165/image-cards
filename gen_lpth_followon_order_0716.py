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

draw.text((32,24), "LPTH  라이트패스 후속 발주", font=bold(22), fill=GRAY)
draw.text((32,58), "11억 발주 떴는데, 종가는 왜 빠졌나", font=bold(28), fill=ACCENT)
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
band(by, bh, GREEN, (10,30,24), "발주 팩트",
     "7/15 08:31 ET, $11M C-UAS 적외선 카메라 후속 발주",
     "게르마늄 렌즈 → 자사 독점 BlackDiamond 소재 전환 포함",
     "신규 고객 아닌 기존 거래 반복(follow-on)")
band(by+step, bh, CYAN, (10,28,32), "장중 반응",
     "발표 직후 +5.56%, 12.16달러까지 상승",
     "뉴스 자체에 대한 시장의 즉각적 반응",
     "BlackDiamond 수직통합 스토리가 실제로 진행 중이라는 신호")
band(by+step*2, bh, RED, (40,14,16), "종가 반전",
     "정규장 종가는 -0.87%, 11.42달러 마감",
     "AAOI -13%, Coherent·Lumentum도 두 자릿수 하락",
     "포토닉스 섹터 전체 밸류에이션 되돌림 — 라이트패스 개별 악재 아님")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.16  |  LPTH  LightPath Technologies", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-16_라이트패스_11M후속발주_대표이미지.png")
img.save(out); print("Saved:", out)
