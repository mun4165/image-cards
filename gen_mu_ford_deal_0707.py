from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-07"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = TEAL

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "마이크론, 포드·GM과 닷새 연속 계약", font=bold(34), fill=ACCENT)
draw.text((32,80), "그런데 주가는 고점 대비 -22%", font=bold(24), fill=GRAY)
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
band(by, bh, BLUE, (10,20,34), "7월 1일",
     "GM과 장기 공급계약(SCA) 체결",
     "자동차용 메모리·스토리지 물량 사전 확보",
     "완성차 향 캐파 분산의 첫 번째 계약")
band(by+step, bh, TEAL, (8,28,26), "7월 6일",
     "포드와도 장기 공급계약(SCA) 체결",
     "버지니아 매나사스 D램 증설분을 자동차 고객에 배정",
     "닷새 사이 완성차 두 곳과 잇단 계약")
band(by+step*2, bh, AMBER, (40,28,10), "현재 (7/6 종가)",
     "984.75달러 — 52주 고점 대비 -22%",
     "6/25 장중 1,255달러 → UBS 목표가는 1,625달러 유지",
     "\"조정은 일시적, 펀더멘털은 견고\" — UBS 코멘트")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.07  |  MU  Micron Technology", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-07_마이크론_포드계약.png")
img.save(out); print("Saved:", out)
