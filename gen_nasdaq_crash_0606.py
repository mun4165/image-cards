from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-06"
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
draw.text((60, 16), "나스닥  -4.18%  —  관세 쇼크 이후 14개월 만의 최대 낙폭", font=bold(32), fill=WHITE)
draw.text((60, 60), "두 트리거가 하루 차이로 겹쳤다  ·  2026.06.05(금)  ·  SOX 반도체 지수 -6%+", font=font(19), fill=GRAY)
draw.line([(60, 98), (W - 60, 98)], fill=DARK_GRAY, width=1)

lx = 60

# ── 왼쪽 상단: 트리거 ① ──
draw.text((lx, 112), "트리거 ①  Broadcom 가이던스 쇼크  (6/3 장 마감 후)", font=bold(20), fill=GRAY)

rows = [
    ("Q3 AI 칩 가이던스",      "$16B",   RED),
    ("시장 기대치",            "$17.2B", GRAY),
    ("미달 규모",              "▼$1.2B", RED),
    ("AVGO 당일 낙폭",        "-12%",   RED),
    ("SOX 반도체 지수",        "-6%+",   ORANGE),
]
y = 144
for label, val, color in rows:
    draw.text((lx, y),        label, font=font(17), fill=GRAY)
    draw.text((lx + 290, y),  val,   font=bold(22), fill=color)
    draw.line([(lx, y + 32), (lx + 530, y + 32)], fill=DARK_GRAY, width=1)
    y += 40

# 핵심 메시지 박스
box_y = y + 4
draw.rounded_rectangle([lx, box_y, lx + 530, box_y + 50], radius=8, fill=(40, 15, 15))
draw.text((lx + 14, box_y + 8),  "AI 성장 가속이라는 서사에 처음으로 균열", font=bold(18), fill=RED)
draw.text((lx + 14, box_y + 32), "실적 미스가 아닌 내러티브의 균열이 핵심", font=font(15), fill=ORANGE)

# ── 왼쪽 하단: 트리거 ② ──
y2 = box_y + 64
draw.line([(lx, y2), (lx + 530, y2)], fill=DARK_GRAY, width=1)
draw.text((lx, y2 + 10), "트리거 ②  5월 고용보고서  (6/5 장 시작 전)", font=bold(20), fill=GRAY)

rows2 = [
    ("5월 비농업 신규고용",      "172,000명",  RED),
    ("시장 예상치",              "85,000명",  GRAY),
    ("4월 CPI",                 "3.8%",      ORANGE),
    ("금리인상 확률 (FedWatch)", "57%+",      RED),
]
y2 += 42
for label, val, color in rows2:
    draw.text((lx, y2),        label, font=font(17), fill=GRAY)
    draw.text((lx + 310, y2),  val,   font=bold(22), fill=color)
    draw.line([(lx, y2 + 32), (lx + 530, y2 + 32)], fill=DARK_GRAY, width=1)
    y2 += 40

# ── 세로 구분선 ──
draw.line([(632, 98), (632, H - 60)], fill=DARK_GRAY, width=1)

# ── 오른쪽 상단: 두 전제 ──
rx = 660
draw.text((rx, 112), "시장이 흔들린 두 전제", font=bold(22), fill=GRAY)

draw.rounded_rectangle([rx, 144, rx + 252, 262], radius=8, fill=(38, 12, 12))
draw.text((rx + 14, 154),  "AI 인프라 투자", font=bold(20), fill=RED)
draw.text((rx + 14, 182),  "무한 성장 전제", font=font(16), fill=GRAY)
draw.text((rx + 14, 206),  "Broadcom 가이던스 미달", font=font(15), fill=ORANGE)
draw.text((rx + 14, 228),  "→  피크아웃 공포", font=bold(16), fill=RED)

draw.rounded_rectangle([rx + 268, 144, rx + 530, 262], radius=8, fill=(38, 12, 12))
draw.text((rx + 282, 154),  "연준 금리 인하", font=bold(20), fill=RED)
draw.text((rx + 282, 182),  "전망 전제", font=font(16), fill=GRAY)
draw.text((rx + 282, 206),  "고용+물가 동시 강세", font=font(15), fill=ORANGE)
draw.text((rx + 282, 228),  "→  인상 가능성 57%+", font=bold(16), fill=RED)

# 동시 붕괴 메시지
draw.rounded_rectangle([rx, 274, rx + 530, 334], radius=8, fill=(50, 22, 0))
draw.text((rx + 14, 282), "두 전제 동시 붕괴 = 성장 정체  +  금리 인상", font=bold(19), fill=AMBER)
draw.text((rx + 14, 310), "기술 성장주에 가장 불리한 환경", font=font(17), fill=ORANGE)

# ── 오른쪽 하단: 다음 변수 ──
draw.line([(rx, 348), (rx + 530, 348)], fill=DARK_GRAY, width=1)
draw.text((rx, 358), "다음 변수", font=bold(22), fill=GRAY)

next_items = [
    (CYAN,   "6/11 (수)",    "5월 CPI 발표  —  이번 급락의 분수령"),
    (PURPLE, "6/16~17",     "FOMC + 점도표  —  금리 경로 공식 확인"),
    (AMBER,  "6/24",        "Micron Q3 실적  —  HBM · DRAM 수요 확인"),
]
y3 = 392
for color, date, desc in next_items:
    draw.rectangle([rx, y3 + 2, rx + 4, y3 + 26], fill=color)
    draw.text((rx + 14, y3),       date, font=bold(21), fill=color)
    draw.text((rx + 14, y3 + 28),  desc, font=font(16), fill=GRAY)
    y3 += 60

# CPI 결론 박스
draw.rounded_rectangle([rx, y3 + 8, rx + 530, y3 + 78], radius=8, fill=(10, 30, 40))
draw.text((rx + 14, y3 + 16), "CPI 하회  →  반등 기회", font=bold(20), fill=CYAN)
draw.text((rx + 14, y3 + 46), "CPI 초과  →  FOMC 전까지 추가 하락 압력", font=font(17), fill=GRAY)

footer(draw, "2026.06.05", "CNBC · CME FedWatch · Broadcom Q2 FY2026 Earnings  |  개인 공부 기록")

out = os.path.join(OUT_DIR, "2026-06-06_나스닥급락_분석.png")
img.save(out)
print("Saved:", out)
