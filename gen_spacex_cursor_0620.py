from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-20"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (60, 70, 82)
AMBER     = (245, 158, 11)
TEAL      = (20, 184, 166)
BLUE      = (59, 130, 246)
CYAN      = (6, 182, 212)
GREEN     = (52, 211, 153)
RED       = (239, 68, 68)
ORANGE    = (249, 115, 22)

ACCENT = BLUE  # 머스크 AI 생태계 수직통합 테마

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

draw.rectangle([0, 0, W, 4], fill=ACCENT)
draw.rectangle([0, 0, 4, H], fill=ACCENT)

# ── 헤더 ──
draw.text((32, 18), "로켓 회사가 코딩 회사를 샀다", font=bold(40), fill=ACCENT)
draw.text((32, 72), "스페이스X, 커서 600억 달러 전액 주식 인수", font=bold(23), fill=WHITE)
draw.text((32, 108), "표면은 'AI 코딩' — 본질은 머스크 AI 생태계의 빈칸 메우기", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("인수 금액",        "600억 달러",  "전액 주식 교환 (현금 아님)",        BLUE),
    ("인수 구조",        "X67 합병",    "앤스피어 = 스페이스X 완전자회사",    CYAN),
    ("대상 = 커서",      "2022년 창업", "연환산 매출 2월 20 → 6월 40억$(포브스)", GREEN),
    ("종결 예정",        "2026 3Q",     "규제 승인 등 남음 · 4월 옵션 행사",   AMBER),
]
y = 158
for label, value, sub, color in metrics:
    draw.text((32, y), label, font=font(17), fill=GRAY)
    draw.text((32, y + 22), value, font=bold(28), fill=color)
    draw.text((32, y + 56), sub, font=font(16), fill=GRAY)
    draw.line([(32, y + 80), (590, y + 80)], fill=DARK_GRAY, width=1)
    y += 92

draw.line([(620, 140), (620, H - 46)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 핵심 논지 ──
draw.text((644, 158), "통섭 — 로켓이 아니라 AI다", font=bold(23), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (BLUE,  "상장 화폐로 산 첫 딜",
     "나스닥 사상 최대 IPO 직후 자사주 인수"),
    (CYAN,  "xAI의 빈칸을 메운다",
     "콜로서스·그록은 있으나 '제품·창구'가 약했다"),
    (GREEN, "못 만들어서 샀다",
     "공동창업자 이탈·그록 논란 → 자본으로 수직통합"),
    (AMBER, "양날의 검",
     "매출 십수 배 값 + 주가가 받쳐줘야 안 비싸다"),
]
y = 204
for color, title, desc in points:
    draw.rectangle([640, y + 3, 644, y + 30], fill=color)
    draw.text((656, y), title, font=bold(20), fill=WHITE)
    draw.text((656, y + 28), desc, font=font(17), fill=GRAY)
    y += 62

draw.line([(644, y + 4), (W - 32, y + 4)], fill=DARK_GRAY, width=1)
y += 18
draw.rounded_rectangle([644, y, W - 32, y + 62], radius=8, fill=(8, 22, 40))
draw.text((658, y + 12), "조직으로 못 만든 제품·데이터를", font=bold(18), fill=BLUE)
draw.text((658, y + 36), "자본으로 사 생태계를 완성한 사건", font=bold(18), fill=BLUE)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.20  |  SpaceX · Cursor  ·  CNBC · Quartz · Forbes", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-20_스페이스X_커서인수_핵심요약.png")
img.save(out)
print("Saved:", out)
