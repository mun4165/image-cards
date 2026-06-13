from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-12"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
GREEN     = (52, 211, 153)
CYAN      = (6, 182, 212)
BLUE      = (59, 130, 246)
AMBER     = (245, 158, 11)

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
draw.text((32, 14), "SIVE — 820만 달러 공시를 끝까지 뜯으면", font=bold(36), fill=WHITE)
draw.text((32, 62), "2026.06.12  |  공시 분석 프레임  |  Sivers Semiconductors", font=font(18), fill=CYAN)
draw.line([(32, 98), (W - 32, 98)], fill=DARK_GRAY, width=1)

CONTENT_TOP = 114
CONTENT_BOT = H - 52

GAP = 12
MID_X = W // 2
MID_Y = (CONTENT_TOP + CONTENT_BOT) // 2

LX1, RX1 = 32, MID_X - GAP // 2
LX2, RX2 = MID_X + GAP // 2, W - 32
TY1, BY1 = CONTENT_TOP, MID_Y - GAP // 2
TY2, BY2 = MID_Y + GAP // 2, CONTENT_BOT

boxes = [
    (LX1, TY1, RX1, BY1, GREEN,
     "계약 성격",
     "샘플인가, 생산 계약인가",
     ["CEO: \"양산 이정표\" 직접 선언",
      "$8.2M — 금액이 아니라 단계 전환의 선언",
      "숫자보다 문장을 먼저 읽어야 하는 이유"]),
    (LX2, TY1, RX2, BY1, BLUE,
     "카운터파티",
     "ALL.SPACE → York Space Systems",
     ["$355M 확정계약 기준 인수 진행 중",
      "스타트업 → NYSE 상장사로 격상",
      "방산 공급망 한 단계 깊이 진입"]),
    (LX1, TY2, RX1, BY2, CYAN,
     "기관 동향",
     "JPMorgan · Fidelity · BlackRock",
     ["JPMorgan 5.25%  —  GF 발표 당일 공시",
      "Fidelity 자체 리서치 후 액티브 진입",
      "BlackRock 인덱스 편입 패시브 오너"]),
    (LX2, TY2, RX2, BY2, AMBER,
     "파이프라인",
     "$799M  —  파이프라인 ≠ 매출",
     ["5개월 만에 +77%  ($450M → $799M)",
      "전환율 20~40% → 실현 추정 $160~320M",
      "파이프라인 → 백로그 → 매출 순서로 추적"]),
]

for lx, ty, rx, by, color, label, title, lines in boxes:
    draw.rounded_rectangle([lx, ty, rx, by], radius=8, fill=(18, 22, 34))
    draw.rectangle([lx, ty, lx + 5, by], fill=color)
    draw.text((lx + 18, ty + 12), label, font=bold(14), fill=color)
    draw.text((lx + 18, ty + 40), title, font=bold(17), fill=WHITE)
    ly = ty + 76
    for line in lines:
        draw.text((lx + 18, ly), "·  " + line, font=font(13), fill=GRAY)
        ly += 26

# ── 하단 결론 바 ──
draw.line([(32, H - 52), (W - 32, H - 52)], fill=DARK_GRAY, width=1)
draw.rounded_rectangle([32, H - 48, W - 32, H - 8], radius=6, fill=(14, 24, 36))
draw.text((52, H - 36), "숫자보다 문장을 먼저 읽는 것  —  공시를 대하는 기본 프레임이다", font=bold(16), fill=CYAN)

out = os.path.join(OUT_DIR, "2026-06-12_SIVE_공시분석프레임.png")
img.save(out)
print("Saved:", out)
