from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-25"
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
    draw.text((60, y+14), label, font=bold(17), fill=color)
    draw.line([(240,y+14),(240,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((264, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((264, y+46), detail, font=font(15), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# ── 빅테크 4사 실적발표 일정 + 관전포인트 ────────────
img, draw = base_canvas(BLUE)
draw.text((32,22), "빅테크 실적 이번주, MSFT·META 29일 AAPL·AMZN 30일", font=bold(28), fill=BLUE)
draw.text((32,76), "29일은 FOMC 금리결정과도 겹친다, 공통 관전포인트는 캐펙스", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, BLUE, (10,18,34), "MSFT · 7/29 장마감후",
     "매출 컨센서스 877억달러, 애저 성장률 39~40% 주목", "분기 캐펙스 컨센서스 351억달러, 전년比 100%대 증가")
band(draw, by+step, bh, TEAL, (8,28,26), "META · 7/29 장마감후",
     "매출 컨센서스 602억달러, 가이던스 상단 근접 기대", "2026 캐펙스 1,250억~1,450억달러로 상향, 재상향 여부 관건")
band(draw, by+step*2, bh, AMBER, (40,28,10), "AAPL · 7/30 장마감후",
     "매출 컨센서스 1,089억~1,100억달러", "중국 아이폰 출하 반등(1분기 +20%) 지속 여부가 변수")
band(draw, by+step*3, bh, GREEN, (10,30,22), "AMZN · 7/30 장마감후",
     "AWS 성장률 28%→33% 가속 전망", "누적 캐펙스 1,510억달러, 잉여현금흐름 12억달러로 급감")
footer(draw, "2026.07.25  |  MSFT META AAPL AMZN  같은 주 실적발표")
out = os.path.join(OUT_DIR, "2026-07-25_빅테크_실적발표_일정.png")
img.save(out); print("Saved:", out)
