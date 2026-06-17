from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-18"
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

ACCENT = TEAL  # 노동시장 구조 분해 테마

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
draw.text((32, 18), "같은 실업률, 다른 물가", font=bold(40), fill=ACCENT)
draw.text((32, 72), "고용과 물가가 안 맞아 보일 때 — 연준 안희주 박사의 두 곡선 이야기", font=bold(24), fill=WHITE)
draw.text((32, 108), "노동시장을 움직이는 충격을 '이직'과 '실직'으로 쪼개면 물가 신호가 갈린다", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 개념 ──
metrics = [
    ("자발적 이직(quits) 주도",   "물가 압력 약",   "더 좋은 자리로 이동 → 임금·물가 자극 작음",  GREEN),
    ("비자발적 실직(job loss) 주도", "물가 압력 강", "잘려서 밀려남 → 인플레 압력 강하게 붙음",   RED),
    ("베버리지 곡선",            "빈일자리 vs 실업", "충격 종류 따라 모양이 흔들린다",            GRAY),
    ("필립스 곡선",              "실업 vs 물가",     "시기마다 연결 강도가 달라진다",              GRAY),
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
draw.text((644, 158), "공식이 빗나갈 때 봐야 할 것", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (TEAL,  "곡선이 깨진 게 아니다",
     "그 시점에 어떤 충격이 지배적이냐가 바뀐 것"),
    (AMBER, "같은 실업률, 다른 신호",
     "이직이 많으냐 실직이 많으냐가 물가를 가른다"),
    (BLUE,  "숫자 하나로 보지 마라",
     "고용도 물가도 '구성'으로 분해해서 본다"),
    (GREEN, "투자자에게도 같은 틀",
     "헤드라인 애매할수록 그 밑의 구조를 본다"),
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
draw.rounded_rectangle([644, y, W - 32, y + 62], radius=8, fill=(6, 36, 33))
draw.text((658, y + 12), "실업률이 같아도", font=bold(18), fill=TEAL)
draw.text((658, y + 36), "이유가 다르면 물가 결과가 다르다", font=bold(18), fill=TEAL)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.18  |  Hie Joo Ahn & J. Rudd, 'A Tale of Two Curves' (Fed FEDS 2024-50)", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-18_안희주_두곡선.png")
img.save(out)
print("Saved:", out)
