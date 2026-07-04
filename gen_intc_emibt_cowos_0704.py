from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-04"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "EMIB-T, TSMC 독점에 균열 낼까", font=bold(40), fill=ACCENT)
draw.text((32,78), "확인된 사실만 정리 — 인텔 vs TSMC 패키징", font=bold(22), fill=GRAY)
draw.line([(32,120),(W-32,120)], fill=DARK_GRAY, width=1)

# 세로 구분선
draw.line([(648,140),(648,556)], fill=DARK_GRAY, width=1)

# ── 좌측: 두 포장 방식 로드맵 ──
draw.text((40,146), "레티클 배수 로드맵", font=bold(20), fill=ACCENT)

draw.text((40,196), "CoWoS-L · TSMC", font=bold(24), fill=TEAL)
draw.text((40,230), "2026  5.5x", font=font(18), fill=WHITE)
draw.text((40,256), "2027  9.5x", font=font(18), fill=WHITE)
draw.text((40,282), "2029  14x", font=font(18), fill=WHITE)

draw.text((40,336), "EMIB-T · 인텔", font=bold(24), fill=AMBER)
draw.text((40,370), "2026  8x", font=font(18), fill=WHITE)
draw.text((40,396), "2028  12x+", font=font(18), fill=WHITE)
draw.text((40,422), "범프피치 45→35→25마이크로미터", font=font(16), fill=GRAY)

draw.text((40,476), "패널활용 90% vs 웨이퍼 60%", font=font(16), fill=GRAY)
draw.text((40,500), "→ TSMC도 CoPoS(사각패널)로 대응 중", font=font(16), fill=CYAN)

# ── 우측: 확인된 채택 현황 ──
RX = 680
draw.text((RX,146), "확인된 채택 현황", font=bold(20), fill=ACCENT)

rows = [
    ("구글 TPU v8e", "EMIB 채택 사실상 확정", GREEN),
    ("메타 · 마벨 · 미디어텍", "차세대 가속기 검토 중", WHITE),
    ("SK하이닉스", "자체 HBM EMIB 통합 테스트", WHITE),
    ("엔비디아 · AMD", "여전히 CoWoS (GPU 대역폭 우선)", GRAY),
]
ry = 190
for name, note, color in rows:
    draw.text((RX,ry), name, font=bold(19), fill=color)
    draw.text((RX,ry+26), note, font=font(16), fill=GRAY)
    ry += 62

draw.text((RX,ry+10), "→ 채택처는 전부 ASIC 진영", font=bold(18), fill=CYAN)
draw.text((RX,ry+38), "GPU 물량은 그대로 TSMC 몫", font=font(16), fill=GRAY)

# ── 하단 핵심 박스 ──
by = 580
draw.rounded_rectangle([32,by,W-32,by+62], radius=8, fill=(8,30,30))
draw.text((50,by+10), "독점의 균열이 아니라, GPU와 ASIC이라는 다른 트랙이 갈라지는 중", font=bold(20), fill=GREEN)
draw.text((50,by+36), "인텔은 EMIB-T 단독공급 리스크, TSMC는 CoPoS로 응수 — 구도는 계속 움직인다", font=font(16), fill=GRAY)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.04  |  INTC · TSMC 첨단 패키징", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-04_INTC_EMIBT_TSMC.png")
img.save(out); print("Saved:", out)
