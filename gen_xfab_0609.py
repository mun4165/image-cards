from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-09"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (60, 70, 82)
AMBER     = (245, 158, 11)
BLUE      = (59, 130, 246)
CYAN      = (6, 182, 212)
GREEN     = (52, 211, 153)
PURPLE    = (167, 139, 250)
RED       = (239, 68, 68)
ACCENT    = CYAN  # 포토닉스 = 빛 = 청록

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)

def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

def make_base(accent_color):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=GRID, width=1)
    draw.rectangle([0, 0, W, 4], fill=accent_color)
    draw.rectangle([0, 0, 4, H], fill=accent_color)
    return img, ImageDraw.Draw(img)

def footer(draw, date_str, tag_str):
    draw.line([(60, H - 52), (W - 60, H - 52)], fill=DARK_GRAY, width=1)
    draw.text((60,      H - 34), date_str, font=font(17), fill=GRAY)
    draw.text((W - 580, H - 34), tag_str,  font=bold(17), fill=ACCENT)

def make_main():
    img, draw = make_base(ACCENT)

    # ── 헤더 ──
    draw.text((60, 22), "X-FAB Silicon Foundries  |  EPA:XFAB", font=bold(38), fill=WHITE)
    draw.text((60, 74), "유럽 유일 특수 아날로그 파운드리  ·  시총 $1.46B  ·  P/B 1.29x", font=font(22), fill=ACCENT)
    draw.line([(60, 114), (W - 60, 114)], fill=DARK_GRAY, width=1)

    CTOP = 130
    CBOT = H - 64
    DIV  = 618

    # ── 왼쪽: 핵심 레이어 ──
    draw.text((60, CTOP), "3개 레이어", font=bold(20), fill=GRAY)

    layers = [
        (RED,    "자동차 (매출 60%)",
                 "Q1 2026  YoY −10%  →  현재 눌림의 원인",
                 "자율주행 확산 시 중기 반전 논리 존재"),
        (AMBER,  "SiC 전력 반도체",
                 "Q1 2026 웨이퍼 출하  YoY +195%  /  QoQ +28%",
                 "AI 데이터센터 전력관리 수요로 EV 공백 대체"),
        (CYAN,   "실리콘 포토닉스 / CPO",
                 "photonixFAB 리드  ·  NVIDIA·Nokia 공식 멤버",
                 "MTP 독점 + TFLN 120GHz+  →  시장 가치 0 부여 중"),
    ]

    item_h = (CBOT - CTOP - 36) // 3
    y = CTOP + 36
    for color, title, line1, line2 in layers:
        draw.rounded_rectangle([60, y, DIV - 20, y + item_h - 10], radius=8, fill=(20, 24, 34))
        draw.rectangle([60, y, 66, y + item_h - 10], fill=color)
        draw.text((82, y + 10),  title, font=bold(19), fill=color)
        draw.text((82, y + 42),  line1, font=font(16), fill=WHITE)
        draw.text((82, y + 66),  line2, font=font(14), fill=GRAY)
        y += item_h

    # ── 세로 구분선 ──
    draw.line([(DIV, 114), (DIV, CBOT)], fill=DARK_GRAY, width=1)

    # ── 오른쪽: 투자 논점 ──
    RX = DIV + 22
    draw.text((RX, CTOP), "투자 논점", font=bold(20), fill=GRAY)

    total_r = CBOT - CTOP - 36
    bull_h  = int(total_r * 0.295)

    bulls = [
        (GREEN,  "Bull — MTP 독점 파운드리",
                 "고볼륨 마이크로 전사 프린팅  전 세계 유일"),
        (BLUE,   "Bull — EU CHIPS Act 2.0",
                 "포토닉스 명시 포함  ·  photonixFAB 직접 수혜 구조"),
    ]

    ry = CTOP + 36
    for color, title, sub in bulls:
        draw.rounded_rectangle([RX, ry, W - 60, ry + bull_h - 8], radius=8, fill=(20, 24, 34))
        draw.rectangle([RX, ry, RX + 6, ry + bull_h - 8], fill=color)
        draw.text((RX + 20, ry + 12), title, font=bold(18), fill=color)
        draw.text((RX + 20, ry + 48), sub,   font=font(15), fill=GRAY)
        ry += bull_h + 8

    # Bear 박스
    bear_h = total_r - bull_h * 2 - 16
    bear_y = ry
    bear_b = bear_y + bear_h - 4
    draw.rounded_rectangle([RX, bear_y, W - 60, bear_b], radius=8, fill=(28, 16, 16))
    draw.rounded_rectangle([RX, bear_y, W - 60, bear_b], radius=8, outline=RED, width=1)
    draw.text((RX + 18, bear_y + 10),  "⚠  Bear",                                        font=bold(16), fill=RED)
    draw.text((RX + 18, bear_y + 44),  "① 자동차 60% 역성장 — 전체 매출 역성장 지속",   font=font(14), fill=GRAY)
    draw.text((RX + 18, bear_y + 72),  "② NVIDIA 계약 없음 — 평가 단계, 구매약정 미체결", font=font(14), fill=GRAY)
    draw.text((RX + 18, bear_y + 100), "③ 카탈리스트까지 18개월+ — 기회비용 존재",       font=font(14), fill=GRAY)

    # ── 핵심 테제 바 ──
    draw.line([(60, CBOT + 4), (W - 60, CBOT + 4)], fill=DARK_GRAY, width=1)
    draw.rounded_rectangle([60, CBOT + 12, W - 60, CBOT + 46], radius=6, fill=(10, 30, 36))
    draw.text((80, CBOT + 18),
              "핵심 테제  →  CPO 옵션이 장부가($1.46B)에 공짜로 껴있다",
              font=bold(20), fill=CYAN)

    footer(draw, "2026.06.09", "X-FAB  ·  photonixFAB  ·  EU CHIPS Act 2.0")

    out = os.path.join(OUT_DIR, "2026-06-09_XFAB_CPO파운드리분석.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
