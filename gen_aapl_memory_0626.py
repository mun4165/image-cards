from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-26"
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

draw.text((32,22), "AAPL 어제 6% 급락, 원인은 칩값이 아니다", font=bold(36), fill=ACCENT)
draw.text((32,74), "팀 쿡이 말한 \"100년에 한 번 오는 홍수\" — 메모리", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

# 핵심 메시지 박스
ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "세계 1등 구매자조차 못 누른 메모리값", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "애플의 비용은 곧 메모리 회사의 매출이다", font=bold(26), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, RED, (40,16,16), "① 애플  AAPL  -6%",
     "맥·아이패드 가격 제품당 $100~300 인상", "원가 못 눌러 소비자에 전가 · 아이폰은 동결")
band(by+step, bh, AMBER, (40,22,10), "② 원인  메모리값",
     "디램 계약가 1분기에 약 2배 (역대 최대)", "AI 데이터센터가 올해 메모리 70% 흡수")
band(by+step*2, bh, GREEN, (10,32,24), "③ 반대편  MU  +16%",
     "애플이 운 날 마이크론은 웃었다", "같은 뉴스의 양면 · 돈은 공급자 쪽에 고인다")

gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "한 줄 요약", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "애플 급락 = 애플이 약해서가 아니라 사이클이 세서",
          font=bold(22), fill=CYAN)
draw.text((52,gy+74), "소비자 쪽=악재 · 공급자 쪽=호재 · 양면을 같이 봐야 돈이 보인다",
          font=font(15), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.26  |  AAPL 가격 인상 — 메모리 100년 홍수의 양면", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-26_AAPL_메모리100년홍수_양면.png")
img.save(out); print("Saved:", out)
