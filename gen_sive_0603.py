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
draw.rectangle([0, 0, W, 4], fill=TEAL)
draw.rectangle([0, 0, 4, H], fill=TEAL)

# ── 헤더 ──
draw.text((32, 18), "SIVE (Sivers Semiconductors)", font=bold(40), fill=TEAL)
draw.text((32, 72), "GF 파트너십으로 신고가  —  광통신 물결의 첫 번째 계단", font=bold(24), fill=WHITE)
draw.text((32, 108), "GlobalFoundries SiPH 레퍼런스 기본 공급사 채택  ·  목표시장 $250억 (2030)", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("오늘 급등 (2026.06.02)",  "+60%",        "신고가 경신  /  SEK 92+",              GREEN),
    ("2026 YTD 수익률",         "+1,700%+",     "연초 대비 누적 상승",                  AMBER),
    ("파트너십 목표시장",        "$250억",       "2030년 플러거블 옵틱스 시장",          CYAN),
    ("선례 (LITE)",             "30억→750억",   "EML+플러거블로 25배 성장",             BLUE),
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
draw.text((644, 158), "투자 포인트 & 리스크", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (TEAL,  "CW 레이저 공급자 지위",
     "SiPH 칩은 레이저 없이 작동 불가  —  SIVE가 그 병목 점유"),
    (GREEN, "GF 레퍼런스 디자인 채택",
     "GF 칩 고객 = 자동으로 SIVE 레이저  /  영업 없이 수요 확보"),
    (AMBER, "CPO 두 번째 파도",
     "플러거블 이후 Co-Packaged Optics로 확장 경로 열림"),
    (RED,   "리스크",
     "매출 $33M 수준  /  현금 소진 중  /  CPO 상용화 지연 가능"),
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
    "① GF 칩 채택 고객사 공개 여부",
    "② CPO 상용화 일정 업데이트",
    "③ 현금 런웨이 — 다음 분기 실적",
]
for line in checks:
    draw.text((644, y), line, font=font(17), fill=GRAY)
    y += 30

# 요약 박스
draw.rounded_rectangle([644, y + 8, W - 32, y + 50], radius=8, fill=(8, 28, 26))
draw.text((658, y + 18), "첫 번째 디자인-윈 확정  —  CPO 상용화가 두 번째 촉매", font=bold(18), fill=TEAL)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.03  |  PR Newswire · StockTitan · CoinCentral", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-03_SIVE_GF파트너십_급등.png")
img.save(out)
print("Saved:", out)
