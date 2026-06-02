from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-02"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (60, 70, 82)
AMBER     = (245, 158, 11)
TEAL      = (20, 184, 166)
BLUE      = (59, 130, 246)
CYAN      = (6, 182, 212)
PURPLE    = (167, 139, 250)
GREEN     = (52, 211, 153)
RED       = (239, 68, 68)
ORANGE    = (249, 115, 22)

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)
def tw(draw, text, f):
    bbox = draw.textbbox((0, 0), text, font=f)
    return bbox[2] - bbox[0]
def centered(draw, text, y, f, color=WHITE):
    w = tw(draw, text, f)
    draw.text(((W - w) // 2, y), text, font=f, fill=color)

def make_base(accent_color):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=GRID, width=1)
    draw.rectangle([0, 0, W, 4], fill=accent_color)
    return img, draw

def footer(draw, source="TrendForce / Tom's Hardware / 각사 IR"):
    draw.line([(60, H-52), (W-60, H-52)], fill=DARK_GRAY, width=1)
    draw.text((60, H-38), f"2026.06.02  |  {source}  |  개인 공부 기록, 투자 추천 아님", font=font(17), fill=GRAY)


# ─────────────────────────────────────────────────────
# 표지
# ─────────────────────────────────────────────────────
def make_cover():
    img, draw = make_base(CYAN)

    wm = font(160)
    wm_text = "NAND"
    wm_w = tw(draw, wm_text, wm)
    img_wm = Image.new("RGBA", (W, H), (0,0,0,0))
    d_wm = ImageDraw.Draw(img_wm)
    d_wm.text(((W-wm_w)//2, 180), wm_text, font=wm, fill=(6, 182, 212, 14))
    img = Image.alpha_composite(img.convert("RGBA"), img_wm).convert("RGB")
    draw = ImageDraw.Draw(img)

    centered(draw, "올바른 비교를 찾아가는 과정", 148, bold(44), WHITE)
    centered(draw, "키옥시아  vs  샌디스크", 210, bold(62), CYAN)
    draw.line([(W//2-200, 292), (W//2+200, 292)], fill=DARK_GRAY, width=1)
    centered(draw, "마이크론과 키옥시아를 비교했더니 비교 자체가 틀렸다", 312, font(24), GRAY)

    tags = ["NAND", "키옥시아", "샌디스크", "메모리반도체", "투자공부"]
    pill_x = 60
    y_pill = 390
    for t in tags:
        pw = tw(draw, t, font(20)) + 28
        draw.rounded_rectangle([pill_x, y_pill, pill_x+pw, y_pill+32], radius=6, fill=DARK_GRAY)
        draw.text((pill_x+14, y_pill+4), t, font=font(20), fill=GRAY)
        pill_x += pw + 12

    centered(draw, "$MU  $SNDK  ·  2026.06.02", 470, font(22), GRAY)
    footer(draw)
    img.save(os.path.join(OUT_DIR, "2026-06-02_키옥시아샌디스크_00_표지.png"))
    print("Saved: 표지")


# ─────────────────────────────────────────────────────
# 중간삽입1 — DRAM vs NAND 차이
# ─────────────────────────────────────────────────────
def make_insert1():
    img, draw = make_base(BLUE)
    draw.rectangle([0, 0, 4, H], fill=BLUE)

    draw.text((60, 44), "마이크론 vs 키옥시아", font=bold(38), fill=WHITE)
    draw.text((60, 96), "파는 제품이 다릅니다", font=font(24), fill=GRAY)
    draw.line([(60, 136), (W-60, 136)], fill=DARK_GRAY, width=1)

    # 마이크론
    draw.rounded_rectangle([60, 154, 600, 510], radius=10, fill=(15, 20, 40))
    draw.text((80, 174), "마이크론 (MU)", font=bold(30), fill=BLUE)
    draw.text((80, 216), "DRAM 79%  /  NAND 21%", font=bold(22), fill=WHITE)
    draw.line([(80, 256), (580, 256)], fill=DARK_GRAY, width=1)
    mu_pts = [
        ("HBM 포함", "AI GPU에 직접 쌓는 메모리"),
        ("GPU 1장당", "HBM이 들어감"),
        ("2026년 물량", "전량 선계약 완료"),
        ("역할", "AI가 지금 연산하는 데이터 처리"),
    ]
    y = 272
    for label, desc in mu_pts:
        draw.text((80, y), f"• {label}:", font=bold(19), fill=BLUE)
        draw.text((80, y+24), f"  {desc}", font=font(19), fill=GRAY)
        y += 54

    # 키옥시아
    draw.rounded_rectangle([680, 154, W-60, 510], radius=10, fill=(15, 30, 20))
    draw.text((700, 174), "키옥시아 (285A)", font=bold(30), fill=TEAL)
    draw.text((700, 216), "NAND 100%  /  HBM 없음", font=bold(22), fill=WHITE)
    draw.line([(700, 256), (W-80, 256)], fill=DARK_GRAY, width=1)
    kx_pts = [
        ("NAND만", "전원 꺼도 데이터 유지"),
        ("HBM", "없음"),
        ("역할", "데이터를 저장해두는 메모리"),
        ("경쟁사", "삼성·SK·마이크론·샌디스크·YMTC"),
    ]
    y = 272
    for label, desc in kx_pts:
        draw.text((700, y), f"• {label}:", font=bold(19), fill=TEAL)
        draw.text((700, y+24), f"  {desc}", font=font(19), fill=GRAY)
        y += 54

    centered(draw, "파는 제품이 다른 두 회사 — 같은 '메모리'라도 직접 비교는 틀린 출발점입니다", 534, font(20), AMBER)
    footer(draw)
    img.save(os.path.join(OUT_DIR, "2026-06-02_키옥시아샌디스크_01_DRAM_vs_NAND.png"))
    print("Saved: 중간삽입1")


# ─────────────────────────────────────────────────────
# 중간삽입2 — HBM 설명 + NAND 경쟁사 점유율
# ─────────────────────────────────────────────────────
def make_insert2():
    img, draw = make_base(PURPLE)
    draw.rectangle([0, 0, 4, H], fill=PURPLE)

    draw.text((60, 44), "HBM이란 무엇인가  +  NAND 경쟁 구도", font=bold(36), fill=WHITE)
    draw.line([(60, 96), (W-60, 96)], fill=DARK_GRAY, width=1)

    # 왼쪽: HBM
    draw.text((60, 112), "HBM (High Bandwidth Memory)", font=bold(24), fill=PURPLE)
    hbm_pts = [
        "AI GPU 위에 직접 쌓아 올리는 메모리",
        "GPU 한 장마다 반드시 들어감",
        "AI 서버 증가 = HBM 수요 직접 비례 증가",
        "삼성·SK하이닉스·마이크론 3사만 생산",
        "마이크론 2026년 물량 전량 선계약 완료",
    ]
    y = 150
    for p in hbm_pts:
        draw.text((68, y), "•  " + p, font=font(20), fill=GRAY)
        y += 34
    draw.rounded_rectangle([60, y+8, 600, y+46], radius=6, fill=(30, 20, 45))
    draw.text((76, y+14), "키옥시아는 HBM을 만들지 않습니다", font=bold(20), fill=PURPLE)

    draw.line([(640, 96), (640, H-60)], fill=DARK_GRAY, width=1)

    # 오른쪽: NAND 점유율
    draw.text((660, 112), "NAND 글로벌 점유율 (TrendForce 2025 Q3)", font=bold(20), fill=WHITE)
    draw.line([(660, 148), (W-60, 148)], fill=DARK_GRAY, width=1)

    shares = [
        ("삼성전자",  "32.3%", RED),
        ("SK하이닉스","19.3%", ORANGE),
        ("키옥시아",  "15.3%", CYAN),
        ("마이크론",  "약 15%", BLUE),
        ("샌디스크",  "12.4%", GREEN),
        ("YMTC(중국)","잔여",   GRAY),
    ]
    y = 164
    for name, share, color in shares:
        bar_w = int((float(share.replace('%','').replace('약 ','').replace('잔여','5')) / 35) * 500)
        draw.rounded_rectangle([660, y, 660+bar_w, y+32], radius=4, fill=color)
        draw.text((660, y+6), f"  {name}", font=bold(18), fill=BG if color != GRAY else WHITE)
        draw.text((W-120, y+6), share, font=bold(20), fill=color)
        y += 44

    footer(draw)
    img.save(os.path.join(OUT_DIR, "2026-06-02_키옥시아샌디스크_02_HBM_NAND경쟁사.png"))
    print("Saved: 중간삽입2")


# ─────────────────────────────────────────────────────
# 중간삽입3 — 시총 비교
# ─────────────────────────────────────────────────────
def make_insert3():
    img, draw = make_base(TEAL)

    centered(draw, "올바른 비교 — 키옥시아 vs 샌디스크", 44, bold(38), WHITE)
    centered(draw, "2026.06.02 기준", 96, font(22), GRAY)
    draw.line([(60, 130), (W-60, 130)], fill=DARK_GRAY, width=1)

    # 키옥시아
    draw.rounded_rectangle([60, 148, 580, 490], radius=10, fill=(15, 28, 30))
    draw.text((80, 170), "키옥시아 (285A)", font=bold(30), fill=TEAL)
    draw.text((80, 212), "도쿄거래소 · 일본", font=font(20), fill=GRAY)
    draw.line([(80, 250), (560, 250)], fill=DARK_GRAY, width=1)
    kx_data = [
        ("시총",    "¥39.6조 (~$200~260B)"),
        ("분기 매출", "약 $6.3B"),
        ("매수",    "한국·미국 직접 불가"),
        ("ADR 상장", "준비 중 — 미정"),
        ("환율",    "엔화 변동 → 달러 시총 변동"),
    ]
    y = 268
    for label, val in kx_data:
        draw.text((80, y), label, font=font(18), fill=GRAY)
        draw.text((80, y+24), val, font=bold(20), fill=WHITE)
        y += 52

    # 샌디스크
    draw.rounded_rectangle([700, 148, W-60, 490], radius=10, fill=(15, 30, 20))
    draw.text((720, 170), "샌디스크 (SNDK)", font=bold(30), fill=GREEN)
    draw.text((720, 212), "나스닥 · 미국", font=font(20), fill=GRAY)
    draw.line([(720, 250), (W-80, 250)], fill=DARK_GRAY, width=1)
    sn_data = [
        ("시총",     "$261.9B"),
        ("분기 매출", "$5.95B"),
        ("매수",     "달러로 바로 가능"),
        ("백로그",   "$42B (Q1 2026 IR 기준)"),
        ("YTD 수익률","+505% (S&P 500 1위)"),
    ]
    y = 268
    for label, val in sn_data:
        draw.text((720, y), label, font=font(18), fill=GRAY)
        draw.text((720, y+24), val, font=bold(20), fill=WHITE)
        y += 52

    centered(draw, "같은 NAND 사업 구조 — 시총은 거의 동일", 516, font(21), AMBER)
    footer(draw, "SNDK IR Q1 2026 / 285A TYO")
    img.save(os.path.join(OUT_DIR, "2026-06-02_키옥시아샌디스크_03_시총비교.png"))
    print("Saved: 중간삽입3")


# ─────────────────────────────────────────────────────
# 중간삽입4 — NAND 기술력 + 방향성
# ─────────────────────────────────────────────────────
def make_insert4():
    img, draw = make_base(AMBER)
    draw.rectangle([0, 0, 4, H], fill=AMBER)

    draw.text((60, 44), "NAND 기술력 비교  +  두 회사의 방향성", font=bold(36), fill=WHITE)
    draw.line([(60, 96), (W-60, 96)], fill=DARK_GRAY, width=1)

    # 레이어 비교 표
    draw.text((60, 112), "레이어(층수) 비교 — 2026년 기준", font=bold(22), fill=AMBER)
    rows = [
        ("키옥시아/샌디스크", "BiCS10", "332레이어", GREEN),
        ("SK하이닉스",        "-",      "321레이어", BLUE),
        ("삼성전자",          "V10",    "430레이어 (준비 중)", ORANGE),
        ("마이크론",          "-",      "232레이어", GRAY),
    ]
    y = 148
    for company, gen, layer, color in rows:
        draw.rounded_rectangle([60, y, 620, y+48], radius=6,
                                fill=(20, 25, 35) if color != GREEN else (15, 30, 20))
        draw.text((76, y+8), company, font=bold(20), fill=color)
        draw.text((280, y+8), gen, font=font(18), fill=GRAY)
        lw = tw(draw, layer, bold(20))
        draw.text((610-lw, y+8), layer, font=bold(20), fill=color)
        y += 56

    draw.text((60, y+8), "BiCS10: 밀도 59%↑ / 읽기속도 33%↑ (출처: TrendForce 2026.05)", font=font(18), fill=GRAY)

    draw.line([(660, 96), (660, H-60)], fill=DARK_GRAY, width=1)

    # 방향성
    draw.text((680, 112), "두 회사의 방향성", font=bold(22), fill=WHITE)
    draw.line([(680, 148), (W-60, 148)], fill=DARK_GRAY, width=1)

    directions = [
        (GREEN,  "샌디스크",
         "S&P 500 YTD 최고 +505%\nNAND 공급 부족 → 가격·실적 동반 상승\n백로그 $42B · Capex +40% YoY"),
        (CYAN,   "키옥시아",
         "Q1 매출 QoQ +83% / 영업이익률 급회복\nBiCS10 2026년 양산 가속\nADR 상장 시 접근성 할인 해소 기대"),
        (AMBER,  "공통",
         "NAND 공급 부족 국면 동반 수혜\nBiCS10 원가 우위 본격화 예정\nCapex 합산 전년비 +40% 투자 중"),
    ]
    y = 164
    for color, name, desc in directions:
        draw.rectangle([676, y, 680, y+80], fill=color)
        draw.text((692, y), name, font=bold(20), fill=color)
        for j, line in enumerate(desc.split("\n")):
            draw.text((692, y+28+j*24), line, font=font(17), fill=GRAY)
        y += 100

    footer(draw)
    img.save(os.path.join(OUT_DIR, "2026-06-02_키옥시아샌디스크_04_기술력_방향성.png"))
    print("Saved: 중간삽입4")


make_cover()
make_insert1()
make_insert2()
make_insert3()
make_insert4()
print("\nAll saved to:", OUT_DIR)
