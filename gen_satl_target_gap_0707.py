from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-07"
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

draw.text((32,24), "SATL 목표가 10달러 vs 주가 5.18달러", font=bold(32), fill=ACCENT)
draw.text((32,80), "애널리스트와 시장, 누가 틀렸나", font=bold(24), fill=GRAY)
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
band(by, bh, BLUE, (10,20,34), "5월 13일",
     "Cantor Fitzgerald 목표가 7 → 10달러 상향",
     "근거: 1분기 매출 +80%, 사상 첫 영업현금흐름 플러스",
     "밸류에이션 = 2028년 매출 기준 — 멀린 완성 이후의 그림")
band(by+step, bh, AMBER, (40,28,10), "6월~7월",
     "주가 10.74달러 → 5.18달러, 한 달여 만에 -52%",
     "그 사이 뉴스는 방산 계약 등 호재 — 악재 없는 하락",
     "급등(연초 대비 +475%) 이후 밸류에이션 되돌림")
band(by+step*2, bh, CYAN, (8,28,34), "체크포인트",
     "갭 = 멀린 전제에 대한 시장의 의심 크기",
     "10월 멀린 첫 발사 + 2분기 현금흐름이 첫 답",
     "현실: 궤도 위성 19기 — 컨스텔레이션은 아직 도면 위")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.07  |  SATL  Satellogic", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-07_SATL_목표가주가갭.png")
img.save(out); print("Saved:", out)
