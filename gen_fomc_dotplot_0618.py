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

ACCENT = AMBER  # 매파 전환 테마

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
draw.text((32, 18), "점도표가 방향을 틀었다", font=bold(40), fill=ACCENT)
draw.text((32, 72), "금리는 동결, 그런데 연준의 시선은 인하 → 인상으로 뒤집혔다", font=bold(24), fill=WHITE)
draw.text((32, 108), "점도표(dot plot) = 연준 위원들이 적정 금리를 점으로 찍은 전망표 · 2026.06.17 FOMC", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("기준금리 결정",         "3.50~3.75% 동결",  "표결 12 대 0 만장일치 · 시장 예상 97%",   GRAY),
    ("올해 말 금리 중앙값",   "3.4% → 3.8%",      "3월=연내 인하 → 6월=연내 최소 1회 인상",  AMBER),
    ("위원 점 분포",          "인상9·동결8·인하1", "딱 절반이 '더 올려야 한다'로 이동",        ORANGE),
    ("2026 물가 전망 상향",   "2.7% → 3.6%",      "헤드라인 +0.9%p · 코어 2.7→3.3%",        RED),
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
draw.text((644, 158), "동결인데 왜 매파인가", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (AMBER, "숫자는 그대로, 방향은 전환",
     "동결은 비이벤트 / 진짜 메시지는 점도표에"),
    (RED,   "물가 전망을 한 번에 상향",
     "중동발 공급 차질 → 인하 명분이 약해졌다"),
    (BLUE,  "워시 신임 의장 첫 회의",
     "본인 점 미제출 · 인하 편향 문구 삭제"),
    (GREEN, "시장은 인상 경계로 선회",
     "트레이더, 이르면 10월 인상 가격에 반영"),
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
draw.rounded_rectangle([644, y, W - 32, y + 62], radius=8, fill=(36, 26, 6))
draw.text((658, y + 12), "동결 = 정해진 결과", font=bold(18), fill=AMBER)
draw.text((658, y + 36), "점도표 3.4% → 3.8% = 진짜 변화", font=bold(18), fill=AMBER)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.17 FOMC  |  금리 동결 · 점도표 매파 전환 · 케빈 워시 첫 회의", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-18_FOMC_점도표방향전환.png")
img.save(out)
print("Saved:", out)
