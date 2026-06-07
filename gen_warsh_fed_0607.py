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

# 그리드
for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

# 테두리
draw.rectangle([0, 0, W, 4], fill=AMBER)
draw.rectangle([0, 0, 4, H], fill=AMBER)

# ── 헤더 ──
draw.text((32, 14), "고용이 강해도 나는 금리 인상을 생각하지 않는다", font=bold(36), fill=WHITE)
draw.text((32, 62), "2026.06.07  |  연준 독해  |  케빈 워시 · FOMC · 큰 그림", font=font(18), fill=AMBER)
draw.line([(32, 96), (W - 32, 96)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 프레임 독해 ──
CONTENT_TOP = 110
CONTENT_BOT = H - 52
LEFT_W = 580

draw.text((32, CONTENT_TOP), "프레임 독해", font=bold(18), fill=GRAY)

left_items = [
    (AMBER, "반복되는 플레이북",
             "강한 고용 → 공포 → 안도 → 유동성",
             "2022년부터 같은 흐름이 반복됐다"),
    (CYAN,  "케빈 워시 인선",
             "\"트럼프에게 금리 인하 약속한 적 없다\"",
             "독립성 연기 → 나중에 인하할 명분 확보"),
    (PURPLE,"데이터 디펜던트의 함정",
             "같은 데이터, 다른 해석",
             "누가 왜 그 데이터를 꺼내는지가 핵심"),
]

item_h = (CONTENT_BOT - CONTENT_TOP - 32) // 3
y = CONTENT_TOP + 32
for color, title, line1, line2 in left_items:
    draw.rounded_rectangle([32, y, LEFT_W, y + item_h - 8], radius=8, fill=(20, 24, 34))
    draw.rectangle([32, y, 38, y + item_h - 8], fill=color)
    draw.text((52, y + 10), title, font=bold(18), fill=color)
    draw.text((52, y + 40), line1, font=font(16), fill=WHITE)
    draw.text((52, y + 66), line2, font=font(14), fill=GRAY)
    y += item_h

# ── 세로 구분선 ──
draw.line([(610, 96), (610, CONTENT_BOT)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 구조적 이유 + 약점 ──
RIGHT_X = 630

draw.text((RIGHT_X, CONTENT_TOP), "구조적 이유", font=bold(18), fill=GRAY)

total_right = CONTENT_BOT - CONTENT_TOP - 32
ritem_h = int(total_right * 0.28)
warn_h   = total_right - ritem_h * 2 - 16

right_top = [
    (GREEN, "중간선거",
            "주가 하락 안고 선거 들어가는 건 불가"),
    (BLUE,  "미중 패권",
            "유동성 끊기면 글로벌 자금 이탈"),
]

ry = CONTENT_TOP + 32
for color, title, sub in right_top:
    draw.rounded_rectangle([RIGHT_X, ry, W - 32, ry + ritem_h - 8], radius=8, fill=(20, 24, 34))
    draw.rectangle([RIGHT_X, ry, RIGHT_X + 6, ry + ritem_h - 8], fill=color)
    draw.text((RIGHT_X + 20, ry + 12), title, font=bold(20), fill=color)
    draw.text((RIGHT_X + 20, ry + 46), sub, font=font(15), fill=GRAY)
    ry += ritem_h + 8

# 약점 박스
warn_y = ry
warn_bot = warn_y + warn_h - 8
draw.rounded_rectangle([RIGHT_X, warn_y, W - 32, warn_bot], radius=8, fill=(28, 16, 16))
draw.rounded_rectangle([RIGHT_X, warn_y, W - 32, warn_bot], radius=8, outline=RED, width=1)
draw.text((RIGHT_X + 20, warn_y + 12), "⚠  이 독해의 약점", font=bold(16), fill=RED)
draw.text((RIGHT_X + 20, warn_y + 44), "모든 발언이 '연기'로 읽히면 반증 불가 논리가 된다", font=font(14), fill=GRAY)
draw.text((RIGHT_X + 20, warn_y + 70), "워시가 시장 기대를 실제로 배신하면 내러티브를 버린다", font=font(14), fill=GRAY)

# ── 하단 바 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.07", font=font(15), fill=GRAY)
draw.text((W - 440, H - 30), "연준 · 케빈 워시 · 금리 인하 큰 그림", font=bold(15), fill=AMBER)

out = os.path.join(OUT_DIR, "2026-06-07_warsh_fed_macro.png")
img.save(out)
print("Saved:", out)
