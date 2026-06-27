from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-27"
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

draw.text((32,22), "세레브라스(CBRS), 아마존과 손잡았는데 왜 못 사나", font=bold(34), fill=ACCENT)
draw.text((32,72), "인퍼런티아·마벨 레이어맵이 숨긴 두 가지", font=bold(20), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)

# 핵심 메시지 박스
ty = 128
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+14), "직관은 도착지만 맞았다", font=bold(18), fill=GRAY)
draw.text((60,ty+44), "아마존이 추론칩을 가진 건 궁합이 아니라 경쟁", font=bold(25), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+15), label, font=bold(20), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+16), headline, font=bold(19), fill=WHITE)
    draw.text((588, y+50), detail, font=font(15), fill=color)

by = 238; bh = 80; step = 88
band(by, bh, AMBER, (40,22,10), "① 첫 번째 착각",
     "인퍼런티아가 있으니 결이 맞다?", "오히려 같은 추론 자리 두고 겹치는 경쟁자")
band(by+step, bh, GREEN, (10,32,24), "② 마벨 우회",
     "세레브라스는 마벨 사슬 밖이다", "수직통합 = 외부 ASIC도 칩 밖 연결도 거의 안 씀")
band(by+step*2, bh, CYAN, (8,28,34), "③ 진짜 단기변수",
     "8~10월 단계적 락업 매물", "한 분기까지 누적 6천만 주+ 출회 가능")

gy = 514; gh=100
draw.rounded_rectangle([32,gy,W-32,gy+gh], radius=10, fill=(40,16,16))
draw.rectangle([32,gy,38,gy+gh], fill=RED)
draw.text((52,gy+14), "좋은 회사 ≠ 좋은 매수가", font=bold(19), fill=RED)
draw.text((52,gy+46), "지금은 펀더멘털보다 수급이 이기는 구간",
          font=bold(22), fill=WHITE)
draw.text((52,gy+78), "진입 방아쇠 = 락업 다 소화된 뒤에도 FY26 가이던스 유지될 때",
          font=font(15), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.27  |  CBRS 세레브라스 — 레이어맵과 수급으로 읽기", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-27_CBRS_레이어맵_인퍼런티아마벨_락업.png")
img.save(out); print("Saved:", out)
