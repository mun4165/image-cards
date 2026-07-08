from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-07"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = BLUE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "브로드컴, 애플과 계약 2031년까지 연장", font=bold(32), fill=ACCENT)
draw.text((32,80), "그런데 왜 여태 4%만 올랐나", font=bold(24), fill=GRAY)
draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
    draw.line([(240,y+18),(240,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((268, y+20), headline, font=bold(25), fill=WHITE)
    draw.text((268, y+62), d1, font=font(19), fill=color)
    draw.text((268, y+92), d2, font=font(17), fill=GRAY)

by = 146; bh = 148; step = 164
band(by, bh, BLUE, (10,20,34), "7월 6일",
     "애플向 커스텀 ASIC 공급계약 2031년까지 연장",
     "애플 연매출 20% 비중 — 브로드컴 최대 고객사",
     "발표 당일 주가 +4%")
band(by+step, bh, AMBER, (40,28,10), "2026년 YTD",
     "이번 소식 전까지 상승률 +4.15%",
     "다른 AI 반도체주 대비 옆으로 긴 한 해",
     "일각에서 AMD·인텔 대안론까지 제기")
band(by+step*2, bh, CYAN, (8,28,34), "목표주가 갭",
     "41명 애널리스트 평균 목표가 523.73달러",
     "현재가 373.60달러 대비 +28.6% 여지",
     "다음 체크: 애플向 매출 가이던스 구체화 여부")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.07  |  AVGO  Broadcom Inc.", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-07_브로드컴_애플계약연장.png")
img.save(out); print("Saved:", out)
