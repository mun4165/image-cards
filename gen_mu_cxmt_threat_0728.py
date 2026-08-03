from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-28"
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

# ── MU, CXMT 상장 쇼크에 진짜 위협받는 지점 ──────────
img, draw = base_canvas(RED)
draw.text((32,22), "마이크론, CXMT 쇼크 진짜 위협받는 지점", font=bold(27), fill=RED)
draw.text((32,74), "HBM 아니라 상용 D램, 두 시장을 나눠 봐야 한다", font=bold(19), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)
by, bh, step = 134, 128, 142
band(draw, by, bh, RED, (40,14,14), "7/27 주가",
     "CXMT 상장 466% 급등 소식에 마이크론 4.3~5.5% 하락, $900.20 마감", "전일 7/24도 -6.99%, 이틀 연속 낙폭 누적")
band(draw, by+step, bh, AMBER, (40,28,10), "CXMT D램 점유율",
     "2025년 3% → 2026년 1분기 8%, 1년새 3배 육박", "세계 4위, 레노보 등 완제품에 이미 탑재")
band(draw, by+step*2, bh, CYAN, (8,28,34), "HBM은 다른 얘기",
     "CXMT HBM 수익화 전 단계, EUV 장비 제약으로 접근 불가", "한국과 기술격차 약 3년, 마이크론 HBM 점유율 21%")
band(draw, by+step*3, bh, GREEN, (10,30,22), "관전 포인트",
     "조달자금 86억달러가 상용D램 넘어 HBM 증설로 번지는 시점", "그 전까진 가격압박·HBM우위 분리해서 볼 것")
footer(draw, "2026.07.28  |  MU(마이크론) · CXMT(창신메모리)  |  D램 · HBM")
out = os.path.join(OUT_DIR, "2026-07-28_MU_CXMT쇼크_진짜위협지점.png")
img.save(out); print("Saved:", out)
