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


img, draw = make_base(AMBER)

# ── 헤더 ──
draw.text((60, 18), "AI 수요가 닌텐도를 건드렸다", font=bold(38), fill=WHITE)
draw.text((60, 66), "메모리 완판 · 가격 인상 · CXMT 추격 — 2026년 반도체 시장 변화 정리", font=font(19), fill=GRAY)
draw.line([(60, 102), (W - 60, 102)], fill=DARK_GRAY, width=1)

# ── 왼쪽 패널 ──
lx = 60

# 섹션 1: 수급 구조
draw.text((lx, 116), "수급 구조", font=bold(18), fill=AMBER)
rows = [
    ("SK하이닉스 2026년",  "DRAM · NAND · HBM  전량 완판",  WHITE),
    ("서버 DRAM 가격",     "+60~70% QoQ  (빅테크 우선 공급)", RED),
    ("HBM 판가",           "$60~100  vs  일반 DDR5  $5~10",   AMBER),
]
y = 146
for label, val, color in rows:
    draw.text((lx, y),       label, font=font(16), fill=GRAY)
    draw.text((lx, y + 20),  val,   font=bold(18), fill=color)
    draw.line([(lx, y + 46), (lx + 560, y + 46)], fill=DARK_GRAY, width=1)
    y += 56

# 섹션 2: 닌텐도
y += 4
draw.text((lx, y), "소비자 파급", font=bold(18), fill=AMBER)
y += 28
draw.rectangle([lx, y, lx + 4, y + 72], fill=ORANGE)
draw.text((lx + 14, y),      "닌텐도 Switch 2 가격 인상",    font=bold(20), fill=WHITE)
draw.text((lx + 14, y + 28), "미국  $449 → $499  (+$50, 9월~)",  font=font(17), fill=ORANGE)
draw.text((lx + 14, y + 50), "일본  ¥10,000 인상  ·  메모리·관세 등 복합 요인", font=font(16), fill=GRAY)
y += 84

# 섹션 3: CXMT 진입
draw.line([(lx, y), (lx + 560, y)], fill=DARK_GRAY, width=1)
y += 10
draw.text((lx, y), "공백 채우는 CXMT", font=bold(18), fill=AMBER)
y += 28
cxmt = [
    (CYAN,  "Corsair DDR5에 CXMT DRAM 탑재 제품 시장 등장"),
    (CYAN,  "기가바이트 등 주요 메인보드 QVL 등록"),
    (GRAY,  "한국 출신 엔지니어 200명+ 재직 (Digitimes)"),
]
for color, text in cxmt:
    draw.text((lx, y), f"·  {text}", font=font(17), fill=color)
    y += 26

# ── 세로 구분선 ──
draw.line([(648, 102), (648, H - 60)], fill=DARK_GRAY, width=1)

# ── 오른쪽 패널 ──
rx = 676

# 기술 격차
draw.text((rx, 116), "CXMT 기술 격차", font=bold(18), fill=AMBER)

gap_items = [
    ("한국 → 중국 HBM 격차",  "3년",     "서울경제 2026.06",   GREEN),
    ("일부 분석 전망",         "2년 이하", "Digitimes",         AMBER),
    ("CXMT 공법",             "MR-MUF",  "SK하이닉스와 동일",  CYAN),
]
y2 = 146
for label, val, note, color in gap_items:
    draw.text((rx, y2),        label, font=font(15), fill=GRAY)
    draw.text((rx + 240, y2),  val,   font=bold(22), fill=color)
    draw.text((rx + 380, y2),  note,  font=font(15), fill=GRAY)
    draw.line([(rx, y2 + 36), (W - 60, y2 + 36)], fill=DARK_GRAY, width=1)
    y2 += 46

# 역설 박스
draw.rounded_rectangle([rx, y2 + 6, W - 60, y2 + 80], radius=8, fill=(30, 20, 5))
draw.text((rx + 16, y2 + 14), "역설  —  VRAM 줄었는데 메모리 기업 호재?", font=bold(18), fill=AMBER)
draw.text((rx + 16, y2 + 40), "엔비디아 RTX 5060  16GB → 8GB 출시", font=font(16), fill=GRAY)
draw.text((rx + 16, y2 + 60), "GDDR7이 소비자 GPU 대신 HBM으로 재배분", font=font(16), fill=ORANGE)
y2 += 92

# 리스크
draw.line([(rx, y2 + 8), (W - 60, y2 + 8)], fill=DARK_GRAY, width=1)
y2 += 18
draw.text((rx, y2), "리스크", font=bold(18), fill=AMBER)
y2 += 28

risks = [
    (RED,  "빅테크 5사 AI 자본지출  ~$7,000억 (2026)"),
    (RED,  "Google  $200억 채권 발행  (100년물 포함)"),
    (GRAY, "UBS: 하이퍼스케일러 차입  $2,300~2,400억 전망"),
]
for color, text in risks:
    draw.text((rx, y2), f"▲  {text}", font=font(17), fill=color)
    y2 += 28

footer(draw, "2026.06.05", "TrendForce · Digitimes · Nintendo IR · CNBC")

out = os.path.join(OUT_DIR, "2026-06-05_메모리대란.png")
img.save(out)
print("Saved:", out)
