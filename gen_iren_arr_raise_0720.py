from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-20"
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
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(196,y+14),(196,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((220, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((220, y+46), detail, font=font(15), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# ── IREN 신규 계약 28억 달러 + ARR 상향 ──────────────────────────
img, draw = base_canvas(CYAN)
draw.text((32,22), "IREN 신규 계약 28억 달러, ARR 목표 40억으로", font=bold(32), fill=CYAN)
draw.text((32,76), "프리마켓 상승 배경, 발표 원문 기준으로 확인했다", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, CYAN, (8,28,34), "발표",
     "7/20 오전 7시(ET) 신규 다년 계약 28억 달러 체결", "한국시간 20시, 리딩 AI 개발사 다수와 합산 계약")
band(draw, by+step, bh, GREEN, (10,30,22), "ARR 상향",
     "연말 목표 37억 달러 → 40억 달러 이상", "목표치의 약 85%가 이미 계약으로 확보")
band(draw, by+step*2, bh, AMBER, (40,28,10), "5월 계약과 차이",
     "엔비디아 단일 34억 달러 vs 이번 다수사 합산 28억", "고객군: MSFT·NVDA·Perplexity 등 + 신규 1곳 미공개")
band(draw, by+step*3, bh, BLUE, (10,20,40), "자금 구조",
     "GPU capex의 45%를 고객 선입금으로 충당", "6/30 기준 현금 76억 달러, 평균 계약기간 약 4년")
footer(draw, "2026.07.20  |  IREN")
out = os.path.join(OUT_DIR, "2026-07-20_IREN_ARR상향.png")
img.save(out); print("Saved:", out)
