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

draw.text((32,24), "SKHY를 사도 하이닉스 주주가 아니다?", font=bold(28), fill=ACCENT)
draw.text((32,80), "ADR과 이중상장 차이", font=bold(24), fill=GRAY)
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
band(by, bh, CYAN, (8,28,34), "ADR",
     "원주 담보로 미국 예탁은행이 발행한 증서",
     "원주는 한국 커스터디 은행에 그대로 보관",
     "SKHY 예탁비율 1대10, ADR 10주 = 원주 1주")
band(by+step, bh, ORANGE, (40,24,10), "이중상장",
     "같은 보통주가 두 거래소에 각각 직접 상장",
     "은행 증서 없이 원주 자체가 양쪽에서 유통",
     "ADR과는 법적 성격이 완전히 다른 구조")
band(by+step*2, bh, GREEN, (10,28,20), "가격 수렴",
     "원주-ADR 전환 창구 상시 개방",
     "괴리 발생 시 차익거래로 다시 수렴",
     "배당·의결권은 예탁은행 통해 패스스루 전달")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.11  |  SKHY  SK Hynix ADR", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-11_SKHY_ADR과이중상장차이.png")
img.save(out); print("Saved:", out)
