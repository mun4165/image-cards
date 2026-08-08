from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-08-08"
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
    draw.line([(360,y+14),(360,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((384, y+15), headline, font=bold(18), fill=WHITE)
    draw.text((384, y+45), detail, font=font(14), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

BY, BH, STEP = 122, 98, 110

img, draw = base_canvas(BLUE)
draw.text((32,22), "SPCX 락업 해제됐는데 주가는 왜 올랐나", font=bold(25), fill=BLUE)
draw.text((32,74), "진짜 시험대는 12월 8일 최종 만료다", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, RED, (40,14,14), "1차 해제  |  8/6, 9.1억주",
     "IPO 공모 6.39억주보다 43% 많은 물량", "유통주 비중 4.9% → 11.8%로 143% 증가")
band(draw, by+step, bh, GREEN, (10,30,22), "반전  |  당일 +6.1% 마감",
     "장중 105.11달러 → 반등 마감, IPO가 대비 여전히 -20%", "선반영 가설: 6월 고점 대비 이미 반토막난 상태였음")
band(draw, by+step*2, bh, ORANGE, (44,20,10), "조건부 물량  |  4.56억주",
     "175.50달러 트리거 미달 시 소멸 아닌 12월로 이연", "현재가 108~113달러, 트리거까지 60%+ 상승 필요")
band(draw, by+step*3, bh, TEAL, (10,32,30), "남은 일정  |  8~10월 소규모 트란쉬",
     "3분기 실적 후 대형 트란쉬(~28%) 추가 예정", "이번 반등 패턴 반복 여부 확인 필요")
band(draw, by+step*4, bh, BLUE, (10,20,40), "분수령  |  12월 8일 최종 만료",
     "잔여 전량 + 이연된 조건부 물량 동시 방출", "역대급 매물 규모, 진짜 시험대")
footer(draw, "2026.08.08  |  SpaceX(SPCX) 락업 해제 구조 분석")
out = os.path.join(OUT_DIR, "2026-08-08_SPCX_락업해제구조.png")
img.save(out); print("Saved:", out)
