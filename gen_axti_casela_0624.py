from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-24"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = ORANGE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "AXTI 12.9% 급등, 11일 전 서명된 계약", font=bold(37), fill=ACCENT)
draw.text((32,74), "Tongmei × Nanjing Casela · InP 장기공급계약", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

# 테제 박스
ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(36,22,8))
draw.rectangle([32,ty,38,ty+96], fill=ORANGE)
draw.text((60,ty+16), "금액보다 구조다", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "$25.4M take-or-pay — 2027년 InP 매출을 미리 못 박은 계약", font=bold(26), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(23), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(22), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, AMBER, (40,22,10), "계약 규모",
     "RMB 1.73억 ≈ $25.4M", "AXT 연매출 $88M의 약 26% · 전량 InP")
band(by+step, bh, GREEN, (10,32,24), "계약 구조",
     "최소 80% 의무 + 50% 선불", "미달 시 취소수수료 — 파는 쪽이 갑")
band(by+step*2, bh, CYAN, (8,28,34), "고객 Casela",
     "데이터컴 레이저 회사(CPO·CW)", "다운스트림 수요가 InP 주문으로 실현")

# 타임라인 박스
gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(40,22,10))
draw.text((52,gy+14), "타임라인", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "6.11 서명   →   6.22 공시·주가 +12.9%   →   2027 월별 납품·매출",
          font=bold(22), fill=AMBER)
draw.text((52,gy+74), "단, 중국 국내거래 — 글로벌 고객 InP 계약이 다음 관문",
          font=font(15), fill=GRAY)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.24  |  AXTI  AXT Inc.", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-24_AXTI_카셀라계약_타임라인.png")
img.save(out); print("Saved:", out)
