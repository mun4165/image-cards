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

# ── CXMT 상장 첫날 472% 폭등 ──────────
img, draw = base_canvas(RED)
draw.text((32,22), "CXMT 상장 첫날 472% 폭등", font=bold(27), fill=RED)
draw.text((32,74), "공모가 8.66위안 → 장중 최고 49.88위안, 시총 1위 등극", font=bold(19), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)
by, bh, step = 134, 128, 142
band(draw, by, bh, RED, (40,14,14), "장중 최고가",
     "49.88위안, 공모가 8.66위안 대비 476% 급등", "7/27 상하이 과창판 상장 첫날")
band(draw, by+step, bh, AMBER, (40,28,10), "시가총액",
     "최고 3조1,400억위안(약 680조원), 중국공상은행 제치고 본토 1위", "유통물량은 전체의 6%대에 불과")
band(draw, by+step*2, bh, CYAN, (8,28,34), "IPO 규모",
     "공모자금 최대 666억1,000만위안(약 14조4천억원)", "2026년 아시아 최대 IPO")
band(draw, by+step*3, bh, GREEN, (10,30,22), "세계 D램 점유율",
     "삼성 38% · SK하이닉스 29% · 마이크론 22% · CXMT 8%", "1년 전 3%에서 8%로 확대")
footer(draw, "2026.07.27  |  CXMT(창신메모리)  |  상하이 과창판 상장")
out = os.path.join(OUT_DIR, "2026-07-27_CXMT_창신메모리_상장첫날.png")
img.save(out); print("Saved:", out)
