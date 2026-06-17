from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR   = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-15"
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
    draw.text((W-530, H-34), right, font=bold(17), fill=AMBER)

def make_card():
    img, draw = make_base()

    # ── 헤더 ──
    draw.text((60, 20), "뉴스보다 먼저 봐야 할 것 — 시장이 그 뉴스를 얼마나 반영했는가", font=bold(30), fill=WHITE)
    draw.text((60, 64), "뉴스의 방향이 아니라  ·  기대와 현실의 간극이 수익의 출처다", font=font(18), fill=AMBER)
    draw.line([(60, 98), (W-60, 98)], fill=DARK_GRAY, width=1)

    CTOP = 110
    CBOT = H - 58
    DIV  = 560

    # ═══════════════════════════════
    # 왼쪽 패널 — 반영 여부 비교
    # ═══════════════════════════════

    # 섹션 레이블
    draw.text((60, CTOP), "반영 여부 체크", font=bold(16), fill=GRAY)
    draw.line([(60, CTOP+24), (DIV-20, CTOP+24)], fill=DARK_GRAY, width=1)

    items = [
        (RED,   "이미 반영",  "금리 인상 (연말 1회)",
                "CME FedWatch 이미 반영 완료",
                "인상 시 타격 제한적  ·  동결·인하는 서프라이즈 상방"),
        (GREEN, "미반영",     "소버린 AI 수요 폭발",
                "각국 독자 AI 인프라 경쟁 — 이번 주말 기점 가속",
                "하이퍼스케일러 외 전 세계 정부 수요 추가"),
        (CYAN,  "미반영",     "네오클라우드 리레이팅",
                "IREN: AI 매출 하반기 가시화 — 시장 인식 아직 채굴사",
                "MU: 기존 AI 수요 + 소버린AI 수요 동시 상향"),
    ]

    y = CTOP + 34
    item_h = (CBOT - y - 4) // 3

    for color, badge, title, line1, line2 in items:
        bg_col = (16, 14, 10) if color == RED else (10, 16, 14) if color == GREEN else (10, 14, 18)
        draw.rounded_rectangle([60, y+2, DIV-20, y+item_h-4], radius=8, fill=bg_col)
        draw.rectangle([60, y+2, 66, y+item_h-4], fill=color)

        # 뱃지
        badge_bg = (40, 20, 20) if color == RED else (14, 36, 26) if color == GREEN else (10, 24, 36)
        draw.rounded_rectangle([74, y+10, 74+60, y+30], radius=4, fill=badge_bg)
        draw.text((78, y+12), badge, font=font(13), fill=color)

        draw.text((148, y+10), title, font=bold(19), fill=WHITE)
        draw.text((82,  y+40), line1, font=font(14), fill=GRAY)
        draw.text((82,  y+62), line2, font=font(13), fill=GRAY)

        y += item_h

    # ── 세로 구분선 ──
    draw.line([(DIV, 98), (DIV, CBOT)], fill=DARK_GRAY, width=1)

    # ═══════════════════════════════
    # 오른쪽 패널 — IREN + MU
    # ═══════════════════════════════
    RX = DIV + 22

    draw.text((RX, CTOP), "연결 종목", font=bold(16), fill=GRAY)
    draw.line([(RX, CTOP+24), (W-60, CTOP+24)], fill=DARK_GRAY, width=1)

    # IREN 박스
    iren_top = CTOP + 34
    iren_bot = CTOP + 34 + (CBOT - CTOP - 34) // 2 - 8

    draw.rounded_rectangle([RX, iren_top, W-60, iren_bot], radius=8, fill=(10, 16, 22))
    draw.rounded_rectangle([RX, iren_top, W-60, iren_bot], radius=8, outline=CYAN, width=1)

    draw.text((RX+14, iren_top+10), "$IREN  —  아직 채굴사 멀티플", font=bold(18), fill=CYAN)

    iren_rows = [
        ("보유 GPU",    "Blackwell 최신 세대"),
        ("전력 자산",   "재생에너지 저가 사이트 확보"),
        ("AI 매출",     "2026 하반기부터 가시화"),
        ("리레이팅",    "AI 매출 찍혀야 멀티플 전환"),
    ]
    ry = iren_top + 44
    for label, val in iren_rows:
        draw.text((RX+14, ry), label, font=font(14), fill=GRAY)
        draw.text((RX+130, ry), val,  font=font(14), fill=WHITE)
        ry += 26

    # MU 박스
    mu_top = iren_bot + 10
    mu_bot = CBOT - 4

    draw.rounded_rectangle([RX, mu_top, W-60, mu_bot], radius=8, fill=(10, 14, 22))
    draw.rounded_rectangle([RX, mu_top, W-60, mu_bot], radius=8, outline=BLUE, width=1)

    draw.text((RX+14, mu_top+10), "$MU  —  수요가 두 방향에서 동시에 온다", font=bold(18), fill=BLUE)

    mu_rows = [
        ("기존 수요",   "빅테크 AI 학습·추론 인프라"),
        ("추가 수요",   "소버린AI → 각국 서버 → 메모리"),
        ("확인 시점",   "2026.06.24  MU Q3 실적"),
    ]
    ry = mu_top + 44
    for label, val in mu_rows:
        draw.text((RX+14, ry), label, font=font(14), fill=GRAY)
        draw.text((RX+130, ry), val,  font=font(14), fill=WHITE)
        ry += 28

    footer(draw, "2026.06.15  ·  개인 공부 기록", "$IREN  $MU  #소버린AI  #AI인프라")

    out = os.path.join(OUT_DIR, "2026-06-15_소버린AI_반영여부.png")
    img.save(out)
    print(f"Saved: {out}")

make_card()
print("Done.")
