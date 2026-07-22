from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-16"
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

draw.text((32,24), "SATL 위성 19기, 진짜 묻는 건 하락폭이 아니다", font=bold(30), fill=ACCENT)
draw.text((32,78), "52주 고점 12달러 → 3.96달러, 냉정하게 다시 뜯어봤다", font=bold(22), fill=GRAY)
draw.line([(32,124),(W-32,124)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
    draw.line([(240,y+18),(240,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((268, y+20), headline, font=bold(24), fill=WHITE)
    draw.text((268, y+62), d1, font=font(18), fill=color)
    draw.text((268, y+92), d2, font=font(16), fill=GRAY)

by = 142; bh = 160; step = 178
band(by, bh, BLUE, (10,20,34), "가격",
     "52주 고점 12.00달러(5/26) → 3.96달러(7/15), -67%",
     "고점은 작년이 아니라 7주 전 단기 스파이크",
     "1년에 걸친 조정이 아니라 급등 후 되돌림 성격")
band(by+step, bh, AMBER, (40,28,10), "위성 수",
     "궤도 위성 19기(운영 18기) vs 목표 200기·5분 재방문",
     "EO 사업은 재방문 빈도가 곧 서비스 가치",
     "멀린(Merlin) 컨스텔레이션 첫 발사 2026년 10월")
band(by+step*2, bh, CYAN, (8,28,34), "체크포인트",
     "스케일업 성공해도 매출 전환은 별개 변수",
     "해석 레이어(SynMax·SpaceKnow)는 외주 중",
     "12→4달러 되돌림 = 시장이 아직 스케일업 안 믿는다는 신호")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.16  |  SATL  Satellogic", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-16_SATL_위성19기스케일업.png")
img.save(out); print("Saved:", out)
