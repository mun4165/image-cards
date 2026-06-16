from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-14"
os.makedirs(OUT_DIR, exist_ok=True)

BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
CYAN      = (6, 182, 212)
AMBER     = (245, 158, 11)

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. 프로필 사진 (800×800)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PW = PH = 800
p_img = Image.new("RGB", (PW, PH), BG)
p_draw = ImageDraw.Draw(p_img, "RGBA")

# 그리드
for x in range(0, PW, 80):
    p_draw.line([(x, 0), (x, PH)], fill=GRID, width=1)
for y in range(0, PH, 80):
    p_draw.line([(0, y), (PW, y)], fill=GRID, width=1)

# CYAN 원형 테두리
cx, cy, r = PW // 2, PH // 2, 370
p_draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=CYAN, width=6)

# "조간" 두 줄
line1, line2 = "조용한", "간호사"
f1 = bold(130)
f2 = bold(130)

b1 = p_draw.textbbox((0, 0), line1, font=f1)
b2 = p_draw.textbbox((0, 0), line2, font=f2)
w1 = b1[2] - b1[0]
h1 = b1[3] - b1[1]
w2 = b2[2] - b2[0]
h2 = b2[3] - b2[1]

gap = 16
total_h = h1 + gap + h2
y1 = cy - total_h // 2
y2 = y1 + h1 + gap

p_draw.text((cx - w1 // 2, y1), line1, font=f1, fill=WHITE)
p_draw.text((cx - w2 // 2, y2), line2, font=f2, fill=CYAN)

p_out = os.path.join(OUT_DIR, "2026-06-14_조용한간호사_프로필.png")
p_img.save(p_out)
print("Saved:", p_out)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2. 썸네일 (1280×720) — v2 클린
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
W, H = 1280, 720
t_img = Image.new("RGB", (W, H), BG)
t_draw = ImageDraw.Draw(t_img, "RGBA")

# 그리드
for x in range(0, W, 80):
    t_draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    t_draw.line([(0, y), (W, y)], fill=GRID, width=1)

# 왼쪽 CYAN 세로 바
t_draw.rectangle([0, 0, 6, H], fill=CYAN)

# 상단 티커 + 회사명
ticker_line = "$LPTH  ·  LightPath Technologies"
t_draw.text((32, 32), ticker_line, font=font(28), fill=CYAN)
t_draw.line([(32, 78), (W - 32, 78)], fill=DARK_GRAY, width=1)

# 메인 훅 텍스트 (3줄)
hook1 = "중국이 게르마늄을"
hook2 = "잠갔을 때,"
hook3 = "미군이 찾은 회사"

t_draw.text((32, 98),  hook1, font=bold(90), fill=WHITE)
t_draw.text((32, 200), hook2, font=bold(90), fill=WHITE)
t_draw.text((32, 320), hook3, font=bold(90), fill=CYAN)

# 하단 구분선 + 서브 텍스트
t_draw.line([(32, 458), (W - 32, 458)], fill=DARK_GRAY, width=1)
t_draw.text((32, 472), "BlackDiamond  ·  NDAA 2030  ·  NRL 독점 라이선스", font=font(22), fill=GRAY)

# 우하단 채널명
ch = "조용한 간호사"
ch_w = int(t_draw.textlength(ch, font=font(22)))
t_draw.text((W - 32 - ch_w, H - 36), ch, font=font(22), fill=GRAY)

t_out = os.path.join(OUT_DIR, "2026-06-14_LPTH_썸네일_v2.png")
t_img.save(t_out)
print("Saved:", t_out)
