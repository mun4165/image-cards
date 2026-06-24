from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-24"
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
draw.text((32,22), "시버스 뒤에 Aeva가 있다?", font=bold(37), fill=ACCENT)
draw.text((32,74), "SIVE 전략적 LiDAR 고객 Q4 2026 양산 램프 (6/24)", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

# 테제 박스
ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,30,28))
draw.rectangle([32,ty,38,ty+96], fill=TEAL)
draw.text((60,ty+16), "공시는 고객을 숨겼다", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "정황은 Aeva · 엔비디아 Hyperion을 가리킨다", font=bold(26), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(23), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(22), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, TEAL, (8,30,28), "공시 팩트",
     "Q4 2026 양산 램프", "레이저·광증폭기 생애매출 $53~138M")
band(by+step, bh, CYAN, (8,28,34), "숨은 고객",
     "Aeva 유력 (추정)", "Nvidia DRIVE Hyperion 채택 · 2028 SOP")
band(by+step*2, bh, GREEN, (10,32,24), "포지션",
     "InP 레이저 업스트림", "FMCW LiDAR·물리적 AI의 광원 공급")

# 체크포인트 박스
gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,30,28))
draw.text((52,gy+14), "체크포인트", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "고객=Aeva는 추정 · 매출 본격화는 2028 SOP라 멀다",
          font=bold(22), fill=TEAL)
draw.text((52,gy+74), "Apple·보스턴다이내믹스 아틀라스설은 현재 미검증",
          font=font(15), fill=GRAY)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.24  |  $SIVE  Sivers Semiconductors", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-24_SIVE_Aeva_LiDAR고객추적.png")
img.save(out); print("Saved:", out)
