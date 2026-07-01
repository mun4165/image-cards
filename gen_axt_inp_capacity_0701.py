from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-01"
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

draw.text((32,22), "AXT, 하반기 InP 캐파 2배", font=bold(40), fill=ACCENT)
draw.text((32,80), "말이 숫자로 찍히는지 보는 체크포인트", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "약속", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "InP(인듐인화물) 캐파 하반기 2배 → 2027 또 2배 · Q1 콜 재확인",
          font=bold(20), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "증거",
     "말이 아니라 서명·재원으로 깔렸다", "6/18 Casela 2,540만 달러 계약 · 4월 6.3억 달러 조달")
band(by+step, bh, BLUE, (12,20,38), "확인",
     "분기마다 세 숫자를 본다", "InP 매출·백로그 / 대미 수출 허가 / 희석 후 주당가치")
band(by+step*2, bh, AMBER, (40,30,8), "주의",
     "캐파 2배 ≠ 매출 2배", "수요·허가 막히면 늘린 생산능력은 비용으로 남는다")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.01  |  헤드라인이 아니라 분기 실적이 답을 줄 자료다", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-01_AXT_InP캐파2배.png")
img.save(out); print("Saved:", out)
