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
draw.rectangle([0, 0, W, 4], fill=AMBER)
draw.rectangle([0, 0, 4, H], fill=AMBER)

# ── 헤더 ──
draw.text((32, 18), "FOMC 프리뷰 (2026.06.17)", font=bold(40), fill=AMBER)
draw.text((32, 72), "다우 신고가 vs 나스닥 하락  —  갈라진 시장이 연준을 기다린다", font=bold(24), fill=WHITE)
draw.text((32, 108), "동결은 정해졌다  ·  진짜 변수는 점도표와 신임 의장 워시의 첫 회견", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("다우 (6/16)",       "+0.64%",   "약 +329p, 52,000 코앞 신고가권",          GREEN),
    ("나스닥 (6/16)",     "하락",     "26,376  /  엔비디아·브로드컴·마이크론 주도",  RED),
    ("FOMC 동결 확률",    "~97%",     "금리 3.50~3.75% 유지  ·  6/17 오후 2시(ET)", AMBER),
    ("다음 캘린더",       "6/24",     "마이크론(MU) 실적",                        CYAN),
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

# ── 오른쪽: 관전 포인트 ──
draw.text((644, 158), "이번 회의 관전 포인트", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (AMBER, "점도표(dot plot)",
     "올해 남은 금리 경로 전망이 갱신된다"),
    (RED,   "워시 첫 기자회견",
     "신임 의장  —  매파 어조 시 인하 기대 축소"),
    (BLUE,  "시장 vs 연준 괴리",
     "쏠린 포지션  —  서프라이즈 시 반응 증폭"),
    (TEAL,  "일본 BOJ",
     "예고된 인상은 선반영  /  엔캐리 청산만 잔존 리스크"),
]
y = 204
for color, title, desc in points:
    draw.rectangle([640, y + 3, 644, y + 30], fill=color)
    draw.text((656, y), title, font=bold(20), fill=WHITE)
    draw.text((656, y + 28), desc, font=font(17), fill=GRAY)
    y += 62

# ── 체크포인트 ──
draw.line([(644, y + 4), (W - 32, y + 4)], fill=DARK_GRAY, width=1)
draw.text((644, y + 14), "무엇을 볼 것인가", font=bold(20), fill=ORANGE)
y += 46

checks = [
    "① 점도표 — 연내 인하 횟수 전망",
    "② 워시 어조 — 매파 vs 비둘기",
    "③ 성장주 → 가치주 로테이션 지속 여부",
]
for line in checks:
    draw.text((644, y), line, font=font(17), fill=GRAY)
    y += 30

# 요약 박스
draw.rounded_rectangle([644, y + 8, W - 32, y + 50], radius=8, fill=(38, 28, 8))
draw.text((658, y + 18), "동결은 비이벤트  —  점도표와 워시의 어조가 방향을 정한다", font=bold(18), fill=AMBER)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.16  |  TheStreet · CME FedWatch · Motley Fool", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-16_FOMC_프리뷰_갈라진시장.png")
img.save(out)
print("Saved:", out)
