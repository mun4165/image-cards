from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-25"
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

# 헤더
draw.text((32,22), "비나텍, Bloom Energy가 택한 슈퍼커패시터", font=bold(37), fill=ACCENT)
draw.text((32,74), "영업이익 489% 추정 — 스토리는 진짜, 숫자는 아직", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

# 테제 박스
ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "AI 데이터센터가 부른 종목", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "연료전지와 GPU 사이 전력 공백을 메우는 순간 전원", font=bold(25), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(22), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(21), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, GREEN, (10,32,24), "확정  공시 계약",
     "Bloom Energy 슈퍼캡 3년 180억", "연 60억 수준 — 이게 계약서의 숫자다")
band(by+step, bh, AMBER, (40,22,10), "추정  시장 전망",
     "2026 매출 1,710억 · 영업익 +489%", "슈퍼캡 1,000억은 가정치, 확정 아님")
band(by+step*2, bh, RED, (40,16,16), "현실  현재 실적",
     "1Q 연결 영업적자 -15억", "PBR 5.5 · 추정PER 76 — 흑자 선반영")

# 결론 박스
gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "어떻게 보느냐", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "독점 수혜주 한 줄로 들면 위험  →  분기 실적으로 검증하는 종목",
          font=bold(22), fill=CYAN)
draw.text((52,gy+74), "분수령: 8/19 2분기 실적 — Bloom 매출 인식 · 연결 흑자 전환 여부",
          font=font(15), fill=GRAY)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.25  |  126340  비나텍 VINATech", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-25_비나텍_블룸에너지슈퍼캡_확정vs추정.png")
img.save(out); print("Saved:", out)
