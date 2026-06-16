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
draw.rectangle([0, 0, W, 4], fill=RED)
draw.rectangle([0, 0, 4, H], fill=RED)

# ── 헤더 ──
draw.text((32, 18), "BoJ, 정책금리 1.00%로 인상", font=bold(40), fill=RED)
draw.text((32, 72), "예고된 한 걸음  —  테이퍼링의 끝을 못박다", font=bold(24), fill=WHITE)
draw.text((32, 108), "일본은행 정책결정회의  ·  6월 17일 시행  ·  '여전히 완화적' 기조 유지", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("정책금리",            "0.75% → 1.00%",  "25bp 인상  /  추가 인상 여지 열어둠",   GREEN),
    ("표결 (금리 · 테이퍼)", "찬성 7 : 반대 1",  "아사다 위원 반대  ·  중도 노선",        AMBER),
    ("테이퍼 바닥 (2027.4~)", "월 2조 엔",       "JGB 매입 축소 중단, 하한선 고정",       CYAN),
    ("JGB 보유잔액 전망",    "-36~39%",        "2024.6 대비 2030.3까지 감소 경로",     BLUE),
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

# ── 오른쪽: 핵심 포인트 ──
draw.text((644, 158), "핵심 포인트", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (TEAL,  "명목 1% = 긴축 아닌 완화 강도 조절",
     "실질금리 단기·중기 구간 여전히 마이너스"),
    (GREEN, "테이퍼 종착지 명시 = 변동성 안전판",
     "급등 시 매입 확대·지정가 오퍼레이션으로 대응"),
    (AMBER, "양 극단에서 반대표 → 중도",
     "다카타·다무라 '더 빨리' vs 아사다 '더 신중'"),
    (RED,   "물가 압력 — 유가 전가 빠름",
     "CPI 2% 크게 상회 가속  /  광범위한 상승 위험"),
]
y = 204
for color, title, desc in points:
    draw.rectangle([640, y + 3, 644, y + 30], fill=color)
    draw.text((656, y), title, font=bold(20), fill=WHITE)
    draw.text((656, y + 28), desc, font=font(17), fill=GRAY)
    y += 62

# ── 체크포인트 ──
draw.line([(644, y + 4), (W - 32, y + 4)], fill=DARK_GRAY, width=1)
draw.text((644, y + 14), "주시할 변수", font=bold(20), fill=ORANGE)
y += 46

checks = [
    "① 유가·중동 정세 → 물가 전가 속도",
    "② 글로벌 AI 수요 흐름",
    "③ 환율 변동이 경제·물가에 미치는 영향",
]
for line in checks:
    draw.text((644, y), line, font=font(17), fill=GRAY)
    y += 30

# 요약 박스
draw.rounded_rectangle([644, y + 8, W - 32, y + 50], radius=8, fill=(36, 12, 12))
draw.text((658, y + 18), "올릴 여지는 열되, 푸는 속도는 바닥을 고정", font=bold(18), fill=RED)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.16  |  Bank of Japan 정책결정회의 발표", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-16_BoJ_금리인상_테이퍼종료.png")
img.save(out)
print("Saved:", out)
