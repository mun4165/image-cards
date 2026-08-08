from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-08-04"
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
    draw.text((60, y+14), label, font=bold(17), fill=color)
    draw.line([(360,y+14),(360,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((384, y+15), headline, font=bold(18), fill=WHITE)
    draw.text((384, y+45), detail, font=font(14), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

BY, BH, STEP = 122, 98, 110

img, draw = base_canvas(ORANGE)
draw.text((32,22), "AMD 8월 4일 실적, 진짜 관전포인트는 3분기다", font=bold(25), fill=ORANGE)
draw.text((32,74), "2분기 숫자보다 하반기 가이던스가 핵심인 이유", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, ORANGE, (44,20,10), "가이던스  |  2분기 컨센서스 이미 근접",
     "매출 112억달러 ±3억  ·  컨센 113억달러", "총마진 56%, 서프라이즈 여지 크지 않음")
band(draw, by+step, bh, BLUE, (10,20,40), "회사 발언  |  성장의 본체는 하반기",
     "MI450 샘플링 중, 양산은 하반기 램프업", "EPYC도 2분기 70%+ 성장 예고")
band(draw, by+step*2, bh, CYAN, (10,28,32), "체크1  |  3분기 가이던스 상향폭",
     "2분기 대비 얼마나 더 높은 성장률 제시하나", "하반기 램프업 실제 시작 신호")
band(draw, by+step*3, bh, GREEN, (10,30,22), "체크2  |  MI450·헬리오스 코멘트 톤",
     "추상적 표현 vs 구체적 물량·계약 규모", "톤 업그레이드 여부가 관건")
band(draw, by+step*4, bh, AMBER, (40,30,8), "리스크  |  숫자 넘겨도 주가 빠질 구조",
     "하반기 기대 이미 반영, 미지근하면 하락", "이미 반영된 기대 vs 새 정보의 게임")
footer(draw, "2026.08.04  |  AMD 2분기 실적 발표 (장 마감 후)")
out = os.path.join(OUT_DIR, "2026-08-04_AMD_실적프리뷰.png")
img.save(out); print("Saved:", out)
