from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-22"
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

draw.text((32,22), "메모리 3사, CXL 컨트롤러 자체개발 접었다", font=bold(26), fill=ACCENT)
draw.text((32,70), "용량 확장은 CXL로, 그런데 왜 핵심 부품 개발에서는 손을 뗐나", font=bold(20), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((58, y+h//2-14), label, font=bold(20), fill=color)
    draw.line([(232,y+16),(232,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((258, y+16), headline, font=bold(19), fill=WHITE)
    draw.text((258, y+52), d1, font=font(16), fill=color)
    draw.text((258, y+80), d2, font=font(14), fill=GRAY)

by = 132; bh = 152; step = 168
band(by, bh, CYAN, (8,28,34), "SK하이닉스",
     "자체 컨트롤러 개발 공식 중단",
     "CXL 3.2 기반 256GB 등 D램 모듈은 계속 확대, 컨트롤러 인력은 PIM으로 재배치",
     "제조(D램 칩)는 유지, 설계(컨트롤러)만 팹리스에 이관")
band(by+step, bh, BLUE, (10,20,34), "삼성전자",
     "외부 판매용 자체개발 중단, 내부 연구용만 유지",
     "1TB CXL 메모리 풀을 블랙웰 GPU와 시연(GPU 8개서 D램 대비 92% 성능)",
     "외부 판매는 팹리스 컨트롤러 구매로 전환")
band(by+step*2, bh, AMBER, (36,26,8), "마이크론",
     "자체 개발 포기, 외부 솔루션 채택",
     "팹리스 프라임마스 컨트롤러로 전환, CZ120/CZ122 D램 모듈만 직접 공급",
     "이유는 공통: 저가 범용 D램(DIMM)이 자사 CXL 사업을 잠식하는 구조")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.22  |  CXL  메모리 3사 컨트롤러 개발 축소  |  CXL 시장 2026년 21억달러 → 2028년 160억달러 전망", font=font(14), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-22_CXL_메모리3사_컨트롤러철수.png")
img.save(out); print("Saved:", out)
