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
draw.rectangle([0, 0, W, 4], fill=CYAN)
draw.rectangle([0, 0, 4, H], fill=CYAN)

# ── 헤더 ──
draw.text((32, 18), "CW 레이저 — CPO가 만든 새 병목", font=bold(40), fill=CYAN)
draw.text((32, 72), "하이퍼스케일러가 '레이저'를 사재기하기 시작했다", font=bold(24), fill=WHITE)
draw.text((32, 108), "AMD·엔비디아, 엔비디아발 병목 피하려 CW 레이저 대규모 PO 협상설", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 팩트 ──
metrics = [
    ("무엇이 바뀌었나",      "EML → CW",     "CPO가 레이저를 모듈 밖 '외부 광원'으로 분리",   CYAN),
    ("수요 단위 변화",       "채널 단위",     "CPO 스위치 1대 = 외부 CW 광원 수십 개",         GREEN),
    ("공급 제약",           "1군이 막혔다",  "루멘텀·코히어런트, EML 계약에 능력 묶임",        AMBER),
    ("잉여 능력은 어디에",   "일본·마콤",     "스미토모·후루카와 등 검증된 여력 거론",          BLUE),
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

# ── 오른쪽: 해석 & 걸러야 할 것 ──
draw.text((644, 158), "해석 & 걸러야 할 것", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (CYAN,  "부족은 상류로 번진다",
     "레이저 → 에피웨이퍼 → InP 기판  /  기판은 소수에 집중된 길목"),
    (GREEN, "검증(퀄) 게이트가 진짜 관문",
     "퀄 1~2년  /  급할수록 검증된 1군·일본계로 물량이 먼저 간다"),
    (AMBER, "'참조 레이저' ≠ 양산 공급",
     "설계 평가에 이름 = 초기 단계  /  단독 양산과는 다른 이야기"),
    (RED,   "채택 속도가 변수",
     "플러거블·LPO 잔존  /  CPO 보급 곡선이 수요 시점을 좌우"),
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
    "① '보도'가 '계약·매출'로 넘어가는 시점",
    "② 엔비디아·AMD CPO 스위치 양산 일정",
    "③ 레이저·에피·InP 백로그의 매출 전환 속도",
]
for line in checks:
    draw.text((644, y), line, font=font(17), fill=GRAY)
    y += 30

# 요약 박스
draw.rounded_rectangle([644, y + 8, W - 32, y + 50], radius=8, fill=(8, 26, 30))
draw.text((658, y + 18), "병목은 실재 — 다만 '부족'과 '수혜 종목'은 별개다", font=bold(18), fill=CYAN)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.16  |  TrendForce · Rosenblatt 보도 기반", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-16_CW레이저_CPO병목.png")
img.save(out)
print("Saved:", out)
