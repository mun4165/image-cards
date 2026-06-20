from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-20"
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

ACCENT = BLUE  # 네오클라우드 테마

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
draw.text((32, 18), "같은 'ARR' 다른 무게 — 네비우스 vs 아이렌", font=bold(38), fill=ACCENT)
draw.text((32, 70), "한쪽은 들어온 돈, 한쪽은 약속된 돈", font=bold(24), fill=WHITE)
draw.text((32, 106), "1년 주가는 둘 다 약 5배 — 그러나 서 있는 지점이 정반대다", font=font(18), fill=GRAY)
draw.line([(32, 140), (W - 32, 140)], fill=DARK_GRAY, width=1)

# ── 좌우 컬럼 헤더 ──
LX, RX = 32, 664
draw.text((LX, 156), "NEBIUS · NBIS", font=bold(26), fill=GREEN)
draw.text((LX, 188), "탑다운 — 계약 먼저, 매출이 빠르게 찍힌다", font=font(17), fill=GRAY)
draw.text((RX, 156), "IREN", font=bold(26), fill=ORANGE)
draw.text((RX, 188), "바텀업 — 전력·GPU 먼저, 계곡을 건너는 중", font=font(17), fill=GRAY)

# 세로 구분선
draw.line([(632, 150), (632, H - 92)], fill=DARK_GRAY, width=1)

# ── 좌측: NBIS ──
left = [
    ("이번 분기 총매출",  "$399M",        "+684% YoY", GREEN),
    ("AI 매출 비중",      "약 94%",        "AI ≈ $375M", GREEN),
    ("ARR 성격",         "실현 $1.9B",    "이미 들어오는 런레이트", CYAN),
    ("분기 손익",         "흑자전환",       "Adj EBITDA +$129.5M", GREEN),
]
y = 228
for label, value, sub, color in left:
    draw.text((LX, y), label, font=font(16), fill=GRAY)
    draw.text((LX, y + 20), value, font=bold(28), fill=color)
    draw.text((LX, y + 54), sub, font=font(15), fill=GRAY)
    draw.line([(LX, y + 76), (600, y + 76)], fill=DARK_GRAY, width=1)
    y += 88

# ── 우측: IREN ──
right = [
    ("이번 분기 총매출",  "$144.8M",      "직전 $184.7M서 감소", RED),
    ("AI 매출 비중",      "약 23%",        "AI $33.6M · 채굴 77%", ORANGE),
    ("ARR 성격",         "약정 $3.1B",    "실현은 연 ~$134M뿐", AMBER),
    ("분기 손익",         "순손실",         "-$247.8M (전환 비용)", RED),
]
y = 228
for label, value, sub, color in right:
    draw.text((RX, y), label, font=font(16), fill=GRAY)
    draw.text((RX, y + 20), value, font=bold(28), fill=color)
    draw.text((RX, y + 54), sub, font=font(15), fill=GRAY)
    draw.line([(RX, y + 76), (W - 32, y + 76)], fill=DARK_GRAY, width=1)
    y += 88

# ── 하단 요약 박스 ──
by = H - 80
draw.rounded_rectangle([32, by, W - 32, by + 50], radius=8, fill=(15, 23, 42))
draw.text((48, by + 9), "같은 'ARR'도 들어온 돈인지 약속된 돈인지부터 구분하라", font=bold(19), fill=BLUE)
draw.text((48, by + 30), "아이렌 변곡점 = 약정과 실현의 거리가 좁혀지는 속도 (8월 방향성 · 11월 실현)", font=font(15), fill=GRAY)

# ── 푸터 ──
draw.text((32, H - 22), "2026.06.20  |  NBIS Q1'26 · IREN Q3 FY26 · stockanalysis.com", font=font(14), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-20_NBIS_IREN_ARR약정vs실현.png")
img.save(out)
print("Saved:", out)
