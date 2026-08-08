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
draw.text((32,22), "RKLB 우주군 3.97억달러 계약, 뉴트론이 안 뜬 상태로 받은 숫자", font=bold(24), fill=BLUE)
draw.text((32,74), "SB-AMTI 플라텔라이트, 매출화는 뉴트론 데뷔가 전제조건", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, BLUE, (10,20,40), "계약  |  8월 4일 발표",
     "미 우주군 SB-AMTI 프로그램, 3억 9,700만달러", "플라텔라이트 설계·제조·발사·운영 수직 통합")
band(draw, by+step, bh, AMBER, (40,30,8), "전제조건  |  발사체 미검증",
     "발사체는 뉴트론(Neutron), 아직 첫 비행 전", "2026년 4분기 목표, 2025년 11월 한 차례 지연 이력")
band(draw, by+step*2, bh, ORANGE, (44,20,10), "구조  |  로켓랩 단독 아님",
     "STR LLC 등 복수 업체 동시 수주(공급망 다원화)", "로켓랩 몫이 공개 3사 중 최대, 독식은 아님")
band(draw, by+step*3, bh, TEAL, (8,32,30), "비교  |  HASTE와 다른 점",
     "HASTE는 실적 있는 일렉트론 기반, 즉시 매출화", "SB-AMTI는 미검증 뉴트론 기반, 매출화 시점 불확실")
band(draw, by+step*4, bh, GREEN, (10,30,22), "watch  |  다음 확인 지점",
     "8월 10일 실적 콜에서 뉴트론 4분기 일정 재확인 여부", "표현이 유지되는지가 이번 계약의 진짜 변수")
footer(draw, "2026.08.05  |  Rocket Lab(RKLB) SB-AMTI 계약 발표 기준")
out = os.path.join(OUT_DIR, "2026-08-05_RKLB_우주군계약.png")
img.save(out); print("Saved:", out)
