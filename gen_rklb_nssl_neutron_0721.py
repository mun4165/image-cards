from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-21"
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

# ── RKLB NSSL 계약한도 확대 + Neutron 엔진시험 ──────────────────────────
img, draw = base_canvas(CYAN)
draw.text((32,22), "로켓랩, NSSL 계약한도 확대 + Neutron 엔진시험", font=bold(30), fill=CYAN)
draw.text((32,76), "발사 임무 수주가 아니라 경쟁 자격 확대, 발표 원문 기준 확인", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, CYAN, (8,28,34), "NSSL 계약",
     "7/20 Phase 3 Lane 1 한도 56억 → 170억 달러", "7개사(SpaceX·ULA·Blue Origin·Rocket Lab 등) 공동 대상")
band(draw, by+step, bh, AMBER, (40,28,10), "의미 구분",
     "신규 임무 수주 아님, 경쟁 자격 한도만 증액", "RKLB 개별 몫은 발표에 명시 안 됨, 향후 입찰로 결정")
band(draw, by+step*2, bh, GREEN, (10,30,22), "Neutron 엔진시험",
     "7/14 2단 AVac 엔진 풀 듀레이션 연소시험 완료", "1단 대비 추력 1.2배, 노즐 2.5m 더 김")
band(draw, by+step*3, bh, BLUE, (10,20,40), "표현 확인",
     "회사 발표는 '완료'까지, '성공' 표현은 없음", "Neutron 첫 비행 목표 2026년 말")
footer(draw, "2026.07.21  |  RKLB")
out = os.path.join(OUT_DIR, "2026-07-21_RKLB_NSSL계약확대_Neutron엔진시험.png")
img.save(out); print("Saved:", out)
