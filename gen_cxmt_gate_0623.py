from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-23"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = ORANGE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "중국 메모리 CXMT — 진짜 변수는 '두 리스트의 틈'", font=bold(36), fill=ACCENT)
draw.text((32,74), "2026.06.23 · 구글 계약설은 썰, 그러나 게이트 구조는 진짜다", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, sub, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(23), fill=color)
    draw.text((60, y+52), sub, font=font(15), fill=GRAY)
    draw.line([(470,y+16),(470,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((498, y+18), headline, font=bold(21), fill=WHITE)
    draw.text((498, y+54), detail, font=font(16), fill=color)

bands = [
    (RED, (34,16,16), "국방부 1260H 리스트", "Chinese military company",
     "CXMT 등재됨", "서구 기업 구매 시 컴플라이언스 심사 필요"),
    (AMBER, (34,24,8), "상무부 Entity List", "직접 거래를 막는 리스트",
     "아직 미등재 (보류 중)", "직접 거래는 안 막힘 = 회색지대"),
    (CYAN, (8,30,36), "이 틈이 가른다", "The Gate",
     "누가 CXMT를 살 수 있나", "PC에 넣는 것과 클라우드·AI에 넣는 건 무게가 다름"),
]
y0 = 130; bh = 92; step = 100
for i,(color,fbg,label,sub,hl,det) in enumerate(bands):
    band(y0+i*step, bh, color, fbg, label, sub, hl, det)

# 하단 핵심 박스 — 메모리 사이클 함의
by = 444
draw.rounded_rectangle([32,by,W-32,by+96], radius=10, fill=(10,22,40))
draw.text((52,by+14), "단기는 강자 편 — 공급부족에 DRAM 계약가 +98% YoY", font=bold(20), fill=GREEN)
draw.text((52,by+50), "장기 위협은 범용 DRAM 바닥 · HBM은 3~4년 뒤처져 아직 인큐번트 방패", font=bold(20), fill=BLUE)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.23  |  CXMT · MU · SK Hynix · Samsung", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-23_CXMT_두리스트의틈.png")
img.save(out); print("Saved:", out)
