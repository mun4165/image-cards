from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-06"
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

draw.text((32,24), "AAOI 내부자매도, 고점에서 던졌다", font=bold(36), fill=ACCENT)
draw.text((32,80), "CEO·이사·임원 2명 Form 4 전량 대조", font=bold(24), fill=GRAY)
draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
    draw.line([(240,y+18),(240,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((268, y+20), headline, font=bold(25), fill=WHITE)
    draw.text((268, y+62), d1, font=font(19), fill=color)
    draw.text((268, y+92), d2, font=font(17), fill=GRAY)

by = 140; bh = 165; step = 182
band(by, bh, RED, (40,16,16), "매도 팩트",
     "5명이 5/19~6/18 총 20만4,904주 매도",
     "CEO 5.8만주 · 이사 5.66만주 · 임원 2명 8.6만주",
     "매도가 $166.53~$205.39, 현재가 $120.95보다 27~41% 위")
band(by+step, bh, AMBER, (40,28,10), "완화 요인",
     "대부분 Rule 10b5-1 사전계획 매도",
     "CEO·임원 2명은 매도 후에도 수십만~수백만주 잔여",
     "계획 자체는 3~6월 사전 채택, 정보이용 시비 아님")
band(by+step*2, bh, CYAN, (8,28,34), "진짜 경계 지점",
     "이사 DeLaney, 본인 보유의 48% 매도",
     "5.66만주 팔고 6.2만주만 남음 — 비중 최대 매도",
     "매도 클러스터가 7/2 섹터 리셋보다 몇 주 앞섰다")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.06  |  AAOI  Applied Optoelectronics", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-06_AAOI_내부자매도_Form4대조.png")
img.save(out); print("Saved:", out)
