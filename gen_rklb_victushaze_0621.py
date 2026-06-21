from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-21"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); RED=(239,68,68); ORANGE=(249,115,22)
ACCENT = BLUE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,18), "Victus Haze, 궤도 데이터로 먼저 드러나다", font=bold(38), fill=ACCENT)
draw.text((32,70), "로켓랩 우주군 긴급대응(TacRS) 미션", font=bold(24), fill=WHITE)
draw.text((32,106), "공식 발표 전 — 추적 데이터상 거의 확실한 강한 정황", font=font(18), fill=GRAY)
draw.line([(32,140),(W-32,140)], fill=DARK_GRAY, width=1)

# 좌측 수치
metrics = [
    ("발사 시점 (추정)", "2026.06.19",            "Electron · LC-1 마히아(뉴질랜드)", CYAN),
    ("등록 물체명",      "VICTUS HAZE PUMA",       "Space-Track 카탈로그 등록", GREEN),
    ("확인된 궤도",      "350×460km · 97.4°",      "태양동기궤도(SSO)", BLUE),
    ("계약 규모",        "약 $32M",                "Pioneer급 위성 직접 제작·운용", AMBER),
]
y=156
for label,value,sub,color in metrics:
    draw.text((32,y), label, font=font(17), fill=GRAY)
    draw.text((32,y+22), value, font=bold(27), fill=color)
    draw.text((32,y+56), sub, font=font(16), fill=GRAY)
    draw.line([(32,y+80),(590,y+80)], fill=DARK_GRAY, width=1); y+=92

draw.line([(620,138),(620,H-46)], fill=DARK_GRAY, width=1)

# 우측 논지
draw.text((644,156), "팩트와 추정을 분리하라", font=bold(23), fill=WHITE)
draw.line([(644,190),(W-32,190)], fill=DARK_GRAY, width=1)
points = [
    (GREEN, "팩트", "위성명 · Electron 상단부 · 궤도 모두 확인"),
    (AMBER, "추정", "아마추어 추적 식별 · 회사 공식 미확인"),
    (CYAN,  "오해 주의", "Victus Nox는 Firefly가 발사 (로켓랩 X)"),
    (ORANGE,"투자 관점", "$32M 단건은 작다 · 본진은 뉴트론"),
]
y=202
for color,title,desc in points:
    draw.rectangle([640,y+3,644,y+30], fill=color)
    draw.text((656,y), title, font=bold(20), fill=WHITE)
    draw.text((656,y+28), desc, font=font(17), fill=GRAY); y+=62

draw.line([(644,y+4),(W-32,y+4)], fill=DARK_GRAY, width=1); y+=18
draw.rounded_rectangle([644,y,W-32,y+62], radius=8, fill=(10,28,52))
draw.text((658,y+12), "수주 금액이 아니라 신뢰 자산이 쌓였다", font=bold(18), fill=BLUE)
draw.text((658,y+36), "긴급대응우주 트랙레코드 누적이 핵심", font=bold(18), fill=BLUE)

draw.line([(32,H-44),(W-32,H-44)], fill=DARK_GRAY, width=1)
draw.text((32,H-30), "2026.06.21  |  RKLB · Victus Haze (TacRS) · Space-Track", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-21_RKLB_빅터스헤이즈.png")
img.save(out); print("Saved:", out)
