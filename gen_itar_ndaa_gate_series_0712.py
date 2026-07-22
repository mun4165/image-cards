from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-12"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

def make_card(filename, kicker, title, subtitle, bands, footer_note):
    img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

    draw.text((32,20), kicker, font=bold(18), fill=GRAY)
    draw.text((32,46), title, font=bold(27), fill=ACCENT)
    draw.text((32,90), subtitle, font=bold(21), fill=GRAY)
    draw.line([(32,132),(W-32,132)], fill=DARK_GRAY, width=1)

    def band(y, h, color, fillbg, label, headline, d1, d2):
        draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
        draw.rectangle([32,y,38,y+h], fill=color)
        draw.text((60, y+h//2-14), label, font=bold(21), fill=color)
        draw.line([(232,y+16),(232,y+h-16)], fill=DARK_GRAY, width=1)
        block_h = 30+14+28+12+26
        ty = y + (h-block_h)//2
        draw.text((258, ty), headline, font=bold(21), fill=WHITE)
        draw.text((258, ty+42), d1, font=font(17), fill=color)
        draw.text((258, ty+76), d2, font=font(16), fill=GRAY)

    by = 152
    avail = (H-30) - by - 20
    step = avail // len(bands)
    bh = step - 16
    for i, b in enumerate(bands):
        band(by+step*i, bh, *b)

    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), footer_note, font=font(15), fill=GRAY)

    out = os.path.join(OUT_DIR, filename)
    img.save(out); print("Saved:", out)


make_card(
    "2026-07-12_ITARNDAA_1of3_물건자체를막는것.png",
    "방산·우주 국가안보 게이트 시리즈 1/3",
    "물건 자체를 막는 것",
    "ITAR vs non-ITAR — 미국 전용이냐, 전세계 자유판매냐",
    [
        (ORANGE, (40,24,10), "ITAR",
         "미국인만 만들 수 있는 물건 카테고리",
         "라이트패스(LPTH) — 美 ITAR등록 공장, 방산렌즈로 美시장 접근",
         "로켓랩 — 발사체가 ITAR통제라 NZ발사엔 美-NZ 정부간 조약(TSA) 별도필요"),
        (GREEN, (10,28,20), "non-ITAR",
         "설계 자체를 미국 통제 밖에 두는 전략",
         "세틀로직 NextGen — 처음부터 non-ITAR로 설계, 수출허가 없이 전세계 판매",
         "해외 주권 국방고객과 1,200만달러 위성계약 체결"),
        (BLUE, (10,20,34), "핵심 차이",
         "같은 위성업계, 정반대 전략",
         "라이트패스·로켓랩 = 美 정부시장 접근이 목적",
         "세틀로직 non-ITAR 라인 = 美 밖 전세계 판매가 목적"),
    ],
    "2026.07.12  |  국가안보 게이트 개념정리  1/3",
)

make_card(
    "2026-07-12_ITARNDAA_2of3_회사이름을찍어막는것.png",
    "방산·우주 국가안보 게이트 시리즈 2/3",
    "회사 이름을 콕 찍어 막는 것",
    "NDAA와 Entity List — 블랙리스트는 산업마다 다르고, 조달 한정이다",
    [
        (ORANGE, (40,24,10), "NDAA 889",
         "통신·CCTV 5개사 한정 조달금지",
         "화웨이·ZTE·하이크비전·다후아·하이테라",
         "연방기관이 이 회사들 장비를 못 삼"),
        (GREEN, (10,28,20), "NDAA 5949",
         "반도체 3개사, 그런데 정부조달에만 적용",
         "SMIC·창신메모리(CXMT)·YMTC, 2027-12-23 발효",
         "애플이 아이폰(민간소비자용)에 CXMT 쓰는 건 이 규정 대상 자체가 아님"),
        (BLUE, (10,20,34), "진짜 관건",
         "Entity List 등재 여부",
         "CXMT는 국방부 1260H명단엔 있지만 상무부 Entity List엔 아직 미등재",
         "애플 로비는 5949 웨이버가 아니라 이 리스트에 안 올라가게 막는 것"),
    ],
    "2026.07.12  |  국가안보 게이트 개념정리  2/3",
)

make_card(
    "2026-07-12_ITARNDAA_3of3_지분과인수를심사하는것.png",
    "방산·우주 국가안보 게이트 시리즈 3/3",
    "지분·인수를 심사하는 것",
    "FOCI와 CFIUS — 누가 회사를 쥐고 있는지가 문제일 때",
    [
        (ORANGE, (40,24,10), "FOCI",
         "안보계약 들어가려면 지배구조부터",
         "로켓랩 — NZ창업, 2013 美델라웨어 법인화로 안보계약 자격 확보",
         "세틀로직 — 텐센트 지분 정리+델라웨어 이전, 美정부용 서비스 자격 확보용"),
        (GREEN, (10,28,20), "CFIUS",
         "외국인의 미국회사 인수 자체를 심사",
         "2018 브로드컴(싱가포르)의 퀄컴 인수, 안보 이유로 무산",
         "FOCI=지배구조 심사, CFIUS=인수거래 승인여부로 국면이 다름"),
    ],
    "2026.07.12  |  국가안보 게이트 개념정리  3/3",
)
