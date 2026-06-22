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
draw.text((32,22), "작은 회사의 도달은 인수자에게로 일어난다", font=bold(37), fill=ACCENT)
draw.text((32,74), "CPO(공동패키지광학) 지도의 세 층 — 사는 자 · 달리는 자 · 통행료", font=bold(21), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, sub, players, role, fact):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+24), label, font=bold(27), fill=color)
    draw.text((60, y+64), sub, font=font(17), fill=GRAY)
    draw.line([(420,y+18),(420,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((448, y+16), players, font=bold(23), fill=WHITE)
    draw.text((448, y+50), role, font=font(18), fill=GRAY)
    draw.text((448, y+78), fact, font=bold(18), fill=color)

# 위층 — 사는 자
band(138, 112, AMBER, (34,28,12),
     "위층 · 사는 자", "build냐 buy냐를 결정",
     "Marvell · AMD · Nvidia · Ciena",
     "보도자료는 말, 인수는 서명된 수표다",
     "Marvell → Celestial AI 인수 (수십억 달러)")

# 가운데 — 달리는 자
band(258, 112, CYAN, (8,30,36),
     "가운데 · 달리는 자", "딥테크 IP는 진짜",
     "POET · Sivers · Celestial · Ayar Labs",
     "그러나 대부분 아직 매출 전(前) 단계",
     "도달 = 자력 매출 아닌 '인수당함' · 단일고객 리스크")

# 아래층 — 통행료
band(378, 112, GREEN, (10,32,24),
     "아래층 · 통행료", "누가 이기든 걷힌다",
     "InP(인듐인) 기판 — 소수 공급사",
     "어떤 레이저가 표준이 돼도 InP는 필요",
     "'도달'이 바이너리가 아닌 유일한 층")

# 하단 핵심 박스
by = 512
draw.rounded_rectangle([32,by,W-32,by+90], radius=10, fill=(8,30,36))
draw.text((52,by+14), "Marvell은 POET를 흔들었고, 시간이 지나 같은 분야 Celestial을 샀다", font=bold(20), fill=AMBER)
draw.text((52,by+50), "달리는 자 = 인수자의 선택을 맞히는 베팅 · 통행료 = 누가 이기든 테마를 그대로 쥔다", font=bold(20), fill=CYAN)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.22  |  CPO  Co-Packaged Optics", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-22_CPO_3층렌즈_인수가도달.png")
img.save(out); print("Saved:", out)
