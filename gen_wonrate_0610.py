from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-10"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (10, 12, 20)
GRID      = (255, 255, 255, 10)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 75)
PURPLE    = (167, 139, 250)
BLUE      = (59, 130, 246)
CYAN      = (6, 182, 212)
GREEN     = (52, 211, 153)
AMBER     = (245, 158, 11)
RED       = (239, 68, 68)
ACCENT    = AMBER

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)
def make_base():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=GRID, width=1)
    draw.rectangle([0, 0, W, 4], fill=ACCENT)
    draw.rectangle([0, 0, 4, H], fill=ACCENT)
    return img, ImageDraw.Draw(img)
def footer(draw, left, right):
    draw.line([(60, H - 50), (W - 60, H - 50)], fill=DARK_GRAY, width=1)
    draw.text((60,      H - 34), left,  font=font(17), fill=GRAY)
    draw.text((W - 440, H - 34), right, font=bold(17), fill=ACCENT)

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.text((60, 20), "원화 약세 = 수출 호재?", font=bold(40), fill=WHITE)
    draw.text((60, 74), "신현송(BIS 전 수석) — 한국에서 이 공식은 깨진다", font=font(20), fill=AMBER)
    draw.line([(60, 110), (W - 60, 110)], fill=DARK_GRAY, width=1)

    CTOP = 124
    CBOT = H - 62
    DIV  = 480

    # ── 왼쪽: 두 경로 비교 ──
    draw.text((60, CTOP), "환율에 작용하는 두 힘", font=bold(19), fill=GRAY)

    # 무역 경로
    draw.rounded_rectangle([60, CTOP + 28, DIV - 16, CTOP + 130], radius=8, fill=(16, 28, 16))
    draw.rectangle([60, CTOP + 28, 66, CTOP + 130], fill=GREEN)
    draw.text((80, CTOP + 36),  "무역 경로 (전통 공식)", font=bold(17), fill=GREEN)
    draw.text((80, CTOP + 66),  "원화↓ → 수출 가격 경쟁력↑", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 90),  "→ 수출 증가 → GDP 상승", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 112), "경제를 올린다", font=font(14), fill=GREEN)

    # 금융 경로
    draw.rounded_rectangle([60, CTOP + 144, DIV - 16, CTOP + 280], radius=8, fill=(28, 12, 12))
    draw.rectangle([60, CTOP + 144, 66, CTOP + 280], fill=RED)
    draw.text((80, CTOP + 152), "금융 경로 (신현송 이론)", font=bold(17), fill=RED)
    draw.text((80, CTOP + 182), "원화↓ → 달러 빚 부담↑", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 206), "→ 기업 재무 악화", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 230), "→ 은행 강제 디레버리징", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 254), "→ 돈줄이 마른다", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 274), "", font=font(14), fill=RED)

    # 결론 박스
    cbox_y = CTOP + 294
    draw.rounded_rectangle([60, cbox_y, DIV - 16, cbox_y + 64], radius=8, fill=(30, 20, 8))
    draw.rounded_rectangle([60, cbox_y, DIV - 16, cbox_y + 64], radius=8, outline=AMBER, width=1)
    draw.text((80, cbox_y + 10), "BIS 2016 실증 결과", font=bold(15), fill=AMBER)
    draw.text((80, cbox_y + 36), "한국에서 금융 경로 > 무역 경로", font=font(15), fill=WHITE)

    # ── 세로 구분선 ──
    draw.line([(DIV, 110), (DIV, CBOT)], fill=DARK_GRAY, width=1)

    # ── 오른쪽 ──
    RX = DIV + 22

    # 악순환 박스
    draw.text((RX, CTOP), "외국인 자금 악순환 구조", font=bold(19), fill=GRAY)

    steps = [
        (AMBER, "원화 약세"),
        (RED,   "외국인 달러 기준 손실"),
        (RED,   "한국 자산 매도"),
        (RED,   "원화 추가 하락"),
        (RED,   "남은 외국인도 매도"),
    ]
    sy = CTOP + 32
    for i, (color, text) in enumerate(steps):
        draw.rounded_rectangle([RX, sy, W - 60, sy + 34], radius=6, fill=(20, 18, 28))
        draw.rectangle([RX, sy, RX + 5, sy + 34], fill=color)
        draw.text((RX + 16, sy + 8), text, font=font(16) if i > 0 else bold(16), fill=WHITE if i > 0 else AMBER)
        if i < len(steps) - 1:
            draw.text((RX + 16, sy + 38), "↓", font=bold(14), fill=DARK_GRAY)
        sy += 50

    # 원죄 박스
    orig_y = sy + 8
    draw.rounded_rectangle([RX, orig_y, W - 60, orig_y + 80], radius=8, fill=(18, 18, 30))
    draw.rounded_rectangle([RX, orig_y, W - 60, orig_y + 80], radius=8, outline=BLUE, width=1)
    draw.text((RX + 16, orig_y + 10), "원죄의 부활 (신현송)", font=bold(16), fill=BLUE)
    draw.text((RX + 16, orig_y + 38), "원화 국채 → 위험이 사라진 게 아니라", font=font(14), fill=WHITE)
    draw.text((RX + 16, orig_y + 58), "외국인에게 전가됐을 뿐", font=font(14), fill=GRAY)

    # NDF 박스
    ndf_y = orig_y + 96
    draw.rounded_rectangle([RX, ndf_y, W - 60, ndf_y + 60], radius=8, fill=(24, 18, 8))
    draw.rectangle([RX, ndf_y, RX + 5, ndf_y + 60], fill=AMBER)
    draw.text((RX + 16, ndf_y + 8),  "NDF 시장 — 꼬리가 몸통을 흔든다", font=bold(15), fill=AMBER)
    draw.text((RX + 16, ndf_y + 34), "서울 장 마감 후 밤새 원화값 결정 → 다음날 서울 끌려다님", font=font(13), fill=GRAY)

    footer(draw, "2026.06.10", "신현송 · BIS · 한국은행")

    out = os.path.join(OUT_DIR, "2026-06-10_환율_금융경로.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
