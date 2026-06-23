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
draw.text((32,22), "Anthropic이 Micron에 들어왔다 — 네 겹의 협약", font=bold(37), fill=ACCENT)
draw.text((32,74), "2026.06.22 발표 · FY3Q 실적(6.25) 사흘 전 · 발표 당일 MU +4~5%", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, sub, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(24), fill=color)
    draw.text((60, y+52), sub, font=font(15), fill=GRAY)
    draw.line([(420,y+16),(420,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((448, y+18), headline, font=bold(21), fill=WHITE)
    draw.text((448, y+54), detail, font=font(16), fill=color)

bands = [
    (AMBER, (34,28,12), "① 공동 설계", "Claude 맞춤 메모리 구조",
     "HBM·DRAM·SSD를 함께 최적화", "목표 = 토큰 이코노믹스(처리비용) 개선"),
    (CYAN, (8,30,36), "② 다년 공급", "Multi-year Supply",
     "데이터센터 메모리 장기 공급", "Anthropic 인프라 확장 물량을 락인"),
    (GREEN, (10,32,24), "③ 지분 투자", "Anthropic Series H",
     "돈 넣은 쪽은 Micron이다", "AI 회사에 메모리 회사가 전략 투자"),
    (BLUE, (10,22,40), "④ 사내 도입", "Claude 확대 적용",
     "엔지니어링·제조·전사 업무", "파는 쪽이 쓰는 쪽이기도 한 구조"),
]
y0 = 130; bh = 86; step = 94
for i,(color,fbg,label,sub,hl,det) in enumerate(bands):
    band(y0+i*step, bh, color, fbg, label, sub, hl, det)

# 하단 핵심 박스
by = 512
draw.rounded_rectangle([32,by,W-32,by+90], radius=10, fill=(10,22,40))
draw.text((52,by+14), "다만 계약 규모(금액·물량)는 미공개", font=bold(20), fill=AMBER)
draw.text((52,by+50), "HBM은 2026 물량 완판 상태 → 신규 증분이냐 캐파 재배분이냐를 6.25 실적이 가른다", font=bold(20), fill=BLUE)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.23  |  MU  Micron Technology × Anthropic", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-23_MU_앤트로픽협약_네겹.png")
img.save(out); print("Saved:", out)
