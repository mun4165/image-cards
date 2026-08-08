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

img, draw = base_canvas(CYAN)
draw.text((32,22), "CRCL 2분기 실적, 매출 미스인데 순이익은 흑자전환", font=bold(25), fill=CYAN)
draw.text((32,74), "엇갈린 두 숫자, 진짜 성장은 다른 곳에 있었다", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, RED, (40,14,14), "매출  |  컨센서스 하회",
     "총매출 7.01억달러, 컨센서스 7.35억+달러", "리저브 수익 6.68억달러, 전년비 +5% 그침")
band(draw, by+step, bh, GREEN, (10,30,22), "순이익  |  흑자전환",
     "계속영업 순이익 4,800만달러", "전년비 5.3억달러 개선, IPO 비용 소멸 효과")
band(draw, by+step*2, bh, BLUE, (10,20,40), "본업  |  USDC 유통량·거래량",
     "유통량 733억달러(+19%), 온체인 14.8조달러(+151%)", "리저브 수익보다 훨씬 가파른 성장")
band(draw, by+step*3, bh, AMBER, (40,30,8), "구조  |  금리 하락이 가린 성장",
     "유통량은 늘어도 국채 금리 하락이 수익 상쇄", "총매출만 보면 성장이 잘 안 보이는 이유")
band(draw, by+step*4, bh, ORANGE, (44,20,10), "watch  |  다음 분기 관전포인트",
     "금리 인하 지속 시 리저브 수익 정체 반복 여부", "Arc 등 기타매출이 의존도 낮출 만큼 크는지")
footer(draw, "2026.08.05  |  Circle Internet Group(CRCL) 2026년 2분기 실적 발표")
out = os.path.join(OUT_DIR, "2026-08-05_CRCL_실적요약.png")
img.save(out); print("Saved:", out)
