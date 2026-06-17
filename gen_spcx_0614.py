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

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):          return ImageFont.truetype(FONT_PATH, size, index=4)

def make_base():
    img  = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    draw.rectangle([0, 0, W, 4], fill=AMBER)
    draw.rectangle([0, 0, 4, H], fill=AMBER)
    return img, ImageDraw.Draw(img)

def box(draw, x1, y1, x2, y2, fill, outline=None, radius=7):
    draw.rounded_rectangle([x1,y1,x2,y2], radius=radius, fill=fill)
    if outline:
        draw.rounded_rectangle([x1,y1,x2,y2], radius=radius, outline=outline, width=1)

def footer(draw, left, right):
    draw.line([(8, H-46), (W-8, H-46)], fill=DARK_GRAY, width=1)
    draw.text((16,   H-30), left,  font=font(16), fill=GRAY)
    draw.text((W-320,H-30), right, font=bold(16), fill=AMBER)

def make_card():
    img, draw = make_base()

    # ── 헤더 ──
    draw.rectangle([0, 4, W, 62], fill=(14, 16, 22))
    draw.text((16, 10), "SpaceX (SPCX)  —  주가가 흔들릴 수 있는 이유", font=bold(28), fill=WHITE)
    draw.text((16, 46), "Anthropic 임대 이슈  +  CFRA 매도 리포트  /  2026.06.14", font=font(14), fill=GRAY)
    draw.line([(0,62),(W,62)], fill=DARK_GRAY, width=1)

    PAD = 8
    TOP = 68
    BOT = H - 52
    DIV = 596

    # ══════════════════════════════
    # 왼쪽 — 이슈 정리
    # ══════════════════════════════

    # Bloomberg 보도
    box(draw, PAD, TOP, DIV-PAD, TOP+38, (18, 16, 10), outline=AMBER)
    draw.rectangle([PAD, TOP, PAD+4, TOP+38], fill=AMBER)
    draw.text((PAD+14, TOP+8), "Bloomberg 보도", font=bold(15), fill=AMBER)

    lines_bloomberg = [
        "Memphis Colossus 1 (텍사스 AI 데이터센터)",
        "전체 용량을 Anthropic에 임대",
        "내부 팀의 지연시간·최적화 문제가 원인",
    ]
    by = TOP + 46
    for line in lines_bloomberg:
        draw.text((PAD+14, by), f"· {line}", font=font(13), fill=WHITE)
        by += 22

    # Anthropic 임대 구조
    by += 6
    box(draw, PAD, by, DIV-PAD, by+34, (10, 18, 24), outline=CYAN)
    draw.rectangle([PAD, by, PAD+4, by+34], fill=CYAN)
    draw.text((PAD+14, by+8), "임대 계약 구조", font=bold(14), fill=CYAN)
    cy = by + 42
    contract_lines = [
        "기간 180일  /  90일 전 해지 통보 가능",
        "SpaceX가 준비되면 언제든 회수 가능",
        "\"망한 것\" 아님 — 비어있는 동안 수익화",
    ]
    for line in contract_lines:
        draw.text((PAD+14, cy), f"· {line}", font=font(13), fill=CYAN)
        cy += 22

    # Starship 한 줄 설명
    cy += 8
    box(draw, PAD, cy, DIV-PAD, cy+60, (16, 12, 20), outline=PURPLE)
    draw.rectangle([PAD, cy, PAD+4, cy+60], fill=PURPLE)
    draw.text((PAD+14, cy+6), "Starship이란", font=bold(14), fill=PURPLE)
    draw.text((PAD+14, cy+28), "높이 120m 초대형 재사용 로켓  /  NASA 달 착륙선 선정", font=font(13), fill=WHITE)
    draw.text((PAD+14, cy+46), "아직 상업 발사 미시작  →  수익화 시점이 핵심 리스크", font=font(13), fill=GRAY)

    # ══════════════════════════════
    # 오른쪽 — CFRA 리포트 + 확인사항
    # ══════════════════════════════
    RX = DIV + PAD

    # CFRA 박스
    box(draw, RX, TOP, W-PAD, TOP+38, (24, 10, 10), outline=RED)
    draw.rectangle([RX, TOP, RX+4, TOP+38], fill=RED)
    draw.text((RX+14, TOP+8), "CFRA  매도(Sell)  리포트", font=bold(15), fill=RED)

    draw.text((RX+14, TOP+46), "목표가", font=font(13), fill=GRAY)
    draw.text((RX+76, TOP+44), "$115", font=bold(22), fill=RED)
    draw.text((RX+148, TOP+46), "vs  현재가", font=font(13), fill=GRAY)
    draw.text((RX+248, TOP+44), "$160.95", font=bold(22), fill=WHITE)
    draw.text((RX+390, TOP+46), "▼ 29% 하방", font=bold(14), fill=RED)

    # 4가지 우려
    ry = TOP + 84
    box(draw, RX, ry, W-PAD, ry+32, (20, 14, 10), outline=AMBER)
    draw.rectangle([RX, ry, RX+4, ry+32], fill=AMBER)
    draw.text((RX+14, ry+8), "핵심 우려  4가지", font=bold(14), fill=AMBER)

    concerns = [
        (RED,    "밸류에이션 과도  —  미래 옵션 대부분 선반영"),
        (AMBER,  "Starship 상업화 지연 리스크"),
        (AMBER,  "Starlink 성장률·마진 기대치 과도"),
        (GRAY,   "AI 데이터센터 수익 아직 미검증"),
    ]
    ry2 = ry + 40
    for color, text in concerns:
        draw.text((RX+14, ry2), f"· {text}", font=font(13), fill=color)
        ry2 += 24

    # 앞으로 확인할 3가지
    ry2 += 8
    box(draw, RX, ry2, W-PAD, BOT, (12, 20, 14), outline=GREEN)
    draw.rectangle([RX, ry2, RX+4, BOT], fill=GREEN)
    draw.text((RX+14, ry2+8), "앞으로 확인할 3가지", font=bold(14), fill=GREEN)
    draw.line([(RX+14, ry2+30),(W-PAD-8, ry2+30)], fill=DARK_GRAY, width=1)

    checks = [
        "Starlink  가입자 수·ARPU·마진 유지 여부",
        "Starship  재사용·상업 발사 일정 준수 여부",
        "Anthropic 임대  →  반복 매출로 증명되는지",
    ]
    cy2 = ry2 + 38
    for i, text in enumerate(checks, 1):
        draw.text((RX+14, cy2), f"{i}.  {text}", font=font(13), fill=WHITE)
        cy2 += 26

    footer(draw, "2026.06.14  SpaceX(SPCX) 이슈 정리", "개인 공부 기록")

    out = os.path.join(OUT_DIR, "2026-06-14_SPCX_주가흔들릴수있는이유.png")
    img.save(out)
    print(f"Saved: {out}")

make_card()
print("Done.")
