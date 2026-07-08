from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-07"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = RED

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "삼성전자, 역대 최대 실적인데 -8%", font=bold(34), fill=ACCENT)
draw.text((32,80), "원인은 한 달 전 그 성과급 구조", font=bold(24), fill=GRAY)
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
band(by, bh, WHITE, (24,24,28), "7월 7일",
     "2분기 잠정 매출 171조 · 영업이익 89.4조",
     "전년比 +129.3% · +1,810.3%, 두 지표 모두 역대 최대",
     "그런데 주가는 발표 당일 오히려 급락")
band(by+step, bh, AMBER, (40,28,10), "하락 이유 ①",
     "시장 기대치 90조~100조에는 못 미침",
     "실적은 역대급이나 눈높이가 이미 더 높았다",
     "장중 -8.33%, 최근 5거래일 누적 -12.18%")
band(by+step*2, bh, CYAN, (8,28,34), "하락 이유 ②",
     "DS부문 영업이익 10.5% 특별성과급",
     "6/24 자사주 21조 매입 재원과 같은 구조",
     "이번엔 비용으로 반영 — 다음 체크는 7/30 정식실적")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.07  |  005930  Samsung Electronics", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-07_삼성전자_실적발표급락.png")
img.save(out); print("Saved:", out)
