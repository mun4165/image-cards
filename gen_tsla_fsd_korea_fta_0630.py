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

draw.text((32,22), "테슬라 FSD 한국 도입", font=bold(40), fill=ACCENT)
draw.text((32,80), "막는 건 차가 아니라 법, 그 법에는 우회로가 있다", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "핵심", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "미국산이면 한미 FTA 자기인증으로 정식 승인 전에 먼저 열린다",
          font=bold(22), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "이미 열림",
     "미국산 HW4 S·X·사이버트럭", "2025.11말 감독형 FSD를 한미 FTA 근거로 OTA 배포")
band(by+step, bh, RED, (40,16,16), "막힌 쪽",
     "중국산 모델3·모델Y", "안전기준이 달라 못 탐 — 무단 활성화 적발은 이 차별 탓")
band(by+step*2, bh, BLUE, (12,20,38), "미국산 HW3",
     "규제 아닌 배포 시점이 변수", "길은 HW4가 증명 · VIN에 감독형 옵션 뜨는지가 신호")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.30  |  소프트웨어는 다 됐다, 병목은 법이었다", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-30_TSLA_테슬라FSD한국_한미FTA.png")
img.save(out); print("Saved:", out)
