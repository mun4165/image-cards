from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-21"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); RED=(239,68,68); ORANGE=(249,115,22)
ACCENT = AMBER

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,18), "국방부가 게르마늄을 공식 리스크로 못 박았다", font=bold(38), fill=ACCENT)
draw.text((32,70), "희토류 공급망 $1.225B 대출 — LPTH 직접 수혜는 아니다", font=bold(23), fill=WHITE)
draw.text((32,104), "돈이 아니라 '말'을 봐야 한다 · 정책 기조가 향하는 방향", font=font(18), fill=GRAY)
draw.line([(32,138),(W-32,138)], fill=DARK_GRAY, width=1)

# 좌측 — 팩트 (돈이 간 곳)
draw.text((32,156), "이번 대출 — 돈이 간 곳", font=bold(22), fill=WHITE)
draw.line([(32,190),(610,190)], fill=DARK_GRAY, width=1)
metrics = [
    ("Energy Fuels", "$725M", "희토류 분리·금속화 시설", CYAN),
    ("Phoenix Tailings", "$500M", "채굴→자석 '프리덤 퍼실리티'", GREEN),
]
y=204
for label,value,sub,color in metrics:
    draw.text((32,y), label, font=font(17), fill=GRAY)
    draw.text((32,y+22), value, font=bold(28), fill=color)
    draw.text((180,y+30), sub, font=font(16), fill=GRAY)
    draw.line([(32,y+66),(610,y+66)], fill=DARK_GRAY, width=1); y+=82

# 핵심 경고 박스 — 직접 수혜 아님
draw.rounded_rectangle([32,y+4,610,y+74], radius=8, fill=(40,20,16))
draw.rectangle([32,y+4,36,y+74], fill=RED)
draw.text((50,y+15), "둘 다 희토류 자석 라인", font=bold(19), fill=RED)
draw.text((50,y+42), "게르마늄·적외선 광학엔 1달러도 안 들어감", font=font(17), fill=GRAY)
y+=92

# 좌측 하단 — 핵심 발언
draw.text((32,y+4), "그래서 봐야 할 건 자금이 아니라 발언", font=bold(18), fill=WHITE)
draw.rounded_rectangle([32,y+34,610,y+126], radius=8, fill=(28,22,8))
draw.text((48,y+48), "“게르마늄·갈륨·희토류가 없으면", font=bold(20), fill=AMBER)
draw.text((48,y+76), "  무기 증산은 헛된 꿈이다”", font=bold(20), fill=AMBER)
draw.text((48,y+104), "— 미 국방부 산업기반정책 차관보", font=font(15), fill=GRAY)

# 가운데 구분선
draw.line([(648,150),(648,H-58)], fill=DARK_GRAY, width=1)

# 우측 — 왜 LPTH 테제의 배경인가
draw.text((672,156), "왜 LPTH 테제의 배경인가", font=bold(22), fill=WHITE)
draw.line([(672,190),(W-32,190)], fill=DARK_GRAY, width=1)
points = [
    (RED,   "병목", "적외선 광학 핵심 소재 = 게르마늄"),
    (ORANGE,"리스크", "정제 게르마늄 다수 中 · 2023년 수출통제"),
    (GREEN, "해답", "BlackDiamond — 게르마늄-프리 광학"),
]
y=204
for color,title,desc in points:
    draw.rectangle([668,y+3,672,y+30], fill=color)
    draw.text((684,y), title, font=bold(20), fill=WHITE)
    draw.text((684,y+27), desc, font=font(17), fill=GRAY); y+=60

draw.line([(672,y+6),(W-32,y+6)], fill=DARK_GRAY, width=1); y+=20
draw.text((672,y), "직접 카탈리스트는 따로 있다", font=bold(20), fill=BLUE)
y+=34
cats = [
    "국방부 Phase 2 자금 (대체재 인증, 직접 수령)",
    "G5 게르마늄-프리 냉각 카메라 양산 시작",
    "백로그 $111M · 85% 방산 · C-UAS·SPEIR",
]
for c in cats:
    draw.text((672,y), "·", font=bold(18), fill=BLUE)
    draw.text((690,y), c, font=font(17), fill=GRAY); y+=30

y+=14
draw.rounded_rectangle([672,y,W-32,y+62], radius=8, fill=(10,28,52))
draw.text((688,y+12), "수급 뉴스가 아니라 방향 확인 뉴스다", font=bold(18), fill=BLUE)
draw.text((688,y+36), "정책 기조가 게르마늄-프리로 굳어지는 중", font=bold(18), fill=BLUE)

# 푸터
draw.line([(32,H-44),(W-32,H-44)], fill=DARK_GRAY, width=1)
draw.text((32,H-30), "2026.06.21  |  LPTH · 국방부 희토류 대출 · 정책 기조", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-21_LPTH_국방부게르마늄정책기조.png")
img.save(out); print("Saved:", out)
