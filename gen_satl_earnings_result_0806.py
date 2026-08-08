from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-08-06"
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

img, draw = base_canvas(GREEN)
draw.text((32,22), "SATL 2분기 실적, 매출 서프라이즈에 첫 영업흑자까지", font=bold(25), fill=GREEN)
draw.text((32,74), "어제 던진 현금흐름 질문에 회사가 직접 답했다", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, GREEN, (10,30,22), "매출  |  컨센서스 대폭 상회",
     "1,590만달러, 전년비 +259%", "컨센서스 933만달러 대비 약 70% 상회")
band(draw, by+step, bh, GREEN, (10,30,22), "수익성  |  창사 첫 흑자",
     "분기 첫 영업이익 흑자 + 조정 EBITDA 흑자", "매출 증가 속도를 비용이 따라잡지 못한 게 아니라 반대로 감")
band(draw, by+step*2, bh, BLUE, (10,20,40), "현금  |  1억1,280만달러",
     "1분기 말 1억2,190만달러 대비 소폭 감소", "멀린 위성군 자본지출 진행 중 — 성장투자용으로 성격 전환")
band(draw, by+step*3, bh, AMBER, (40,30,8), "파이프라인  |  RPO 8,070만달러",
     "잔여계약이행의무, 분기 매출의 5배 규모", "정부위성 인도·지구관측 파트너십이 다분기 매출로 예약된 상태")
band(draw, by+step*4, bh, ORANGE, (44,20,10), "watch  |  다음 관전포인트",
     "멀린 첫 발사 2026년 10월, 초기 위성군 완료 2027년 상반기", "이번 흑자가 일회성인지 구조적인지는 다음 1~2분기가 확인 지점")
footer(draw, "2026.08.06  |  Satellogic(SATL) 2026년 2분기 실적 발표")
out = os.path.join(OUT_DIR, "2026-08-06_SATL_실적결과.png")
img.save(out); print("Saved:", out)
