from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-15"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(239,68,68)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "IBM  뭘 파는 회사길래 -25%", font=bold(22), fill=GRAY)
draw.text((32,58), "사업구조부터 보고, 크리슈나 발언 두 갈래로 정리", font=bold(28), fill=ACCENT)
draw.line([(32,110),(W-32,110)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(20), fill=color)
    draw.line([(280,y+16),(280,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((306, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((306, y+56), d1, font=font(16), fill=color)
    draw.text((306, y+84), d2, font=font(15), fill=GRAY)

by = 130; bh = 168; step = 186
band(by, bh, CYAN, (10,28,32), "IBM이 파는 것",
     "소프트웨어·컨설팅·인프라 3사업부",
     "2025 매출: SW $299.6억 > 컨설팅 $210.6억 > 인프라 $157.2억",
     "메인프레임·서버인 인프라가 셋 중 가장 작은 사업부")
band(by+step, bh, RED, (40,14,14), "크리슈나 발언 두 갈래",
     "매크로 요인과 자체 실행 문제",
     "고객사 메모리·서버 선매입으로 SW·컨설팅 예산 축소",
     "\"we faltered\" — 대형 계약 다수 예정 시점에 못 닫힘")
band(by+step*2, bh, ORANGE, (40,26,10), "소프트웨어 시장 영향",
     "SW 매출 자체는 이번에도 +5% 성장",
     "흔들린 건 실적이 아니라 예산 우선순위",
     "메모리·서버값 계속 오르면 다른 벤더로도 번질 수 있는 흐름")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.15  |  IBM  Business Breakdown", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-15_IBM_사업구조_대표이미지.png")
img.save(out); print("Saved:", out)
