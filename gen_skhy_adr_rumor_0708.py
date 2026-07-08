from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-08"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "SK하이닉스 나스닥 상장 D-2", font=bold(32), fill=ACCENT)
draw.text((32,80), "발행가 낮추려고 판다는 소문, 숫자로 따져봤다", font=bold(24), fill=GRAY)
draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
    draw.line([(250,y+18),(250,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((278, y+22), headline, font=bold(25), fill=WHITE)
    draw.text((278, y+64), d1, font=font(19), fill=color)
    draw.text((278, y+96), d2, font=font(17), fill=GRAY)

by = 150; bh = 152; step = 170
band(by, bh, BLUE, (10,20,34), "지렛대",
     "기준가 255.5만 → 242.5만 원으로 인하",
     "잠정가 ADR당 24만2,500원(≈158달러) = 국내 종가의 1/10",
     "7/7 장중 -6.7%, 218만6,000원까지 급락")
band(by+step, bh, RED, (40,15,15), "반박",
     "7/7 하락은 반도체 업종 전체 투매",
     "필라델피아 반도체지수 -4.5%, MU -4.71%($938.38)",
     "촉발 = 삼성 실적 + DeepSeek 자체칩 보도, 발행가와 무관")
band(by+step*2, bh, CYAN, (8,28,34), "체크포인트",
     "7/9 최종 발행가 · 7/10 나스닥 데뷔(SKHY)",
     "수요는 물량의 수 배 초과 (베일리 기포드 등 3사 ~70억 달러)",
     "선례: TSMC ADR 대만 원주 대비 16% 프리미엄")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.08  |  SKHY  SK Hynix", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-08_SK하이닉스_ADR발행가매도설.png")
img.save(out); print("Saved:", out)
