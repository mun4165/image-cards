from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-02"
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

draw.text((32,22), "NBIS -17%, 메타 컴퓨트 발표에 무너졌다", font=bold(38), fill=ACCENT)
draw.text((32,80), "코어위브보다 더 빠진 이유 · IREN이 짚은 2030년", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

# 핵심 밴드 — 7/1 낙폭 비교
ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "7/1 종가", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "NBIS $229.18 (-17.01%)   ·   CRWV $85.69 (-13.92%)",
          font=bold(20), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, ORANGE, (40,24,10), "①  메타 컴퓨트",
     "메타, 남는 AI 컴퓨트를 외부 판매 준비", "raw GPU + 호스팅 모델(Muse Spark) · Bloomberg 보도")
band(by+step, bh, BLUE, (12,20,38), "②  IREN 2030년",
     "1GW AI 팩토리, 오늘 시작해도 첫 가동 2030년", "부지·전력·GPU 병목 — 컴퓨트는 남는 물건이 아니다")
band(by+step*2, bh, GREEN, (10,32,24), "③  낙폭의 역설",
     "풀스택 NBIS가 raw 캐파 CRWV보다 더 빠짐", "펀더 아닌 뉴클라우드 바스켓 매도 정황")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.02  |  종가 stockanalysis.com  |  메타 클라우드 사업은 보도 단계, 확정 아님", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-02_NBIS_메타컴퓨트_IREN2030.png")
img.save(out); print("Saved:", out)
