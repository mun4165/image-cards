from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-20"
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
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(196,y+14),(196,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((220, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((220, y+46), detail, font=font(15), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# ── SOXX 베어마켓 vs S&P500 디버전스, 메타컴퓨트 트리거 ──────────────────────────
img, draw = base_canvas(RED)
draw.text((32,22), "SOXX 베어마켓인데 S&P500은 -2%, 왜 갈렸나", font=bold(32), fill=RED)
draw.text((32,76), "유동성 충격이 아니라 로테이션이라는 근거를 짚었다", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, RED, (40,14,14), "디버전스",
     "SOXX 6/2 고점 대비 -20.3% (베어마켓)", "같은 기간 S&P500은 -2.0%, 다우는 오히려 사상 최고치")
band(draw, by+step, bh, AMBER, (40,28,10), "트리거",
     "7/1 메타플랫폼스 \"메타컴퓨트\" 발표", "잉여 AI 컴퓨팅을 외부에 판매, 메타 주가는 +8.81%")
band(draw, by+step*2, bh, ORANGE, (40,22,10), "당일 반응",
     "마이크론 -10.57%, AMD -6.89%, 엔비디아 -1.25%", "반도체·클라우드 시총 약 2,000억 달러 증발 추산")
band(draw, by+step*3, bh, BLUE, (10,20,40), "해석",
     "컴퓨팅 희소성 프리미엄이 꺾이는 재평가 국면", "지수는 버팀 = 이탈 아닌 반도체發 로테이션")
footer(draw, "2026.07.20  |  SOXX")
out = os.path.join(OUT_DIR, "2026-07-20_SOXX_로테이션.png")
img.save(out); print("Saved:", out)
