from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-24"
os.makedirs(OUT_DIR, exist_ok=True)

# 네이버 블로그 타이틀: 기본 스킨 가로 966px 안전. 높이 조절 가능.
W, H = 966, 340
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
# 전체 프레임 (4면 시안)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)
draw.rectangle([0,H-4,W,H], fill=ACCENT); draw.rectangle([W-4,0,W,H], fill=ACCENT)

cx = W//2

# 상단 키커 (안 변하는 문구)
draw.text((cx, 54), "기업 리서치 · 투자 기록",
          font=bold(18), fill=GRAY, anchor="mm")

# 메인 타이틀
draw.text((cx, 138), "조용한간호사의 투자일기", font=bold(60), fill=WHITE, anchor="mm")

# 시안 구분선 (짧게 중앙)
draw.line([(cx-130, 188),(cx+130, 188)], fill=ACCENT, width=2)

# 태그라인
draw.text((cx, 222), "통섭과 통찰로, 기업을 처절하게 판다",
          font=bold(26), fill=ACCENT, anchor="mm")

# 하단 깔때기 한 줄
draw.text((cx, 292), "실시간 메모 X @quietnurse_   |   투자 전자책 「처절하게 기업을 팠다」",
          font=font(18), fill=GRAY, anchor="mm")

out = os.path.join(OUT_DIR, "2026-06-24_블로그타이틀배너.png")
img.save(out); print("Saved:", out)
