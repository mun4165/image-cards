from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-15"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(239,68,68)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "AEHR  어닝콜이 광학 섹터에 주는 신호", font=bold(22), fill=GRAY)
draw.text((32,58), "번인 테스트 백로그 = 광인터커넥트 양산 전환의 후공정 증거", font=bold(28), fill=ACCENT)
draw.line([(32,110),(W-32,110)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(20), fill=color)
    draw.line([(280,y+16),(280,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((306, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((306, y+56), d1, font=font(16), fill=color)
    draw.text((306, y+84), d2, font=font(15), fill=GRAY)

by = 130; bh = 168; step = 186
band(by, bh, GREEN, (10,32,22), "가이던스 신호",
     "FY27 매출 $130~150M 중 포토닉스 15~20%",
     "4분기 매출의 80%가 AI+실리콘포토닉스 (전년 56%)",
     "분기 수주 $60.7M 사상 최대, 유효 백로그 $100.6M")
band(by+step, bh, CYAN, (10,28,32), "메커니즘",
     "번인 테스트 장비는 양산 직전에 사는 물건",
     "샘플·검증 단계에서는 이 규모의 장비 주문이 나오지 않음",
     "백로그 = 하이퍼스케일러 광인터커넥트의 양산 전환 증거")
band(by+step*2, bh, ORANGE, (40,26,10), "교차 확인",
     "업스트림 소재와 후공정 장비가 같은 방향",
     "레이저·기판·웨이퍼에서 보던 광학 수요 신호를",
     "전혀 다른 위치의 테스트 장비 주문서가 다시 확인해주는 그림")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.15  |  AEHR  Q4 FY2026 Earnings Call", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-15_AEHR_광학수요교차확인.png")
img.save(out); print("Saved:", out)
