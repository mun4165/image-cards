from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-23"
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

# ── LPTH $13M 광학조립체 후속발주, 7/15건과 별개 ──────────────────────────
img, draw = base_canvas(CYAN)
draw.text((32,22), "LightPath, $1,300만 광학조립체 후속발주", font=bold(30), fill=CYAN)
draw.text((32,76), "지난주 $1,100만 카메라 발주와는 별개 계약, 원문 기준 확인", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, CYAN, (8,28,34), "7/22 신규건",
     "$1,300만, C-UAS·방산 시스템 공급업체향 광학조립체", "완제품 카메라 아닌 부품·서브어셈블리 성격")
band(draw, by+step, bh, AMBER, (40,28,10), "7/15건과 구분",
     "$1,100만 적외선카메라(완제품)+BlackDiamond 소재전환", "금액·고객표기·납품형태·PR번호 전부 다른 별개계약")
band(draw, by+step*2, bh, GREEN, (10,30,22), "마진 구도",
     "회사 자체 코멘트: 조립체·완제품이 부품보다 고마진", "직전분기 총이익률 29%→36%, 조립체 비중확대가 주원인")
band(draw, by+step*3, bh, BLUE, (10,20,40), "확인 안 된 것",
     "두 계약 고객사 동일 여부 미확인(둘 다 익명)", "납품완료 예상 2027년, 소재 언급은 이번 건에 없음")
footer(draw, "2026.07.23  |  LPTH")
out = os.path.join(OUT_DIR, "2026-07-23_LPTH_13M광학조립체후속발주.png")
img.save(out); print("Saved:", out)
