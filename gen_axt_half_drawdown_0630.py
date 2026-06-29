from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-30"
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

draw.text((32,22), "AXT(AXTI) 고점 대비 반토막", font=bold(40), fill=ACCENT)
draw.text((32,80), "논지가 깨진 건지, 거품이 빠진 건지", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "지금 가격", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "1년 새 $1.85 → $143 → $71 — 70배 뛴 뒤 절반 반납",
          font=bold(22), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "논지는 멀쩡",
     "통행료 자리는 강화됐다", "6/18 Casela $25.4M InP 공급계약 · 4월 $632.5M 증설 capex")
band(by+step, bh, RED, (40,16,16), "진짜 달라진 것",
     "치어리딩 안 한다", "856만 주 희석 · 대미 수출허가 미해결 · 출발점이 $71")
band(by+step*2, bh, BLUE, (12,20,38), "갈라서 볼 것",
     "주가 ≠ 논지", "답은 다음 분기 InP 백로그·수출허가지, 오늘 호가창이 아니다")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.30  |  빠진 건 주가지 논지가 아니다 — 단, 변한 변수는 짚는다", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-30_AXT_고점대비반토막.png")
img.save(out); print("Saved:", out)
