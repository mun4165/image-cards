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
ACCENT    = PURPLE

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
    draw.text((W-480,H-30), right, font=bold(16), fill=ACCENT)

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.rectangle([0, 4, W, 54], fill=(14, 12, 22))
    draw.text((16, 10), "SATL  Satellogic — ROTH 런던 컨퍼런스 프리뷰", font=bold(30), fill=WHITE)
    draw.text((16, 44), "CFO 퇴임 이후 첫 기관 대면  /  Roth Capital 코멘트 6.09  /  컨퍼런스 6.16~18", font=font(15), fill=GRAY)
    draw.line([(0,54),(W,54)], fill=DARK_GRAY, width=1)

    PAD = 6
    TOP = 60
    BOT = H - 50
    DIV = 590

    # ════════════════
    # 왼쪽
    # ════════════════

    # Roth Capital 코멘트 박스
    box(draw, PAD, TOP, DIV-PAD, TOP+172, (14,22,14), outline=GREEN)
    draw.text((PAD+14, TOP+8), "Roth Capital 코멘트  —  6.09", font=bold(15), fill=GREEN)
    draw.line([(PAD+14, TOP+34),(DIV-PAD-8, TOP+34)], fill=DARK_GRAY, width=1)

    roth = [
        ("레이팅",      "Buy 유지",           GREEN),
        ("목표주가",    "$15",                GREEN),
        ("업사이드",    "+71%  현재가 기준",  GREEN),
        ("발언",        '"orderly management transition"', WHITE),
        ("재확인",      "Merlin 2027 H1 배치 일정 유지", CYAN),
        ("추가 언급",   "국제 정부 계약 추가 기대",       CYAN),
    ]
    ry = TOP + 42
    for label, val, color in roth:
        draw.text((PAD+14,  ry), label, font=font(13), fill=GRAY)
        draw.text((PAD+110, ry), val,   font=bold(14), fill=color)
        ry += 22

    # 컨퍼런스 정보 박스
    box(draw, PAD, TOP+178, DIV-PAD, TOP+322, (16,14,26), outline=PURPLE)
    draw.rectangle([PAD, TOP+178, PAD+4, TOP+322], fill=PURPLE)
    draw.text((PAD+14, TOP+186), "컨퍼런스 정보", font=bold(15), fill=PURPLE)
    draw.line([(PAD+14, TOP+210),(DIV-PAD-8, TOP+210)], fill=DARK_GRAY, width=1)

    conf = [
        ("일정",   "6.16~18 (3일)"),
        ("장소",   "Four Seasons Hotel London at Park Lane"),
        ("주관",   "Roth Capital  —  16년째"),
        ("규모",   "80개+ 성장주 CEO  /  기관투자자 전용"),
        ("형식",   "40분 1-on-1 미팅"),
        ("SATL",  "CEO Kargieman + SVP Finance Driver"),
    ]
    cy = TOP + 218
    for label, val in conf:
        draw.text((PAD+14,  cy), label, font=font(13), fill=GRAY)
        draw.text((PAD+90,  cy), val,   font=font(14), fill=WHITE)
        cy += 22

    # Reg FD 박스
    box(draw, PAD, TOP+328, DIV-PAD, TOP+440, (22,16,12), outline=AMBER)
    draw.text((PAD+14, TOP+336), "Reg FD — 이 자리에서 새 정보가 안 나오는 이유", font=bold(14), fill=AMBER)
    draw.line([(PAD+14, TOP+358),(DIV-PAD-8, TOP+358)], fill=DARK_GRAY, width=1)
    draw.text((PAD+14, TOP+366), "SEC 규정상 중요 정보를 특정 투자자에게 먼저 말하면", font=font(13), fill=GRAY)
    draw.text((PAD+14, TOP+386), "즉시 전체 시장에 공시 의무. CEO가 하고 싶어도 법적으로 불가.", font=font(13), fill=WHITE)
    draw.text((PAD+14, TOP+410), "기관이 읽는 건 → 기존 가이던스를 얼마나 자신있게 말하냐", font=bold(13), fill=AMBER)

    # 체크포인트
    box(draw, PAD, TOP+446, DIV-PAD, BOT, (12,20,20), outline=CYAN)
    draw.text((PAD+14, TOP+454), "다음 체크포인트", font=bold(14), fill=CYAN)
    draw.line([(PAD+14, TOP+476),(DIV-PAD-8, TOP+476)], fill=DARK_GRAY, width=1)
    draw.text((PAD+14, TOP+484), "6.18+  Roth 애널리스트 takeaway 노트 미디어 공개", font=font(14), fill=WHITE)
    draw.text((PAD+14, TOP+508), "6.23   Northland Growth Conference  (온라인, Ryan Driver)", font=font(13), fill=GRAY)
    draw.line([(PAD+14, TOP+532),(DIV-PAD-8, TOP+532)], fill=DARK_GRAY, width=1)
    draw.text((PAD+14, TOP+540), "읽어야 할 것  →  CEO 답변 뉘앙스  /  Merlin 재확인 여부", font=font(13), fill=CYAN)
    draw.text((PAD+14, TOP+562), "CFO 공백 언급 방식  /  계약 파이프라인 구체성 수준", font=font(13), fill=GRAY)

    # ════════════════
    # 오른쪽 — 예상 질문
    # ════════════════
    RX = DIV + PAD

    box(draw, RX, TOP, W-PAD, BOT, (14,14,22))
    draw.rectangle([RX, TOP, RX+4, BOT], fill=PURPLE)
    draw.text((RX+14, TOP+8), "기관 예상 질문", font=bold(17), fill=PURPLE)

    # 업계 패턴
    draw.line([(RX+14, TOP+36),(W-PAD-8, TOP+36)], fill=DARK_GRAY, width=1)
    draw.text((RX+14, TOP+42), "업계 패턴  —  이런 컨퍼런스에서 반복되는 질문들", font=bold(13), fill=GRAY)

    patterns = [
        "가이던스 컨펌   —  \"다음 분기도 유지 가능한가\"",
        "계약 파이프라인  —  \"협의 중인 고객이 몇 개나 되냐\"",
        "자금 조달 계획   —  \"언제 또 돈이 필요하냐\"",
        "리스크           —  \"지금 가장 걱정하는 게 뭐냐\"",
    ]
    py = TOP + 62
    for pt in patterns:
        draw.text((RX+14, py), f"· {pt}", font=font(13), fill=GRAY)
        py += 22

    # SATL 특화 질문
    draw.line([(RX+14, py+4),(W-PAD-8, py+4)], fill=DARK_GRAY, width=1)
    draw.text((RX+14, py+12), "지금 SATL 상황에서 예상되는 질문", font=bold(14), fill=WHITE)

    questions = [
        (AMBER,  "①  CFO 후임",       "언제 채우냐  /  내부 승진 vs 외부 영입"),
        (RED,    "②  Merlin 일정",    "2027 H1 배치 슬립 없냐  —  CEO 입으로 직접 확인"),
        (RED,    "③  국방 피봇",      "코어 위성촬영 사업 방향은  /  -17.4% 당시 시장 해석 반박 가능한가"),
        (CYAN,   "④  계약 파이프라인", "Roth 언급 국제 정부 계약  —  실체 있냐  /  몇 개 협의 중"),
        (GREEN,  "⑤  흑자 전환",      "Q1 매출 $6.1M +80%YoY  /  수익성 전환 타임라인"),
    ]
    qy = py + 32
    for color, title, desc in questions:
        box(draw, RX+10, qy, W-PAD-8, qy+52, (18,18,28))
        draw.rectangle([RX+10, qy, RX+14, qy+52], fill=color)
        draw.text((RX+22, qy+6),  title, font=bold(14), fill=color)
        draw.text((RX+22, qy+28), desc,  font=font(12), fill=GRAY)
        qy += 58

    footer(draw, "2026.06.12  SATL ROTH London Conference Preview", "SATL  ·  Roth Capital  ·  Reg FD")

    out = os.path.join(OUT_DIR, "2026-06-12_SATL_ROTH런던프리뷰.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
