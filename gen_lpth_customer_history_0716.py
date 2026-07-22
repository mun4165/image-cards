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
draw.text((32,58), "$11M 후속 발주, '글로벌 기술 고객'의 정체는", font=bold(28), fill=ACCENT)
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
     "고객명은 비공개(NDA 관용구) — 정부기관을 뜻하는 표현 아님")
band(by+step, bh, CYAN, (10,28,32), "같은 고객 거래 이력",
     "2025.09.03 $18.2M → 09.17 $22.1M → 2026.07.15 $11M",
     "\"leading global technology customer\" 표현 3건 동일",
     "10개월간 확인된 합계 $51.3M")
band(by+step*2, bh, ORANGE, (40,26,10), "예측 가능성",
     "이번엔 선반영 가이드·매출인식 시점 공시 없음",
     "9월 두 건은 \"CY26~27 합계 $40.3M\" 명시했었음",
     "이번은 \"over the course of this program\"뿐 — 특정 불가")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.16  |  LPTH  LightPath Technologies", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-16_라이트패스_고객이력_대표이미지.png")
img.save(out); print("Saved:", out)
