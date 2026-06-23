from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-23"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = RED

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "코스피 8% 폭락 · 서킷브레이커 발동", font=bold(38), fill=ACCENT)
draw.text((32,76), "원인은 한국에 있지 않다 — 글로벌 위험회피의 충격이 가장 크게 닿는 자리", font=bold(20), fill=GRAY)
draw.line([(32,120),(W-32,120)], fill=DARK_GRAY, width=1)

# 좌측 — 오늘의 팩트
draw.text((48, 142), "오늘의 팩트", font=bold(22), fill=WHITE)
facts = [
    ("14:33", "코스피 -8%대 · 1단계 서킷브레이커"),
    ("8,378", "지수 급락 · 매매 20분 중단"),
    ("14:37", "코스닥도 -8%대 동반 서킷"),
    ("올해 4번째", "반복되는 변동성 국면"),
]
fy = 186
for big, sub in facts:
    draw.text((48, fy), big, font=bold(30), fill=ACCENT)
    draw.text((48, fy+38), sub, font=font(16), fill=GRAY)
    fy += 84

# 세로 구분선
draw.line([(560,150),(560,500)], fill=DARK_GRAY, width=1)

# 우측 — 진짜 원인
draw.text((588, 142), "진짜 원인 두 가지", font=bold(22), fill=WHITE)
def reason(y, color, label, l1, l2):
    draw.text((588, y), label, font=bold(22), fill=color)
    draw.text((588, y+34), l1, font=font(17), fill=WHITE)
    draw.text((588, y+60), l2, font=font(16), fill=GRAY)
reason(190, AMBER, "① 미국 금리인상 공포",
       "5월 고용 +17.2만 (전망 8만의 2배 초과)",
       "연말 금리인상 확률 70%+ → 기술주 선흔들림")
reason(300, CYAN, "② 중동 지정학",
       "미·이란 협상 교착 · 호르무즈 무력충돌",
       "원유 길목 불안 → 유가·안전자산 동시 자극")
reason(410, BLUE, "왜 하필 한국이 8%인가",
       "수출·반도체·외국인 민감 = 고베타 시장",
       "기업이 무너진 게 아니라 충격이 가장 크게 전달")

# 하단 핵심 박스
by = 522
draw.rounded_rectangle([32,by,W-32,by+88], radius=10, fill=(34,20,20))
draw.text((52,by+14), "전날 Micron은 +6.8% 신고가권 마감 (Anthropic 협약)", font=bold(20), fill=GREEN)
draw.text((52,by+48), "개별 펀더멘털 붕괴가 아닌 매크로발 위험회피 → 패닉의 성격이 다르다", font=bold(20), fill=RED)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.23  |  KOSPI 서킷브레이커 (올해 4번째)", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-23_코스피_서킷브레이커_원인.png")
img.save(out); print("Saved:", out)
