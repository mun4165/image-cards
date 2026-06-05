from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-05"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
RED       = (239, 68, 68)
ORANGE    = (249, 115, 22)
AMBER     = (245, 158, 11)
GREEN     = (52, 211, 153)
CYAN      = (6, 182, 212)
PURPLE    = (167, 139, 250)

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)

def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

def make_base(accent):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=GRID, width=1)
    draw.rectangle([0, 0, W, 4], fill=accent)
    draw.rectangle([0, 0, 4, H], fill=accent)
    return img, ImageDraw.Draw(img)

def footer(draw, date_str, source_str):
    draw.line([(60, H - 52), (W - 60, H - 52)], fill=DARK_GRAY, width=1)
    draw.text((60, H - 36), f"{date_str}  |  {source_str}", font=font(17), fill=GRAY)


img, draw = make_base(PURPLE)

# ── 헤더 ──
draw.text((60, 18), "SIVE  6/15 주주총회 — 이사회 교체·희석 카드·전환사채", font=bold(33), fill=WHITE)
draw.text((60, 62), "시버스세미컨덕터 2026 AGM 핵심 안건 압축 정리", font=font(20), fill=GRAY)
draw.line([(60, 98), (W - 60, 98)], fill=DARK_GRAY, width=1)

# ── 왼쪽 ──
lx = 60

# 이사회 변경
draw.text((lx, 112), "이사회 변경", font=bold(21), fill=GRAY)

board = [
    ("퇴임", "Tomas Duffy · Erik Fällström · Keith Halsey", RED),
    ("신임", "Joakim Nideborn(부회장) · Helena Svancar",    GREEN),
    ("유임", "Bami Bastani(회장) · Karin Raj · Todd Thomson", GRAY),
]
y = 144
for tag, names, color in board:
    draw.rectangle([lx, y, lx + 4, y + 38], fill=color)
    draw.text((lx + 14, y + 2),  tag,   font=bold(17), fill=color)
    draw.text((lx + 14, y + 22), names, font=font(15), fill=GRAY)
    y += 48

draw.line([(lx, y + 4), (lx + 560, y + 4)], fill=DARK_GRAY, width=1)

# P11 옵션
y += 18
draw.text((lx, y), "P11 직원 스톡옵션", font=bold(21), fill=GRAY)
y += 30
draw.text((lx, y),       "최대 7,000,000 옵션  |  희석 ~2.0%", font=font(17), fill=AMBER)
draw.text((lx, y + 24),  "행사가: 부여 시점 VWAP × 110%", font=font(17), fill=GRAY)
draw.text((lx, y + 48),  "가결 요건: 전체 의결권 9/10 이상", font=bold(17), fill=ORANGE)

draw.line([(lx, y + 76), (lx + 560, y + 76)], fill=DARK_GRAY, width=1)

# 배당
y += 90
draw.text((lx, y), "배당", font=bold(21), fill=GRAY)
draw.text((lx, y + 30), "FY2025 이익 전액 이월  —  배당 없음", font=font(17), fill=GRAY)

# 주식 발행 권한
draw.line([(lx, y + 58), (lx + 560, y + 58)], fill=DARK_GRAY, width=1)
y += 72
draw.text((lx, y), "일반 주식 발행 권한", font=bold(21), fill=GRAY)
draw.text((lx, y + 30), "최대 53,844,956주  —  현 발행주식 대비 약 15% 희석", font=font(17), fill=AMBER)
draw.text((lx, y + 54), "이사회 단독 집행 가능  |  방식 제한 없음", font=font(16), fill=GRAY)

# ── 세로 구분선 ──
draw.line([(648, 98), (648, H - 60)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 전환사채 핵심 ──
rx = 672
draw.text((rx, 112), "전환사채  —  가장 눈에 걸린 안건", font=bold(21), fill=GRAY)

cb = [
    ("발행 금액",  "USD 327,072",           WHITE),
    ("이자율",    "10.85%  연고정",          AMBER),
    ("만기",      "2029년 12월 31일",        GRAY),
    ("전환가",    "4.77 SEK / 주",           CYAN),
    ("발행 대상", "Bootstrap Europe 4.0",   GRAY),
]
y = 144
for label, val, color in cb:
    draw.text((rx, y),        label, font=font(16), fill=GRAY)
    draw.text((rx + 200, y),  val,   font=bold(20), fill=color)
    draw.line([(rx, y + 32), (W - 60, y + 32)], fill=DARK_GRAY, width=1)
    y += 42

# 핵심 박스
y += 6
draw.rounded_rectangle([rx, y, W - 60, y + 100], radius=8, fill=(10, 30, 50))
draw.text((rx + 16, y + 10), "전환가  4.77 SEK", font=bold(28), fill=CYAN)
draw.text((rx + 16, y + 46), "현재 주가  SEK 80  →  전환가 대비 약 17배",  font=bold(20), fill=ORANGE)
draw.text((rx + 16, y + 74), "Bootstrap 입장에선 이미 확정된 수익",        font=font(17), fill=GRAY)

# 연간 수익률 메모
y += 114
draw.rounded_rectangle([rx, y, W - 60, y + 52], radius=8, fill=(25, 25, 15))
draw.text((rx + 16, y + 8),  "YTD +1,700%  올랐는데", font=bold(19), fill=AMBER)
draw.text((rx + 16, y + 32), "재무 구조는 아직 정비 중  —  둘 다 봐야 한다", font=font(16), fill=GRAY)

footer(draw, "2026.06.05", "Sivers Semiconductors AGM Notice  |  PR Newswire")

out = os.path.join(OUT_DIR, "2026-06-05_SIVE_AGM.png")
img.save(out)
print("Saved:", out)
