from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-06"
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

draw.text((32,24), "IREN, 앤트로픽 데이터센터 조각을 가져갈 수 있을까", font=bold(36), fill=ACCENT)
draw.text((32,80), "11개 조건 체크리스트 대조", font=bold(24), fill=GRAY)
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
band(by, bh, GREEN, (10,32,22), "체크리스트 부합",
     "재무·부지·전력·해저케이블 — 8개 조건 매치",
     "92억 달러 구조화 자금조달 · 800MW 번디 캠퍼스",
     "싱가포르·한국·일본행 APAC 해저광케이블 — 메트로 사이트엔 없는 것")
band(by+step, bh, AMBER, (40,28,10), "넘어야 할 벽",
     "가동 개시 2028년 · 완공 실적 아직 없음",
     "앤트로픽 비투자등급 — 임대인이 자금조달 리스크 부담",
     "CDC(Infratil 후원)가 500MW 유력 후보로 거론됨")
band(by+step*2, bh, CYAN, (8,28,34), "현실적 결론",
     "노릴 몫은 500MW 아닌 100~200MW 조각",
     "216억 달러는 원본 보도 미확인 수치 · 계약 미체결",
     "FID(최종투자결정)까지 최소 6주 남음")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.06  |  IREN  Iris Energy", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-06_IREN_앤트로픽체크리스트.png")
img.save(out); print("Saved:", out)
