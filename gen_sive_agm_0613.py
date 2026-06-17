from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-14"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (10, 12, 18)
GRID      = (255, 255, 255, 10)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 56, 70)
BLUE      = (59, 130, 246)
GREEN     = (52, 211, 153)
RED       = (239, 68, 68)
AMBER     = (245, 158, 11)
CYAN      = (6, 182, 212)
PURPLE    = (167, 139, 250)
ACCENT    = AMBER

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
    draw.rounded_rectangle([x1,y1,x2,y2], radius=radius, fill=fill)
    if outline:
        draw.rounded_rectangle([x1,y1,x2,y2], radius=radius, outline=outline, width=1)

def footer(draw, left, right):
    draw.line([(8, H-46), (W-8, H-46)], fill=DARK_GRAY, width=1)
    draw.text((16,   H-30), left,  font=font(16), fill=GRAY)
    draw.text((W-430,H-30), right, font=bold(16), fill=ACCENT)

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.rectangle([0, 4, W, 56], fill=(18, 14, 8))
    draw.text((16, 10), "SIVE  Sivers Semiconductors — 주주총회 D-1", font=bold(30), fill=WHITE)
    draw.text((16, 46), "AGM 6.15  /  나스닥 이중상장 분기점  /  5384만주 신주 발행 권한 승인 안건", font=font(15), fill=GRAY)
    draw.line([(0,56),(W,56)], fill=DARK_GRAY, width=1)

    # ── 5384만주 흐름 체인 ──
    CHAIN_Y = 62
    NODE_H  = 80
    nodes = [
        (AMBER,  "AGM",      "6.15",      "내일 표결"),
        (AMBER,  "5384만주", "신주 권한", "이사회 부여"),
        (CYAN,   "나스닥",   "이중상장",  "미국 유통물량"),
        (RED,    "희석",     "최대 15%",  "기존 주주"),
        (GREEN,  "통과 시",  "상장 경로", "열림"),
    ]
    n = len(nodes)
    node_w = (W - 32) // n

    for i, (color, label, val, sub) in enumerate(nodes):
        x1 = 16 + i * node_w
        x2 = x1 + node_w - 8
        cx = (x1 + x2) // 2
        box(draw, x1, CHAIN_Y, x2, CHAIN_Y + NODE_H, (18, 14, 8), outline=color)
        draw.text((cx - len(label)*5, CHAIN_Y + 6),  label, font=bold(14), fill=color)
        tw = len(val) * 8
        draw.text((cx - tw//2,        CHAIN_Y + 28), val,   font=bold(18), fill=WHITE)
        draw.text((cx - len(sub)*4,   CHAIN_Y + 56), sub,   font=font(11), fill=GRAY)
        if i < n - 1:
            draw.text((x2 + 4, CHAIN_Y + NODE_H//2 - 10), "→", font=bold(18), fill=DARK_GRAY)

    PAD = 6
    TOP = CHAIN_Y + NODE_H + 8
    BOT = H - 50
    DIV = 620

    # ════ 왼쪽 — 4가지 안건 ════
    box(draw, PAD, TOP, DIV-PAD, BOT, (14, 12, 8))
    draw.rectangle([PAD, TOP, PAD+4, BOT], fill=AMBER)
    draw.text((PAD+14, TOP+8), "주총 안건 전체", font=bold(16), fill=AMBER)
    draw.line([(PAD+14, TOP+32),(DIV-PAD-8, TOP+32)], fill=DARK_GRAY, width=1)

    # 안건 1 — 핵심
    box(draw, PAD+8, TOP+40, DIV-PAD-8, TOP+148, (22, 18, 8), outline=AMBER)
    draw.rectangle([PAD+8, TOP+40, PAD+12, TOP+148], fill=AMBER)
    draw.text((PAD+20, TOP+46), "안건 ①  5384만주 신주 발행 권한 부여", font=bold(13), fill=AMBER)
    draw.text((PAD+20, TOP+68), "목적  →  나스닥 이중상장용 미국 유통 주식 생성", font=font(12), fill=WHITE)
    draw.text((PAD+20, TOP+88), "구조  →  이사회에 권한만 부여  /  즉시 전량 발행 아님", font=font(12), fill=GRAY)
    draw.text((PAD+20, TOP+108), "희석  →  발행 시 기존 주주 최대 ~15% 지분율 하락", font=font(12), fill=RED)
    draw.text((PAD+20, TOP+128), "부결 시  →  나스닥 상장 경로 차단  /  재료 소멸", font=bold(12), fill=AMBER)

    # 안건 2 — 스톡옵션
    box(draw, PAD+8, TOP+154, DIV-PAD-8, TOP+238, (16, 16, 22), outline=PURPLE)
    draw.rectangle([PAD+8, TOP+154, PAD+12, TOP+238], fill=PURPLE)
    draw.text((PAD+20, TOP+160), "안건 ②  장기 인센티브 스톡옵션  700만주", font=bold(13), fill=PURPLE)
    draw.text((PAD+20, TOP+182), "CEO 100만주  /  행사가 VWAP 110%  /  3년 분할 행사", font=font(12), fill=GRAY)
    draw.text((PAD+20, TOP+202), "⚠  90% 이상 찬성 필요  —  높은 문턱  →  경영진 신뢰 바로미터", font=bold(12), fill=PURPLE)
    draw.text((PAD+20, TOP+222), "주가가 부여 시점 +10% 이상 올라야 경영진 수익 발생", font=font(11), fill=GRAY)

    # 안건 3,4
    box(draw, PAD+8, TOP+244, DIV-PAD-8, TOP+318, (14, 18, 14), outline=GREEN)
    draw.rectangle([PAD+8, TOP+244, PAD+12, TOP+318], fill=GREEN)
    draw.text((PAD+20, TOP+250), "안건 ③  Bootstrap Europe 전환사채 32.7만달러 추가", font=bold(12), fill=GREEN)
    draw.text((PAD+20, TOP+270), "연 10.85%  /  전환가 4.77 SEK  /  3월 1200만달러 계약의 잔여분", font=font(11), fill=GRAY)
    draw.line([(PAD+20, TOP+292),(DIV-PAD-10, TOP+292)], fill=DARK_GRAY, width=1)
    draw.text((PAD+20, TOP+298), "안건 ④  무배당 유지  —  전액 재투자 정책 지속", font=bold(12), fill=GRAY)

    # ════ 오른쪽 — 리스크 + 체크포인트 ════
    RX = DIV + PAD

    # 리스크 박스
    box(draw, RX, TOP, W-PAD, TOP+238, (18, 10, 10), outline=RED)
    draw.rectangle([RX, TOP, RX+4, TOP+238], fill=RED)
    draw.text((RX+14, TOP+8), "주총 전 알아야 할 리스크", font=bold(15), fill=RED)
    draw.line([(RX+14, TOP+32),(W-PAD-8, TOP+32)], fill=DARK_GRAY, width=1)

    risks = [
        (RED,   "스웨덴 검찰 형사조사",
                "나스닥 발표 48시간 전 주가 급등  /  정보 유출 의혹"),
        (AMBER, "숏셀러 Ningi Research 공격",
                "2025 매출 31% 의심  /  연구보조금→상업매출 분류 주장"),
        (RED,   "내부자 전량 매도",
                "이사 Achilles Capital 2900만주 전부 매도  /  3개월 매수 0건"),
    ]
    ry = TOP + 40
    for color, title, desc in risks:
        box(draw, RX+8, ry, W-PAD-8, ry+56, (22, 14, 14))
        draw.rectangle([RX+8, ry, RX+12, ry+56], fill=color)
        draw.text((RX+20, ry+6),  title, font=bold(12), fill=color)
        draw.text((RX+20, ry+28), desc,  font=font(11), fill=GRAY)
        ry += 62

    # 체크포인트 박스
    box(draw, RX, TOP+244, W-PAD, BOT, (10, 18, 16), outline=CYAN)
    draw.rectangle([RX, TOP+244, RX+4, BOT], fill=CYAN)
    draw.text((RX+14, TOP+252), "6.15 이후 볼 것", font=bold(15), fill=CYAN)
    draw.line([(RX+14, TOP+276),(W-PAD-8, TOP+276)], fill=DARK_GRAY, width=1)

    checks = [
        (GREEN,  "5384만주 통과", "나스닥 경로 유지  /  상장 준비 구체화"),
        (RED,    "5384만주 부결", "나스닥 차단  /  밸류에이션 재조정"),
        (PURPLE, "옵션 90% 여부", "경영진 신뢰도 지표  /  통과율 수치 확인"),
        (AMBER,  "형사조사 진행", "상장 심사와 병행  /  결과 연동 리스크"),
    ]
    cy = TOP + 284
    for color, title, desc in checks:
        draw.text((RX+14, cy),    f"· {title}", font=bold(12), fill=color)
        draw.text((RX+14, cy+18), f"  {desc}",  font=font(11), fill=GRAY)
        cy += 40

    footer(draw, "2026.06.14  SIVE AGM 주주총회 D-1 분석", "SIVE  ·  Nasdaq  ·  5384만주  ·  이중상장")

    out = os.path.join(OUT_DIR, "2026-06-14_SIVE_AGM주총.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
