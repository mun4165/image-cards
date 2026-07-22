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

# ── AXT 오늘 +6.5%, 노스랜드 목표가 125달러 ──────────────────────
img, draw = base_canvas(AMBER)
draw.text((32,22), "AXT 오늘 +6.5%, 목표가 125달러로 올랐다", font=bold(32), fill=AMBER)
draw.text((32,76), "노스랜드캐피탈 상향 근거와 배경 재료를 원문 기준으로 확인했다", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, AMBER, (40,28,10), "목표가 상향",
     "노스랜드캐피탈, Outperform 유지 목표가 125달러", "NCM 성장 컨퍼런스 발표 후 저가매수 기회로 판단")
band(draw, by+step, bh, BLUE, (10,20,40), "이사회 재편",
     "세무·회계 전문가 Tracy Liu 독립이사 합류", "ACM Research 감사위원장 겸임, 미중 조세·STAR마켓 전문성")
band(draw, by+step*2, bh, TEAL, (8,28,28), "상장 경로 전환",
     "Tongmei, 상하이 STAR마켓 철회 → 홍콩거래소", "GaAs 중심에서 InP 중심으로 상장 스토리 재편")
band(draw, by+step*3, bh, GREEN, (10,30,22), "수요 근거",
     "Casela와 2027년 InP 공급계약 2,540만 달러", "6/11 서명, 약정물량 80% 미만 시 위약금 조항")
footer(draw, "2026.07.20  |  AXT / AXTI")
out = os.path.join(OUT_DIR, "2026-07-20_AXTI_노스랜드목표가.png")
img.save(out); print("Saved:", out)
