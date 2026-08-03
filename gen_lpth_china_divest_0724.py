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

# ── LPTH 중국 자회사 450만달러 매각, 매수인=현지 경영진 ────────────────────
img, draw = base_canvas(ORANGE)
draw.text((32,22), "LightPath, 중국 자회사 450만달러 매각", font=bold(30), fill=ORANGE)
draw.text((32,76), "매수인은 그 법인의 기존 경영진 소유 회사, 원문 8-K 기준", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, ORANGE, (40,24,10), "7/23 최종계약",
     "전장 소재 LPOIZ 제조시설·사업 전체, 450만달러 현금", "매수인 Hengtu Optical=현지 경영진 소유 법인(MBO)")
band(draw, by+step, bh, AMBER, (40,28,10), "지급 구조",
     "최대 5년 분할, 연 최소 50만달러+금융이자 4%", "연체 시 지연이자 7%, 목돈 일시수령 아닌 채권성격")
band(draw, by+step*2, bh, CYAN, (8,28,34), "매각 이유",
     "NDAA(국방수권법) 준수=서방 진영 제조기지 요건", "방산 C-UAS 발주 자격 확보 목적, 최근 발주 흐름과 연결")
band(draw, by+step*3, bh, GREEN, (10,30,22), "완전 철수 아님",
     "매각 후에도 Hengtu가 美·유럽 상업고객향 제3자 공급 지속", "소유·회계상 중국 노출만 분리, 제품 공급망은 유지")
footer(draw, "2026.07.24  |  LPTH")
out = os.path.join(OUT_DIR, "2026-07-24_LPTH_중국자회사450만달러매각.png")
img.save(out); print("Saved:", out)
