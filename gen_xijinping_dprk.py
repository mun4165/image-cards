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
AMBER     = (245, 158, 11)
GREEN     = (52, 211, 153)
CYAN      = (6, 182, 212)
PURPLE    = (167, 139, 250)
GOLD      = (212, 175, 55)

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

# 상단/좌측 테두리
draw.rectangle([0, 0, W, 4], fill=RED)
draw.rectangle([0, 0, 4, H], fill=RED)

# ── 헤더 ──
draw.text((32, 14), "시진핑, 7년 만에 방북", font=bold(42), fill=WHITE)
draw.text((32, 66), "2026.06.08 ~ 09  |  1박 2일 국빈 방문  |  2019년 이후 첫 방북", font=font(19), fill=RED)
draw.line([(32, 100), (W - 32, 100)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 배경 ──
draw.text((32, 114), "왜 지금인가", font=bold(20), fill=GRAY)

reasons = [
    (GOLD,   "65주년",    "북중우호협력상호원조조약 체결 65주년"),
    (CYAN,   "영향력 복원", "북러 밀착으로 약해진 대북 영향력 만회"),
    (PURPLE, "간접 중재",  "트럼프↔김정은 메시지 전달 역할 가능성"),
]
y = 148
for color, tag, desc in reasons:
    draw.rounded_rectangle([32, y, 44, y + 52], radius=2, fill=color)
    draw.text((56, y + 4), tag, font=bold(18), fill=color)
    draw.text((56, y + 28), desc, font=font(15), fill=GRAY)
    y += 68

# 핵심 메시지 박스
draw.rounded_rectangle([32, y + 8, 390, y + 80], radius=8, fill=(25, 20, 10))
draw.text((50, y + 18), "중국의 선언:", font=font(15), fill=GRAY)
draw.text((50, y + 40), "\"북한은 여전히 내 파트너\"", font=bold(20), fill=AMBER)

# ── 세로 구분선 ──
draw.line([(420, 100), (420, H - 44)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 4대 의제 ──
draw.text((444, 114), "4대 의제", font=bold(20), fill=GRAY)
draw.line([(444, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

agendas = [
    (RED,    "① 한반도 정세",      "한미일 vs 북중러 구도 속 전략 조율"),
    (GREEN,  "② 북중 경제협력",    "철도·물류, 국경 개발, 광물, 관광 재개"),
    (CYAN,   "③ 북중러 동해 협력", "3국 물류·군사 협력 구체화"),
    (AMBER,  "④ 북미 대화",        "시진핑 간접 중재 → 북핵 협상 재개 촉각"),
]

y = 156
for color, title, detail in agendas:
    draw.rounded_rectangle([444, y, W - 32, y + 88], radius=8, fill=(20, 22, 30))
    draw.rectangle([444, y, 450, y + 88], fill=color)
    draw.text((466, y + 12), title, font=bold(22), fill=color)
    draw.text((466, y + 46), detail, font=font(17), fill=WHITE)
    y += 102

# ── 하단 바 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.05", font=font(15), fill=GRAY)
draw.text((W - 300, H - 30), "시진핑 방북  |  한반도 지정학", font=bold(15), fill=RED)

out = os.path.join(OUT_DIR, "2026-06-05_시진핑방북.png")
img.save(out)
print("Saved:", out)
