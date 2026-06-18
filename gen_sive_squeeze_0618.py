from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-18"
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

ACCENT = AMBER  # 수급·경계 테마

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
draw.rectangle([0, 0, W, 4], fill=ACCENT)
draw.rectangle([0, 0, 4, H], fill=ACCENT)

# ── 헤더 ──
draw.text((32, 18), "10% 올랐는데 뉴스가 없다", font=bold(40), fill=ACCENT)
draw.text((32, 72), "숏스퀴즈와 펀더멘털을 구분하는 법 — SIVE 6/17 사례", font=bold(24), fill=WHITE)
draw.text((32, 108), "뉴스 없는 급등은 '회사가 좋아졌다'가 아니라 '수급이 쏠렸다'일 때가 많다", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("6/17 급등",            "+10.10%",     "101.90 SEK  /  당일 신규 뉴스 0",       AMBER),
    ("3월 저점 대비",         "약 30배",      "전형적 숏스퀴즈 궤적",                  RED),
    ("펀더 재료(GF·올스페이스)", "며칠~몇주 전", "이미 알려진 정보  /  오늘 신규 아님",    GRAY),
    ("희석 변수",            "신주 ~15%",    "6/15 나스닥 2차상장 투표",              BLUE),
]
y = 158
for label, value, sub, color in metrics:
    draw.text((32, y), label, font=font(17), fill=GRAY)
    draw.text((32, y + 22), value, font=bold(28), fill=color)
    draw.text((32, y + 56), sub, font=font(16), fill=GRAY)
    draw.line([(32, y + 80), (590, y + 80)], fill=DARK_GRAY, width=1)
    y += 92

# 세로 구분선
draw.line([(620, 140), (620, H - 46)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 핵심 논지 ──
draw.text((644, 158), "가격과 뉴스를 분리하라", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (AMBER, "'펀더 있다' ≠ '오늘 펀더로 올랐다'",
     "이 글의 핵심 — 두 가지를 섞지 마라"),
    (RED,   "숏스퀴즈란",
     "공매도 커버 매수가 가격을 더 밀어올리는 연쇄"),
    (GREEN, "펀더는 펀더 뉴스로 확인",
     "실적 반등 · 확정 발주(PO)에서 온다"),
    (BLUE,  "스퀴즈는 꺼지면 리프라이싱",
     "결국 펀더가 정당화하는 수준으로 재매김"),
]
y = 204
for color, title, desc in points:
    draw.rectangle([640, y + 3, 644, y + 30], fill=color)
    draw.text((656, y), title, font=bold(20), fill=WHITE)
    draw.text((656, y + 28), desc, font=font(17), fill=GRAY)
    y += 62

# 요약 박스
draw.line([(644, y + 4), (W - 32, y + 4)], fill=DARK_GRAY, width=1)
y += 18
draw.rounded_rectangle([644, y, W - 32, y + 62], radius=8, fill=(40, 30, 6))
draw.text((658, y + 12), "이유 없이 급등했다면, 먼저 한 가지를 물어라", font=bold(18), fill=AMBER)
draw.text((658, y + 36), "오늘 새 뉴스가 있었는가", font=bold(18), fill=AMBER)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.18  |  stockanalysis · PR Newswire · 회사 공시", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-18_SIVE_숏스퀴즈vs펀더_핵심요약.png")
img.save(out)
print("Saved:", out)
