from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-26"
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
    draw.line([(272,y+14),(272,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((296, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((296, y+46), detail, font=font(15), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# ── RKLB 수직계열화: 레이어별 매출원 ────────────
img, draw = base_canvas(CYAN)
draw.text((32,22), "RKLB 수직계열화, 레이어별 매출원은?", font=bold(30), fill=CYAN)
draw.text((32,76), "Launch~Software는 1회성 매출, Iridium 완결시 반복 서비스 매출 추가", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, BLUE, (10,18,34), "Launch / Components",
     "Electron·HASTE·Neutron + 부품 Merchant 판매", "발사 계약 매출 + 타사 위성 부품 단품 판매")
band(draw, by+step, bh, TEAL, (8,28,26), "Spacecraft / Payload",
     "Photon·Lightning 등 위성 버스 완제품 판매", "SDA 18기 계약, 광통신·EO 탑재체 통합")
band(draw, by+step*2, bh, AMBER, (40,28,10), "SDA T2TL-Beta 시험대",
     "US$515M Firm-Fixed-Price, 원가초과=회사부담", "내부생산 부품이 실제 마진을 만드는지 첫 검증")
band(draw, by+step*3, bh, GREEN, (10,30,22), "Iridium (거래 종결 전)",
     "가입자 250만+ 반복 서비스 매출 레이어 추가", "기업가치 $8.0B, 종결목표 2027년 중반")
footer(draw, "2026.07.26  |  RKLB  Rocket Lab")
out = os.path.join(OUT_DIR, "2026-07-26_RKLB_수직계열화_레이어.png")
img.save(out); print("Saved:", out)
