from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-17"
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

ACCENT = ORANGE  # RKLB 강조색 (로켓 화염)

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
draw.text((32, 18), "RKLB (Rocket Lab)", font=bold(40), fill=ACCENT)
draw.text((32, 72), "'페이로드 통합 완료' 트윗  —  늘 하던 일을 뉴스처럼 발표하는 이유", font=bold(24), fill=WHITE)
draw.text((32, 108), "90번째 Electron 'Ten Owl Of Ten'  ·  6/18 NZT  ·  신스펙티브 StriX 10번째", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("Q1 2026 총매출",        "$200.3M",      "+64% YoY  /  분기 최대",            GREEN),
    ("매출 구조",             "Space 68%",    "Launch 32%  —  발사는 더 이상 주력 아님", BLUE),
    ("총 백로그",             "$2.2B",        "정부 비중 49% (Q4 35%→상승)",       TEAL),
    ("Neutron 첫 발사 목표",   "2026 Q4",      "2025→지연  /  1단 탱크 시험 파열",   AMBER),
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
draw.text((644, 158), "트윗 한 꺼풀 벗기기", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (TEAL,  "페이로드 통합 = 루틴",
     "매 발사마다 하는 표준 조립  /  뉴스 아닌 카운트다운 마케팅"),
    (BLUE,  "발사 잘하는 건 호재 아님",
     "성공=기대치 충족, 실패만 처벌  /  하한선이지 업사이드 아님"),
    (GREEN, "매출 2/3가 Space Systems",
     "발사는 신뢰의 토대  /  돈은 위성·부품 제조에서 번다"),
    (RED,   "리스크 — Neutron 지연",
     "주가 진짜 레버리지  /  Electron 트윗 100개보다 Neutron 1발"),
]
y = 204
for color, title, desc in points:
    draw.rectangle([640, y + 3, 644, y + 30], fill=color)
    draw.text((656, y), title, font=bold(20), fill=WHITE)
    draw.text((656, y + 28), desc, font=font(17), fill=GRAY)
    y += 62

# ── 체크포인트 ──
draw.line([(644, y + 4), (W - 32, y + 4)], fill=DARK_GRAY, width=1)
draw.text((644, y + 14), "진짜 체크포인트", font=bold(20), fill=ORANGE)
y += 46

checks = [
    "① Neutron 첫 발사가 2026 Q4를 지키는지",
    "② Space Systems 백로그·정부 비중 추이",
    "③ 6/18 발사는 성공이 기본값 — 재료 아님",
]
for line in checks:
    draw.text((644, y), line, font=font(17), fill=GRAY)
    y += 30

# 요약 박스
draw.rounded_rectangle([644, y + 8, W - 32, y + 50], radius=8, fill=(40, 22, 8))
draw.text((658, y + 18), "잘하는지가 아니라, 매출이 어디로 이동하는지를 본다", font=bold(18), fill=ORANGE)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.17  |  Rocket Lab · RKLB Q1 2026 실적 · SpaceNews", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-17_RKLB_페이로드통합_트윗해부.png")
img.save(out)
print("Saved:", out)
