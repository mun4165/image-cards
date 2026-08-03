from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-29"
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
    draw.line([(240,y+14),(240,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((264, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((264, y+46), detail, font=font(15), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# ── AXT 통메이, 상해 철회하고 홍콩으로 ─────────────────
img, draw = base_canvas(TEAL)
draw.text((32,22), "AXT 자회사 통메이, 상해 대신 홍콩 상장", font=bold(26), fill=TEAL)
draw.text((32,76), "상장 스토리 재편 + PE펀드 상환청구권, 두 갈래로 본다", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 128, 142
band(draw, by, bh, RED, (40,14,14), "6/26 철회",
     "상해거래소 스타마켓 상장 신청 철회, 7/8 SSE 공식 접수", "3년 넘게 대기하던 GaAs·마이크로LED 중심 신청")
band(draw, by+step, bh, CYAN, (8,28,34), "홍콩 전환",
     "새 신청은 InP(인화인듐)·AI데이터센터 중심으로 재편", "국제 기관·리테일 투자자 접근성 확대가 회사 측 논리")
band(draw, by+step*2, bh, AMBER, (40,28,10), "PE펀드 상환청구권",
     "중국 PE펀드 11곳, RMB 3.24억위안(약 4900만$) 투자분", "상해 상장 전제 계약 → 철회로 원금 상환청구권 자동발동")
band(draw, by+step*3, bh, GREEN, (10,30,22), "현재 상태",
     "회사는 전액 상환 자금 보유 주장, 펀드별 유지·상환 협의중", "홍콩 신청 시점·목표 조달규모는 아직 미공개")
footer(draw, "2026.07.29  |  $AXTI  AXT · 통메이")
out = os.path.join(OUT_DIR, "2026-07-29_AXTI_통메이_홍콩상장.png")
img.save(out); print("Saved:", out)
