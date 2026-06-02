from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-02"
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

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)
def tw(draw, text, f):
    bbox = draw.textbbox((0, 0), text, font=f)
    return bbox[2] - bbox[0]
def centered(draw, text, y, f, color=WHITE):
    w = tw(draw, text, f)
    draw.text(((W - w) // 2, y), text, font=f, fill=color)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)
draw.rectangle([0, 0, W, 4], fill=TEAL)
draw.rectangle([0, 0, 4, H], fill=TEAL)

# 헤더
draw.text((60, 44), "키옥시아 (285A)", font=bold(48), fill=TEAL)
draw.text((60, 106), "2026.06.02 인베스터 데이", font=font(24), fill=GRAY)
draw.line([(60, 146), (W - 60, 146)], fill=DARK_GRAY, width=1)

# 왼쪽: 핵심 수치
metrics = [
    ("FY2026 매출",       "¥2,337.6B",  "+37% YoY",    TEAL),
    ("Q1 FY2027 영업이익", "¥1.298조",   "+29배 YoY",   GREEN),
    ("Q1 FY2027 순이익",  "¥869B",      "+48배 YoY",   AMBER),
    ("영업이익률",         "60%",        "그로스마진 66%", AMBER),
]
y = 166
for label, value, sub, color in metrics:
    draw.text((60, y), label, font=font(19), fill=GRAY)
    draw.text((60, y + 26), value, font=bold(34), fill=color)
    draw.text((60, y + 68), sub, font=font(19), fill=GRAY)
    draw.line([(60, y + 96), (560, y + 96)], fill=DARK_GRAY, width=1)
    y += 110

# 세로 구분선
draw.line([(640, 140), (640, H - 60)], fill=DARK_GRAY, width=1)

# 오른쪽: 핵심 발표
draw.text((672, 166), "핵심 발표", font=bold(28), fill=WHITE)
draw.line([(672, 206), (W - 60, 206)], fill=DARK_GRAY, width=1)

points = [
    (GREEN,  "NVIDIA AI 메모리 파트너십",
     "엔비디아 AI 서버 공급망 공식 편입"),
    (CYAN,   "미국 ADS 상장 공식화",
     "SEC F-6 파일링 완료 · NYSE 상장 일정 미확정"),
    (AMBER,  "NAND 시장 전망",
     "2026년 비트 성장 15~19% · 2027년 공급 부족"),
    (TEAL,   "BiCS10 양산 가속",
     "332레이어 · 밀도 59%↑ · 2026년 본격 출하"),
]
y = 218
for color, title, desc in points:
    draw.rectangle([668, y, 672, y + 64], fill=color)
    draw.text((688, y), title, font=bold(22), fill=WHITE)
    draw.text((688, y + 32), desc, font=font(19), fill=GRAY)
    y += 84

# 푸터
draw.line([(60, H - 52), (W - 60, H - 52)], fill=DARK_GRAY, width=1)
draw.text((60, H - 38), "2026.06.02  |  키옥시아 IR / TrendForce  |  개인 공부 기록, 투자 추천 아님", font=font(17), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-02_키옥시아_인베스터데이.png")
img.save(out)
print("Saved:", out)
