from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-24"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = AMBER

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "엑스팹, 유럽 칩법에서 1.28억 유로 받았다", font=bold(37), fill=ACCENT)
draw.text((32,74), "Fab4Micro · 에르푸르트 MEMS 오픈 파운드리 (6/24)", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

# 테제 박스
ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(36,22,8))
draw.rectangle([32,ty,38,ty+96], fill=AMBER)
draw.text((60,ty+16), "보조금이 핵심이 아니다", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "유럽이 MEMS 위탁생산을 안으로 끌어온다는 신호", font=bold(26), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(23), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(22), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, AMBER, (40,22,10), "무슨 일",
     "1.28억 유로 CHIPS Act 보조", "독일 팹 총 6.23억 유로 승인 중 X-FAB 몫")
band(by+step, bh, GREEN, (10,32,24), "무엇에",
     "MEMS 오픈 파운드리", "팹리스·스타트업 위탁생산을 EU 내재화")
band(by+step*2, bh, BLUE, (10,20,38), "큰 그림",
     "EU 칩법 2.0 순풍", "유럽 스페셜티 파운드리에 구조적 수혜")

# 체크포인트 박스
gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(36,22,8))
draw.text((52,gy+14), "체크포인트", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "상업가동 2029 — 보조금은 capex지 즉시 매출이 아님",
          font=bold(22), fill=AMBER)
draw.text((52,gy+74), "단기 드라이버는 여전히 SiC 파워·자동차 회복 사이클",
          font=font(15), fill=GRAY)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.24  |  $XFAB  X-FAB Silicon Foundries", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-24_XFAB_칩스법_MEMS오픈파운드리.png")
img.save(out); print("Saved:", out)
