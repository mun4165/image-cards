from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-12"
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
ACCENT    = GREEN

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
    draw.text((W-460,H-30), right, font=bold(16), fill=ACCENT)

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.rectangle([0, 4, W, 56], fill=(10, 18, 14))
    draw.text((16, 10), "LPTH  LightPath Technologies — Secure America Act 연결고리", font=bold(30), fill=WHITE)
    draw.text((16, 46), "6.10 서명  $700억  /  CBP 기술 $34.5억  /  DHS C-UAS $15억  /  FY2029까지 예산 고정", font=font(15), fill=GRAY)
    draw.line([(0,56),(W,56)], fill=DARK_GRAY, width=1)

    # ── 공급망 체인 노드 ──
    CHAIN_Y = 62
    NODE_H  = 80
    nodes = [
        (AMBER,  "법안",      "$700억",   "Secure America Act"),
        (AMBER,  "CBP",       "$34.5억",  "기술·감시 인프라"),
        (CYAN,   "AST",       "723탑",    "Program of Record"),
        (CYAN,   "QuickSet",  "팬틸트",   "EO/IR  CBP 기존 납품"),
        (GREEN,  "LPTH",      "쿨드 IR",  "렌즈·카메라  포지션 확보"),
    ]
    n = len(nodes)
    total_w = W - 32
    node_w  = total_w // n

    for i, (color, label, val, sub) in enumerate(nodes):
        x1 = 16 + i * node_w
        x2 = x1 + node_w - 8
        cx = (x1 + x2) // 2
        box(draw, x1, CHAIN_Y, x2, CHAIN_Y + NODE_H, (14, 16, 26), outline=color)
        draw.text((cx - len(label)*5, CHAIN_Y + 6),  label, font=bold(14), fill=color)
        tw = len(val) * 9
        draw.text((cx - tw//2,        CHAIN_Y + 28), val,   font=bold(20), fill=WHITE)
        draw.text((cx - len(sub)*4,   CHAIN_Y + 56), sub,   font=font(11), fill=GRAY)
        if i < n - 1:
            draw.text((x2 + 4, CHAIN_Y + NODE_H//2 - 10), "→", font=bold(18), fill=DARK_GRAY)

    # ── 하단 2분할 ──
    PAD = 6
    TOP = CHAIN_Y + NODE_H + 8   # 150
    BOT = H - 50                  # 670
    DIV = 610

    # ════ 왼쪽 ════

    # 예산 분해 박스
    box(draw, PAD, TOP, DIV-PAD, TOP+162, (12, 18, 14), outline=AMBER)
    draw.text((PAD+14, TOP+8), "Secure America Act 예산 분해", font=bold(15), fill=AMBER)
    draw.line([(PAD+14, TOP+32),(DIV-PAD-8, TOP+32)], fill=DARK_GRAY, width=1)

    budget_rows = [
        ("ICE",           "$385억",     "이민 단속·구금 시설",          WHITE),
        ("CBP",           "$220~260억", "국경순찰·기술 인프라",          WHITE),
        ("DHS 기술",      "$34.5억",    "감시탑·광학 장비 직접 명시",    GREEN),
        ("DHS C-UAS",     "$15억",      "대드론 조달 비히클 신설",       GREEN),
        ("집행 기간",     "FY2029",     "트럼프 임기 말까지 예산 고정",  CYAN),
    ]
    ry = TOP + 40
    for label, val, note, color in budget_rows:
        draw.text((PAD+14,  ry), label, font=font(12), fill=GRAY)
        draw.text((PAD+145, ry), val,   font=bold(14), fill=color)
        draw.text((PAD+268, ry), note,  font=font(11), fill=GRAY)
        ry += 24

    # 공급 포지션 박스
    box(draw, PAD, TOP+168, DIV-PAD, BOT, (12, 14, 20), outline=CYAN)
    draw.text((PAD+14, TOP+176), "LPTH 공급 포지션  —  법안 이전부터 이미 자리 잡혀 있었다", font=bold(13), fill=CYAN)
    draw.line([(PAD+14, TOP+198),(DIV-PAD-8, TOP+198)], fill=DARK_GRAY, width=1)

    positions = [
        (GREEN, "Border Surveillance", "LWIR 렌즈  DHS 예산 배정 대기 → 이번 법안으로 해소"),
        (GREEN, "Counter-UAS  $30M",   "백로그 27%  SUADS 중심  C-UAS $15억 비히클과 직결"),
        (WHITE, "미공개 PO  $9.6M",    "Tier-1 방산 냉각형 IR  장거리 국경·감시 탐지 추정"),
        (BLUE,  "SPEIR  해군 파노라믹", "L3Harris prime  알레이버크급 수상함 전체 확대 예정"),
    ]
    py = TOP + 206
    for color, title, desc in positions:
        box(draw, PAD+8, py, DIV-PAD-8, py+44, (18, 20, 28))
        draw.rectangle([PAD+8, py, PAD+12, py+44], fill=color)
        draw.text((PAD+20, py+4),  title, font=bold(13), fill=color)
        draw.text((PAD+20, py+24), desc,  font=font(11), fill=GRAY)
        py += 50

    draw.line([(PAD+14, py+4),(DIV-PAD-8, py+4)], fill=DARK_GRAY, width=1)
    draw.text((PAD+14, py+12), "다음 체크  →", font=bold(12), fill=CYAN)
    draw.text((PAD+14, py+30), "DHS 예산 배정 공시  /  LPTH 확정 PO 발표  /  QuickSet M&A 움직임", font=font(12), fill=GRAY)

    # ════ 오른쪽 ════
    RX = DIV + PAD

    # QuickSet 연결 박스
    box(draw, RX, TOP, W-PAD, TOP+172, (14, 16, 24), outline=CYAN)
    draw.rectangle([RX, TOP, RX+4, TOP+172], fill=CYAN)
    draw.text((RX+14, TOP+8), "QuickSet — 같은 탑에 올라가는 팬틸트", font=bold(15), fill=CYAN)
    draw.line([(RX+14, TOP+32),(W-PAD-8, TOP+32)], fill=DARK_GRAY, width=1)

    qs_rows = [
        ("제품",   "MPT-50 / MPT-130  팬틸트 EO/IR"),
        ("고객",   "CBP  DHS  해병대  공군  해군  국무부"),
        ("프로그램", "CBP AST 723개  PoR  취소 어려운 다년 조달"),
        ("구조",   "LPTH 쿨드 IR 카메라  +  QuickSet 팬틸트  =  감시탑"),
        ("시사점", "같은 지붕 아래  →  수직통합 M&A 논리 성립"),
    ]
    qy = TOP + 40
    for label, val in qs_rows:
        draw.text((RX+14, qy), label, font=font(12), fill=GRAY)
        draw.text((RX+100, qy), val,  font=font(13), fill=WHITE)
        qy += 26

    # 인수 테제 박스
    box(draw, RX, TOP+178, W-PAD, BOT, (14, 22, 16), outline=GREEN)
    draw.rectangle([RX, TOP+178, RX+4, BOT], fill=GREEN)
    draw.text((RX+14, TOP+186), "인수 테제  —  양방향", font=bold(15), fill=GREEN)
    draw.line([(RX+14, TOP+210),(W-PAD-8, TOP+210)], fill=DARK_GRAY, width=1)

    acq_rows = [
        (CYAN,  "LPTH → QuickSet 인수",   "$60~200M  주식+부채 혼합  감시탑 수직통합"),
        (CYAN,  "LPTH → OpenWorks 인수",  "$30~60M  UK 기반  SkyWall CUAS 네트"),
        (AMBER, "LPTH 피인수 가능성",      "시총 $1.03B  Northrop / L3Harris 소화 가능"),
        (AMBER, "Northrop 이사 영입",      "Mark Caylor  前 Northrop MS 사장  2026.04 취임"),
    ]
    ay = TOP + 218
    for color, title, desc in acq_rows:
        draw.text((RX+14, ay),    title, font=bold(13), fill=color)
        draw.text((RX+14, ay+18), desc,  font=font(11), fill=GRAY)
        ay += 44

    footer(draw, "2026.06.12  LPTH × Secure America Act", "LPTH  ·  QuickSet  ·  CBP  ·  C-UAS")

    out = os.path.join(OUT_DIR, "2026-06-12_LPTH_SecureAmericaAct.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
