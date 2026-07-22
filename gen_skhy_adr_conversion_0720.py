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

# ── SK하이닉스 원주-ADR 상호전환 ──────────────────────────
img, draw = base_canvas(AMBER)
draw.text((32,22), "원주-ADR 상호전환 29일부터, 프리미엄은 안 꺼진다", font=bold(32), fill=AMBER)
draw.text((32,76), "예탁결제원 발표는 실재, 괴리 즉시 해소는 구조적으로 어렵다", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, CYAN, (8,28,34), "발표",
     "7/18 예탁결제원, 상호전환 신청 7/29 이후 가능", "원주 신주 국내 상장일 기준, 씨티은행이 세부일정 공지")
band(draw, by+step, bh, RED, (40,14,14), "프리미엄",
     "원주 7/10 218만원 → 7/14 191.3만원(-12.25%)", "ADR은 원주 환산가 대비 50%대 프리미엄 형성")
band(draw, by+step*2, bh, AMBER, (40,28,10), "비대칭 한도",
     "ADR→원주 무제한, 원주→ADR은 발행한도 내만", "F-6 한도 25%, 기발행 2.5% 제외 여유분 약 22.5%")
band(draw, by+step*3, bh, GREEN, (10,30,22), "TSMC 사례",
     "상호전환 있어도 작년 19.1%·올해 17.5% 유지", "SK하이닉스도 완전 해소보다 축소·유지 쪽 무게")
footer(draw, "2026.07.20  |  SK하이닉스 ADR")
out = os.path.join(OUT_DIR, "2026-07-20_SK하이닉스_ADR상호전환.png")
img.save(out); print("Saved:", out)
