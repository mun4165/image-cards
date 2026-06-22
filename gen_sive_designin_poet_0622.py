from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-22"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "Sivers — 한 종목이 다섯 곳에 디자인인", font=bold(38), fill=ACCENT)
draw.text((32,76), "플러거블 · CPO · 외부광원에 같은 레이저가 깔렸다", font=bold(22), fill=GRAY)
draw.line([(32,120),(W-32,120)], fill=DARK_GRAY, width=1)

# 가운데 세로 구분선
MIDX = 648
draw.line([(MIDX,150),(MIDX,604)], fill=DARK_GRAY, width=1)

# ── 좌측: 확인된 디자인인 5곳 ──
draw.text((50,150), "1차 자료로 확인된 디자인인 5곳", font=bold(23), fill=WHITE)
designs = [
    ("Jabil (JBL)",        "1.6T 플러거블 트랜시버 · 전력 2.5배 절감", CYAN),
    ("GlobalFoundries",    "CPO 레퍼런스 설계에 레이저 통합",          BLUE),
    ("O-Net · Enablence",  "CPO용 외부광원(ELS) 공동 개발",            GREEN),
    ("POET",               "외부광원 모듈 — POET조차 Sivers의 고객",   TEAL),
    ("Ayar Labs",          "16파장 레이저 · 공개된 유일 공급사",        AMBER),
]
top, step = 200, 78
for i,(co,role,color) in enumerate(designs):
    y = top + step*i
    draw.ellipse([54,y+4,78,y+28], fill=color)
    draw.text((61,y+5), str(i+1), font=bold(20), fill=BG)
    draw.text((96,y-2), co, font=bold(24), fill=color)
    draw.text((96,y+30), role, font=font(18), fill=GRAY)

# ── 우측: POET와 무엇이 다른가 ──
RX = 680
draw.text((RX,150), "POET와 무엇이 다른가", font=bold(23), fill=WHITE)

draw.rounded_rectangle([RX,196,W-32,290], radius=8, fill=(34,16,16))
draw.text((RX+18,208), "POET = 단일 방식 베팅", font=bold(21), fill=RED)
draw.text((RX+18,240), "고유 옵티컬 인터포저가 표준으로", font=font(18), fill=GRAY)
draw.text((RX+18,262), "채택돼야 생존 — 밀리면 통째로 흔들림", font=font(18), fill=GRAY)

draw.rounded_rectangle([RX,304,W-32,398], radius=8, fill=(8,30,36))
draw.text((RX+18,316), "Sivers = 아키텍처 중립 부품", font=bold(21), fill=CYAN)
draw.text((RX+18,348), "플러거블이든 CPO든, 누가 표준이", font=font(18), fill=GRAY)
draw.text((RX+18,370), "돼도 빛 만드는 레이저는 필요", font=font(18), fill=GRAY)

draw.text((RX,420), "단, 안전하다는 뜻은 아니다", font=bold(20), fill=AMBER)
draw.text((RX+4,452), "•  5곳 모두 '외부 레이저' 한 전제 위 →", font=font(18), fill=GRAY)
draw.text((RX+22,476), "분산 아닌 한 덩어리 베팅", font=font(18), fill=GRAY)
draw.text((RX+4,506), "•  디자인인 ≠ 매출 (레이저는 소액 BOM,", font=font(18), fill=GRAY)
draw.text((RX+22,530), "큰 고객은 공급사 이중화)", font=font(18), fill=GRAY)

# 하단 핵심 박스
by = 622
draw.rounded_rectangle([32,by,W-32,by+58], radius=8, fill=(8,30,36))
draw.text((50,by+9), "결국 '외부 레이저 시대 + Sivers가 그걸 돈으로 바꾼다'는 한 줄짜리 베팅", font=bold(20), fill=CYAN)
draw.text((50,by+34), "다섯이라는 숫자가 그 단일함을 가려줄 뿐이다", font=font(16), fill=GRAY)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.22  |  SIVE  Sivers Semiconductors", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-22_SIVE_디자인인5곳_POET비교.png")
img.save(out); print("Saved:", out)
