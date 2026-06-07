from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-05"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
RED       = (239, 68, 68)
ORANGE    = (249, 115, 22)
AMBER     = (245, 158, 11)
GREEN     = (52, 211, 153)
CYAN      = (6, 182, 212)
PURPLE    = (167, 139, 250)

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")

for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

draw.rectangle([0, 0, W, 4], fill=CYAN)
draw.rectangle([0, 0, 4, H], fill=CYAN)

# ── 헤더 ──
draw.text((32, 14), "JPMorgan, $SIVE 지분 5.25% 취득", font=bold(38), fill=WHITE)
draw.text((32, 62), "2026.06.02  |  거래 전 보유량 0주 → 하루 만에 5.25%  |  GF 발표 당일", font=font(18), fill=CYAN)
draw.line([(32, 96), (W - 32, 96)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 포지션 구조 ──
draw.text((32, 110), "포지션 구조", font=bold(19), fill=GRAY)

# 총 취득 강조
draw.rounded_rectangle([32, 138, 390, 212], radius=8, fill=(15, 30, 40))
draw.rounded_rectangle([32, 138, 390, 212], radius=8, outline=CYAN, width=2)
draw.text((50, 146), "총 취득", font=font(15), fill=GRAY)
draw.text((50, 170), "16,098,583주  /  5.25%", font=bold(24), fill=CYAN)

items = [
    (GREEN,  "직접 주식",         "10,049,558주  (3.14%)"),
    (PURPLE, "현금결제 파생상품", "~6,049,025주  (스왑 추정)"),
    (AMBER,  "보유 법인",         "JP Morgan Securities plc (영국)"),
    (GRAY,   "플래깅 사유",       '"Köp" — 스웨덴어 매수'),
]
y = 224
for color, label, value in items:
    draw.rounded_rectangle([32, y, 390, y + 100], radius=6, fill=(20, 22, 30))
    draw.rectangle([32, y, 37, y + 100], fill=color)
    draw.text((50, y + 14), label, font=font(15), fill=GRAY)
    draw.text((50, y + 44), value, font=bold(19), fill=color)
    y += 110

# ── 세로 구분선 ──
draw.line([(420, 96), (420, H - 44)], fill=DARK_GRAY, width=1)

# ── 오른쪽 상단: 해석 ──
draw.text((444, 110), "가장 유력한 해석", font=bold(19), fill=GRAY)
draw.line([(444, 138), (W - 32, 138)], fill=DARK_GRAY, width=1)

draw.rounded_rectangle([444, 148, W - 32, 346], radius=8, fill=(15, 25, 15))
draw.rectangle([444, 148, 450, 346], fill=GREEN)
draw.text((466, 160), "나스닥 이중상장 언더라이터 포지셔닝", font=bold(20), fill=GREEN)

reasons = [
    "→  SIVE, 2026.04.16 나스닥 NY 이중상장 공식 검토 발표",
    "→  직접주식 + 스왑 혼합 구조 = ECM 딜 준비 전형 패턴",
    "→  JP Morgan Securities plc(영국) 보유 = 글로벌 ECM 운영 주체",
    "→  AGM 6월 15일 — 이중상장 의결 임박",
]
ry = 200
for r in reasons:
    draw.text((466, ry), r, font=font(16), fill=WHITE)
    ry += 32

# ── 오른쪽 중단: 카운터 시그널 ──
draw.rounded_rectangle([444, 358, W - 32, 516], radius=8, fill=(30, 15, 15))
draw.rectangle([444, 358, 450, 516], fill=RED)
draw.text((466, 368), "카운터 시그널", font=bold(19), fill=RED)
draw.text((466, 402), "5월 29일 — GF 발표 3일 전", font=bold(20), fill=WHITE)
draw.text((466, 438), "무선사업부 대표, 보유 전량 140만 주 매도", font=font(17), fill=GRAY)
draw.text((466, 468), "약 1억 크로나 (130억 원) 규모 전량 청산", font=font(17), fill=RED)
draw.text((466, 494), "JPMorgan이 사는 날, 내부자는 팔았다", font=bold(15), fill=RED)

# ── 오른쪽 하단: 체크포인트 ──
draw.rounded_rectangle([444, 528, W - 32, 660], radius=8, fill=(20, 20, 35))
draw.rectangle([444, 528, 450, 660], fill=AMBER)
draw.text((466, 538), "다음 체크포인트", font=bold(19), fill=AMBER)
draw.text((466, 574), "6월 15일 AGM  —  나스닥 이중상장 의결", font=bold(20), fill=WHITE)
draw.text((466, 612), "통과 →  JPMorgan 포지션 맥락 확정", font=font(16), fill=GREEN)
draw.text((466, 638), "부결 →  해석 전면 재검토", font=font(16), fill=RED)

# ── 하단 바 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.05", font=font(15), fill=GRAY)
draw.text((W - 260, H - 30), "$SIVE  Sivers Semiconductors", font=bold(15), fill=CYAN)

out = os.path.join(OUT_DIR, "2026-06-05_SIVE_JPMorgan5%.png")
img.save(out)
print("Saved:", out)
