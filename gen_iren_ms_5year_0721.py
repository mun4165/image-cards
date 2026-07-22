from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-21"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

def base_canvas(accent):
    img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    draw.rectangle([0,0,W,4], fill=accent); draw.rectangle([0,0,4,H], fill=accent)
    return img, draw

def band(draw, y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(18), fill=color)
    draw.line([(228,y+14),(228,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((252, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((252, y+46), detail, font=font(15), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# ── IREN-Microsoft 97억달러 계약, 5년이 아직 시작 안 됐다 ──────────────────────────
img, draw = base_canvas(CYAN)
draw.text((32,22), "IREN-MS 97억달러 계약, 아직 5년이 시작 안 됐다", font=bold(28), fill=CYAN)
draw.text((32,76), "5년 시계는 서명일이 아니라 인도·인수 시점부터, 원문 공시 기준 확인", font=bold(18), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, CYAN, (8,28,34), "계약 개요",
     "2025/11/3 공시, 2031년까지 97억 달러, 평균 5년 기간", "IE US Hardware 3(IREN 자회사) ↔ Microsoft")
band(draw, by+step, bh, AMBER, (40,28,10), "5년의 시작점",
     "서명일 아닌 트랜치별 인도·인수 시점부터 카운트", "2025년말 10-Q 기준 인도·인수 완료 0건")
band(draw, by+step*2, bh, GREEN, (10,30,22), "200MW의 정체",
     "Horizon 1~4 전체 합산, 전량 MS 계약 대상", "Childress 750MW 중 나머지는 NVIDIA 등 별개")
band(draw, by+step*3, bh, BLUE, (10,20,40), "Horizon 1 현황",
     "MS 핸드오버 '2026년 3분기 중' 예정 표현 그대로", "7/19 가동설은 근거 없는 개인 루머로 확인")
footer(draw, "2026.07.21  |  IREN")
out = os.path.join(OUT_DIR, "2026-07-21_IREN_MS계약9.7조_5년미시작.png")
img.save(out); print("Saved:", out)
