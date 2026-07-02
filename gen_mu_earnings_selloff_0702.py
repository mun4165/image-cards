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

draw.text((32,22), "MU, 실적 대박에 -10% 무너졌다", font=bold(40), fill=ACCENT)
draw.text((32,80), "숫자는 좋았는데 왜 팔았나 · 세 악재가 겹친 자리", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

# 핵심 밴드 — 실적 vs 주가
ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "7/1 종가", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "$1,032.28   -$122.01  (-10.57%)   ·   FQ3·Q4 가이던스는 컨센 상회",
          font=bold(20), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, RED, (40,16,16), "악재 ①  재료 소멸",
     "올해 이미 +267% · 좋은 실적은 선반영", "실적 확인되자 차익실현 매도(sell the news)")
band(by+step, bh, ORANGE, (40,24,10), "악재 ②  애플 CXMT",
     "애플, 중국산 저가 DRAM 구매 로비 보도", "승인 시 고객 이탈 · 마이크론 가격 협상력 훼손")
band(by+step*2, bh, BLUE, (12,20,38), "악재 ③  SK하이닉스",
     "HBM 1위 경쟁사, 미국 증시 상장 추진 보도", "메모리 베팅 자금이 경쟁사로 분산될 우려")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.02  |  종가 stockanalysis.com  |  ②③은 보도·전망 단계, 확정 사실 아님", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-02_MU_실적대박_10퍼급락_세악재.png")
img.save(out); print("Saved:", out)
