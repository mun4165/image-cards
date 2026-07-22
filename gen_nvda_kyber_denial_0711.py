from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-11"
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

draw.text((32,24), "NVDA 카이버 지연설 부인", font=bold(29), fill=ACCENT)
draw.text((32,80), "부인한 건 절반뿐이다", font=bold(24), fill=GRAY)
draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
    draw.line([(250,y+18),(250,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((278, y+22), headline, font=bold(23), fill=WHITE)
    draw.text((278, y+64), d1, font=font(18), fill=color)
    draw.text((278, y+96), d2, font=font(17), fill=GRAY)

by = 150; bh = 152; step = 170
band(by, bh, RED, (40,15,15), "7월6일",
     "세미애널리시스, 카이버 랙 2027→2028 지연 보도",
     "78층 PCB 미드플레인 수율 문제가 원인",
     "대상은 루빈 울트라(VR300)용 랙, 루빈(VR200) 아님")
band(by+step, bh, GREEN, (10,28,20), "엔비디아 반응",
     "\"로드맵은 그대로다\" 한 줄 성명으로 즉시 부인",
     "부인 당일 주가 1%대 상승",
     "세부 반박·수치 없이 결론 한 문장뿐")
band(by+step*2, bh, BLUE, (10,20,34), "부인이 안 덮은 것",
     "PCB 수율 문제 자체는 별도 반박 안 함",
     "하이퍼스케일러 거부로 백업 랙 설계 이미 취소",
     "\"2건 부인\"이 아니라 보고서 1건에 대한 대응")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.11  |  NVDA  NVIDIA", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-11_NVDA_카이버지연부인.png")
img.save(out); print("Saved:", out)
