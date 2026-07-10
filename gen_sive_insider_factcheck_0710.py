from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-10"
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

draw.text((32,24), "SIVE CEO 내부자매수 팩트체크", font=bold(30), fill=ACCENT)
draw.text((32,80), "매수는 진짜, 그런데 같은 날 더 큰 매도가 있었다", font=bold(22), fill=GRAY)
draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
    draw.line([(250,y+18),(250,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((278, y+22), headline, font=bold(24), fill=WHITE)
    draw.text((278, y+64), d1, font=font(18), fill=color)
    draw.text((278, y+96), d2, font=font(17), fill=GRAY)

by = 150; bh = 152; step = 170
band(by, bh, BLUE, (10,20,34), "확인된 사실",
     "7/9 CEO 포함 내부자 4명이 총 241만 크로나 매수",
     "CEO Vickram Vathulya 24,000주 · 약 96만 크로나",
     "이사 3명(Thomson·Raj·Svancar) 합산 145만 크로나 추가 매수")
band(by+step, bh, RED, (40,15,15), "숫자 정정",
     "\"100만 크로나\" 아님 — CEO 매수분은 정확히 96만 크로나",
     "같은 날 포토닉스 사업부장 McKee는 400만+크로나 전량 매도",
     "GFS·Jabil 파트너십도 새 소식 아님(각 6/2·4/15 기발표)")
band(by+step*2, bh, CYAN, (8,28,34), "놓친 맥락",
     "매수 시점이 경영진 락업 해제(7/16) 직전이라는 점",
     "회사는 2분기 실적일을 8/6→8/27로 조정, 락업 후 매도창구 개방",
     "CEO 매수분은 기존 보유(2억 크로나+)의 0.5%도 안 되는 규모")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.10  |  SIVE  Sivers Semiconductors", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-10_SIVE_CEO내부자매수팩트체크.png")
img.save(out); print("Saved:", out)
