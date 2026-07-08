from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-07"
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

draw.text((32,24), "IREN, 루빈(VR200) 지연이 호재라는 논리", font=bold(30), fill=ACCENT)
draw.text((32,78), "확인해보니 절반만 맞다", font=bold(24), fill=GRAY)
draw.line([(32,126),(W-32,126)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(22), fill=color)
    draw.line([(230,y+18),(230,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((256, y+18), headline, font=bold(23), fill=WHITE)
    draw.text((256, y+58), d1, font=font(18), fill=color)
    draw.text((256, y+88), d2, font=font(16), fill=GRAY)

by = 144; bh = 150; step = 166
band(by, bh, CYAN, (8,28,34), "HBM4",
     "SK하이닉스 양산 램프업 2Q→3Q, 3개월 지연",
     "루빈(VR200) 2026 출하비중 29%→22% (TrendForce)",
     "블랙웰 비중은 61%→71%로 확대 — 확인된 사실")
band(by+step, bh, AMBER, (40,28,10), "카이버(Kyber)",
     "2027→2028 지연, 원인은 PCB 미드플레인 결함",
     "대상은 루빈 울트라(VR300)— 루빈(VR200)과 다른 세대",
     "HBM4·VR200 지연과 인과관계 아님")
band(by+step*2, bh, BLUE, (10,20,34), "IREN 스위트워터 1",
     "1.4GW, 2026년 4월 가동 — 애초 베라루빈용 설계",
     "차일드리스는 GB300(MS $97억)·블랙웰(NVDA $34억) 확보",
     "스위트워터 실제 배정 GPU는 미공시, 추정 단계")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.07  |  IREN  Iris Energy Ltd.", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-07_IREN_루빈지연팩트체크.png")
img.save(out); print("Saved:", out)
