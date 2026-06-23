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
draw.text((32,22), "빅테크가 무너진 날, 자세히 보면 '회전'이었다", font=bold(37), fill=ACCENT)
draw.text((32,74), "2026.06.22 미국장 · 플랫폼 대형주는 하락, 반도체는 상승", font=bold(20), fill=GRAY)
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
    (RED, (34,16,16), "① GOOGL", "Alphabet",
     "재심 기각 + 영국 검색 규제", "법적·규제 악재 겹침 · 3%대 후반 하락"),
    (ORANGE, (34,22,12), "② 빅테크 캐펙스", "Amazon · Meta · Microsoft",
     "AI 설비투자 과잉 우려", "'성장 기대'가 '현금 소진' 경계감으로"),
    (GREEN, (10,32,24), "③ 반도체", "Semiconductors",
     "같은 시간 오히려 상승", "MU +6.8% · 돈이 옮겨간 자리"),
]
y0 = 130; bh = 92; step = 100
for i,(color,fbg,label,sub,hl,det) in enumerate(bands):
    band(y0+i*step, bh, color, fbg, label, sub, hl, det)

# 하단 핵심 박스
by = 444
draw.rounded_rectangle([32,by,W-32,by+96], radius=10, fill=(10,22,40))
draw.text((52,by+16), "돈이 빠진 게 아니라 자리를 옮긴 것", font=bold(22), fill=AMBER)
draw.text((52,by+54), "광고·플랫폼 → AI 하드웨어·메모리 · 빅테크 급락을 기술주 붕괴로 읽으면 방향을 놓친다", font=bold(20), fill=BLUE)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.23  |  GOOGL · MU", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-23_빅테크_섹터로테이션.png")
img.save(out); print("Saved:", out)
