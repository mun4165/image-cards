from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-17"
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

ACCENT = CYAN  # 냉각(cool) 적외선 테마

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

# 상단·좌측 강조선
draw.rectangle([0, 0, W, 4], fill=ACCENT)
draw.rectangle([0, 0, 4, H], fill=ACCENT)

# ── 헤더 ──
draw.text((32, 18), "게르마늄-프리 냉각 MWIR", font=bold(40), fill=ACCENT)
draw.text((32, 72), "중국이 쥔 소재 하나가 미국 국방 광학의 급소가 됐다", font=bold(24), fill=WHITE)
draw.text((32, 108), "MWIR(Mid-Wave InfraRed) = 중파장 적외선 3~5㎛ · 멀리 있는 표적을 정밀하게 식별", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("中 정제 게르마늄 점유",   "약 60%",    "2023~ 中 수출통제 → 가격 급등",          RED),
    ("MWIR 파장대",            "3~5㎛",     "단파장일수록 장거리 해상도 유리",          CYAN),
    ("냉각식 작동 온도",        "-196°C",    "≈77K 스털링 쿨러 / 광자를 직접 셈",        BLUE),
    ("게르마늄 굴절률",         "≈4.0",      "but dn/dT 큼 → 온도 오르면 초점흐림",      AMBER),
]
y = 158
for label, value, sub, color in metrics:
    draw.text((32, y), label, font=font(17), fill=GRAY)
    draw.text((32, y + 22), value, font=bold(28), fill=color)
    draw.text((32, y + 56), sub, font=font(16), fill=GRAY)
    draw.line([(32, y + 80), (590, y + 80)], fill=DARK_GRAY, width=1)
    y += 92

# 세로 구분선
draw.line([(620, 140), (620, H - 46)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 핵심 논지 ──
draw.text((644, 158), "왜 방산이 여기 몰리나", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (CYAN,  "장거리엔 '냉각 MWIR'이 정답",
     "비냉각=둔감, 냉각=민감도 압도 / 수km 식별 가능"),
    (RED,   "게르마늄이 급소",
     "공급망 中 의존 + 열에 초점 흔들림(dn/dT)"),
    (GREEN, "해법 = 게르마늄-프리",
     "칼코게나이드·블랙다이아몬드 / 드롭인 교체"),
    (AMBER, "공짜 점심은 아님",
     "굴절률 낮아 렌즈 커짐 / 엔트리부터 순차 대체"),
]
y = 204
for color, title, desc in points:
    draw.rectangle([640, y + 3, 644, y + 30], fill=color)
    draw.text((656, y), title, font=bold(20), fill=WHITE)
    draw.text((656, y + 28), desc, font=font(17), fill=GRAY)
    y += 62

# 요약 박스
draw.line([(644, y + 4), (W - 32, y + 4)], fill=DARK_GRAY, width=1)
y += 18
draw.rounded_rectangle([644, y, W - 32, y + 62], radius=8, fill=(6, 30, 36))
draw.text((658, y + 12), "냉각 MWIR = 멀리 보는 '성능'", font=bold(18), fill=CYAN)
draw.text((658, y + 36), "게르마늄-프리 = 적성국 소재 없이 만드는 '조달 안정'", font=bold(18), fill=CYAN)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.17  |  적외선 광학 · 게르마늄-프리 냉각 MWIR · LPTH BlackDiamond", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-17_LPTH_게르마늄프리냉각MWIR.png")
img.save(out)
print("Saved:", out)
