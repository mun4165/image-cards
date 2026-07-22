from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-09"
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

draw.text((32,24), "IREN RAISE 서밋 데이1 발언 팩트체크", font=bold(30), fill=ACCENT)
draw.text((32,80), "GB300 아니라 HGX B300, 미란티스는 인수였다", font=bold(22), fill=GRAY)
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
band(by, bh, BLUE, (10,20,34), "확인된 사실",
     "RAISE 서밋 참가, 6/29 Exemplar Cloud 인증, 5/5 미란티스 인수 발표",
     "인증은 엔비디아 HGX B300 트레이닝 기준(IREN 공식)",
     "미란티스는 6.25억달러 규모 M&A, k0rdent 플랫폼 흡수 목적")
band(by+step, bh, RED, (40,15,15), "정정 필요",
     "\"GB300 인증\" 아님 — HGX B300과 GB300은 다른 제품",
     "\"미란티스 계약\" 아님 — 신규 고객 아닌 인수 클로징",
     "\"단 3곳만 보유\"도 공식 확인 안 됨(소수 그룹까지만 명시)")
band(by+step*2, bh, CYAN, (8,28,34), "아직 미확인",
     "호라이즌 일정·MSFT/NVDA 코멘트·베라루빈 배정·선지급 조건",
     "8-K·보도자료 어디에도 게시 안 됨(7/9 기준)",
     "다음 확인 지점: FY26 4분기 실적(8월말 예상)")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.09  |  IREN  Iris Energy", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-09_IREN_RAISE서밋팩트체크.png")
img.save(out); print("Saved:", out)
