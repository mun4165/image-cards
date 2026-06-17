from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-10"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (10, 13, 18)
GRID      = (255, 255, 255, 10)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (48, 54, 66)
CYAN      = (6, 182, 212)
GREEN     = (52, 211, 153)
BLUE      = (59, 130, 246)
AMBER     = (245, 158, 11)
PURPLE    = (167, 139, 250)
RED       = (239, 68, 68)
ACCENT    = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):          return ImageFont.truetype(FONT_PATH, size, index=4)

def make_base():
    img  = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    draw.rectangle([0, 0, W, 4], fill=ACCENT)
    draw.rectangle([0, 0, 4, H], fill=ACCENT)
    return img, ImageDraw.Draw(img)

def box(draw, x1, y1, x2, y2, fill, outline=None, radius=7):
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill)
    if outline:
        draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, outline=outline, width=1)

def footer(draw, left, right):
    draw.line([(8, H-44), (W-8, H-44)], fill=DARK_GRAY, width=1)
    draw.text((16,   H-30), left,  font=font(16), fill=GRAY)
    draw.text((W-460,H-30), right, font=bold(16), fill=ACCENT)

def make_main():
    img, draw = make_base()

    # ── 헤더 (얇게) ──
    draw.rectangle([0, 4, W, 52], fill=(14, 18, 26))
    draw.text((16, 10), "LITE  Lumentum — 미즈호 테크 컨퍼런스 2026.06.09", font=bold(28), fill=WHITE)
    draw.text((820, 14), "CPO 광학 섹터 타임라인 최전선", font=font(18), fill=CYAN)
    draw.line([(0, 52), (W, 52)], fill=DARK_GRAY, width=1)

    PAD = 6
    TOP = 58
    BOT = H - 48

    # ── 3단 레이아웃 ──
    C1X1, C1X2 = PAD, 430
    C2X1, C2X2 = 436, 840
    C3X1, C3X2 = 846, W - PAD

    # ════════════════════════════════
    # 컬럼 1 — Scale-Out vs Scale-Up
    # ════════════════════════════════

    # Scale-Out
    box(draw, C1X1, TOP, C1X2, TOP+152, (12,22,16))
    draw.rectangle([C1X1, TOP, C1X1+5, TOP+152], fill=GREEN)
    draw.text((C1X1+14, TOP+8),  "Scale-Out  —  지금 돈 버는 구간", font=bold(16), fill=GREEN)
    draw.text((C1X1+14, TOP+36), "서버 ↔ 서버  노드 간 연결", font=font(14), fill=GRAY)
    draw.line([(C1X1+14, TOP+58),(C1X2-10, TOP+58)], fill=DARK_GRAY, width=1)
    draw.text((C1X1+14, TOP+66), "수주잔고",       font=font(13), fill=GRAY)
    draw.text((C1X1+130,TOP+64), "수십억 달러 이미 진행",  font=bold(14), fill=WHITE)
    draw.text((C1X1+14, TOP+96), "EML 레이저",     font=font(13), fill=GRAY)
    draw.text((C1X1+130,TOP+94), "YoY +50%+  2026.12",     font=bold(14), fill=GREEN)
    draw.text((C1X1+14, TOP+126),"타임라인",        font=font(13), fill=GRAY)
    draw.text((C1X1+130,TOP+124),"진행 중",                 font=bold(14), fill=WHITE)

    # Scale-Up
    box(draw, C1X1, TOP+158, C1X2, TOP+320, (12,18,28))
    draw.rectangle([C1X1, TOP+158, C1X1+5, TOP+320], fill=BLUE)
    draw.text((C1X1+14, TOP+166), "Scale-Up  —  다음 물결", font=bold(16), fill=BLUE)
    draw.text((C1X1+14, TOP+194), "칩 ↔ 광 직접 통합  노드 내", font=font(14), fill=GRAY)
    draw.line([(C1X1+14, TOP+216),(C1X2-10, TOP+216)], fill=DARK_GRAY, width=1)
    draw.text((C1X1+14, TOP+224), "TAM",            font=font(13), fill=GRAY)
    draw.text((C1X1+130,TOP+222), "$5B+ 증분 수익",          font=bold(14), fill=BLUE)
    draw.text((C1X1+14, TOP+254), "출하 시작",      font=font(13), fill=GRAY)
    draw.text((C1X1+130,TOP+252), "2027 H2",                  font=bold(14), fill=WHITE)
    draw.text((C1X1+14, TOP+284), "본격 램프",      font=font(13), fill=GRAY)
    draw.text((C1X1+130,TOP+282), "2028",                     font=bold(14), fill=WHITE)

    # OCS
    box(draw, C1X1, TOP+326, C1X2, TOP+418, (18,14,28))
    draw.rectangle([C1X1, TOP+326, C1X1+5, TOP+418], fill=PURPLE)
    draw.text((C1X1+14, TOP+334), "OCS  —  세 번째 카테고리", font=bold(16), fill=PURPLE)
    draw.text((C1X1+14, TOP+362), "광학 회로 스위치  전기→광학 라우팅", font=font(14), fill=GRAY)
    draw.text((C1X1+14, TOP+390), "데이터센터 진입",font=font(13), fill=GRAY)
    draw.text((C1X1+130,TOP+388), "2026 H2 시작",             font=bold(14), fill=PURPLE)

    # 핵심 발언 박스
    box(draw, C1X1, TOP+424, C1X2, BOT, (20,18,12), outline=AMBER)
    draw.text((C1X1+14, TOP+434), "경영진 발언", font=bold(14), fill=AMBER)
    draw.text((C1X1+14, TOP+458), '"수요가 있다는 건 명확하다"', font=bold(15), fill=WHITE)
    draw.text((C1X1+14, TOP+484), '"문제는 실행이다"',           font=bold(15), fill=WHITE)
    draw.text((C1X1+14, TOP+512), "리스크: 수요 불확실성 → 생산 스케일링", font=font(13), fill=AMBER)

    # ════════════════════════════════
    # 컬럼 2 — 재무 + 하이퍼스케일러
    # ════════════════════════════════

    # 재무 지표
    box(draw, C2X1, TOP, C2X2, TOP+246, (14,16,24))
    draw.text((C2X1+14, TOP+8), "재무 방향", font=bold(17), fill=CYAN)
    fin_rows = [
        ("현재 분기 매출",    "~$1B",      WHITE),
        ("목표 분기 매출",    "$2B",        CYAN),
        ("목표 영업이익률",   "40%",        CYAN),
        ("달성 기간",         "18~24개월",  GRAY),
        ("Q3 영업이익률",     "32.2%",      GREEN),
        ("Q4 가이던스 OPM",   "35~36%",     GREEN),
    ]
    ry = TOP + 40
    for label, val, color in fin_rows:
        draw.text((C2X1+14, ry),   label, font=font(13), fill=GRAY)
        draw.text((C2X1+200, ry),  val,   font=bold(16), fill=color)
        ry += 32

    # 하이퍼스케일러 박스
    box(draw, C2X1, TOP+252, C2X2, TOP+418, (16,20,14))
    draw.rectangle([C2X1, TOP+252, C2X1+5, TOP+418], fill=GREEN)
    draw.text((C2X1+14, TOP+260), "왜 이번이 다른가", font=bold(16), fill=GREEN)
    draw.text((C2X1+14, TOP+290), "고객이 달라졌다", font=font(14), fill=GRAY)
    draw.line([(C2X1+14, TOP+312),(C2X2-10, TOP+312)], fill=DARK_GRAY, width=1)
    draw.text((C2X1+14, TOP+320), "과거",  font=font(13), fill=GRAY)
    draw.text((C2X1+80, TOP+318), "통신사  —  수요 예측 불안정",  font=font(14), fill=GRAY)
    draw.text((C2X1+14, TOP+350), "현재",  font=font(13), fill=GREEN)
    draw.text((C2X1+80, TOP+348), "구글·아마존·MS 직납",         font=bold(14), fill=WHITE)
    draw.text((C2X1+14, TOP+380), "백로그", font=font(13), fill=GRAY)
    draw.text((C2X1+80, TOP+378), "$2조  공개 약속·집행",         font=bold(14), fill=GREEN)

    # Greensboro 팹
    box(draw, C2X1, TOP+424, C2X2, BOT, (18,16,24), outline=BLUE)
    draw.text((C2X1+14, TOP+434), "Greensboro 팹", font=bold(15), fill=BLUE)
    draw.text((C2X1+14, TOP+460), "InP 레이저 자체 생산 팹", font=font(14), fill=GRAY)
    draw.text((C2X1+14, TOP+486), "2028년 초 라인 스타트",    font=bold(14), fill=WHITE)
    draw.text((C2X1+14, TOP+512), "Scale-Up CPO 캐파 확보 목적", font=font(13), fill=GRAY)

    # ════════════════════════════════
    # 컬럼 3 — 공급망 + 섹터 함의
    # ════════════════════════════════

    # 공급망 레이어
    box(draw, C3X1, TOP, C3X2, TOP+290, (14,16,22))
    draw.text((C3X1+14, TOP+8), "InP 공급망 레이어", font=bold(16), fill=CYAN)

    chain = [
        (GRAY,   "InP 기판",       "단결정 원재료"),
        (BLUE,   "InP 에피웨이퍼", "레이저 구조 층 증착"),
        (PURPLE, "InP 레이저 칩",  "팹 공정 → 발광 소자"),
        (CYAN,   "CPO 모듈",       "최종 집적 납품"),
    ]
    cy = TOP + 42
    for i, (color, label, desc) in enumerate(chain):
        box(draw, C3X1+10, cy, C3X2-10, cy+46, (18,20,30))
        draw.rectangle([C3X1+10, cy, C3X1+15, cy+46], fill=color)
        draw.text((C3X1+24, cy+6),  label, font=bold(14), fill=color)
        draw.text((C3X1+24, cy+26), desc,  font=font(12), fill=GRAY)
        if i < 3:
            draw.text((C3X1+14, cy+50), "↓", font=bold(13), fill=DARK_GRAY)
        cy += 58

    # EML 신호 전달 박스
    box(draw, C3X1, TOP+296, C3X2, TOP+390, (20,18,12), outline=AMBER)
    draw.text((C3X1+14, TOP+304), "EML +50% 신호 전달 방향", font=bold(14), fill=AMBER)
    draw.text((C3X1+14, TOP+330), "루멘텀(모듈) 수요", font=font(13), fill=GRAY)
    draw.text((C3X1+14, TOP+352), "→ 레이저칩 → 에피웨이퍼", font=font(13), fill=WHITE)
    draw.text((C3X1+14, TOP+370), "순서대로 업스트림에 전달", font=font(13), fill=AMBER)

    # 섹터 함의
    box(draw, C3X1, TOP+396, C3X2, BOT, (12,22,16), outline=GREEN)
    draw.text((C3X1+14, TOP+406), "섹터 함의", font=bold(15), fill=GREEN)
    points = [
        "수요 가시성 — 업계 최상단에서 확인",
        "2026 H2  Scale-Out 가속",
        "2027~28  Scale-Up 본격화",
        "OCS 신규 카테고리 추가",
    ]
    py = TOP + 432
    for pt in points:
        draw.text((C3X1+14, py), f"· {pt}", font=font(13), fill=WHITE)
        py += 26

    footer(draw, "2026.06.10  Mizuho Technology Conference", "LITE  ·  CPO  ·  OCS  ·  InP")

    out = os.path.join(OUT_DIR, "2026-06-10_LITE_CPO전체.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
