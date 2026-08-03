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

# ── 알파벳 캐펙스 상향, 주가는 빠지고 마이크론은 오른 괴리 ──────────────────
img, draw = base_canvas(GREEN)
draw.text((32,22), "알파벳 캐펙스 195억~205억달러로 상향", font=bold(30), fill=GREEN)
draw.text((32,76), "주가는 6%대 급락, 같은 날 마이크론은 3.20% 상승", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, GREEN, (10,30,22), "알파벳 7/22 실적",
     "2분기 캐펙스 449억달러 사상최대, 매출 24%↑ 컨센서스 상회", "그런데도 주가는 캐펙스 부담으로 6%대 급락")
band(draw, by+step, bh, AMBER, (40,28,10), "가이던스 변화",
     "2026년 캐펙스 1,800억~1,900억 → 1,950억~2,050억달러", "2027년엔 '대폭 확대' 추가 예고")
band(draw, by+step*2, bh, CYAN, (8,28,34), "마이크론(MU)은 반대 반응",
     "990.21달러, +3.20% 마감 — 서버향 HBM·D램 공급사", "캐펙스=알파벳 비용, 마이크론엔 곧 수요")
band(draw, by+step*3, bh, BLUE, (10,20,40), "확인 안 된 것",
     "가이던스는 상위 지표일 뿐, 확정 발주 물량 아님", "다음 분기 HBM 매출 비중으로 실제 반영 확인 필요")
footer(draw, "2026.07.24  |  MU / GOOGL")
out = os.path.join(OUT_DIR, "2026-07-24_MU_알파벳캐펙스195억달러.png")
img.save(out); print("Saved:", out)
