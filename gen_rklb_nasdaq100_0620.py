from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-20"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); RED=(239,68,68); ORANGE=(249,115,22)
ACCENT = TEAL

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,18), "로켓랩, 6/22 나스닥100 편입", font=bold(40), fill=ACCENT)
draw.text((32,72), "우주 기업이 빅테크 지수에 들어간다", font=bold(24), fill=WHITE)
draw.text((32,108), "패시브 자금은 호재 — 단, 편입은 단기 수급 이벤트", font=font(18), fill=GRAY)
draw.line([(32,142),(W-32,142)], fill=DARK_GRAY, width=1)

# 좌측 수치
metrics = [
    ("편입 발효",      "6/22(월) 개장 전", "분기 리밸런싱 편입", TEAL),
    ("1분기 매출",     "$200.3M",         "분기 최대 · +63.5% YoY", GREEN),
    ("수주 잔고",      "$2.2B",           "백로그 +108% YoY", GREEN),
    ("주가 / 1년",     "약 +280%",        "밸류에이션 부담 구간", AMBER),
]
y=158
for label,value,sub,color in metrics:
    draw.text((32,y), label, font=font(17), fill=GRAY)
    draw.text((32,y+22), value, font=bold(28), fill=color)
    draw.text((32,y+56), sub, font=font(16), fill=GRAY)
    draw.line([(32,y+80),(590,y+80)], fill=DARK_GRAY, width=1); y+=92

draw.line([(620,140),(620,H-46)], fill=DARK_GRAY, width=1)

# 우측 논지
draw.text((644,158), "수급 이벤트와 사업 성장을 분리하라", font=bold(23), fill=WHITE)
draw.line([(644,192),(W-32,192)], fill=DARK_GRAY, width=1)
points = [
    (GREEN, "패시브 자금 유입", "나스닥100 추종 ETF 기계적 매수"),
    (CYAN,  "대형주 위상 격상", "테마주 → 인덱스 구성종목"),
    (BLUE,  "수주의 질", "우주군 T3 $816M · HASTE $190M"),
    (ORANGE,"진짜 변곡점 = 뉴트론", "4분기 첫 발사 · 상업계약 5건"),
]
y=204
for color,title,desc in points:
    draw.rectangle([640,y+3,644,y+30], fill=color)
    draw.text((656,y), title, font=bold(20), fill=WHITE)
    draw.text((656,y+28), desc, font=font(17), fill=GRAY); y+=62

draw.line([(644,y+4),(W-32,y+4)], fill=DARK_GRAY, width=1); y+=18
draw.rounded_rectangle([644,y,W-32,y+62], radius=8, fill=(8,38,34))
draw.text((658,y+12), "편입은 일회성 수급 — 전후 변동성↑", font=bold(18), fill=TEAL)
draw.text((658,y+36), "본질 변곡점은 4분기 뉴트론 첫 발사", font=bold(18), fill=TEAL)

draw.line([(32,H-44),(W-32,H-44)], fill=DARK_GRAY, width=1)
draw.text((32,H-30), "2026.06.20  |  RKLB Q1'26 · Nasdaq · stockanalysis.com", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-20_RKLB_나스닥100편입.png")
img.save(out); print("Saved:", out)
