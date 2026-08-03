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

# ── 샌프란시스코 AI 서밋, 9500억달러의 실체 ──────────
img, draw = base_canvas(CYAN)
draw.text((32,22), "9500억달러, 샌프란 AI 서밋 숫자의 실체", font=bold(27), fill=CYAN)
draw.text((32,74), "국가 투자유치액 아닌, 삼성·SK 5년 반도체 공급계약 합산", font=bold(19), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)
by, bh, step = 134, 128, 142
band(draw, by, bh, CYAN, (8,28,34), "9500억달러",
     "삼성전자·SK가 빅테크와 맺는 5년치 메모리 반도체 장기공급 합산", "7/24 '샌프란시스코 AI 선언'에서 발표")
band(draw, by+step, bh, AMBER, (40,28,10), "그 안의 SK 몫",
     "SK-엔비디아 5000억달러 LOI, 2GW 데이터센터 + HBM4 공동개발", "9500억달러 중 SK그룹이 차지하는 부분")
band(draw, by+step*2, bh, GREEN, (10,30,22), "그날 모인 사람들",
     "이재용·최태원·정의선·이해진, 젠슨 황·올트먼·아모데이·혹 탄", "만찬서 젠슨 황 '한국은 지금 AI 황금시대'")
band(draw, by+step*3, bh, RED, (40,14,14), "확인해둘 지점",
     "다수 항목이 구속력 없는 의향서(LOI) 단계", "확정 계약 전환 시점·조건은 후속 확인 필요")
footer(draw, "2026.07.27  |  삼성전자 · SK · 엔비디아  |  샌프란시스코 AI 서밋")
out = os.path.join(OUT_DIR, "2026-07-27_SK_샌프란시스코AI서밋_950B.png")
img.save(out); print("Saved:", out)
