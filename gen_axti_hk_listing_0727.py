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

# ── AXT 통메이 홍콩상장, 632억 증자와는 다른 이야기 ──────────
img, draw = base_canvas(TEAL)
draw.text((32,22), "AXT 자회사 통메이, 상해 대신 홍콩 상장", font=bold(24), fill=TEAL)
draw.text((32,74), "6.3억 달러 증자와는 시점도 목적도 다른 사건이다", font=bold(19), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)
by, bh, step = 134, 128, 142
band(draw, by, bh, AMBER, (40,28,10), "4월 21일 증자",
     "AXT 본사가 나스닥에서 직접 조달, 옵션 포함 6.325억 달러", "이미 완료된 사건, 통메이 캐파 확장 자금")
band(draw, by+step, bh, RED, (40,14,14), "6월 26일 철회",
     "상해거래소 스타마켓 상장 신청 철회, 7/8 공식 접수", "GaAs·마이크로LED 중심 서사였음")
band(draw, by+step*2, bh, CYAN, (8,28,34), "홍콩 상장 전환",
     "새 신청은 InP(인화인듐) 중심으로 재편, 아직 신청 단계", "완료되면 통메이 지분가치 첫 시장평가")
band(draw, by+step*3, bh, GREEN, (10,30,22), "캐파 목표",
     "InP 분기 생산 2026말 약 3500만$ → 2027~28 6500만~7000만$", "실탄은 이미 4월 증자로 확보")
footer(draw, "2026.07.27  |  AXT · 통메이  |  홍콩상장 전환 분석")
out = os.path.join(OUT_DIR, "2026-07-27_AXTI_통메이_홍콩상장.png")
img.save(out); print("Saved:", out)
