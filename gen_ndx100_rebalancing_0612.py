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
    draw.text((W-420,H-30), right, font=bold(16), fill=ACCENT)

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.rectangle([0, 4, W, 56], fill=(10, 16, 24))
    draw.text((16, 10), "나스닥 100  6월 리밸런싱 — AI 인프라 IN / 레거시 OUT", font=bold(27), fill=WHITE)
    draw.text((16, 44), "2026.06.22 효력 발생  /  QQQ $3,000억 패시브 강제 매수", font=font(14), fill=GRAY)
    draw.line([(0,56),(W,56)], fill=DARK_GRAY, width=1)

    PAD = 6
    TOP = 62
    BOT = H - 52
    DIV = 580

    # ══════════════════════
    # 왼쪽 — 편입
    # ══════════════════════
    box(draw, PAD, TOP, DIV-PAD, TOP+42, (10, 22, 14), outline=GREEN)
    draw.rectangle([PAD, TOP, PAD+4, TOP+42], fill=GREEN)
    draw.text((PAD+14, TOP+8),  "편입  5종", font=bold(16), fill=GREEN)
    draw.text((PAD+120, TOP+10), "6월 22일 QQQ 강제 매수 대상", font=font(13), fill=GRAY)

    entries = [
        ("ALAB", "Astera Labs",    "AI 데이터센터 연결 칩 (PCIe·CXL 스위치)",   GREEN),
        ("CRWV", "CoreWeave",      "GPU 클라우드 인프라  /  MS 최대 고객",       GREEN),
        ("NBIS", "Nebius Group",   "AI 클라우드 플랫폼  /  구 Yandex 클라우드", GREEN),
        ("RKLB", "Rocket Lab",     "소형 발사체 + 우주시스템  /  NDX 100 첫 우주주",  CYAN),
        ("TER",  "Teradyne",       "반도체 테스트 장비  /  AI·HBM 칩 테스트",   GREEN),
    ]
    ey = TOP + 50
    for ticker, name, desc, color in entries:
        box(draw, PAD+8, ey, DIV-PAD-6, ey+46, (12, 20, 14))
        draw.rectangle([PAD+8, ey, PAD+12, ey+46], fill=color)
        draw.text((PAD+20, ey+5),  ticker, font=bold(16), fill=color)
        draw.text((PAD+80, ey+6),  name,   font=bold(13), fill=WHITE)
        draw.text((PAD+20, ey+28), desc,   font=font(12), fill=GRAY)
        ey += 52

    # ══════════════════════
    # 오른쪽 — 편출 + 경향성
    # ══════════════════════
    RX = DIV + PAD

    box(draw, RX, TOP, W-PAD, TOP+42, (22, 10, 10), outline=RED)
    draw.rectangle([RX, TOP, RX+4, TOP+42], fill=RED)
    draw.text((RX+14, TOP+8),  "편출  5종", font=bold(16), fill=RED)
    draw.text((RX+120, TOP+10), "6월 22일 QQQ 강제 매도 대상", font=font(13), fill=GRAY)

    exits = [
        ("CHTR", "Charter Comms",  "케이블 통신  →  레거시"),
        ("CTSH", "Cognizant",      "전통 IT 아웃소싱  →  레거시"),
        ("INSM", "Insmed",         "바이오  /  편입 6개월 만에 편출"),
        ("VRSK", "Verisk Analytics","보험·리스크 데이터  →  레거시"),
        ("ZS",   "Zscaler",        "클라우드 보안  /  성장 둔화"),
    ]
    xy = TOP + 50
    for ticker, name, desc in exits:
        box(draw, RX+6, xy, W-PAD-6, xy+46, (22, 12, 12))
        draw.rectangle([RX+6, xy, RX+10, xy+46], fill=RED)
        draw.text((RX+18, xy+5),  ticker, font=bold(16), fill=RED)
        draw.text((RX+76, xy+6),  name,   font=bold(13), fill=WHITE)
        draw.text((RX+18, xy+28), desc,   font=font(12), fill=GRAY)
        xy += 52

    # 경향성 요약 박스
    box(draw, RX, xy+4, W-PAD, BOT, (12, 16, 24), outline=CYAN)
    draw.rectangle([RX, xy+4, RX+4, BOT], fill=CYAN)
    draw.text((RX+14, xy+12), "핵심 경향성", font=bold(14), fill=CYAN)
    draw.line([(RX+14, xy+32),(W-PAD-8, xy+32)], fill=DARK_GRAY, width=1)

    trends = [
        (GREEN,  "AI 인프라가 레거시 IT를 밀어냄 — 같은 기술 섹터 내 구조 교체"),
        (CYAN,   "우주 섹터 공식 인정 — NDX 100 최초 순수 발사체 편입"),
        (AMBER,  "회전 가속 — 방법론 개편 후 6개월 만에 편출 가능"),
        (GRAY,   "S&P 500 차이: 4분기 GAAP 흑자 필수 / NDX 100: 흑자 요건 없음"),
    ]
    ty = xy + 40
    for color, text in trends:
        draw.text((RX+14, ty), f"· {text}", font=font(12), fill=color)
        ty += 22

    footer(draw, "2026.06.12  나스닥 100 리밸런싱 분석", "6월 22일 효력  ·  개인 공부 기록")

    out = os.path.join(OUT_DIR, "2026-06-12_NDX100_리밸런싱.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
