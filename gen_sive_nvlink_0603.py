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

# 강조선
draw.rectangle([0, 0, W, 4], fill=TEAL)
draw.rectangle([0, 0, 4, H], fill=TEAL)

# ── 헤더 ──
draw.text((32, 18), "SIVE (Sivers Semiconductors)", font=bold(40), fill=TEAL)
draw.text((32, 72), "NVLink CPO 레이저 공급망 — 팩트체크", font=bold(24), fill=WHITE)
draw.text((32, 108), "Ayar Labs NVLink 합류  ·  GFS 레퍼런스 레이저 채택  ·  2026.06.02", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("당일 급등 (2026.06.02)",      "+50~70%",     "GFS 협업 발표 당일 급등 / 신고가",          GREEN),
    ("Ayar Labs 최근 펀딩",          "$500M",       "2026 시리즈 E  /  Nvidia · AMD 참여",        CYAN),
    ("애널리스트 목표가 (Redeye)",   "6.20 SEK",    "유일한 커버리지  /  현재가 대비 크게 낮음",  RED),
    ("볼륨 램프 예상 시점",          "2027년~",     "경영진 가이던스  /  Q1 매출 -22% YoY",       AMBER),
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

# ── 오른쪽: 확인 결과 ──
draw.text((644, 158), "팩트체크 결과", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (TEAL,  "확인됨 — Ayar 레이저 공급사",
     "Lumentum·Macom 웹사이트 제거  /  Sivers 단독 공개 공급사"),
    (GREEN, "확인됨 — GFS 생태계 연결",
     "Marvell · Lightmatter · Ayar 모두 GFS 플랫폼 사용"),
    (AMBER, "추론 — Celestial·Lightmatter 고객 관계",
     "출처가 단일 인물  /  공식 공시·독립 미디어 확인 없음"),
    (RED,   "리스크 — 주가 선반영",
     "내러티브 이미 50~70% 반영  /  GFS 협약에 물량 보장 없음"),
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
    "① Marvell·Lightmatter 고객 관계 1차 소스 확인",
    "② GFS 레퍼런스 협약 → 실수주 계약 전환 여부",
    "③ Q2 2026 실적  —  매출 반등 확인",
]
for line in checks:
    draw.text((644, y), line, font=font(17), fill=GRAY)
    y += 30

# 요약 박스
draw.rounded_rectangle([644, y + 8, W - 32, y + 50], radius=8, fill=(8, 28, 26))
draw.text((658, y + 18), "방향은 맞다  —  주가 선반영 여부가 진짜 질문", font=bold(18), fill=TEAL)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.03  |  Ayar Labs · GlobalFoundries · Sivers IR  |  개인 공부 기록, 투자 추천 아님", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-03_SIVE_NVLink_CPO팩트체크.png")
img.save(out)
print("Saved:", out)
