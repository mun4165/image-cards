from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-11"
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

draw.text((32,24), "META 내부 메모 유출", font=bold(29), fill=ACCENT)
draw.text((32,80), "\"잉여 컴퓨트 판다\"더니 정반대였다", font=bold(24), fill=GRAY)
draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
    draw.line([(250,y+18),(250,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((278, y+22), headline, font=bold(24), fill=WHITE)
    draw.text((278, y+64), d1, font=font(18), fill=color)
    draw.text((278, y+96), d2, font=font(17), fill=GRAY)

by = 150; bh = 152; step = 170
band(by, bh, ORANGE, (40,24,10), "7월1일",
     "메타컴퓨트 신설 보도, 메타 주가 9%대 급등",
     "코어위브 -13.9%, 네비우스 -17.0% 동반 급락",
     "시장은 뉴클라우드 테마 전체 매도로 반응")
band(by+step, bh, GREEN, (10,28,20), "7월9일",
     "내부 메모 유출 — 2027년 캐파 2배 14GW 확대",
     "2026 capex 가이던스 상단 1,450억달러까지 가능",
     "삼성전자·샌디스크·스미토모전기 공급계약 공개")
band(by+step*2, bh, BLUE, (10,20,34), "시사점",
     "\"잉여\"가 아니라 수요가 증설 속도를 앞지른다는 신호",
     "자체 칩 아이리스, 9월 TSMC 양산 돌입",
     "메모리·광섬유 수요 전이 시차는 통상 6~12개월")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.11  |  META  Meta Platforms", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-11_META_내부메모유출.png")
img.save(out); print("Saved:", out)
