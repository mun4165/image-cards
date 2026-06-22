from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-22"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "마이크론을 팠더니 인텔이 읽혔다", font=bold(40), fill=ACCENT)
draw.text((32,78), "한 산업의 병목 단어 하나가, 옆을 보는 렌즈가 된다", font=bold(22), fill=GRAY)
draw.line([(32,120),(W-32,120)], fill=DARK_GRAY, width=1)

# 세로 구분선 (좌: 통섭 흐름 / 우: 두 포장 방식)
draw.line([(648,140),(648,556)], fill=DARK_GRAY, width=1)

# ── 좌측: 통섭이 연결된 순서 ──
draw.text((40,146), "이렇게 연결됐다", font=bold(20), fill=ACCENT)
steps = [
    ("1   마이크론을 기초부터 팠다", "CoWoS = GPU와 HBM을 한 판에 붙이는 포장", "그 포장을 사실상 TSMC가 쥔 병목이다", TEAL),
    ("2   병목 단어 하나를 얻었다", "'잘 만드는 것'만큼 '잘 붙이는 것'이 중요", "패키징이라는 말이 크게 보이기 시작", BLUE),
    ("3   인텔 뉴스가 다르게 읽혔다", "SK하이닉스 前 CEO를 영입했는데,", "직책이 '첨단 패키징 총괄'이었다", AMBER),
]
ys = [190, 296, 402]
for (head, s1, s2, color), y in zip(steps, ys):
    draw.ellipse([42,y+6,58,y+22], fill=color)
    draw.text((72,y), head, font=bold(23), fill=WHITE)
    draw.text((72,y+33), s1, font=font(17), fill=color)
    draw.text((72,y+57), s2, font=font(17), fill=GRAY)
draw.text((78,266), "↓", font=bold(24), fill=DARK_GRAY)
draw.text((78,372), "↓", font=bold(24), fill=DARK_GRAY)

# ── 우측: 두 포장 방식, 쉽게 ──
RX = 680
draw.text((RX,146), "두 포장 방식, 쉽게", font=bold(20), fill=ACCENT)
draw.text((RX,196), "CoWoS · TSMC", font=bold(24), fill=TEAL)
draw.text((RX,230), "실리콘 깔판을 통째로 깐다", font=font(18), fill=WHITE)
draw.text((RX,256), "튼튼하지만 비싸고 크게 못 키운다", font=font(17), fill=GRAY)

draw.text((RX,316), "EMIB · 인텔", font=bold(24), fill=AMBER)
draw.text((RX,350), "필요한 곳만 다리로 잇는다", font=font(18), fill=WHITE)
draw.text((RX,376), "더 싸고 크게 키우기 유리하다", font=font(17), fill=GRAY)

draw.text((RX,446), "포장 자체가 부족해진 지금,", font=font(17), fill=GRAY)
draw.text((RX,472), "EMIB의 강점이 새로 부각된다", font=bold(18), fill=CYAN)

# ── 하단 핵심 박스 ──
by = 580
draw.rounded_rectangle([32,by,W-32,by+62], radius=8, fill=(8,30,30))
draw.text((50,by+10), "포장 싸움의 승자가 누구든, 그 사이 HBM은 어차피 박힌다", font=bold(20), fill=GREEN)
draw.text((50,by+36), "한 분야를 깊이 파면, 그 깊이가 옆 분야를 읽는 렌즈가 된다 — 아는 만큼 보인다", font=font(16), fill=GRAY)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.22  |  통섭 · CoWoS vs EMIB", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-22_통섭_CoWoS_EMIB.png")
img.save(out); print("Saved:", out)
