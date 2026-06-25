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

draw.text((32,22), "RKLB, NASA가 또 골랐다", font=bold(36), fill=ACCENT)
draw.text((32,74), "전용 Electron 발사 3건을 한 번에 — 고른 이유는 가격이 아니다", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

# 핵심 메시지 박스
ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "NASA가 같은 회사를 반복해서 고르는 구조", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "싸서가 아니라 정확하고 신뢰돼서 고른다", font=bold(26), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "① 정확도  PolSIR",
     "미터 수준 궤도 정확도로 선정", "합승 발사로는 못 가는 자리 · 전용 발사가 차지")
band(by+step, bh, BLUE, (12,20,38), "② 신뢰  Electron",
     "90회+ 성공 발사로 쌓은 실적", "TSIS-2는 발사 7개월 전 예약 · 빠른 대응 발사")
band(by+step*2, bh, GREEN, (10,32,24), "③ 누적  NASA 관계",
     "Aspera · LOXSAT 임무도 줄 서 있다", "한 계약이 아니라 2027년 일정까지 겹겹이")

gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "한 줄 요약", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "맡은 일을 매번 해내서 다음 일을 또 받는 회사",
          font=bold(22), fill=CYAN)
draw.text((52,gy+74), "실패가 곧 끝인 우주에서 신뢰의 누적은 그 자체가 해자다",
          font=font(15), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.26  |  RKLB — NASA 전용 Electron 발사 3건 수주(TSIS-2 · PolSIR)", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-26_RKLB_NASA_3개임무.png")
img.save(out); print("Saved:", out)
