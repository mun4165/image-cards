from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-15"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 10)
WHITE     = (255, 255, 255)
GRAY      = (130, 145, 165)
DARK_GRAY = (45, 58, 72)
BLUE      = (74, 144, 217)
BLUE_DIM  = (28, 65, 120)
BLUE_BG   = (16, 32, 58)
AMBER     = (245, 180, 50)
RED       = (239, 90, 80)
GREEN     = (72, 200, 140)
YELLOW    = (240, 200, 60)

def font(size):
    return ImageFont.truetype(FONT_PATH, size, index=0)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")

# 배경 그리드
for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

# 상단 강조선
draw.rectangle([0, 0, W, 4], fill=BLUE)

# ── 태그 ──
draw.rounded_rectangle([32, 22, 248, 52], radius=15, fill=BLUE_BG)
draw.rounded_rectangle([32, 22, 248, 52], radius=15, outline=BLUE_DIM, width=1)
draw.text((50, 30), "GEOPOLITICS · 2026.06.15", font=font(14), fill=BLUE)

# ── 타이틀 ──
draw.text((32, 66), "이란 휴전협정 &", font=bold(52), fill=WHITE)
draw.text((32, 126), "호르무즈 해협 개방", font=bold(52), fill=BLUE)
draw.text((32, 190), "트럼프 \"딜 완료\" 선언  —  6월 19일 스위스 서명 예정", font=font(18), fill=GRAY)

# 세로 구분선
draw.line([(550, 22), (550, H - 50)], fill=DARK_GRAY, width=1)

# ── 왼쪽 하단: DEAL 조건 ──
LX = 32
LY = 234
draw.text((LX, LY), "DEAL 핵심 조건", font=bold(16), fill=GRAY)
draw.line([(LX, LY + 28), (510, LY + 28)], fill=DARK_GRAY, width=1)

conditions = [
    ("호르무즈 통행",  "통행료 없이 완전 개방",        BLUE),
    ("기뢰 제거",      "이란, 30일 이내 전량 제거 의무", AMBER),
    ("휴전 기간",      "60일 연장 → 최종 딜 협상 진행", WHITE),
    ("서명 일정",      "6월 19일, 스위스",              GREEN),
]

cy = LY + 44
for label, value, color in conditions:
    draw.rounded_rectangle([LX, cy, 518, cy + 52], radius=8, fill=(20, 26, 36))
    draw.rectangle([LX, cy, LX + 4, cy + 52], fill=color)
    draw.text((LX + 18, cy + 8), label, font=font(14), fill=GRAY)
    draw.text((LX + 18, cy + 30), value, font=bold(17), fill=color)
    cy += 62

# ── 오른쪽: MARKET SIGNAL ──
RX = 578
RY = 22

draw.text((RX, RY), "MARKET SIGNAL", font=bold(16), fill=GRAY)
draw.line([(RX, RY + 28), (W - 32, RY + 28)], fill=DARK_GRAY, width=1)

signals = [
    ("유가",            "단기 하락 압력",           "봉쇄 프리미엄 해소  /  OPEC+ 감산이 바닥 지탱",                  RED),
    ("운임 (BDI·컨)", "점진적 정상화",            "홍해 우회 변수 잔존  /  드라마틱한 하락 없음",                    YELLOW),
    ("방산",            "모멘텀 약화",              "리스크 해소로 수혜 약화  /  중동 재무장 사이클은 유지",            AMBER),
    ("반도체·전자",    "간접 긍정",                "운임 안정 + 에너지 하락  →  공급망 원가 압력 완화",              GREEN),
]

sy = RY + 44
ROW_H = (H - 50 - sy) // 4 - 6
for name, signal, desc, color in signals:
    draw.rounded_rectangle([RX, sy, W - 32, sy + ROW_H], radius=8, fill=(18, 24, 34))
    draw.rectangle([RX, sy, RX + 4, sy + ROW_H], fill=color)
    draw.text((RX + 18, sy + 10), name, font=bold(18), fill=WHITE)
    draw.rounded_rectangle([RX + 18, sy + 38, RX + 18 + len(signal) * 14 + 16, sy + 62], radius=6, fill=(28, 36, 52))
    draw.text((RX + 26, sy + 41), signal, font=bold(14), fill=color)
    draw.text((RX + 18, sy + ROW_H - 26), desc, font=font(13), fill=GRAY)
    sy += ROW_H + 6

# ── 하단 ──
draw.line([(32, H - 46), (W - 32, H - 46)], fill=DARK_GRAY, width=1)
draw.text((32, H - 32), "개인 공부 기록  ·  투자 권유 아님", font=font(15), fill=(50, 68, 90))
draw.text((W - 200, H - 32), "#이란 #호르무즈 #지정학", font=font(15), fill=(50, 68, 90))

out = os.path.join(OUT_DIR, "2026-06-15_이란_호르무즈.png")
img.save(out, "PNG")
print("Saved:", out)
