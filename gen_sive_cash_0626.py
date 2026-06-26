from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-26"
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

draw.text((32,22), "SIVE 어제 -21% 폭락", font=bold(36), fill=ACCENT)
draw.text((32,74), "원인은 회계가 아니라 현금이 마르는 속도다", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

# 핵심 메시지 박스
ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "이 종목의 체온계는 매출이 아니다", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "흑자 전까지 버틸 현금 활주로가 진짜 리스크", font=bold(26), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, AMBER, (40,22,10), "① 회계 재작성  덜 무섭다",
     "매출은 안 깎였다 (오히려 소폭 상향)", "손실 확대 대부분 비현금 · 분식보다 보수화")
band(by+step, bh, RED, (40,16,16), "② 진짜 위험  현금",
     "분기 현금소진이 보유 현금의 약 2배", "현금 2,660만 vs 분기 소진 -4,920만 SEK")
band(by+step*2, bh, GREEN, (10,32,24), "③ 사업  안 깨졌다",
     "GlobalFoundries CPO 협업 · 매출 성장 지속", "문제는 제품이 아니라 버틸 현금과 희석")

gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "한 줄 요약", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "부도 위기는 아니다 · 단 낙폭과대=매수로 줍기엔 이르다",
          font=bold(22), fill=CYAN)
draw.text((52,gy+74), "15% 희석권한은 곧 쓸 권한 · 주가 낮을수록 희석은 더 아프다",
          font=font(15), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.26  |  SIVE -21% — 회계 재작성·집단소송·현금 활주로", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-26_SIVE_21퍼급락_현금활주로.png")
img.save(out); print("Saved:", out)
