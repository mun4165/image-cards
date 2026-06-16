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
AMBER     = (245, 158, 11)
CYAN      = (6, 182, 212)
BLUE      = (59, 130, 246)
GREEN     = (52, 211, 153)
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
draw.rectangle([0, 0, W, 4], fill=CYAN)
draw.rectangle([0, 0, 4, H], fill=CYAN)

# ── 헤더 ──
draw.text((32, 14), "$AAOI  Spectrum QuantumLink 딜  +14%", font=bold(36), fill=WHITE)
draw.text((32, 62), "2026.06.15  |  하드웨어 납품사  →  소프트웨어 구독 플랫폼", font=font(17), fill=CYAN)
draw.line([(32, 98), (W - 32, 98)], fill=DARK_GRAY, width=1)

CONTENT_TOP = 114
CONTENT_BOT = H - 52

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("6/15 등락",             "+14.46%",  "$193.22 마감  /  5/29 $158 대비 +22%",           GREEN),
    ("Rosenblatt 목표가",     "$220",     "상향 전 $140  /  Amazon 800G + Oracle 퀄 근거",  CYAN),
    ("Raymond James 목표가",  "$160",     "상향 전 $72.50  /  Outperform 유지",              BLUE),
    ("2026 매출 가이던스",    "$1B+",     "Q1 역대 최고  /  Q3 2027 트랜시버 $1.4B 목표",   AMBER),
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

# ── 오른쪽: 핵심 이슈 & 체크포인트 ──
RX = 568
draw.text((RX, CONTENT_TOP), "핵심 이슈 & 체크포인트", font=bold(18), fill=GRAY)
draw.line([(RX, CONTENT_TOP + 28), (W - 32, CONTENT_TOP + 28)], fill=DARK_GRAY, width=1)

points = [
    (CYAN,  "QuantumLink 딜 — 사업 모델 전환",
     ["Spectrum 브로드밴드 망에 소프트웨어 공급자로 진입",
      "하드웨어 일회성 납품  →  구독형 반복 매출 레이어 추가"]),
    (GREEN, "800G 수주 현황",
     ["Amazon 800G 납품 진행 중  /  Oracle 퀄 진행 중",
      "Q3 2027까지 광트랜시버 매출 $1.4B 목표"]),
    (RED,   "[주의]  임원 매도 집중",
     ["CFO 4,000주 (6/10)  /  Chang 4,000주 (6/5)  /  Yeh 10,000주 (6/4)",
      "고점 구간 매도 집중  —  단기 변동성 열어둘 것"]),
]

START_Y = CONTENT_TOP + 38
GAP = 8
N_TOTAL = len(points) + 1  # 3개 이슈 + 확인포인트
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

# 다음 확인 포인트 박스 — CONTENT_BOT까지 꽉 채움
draw.rounded_rectangle([RX, y, W - 32, CONTENT_BOT], radius=8, fill=(10, 24, 36))
draw.rectangle([RX, y, RX + 4, CONTENT_BOT], fill=CYAN)
mid = y + (CONTENT_BOT - y) // 2
draw.text((RX + 18, mid - 22), "다음 확인 포인트", font=bold(16), fill=CYAN)
draw.text((RX + 18, mid + 4), "Oracle 퀄 통과 여부  +  800G 납품 확대 공식 발표", font=font(15), fill=GRAY)

# ── 푸터 ──
draw.line([(32, H - 52), (W - 32, H - 52)], fill=DARK_GRAY, width=1)
draw.text((32, H - 36), "2026.06.15~16  |  StocksToTrade · Rosenblatt · Raymond James · GuruFocus", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-16_AAOI_QuantumLink_card.png")
img.save(out)
print("Saved:", out)
