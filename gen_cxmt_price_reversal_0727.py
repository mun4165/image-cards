from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-27"
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

# ── CXMT, 삼성보다 비싸게 받는다 ──────────
img, draw = base_canvas(AMBER)
draw.text((32,22), "CXMT, 삼성보다 비싸게 받는다", font=bold(27), fill=AMBER)
draw.text((32,74), "애플까지 접촉한 이유는 저가가 아니라 지렛대", font=bold(19), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)
by, bh, step = 134, 128, 142
band(draw, by, bh, AMBER, (40,28,10), "가격 역전",
     "64GB DDR5 서버메모리, 삼성(약1,240달러)보다 CXMT가 더 비쌈", "7/24 로이터, 화웨이 할인요청도 거부")
band(draw, by+step, bh, RED, (40,14,14), "저가 전략 폐기 이유",
     "삼성·SK·마이크론이 HBM에 캐파 몰빵, 범용D램 공급 오히려 감소", "AI 수요로 표준 D램가 2026년 초 55~60% 폭등")
band(draw, by+step*2, bh, CYAN, (8,28,34), "애플의 접촉",
     "CXMT·YMTC와 협상 중, 기술검증까지만 진행 (공급계약 아직 없음)", "목적은 저가 아닌 3사 가격협상 지렛대")
band(draw, by+step*3, bh, GREEN, (10,30,22), "매출 구조",
     "2025년 매출 99%가 범용 DDR/LPDDR, HBM 비중 2% 미만", "고객은 화웨이·샤오미 등 중국 내수 위주")
footer(draw, "2026.07.27  |  CXMT(창신메모리)  |  삼성전자 · 애플 · 화웨이")
out = os.path.join(OUT_DIR, "2026-07-27_CXMT_삼성보다_비싸게받는이유.png")
img.save(out); print("Saved:", out)
