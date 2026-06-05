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

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")

# 그리드
for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

# 상단/좌측 테두리
draw.rectangle([0, 0, W, 4], fill=AMBER)
draw.rectangle([0, 0, 4, H], fill=AMBER)

# ── 헤더 ──
draw.text((32, 14), "$AXTI  —  미국 수출 1%인데 왜 중국 규제가 더 위험한가", font=bold(34), fill=WHITE)
draw.text((32, 60), "2026.06.05  |  생산기지 = 베이징  |  갈륨·게르마늄 수출 규제", font=font(18), fill=AMBER)
draw.line([(32, 92), (W - 32, 92)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 구조 다이어그램 ──
draw.text((32, 106), "매출 구조", font=bold(19), fill=GRAY)

# 베이징 공장 박스
draw.rounded_rectangle([32, 136, 390, 210], radius=8, fill=(20, 30, 50))
draw.rounded_rectangle([32, 136, 390, 210], radius=8, outline=CYAN, width=2)
draw.text((50, 148), "Beijing Tongmei", font=bold(22), fill=CYAN)
draw.text((50, 178), "실제 생산 기지 (중국 베이징)", font=font(15), fill=GRAY)

# 화살표 + 목적지
arrow_x = 210
draw.line([(arrow_x, 210), (arrow_x, 250)], fill=DARK_GRAY, width=2)
draw.polygon([(arrow_x-6, 248), (arrow_x+6, 248), (arrow_x, 258)], fill=DARK_GRAY)

# 아태 박스
draw.rounded_rectangle([60, 262, 360, 316], radius=6, fill=(15, 35, 25))
draw.rounded_rectangle([60, 262, 360, 316], radius=6, outline=GREEN, width=2)
draw.text((80, 270), "아태 (한국·일본·대만)", font=bold(18), fill=GREEN)
draw.text((80, 294), "매출 비중  78%", font=font(15), fill=GREEN)

# US 박스
draw.rounded_rectangle([60, 328, 360, 382], radius=6, fill=(30, 20, 20))
draw.rounded_rectangle([60, 328, 360, 382], radius=6, outline=RED, width=2)
draw.text((80, 336), "미국", font=bold(18), fill=RED)
draw.text((80, 360), "매출 비중  1%", font=font(15), fill=RED)

# 핵심 포인트
draw.rounded_rectangle([32, 398, 390, 470], radius=6, fill=(30, 25, 10))
draw.text((50, 410), "아태 78%도", font=font(16), fill=GRAY)
draw.text((50, 432), "베이징에서 만들어서 나간다", font=bold(18), fill=AMBER)
draw.text((50, 456), "→ 중국법 적용 대상", font=font(15), fill=AMBER)

# ── 세로 구분선 ──
draw.line([(420, 92), (420, H - 44)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 규제 비교 ──
draw.text((444, 106), "규제 비교", font=bold(19), fill=GRAY)
draw.line([(444, 134), (W - 32, 134)], fill=DARK_GRAY, width=1)

# 미국 BIS
draw.rounded_rectangle([444, 144, 840, 310], radius=8, fill=(25, 15, 15))
draw.rectangle([444, 144, 448, 310], fill=RED)
draw.text((462, 152), "미국 BIS 규제", font=bold(20), fill=RED)
draw.text((462, 184), "누구한테 파느냐", font=bold(17), fill=WHITE)
draw.text((462, 210), "→ 판매처 제한", font=font(16), fill=GRAY)
draw.text((462, 238), "특정 국가·기업 판매 금지", font=font(15), fill=GRAY)
draw.text((462, 262), "AXTI 매출 1%에 해당", font=font(15), fill=RED)
draw.text((462, 286), "영향 범위: 제한적", font=bold(15), fill=RED)

# 중국 MOFCOM
draw.rounded_rectangle([444, 324, 840, 520], radius=8, fill=(15, 25, 15))
draw.rectangle([444, 324, 448, 520], fill=GREEN)
draw.text((462, 332), "중국 MOFCOM 규제", font=bold(20), fill=GREEN)
draw.text((462, 364), "어디서 출발하느냐", font=bold(17), fill=WHITE)
draw.text((462, 390), "→ 생산·출하 자체 차단", font=font(16), fill=GRAY)
draw.text((462, 418), "갈륨(Ga)·게르마늄(Ge) 수출 허가제", font=font(15), fill=GRAY)
draw.text((462, 442), "GaAs·InP·Ge 기판 전부 해당", font=font(15), fill=GRAY)
draw.text((462, 466), "아태 78% + 미국 1% 전부 영향", font=font(15), fill=GREEN)
draw.text((462, 492), "영향 범위: 전체 매출", font=bold(15), fill=GREEN)

# ── 오른쪽 끝: 핵심 결론 ──
draw.rounded_rectangle([860, 144, W - 32, 520], radius=8, fill=(18, 22, 32))
draw.rectangle([860, 144, 864, 520], fill=PURPLE)
draw.text((880, 152), "핵심", font=bold(20), fill=PURPLE)
draw.text((880, 190), "허가 지연 or 거부 시", font=font(16), fill=GRAY)
draw.text((880, 216), "어디에 팔든", font=bold(22), fill=WHITE)
draw.text((880, 248), "공장이 멈춘다", font=bold(28), fill=PURPLE)

draw.line([(880, 292), (W - 48, 292)], fill=DARK_GRAY, width=1)

draw.text((880, 308), "2023.08", font=bold(15), fill=AMBER)
draw.text((880, 330), "중국, 갈륨·게르마늄", font=font(15), fill=GRAY)
draw.text((880, 352), "전략 물자 지정", font=font(15), fill=GRAY)

draw.line([(880, 388), (W - 48, 388)], fill=DARK_GRAY, width=1)

draw.text((880, 404), "리스크 순위", font=bold(15), fill=AMBER)
draw.text((880, 428), "① 중국 수출 허가", font=font(15), fill=GREEN)
draw.text((880, 452), "② 미·중 갈등 심화", font=font(15), fill=AMBER)
draw.text((880, 476), "③ 미국 BIS 제재", font=font(15), fill=RED)
draw.text((880, 500), "(직접 영향 작음)", font=font(13), fill=GRAY)

# ── 하단 바 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.05", font=font(15), fill=GRAY)
draw.text((W - 220, H - 30), "$AXTI  AXT Inc.", font=bold(15), fill=AMBER)

out = os.path.join(OUT_DIR, "2026-06-05_AXTI_중국규제리스크.png")
img.save(out)
print("Saved:", out)
