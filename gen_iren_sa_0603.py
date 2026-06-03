from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-03"
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
draw.rectangle([0, 0, W, 4], fill=GREEN)
draw.rectangle([0, 0, 4, H], fill=GREEN)

# ── 헤더 ──
draw.text((32, 18), "IREN (Iris Energy)", font=bold(40), fill=GREEN)
draw.text((32, 72), "호주 첫 데이터센터 캠퍼스  —  사우스오스트레일리아 800MW", font=bold(24), fill=WHITE)
draw.text((32, 108), "송전 연결 협약 서명  ·  아태 지역 최대급  ·  2026.06.03 발표", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("캠퍼스 규모",       "800MW",       "원전 1기 출력의 80% — 아태 최대급",         GREEN),
    ("위치",              "Bundey, SA",  "애들레이드 북동쪽 125km",                   CYAN),
    ("전력 목표",         "100% 재생",   "SA 주 2027년 100% 순재생에너지 목표",       TEAL),
    ("해저케이블 연결",   "4개국",       "싱가포르 · 한국 · 일본 · 인도네시아",      BLUE),
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

# ── 오른쪽: 투자 포인트 & 리스크 ──
draw.text((644, 158), "포인트 & 리스크", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (GREEN, "아태 시장 첫 진출",
     "북미 일변도 포트폴리오  —  지역 다변화 본격화"),
    (TEAL,  "클린에너지 정렬",
     "SA 재생에너지 목표 + IREN 클린컴퓨트 전략 일치"),
    (CYAN,  "전략적 연결성",
     "해저케이블 4개국 직결  —  AI 수요 아태 포지셔닝"),
    (RED,   "리스크",
     "고객 미확정  /  규제 승인 전  /  착공 미정 초기 단계"),
]
y = 204
for color, title, desc in points:
    draw.rectangle([640, y + 3, 644, y + 30], fill=color)
    draw.text((656, y), title, font=bold(20), fill=WHITE)
    draw.text((656, y + 28), desc, font=font(17), fill=GRAY)
    y += 62

# ── 체크포인트 ──
draw.line([(644, y + 4), (W - 32, y + 4)], fill=DARK_GRAY, width=1)
draw.text((644, y + 14), "다음 체크포인트", font=bold(20), fill=ORANGE)
y += 46

checks = [
    "① SA 캠퍼스 앵커 고객 발표 여부",
    "② 규제 승인 완료 시점",
    "③ 착공 일정 구체화",
]
for line in checks:
    draw.text((644, y), line, font=font(17), fill=GRAY)
    y += 30

# 요약 박스
draw.rounded_rectangle([644, y + 8, W - 32, y + 50], radius=8, fill=(8, 26, 18))
draw.text((658, y + 18), "송전 확보 완료  —  고객 계약이 나오는 순간이 실질 트리거", font=bold(18), fill=GREEN)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.03  |  GlobeNewswire · IREN IR", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-03_IREN_SA_800MW.png")
img.save(out)
print("Saved:", out)
