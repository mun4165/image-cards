from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-30"
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
    draw.line([(268,y+14),(268,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((292, y+15), headline, font=bold(18), fill=WHITE)
    draw.text((292, y+45), detail, font=font(14), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# ── 오라클 CDS 18년 만에 최고 vs 네오클라우드 CDS ────
img, draw = base_canvas(RED)
draw.text((32,22), "오라클 부도보험료(CDS), 2008년 이후 최고치", font=bold(25), fill=RED)
draw.text((32,74), "5년물 CDS 215bp, 연초 144bp에서 7개월 만에 71bp 상승", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = 124, 106, 119
band(draw, by, bh, RED, (40,14,14), "CDS  |  7/28 기준",
     "오라클 5년물 215bp · 2008년 금융위기 집계 이후 최고치", "채권 1,000만달러당 연 21.5만달러 보험료 필요")
band(draw, by+step, bh, ORANGE, (44,20,10), "강등  |  7/9 S&P",
     "신용등급 BBB → BBB-(투자등급 최하단, 투기등급 한 단계 위)", "capex 600억→900억~950억달러, FCF적자 240억→420억달러")
band(draw, by+step*2, bh, AMBER, (40,28,10), "구조  |  RPO 6,380억달러",
     "전년比 363% 급증, 이 중 절반가량이 오픈AI 한 곳", "오라클이 먼저 데이터센터 짓고, 오픈AI가 나중에 대금 지급")
band(draw, by+step*3, bh, BLUE, (10,20,40), "빅테크  |  같은 방향, 다른 폭",
     "엔비디아 79bp · 알파벳 67bp, 둘 다 사상 최고치", "CDX IG지수는 안정적 — 시장전체 아닌 AI집중기업만 경고등")
band(draw, by+step*4, bh, GREEN, (10,30,22), "네오클라우드  |  훨씬 크게 반응",
     "CoreWeave CDS 855bp(부도확률 약50%) · 한달 -36%", "Nebius 한달 -43% · IREN도 동반하락(CDS수치 미확인)")
footer(draw, "2026.07.30  |  $ORCL  오라클 · CoreWeave · Nebius · IREN")
out = os.path.join(OUT_DIR, "2026-07-30_ORCL_CDS부도보험료18년만최고.png")
img.save(out); print("Saved:", out)
