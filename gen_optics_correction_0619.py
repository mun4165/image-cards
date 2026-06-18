from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-19"
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

ACCENT = CYAN  # 광학·포토닉스 테마

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
draw.text((32, 18), "광학섹터가 왜 이렇게 빠지나", font=bold(40), fill=ACCENT)
draw.text((32, 72), "수요 붕괴가 아니라 과열의 되돌림 — AI 광통신주 조정", font=bold(24), fill=WHITE)
draw.text((32, 108), "리포트 한 장에 무너졌지만, 수요 데이터는 여전히 위를 가리킨다", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("6/9 셀오프",      "AAOI -17%",   "POET -12% · COHR -11% · LITE -8%",   RED),
    ("고점 대비 낙폭",   "AAOI -47%",   "COHR -40% · LITE -35% · FN -13%",    ORANGE),
    ("직접 방아쇠",     "CPO 지연",     "SemiAnalysis 리포트 한 장",           AMBER),
    ("매크로",         "Fed 점도표",   "18명 중 9명 2026 금리인상 전망",       BLUE),
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
draw.text((644, 158), "수요가 아니라 멀티플이 흔들렸다", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (GREEN, "수요는 안 꺾였다",
     "메타·오라클 capex 2배 / 1.6T 30~40% 부족"),
    (ORANGE, "과열의 되돌림",
     "올랐던 만큼 빠진 멀티플·수급 조정"),
    (RED,   "같은 악재, 갈린 낙폭",
     "AAOI -17% vs LITE -8% = 펀더 아닌 수급"),
    (CYAN,  "CPO냐 꽂는 방식이냐",
     "지연은 종목마다 방향이 정반대"),
]
y = 204
for color, title, desc in points:
    draw.rectangle([640, y + 3, 644, y + 30], fill=color)
    draw.text((656, y), title, font=bold(20), fill=WHITE)
    draw.text((656, y + 28), desc, font=font(17), fill=GRAY)
    y += 62

# 요약 박스
draw.line([(644, y + 4), (W - 32, y + 4)], fill=DARK_GRAY, width=1)
y += 18
draw.rounded_rectangle([644, y, W - 32, y + 62], radius=8, fill=(6, 34, 40))
draw.text((658, y + 12), "빠졌다고 한 바구니에 담기 전에", font=bold(18), fill=CYAN)
draw.text((658, y + 36), "내 종목이 어느 기술 라인인지부터 확인하라", font=bold(18), fill=CYAN)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.19  |  SemiAnalysis · 24/7 Wall St · McKinsey", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-19_광학섹터_조정_핵심요약.png")
img.save(out)
print("Saved:", out)
