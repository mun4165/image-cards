from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-19"
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

ACCENT = AMBER  # 가격 압박·수요 자백 테마

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

draw.rectangle([0, 0, W, 4], fill=ACCENT)
draw.rectangle([0, 0, 4, H], fill=ACCENT)

# ── 헤더 ──
draw.text((32, 18), "애플조차 못 버틴다", font=bold(40), fill=ACCENT)
draw.text((32, 72), "팀 쿡 '가격 인상 불가피' — 메모리는 지금 슈퍼사이클이다", font=bold(23), fill=WHITE)
draw.text((32, 108), "세계 최대 부품 구매자의 자백 = '메모리가 부족하고 비싸다'", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("팀 쿡 발언(WSJ)",   "\"불가피\"",   "메모리·스토리지 비용 흡수 한계",       AMBER),
    ("부품 비용 상승",     "약 4배↑",     "AI 빌드아웃 경쟁의 결과",              RED),
    ("싹쓸이 주체",        "하이퍼스케일러", "구글·MS·메타·아마존 capex 급증",       BLUE),
    ("진짜 급소",          "DRAM",        "공급은 HBM으로 쏠림 + 온디바이스 AI",   CYAN),
]
y = 158
for label, value, sub, color in metrics:
    draw.text((32, y), label, font=font(17), fill=GRAY)
    draw.text((32, y + 22), value, font=bold(28), fill=color)
    draw.text((32, y + 56), sub, font=font(16), fill=GRAY)
    draw.line([(32, y + 80), (590, y + 80)], fill=DARK_GRAY, width=1)
    y += 92

draw.line([(620, 140), (620, H - 46)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 핵심 논지 ──
draw.text((644, 158), "통섭 — 마이크론 폭등과 양면", font=bold(23), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (AMBER, "사는 쪽이 못 버틴다",
     "= 파는 쪽이 가격 결정력을 쥔다"),
    (GREEN, "메모리 제조사엔 호재",
     "애플 가격 인상 = 수요측의 자백"),
    (CYAN,  "한 흐름의 양면",
     "팀 쿡 발언 ↔ 마이크론 사상 최고가"),
    (BLUE,  "테마 안에서도 갈린다",
     "광학은 멀티플 조정, 메모리는 가격 상승"),
]
y = 204
for color, title, desc in points:
    draw.rectangle([640, y + 3, 644, y + 30], fill=color)
    draw.text((656, y), title, font=bold(20), fill=WHITE)
    draw.text((656, y + 28), desc, font=font(17), fill=GRAY)
    y += 62

draw.line([(644, y + 4), (W - 32, y + 4)], fill=DARK_GRAY, width=1)
y += 18
draw.rounded_rectangle([644, y, W - 32, y + 62], radius=8, fill=(40, 30, 6))
draw.text((658, y + 12), "단순 가격 인상 예고가 아니다", font=bold(18), fill=AMBER)
draw.text((658, y + 36), "사이클의 위치를 알려주는 신호다", font=bold(18), fill=AMBER)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.19  |  AAPL · MU  ·  WSJ · MacRumors", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-19_애플_팀쿡_칩가격인상_핵심요약.png")
img.save(out)
print("Saved:", out)
