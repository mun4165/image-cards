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


img, draw = make_base(RED)

# ── 헤더 ──
draw.text((60, 18), "MU  -7.74%  —  브로드컴이 쏜 총에 맞은 마이크론", font=bold(36), fill=WHITE)
draw.text((60, 64), "마이크론 고유 악재 없음  ·  ASIC 가이던스와 HBM 수요는 다른 시장", font=font(20), fill=GRAY)
draw.line([(60, 100), (W - 60, 100)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 브로드컴 쇼크 원인 ──
lx = 60
draw.text((lx, 114), "브로드컴(AVGO) 가이던스 쇼크", font=bold(21), fill=GRAY)

rows = [
    ("Q3 AI 칩 가이던스",  "$160억",   RED),
    ("시장 기대치",        "$172억",   GRAY),
    ("차이",              "-$12억",   RED),
    ("AVGO 당일 주가",    "-14%",     RED),
    ("MU 동반 하락",       "-7.74%",  ORANGE),
]
y = 146
for label, val, color in rows:
    draw.text((lx, y),        label, font=font(17), fill=GRAY)
    draw.text((lx + 290, y),  val,   font=bold(22), fill=color)
    draw.line([(lx, y + 34), (lx + 530, y + 34)], fill=DARK_GRAY, width=1)
    y += 44

# 핵심 메시지 박스
draw.rounded_rectangle([lx, y + 8, lx + 530, y + 60], radius=8, fill=(40, 15, 15))
draw.text((lx + 16, y + 18), "MU는 반도체 섹터 ETF 매도에 휩쓸린 것", font=bold(19), fill=RED)
draw.text((lx + 16, y + 42), "마이크론 고유의 악재가 아니다", font=font(17), fill=ORANGE)

# ── 왼쪽 아래: 브로드컴 Q3 미달 맥락 ──
y2 = y + 80
draw.line([(lx, y2), (lx + 530, y2)], fill=DARK_GRAY, width=1)
draw.text((lx, y2 + 12), "왜 시장이 과잉반응했나", font=bold(21), fill=GRAY)
context = [
    ("연간 AI 가이던스",   "미상향 → 'AI 투자 피크아웃?' 공포",  AMBER),
    ("YTD 반도체 급등",    "차익실현 빌미로 작동",               ORANGE),
    ("섹터 ETF 자동 매도", "MU·ARM·SanDisk 동반 하락",         GRAY),
]
y2 += 46
for label, val, color in context:
    draw.text((lx, y2),        label, font=font(16), fill=GRAY)
    draw.text((lx, y2 + 20),   val,   font=bold(17), fill=color)
    y2 += 52

# ── 세로 구분선 ──
draw.line([(632, 100), (632, H - 60)], fill=DARK_GRAY, width=1)

# ── 오른쪽 위: ASIC vs HBM 구분 ──
rx = 660
draw.text((rx, 114), "ASIC ≠ HBM  —  다른 시장이다", font=bold(21), fill=GRAY)

cols = [
    ("브로드컴 ASIC",    "구글·메타 자체 설계 AI 칩\n빅테크 발주 물량에 의존",    ORANGE),
    ("마이크론 HBM",     "GPU 1장당 필수 탑재 메모리\nAI 추론 트래픽 증가 = 수요↑", CYAN),
]
y = 148
for title, desc, color in cols:
    draw.rectangle([rx, y, rx + 4, y + 68], fill=color)
    draw.text((rx + 14, y),      title, font=bold(22), fill=color)
    for i, line in enumerate(desc.split('\n')):
        draw.text((rx + 14, y + 30 + i * 22), line, font=font(17), fill=GRAY)
    y += 96

draw.line([(rx, y), (W - 60, y)], fill=DARK_GRAY, width=1)

# ── 오른쪽 아래: 마이크론 현황 + 6/24 ──
y += 12
draw.text((rx, y), "마이크론 펀더멘털 — 변한 것 없다", font=bold(21), fill=GRAY)
y += 32

status = [
    ("HBM 2026년 전량 완판",   GREEN),
    ("시총 $1조 달성",         GREEN),
    ("애널 46명 전원 매수",    GREEN),
]
for label, color in status:
    draw.text((rx, y), f"✓  {label}", font=font(19), fill=color)
    y += 30

y += 8
draw.rounded_rectangle([rx, y, W - 60, y + 70], radius=8, fill=(10, 30, 40))
draw.text((rx + 16, y + 8),  "▶  6월 24일 Q3 실적 발표", font=bold(22), fill=CYAN)
draw.text((rx + 16, y + 38), "HBM 성장률 + DRAM ASP — 진짜 판단은 그날", font=font(18), fill=GRAY)

footer(draw, "2026.06.05", "Broadcom Q2 FY2026 Earnings  |  MU 종가 기준")

out = os.path.join(OUT_DIR, "2026-06-05_MU_브로드컴쇼크.png")
img.save(out)
print("Saved:", out)
