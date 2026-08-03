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

# ── FOMC 7월 29일, 동결 확률 며칠새 출렁 ────────────────────
img, draw = base_canvas(BLUE)
draw.text((32,22), "FOMC 7월 29일, 동결 확률 며칠새 출렁", font=bold(30), fill=BLUE)
draw.text((32,76), "CME 페드워치 기준, 워시 신임 의장 매파 발언과 겹친 흐름", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, BLUE, (10,20,34), "회의 일정",
     "7/28~29 이틀회의, 29일 오후2시(ET) 결과발표", "한국시간 30일 새벽3시, 2시30분 기자회견")
band(draw, by+step, bh, AMBER, (40,28,10), "확률 흐름",
     "동결 확률 7/21 87% → 7/23 63.5%로 급락", "인상 확률 20~30%대, 인하는 사실상 0%")
band(draw, by+step*2, bh, ORANGE, (40,24,10), "매파 배경",
     "6월 근원물가 전년比 3.7%, 목표 2% 크게 상회", "워시 신임의장 강경발언+포워드가이던스 폐지")
band(draw, by+step*3, bh, CYAN, (8,28,34), "시장 영향",
     "동결도 워시 기자회견 톤 따라 조정 가능성", "서프라이즈 인상시 나스닥·반도체 가장 민감")
footer(draw, "2026.07.24  |  FOMC")
out = os.path.join(OUT_DIR, "2026-07-24_FOMC_동결확률출렁.png")
img.save(out); print("Saved:", out)
