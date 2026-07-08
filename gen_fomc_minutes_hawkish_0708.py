from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-08"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = AMBER

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "6월 FOMC 의사록, 오늘 밤 공개", font=bold(32), fill=ACCENT)
draw.text((32,80), "점도표 9명이 인상 쪽으로 돌아선 이유", font=bold(24), fill=GRAY)
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
band(by, bh, BLUE, (10,20,34), "6/17",
     "기준금리 3.50~3.75% 만장일치 동결",
     "점도표 중간값: 3월 인하 전망 → 6월 인상 전망으로 반전",
     "18명 중 9명 연내 인상, 6명은 25bp 두 차례")
band(by+step, bh, AMBER, (40,28,10), "성명서",
     "341단어(4/29) → 130단어로 축소",
     "완화 시사 문구 삭제",
     "케빈 워시 첫 회의 — 본인 점 미제출, SEP 개편 태스크포스 예고")
band(by+step*2, bh, CYAN, (8,28,34), "7/9 새벽 3시",
     "의사록 공개 (한국시간)",
     "관전: 인상 9명 논거가 경계인지 임박인지",
     "완화 문구 삭제가 합의였는지 이견이 있었는지")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.08  |  FOMC  연방준비제도", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-08_FOMC의사록_점도표.png")
img.save(out); print("Saved:", out)
