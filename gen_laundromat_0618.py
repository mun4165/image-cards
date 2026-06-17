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

ACCENT = AMBER  # 47만 달러의 함정 테마

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
draw.text((32, 18), "47만 달러의 함정", font=bold(40), fill=ACCENT)
draw.text((32, 72), "간호사 그만두고 빨래방으로 성공한 이야기를 투자자의 눈으로 다시 읽기", font=bold(24), fill=WHITE)
draw.text((32, 108), "성공담의 숫자는 매출이지 순익이 아니다 — 헤드라인 뒤의 구조를 본다", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 숫자 분해 ──
metrics = [
    ("헤드라인 매출",     "$47.5만",   "기사가 강조하는 '연 수익'",            AMBER),
    ("순마진 현실",       "20~35%",    "잘 굴러가는 빨래방 기준",              ORANGE),
    ("실제 손에 쥐는 돈",  "$10~15만",  "공과금·임대료·인력 차감 후 추정",      GREEN),
    ("인수가",           "$30만",      "맨손 창업이 아니라 운영 중인 가게 인수", BLUE),
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
draw.text((644, 158), "성공담을 읽는 네 가지 눈", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (AMBER, "매출은 순익이 아니다",
     "공과금만 매출의 20~30%를 먹는 업종"),
    (BLUE,  "창업이 아니라 현금흐름 인수",
     "검증된 가게를 산 게 진짜 핵심"),
    (RED,   "생존자 편향을 걷어내라",
     "폐업한 빨래방 수십 곳은 안 비춘다"),
    (GREEN, "본질은 반복 수요",
     "매주 끊기지 않는 귀찮은 일에 돈이 있다"),
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
draw.rounded_rectangle([644, y, W - 32, y + 62], radius=8, fill=(48, 32, 4))
draw.text((658, y + 12), "기계가 돈을 버는 게 아니다", font=bold(18), fill=AMBER)
draw.text((658, y + 36), "반복해서 올 이유를 만든 사람이 번다", font=bold(18), fill=AMBER)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.18  |  CNBC Make It — 빨래방 인수 사례", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-18_빨래방_47만달러함정.png")
img.save(out)
print("Saved:", out)
