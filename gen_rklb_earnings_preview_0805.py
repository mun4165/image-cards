from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-08-05"
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
draw.text((32,22), "RKLB 8월 10일 실적, 적자 확대가 정상인 이유", font=bold(25), fill=BLUE)
draw.text((32,74), "진짜 변수는 매출·마진이 아니라 뉴트론 일정", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, BLUE, (10,20,40), "1분기  |  모든 가이던스 지표 상회",
     "매출 2.003억달러(+63.5%)  ·  총마진 38.2%", "수주잔고 22억달러, 사상 최고 마진")
band(draw, by+step, bh, ORANGE, (44,20,10), "2분기 가이던스  |  적자 확대는 계획된 것",
     "매출 2.25~2.4억달러  ·  EBITDA손실 2000~2600만", "뉴트론 개발비·인수비용 반영, 악화 아님")
band(draw, by+step*2, bh, CYAN, (10,28,32), "핵심변수  |  뉴트론 4분기 첫 비행 일정",
     "회사 목표 여전히 2026년 4분기 유지", "\"시험대 부품 탑재\"가 CEO 제시 기준")
band(draw, by+step*3, bh, GREEN, (10,30,22), "베팅  |  미발사 상태에서 계약 5건",
     "발사단가 5,000만~5,500만달러", "일렉트론(840만달러) 대비 6배 단가")
band(draw, by+step*4, bh, AMBER, (40,30,8), "리스크  |  헤드라인 적자만 보면 오판",
     "손실이 가이던스 범위 내인지가 진짜 기준", "뉴트론 일정 후퇴 시에만 경고 신호")
footer(draw, "2026.08.10  |  RKLB 로켓랩 2분기 실적 발표 (장 마감 후)")
out = os.path.join(OUT_DIR, "2026-08-05_RKLB_실적프리뷰.png")
img.save(out); print("Saved:", out)
