from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-08-02"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

def base_canvas(accent):
    img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    draw.rectangle([0,0,W,4], fill=accent); draw.rectangle([0,0,4,H], fill=accent)
    return img, draw

def band(draw, y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(17), fill=color)
    draw.line([(268,y+14),(268,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((292, y+15), headline, font=bold(18), fill=WHITE)
    draw.text((292, y+45), detail, font=font(14), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

BY, BH, STEP = 122, 98, 110

img, draw = base_canvas(CYAN)
draw.text((32,22), "로켓랩-iQPS 18회 계약, 진짜 핵심은 따로 있다", font=bold(25), fill=CYAN)
draw.text((32,74), "합성개구레이더와 분리장치 락인 구조", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, CYAN, (10,28,32), "계약  |  7/30 3회 추가",
     "누적 18회, 9개월 사이 세번째 다회계약", "2025.10 → 2026.04 → 2026.07")
band(draw, by+step, bh, BLUE, (10,20,40), "기술  |  합성개구레이더(SAR)",
     "작은 안테나 + 이동거리를 계산으로 합성", "구름·야간에도 촬영, 광학위성과 다른 원리")
band(draw, by+step*2, bh, GREEN, (10,30,22), "목표  |  36기 컨스텔레이션",
     "완성시 지구 전지점 평균 10분 관측", "아직 일부만 궤도상, 미완성 단계")
band(draw, by+step*3, bh, ORANGE, (44,20,10), "핵심  |  분리장치 18회 소급확정",
     "매출 비중은 작음, 진짜 의미는 락인", "인터페이스 고정 → 전환비용 상승")
band(draw, by+step*4, bh, AMBER, (40,30,8), "리스크  |  6월 발사중단",
     "iQPS 발사 7기 성공, 8번째 재조정중", "현금흐름보다 고객 이탈 여부 신호")
footer(draw, "2026.08.02  |  RKLB 로켓랩  iQPS 계약과 SAR 원리")
out = os.path.join(OUT_DIR, "2026-08-02_RKLB_iQPS_SAR_계약구조.png")
img.save(out); print("Saved:", out)
