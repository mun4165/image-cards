from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-07"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
RED       = (239, 68, 68)
AMBER     = (245, 158, 11)
GREEN     = (52, 211, 153)
CYAN      = (6, 182, 212)
BLUE      = (59, 130, 246)
PURPLE    = (167, 139, 250)

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")

for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

draw.rectangle([0, 0, W, 4], fill=BLUE)
draw.rectangle([0, 0, 4, H], fill=BLUE)

# ── 헤더 ──
draw.text((32, 14), "구글이 주식을 팔아 $847억을 모았다", font=bold(38), fill=WHITE)
draw.text((32, 62), "2026.06.01  |  Alphabet 역대 최대 자본 조달  |  버크셔 $100억 사모 참여", font=font(18), fill=BLUE)
draw.line([(32, 96), (W - 32, 96)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 조달 구조 ──
draw.text((32, 110), "조달 구조", font=bold(19), fill=GRAY)

# 왼쪽: 조달 구조 3개 + 합계 — H-52까지 균등 배분
CONTENT_TOP = 138
CONTENT_BOT = H - 52
total_h = CONTENT_BOT - CONTENT_TOP
item_h = total_h // 4  # 3개 + 합계

items = [
    (BLUE,   "공개 주식 공모",           "$300억",  "보통주 + 전환우선주 각 $150억"),
    (CYAN,   "장외 매도 프로그램",        "$400억",  "Q3 2026 시작 — 상시 매도 구조"),
    (PURPLE, "버크셔 해서웨이 사모 배정", "$100억",  "주당 $348~$352  워런 버핏 직접 참여"),
]
y = CONTENT_TOP
for color, label, amount, sub in items:
    draw.rounded_rectangle([32, y, 400, y + item_h - 6], radius=8, fill=(18, 22, 32))
    draw.rectangle([32, y, 38, y + item_h - 6], fill=color)
    draw.text((52, y + 10), label, font=font(15), fill=GRAY)
    draw.text((52, y + 34), amount, font=bold(34), fill=color)
    draw.text((52, y + 80), sub, font=font(14), fill=GRAY)
    y += item_h

draw.rounded_rectangle([32, y, 400, CONTENT_BOT], radius=8, fill=(15, 25, 45))
draw.rounded_rectangle([32, y, 400, CONTENT_BOT], radius=8, outline=BLUE, width=2)
draw.text((52, y + 10), "총 조달 규모", font=font(15), fill=GRAY)
draw.text((52, y + 36), "$847억 5,000만", font=bold(30), fill=WHITE)
draw.text((52, y + 76), "구글 역대 최대 단일 자본 조달", font=font(14), fill=BLUE)

# ── 세로 구분선 ──
draw.line([(430, 96), (430, H - 44)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 돈의 흐름 — 균등 배분 ──
draw.text((454, 110), "이 돈의 끝단", font=bold(19), fill=GRAY)
draw.line([(454, 138), (W - 32, 138)], fill=DARK_GRAY, width=1)

flow = [
    (BLUE,   "$847억 Capex 투입",          "AI 컴퓨팅 인프라 확장 — 구글 공식 발표"),
    (CYAN,   "서버 · 데이터센터 · 네트워크","2025년 capex $914억, 전년 대비 +74%"),
    (GREEN,  "GPU / TPU (AI 가속기)",       "구글 자체 TPU + 엔비디아 GPU 병행"),
    (AMBER,  "HBM 수요 폭발",               "AI 가속기 1개당 HBM 탑재 필수"),
    (RED,    "DRAM 공급 감소 → 가격 상승",  "HBM 증산 시 일반 DRAM 팹 capacity 전환"),
]
fy = CONTENT_TOP
fbox_h = (CONTENT_BOT - CONTENT_TOP) // 5
for color, title, sub in flow:
    draw.rounded_rectangle([454, fy, W - 32, fy + fbox_h - 6], radius=6, fill=(20, 22, 30))
    draw.rectangle([454, fy, 460, fy + fbox_h - 6], fill=color)
    draw.text((474, fy + 10), title, font=bold(18), fill=color)
    draw.text((474, fy + 40), sub, font=font(14), fill=GRAY)
    fy += fbox_h

# ── 하단 바 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.07", font=font(15), fill=GRAY)
draw.text((W - 340, H - 30), "Alphabet  |  AI 인프라 자본 조달", font=bold(15), fill=BLUE)

out = os.path.join(OUT_DIR, "2026-06-07_Alphabet_equity_raise.png")
img.save(out)
print("Saved:", out)
