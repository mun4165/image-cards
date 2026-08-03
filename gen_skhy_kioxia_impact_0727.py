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

# ── SK하이닉스 키옥시아 최대주주 되면 바뀌는 것 ──────────
img, draw = base_canvas(AMBER)
draw.text((32,22), "SK하이닉스, 키옥시아 최대주주 되면 뭐가 바뀌나", font=bold(24), fill=AMBER)
draw.text((32,74), "지분율 1위와 의결권 확보는 다른 단계다", font=bold(19), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)
by, bh, step = 134, 128, 142
band(draw, by, bh, AMBER, (40,28,10), "지분율 1위",
     "도시바 추가매각 시 SPC(14.17%)가 지분율로 앞지를 가능성", "CB라 의결권 없음, 실질 영향 거의 없음")
band(draw, by+step, bh, RED, (40,14,14), "의결권 확보",
     "CB 주식전환 + 한국·일본 등 각국 경쟁당국 승인 필요", "통과 시 이사회 발언권 실제로 열림")
band(draw, by+step*2, bh, CYAN, (8,28,34), "반응",
     "키옥시아 '이해상충' 우려 공식표명, 일본정부도 민감 대응", "SK하이닉스 낸드 점유율 약 20%, 직접 경쟁사")
band(draw, by+step*3, bh, GREEN, (10,30,22), "SK그룹 내부",
     "2028년까지 의결권 15%↓ 자체 약속, 승인 통과 신중론", "지금은 가능성 단계, 확정 시나리오 아님")
footer(draw, "2026.07.27  |  SK하이닉스 · 키옥시아  |  지분구조 영향 분석")
out = os.path.join(OUT_DIR, "2026-07-27_SKHY_키옥시아_최대주주_영향.png")
img.save(out); print("Saved:", out)
