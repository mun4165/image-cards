from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-16"
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

draw.text((32,24), "RKLB  발사 직전 멈춘 QPS-SAR-13", font=bold(22), fill=GRAY)
draw.text((32,58), "고객 iQPS 결산은 반대 방향을 가리키고 있었다", font=bold(28), fill=ACCENT)
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
band(by, bh, GREEN, (10,32,22), "확인된 사실",
     "일렉트론 15회 계약 · 7회 완료 전부 성공",
     "QPS-SAR-13(MIKURA-I) = 8번째 임무",
     "7/1 카운트다운 막판 자동 중단 · 재발사일 미정")
band(by+step, bh, CYAN, (10,28,32), "iQPS 결산",
     "FY2027 매출 100억엔 · 영업흑자 전환 가이던스",
     "1년 안에 위성 7기 추가 발사 → 기말 16기 운용",
     "생산능력 연 20기 · 최종 12궤도 36기 콘스텔레이션")
band(by+step*2, bh, ORANGE, (40,26,10), "해석",
     "발사 횟수보다 반복 고객의 증가 속도",
     "BlackSky · Synspective · iQPS = 반복 발사 프로그램",
     "재발사일 발표 = 후속 일정 공개의 트리거")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.16  |  RKLB × iQPS  Electron Recurring Launch", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-16_RKLB_iQPS반복발사.png")
img.save(out); print("Saved:", out)
