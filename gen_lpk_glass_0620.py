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

ACCENT = CYAN  # 유리·포토닉스 테마

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
draw.text((32, 18), "1년에 5배 오른 독일 레이저주, LPKF", font=bold(40), fill=ACCENT)
draw.text((32, 72), "유리 기판 시대의 곡괭이 — 저평가인가, 과열인가", font=bold(24), fill=WHITE)
draw.text((32, 108), "매출은 줄고 적자인데 주가는 연초 대비 +329%", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("주가 / 연초 대비",  "EUR 29.5 · +329%",  "52주 EUR 5.35 → 30.30 (사상최고 부근)",  GREEN),
    ("밸류에이션",       "시총 EUR 721M",     "EV/매출 약 6배 (매출은 역성장 중)",        ORANGE),
    ("실적 (TTM)",      "매출 EUR 115M",     "-12% · 순손실 EUR 17.5M · PER 산정불가",   RED),
    ("증권가 목표가",     "EUR 15.5 · Hold",   "현재가 대비 약 절반 수준",                 BLUE),
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
draw.text((644, 158), "기술은 진짜, 가격은 미래 선반영", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (GREEN, "차별적 기술 LIDE",
     "10um 이하 유리 미세가공 = 글래스 코어 길목"),
    (CYAN,  "첫 양산 주문 확보",
     "2026년 1분기 첫 양산용 발주"),
    (ORANGE, "본격 매출은 아직 앞",
     "업계 양산 2027 · TSMC 유리기판 2028"),
    (RED,   "선반영된 기대값",
     "본업 역성장·적자 위에 미래가치만 얹힘"),
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
draw.text((658, y + 12), "기술이 좋다 ≠ 지금 주식이 싸다", font=bold(18), fill=CYAN)
draw.text((658, y + 36), "발주·흑자전환·양산일정, 숫자로 확인하라", font=bold(18), fill=CYAN)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.20  |  stockanalysis.com · The Elec", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-20_LPK_유리기판_핵심요약.png")
img.save(out)
print("Saved:", out)
