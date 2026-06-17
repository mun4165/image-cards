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
ACCENT    = GREEN

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
    draw.text((60, 20), "SIVE  Sivers — 개발에서 양산으로", font=bold(38), fill=WHITE)
    draw.text((60, 72), "ALL.SPACE Ka-band 빔포밍 IC  ·  다년간 양산 계약  ·  방산 실전 운용", font=font(20), fill=GREEN)
    draw.line([(60, 108), (W - 60, 108)], fill=DARK_GRAY, width=1)

    CTOP = 122
    CBOT = H - 62
    DIV  = 560

    # ── 왼쪽: 계약 핵심 ──
    draw.text((60, CTOP), "계약 핵심", font=bold(19), fill=GRAY)

    draw.rounded_rectangle([60, CTOP + 28, DIV - 16, CTOP + 120], radius=8, fill=(12, 28, 18))
    draw.rectangle([60, CTOP + 28, 66, CTOP + 120], fill=GREEN)
    draw.text((80, CTOP + 36),  "$8.2M  Ka-band 빔포밍 IC 양산 계약", font=bold(18), fill=GREEN)
    draw.text((80, CTOP + 70),  "납품 기간  ·  2027년까지 순차 진행", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 96),  "Sivers 역대 단일 계약 최대 규모 수준", font=font(14), fill=GRAY)

    draw.rounded_rectangle([60, CTOP + 132, DIV - 16, CTOP + 242], radius=8, fill=(16, 20, 36))
    draw.rectangle([60, CTOP + 132, 66, CTOP + 242], fill=BLUE)
    draw.text((80, CTOP + 140), "실전 운용 고객", font=bold(17), fill=BLUE)
    draw.text((80, CTOP + 172), "미 육군  ·  미 해군  ·  캐나다 해군", font=font(16), fill=WHITE)
    draw.text((80, CTOP + 200), "Telesat  ·  SES  ·  Viasat", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 222), "LEO · MEO · GEO  전 궤도 커버", font=font(14), fill=GRAY)

    draw.rounded_rectangle([60, CTOP + 254, DIV - 16, CTOP + 344], radius=8, fill=(24, 18, 40))
    draw.rectangle([60, CTOP + 254, 66, CTOP + 344], fill=AMBER)
    draw.text((80, CTOP + 262), "카운터파티 변화", font=bold(17), fill=AMBER)
    draw.text((80, CTOP + 294), "ALL.SPACE → York Space Systems(YSS) 인수", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 320), "스타트업 → NYSE 상장사  ·  계약 연속성 유지", font=font(14), fill=GRAY)

    # ── 세로 구분선 ──
    draw.line([(DIV, 108), (DIV, CBOT)], fill=DARK_GRAY, width=1)

    # ── 오른쪽: 의미 + CEO 발언 ──
    RX = DIV + 22

    draw.text((RX, CTOP), "이 계약이 중요한 이유", font=bold(19), fill=GRAY)

    # CEO 발언 박스
    ceo_y = CTOP + 28
    draw.rounded_rectangle([RX, ceo_y, W - 60, ceo_y + 110], radius=8, fill=(18, 26, 18))
    draw.rounded_rectangle([RX, ceo_y, W - 60, ceo_y + 110], radius=8, outline=GREEN, width=1)
    draw.text((RX + 18, ceo_y + 12), "CEO Vickram Vathulya", font=bold(16), fill=GREEN)
    draw.text((RX + 18, ceo_y + 44), "“개발·초기 생산에서", font=font(15), fill=WHITE)
    draw.text((RX + 18, ceo_y + 68), " 대규모 다년간 양산 배치로 이행하는", font=font(15), fill=WHITE)
    draw.text((RX + 18, ceo_y + 90), " 중요한 이정표”", font=bold(15), fill=WHITE)

    # 빔포밍 IC 설명
    bx_y = ceo_y + 126
    draw.rounded_rectangle([RX, bx_y, W - 60, bx_y + 86], radius=8, fill=(16, 22, 34))
    draw.rectangle([RX, bx_y, RX + 5, bx_y + 86], fill=CYAN)
    draw.text((RX + 18, bx_y + 10), "빔포밍 IC가 하는 일", font=bold(16), fill=CYAN)
    draw.text((RX + 18, bx_y + 40), "터미널 1대가 여러 위성을 동시 추적", font=font(15), fill=WHITE)
    draw.text((RX + 18, bx_y + 64), "LEO 위성 증가 → 터미널당 IC 수량도 증가", font=font(14), fill=GRAY)

    # 핵심 요약 박스
    lbox_y = bx_y + 100
    lbox_b = CBOT - 4
    draw.rounded_rectangle([RX, lbox_y, W - 60, lbox_b], radius=8, fill=(20, 30, 20))
    draw.rounded_rectangle([RX, lbox_y, W - 60, lbox_b], radius=8, outline=GREEN, width=1)
    draw.text((RX + 18, lbox_y + 12), "전환점 신호", font=bold(17), fill=GREEN)
    draw.text((RX + 18, lbox_y + 46), "양산이라는 말은 계약서가 증명한다", font=font(16), fill=WHITE)
    draw.text((RX + 18, lbox_y + 76), "방산 + 상업 위성  두 수요 동시 확보", font=font(15), fill=GRAY)
    draw.text((RX + 18, lbox_y + 104),"리스크: 규모·수익성 전환 시점 불투명", font=font(14), fill=RED)

    footer(draw, "2026.06.10", "SIVE  ·  Sivers Semiconductors  ·  ALL.SPACE")

    out = os.path.join(OUT_DIR, "2026-06-10_SIVE_AllSpace.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
