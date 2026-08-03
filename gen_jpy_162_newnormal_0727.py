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

# ── 엔저 162엔, 뉴노멀이 아니라 기울어진 레인지 ──────────────────────────
img, draw = base_canvas(RED)
draw.text((32,22), "엔저 162엔, 40년 만의 최저치는 뉴노멀이 아니다", font=bold(26), fill=RED)
draw.text((32,76), "구조적 약세는 맞지만 캐리트레이드 청산 리스크는 여전하다", font=bold(18), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, RED, (40,16,14), "환율 레벨",
     "달러당 162엔대, 1986년 이후 40년 만 최저", "실질실효환율 기준 1970년대 수준까지 하락")
band(draw, by+step, bh, AMBER, (40,28,10), "적극재정파 논리",
     "110엔대=안전자산 프리미엄의 오버슈팅", "140~150엔대를 뉴노멀로, 재정으로 서민 보완")
band(draw, by+step*2, bh, CYAN, (8,28,34), "반박 지점",
     "2024년 8월 캐리트레이드 청산, 엔 급등 재현", "안전자산 지위 소멸론과 정면 배치")
band(draw, by+step*3, bh, ORANGE, (38,22,10), "한국 영향",
     "반도체는 비켜가고 자동차·관광은 직격", "한은 금리 운신폭 압박, 크기는 시기별 변동")
footer(draw, "2026.07.27  |  USD/JPY · 엔 캐리트레이드")
out = os.path.join(OUT_DIR, "2026-07-27_엔저162엔_뉴노멀아닌이유.png")
img.save(out); print("Saved:", out)
