from PIL import Image, ImageDraw, ImageFont
import os

# 리틀리 책1 상품 표지 — 블로그 프로필 카드(gen_blog_profile_0624.py) 톤 매칭
# 다크+시안, 심전도→차트 모티프 유지. 단 '전자책 표지'답게 책 제목이 주인공.
FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-24"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1080, 1080
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
CYAN=(6,182,212); GREEN=(52,211,153)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 108): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 108): draw.line([(0,y),(W,y)], fill=GRID, width=1)

# 모서리 ㄱ자 액센트 (4코너)
L=80; t=8; m=40
for (ox,oy,dx,dy) in [(m,m,1,1),(W-m,m,-1,1),(m,H-m,1,-1),(W-m,H-m,-1,-1)]:
    draw.line([(ox,oy),(ox+dx*L,oy)], fill=ACCENT, width=t)
    draw.line([(ox,oy),(ox,oy+dy*L)], fill=ACCENT, width=t)

cx = W//2

# 상단 배지: 투자 전자책
badge_txt = "투자 전자책"
bf = bold(34)
bb = draw.textbbox((0,0), badge_txt, font=bf)
bw, bh = bb[2]-bb[0], bb[3]-bb[1]
padx, pady = 34, 18
by = 215
draw.rounded_rectangle([cx-bw//2-padx, by-bh//2-pady, cx+bw//2+padx, by+bh//2+pady],
                       radius=40, outline=ACCENT, width=3)
draw.text((cx, by), badge_txt, font=bf, fill=ACCENT, anchor="mm")

# 제목 (주인공)
draw.text((cx, 400), "처절하게", font=bold(128), fill=WHITE, anchor="mm")
draw.text((cx, 540), "기업을 팠다", font=bold(128), fill=WHITE, anchor="mm")

# 부제
draw.text((cx, 645), "생각이 쌓이면 흔들리지 않는다", font=font(40), fill=GRAY, anchor="mm")

# 모티프: 심전도선 → 차트선 (간호사 → 투자, 통섭) — 프로필 카드와 동일 디자인 확대
my = 800
ecg = [(190,my),(280,my),(310,my-14),(340,my+14),(380,my),
       (412,my),(428,my-96),(454,my+76),(474,my),(540,my)]
draw.line(ecg, fill=CYAN, width=6, joint="curve")
draw.ellipse([530,my-10,550,my+10], fill=CYAN)
chart = [(540,my),(610,my-38),(680,my-18),(750,my-74),(820,my-50),(890,my-128)]
draw.line(chart, fill=GREEN, width=6, joint="curve")
ax,ay = 890,my-128
draw.line([(ax,ay),(ax-26,ay+10)], fill=GREEN, width=6)
draw.line([(ax,ay),(ax-10,ay+26)], fill=GREEN, width=6)

# 하단 저자
draw.text((cx, 950), "조용한간호사", font=bold(46), fill=WHITE, anchor="mm")
draw.text((cx, 1002), "X  @quietnurse_", font=bold(30), fill=ACCENT, anchor="mm")

out = os.path.join(OUT_DIR, "2026-06-24_리틀리_책1표지.png")
img.save(out); print("Saved:", out)
