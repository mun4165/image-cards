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

draw.text((32,24), "SKHY 상장 첫날 +13% 마감", font=bold(29), fill=ACCENT)
draw.text((32,80), "그런데 국내 본주는 왜 빠졌나", font=bold(24), fill=GRAY)
draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
    draw.line([(250,y+18),(250,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((278, y+22), headline, font=bold(25), fill=WHITE)
    draw.text((278, y+64), d1, font=font(19), fill=color)
    draw.text((278, y+96), d2, font=font(17), fill=GRAY)

by = 150; bh = 152; step = 170
band(by, bh, GREEN, (10,28,20), "나스닥",
     "SKHYV 168달러 안팎 마감, 공모가 대비 약 13%↑",
     "장중 177달러 터치, 거래량 약 1억700만주",
     "시가총액 약 1조2,000억달러로 마이크론 추월")
band(by+step, bh, RED, (40,15,15), "국내 본주",
     "코스피 000660, 장중 +5%대에서 -0.27% 마감",
     "외국인 1조7,181억원 순매도, 이날 코스피 순매도 1위",
     "코스피 지수는 3%대 급등, 본주만 상승분 반납")
band(by+step*2, bh, BLUE, (10,20,34), "13일",
     "정식 티커 SKHY 전환, 일정 변경 없음",
     "최태원 회장 CNBC \"5년내 생산 2배 늘려도 수요는 5~6배\"",
     "HBM 수요 사이클이 여전히 초입이라는 메시지")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.11  |  SKHY  SK Hynix", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-11_SKHY_상장첫날결과.png")
img.save(out); print("Saved:", out)
