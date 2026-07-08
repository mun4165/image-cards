from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-06"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); ROW_A=(18,23,30); ROW_B=(24,30,39); HILITE=(20,32,30)
BLUE=(59,130,246); TEAL=(20,184,166); AMBER=(245,158,11); GREEN=(52,211,153); ORANGE=(249,115,22)

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

def base_canvas(accent, title, subtitle):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    draw.rectangle([0,0,W,4], fill=accent); draw.rectangle([0,0,4,H], fill=accent)
    draw.text((32,24), title, font=bold(36), fill=accent)
    draw.text((32,80), subtitle, font=bold(24), fill=GRAY)
    draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)
    return img, draw

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

FOOTER = "2026.07.06  |  $MU  Micron Technology"

# ============ 10장: 메모리 옆자리 세 회사 (2줄 셀 그리드) ============
img, draw = base_canvas(ORANGE, "메모리 옆자리, 세 번째 자리", "마이크론이 못 파는 수요가 흘러가는 곳")

cols10 = [("회사", 32, 210), ("포지션", 242, 300), ("핵심 수치", 542, 340), ("반박(리스크)", 882, 366)]
header_y = 150
for label, x, w in cols10:
    draw.text((x, header_y+8), label, font=bold(19), fill=GRAY)
draw.line([(32, header_y+56), (W-32, header_y+56)], fill=DARK_GRAY, width=1)

rows10 = [
    (BLUE, "Camtek", "CAMT", "3D 계측 장비(HBM 적층 검사)",
     "2026~27년 주문 약 2.6억 달러 확보",
     "후행 수요 + 메모리 3사 의존, 주가 이미 반영"),
    (TEAL, "Rambus", "RMBS", "메모리 인터페이스 로열티",
     "1분기 제품매출 8,800만 달러(+15% YoY)",
     "출하량 후행 성장, 강점 이미 주가에 반영"),
    (AMBER, "Sandisk", "SNDK", "순수 낸드 제조(WD 분사)",
     "매출총이익률 가이던스 65~67%",
     "낸드 사이클 더 험함, 계약 하한선 보호 없음"),
]
row_y, row_h = 214, 140
for i, (color, name, ticker, pos, headline, risk) in enumerate(rows10):
    y0 = row_y + i*row_h
    bg = ROW_A if i % 2 == 0 else ROW_B
    draw.rounded_rectangle([32, y0, W-32, y0+row_h-10], radius=8, fill=bg)
    draw.rectangle([32, y0, 38, y0+row_h-10], fill=color)
    draw.text((60, y0+16), name, font=bold(25), fill=color)
    draw.text((60, y0+52), ticker, font=font(17), fill=GRAY)
    draw.text((242, y0+18), pos, font=font(19), fill=WHITE)
    draw.text((542, y0+18), headline, font=bold(19), fill=WHITE)
    draw.text((882, y0+18), risk, font=font(16), fill=GRAY)

footer(draw, FOOTER)
out = os.path.join(OUT_DIR, "2026-07-06_메모리옆자리세회사.png")
img.save(out); print("Saved:", out)

# ============ 7장: 실적 발표 숫자 비교 (그리드) ============
img, draw = base_canvas(GREEN, "숫자로 보는 한 분기 궤적", "매출 · EPS · 매출총이익률, 4개 시점 비교")

cols7 = [("항목", 32, 220), ("1년 전", 252, 240), ("직전분기", 492, 240), ("이번분기(실적)", 732, 250), ("가이던스(다음)", 982, 266)]
header_y = 150
for label, x, w in cols7:
    draw.text((x, header_y+8), label, font=bold(18), fill=GRAY)
draw.line([(32, header_y+56), (W-32, header_y+56)], fill=DARK_GRAY, width=1)

rows7 = [
    ("매출", "약 93억 달러", "약 238.6억 달러", "약 414.6억 달러", "약 500억 달러", True),
    ("EPS(비GAAP)", "—", "12.20달러", "25.11달러(예상 20달러)", "약 31달러", False),
    ("매출총이익률", "—", "약 75%", "약 84.6%", "약 86%", False),
]
row_y, row_h = 214, 130
for i, (label, y1, prev, now, guide, hilite) in enumerate(rows7):
    y0 = row_y + i*row_h
    bg = HILITE if hilite else (ROW_A if i % 2 == 0 else ROW_B)
    draw.rounded_rectangle([32, y0, W-32, y0+row_h-10], radius=8, fill=bg)
    if hilite:
        draw.rectangle([32, y0, 38, y0+row_h-10], fill=GREEN)
    lc = GREEN if hilite else WHITE
    draw.text((60 if hilite else 32+16, y0+row_h//2-30), label, font=bold(22), fill=lc)
    draw.text((252, y0+row_h//2-14), y1, font=font(19), fill=(GRAY if y1=="—" else WHITE))
    draw.text((492, y0+row_h//2-14), prev, font=font(19), fill=(GRAY if prev=="—" else WHITE))
    draw.text((732, y0+row_h//2-14), now, font=bold(19), fill=WHITE)
    draw.text((982, y0+row_h//2-14), guide, font=font(19), fill=WHITE)

note_y = row_y + row_h*len(rows7) + 14
draw.text((32, note_y), "실적·가이던스 모두 시장 컨센서스를 상회 — 6장 세 시나리오 중 가장 강한 첫 번째를 넘어선 결과", font=font(16), fill=GRAY)

footer(draw, FOOTER)
out = os.path.join(OUT_DIR, "2026-07-06_실적궤적비교.png")
img.save(out); print("Saved:", out)

# ============ 6장: 메모리 사이클 약사 (밴드 스타일) ============
img, draw = base_canvas(AMBER, "\"이번엔 다르다\"는 말은 매번 나왔다", "메모리 사이클 약사 — 30년 반복된 패턴")

def band(draw, y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
    draw.line([(240,y+18),(240,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((268, y+20), headline, font=bold(24), fill=WHITE)
    draw.text((268, y+62), d1, font=font(18), fill=color)
    draw.text((268, y+92), d2, font=font(16), fill=GRAY)

bands6 = [
    dict(color=BLUE, fillbg=(14,24,44), label="2017~18",
         headline="첫 번째 슈퍼사이클 — 마진 70%까지",
         d1="서버·스마트폰 수요 붐, \"이번엔 다르다\" 등장",
         d2="2018~19년 증설 물량 쏟아지며 가격 붕괴"),
    dict(color=TEAL, fillbg=(10,32,30), label="2021~22",
         headline="팬데믹 특수 회복 — 오래가지 못함",
         d1="재고 쌓인 채로 소비 둔화와 충돌",
         d2="곧바로 사상 최악 다운사이클로 전환"),
    dict(color=AMBER, fillbg=(40,28,10), label="2022~23",
         headline="사상 최악 다운사이클",
         d1="매출 308억→155억 달러(반토막), GAAP 순손실 58.3억 달러",
         d2="주가 98달러대 → 49달러대(반토막)"),
]
by, bh, step = 146, 148, 164
for i, b in enumerate(bands6):
    band(draw, by+step*i, bh, b["color"], b["fillbg"], b["label"], b["headline"], b["d1"], b["d2"])

footer(draw, FOOTER)
out = os.path.join(OUT_DIR, "2026-07-06_메모리사이클약사.png")
img.save(out); print("Saved:", out)
