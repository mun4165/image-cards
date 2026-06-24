from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-24"
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

# 헤더
draw.text((32,22), "AXTI는 컴파운더가 아니라 사이클주다", font=bold(37), fill=ACCENT)
draw.text((32,74), "InP 병목은 진짜다 — 다만 만료일이 찍혀 있다", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

# 테제 박스
ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "실리콘은 빛을 못 만든다", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "발광은 InP에서만 — AXT가 광학 스택의 진짜 밑바닥", font=bold(26), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(22), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(21), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, AMBER, (40,22,10), "만료일 ①  기술",
     "양자점 레이저, 실리콘 직접 성장", "성공 시 InP 기판 자체를 우회 (3~5년+)")
band(by+step, bh, GREEN, (10,32,24), "만료일 ②  리쇼어링",
     "Coherent 텍사스 자체 InP 2배 증설", "고객이 직접 만들기 시작 = 이탈 동기")
band(by+step*2, bh, ORANGE, (40,22,10), "만료일 ③  중국",
     "Tongmei STAR마켓 IPO 4년째 표류", "최대 변수는 수요 아닌 수출허가")

# 결론 박스
gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "어떻게 보느냐", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "AI 수요 베팅이 아니라  →  중국 허가 정상화 + 수급 사이클 베팅",
          font=bold(22), fill=CYAN)
draw.text((52,gy+74), "매도 시그널: 공급이 수요 따라잡음 · QD레이저 양산 진전",
          font=font(15), fill=GRAY)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.24  |  AXTI  AXT Inc.", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-24_AXTI_사이클주_InP병목만료일.png")
img.save(out); print("Saved:", out)
