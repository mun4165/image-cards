from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-29"
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

draw.text((32,22), "반도체 사흘째 급락, 코스피 8,200선", font=bold(36), fill=ACCENT)
draw.text((32,74), "HBM 사이클이 꺾인 건가 — 수급발 약세와 펀더멘털을 가르는 법", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "같은 급락이라도 원인이 다르면 결론이 정반대다", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "떨어지는 차트는 공포를, 데이터는 답을 준다", font=bold(24), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "가능성 A · 노이즈",
     "수급발 약세", "2주 급등 차익실현 + 외국인 매도 → 단순 되돌림")
band(by+step, bh, RED, (40,16,16), "가능성 B · 위험",
     "펀더멘털 훼손", "메모리 수요 사이클 자체가 꺾인 신호 → 추세 전환")
band(by+step*2, bh, BLUE, (12,20,38), "지금 사실",
     "가격은 빠졌으나 수요 데이터는 미발표", "방아쇠는 '검은 화요일' 후 외국인 매도 = 수급 쪽")

gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "답을 줄 한 날짜 — 7월 29일 SK하이닉스 2분기 실적", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "이익 숫자가 아니라 → 비트그로스 · capex · HBM 코멘트를 본다",
          font=bold(20), fill=CYAN)
draw.text((52,gy+76), "한국 기업은 숫자 가이던스를 안 준다 · 강하다면 노이즈, 둔화면 사이클 경계",
          font=font(15), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.29  |  무서워서 던지기 전에, 무엇이 답을 줄 자료이고 그게 언제 나오는지부터 안다", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-29_HYNIX_수급이냐사이클이냐.png")
img.save(out); print("Saved:", out)
