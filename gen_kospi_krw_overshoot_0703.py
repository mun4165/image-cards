from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-03"
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

draw.text((32,22), "원달러 1,550원, 이미 와있다", font=bold(38), fill=ACCENT)
draw.text((32,80), "코스피는 아직 안 붙었다 · 이중손실 공포 vs 오버슈팅 매수 신호", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

# 핵심 밴드 — 현재 레벨
ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "7/1 원달러", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "1,552~1,559원 (금융위기 이후 최고)   ·   코스피 7,648 (6/8 저점 7,484 대비 반등)",
          font=bold(19), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, ORANGE, (40,24,10), "①  외국인 매도",
     "19거래일 연속 순매도, 리밸런싱 vs 모멘텀", "현대차증권: 시총 대비론 2020~22보다 작다")
band(by+step, bh, RED, (38,14,14), "②  이중손실 시나리오",
     "환율+주가 동반 하락하면 매도 가속", "환헤지 없는 외국인일수록 이탈 속도 빨라짐")
band(by+step*2, bh, GREEN, (10,32,24), "③  메모리는 내러티브 쇼크",
     "구글, 컴퓨트 부족으로 메타 제미나이 제한(6/28 FT)", "체크포인트: 7/7 삼성전자 잠정실적 · 7월말 빅테크 capex")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.03  |  환율 investing.com · 코스피 KRX 기준", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-03_코스피_원달러오버슈팅.png")
img.save(out); print("Saved:", out)
