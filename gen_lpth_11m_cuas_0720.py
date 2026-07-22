from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-20"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = GREEN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "LPTH, C-UAS 적외선 카메라 $1,100만 후속 발주", font=bold(28), fill=ACCENT)
draw.text((32,76), "게르마늄에서 BlackDiamond로, 소재 전환이 계약에 명시됐다", font=bold(20), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(20), fill=color)
    draw.line([(224,y+16),(224,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((250, y+16), headline, font=bold(21), fill=WHITE)
    draw.text((250, y+52), d1, font=font(17), fill=color)
    draw.text((250, y+80), d2, font=font(15), fill=GRAY)

by = 140; bh = 118; step = 133
band(by, bh, GREEN, (10,30,20), "발주",
     "$1,100만 규모, C-UAS(대드론) 응용 적외선 카메라",
     "고객사 = '선도적 글로벌 기술 고객', 실명 비공개",
     "기존 고객사의 반복(후속) 발주")
band(by+step, bh, CYAN, (8,28,34), "소재전환",
     "게르마늄 → BlackDiamond(자체 소재)",
     "미국 내 생산, 비(非)게르마늄 대안",
     "\"게르마늄 수출 제한 강화 속 공급망 확보에 도움\" — 회사 설명")
band(by+step*2, bh, AMBER, (34,26,8), "CEO 코멘트 (샘 루빈)",
     "\"가장 중요한 고객사 중 하나와의 관계 심화\"",
     "\"공공 안전 응용 분야에서 적외선 카메라의 역할 확대\"",
     "신뢰성·성능이 핵심적인 분야로 명시")
band(by+step*3, bh, RED, (34,14,14), "미확인",
     "고객사명은 공개되지 않음",
     "추정하지 않고 '미확인' 상태로 다룸",
     "확인 안 된 걸 확인된 것처럼 다루면 판단이 흔들린다")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.15 발표 | LPTH  LightPath Technologies", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-20_LPTH_11M후속발주.png")
img.save(out); print("Saved:", out)
