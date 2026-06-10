from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-11"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
RED       = (239, 68, 68)
AMBER     = (245, 158, 11)
GREEN     = (52, 211, 153)
CYAN      = (6, 182, 212)
BLUE      = (59, 130, 246)

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")

for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

draw.rectangle([0, 0, W, 4], fill=CYAN)
draw.rectangle([0, 0, 4, H], fill=CYAN)

# ── 헤더 ──
draw.text((32, 14), "SpaceX $SPCX — 상장 전날 소송, 이게 리스크인가", font=bold(36), fill=WHITE)
draw.text((32, 62), "2026.06.11  |  Nasdaq 상장 D-1  |  공모가 $135", font=font(18), fill=CYAN)
draw.line([(32, 98), (W - 32, 98)], fill=DARK_GRAY, width=1)

CONTENT_TOP = 114
CONTENT_BOT = H - 52

# ── 왼쪽 ──
LEFT_W = 490

# IPO 핵심 수치 박스
draw.text((32, CONTENT_TOP), "IPO 핵심", font=bold(17), fill=GRAY)
ipo_box_h = 150
draw.rounded_rectangle([32, CONTENT_TOP + 26, LEFT_W, CONTENT_TOP + 26 + ipo_box_h], radius=10, fill=(14, 24, 36))
draw.rounded_rectangle([32, CONTENT_TOP + 26, LEFT_W, CONTENT_TOP + 26 + ipo_box_h], radius=10, outline=CYAN, width=2)

stats = [
    ("공모가", "$135  고정"),
    ("시총",   "$1.77조  —  역대 최대 IPO"),
    ("조달",   "$750억"),
    ("수요",   "2배 초과청약  /  기관 $100억+"),
]
sy = CONTENT_TOP + 42
for label, val in stats:
    draw.text((52, sy), label, font=font(13), fill=GRAY)
    draw.text((120, sy), val, font=bold(14), fill=WHITE)
    sy += 28

# 소송 박스
draw.text((32, CONTENT_TOP + 26 + ipo_box_h + 16), "소송 내용", font=bold(17), fill=GRAY)
suit_top = CONTENT_TOP + 26 + ipo_box_h + 42
suit_bot = CONTENT_BOT
draw.rounded_rectangle([32, suit_top, LEFT_W, suit_bot], radius=8, fill=(28, 18, 18))
draw.rectangle([32, suit_top, 38, suit_bot], fill=RED)

suit_lines = [
    ("6월 9일 제기", RED),
    ("환경단체 → 연방법원 가처분 청구", WHITE),
    ("Starbase 토지 교환 중단 요구", WHITE),
    ("", None),
    ("교환 구조", GRAY),
    ("SpaceX 683에이커  →  연방정부", WHITE),
    ("연방 보호구역 715에이커  →  SpaceX", WHITE),
    ("", None),
    ("FWS 6월 1일 이미 승인 완료", AMBER),
]
ly = suit_top + 14
for text, color in suit_lines:
    if text and color:
        draw.text((52, ly), text, font=font(13) if color == GRAY else bold(13), fill=color)
        ly += 26
    else:
        ly += 8

# ── 세로 구분선 ──
draw.line([(514, 98), (514, CONTENT_BOT)], fill=DARK_GRAY, width=1)

# ── 오른쪽 ──
RX = 534

# 판단 박스
draw.text((RX, CONTENT_TOP), "소송이 IPO에 미치는 영향", font=bold(17), fill=GRAY)
judge_h = 110
draw.rounded_rectangle([RX, CONTENT_TOP + 26, W - 32, CONTENT_TOP + 26 + judge_h], radius=8, fill=(16, 30, 20))
draw.rounded_rectangle([RX, CONTENT_TOP + 26, W - 32, CONTENT_TOP + 26 + judge_h], radius=8, outline=GREEN, width=2)
draw.text((RX + 20, CONTENT_TOP + 42), "없다", font=bold(28), fill=GREEN)
draw.text((RX + 20, CONTENT_TOP + 82), "기관들은 로드쇼(6월 4일~)에서 이미 알고 있었다", font=font(14), fill=GRAY)
draw.text((RX + 20, CONTENT_TOP + 106), "알고도 2배 초과청약  —  시장이 소화한 것", font=bold(14), fill=WHITE)

# 진짜 변수 3개
var_top = CONTENT_TOP + 26 + judge_h + 16
draw.text((RX, var_top), "상장 이후 진짜 변수", font=bold(17), fill=GRAY)

variables = [
    (AMBER,  "Musk 지분 오버행",      "보유 지분 ~40%  /  락업 해제 후 매각 가능성"),
    (RED,    "개인 배정 물량 30%",    "소매 비중 높을수록 첫날 변동성 확대"),
    (BLUE,   "S&P 500 편입 요건",     "4분기 연속 GAAP 흑자 필요  /  FY25 영업손실 $26억"),
]

vy = var_top + 26
vbox_h = (CONTENT_BOT - vy) // 3 - 5

for color, title, desc in variables:
    draw.rounded_rectangle([RX, vy, W - 32, vy + vbox_h], radius=8, fill=(18, 22, 34))
    draw.rectangle([RX, vy, RX + 6, vy + vbox_h], fill=color)
    draw.text((RX + 20, vy + 12), title, font=bold(16), fill=color)
    draw.text((RX + 20, vy + 42), desc, font=font(13), fill=GRAY)
    vy += vbox_h + 5

# ── 하단 결론 바 ──
draw.line([(32, H - 52), (W - 32, H - 52)], fill=DARK_GRAY, width=1)
draw.rounded_rectangle([32, H - 48, W - 32, H - 8], radius=6, fill=(14, 24, 36))
draw.text((52, H - 36), "소송은 노이즈  —  주가 방향은 Musk 오버행·개인 물량·지수 편입 타임라인이 결정한다", font=bold(16), fill=CYAN)

out = os.path.join(OUT_DIR, "2026-06-11_SPCX_IPO_lawsuit.png")
img.save(out)
print("Saved:", out)
