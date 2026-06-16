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
draw.rectangle([0, 0, W, 4], fill=BLUE)
draw.rectangle([0, 0, 4, H], fill=BLUE)

# ── 헤더 ──
draw.text((32, 18), "AEHR (Aehr Test Systems)", font=bold(40), fill=BLUE)
draw.text((32, 72), "매출은 반토막, 수주는 사상 최대  —  번인 장비의 시차", font=bold(24), fill=WHITE)
draw.text((32, 108), "웨이퍼 레벨 번인(WLBI) 사실상 독점  ·  SiC에서 AI·포토닉스로 확장 중", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("Q3 FY2026 매출",      "$10.3M",   "전년비 -44%  (출하 기준, 후행)",       RED),
    ("분기 수주",           "$37.2M",   "book-to-bill 3.5배 초과",              GREEN),
    ("유효 백로그",         "$50.9M",   "사상 최대  /  하반기 수주 $92M+",       AMBER),
    ("시총 / 1년 수익률",   "~$3.4B",   "주가 ~$108  /  1년 약 +10배",          CYAN),
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

# ── 오른쪽: 포인트 & 리스크 ──
draw.text((644, 158), "포인트 & 리스크", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (BLUE,  "수주가 매출에 선행한다",
     "B/B 3.5배  —  매출은 출하 시점, 수주는 6~12개월 앞"),
    (GREEN, "WLBI 독점 + 소모품 반복매출",
     "FOX 장비 + WaferPak 컨택터의 면도기-면도날 구조"),
    (TEAL,  "단일고객에서 멀티마켓으로",
     "SiC(온세미)  →  AI 프로세서·실리콘 포토닉스·플래시"),
    (RED,   "리스크",
     "최대 AI 물량은 아직 PO 아닌 forecast  /  매출 20배"),
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
    "① Q4 FY2026 — 비GAAP 흑자 복귀 여부",
    "② AI 고객 forecast → 확정 PO 전환",
    "③ 백로그의 매출 전환 타임라인",
]
for line in checks:
    draw.text((644, y), line, font=font(17), fill=GRAY)
    y += 30

# 요약 박스
draw.rounded_rectangle([644, y + 8, W - 32, y + 50], radius=8, fill=(10, 22, 40))
draw.text((658, y + 18), "수주는 사상 최대, 매출은 시차  —  관건은 forecast의 PO 전환", font=bold(18), fill=BLUE)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.16  |  Aehr IR · Motley Fool · LSEG · stockanalysis", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-16_AEHR_수주백로그_시차.png")
img.save(out)
print("Saved:", out)
