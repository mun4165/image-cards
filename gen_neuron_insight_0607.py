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


img, draw = make_base(PURPLE)

# ── 헤더 ──
draw.text((60, 16), "뉴런인사이트를 읽으며", font=bold(24), fill=PURPLE)
draw.text((60, 52), "병목을 찾는 것과 발견되는 것 사이", font=bold(36), fill=WHITE)
draw.line([(60, 104), (W - 60, 104)], fill=DARK_GRAY, width=1)

lx = 60

# ── 왼쪽: 책 구절 ──
draw.text((lx, 118), "책에서 멈춘 구절들", font=bold(20), fill=GRAY)

quotes = [
    ("p.21", "좋은 자산을 골랐다면, 그 판단을\n무관심으로 지켜보는 것은 효과가 크다"),
    ("p.29", "성공에 행운이 컸다면\n실패에는 불운이 컸다고 믿어야 한다"),
    ("p.39", "본질에만 집중해도 충분하다"),
    ("p.166","마지막으로 닿는 곳은\n결국 자신의 판단이다"),
]

y = 150
for page, text in quotes:
    draw.rounded_rectangle([lx, y, lx + 530, y + 72], radius=6, fill=(25, 20, 40))
    draw.text((lx + 14, y + 8),  page, font=bold(16), fill=PURPLE)
    for i, line in enumerate(text.split('\n')):
        draw.text((lx + 14, y + 30 + i * 22), line, font=font(17), fill=WHITE)
    y += 84

# ── 세로 구분선 ──
draw.line([(632, 104), (632, H - 60)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 나만의 인사이트 ──
rx = 660
draw.text((rx, 118), "읽다가 직접 마주한 것", font=bold(20), fill=GRAY)

# 핵심 긴장 박스
draw.rounded_rectangle([rx, 150, rx + 530, 270], radius=8, fill=(30, 20, 50))
draw.text((rx + 14, 160), "병목을 찾는 것", font=bold(22), fill=PURPLE)
draw.text((rx + 14, 192), "≠", font=bold(28), fill=AMBER)
draw.text((rx + 14, 228), "그 병목이 시장에 발견되는 것", font=bold(22), fill=WHITE)

# 맹점 설명
draw.rounded_rectangle([rx, 282, rx + 530, 390], radius=8, fill=(20, 18, 10))
draw.text((rx + 14, 292), "틈새 투자의 구조적 약점", font=bold(18), fill=AMBER)
draw.text((rx + 14, 322), "남들이 모른다 = 기회", font=font(17), fill=GRAY)
draw.text((rx + 14, 346), "남들이 모른 채 끝난다 = 투자 미완성", font=bold(17), fill=ORANGE)
draw.text((rx + 14, 370), "발견의 트리거가 테제의 일부여야 한다", font=font(16), fill=GRAY)

# 결론 박스
draw.line([(rx, 404), (rx + 530, 404)], fill=DARK_GRAY, width=1)
draw.text((rx, 416), "이 책이 말하는 것", font=bold(20), fill=GRAY)

draw.rounded_rectangle([rx, 448, rx + 530, 556], radius=8, fill=(18, 28, 18))
draw.text((rx + 14, 458), "투자 기법이 아니다", font=bold(20), fill=GREEN)
draw.text((rx + 14, 490), "투자하는 사람에 대한 책이다", font=font(18), fill=GRAY)
draw.text((rx + 14, 518), "나 자신을 알게 될 때 부는 따라온다  — p.31", font=font(16), fill=GREEN)

# 마지막 한 줄
draw.rounded_rectangle([rx, 568, rx + 530, 630], radius=8, fill=(25, 20, 40))
draw.text((rx + 14, 578), '"확신을 팔지 않고 확률을 말할 것"', font=bold(19), fill=PURPLE)
draw.text((rx + 14, 608), "— 뉴런인사이트 p.159", font=font(16), fill=GRAY)

footer(draw, "2026.06.07", "뉴런인사이트 독서 기록")

out = os.path.join(OUT_DIR, "2026-06-07_뉴런인사이트_병목과발견.png")
img.save(out)
print("Saved:", out)
