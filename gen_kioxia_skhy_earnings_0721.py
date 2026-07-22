from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-21"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); RED=(248,113,113); ORANGE=(249,115,22); BLUE=(59,130,246); TEAL=(20,184,166)

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

img, draw = base_canvas(TEAL)
draw.text((32,22), "SK하이닉스·키옥시아 실적발표 이틀 간격", font=bold(32), fill=TEAL)
draw.text((32,76), "낸드 공급과잉 우려를 확인하는 첫 구간이다", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, BLUE, (10,20,40), "SK하이닉스",
     "7/29(수) 오전 9시, 2분기 실적 컨퍼런스콜", "청주 낸드공장 80조원 증설 이후 첫 실적발표")
band(draw, by+step, bh, RED, (40,14,14), "키옥시아",
     "7/31(금) 오후 3시30분, 1분기 결산발표", "하이닉스 가이던스 본 다음 이틀 뒤 자기 실적 공개")
band(draw, by+step*2, bh, AMBER, (40,28,10), "관전 포인트",
     "capex 배분·ASP 코멘트·맞대응 증설 여부", "낸드 ASP(평균판매가) 코멘트가 서로 밸류에이션에 연동")
band(draw, by+step*3, bh, ORANGE, (40,22,10), "배경",
     "키옥시아 고점대비 -54%, 7/2 하이닉스 발표가 트리거", "연간 capex의 9~10배 규모 증설에 공급전제 흔들림")
footer(draw, "2026.07.21  |  285A  000660")
out = os.path.join(OUT_DIR, "2026-07-21_실적발표일정.png")
img.save(out); print("Saved:", out)
