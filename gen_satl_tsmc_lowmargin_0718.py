from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-18"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "SATL 저마진 전략, TSMC처럼 통할까", font=bold(30), fill=ACCENT)
draw.text((32,78), "두 조건을 대입해서 검증했다", font=bold(22), fill=GRAY)
draw.line([(32,124),(W-32,124)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(22), fill=color)
    draw.line([(240,y+18),(240,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((268, y+20), headline, font=bold(23), fill=WHITE)
    draw.text((268, y+58), d1, font=font(18), fill=color)
    draw.text((268, y+88), d2, font=font(16), fill=GRAY)

by = 142; bh = 160; step = 178
band(by, bh, RED, (36,14,14), "가격",
     "사흘 -8.12%→-9.85%→+7.00%, 3.82달러(7/17)",
     "52주 고점 12.00달러(5/26) 대비 -68%",
     "이 사흘간 회사발 뉴스는 없었다")
band(by+step, bh, BLUE, (10,20,34), "조건①",
     "복제 불가능한 원가우위 — 미충족",
     "TSMC: 수십조 원 진입장벽, 아무도 못 따라옴",
     "SATL: 셀링포인트가 '저비용' — 낮은 장벽은 난입을 부른다")
band(by+step*2, bh, CYAN, (8,28,34), "조건②",
     "고객 락인 — 미충족",
     "TSMC: 공정 전용 설계자산에 수십억 달러 묶임",
     "SATL: SynMax·SpaceKnow의 배타적 의존 증거 없음")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.18  |  SATL  Satellogic", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-18_SATL_저마진전략TSMC.png")
img.save(out); print("Saved:", out)
