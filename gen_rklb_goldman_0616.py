from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-16"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
BLUE      = (59, 130, 246)
CYAN      = (6, 182, 212)
GREEN     = (52, 211, 153)
AMBER     = (245, 158, 11)
PURPLE    = (167, 139, 250)
RED       = (239, 68, 68)

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")

# 그리드
for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

# 상단·좌측 강조선
draw.rectangle([0, 0, W, 4], fill=BLUE)
draw.rectangle([0, 0, 4, H], fill=BLUE)

# ── 헤더 ──
draw.text((32, 14), "골드만삭스는 왜 $RKLB를 $1억 더 샀나", font=bold(36), fill=WHITE)
draw.text((32, 62), "2026.06.16  |  13F 너머의 진짜 thesis — 선행매수 vs 깊은 분석", font=font(17), fill=BLUE)
draw.line([(32, 98), (W - 32, 98)], fill=DARK_GRAY, width=1)

CONTENT_TOP = 114
CONTENT_BOT = H - 52

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("골드만삭스 지분 증가",   "+136.7%",   "공개 13F 기준  /  Q1 2026",                  BLUE),
    ("추정 투자 금액",         "~$100M",    "절대 금액 기준 의미 있는 규모",               CYAN),
    ("RKLB Q1 2026 매출",     "$200.3M",   "+63.5% YoY  /  분기 사상 최대",              GREEN),
    ("수주잔고",               "$2.2B",     "Q1 계약 31건  /  2025년 전체 초과",          AMBER),
]
y = CONTENT_TOP
for label, value, sub, color in metrics:
    draw.text((32, y), label, font=font(16), fill=GRAY)
    draw.text((32, y + 22), value, font=bold(28), fill=color)
    draw.text((32, y + 56), sub, font=font(14), fill=GRAY)
    draw.line([(32, y + 80), (520, y + 80)], fill=DARK_GRAY, width=1)
    y += 90

# ── 세로 구분선 ──
draw.line([(548, 98), (548, CONTENT_BOT)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 핵심 포인트 ──
RX = 568
draw.text((RX, CONTENT_TOP), "핵심 포인트", font=bold(18), fill=GRAY)
draw.line([(RX, CONTENT_TOP + 28), (W - 32, CONTENT_TOP + 28)], fill=DARK_GRAY, width=1)

points = [
    (RED,    "[주의]  13F는 45일 지연 공개",
     ["1~3월 포지션이 5월 중순에야 공개됨",
      "언제 샀는지 알 수 없고 이미 팔았을 수도 있다"]),
    (BLUE,   "골드만이 실제로 본 것",
     ["수주잔고 $2B 근접  /  국방부 HASTE $190M 계약",
      "Neutron 타임라인  /  Electron 발사 성공률 — 모두 공개 정보"]),
    (GREEN,  "같은 방향으로 움직인 기관들",
     ["BlackRock +14.8% 추가 매수  /  기관 순매수 541개사",
      "단독 베팅이 아닌 우주·방산 섹터 전반 자금 유입"]),
]

START_Y = CONTENT_TOP + 38
GAP = 8
N_TOTAL = len(points) + 1
ROW_H = (CONTENT_BOT - START_Y - GAP * (N_TOTAL - 1)) // N_TOTAL

y = START_Y
for color, title, lines in points:
    draw.rounded_rectangle([RX, y, W - 32, y + ROW_H], radius=8, fill=(20, 24, 34))
    draw.rectangle([RX, y, RX + 4, y + ROW_H], fill=color)
    draw.text((RX + 18, y + 10), title, font=bold(17), fill=WHITE)
    dy = y + 40
    for line in lines:
        draw.text((RX + 18, dy), line, font=font(14), fill=GRAY)
        dy += 24
    y += ROW_H + GAP

# 다음 확인 포인트
draw.rounded_rectangle([RX, y, W - 32, CONTENT_BOT], radius=8, fill=(12, 18, 36))
draw.rectangle([RX, y, RX + 4, CONTENT_BOT], fill=PURPLE)
mid = y + (CONTENT_BOT - y) // 2
draw.text((RX + 18, mid - 22), "다음 확인 포인트", font=bold(16), fill=PURPLE)
draw.text((RX + 18, mid + 4), "Q2 2026 실적  —  가이던스 $225~240M 달성 여부", font=font(15), fill=GRAY)

# ── 푸터 ──
draw.line([(32, H - 52), (W - 32, H - 52)], fill=DARK_GRAY, width=1)
draw.text((32, H - 36), "2026.06.16  |  SEC 13F · StockTitan · Simply Wall St · CNBC", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-16_RKLB_Goldman_card.png")
img.save(out)
print("Saved:", out)
