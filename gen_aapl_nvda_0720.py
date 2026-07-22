from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-20"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = BLUE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,22), "애플, 시총은 앞섰는데 시리는 구글 것", font=bold(34), fill=ACCENT)
draw.text((32,76), "이익 우선 전략의 승리인가, AI 외주로 수습 중인가", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(196,y+14),(196,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((220, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((220, y+46), detail, font=font(15), fill=color)

by = 136; bh = 130; step = 144
band(by, bh, GREEN, (10,30,22), "시총",
     "7/17 장중 애플, 엔비디아 시총 재역전", "연초 대비 애플 +23% vs 엔비디아 +9%")
band(by+step, bh, RED, (40,14,14), "시리 실체",
     "구글과 연 10억 달러 계약, 제미나이로 구동", "1.2조 파라미터, 애플 자체 모델의 8배")
band(by+step*2, bh, AMBER, (40,28,10), "핵심",
     "오픈AI·앤트로픽까지 검토 후 구글 최종 선택", "AI 외주로 수습, 이익우선 전략의 증거는 아님")
band(by+step*3, bh, CYAN, (8,28,34), "관전포인트",
     "제미나이 시리 실사용 반응 + 다음 분기 capex 가이던스", "두 조건에 이번 프리미엄의 지속성이 달림")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.20  |  AAPL vs NVDA", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-20_애플_엔비디아_시총역전.png")
img.save(out); print("Saved:", out)
