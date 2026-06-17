from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-13"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (8, 10, 16)
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
    draw.rectangle([0, 4, W, 56], fill=(8, 16, 22))
    draw.text((16, 10), "SPCX  SpaceX — 상장 첫날 결과 & 앞으로 볼 것들", font=bold(30), fill=WHITE)
    draw.text((16, 46), "6.12 Nasdaq 상장  /  역대 최대 IPO $750억  /  개인 배정 30%  /  기관 2배 초과청약", font=font(15), fill=GRAY)
    draw.line([(0,56),(W,56)], fill=DARK_GRAY, width=1)

    # ── 가격 체인 노드 ──
    CHAIN_Y = 62
    NODE_H  = 80
    nodes = [
        (GRAY,   "공모가",  "$135",   "IPO 고정"),
        (CYAN,   "시초가",  "$150",   "+11%"),
        (GREEN,  "종가",    "$161",   "+19%"),
        (AMBER,  "장중고가","$176",   "장중 최고"),
        (PURPLE, "시총",    "$2.1조", "상장일 기준"),
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
        draw.text((cx - len(sub)*4,   CHAIN_Y + 56), sub,   font=font(12), fill=GRAY)
        if i < n - 1:
            draw.text((x2 + 4, CHAIN_Y + NODE_H//2 - 10), "→", font=bold(18), fill=DARK_GRAY)

    # ── 하단 2분할 ──
    PAD = 6
    TOP = CHAIN_Y + NODE_H + 8   # 150
    BOT = H - 50                  # 670
    DIV = 580

    # ════ 왼쪽 ════

    # 상장 팩트 박스
    box(draw, PAD, TOP, DIV-PAD, TOP+168, (10, 18, 22), outline=CYAN)
    draw.rectangle([PAD, TOP, PAD+4, TOP+168], fill=CYAN)
    draw.text((PAD+14, TOP+8), "상장 팩트", font=bold(15), fill=CYAN)
    draw.line([(PAD+14, TOP+32),(DIV-PAD-8, TOP+32)], fill=DARK_GRAY, width=1)

    facts = [
        ("조달 규모",    "$750억",      "역대 최대 IPO 기록",          WHITE),
        ("기관 수요",    "2배 초과청약", "수요 확인 완료",              GREEN),
        ("개인 배정",    "30%",         "소매 투자자 배정 이례적 고비율", AMBER),
        ("상장 시총",    "$2.1조",      "상장일 종가 기준",             WHITE),
        ("재무 현황",    "GAAP 손실",   "영업손실 $26억  EBITDA +$66억",RED),
    ]
    ry = TOP + 40
    for label, val, note, color in facts:
        draw.text((PAD+14,  ry), label, font=font(12), fill=GRAY)
        draw.text((PAD+110, ry), val,   font=bold(14), fill=color)
        draw.text((PAD+250, ry), note,  font=font(11), fill=GRAY)
        ry += 26

    # 소송·이슈 박스
    box(draw, PAD, TOP+174, DIV-PAD, BOT, (18, 14, 12), outline=AMBER)
    draw.rectangle([PAD, TOP+174, PAD+4, BOT], fill=AMBER)
    draw.text((PAD+14, TOP+182), "상장 전 소송  —  노이즈 vs 리스크", font=bold(14), fill=AMBER)
    draw.line([(PAD+14, TOP+204),(DIV-PAD-8, TOP+204)], fill=DARK_GRAY, width=1)

    draw.text((PAD+14, TOP+212), "6.09  환경단체 연방법원 소송 제기", font=bold(13), fill=AMBER)
    draw.text((PAD+14, TOP+232), "텍사스 Starbase 발사장 확장 토지교환 무효화 시도", font=font(12), fill=GRAY)
    draw.text((PAD+14, TOP+252), "FWS 6.01 승인 완료  /  트럼프 행정부 뒤집기 기준 매우 높음", font=font(12), fill=WHITE)

    draw.line([(PAD+14, TOP+274),(DIV-PAD-8, TOP+274)], fill=DARK_GRAY, width=1)
    draw.text((PAD+14, TOP+282), "판단  →  발사 허가와 별개  /  Falcon 9·Starship 운용 즉각 영향 없음", font=font(12), fill=GRAY)
    draw.text((PAD+14, TOP+302), "실질 리스크  →  Starbase 부지 확장 수개월 지연 가능성", font=bold(12), fill=AMBER)
    draw.text((PAD+14, TOP+322), "소송 자체보다 아래 5가지가 주가에 더 영향을 준다", font=font(12), fill=GRAY)

    # ════ 오른쪽 ════
    RX = DIV + PAD

    box(draw, RX, TOP, W-PAD, BOT, (12, 14, 20))
    draw.rectangle([RX, TOP, RX+4, BOT], fill=CYAN)
    draw.text((RX+14, TOP+8), "앞으로 볼 것들", font=bold(17), fill=CYAN)
    draw.line([(RX+14, TOP+34),(W-PAD-8, TOP+34)], fill=DARK_GRAY, width=1)

    watches = [
        (RED,    "① 머스크 락업 해제",
                 "지분 40%  /  락업 해제 일정 확인 필수  /  매각 시 최강 하방 압력"),
        (AMBER,  "② 개인 30% 물량 소화",
                 "소매 비율 높을수록 초기 변동성 확대  /  첫 주 거래량 패턴 확인"),
        (GREEN,  "③ S&P 500 편입 요건",
                 "4분기 연속 GAAP 흑자 필요  /  현재 손실 구조  /  편입 시 패시브 강제 수요"),
        (CYAN,   "④ Starship 상업화 일정",
                 "상업 발사 시작 = 수익 구조 전환  /  단가 Falcon 9 대비 대폭 절감"),
        (PURPLE, "⑤ Starlink 가입자 성장",
                 "분기 구독자 수·ARPU가 흑자 전환 속도 결정  /  꺾이면 밸류 논리 흔들림"),
    ]
    wy = TOP + 44
    for color, title, desc in watches:
        box(draw, RX+10, wy, W-PAD-8, wy+72, (18, 18, 28))
        draw.rectangle([RX+10, wy, RX+14, wy+72], fill=color)
        draw.text((RX+22, wy+8),  title, font=bold(14), fill=color)
        draw.text((RX+22, wy+34), desc,  font=font(11), fill=GRAY)
        wy += 78

    footer(draw, "2026.06.13  SpaceX SPCX IPO 첫날 결과", "SPCX  ·  Nasdaq  ·  Starlink  ·  Starship")

    out = os.path.join(OUT_DIR, "2026-06-13_SPCX_IPO상장.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
