from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-23"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = TEAL

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "외국인이 미국 우주산업을 뚫는다는 것", font=bold(37), fill=ACCENT)
draw.text((32,74), "ITAR·FOCI라는 벽을 넘어가는 로켓랩과 세틀로직", font=bold(21), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, sub, players, role, fact):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+24), label, font=bold(27), fill=color)
    draw.text((60, y+64), sub, font=font(17), fill=GRAY)
    draw.line([(440,y+18),(440,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((468, y+16), players, font=bold(23), fill=WHITE)
    draw.text((468, y+50), role, font=font(18), fill=GRAY)
    draw.text((468, y+78), fact, font=bold(18), fill=color)

# 벽 — 외국계를 막는 두 관문
band(138, 112, RED, (34,16,16),
     "두 개의 관문", "외국계를 거르는 보이지 않는 벽",
     "ITAR (국제무기거래규정)",
     "로켓·위성 기술의 수출과 접근을 통제",
     "FOCI (외국인 소유·통제·영향력) 규제")

# 로켓랩 — 끈기
band(258, 112, BLUE, (12,22,40),
     "로켓랩 · 끈기", "뉴질랜드의 독학 엔지니어 피터 벡",
     "코슬라 · 베서머 · 록히드마틴 투자 유치",
     "2013 미국 법인 전환 · 2020 롱비치 본사",
     "기술력으로 미국 우주산업 한복판에 진입")

# 세틀로직 — 돌파
band(378, 112, GREEN, (10,32,24),
     "세틀로직 · 돌파", "아르헨티나 출신 카르기에만, NASA 인맥 없이",
     "우루과이 본사 → 델라웨어 재법인(2025)",
     "수출통제 밖이라는 이점을 스스로 내려놓음",
     "ITAR 진입 · FOCI 돌파 · 해양대기청 라이선스")

# 하단 핵심 박스
by = 512
draw.rounded_rectangle([32,by,W-32,by+90], radius=10, fill=(8,28,26))
draw.text((52,by+14), "남들이 못 파는 니치(틈새)를 파고드는 두 회사", font=bold(20), fill=BLUE)
draw.text((52,by+50), "시장에 도달하기까지 시간이 걸려도, 그 여정 자체가 증명이다", font=bold(20), fill=GREEN)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.23  |  RKLB · SATL", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-23_로켓랩_세틀로직_ITAR_FOCI.png")
img.save(out); print("Saved:", out)
