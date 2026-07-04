from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-04"
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

draw.text((32,22), "RKLB 계약 트래커, 원문과 대조하니", font=bold(36), fill=ACCENT)
draw.text((32,76), "이름값 큰 계약일수록 로켓랩 몫을 확인해야 한다", font=bold(21), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(196,y+14),(196,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((220, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((220, y+46), detail, font=font(15), fill=color)

by = 136; bh = 92; step = 100
band(by, bh, RED, (40,14,14), "반전",
     "우주 요격체(SBI) 계약 — 주인공 아니다", "프라임=레이시온, 로켓랩은 서브 / 시연은 2028년")
band(by+step, bh, GREEN, (10,30,20), "저평가",
     "정지궤도 위성 계약 9,000만 달러", "로켓랩이 설계·제작·발사·운영 전부 맡는 프라임 계약")
band(by+step*2, bh, CYAN, (8,28,34), "숫자",
     "백로그 18.5억 달러 → 22억 달러+", "익명 고객 1곳의 뉴트론5·일렉트론3 계약이 핵심 동력")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.04  |  출처: 각사 보도자료·1분기 실적발표 원문 대조", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-04_RKLB_계약트래커_팩트체크.png")
img.save(out); print("Saved:", out)
