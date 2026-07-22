from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-12"
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

draw.text((32,24), "LPTH \"이리디움처럼 인수될까\"", font=bold(28), fill=ACCENT)
draw.text((32,80), "확인해보니 병목은 다른 곳에 있었다", font=bold(24), fill=GRAY)
draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
    draw.line([(250,y+18),(250,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((278, y+22), headline, font=bold(22), fill=WHITE)
    draw.text((278, y+64), d1, font=font(18), fill=color)
    draw.text((278, y+96), d2, font=font(17), fill=GRAY)

by = 150; bh = 152; step = 170
band(by, bh, ORANGE, (40,24,10), "대입 가설",
     "로켓랩-이리디움 인수 논리를 LPTH에 대입",
     "이리디움 인수 근거 = 전세계 유일 L밴드 주파수(재산권)",
     "라이트패스 칼코게나이드 유리도 같은 논리 적용될까")
band(by+step, bh, GREEN, (10,28,20), "확인 1",
     "소재 자체는 유일하지 않았다",
     "어벤티어·안도버·UQG·중국 웨이브렝스(연 10톤)도 생산",
     "이리디움 스펙트럼과 달리 인수 없이도 접근 가능한 기술")
band(by+step*2, bh, BLUE, (10,20,34), "확인 2",
     "국방에 쓸 자격은 소수만 갖고 있었다",
     "라이트패스=ITAR+MIL-spec+DLA 자금, 중국산은 배제",
     "병목은 실재하나 결론은 인수보다 독립 리레이팅")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.12  |  LPTH  LightPath Technologies", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-12_LPTH_이리디움인수논리대입.png")
img.save(out); print("Saved:", out)
