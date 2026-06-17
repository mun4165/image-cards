from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR   = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-16"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (10, 11, 16)
GRID      = (255, 255, 255, 10)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (52, 56, 68)
AMBER     = (245, 158, 11)
GREEN     = (52, 211, 153)
BLUE      = (59, 130, 246)
RED       = (239, 68, 68)
CYAN      = (6, 182, 212)

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

def footer(draw, left, right):
    draw.line([(60, H-50), (W-60, H-50)], fill=DARK_GRAY, width=1)
    draw.text((60,    H-34), left,  font=font(17), fill=GRAY)
    draw.text((W-420, H-34), right, font=bold(17), fill=AMBER)

def make_card():
    img, draw = make_base()

    # ── 헤더 ──
    draw.text((60, 20), "SIVE  주주총회 결과", font=bold(34), fill=WHITE)
    draw.text((60, 66), "2026.06.15  ·  핵심 압축", font=font(18), fill=AMBER)
    draw.line([(60, 100), (W-60, 100)], fill=DARK_GRAY, width=1)

    CTOP = 114
    CBOT = H - 58
    DIV  = 590

    # ══════════════════════════════
    # 왼쪽 — 승인된 것
    # ══════════════════════════════
    draw.text((60, CTOP), "주총에서 승인된 것", font=bold(16), fill=GREEN)
    draw.line([(60, CTOP+26), (DIV-20, CTOP+26)], fill=DARK_GRAY, width=1)

    approved = [
        ("신주 5,384만 주 발행 수권",
         "기존 주식 대비 최대 15% 희석 한도  ·  발행가 = 시장가"),
        ("이사회 재편",
         "Nideborn 신규(부의장)  ·  Svancar 신규  ·  Bastani 의장 재선임"),
        ("소규모 전환사채",
         "$327K  ·  이자율 10.85%  ·  만기 2029.12"),
    ]

    y = CTOP + 36
    row_h = (CBOT - y - 4) // 3

    for title, sub in approved:
        draw.rounded_rectangle([60, y+2, DIV-20, y+row_h-4], radius=8, fill=(10, 18, 14))
        draw.rectangle([60, y+2, 66, y+row_h-4], fill=GREEN)
        draw.text((80, y+12), "✓  " + title, font=bold(18), fill=WHITE)
        draw.text((80, y+44), sub,            font=font(14), fill=GRAY)
        y += row_h

    # ── 구분선 ──
    draw.line([(DIV, 100), (DIV, CBOT)], fill=DARK_GRAY, width=1)

    # ══════════════════════════════
    # 오른쪽 — 미확정 + 리스크
    # ══════════════════════════════
    RX = DIV + 22

    draw.text((RX, CTOP), "미확정 / 진행 중", font=bold(16), fill=RED)
    draw.line([(RX, CTOP+26), (W-60, CTOP+26)], fill=DARK_GRAY, width=1)

    # 나스닥 이중상장 박스
    nasdaq_top = CTOP + 36
    nasdaq_bot = CTOP + 36 + (CBOT - CTOP - 36) // 2 - 6

    draw.rounded_rectangle([RX, nasdaq_top, W-60, nasdaq_bot], radius=8, fill=(16, 12, 10))
    draw.rounded_rectangle([RX, nasdaq_top, W-60, nasdaq_bot], radius=8, outline=AMBER, width=1)

    draw.text((RX+14, nasdaq_top+12), "나스닥 이중상장  —  아직 미확정", font=bold(19), fill=AMBER)

    nasdaq_rows = [
        "주총 결의 없음  ·  여전히 'potential' 단계",
        "나스닥 거래소 심사·승인 별도 절차 남음",
        "주총 직후 주가 반응  -4%",
    ]
    ry = nasdaq_top + 50
    for row in nasdaq_rows:
        draw.text((RX+14, ry), "·  " + row, font=font(14), fill=GRAY)
        ry += 26

    # 리스크 박스
    risk_top = nasdaq_bot + 10
    risk_bot = CBOT - 4

    draw.rounded_rectangle([RX, risk_top, W-60, risk_bot], radius=8, fill=(16, 10, 10))
    draw.rounded_rectangle([RX, risk_top, W-60, risk_bot], radius=8, outline=RED, width=1)

    draw.text((RX+14, risk_top+12), "해소되지 않은 리스크", font=bold(19), fill=RED)

    risk_rows = [
        "Ningi Research  —  매출 31% 과대계상 의혹 진행 중",
        "스웨덴 검찰  —  내부자 거래 형사 조사 진행 중",
        "다음 확인:  2026.08.06  Q2 실적 발표",
    ]
    ry = risk_top + 50
    for row in risk_rows:
        draw.text((RX+14, ry), "·  " + row, font=font(14), fill=GRAY)
        ry += 26

    footer(draw, "2026.06.15  ·  개인 공부 기록", "$SIVE  #주주총회  #나스닥이중상장")

    out = os.path.join(OUT_DIR, "2026-06-16_SIVE_AGM.png")
    img.save(out)
    print(f"Saved: {out}")

make_card()
print("Done.")
