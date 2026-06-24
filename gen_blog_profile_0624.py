from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-24"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 640, 640
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 64): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 64): draw.line([(0,y),(W,y)], fill=GRID, width=1)

# 모서리 ㄱ자 액센트 (4코너)
L=46; t=5
for (ox,oy,dx,dy) in [(24,24,1,1),(W-24,24,-1,1),(24,H-24,1,-1),(W-24,H-24,-1,-1)]:
    draw.line([(ox,oy),(ox+dx*L,oy)], fill=ACCENT, width=t)
    draw.line([(ox,oy),(ox,oy+dy*L)], fill=ACCENT, width=t)

cx = W//2

# 키커
draw.text((cx, 196), "기업 리서치 · 투자 기록", font=bold(22), fill=GRAY, anchor="mm")

# 이름
draw.text((cx, 262), "조용한간호사", font=bold(74), fill=WHITE, anchor="mm")

# 모티프: 심전도선 → 차트선 (간호사 → 투자, 통섭)
my = 380
# ECG (왼쪽)
ecg = [(96,my),(150,my),(168,my-8),(186,my+8),(210,my),
       (228,my),(238,my-58),(252,my+46),(264,my),(300,my)]
draw.line(ecg, fill=CYAN, width=4, joint="curve")
# 전환점 표시
draw.ellipse([294,my-6,306,my+6], fill=CYAN)
# 차트 상승 계단 (오른쪽)
chart = [(300,my),(340,my-22),(380,my-10),(420,my-44),(460,my-30),(508,my-78)]
draw.line(chart, fill=GREEN, width=4, joint="curve")
# 상승 화살촉
ax,ay = 508,my-78
draw.line([(ax,ay),(ax-16,ay+6)], fill=GREEN, width=4)
draw.line([(ax,ay),(ax-6,ay+16)], fill=GREEN, width=4)

# 하단 핸들
draw.text((cx, 486), "X  @quietnurse_", font=bold(24), fill=ACCENT, anchor="mm")
draw.text((cx, 528), "통섭과 통찰로, 기업을 처절하게 판다", font=font(19), fill=GRAY, anchor="mm")

out = os.path.join(OUT_DIR, "2026-06-24_블로그프로필.png")
img.save(out); print("Saved:", out)
