from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-24"
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

# ── INTC 2분기 실적: non-GAAP 흑자전환 vs GAAP 110억달러 적자 ────────────
img, draw = base_canvas(RED)
draw.text((32,22), "INTC 흑자전환? GAAP은 110억달러 적자", font=bold(30), fill=RED)
draw.text((32,76), "non-GAAP EPS 0.42달러 vs GAAP 순손실 110억달러, 같은 분기 다른 그림", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, RED, (40,14,14), "GAAP 기준",
     "순손실 110억달러, 주당 -2.16달러", "CHIPS Act 에스크로 주식 시가평가손 125억달러 반영")
band(draw, by+step, bh, GREEN, (10,30,22), "non-GAAP 기준",
     "순이익 22억달러, EPS 0.42달러(예상 0.22)", "매출 161억달러 +25%, 영업 실질 개선은 맞음")
band(draw, by+step*2, bh, AMBER, (40,28,10), "파운드리",
     "매출 58억달러 +31%, 영업손실은 21억달러 지속", "18A 수율 목표比 25% 초과, 외부매출 비중은 5%뿐")
band(draw, by+step*3, bh, CYAN, (8,28,34), "다음 확인 지점",
     "14A 외부 고객 확정 0건, 잠재 2곳 테스트칩 단계", "확약 시점은 2026 하반기~2027년 초로 회사도 인정")
footer(draw, "2026.07.24  |  INTC  Intel Corporation")
out = os.path.join(OUT_DIR, "2026-07-24_INTC_GAAP적자.png")
img.save(out); print("Saved:", out)
