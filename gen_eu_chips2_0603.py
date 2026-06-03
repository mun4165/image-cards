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
PURPLE    = (168, 85, 247)

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

# 상단·좌측 강조선 (BLUE — EU 느낌)
draw.rectangle([0, 0, W, 4], fill=BLUE)
draw.rectangle([0, 0, 4, H], fill=BLUE)

# ── 헤더 ──
draw.text((32, 18), "EU 기술 주권 패키지 — 2026.06.03 공식 발표", font=bold(36), fill=BLUE)
draw.text((32, 68), "CHIPS Act 2.0  :  공급 유치 → 수요 창출  /  포토닉스, 전략 인프라로 분류", font=bold(22), fill=WHITE)
draw.text((32, 104), "Technological Indispensability — 전 세계 공급망이 유럽 기술 없이 기능할 수 없는 구조", font=font(17), fill=GRAY)
draw.line([(32, 136), (W - 32, 136)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 패키지 핵심 내용 ──
draw.text((32, 150), "패키지 핵심 내용", font=bold(22), fill=WHITE)
draw.line([(32, 180), (590, 180)], fill=DARK_GRAY, width=1)

items = [
    (BLUE,   "CHIPS Act 2.0",
     "공급 측 → 수요 측 전환  /  수요 집계·조달 인센티브"),
    (CYAN,   "포토닉스 전략 인프라 지정",
     "SiPH·CPO를 EU가 구조적 우위 가능 도메인으로 분류"),
    (PURPLE, "Cloud & AI Development Act",
     "클라우드 주권 4단계 분류  /  AI 인프라 유럽화"),
    (GREEN,  "위기 관리 도구",
     "공급 충격 시 공동 구매·우선 주문 권한 부여"),
]
y = 192
for color, title, desc in items:
    draw.rectangle([28, y + 3, 32, y + 30], fill=color)
    draw.text((44, y), title, font=bold(20), fill=WHITE)
    draw.text((44, y + 28), desc, font=font(17), fill=GRAY)
    draw.line([(32, y + 72), (590, y + 72)], fill=DARK_GRAY, width=1)
    y += 80

# 왼쪽 하단: 배경 맥락
draw.text((32, y + 8), "배경", font=bold(18), fill=ORANGE)
draw.line([(32, y + 34), (590, y + 34)], fill=DARK_GRAY, width=1)
context = [
    "유럽 포토닉스 80개 기업·Photonics21·PhotonDelta 수년간 로비 성과",
    "EU 반도체 글로벌 점유율 10% 미만  —  미국·아시아 의존 탈피 목표",
    "2031년까지 통합 포토닉스 시장 +350% 성장, €650억 규모 전망",
]
cy = y + 44
for line in context:
    draw.text((32, cy), line, font=font(16), fill=GRAY)
    cy += 26

# 세로 구분선
draw.line([(620, 136), (620, H - 46)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 수혜 구조 ──
draw.text((644, 150), "유럽 포토닉스 수혜 구조", font=bold(22), fill=WHITE)
draw.line([(644, 180), (W - 32, 180)], fill=DARK_GRAY, width=1)

players = [
    (AMBER,  "X-FAB (XFAB)",
     "photonixFAB 컨소시엄 주도  /  EU SiPH 가치사슬 산업화"),
    (TEAL,   "Sivers Semiconductors (SIVE)",
     "유럽 AI DC용 CW 레이저  /  2027년 대량생산 목표"),
]
y = 192
for color, title, desc in players:
    draw.rectangle([640, y + 3, 644, y + 28], fill=color)
    draw.text((656, y), title, font=bold(19), fill=WHITE)
    draw.text((656, y + 26), desc, font=font(16), fill=GRAY)
    y += 56

# 구분선
draw.line([(644, y + 8), (W - 32, y + 8)], fill=DARK_GRAY, width=1)
draw.text((644, y + 18), "확인된 사실 vs 미확인", font=bold(20), fill=ORANGE)
y += 50

checks = [
    (GREEN, "✓  EU 패키지 6.3 발표  /  CHIPS Act 2.0  /  수요 인센티브 방향"),
    (GREEN, "✓  포토닉스 전략 인프라  /  X-FAB EU 펀딩 수령"),
    (RED,   "?  XFAB·SIVE 청사진 직접 명시  /  €30M~500M 자금 범위"),
]
for color, text in checks:
    draw.text((644, y), text, font=font(16), fill=color)
    y += 28

# 요약 박스
draw.rounded_rectangle([644, y + 8, W - 32, y + 50], radius=8, fill=(10, 18, 35))
draw.text((658, y + 18), "정책 방향 × 기술 방향 일치  —  세부 조문 확인 구간", font=bold(17), fill=BLUE)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.03  |  Euronews · Altair Media · X-FAB IR  |  개인 공부 기록, 투자 추천 아님", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-03_EU_CHIPS2_기술주권패키지.png")
img.save(out)
print("Saved:", out)
