from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-20"
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
draw.text((32,18), "마이크론 실적 6/24 (한국 6/25 새벽)", font=bold(40), fill=ACCENT)
draw.text((32,72), "이미 8배 오른 메모리주의 진짜 시험대", font=bold(24), fill=WHITE)
draw.text((32,108), "관건은 '얼마나 좋냐'가 아니라 '높아진 기대를 또 넘냐'다", font=font(18), fill=GRAY)
draw.line([(32,142),(W-32,142)], fill=DARK_GRAY, width=1)

# 좌측 수치
metrics = [
    ("컨센서스 매출",   "약 $34.5B",  "가이던스 $35.5B · +274% YoY", GREEN),
    ("컨센서스 EPS",    "약 $19.7",   "+900%+ YoY", GREEN),
    ("주가 / 1년",      "$1,134",     "약 +820% (사상 최고권)", CYAN),
    ("기대 이동",       "EPS 컨센↑",  "3개월전 $11.7 → $19.7", AMBER),
]
y=158
for label,value,sub,color in metrics:
    draw.text((32,y), label, font=font(17), fill=GRAY)
    draw.text((32,y+22), value, font=bold(28), fill=color)
    draw.text((32,y+56), sub, font=font(16), fill=GRAY)
    draw.line([(32,y+80),(590,y+80)], fill=DARK_GRAY, width=1); y+=92

draw.line([(620,140),(620,H-46)], fill=DARK_GRAY, width=1)

# 우측 논지
draw.text((644,158), "주가는 실적이 아니라 가이던스가 정한다", font=bold(23), fill=WHITE)
draw.line([(644,192),(W-32,192)], fill=DARK_GRAY, width=1)
points = [
    (GREEN, "HBM 완판", "향후 여러 분기 sold out 선언"),
    (CYAN,  "진짜 변수 = 다음 가이던스", "이번 분기 숫자는 이미 선반영"),
    (BLUE,  "HBM 2027 배정·고객계약", "내년 물량을 누구에게 얼마에"),
    (RED,   "리스크 = 기대 선반영", "소문에 사서 뉴스에 파는 패턴"),
]
y=204
for color,title,desc in points:
    draw.rectangle([640,y+3,644,y+30], fill=color)
    draw.text((656,y), title, font=bold(20), fill=WHITE)
    draw.text((656,y+28), desc, font=font(17), fill=GRAY); y+=62

draw.line([(644,y+4),(W-32,y+4)], fill=DARK_GRAY, width=1); y+=18
draw.rounded_rectangle([644,y,W-32,y+62], radius=8, fill=(15,23,42))
draw.text((658,y+12), "'기대를 또 넘느냐'의 시험대", font=bold(18), fill=BLUE)
draw.text((658,y+36), "다음 가이던스 · HBM 2027 배정을 봐라", font=bold(18), fill=BLUE)

draw.line([(32,H-44),(W-32,H-44)], fill=DARK_GRAY, width=1)
draw.text((32,H-30), "2026.06.20  |  Zacks · AlphaStreet · stockanalysis.com", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-20_MU_실적프리뷰.png")
img.save(out); print("Saved:", out)
