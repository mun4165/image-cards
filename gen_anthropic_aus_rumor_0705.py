from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-05"
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

draw.text((32,22), "앤트로픽 호주 15조 데이터센터", font=bold(34), fill=ACCENT)
draw.text((32,74), "\"주인공이 IREN\" 소문, 팩트체크", font=bold(21), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(196,y+14),(196,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((220, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((220, y+46), detail, font=font(15), fill=color)

by = 134; bh = 92; step = 100
band(by, bh, GREEN, (10,32,22), "확인된 사실",
     "1.4GW · 최대 150억 달러 규모 투자 준비", "기밀 입찰서류 기준, FID 4~6주 내 예정")
band(by+step, bh, AMBER, (40,28,10), "확인 안 된 것",
     "파트너가 IREN·SharonAI라는 근거 없음", "IREN 확인 고객=MSFT, SharonAI 확인 상대=NVIDIA")
band(by+step*2, bh, CYAN, (8,28,34), "구분할 것",
     "이전 MOU(4월)는 금액·용량 언급 자체 없음", "이번 숫자는 별개의 새 보도")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.05  |  Anthropic · IREN", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-05_앤트로픽호주데이터센터_팩트체크.png")
img.save(out); print("Saved:", out)
