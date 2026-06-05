from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-05"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
AMBER     = (245, 158, 11)
CYAN      = (6, 182, 212)
GREEN     = (52, 211, 153)

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

def base_canvas():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=GRID, width=1)
    draw.rectangle([0, 0, W, 4], fill=CYAN)
    draw.rectangle([0, 0, 4, H], fill=CYAN)
    return img, draw

img, draw = base_canvas()

# ── 헤더 ──
draw.text((32, 14), "SATL", font=bold(40), fill=CYAN)
draw.text((130, 18), "세틀로직, 퇴역 장성 3인 영입 — 미 방산·정보 인맥 집중 확보", font=bold(23), fill=WHITE)
draw.text((130, 56), "NASDAQ: SATL  |  위성 지구관측(EO)  |  2026.06.05", font=font(15), fill=GRAY)
draw.line([(32, 86), (W - 32, 86)], fill=DARK_GRAY, width=1)

# ── 3 컬럼 레이아웃 ──
col_w = 392
col_x = [32, 444, 856]
CARD_TOP = 96
CARD_BOT = 614

people = [
    {
        "color": CYAN,
        "name": "마이클 E. 윌리엄슨",
        "rank": "육군 중장 (예비역)",
        "role": "이사회 독립 이사",
        "date": "선임: 2026.06.04",
        "bg": "방산 조달 전문가",
        "details": [
            "1983년 임관 / 30년+ 방산 조달",
            "육군 조달·군수·기술 차관보",
            "군 부차관보 역임",
            "록히드 마틴 고위 임원 출신",
        ],
        "insight": "미 육군 계약 채널 확보",
    },
    {
        "color": GREEN,
        "name": "프랭크 D. 휘트워스 3세",
        "rank": "해군 중장 (예비역)",
        "role": "전략 자문",
        "date": "선임: 2026.03.25",
        "bg": "NGA 8대 국장",
        "details": [
            "NGA = 위성영상·지형정보 공급 기관",
            "AI/ML 프로젝트 '메이븐' 실전화 주도",
            "정보기관·군 직접 고객 네트워크",
            "세틀로직 핵심 타겟 고객군과 직결",
        ],
        "insight": "정보기관 직접 접근 채널",
    },
    {
        "color": AMBER,
        "name": "조지프 F. 던포드 주니어",
        "rank": "해병대 대장 (예비역)",
        "role": "이사회 이사",
        "date": "합류: 2022",
        "bg": "합참의장 (2015~2019)",
        "details": [
            "대통령·국방장관 핵심 군사 자문",
            "므누신 Liberty Strategic Capital",
            "$1.5억 투자 당시 이사회 합류",
            "최고위 국방 의사결정 라인",
        ],
        "insight": "최고위 국방 의사결정 직결",
    },
]

for i, (p, cx) in enumerate(zip(people, col_x)):
    color = p["color"]

    # 카드 배경
    draw.rounded_rectangle([cx, CARD_TOP, cx + col_w, CARD_BOT], radius=6, fill=(18, 22, 32))
    draw.rectangle([cx, CARD_TOP, cx + 4, CARD_BOT], fill=color)

    y = CARD_TOP + 18

    # 이름
    draw.text((cx + 16, y), p["name"], font=bold(20), fill=WHITE)
    y += 32

    # 계급
    draw.text((cx + 16, y), p["rank"], font=font(15), fill=color)
    y += 28

    # 역할 배지
    draw.rounded_rectangle([cx + 16, y, cx + col_w - 16, y + 30], radius=4, fill=(28, 36, 52))
    draw.text((cx + 22, y + 6), p["role"] + "   |   " + p["date"], font=bold(13), fill=color)
    y += 44

    # 구분선
    draw.line([(cx + 16, y), (cx + col_w - 16, y)], fill=DARK_GRAY, width=1)
    y += 16

    # 배경 레이블
    draw.text((cx + 16, y), p["bg"], font=bold(17), fill=color)
    y += 34

    # 세부 내용
    for detail in p["details"]:
        draw.rectangle([cx + 16, y + 8, cx + 20, y + 14], fill=(80, 92, 108))
        draw.text((cx + 28, y), detail, font=font(14), fill=GRAY)
        y += 34

    y += 10
    # 구분선
    draw.line([(cx + 16, y), (cx + col_w - 16, y)], fill=DARK_GRAY, width=1)
    y += 16

    # 인사이트
    draw.text((cx + 16, y), "→  " + p["insight"], font=bold(15), fill=color)

    # 컬럼 구분선 (마지막 제외)
    if i < 2:
        div_x = cx + col_w + 10
        draw.line([(div_x, CARD_TOP), (div_x, CARD_BOT)], fill=DARK_GRAY, width=1)

# ── 하단 배너 ──
draw.rounded_rectangle([32, CARD_BOT + 8, W - 32, H - 10], radius=6, fill=(4, 20, 30))
draw.text((52, CARD_BOT + 18), "NGA 국장  +  합참의장  +  방산 조달 전문가", font=bold(18), fill=WHITE)
draw.text((52, CARD_BOT + 46), "세틀로직이 어느 문을 두드리는지, 이 세 사람이 말해준다", font=font(15), fill=CYAN)

out_path = os.path.join(OUT_DIR, "2026-06-05_SATL_장성3인영입.png")
img.save(out_path)
print(f"Saved: {out_path}")
