from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-23"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = BLUE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "코어위브 vs 네비우스 vs 아이렌", font=bold(37), fill=ACCENT)
draw.text((32,74), "같은 네오클라우드(AI 전용 클라우드), 강점이 셋 다 다르다", font=bold(21), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, sub, players, role, fact):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+24), label, font=bold(27), fill=color)
    draw.text((60, y+64), sub, font=font(17), fill=GRAY)
    draw.line([(440,y+18),(440,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((468, y+16), players, font=bold(23), fill=WHITE)
    draw.text((468, y+50), role, font=font(18), fill=GRAY)
    draw.text((468, y+78), fact, font=bold(18), fill=color)

# 코어위브 — 규모
band(138, 112, AMBER, (34,28,12),
     "코어위브 · 규모", "가장 순수한 AI 클라우드 사업자",
     "1분기 매출 20.8억$ · 수주잔고 994억$",
     "가동 전력 1GW 초과 · 계약 전력 3.5GW 이상",
     "부채 ~300억$ · 분기 이자 3.88억$ (재무 부담)")

# 네비우스 — 재무
band(258, 112, CYAN, (8,30,36),
     "네비우스 · 재무", "엔비디아와 서버 랙 자체 설계",
     "현금 60억$ 이상 · 전환사채 ~40억$",
     "셋 중 재무 체력이 가장 탄탄",
     "연결 전력 800MW → 1GW 확보 목표")

# 아이렌 — 전력
band(378, 112, GREEN, (10,32,24),
     "아이렌 · 전력", "비트코인 채굴에서 AI로 전환",
     "마이크로소프트 97억$ · 엔비디아 직접계약",
     "전력·부지(캠퍼스)를 이미 쥔 출발점",
     "2026년 말 GPU(그래픽처리장치) 14만 개 목표")

# 하단 핵심 박스
by = 512
draw.rounded_rectangle([32,by,W-32,by+90], radius=10, fill=(16,24,40))
draw.text((52,by+14), "규모는 코어위브 · 재무는 네비우스 · 전력은 아이렌", font=bold(20), fill=AMBER)
draw.text((52,by+50), "같은 AI 인프라주로 묶이지만, 강점과 위험이 서로 다르다", font=bold(20), fill=CYAN)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.23  |  CRWV · NBIS · IREN", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-23_네오클라우드_3사비교.png")
img.save(out); print("Saved:", out)
