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

# 상단·좌측 강조선 — TEAL (해양 테마)
draw.rectangle([0, 0, W, 4], fill=TEAL)
draw.rectangle([0, 0, 4, H], fill=TEAL)

# ── 헤더 ──
draw.text((32, 18), "세틀로직 (SATL)", font=bold(44), fill=TEAL)
draw.text((32, 72), "밴쿠버 해양 안보 컨퍼런스에 나온 이유", font=bold(28), fill=WHITE)
draw.text((32, 110), "Maritime Domain Awareness Summit 2026  ·  2026.06.03~04  ·  Vancouver", font=font(18), fill=GRAY)
draw.line([(32, 146), (W - 32, 146)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 고객 버티컬 현황 ──
draw.text((32, 158), "고객 버티컬 확장 현황", font=bold(22), fill=WHITE)
draw.line([(32, 188), (590, 188)], fill=DARK_GRAY, width=1)

verticals = [
    (GREEN,  "방위",      "$1,800만 본계약 (시범→정식 전환)  ·  골든돔 프로그램"),
    (BLUE,   "정보",      "NGA 상업위성 프로그램 공식 편입"),
    (TEAL,   "해양 안보", "Maritime Domain Awareness  ·  진행 중"),
]
y = 200
for color, title, desc in verticals:
    draw.rectangle([28, y + 4, 32, y + 36], fill=color)
    draw.text((44, y), title, font=bold(22), fill=WHITE)
    draw.text((44, y + 28), desc, font=font(17), fill=GRAY)
    draw.line([(32, y + 60), (590, y + 60)], fill=DARK_GRAY, width=1)
    y += 72

# 왼쪽 하단: 핵심 수치
y += 8
metrics = [
    ("수주잔고",   "$1.1억",  "역대 최고  ·  Q1 2026 기준"),
    ("최근 계약",  "$1,800만", "국제 방위 고객  ·  1년 고주파 관측 계약"),
]
for label, value, sub in metrics:
    draw.text((32, y), label, font=font(17), fill=GRAY)
    draw.text((32, y + 22), value, font=bold(28), fill=AMBER)
    draw.text((32, y + 56), sub, font=font(16), fill=GRAY)
    draw.line([(32, y + 78), (590, y + 78)], fill=DARK_GRAY, width=1)
    y += 90

# 세로 구분선
draw.line([(620, 143), (620, H - 46)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 왜 해양 안보인가 ──
draw.text((644, 158), "왜 해양 안보가 위성 데이터를 원하나", font=bold(22), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

reasons = [
    (CYAN,   "AIS만으로는 안 됨",
     "선박 식별 시스템은 끄면 그만  —  위에서 봐야 한다"),
    (TEAL,   "기존 정찰위성은 느리다",
     "하루 1회 재방문  →  세틀로직은 고주파 다회 촬영"),
    (GREEN,  "불법 조업·밀수·적국 함정",
     "실시간 해역 감시 수요  —  상업위성이 채우는 공백"),
]
y = 204
for color, title, desc in reasons:
    draw.rectangle([640, y + 3, 644, y + 30], fill=color)
    draw.text((656, y), title, font=bold(19), fill=WHITE)
    draw.text((656, y + 28), desc, font=font(17), fill=GRAY)
    y += 64

# ── 체크포인트 ──
draw.line([(644, y + 8), (W - 32, y + 8)], fill=DARK_GRAY, width=1)
draw.text((644, y + 18), "다음 체크포인트", font=bold(20), fill=ORANGE)
y += 50

checks = [
    "① 해양 안보 고객 계약 발표 여부 (수시)",
    "② Q2 실적 — 방위 버티컬 매출 비중 추이 (8월)",
    "③ 수주잔고 $1.1억 유지 또는 증가 여부",
]
for line in checks:
    draw.text((644, y), line, font=font(17), fill=GRAY)
    y += 30

# 요약 박스
draw.rounded_rectangle([644, y + 8, W - 32, y + 52], radius=8, fill=(10, 35, 38))
draw.text((658, y + 18), "세일즈가 움직이고 있다  —  버티컬이 쌓이는 중", font=bold(18), fill=TEAL)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.03  |  Satellogic IR · LinkedIn", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-03_SATL_해양안보서밋.png")
img.save(out)
print("Saved:", out)
