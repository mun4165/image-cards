from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-28"
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

draw.text((32,22), "한 도시가 60년을 가로질러", font=bold(36), fill=ACCENT)
draw.text((32,74), "소련 최초의 반도체와 LPTH 방산 렌즈, 같은 도시 리가(Riga)", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "칩워의 명제 — 기술은 청사진으로 복제되지 않는다", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "기술은 문서가 아니라 도시의 손(암묵지)에 축적된다", font=bold(24), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "1936 · 정밀광학",
     "리가 VEF, 세계 최소 카메라 미녹스(Minox)", "정밀광학 제조 DNA가 그 도시에 심긴다")
band(by+step, bh, BLUE, (12,20,38), "1962 · 반도체",
     "오소킨 RZPP, 소련 최초의 집적회로(IC)", "재료=게르마늄, 용도=우주·군사 · 칩워 7장 등장")
band(by+step*2, bh, ORANGE, (38,24,8), "현재 · 방산광학",
     "LightPath(ISP Optics), 게르마늄 IR 렌즈", "같은 도시·같은 소재·같은 손·같은 군우주 용도")

gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "투자자가 가져갈 한 줄", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "기업이 아니라 그 기업이 선 땅의 60년 누적을 보라",
          font=bold(22), fill=CYAN)
draw.text((52,gy+76), "보조금을 퍼부어도 못 베끼는 해자 = 한 도시가 쌓은 손의 숙련",
          font=font(15), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.28  |  게르마늄이라는 한 소재와 리가라는 한 도시가 반도체와 방산을 같은 실로 꿴다", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-28_LPTH_리가게르마늄_도시의손.png")
img.save(out); print("Saved:", out)
