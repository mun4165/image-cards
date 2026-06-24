from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-24"
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
draw.text((32,22), "데이터 사가던 고객을, 파트너로 끌어올렸다", font=bold(37), fill=ACCENT)
draw.text((32,74), "Satellogic × SynMax 전략적 협업 (6/23)", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

# 테제 박스
ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "벤더에서 플랫폼으로", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "SynMax가 세틀로직 인프라 위에 올라탄 첫 외부 사례", font=bold(26), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(23), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(22), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, CYAN, (8,28,34), "관계 변화",
     "고객 → 공동 파트너", "데이터 구매에서 inaugural partner로 격상")
band(by+step, bh, GREEN, (10,32,24), "같은 날 신호",
     "노스랜드 컨퍼런스도 동일 메시지", "일회성 이미지 → persistent monitoring 전환")
band(by+step*2, bh, BLUE, (10,20,38), "멀린(Merlin)",
     "2026.10 첫 발사 · 1m 일일 전지구", "지속 감시 구독 모델의 공급 전제조건")

# 체크포인트 박스
gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,24,30))
draw.text((52,gy+14), "체크포인트", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "원래 Planet($PL) 고객 — 세틀로직을 끊는 게 아니라 주력으로 추가하는 그림",
          font=bold(22), fill=CYAN)
draw.text((52,gy+74), "금액·독점 미공시 · 전환이 구독 매출로 찍히는지가 진짜 검증",
          font=font(15), fill=GRAY)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.24  |  $SATL  Satellogic", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-24_SATL_SynMax파트너격상.png")
img.save(out); print("Saved:", out)
