from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-14"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1080, 1080
BG        = (13, 18, 28)
WHITE     = (255, 255, 255)
GRAY      = (120, 140, 165)
DARK_GRAY = (40, 55, 75)
BLUE      = (79, 163, 255)
BLUE_DIM  = (30, 70, 130)
BLUE_BG   = (18, 35, 65)
GOLD      = (220, 170, 60)

def font(size):
    return ImageFont.truetype(FONT_PATH, size, index=0)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")

# 배경 그리드
for x in range(0, W, 72):
    draw.line([(x, 0), (x, H)], fill=(255,255,255,8), width=1)
for y in range(0, H, 72):
    draw.line([(0, y), (W, y)], fill=(255,255,255,8), width=1)

# 상단 강조선
draw.rectangle([0, 0, W, 5], fill=BLUE)

# ── 태그 ──
TAG_X, TAG_Y = 60, 48
draw.rounded_rectangle([TAG_X, TAG_Y, TAG_X+180, TAG_Y+34], radius=17, fill=BLUE_BG)
draw.rounded_rectangle([TAG_X, TAG_Y, TAG_X+180, TAG_Y+34], radius=17, outline=BLUE_DIM, width=1)
draw.text((TAG_X+18, TAG_Y+7), "2026.06.16–17", font=font(15), fill=BLUE)

# ── 메인 타이틀 ──
draw.text((60, 104), "BOJ · FOMC", font=bold(54), fill=BLUE)
draw.text((60, 168), "같은 주에 열린다", font=bold(38), fill=WHITE)
draw.text((60, 222), "일본 금리인상 가능성 + 미국 점도표", font=font(22), fill=GRAY)

# 구분선
draw.line([(60, 278), (W-60, 278)], fill=DARK_GRAY, width=1)

# ── BOJ 블록 ──
BX = 60
BY = 308
COL_W = W // 2 - 80  # 각 컬럼 너비

draw.text((BX, BY), "BOJ  ·  6월 16일", font=bold(22), fill=(140, 180, 230))
draw.text((BX, BY+38), "0.75%  →  1.0%", font=bold(36), fill=WHITE)
draw.text((BX, BY+84), "+0.25%p 인상 논의 중", font=font(19), fill=GRAY)

# 서베이 박스
draw.rounded_rectangle([BX, BY+118, BX+COL_W, BY+196], radius=10, fill=(20, 30, 50))
draw.text((BX+18, BY+128), "블룸버그  51명 중 49명  인상 예상", font=font(18), fill=GRAY)
draw.text((BX+18, BY+158), "로이터     60명 전원    동결 예상", font=font(18), fill=GRAY)

draw.text((BX, BY+216), "→ 인상 시 엔캐리 청산 압력 발생", font=font(18), fill=(160, 190, 220))

# 세로 구분선
SEP_X = W // 2
draw.line([(SEP_X, BY), (SEP_X, BY+250)], fill=DARK_GRAY, width=1)

# ── FOMC 블록 ──
FX = W // 2 + 30
FY = 308

draw.text((FX, FY), "FOMC  ·  6월 17일", font=bold(22), fill=(140, 180, 230))
draw.text((FX, FY+38), "3.50–3.75%", font=bold(36), fill=WHITE)
draw.text((FX, FY+84), "동결 유력", font=font(19), fill=GRAY)

draw.rounded_rectangle([FX, FY+118, FX+COL_W, FY+196], radius=10, fill=(20, 30, 50))
draw.text((FX+18, FY+128), "5월 CPI  4.2%  (3년여 만의 최고)", font=font(18), fill=GRAY)
draw.text((FX+18, FY+158), "5월 실업률  4.3%  /  고용 +17.2만", font=font(18), fill=GRAY)

draw.text((FX, FY+216), "→ 점도표(Dot Plot) 숫자가 방향 결정", font=font(18), fill=(160, 190, 220))

# ── 구분선 ──
draw.line([(60, 588), (W-60, 588)], fill=DARK_GRAY, width=1)

# ── 관전 포인트 ──
draw.text((60, 610), "관전 포인트", font=bold(24), fill=BLUE)

points = [
    ("BOJ", "인상 단행 여부 자체가 서프라이즈. 두 기관 서베이가 정반대라 어느 쪽이든 충격이 온다."),
    ("FOMC", "점도표 숫자 먼저, 파월 기자회견 톤 그다음. 연내 인하 횟수 변화가 핵심이다."),
    ("공통", "두 이벤트 이틀 연속. 변동성이 크게 올 수 있는 구간이다."),
]

py = 658
for label, text in points:
    draw.ellipse([60, py+5, 72, py+17], fill=BLUE)
    draw.text((88, py), label, font=bold(20), fill=(180, 210, 255))
    draw.text((88, py+28), text, font=font(18), fill=GRAY)
    py += 90

# ── 하단 ──
draw.line([(60, H-60), (W-60, H-60)], fill=DARK_GRAY, width=1)
draw.text((60, H-44), "개인 공부 기록  ·  투자 권유 아님", font=font(17), fill=(50, 70, 95))
draw.text((W-240, H-44), "2026.06.14", font=font(17), fill=(50, 70, 95))

out = os.path.join(OUT_DIR, "2026-06-14_BOJ_FOMC.png")
img.save(out, "PNG")
print("Saved:", out)
