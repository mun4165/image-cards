from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-05"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
RED       = (239, 68, 68)
ORANGE    = (249, 115, 22)
AMBER     = (245, 158, 11)
GREEN     = (52, 211, 153)
CYAN      = (6, 182, 212)
PURPLE    = (167, 139, 250)

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)

def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

def make_base(accent):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=GRID, width=1)
    draw.rectangle([0, 0, W, 4], fill=accent)
    draw.rectangle([0, 0, 4, H], fill=accent)
    return img, ImageDraw.Draw(img)

def footer(draw, date_str, source_str):
    draw.line([(60, H - 52), (W - 60, H - 52)], fill=DARK_GRAY, width=1)
    draw.text((60, H - 36), f"{date_str}  |  {source_str}", font=font(17), fill=GRAY)


img, draw = make_base(CYAN)

# ── 헤더 ──
draw.text((60, 18), "LPTH — 노스런이 10% 아래로 내려가는 중이다", font=bold(34), fill=WHITE)
draw.text((60, 62), "오퍼링 구주매출 이후 지분 변화 · SEC 공시 의무 기준선", font=font(20), fill=GRAY)
draw.line([(60, 98), (W - 60, 98)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 지분 변화 타임라인 ──
lx = 60
draw.text((lx, 112), "노스런 지분 변화", font=bold(21), fill=GRAY)

rows = [
    ("2026.02.24", "13D/A 공시",               "17.7%", WHITE),
    ("2026.03.04", "13D/A 공시",               "16.2%", GRAY),
    ("2026.03",    "우선주 전환 후 매도 ($12)",  "—",     GRAY),
    ("2026.05.04", "13D/A 공시",               "14.7%", AMBER),
    ("2026.05",    "공개시장 매도 ($12~13)",     "—",     GRAY),
    ("2026.06.03", "오퍼링 구주매출 $14 × 357만주", "~9.6%", ORANGE),
]

y = 144
for date, event, stake, color in rows:
    draw.text((lx, y),        date,  font=font(15), fill=GRAY)
    draw.text((lx + 110, y),  event, font=font(15), fill=color)
    draw.text((lx + 460, y),  stake, font=bold(18), fill=color)
    draw.line([(lx, y + 30), (lx + 560, y + 30)], fill=DARK_GRAY, width=1)
    y += 38

# 10% 기준선 강조 박스
y += 4
draw.rounded_rectangle([lx, y, lx + 560, y + 52], radius=8, fill=(30, 50, 60))
draw.rectangle([lx, y, lx + 4, y + 52], fill=CYAN)
draw.text((lx + 16, y + 8),  "▶  현재 추정 지분 ~9.6%", font=bold(20), fill=CYAN)
draw.text((lx + 16, y + 32), "잔여 우선주 전환 예정분 약 640만주 상당 보유 중", font=font(16), fill=GRAY)

# 취득단가 vs 매도단가
y += 64
draw.line([(lx, y), (lx + 560, y)], fill=DARK_GRAY, width=1)
y += 12
draw.text((lx, y), "우선주 취득 $2.15  →  오퍼링 매도 $14.00  =  수익률 6배+", font=bold(18), fill=GREEN)

# ── 세로 구분선 ──
draw.line([(648, 98), (648, H - 60)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 오퍼링 구조 ──
rx = 672
draw.text((rx, 112), "오퍼링 구조 ($1억)", font=bold(21), fill=GRAY)

deals = [
    ("Primary",   "신주 3,571,400주  →  라이트패스 수취",   "$4,700만",  CYAN),
    ("Secondary", "구주 3,571,400주  →  노스런 수취",       "$5,000만",  ORANGE),
]
y = 144
for tag, desc, amount, color in deals:
    draw.rectangle([rx, y, rx + 4, y + 56], fill=color)
    draw.text((rx + 14, y),      tag,    font=bold(20), fill=color)
    draw.text((rx + 14, y + 26), desc,   font=font(16), fill=GRAY)
    draw.text((rx + 14, y + 44), amount, font=bold(18), fill=color)
    y += 72

draw.line([(rx, y), (W - 60, y)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 10% 기준 공시 의무 ──
y += 12
draw.text((rx, y), "10%  기준선 — 공시 의무가 달라진다", font=bold(21), fill=GRAY)
y += 34

above = [
    ("Section 16 내부자 분류",         WHITE),
    ("Form 4  —  거래 후 2영업일 내 공시", AMBER),
    ("단기매매차익 반환 의무 (6개월)",    AMBER),
]
draw.text((rx, y), "10% 이상", font=bold(17), fill=GREEN)
y += 26
for item, color in above:
    draw.text((rx + 12, y), f"·  {item}", font=font(16), fill=color)
    y += 24

y += 8
below = [
    ("Form 4 공시 의무 소멸",         ORANGE),
    ("13F 연간 보고서로만 파악 가능",   ORANGE),
    ("실시간 매매 동향 추적 불가",      RED),
]
draw.text((rx, y), "10% 미만", font=bold(17), fill=RED)
y += 26
for item, color in below:
    draw.text((rx + 12, y), f"·  {item}", font=font(16), fill=color)
    y += 24

# 13D/A 요약 박스
y += 8
draw.rounded_rectangle([rx, y, W - 60, y + 62], radius=8, fill=(30, 20, 10))
draw.text((rx + 16, y + 8),  "Schedule 13D/A  —  지분 1%p 변동마다 2영업일 내 수정 공시", font=font(16), fill=AMBER)
draw.text((rx + 16, y + 32), "올해만 3회  :  17.7% → 16.2% → 14.7%  →  오퍼링 후 13D/A 예정", font=bold(17), fill=ORANGE)

footer(draw, "2026.06.05", "SEC EDGAR  |  Form 4 · Schedule 13D/A · 8-K 기준")

out = os.path.join(OUT_DIR, "2026-06-05_LPTH_노스런블록딜.png")
img.save(out)
print("Saved:", out)
