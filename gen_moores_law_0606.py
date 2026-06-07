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


img, draw = make_base(CYAN)

# ── 헤더 ──
draw.text((60, 16), "칩워를 읽다가", font=bold(28), fill=CYAN)
draw.text((60, 54), "반도체 진입장벽의 본질은 '자본'이 아니라 '시간'이다", font=bold(34), fill=WHITE)
draw.line([(60, 104), (W - 60, 104)], fill=DARK_GRAY, width=1)

lx = 60

# ── 왼쪽: 무어의 법칙 ──
draw.text((lx, 118), "무어의 법칙", font=bold(22), fill=GRAY)

draw.rounded_rectangle([lx, 150, lx + 530, 230], radius=8, fill=(10, 35, 45))
draw.text((lx + 20, 162), '"컴퓨터의 연산력은 매년 두 배가 된다"', font=bold(20), fill=CYAN)
draw.text((lx + 20, 196), '— 고든 무어, 1965', font=font(17), fill=GRAY)

draw.text((lx, 248), "이것이 의미하는 것", font=bold(20), fill=GRAY)

items = [
    (CYAN,   "매년 더 복잡한 소재"),
    (CYAN,   "매년 더 정밀한 장비"),
    (CYAN,   "매년 더 까다로운 공정"),
]
y = 280
for color, text in items:
    draw.rectangle([lx, y + 4, lx + 4, y + 26], fill=color)
    draw.text((lx + 16, y), text, font=font(20), fill=WHITE)
    y += 44

draw.text((lx, y + 8), "그 복잡함은 역사처럼 레이어로 쌓인다.", font=bold(20), fill=AMBER)

# 공정 레이어 시각화
ly = y + 50
layer_labels = ["수율 노하우", "공정 레시피", "장비 협업", "실패 데이터", "엔지니어 직관"]
layer_colors = [
    (6, 182, 212, 200),
    (6, 182, 212, 160),
    (6, 182, 212, 120),
    (6, 182, 212, 80),
    (6, 182, 212, 50),
]
bar_w = 530
for i, (label, color) in enumerate(zip(layer_labels, layer_colors)):
    bw = int(bar_w * (1 - i * 0.1))
    draw.rectangle([lx, ly, lx + bw, ly + 28], fill=color[:3])
    draw.text((lx + 10, ly + 6), label, font=font(16), fill=BG)
    ly += 32

# ── 세로 구분선 ──
draw.line([(632, 104), (632, H - 60)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 자본 vs 시간 ──
rx = 660
draw.text((rx, 118), "왜 후발주자가 못 따라오나", font=bold(22), fill=GRAY)

# 자본 박스
draw.rounded_rectangle([rx, 150, rx + 248, 252], radius=8, fill=(35, 25, 10))
draw.text((rx + 14, 160), "자본", font=bold(28), fill=AMBER)
draw.text((rx + 14, 198), "복제 가능하다", font=font(18), fill=GRAY)
draw.text((rx + 14, 224), "중국도 있고 사우디도 있다", font=font(15), fill=DARK_GRAY)

# 시간 박스
draw.rounded_rectangle([rx + 264, 150, rx + 530, 252], radius=8, fill=(10, 35, 45))
draw.text((rx + 278, 160), "시간", font=bold(28), fill=CYAN)
draw.text((rx + 278, 198), "복제 불가능하다", font=bold(18), fill=WHITE)
draw.text((rx + 278, 224), "30년의 실패가 곧 해자", font=font(15), fill=CYAN)

# 핵심 결론 박스
draw.rounded_rectangle([rx, 266, rx + 530, 346], radius=8, fill=(20, 40, 30))
draw.text((rx + 14, 276), "반도체는 '자본 집약적'이 아니다", font=bold(20), fill=GREEN)
draw.text((rx + 14, 310), "'시간 집약적'이다 — 이게 정확한 표현이다", font=font(18), fill=GRAY)

# 사례들
draw.line([(rx, 360), (rx + 530, 360)], fill=DARK_GRAY, width=1)
draw.text((rx, 370), "같은 이유로 설명되는 두 가지", font=bold(20), fill=GRAY)

cases = [
    (RED,   "중국 반도체 굴기 실패",
             "수천억 달러를 쏟아도 선단 공정에서 막힌다"),
    (PURPLE, "TSMC 대체 불가",
             "새 공장을 지어도 수십 년의 공정 레이어는 이식 안 된다"),
]
y2 = 406
for color, title, desc in cases:
    draw.rectangle([rx, y2 + 2, rx + 4, y2 + 28], fill=color)
    draw.text((rx + 14, y2), title, font=bold(20), fill=color)
    draw.text((rx + 14, y2 + 30), desc, font=font(16), fill=GRAY)
    y2 += 72

# 마무리 인용
draw.rounded_rectangle([rx, y2 + 8, rx + 530, y2 + 76], radius=8, fill=(20, 20, 35))
draw.text((rx + 14, y2 + 16), "무어의 법칙은 기술 예측이면서", font=font(18), fill=GRAY)
draw.text((rx + 14, y2 + 42), "동시에 진입장벽의 다른 이름이었다", font=bold(20), fill=PURPLE)

footer(draw, "2026.06.06", "칩워 (Chris Miller) — 개인 독서 기록")

out = os.path.join(OUT_DIR, "2026-06-06_무어의법칙_해자.png")
img.save(out)
print("Saved:", out)
