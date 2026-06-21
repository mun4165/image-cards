from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-21"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); RED=(239,68,68); ORANGE=(249,115,22)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "같은 광통신 붐, 사다리의 다른 칸", font=bold(40), fill=ACCENT)
draw.text((32,78), "AXT는 업스트림 InP 기판, AOI는 다운스트림 완제품 모듈", font=bold(22), fill=GRAY)
draw.line([(32,120),(W-32,120)], fill=DARK_GRAY, width=1)

# 좌측 — 공급망 사다리 (위=업스트림)
draw.text((32,152), "광트랜시버 공급망 사다리", font=bold(21), fill=WHITE)
NODE_X = 60
nodes = [
    ("인듐 원재료",          "원자재",                         GRAY,  False),
    ("InP 기판 · 웨이퍼",    "← AXT  업스트림 · 공급부족 70%", CYAN,  True),
    ("에피택셜 · 레이저칩",  "Coherent · Lumentum 등",         GRAY,  False),
    ("트랜시버 모듈",        "← AOI  다운스트림 · ASP 100% 노출", AMBER, True),
    ("AI 데이터센터",        "최종 수요처",                    GRAY,  False),
]
top, step = 196, 86
draw.line([(NODE_X, top+6),(NODE_X, top+step*(len(nodes)-1)+6)], fill=DARK_GRAY, width=3)
for i,(head,sub,color,hl) in enumerate(nodes):
    y = top + step*i
    r = 13 if hl else 8
    draw.ellipse([NODE_X-r,y+6-r,NODE_X+r,y+6+r], fill=color)
    if hl:
        draw.ellipse([NODE_X-r-5,y+6-r-5,NODE_X+r+5,y+6+r+5], outline=color, width=2)
    tx = NODE_X+32
    draw.text((tx,y-7), head, font=bold(21 if hl else 19), fill=(WHITE if hl else GRAY))
    draw.text((tx,y+20), sub, font=font(16), fill=color if hl else DARK_GRAY)

# 가운데 구분선
draw.line([(700,150),(700,H-58)], fill=DARK_GRAY, width=1)

# 우측 — 두 종목 비교 카드
def card(x, y, w, h, color, ticker, name, rows):
    draw.rounded_rectangle([x,y,x+w,y+h], radius=10, fill=(20,26,34))
    draw.rectangle([x,y,x+5,y+h], fill=color)
    draw.text((x+20,y+14), ticker, font=bold(26), fill=color)
    draw.text((x+118,y+22), name, font=font(17), fill=GRAY)
    ry = y+58
    for label, val in rows:
        draw.text((x+20,ry), label, font=font(16), fill=GRAY)
        draw.text((x+150,ry), val, font=bold(17), fill=WHITE)
        ry += 30

CX, CW = 730, 518
card(CX, 168, CW, 192, CYAN, "AXT", "InP 기판 · 순수 업스트림", [
    ("시가총액", "약 $5.4B"),
    ("가격 방패", "공급부족 70% 시장의 35% 점유"),
    ("실적", "Q2 첫 GAAP 흑자 가이드 · 백로그 $100M+"),
    ("리스크", "중국 수출허가 · 6인치는 추격자"),
])
card(CX, 374, CW, 192, AMBER, "AOI", "완제품 트랜시버 · 다운스트림", [
    ("시가총액", "약 $13B  (매출의 약 12배)"),
    ("가격 방패", "약함 — 단가 직접 노출 · CPO 매출 0"),
    ("캐파", "월 10만→65만개  증설 = 글럿 공급원"),
    ("리스크", "고객 2곳이 매출 82% · GAAP 적자"),
])

# 하단 핵심 박스
by = 580
draw.rounded_rectangle([730,by,W-32,by+62], radius=8, fill=(8,30,36))
draw.text((748,by+12), "같은 붐이라도, 가격을 지키는 칸과 물량만 지키는 칸은 다르다", font=bold(19), fill=CYAN)
draw.text((748,by+37), "AXT는 부족이 방패, AOI는 증설이 곧 자기 발등 — 갈림길은 ASP 곡선", font=font(16), fill=GRAY)

# 푸터
draw.line([(32,H-44),(W-32,H-44)], fill=DARK_GRAY, width=1)
draw.text((32,H-30), "2026.06.18  |  $AXTI  ·  $AAOI", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-21_AAOI_AXTI_병목사다리.png")
img.save(out); print("Saved:", out)
