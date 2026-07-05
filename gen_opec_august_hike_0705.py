from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-05"
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

draw.text((32,22), "OPEC+ 8월 증산", font=bold(36), fill=ACCENT)
draw.text((32,76), "18.8만배럴, 이번엔 서류상이 아니다", font=bold(21), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(196,y+14),(196,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((220, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((220, y+46), detail, font=font(15), fill=color)

by = 136; bh = 92; step = 100
band(by, bh, CYAN, (8,28,34), "증산규모",
     "8월 하루 18.8만배럴, 6·7월과 동일폭", "7개국: 사우디·러시아·이라크·쿠웨이트 등")
band(by+step, bh, GREEN, (10,30,20), "진짜변화",
     "호르무즈 정상화, 유가 72달러대 복귀", "봄엔 서류상 증산, 지금은 실물공급 가능성")
band(by+step*2, bh, AMBER, (40,28,10), "남은변수",
     "감산분 37.9만배럴 남음, 9월말 완전해제 전망", "이라크는 별도로 쿼터 상향 요구 중")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.05  |  OPEC+", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-05_OPEC_8월증산.png")
img.save(out); print("Saved:", out)
