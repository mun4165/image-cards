from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-09"
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

# 테두리 (RED — 중국 반도체 테마)
draw.rectangle([0, 0, W, 4], fill=RED)
draw.rectangle([0, 0, 4, H], fill=RED)

# ── 헤더 ──
draw.text((32, 14), "창신메모리(CXMT) — 중국 DRAM 굴기 핵심압축", font=bold(36), fill=WHITE)
draw.text((32, 62), "2026.06.09  |  중국 반도체  |  세계 4위 DRAM · IPO 추진 · 시장점유율 7.67%", font=font(18), fill=RED)
draw.line([(32, 96), (W - 32, 96)], fill=DARK_GRAY, width=1)

CONTENT_TOP = 110
CONTENT_BOT = H - 52
LEFT_W = 580

# ── 왼쪽: 핵심 수치 ──
draw.text((32, CONTENT_TOP), "핵심 수치", font=bold(18), fill=GRAY)

left_items = [
    (RED,    "세계 4위 DRAM",
              "시장점유율 7.67%  |  웨이퍼 26만 장/월",
              "3년 만에 3배 증설 — 세계 DRAM 물량 10% 점유"),
    (AMBER,  "Q1 2026 실적",
              "매출 +719% YoY  |  순이익 +1,268% 흑전",
              "상반기 순이익 가이던스 9~11조 원"),
    (CYAN,   "IPO 추진 중",
              "조달 목표 6조 원  |  상하이 STAR Market",
              "시장 기대 시총 최대 400조 원"),
]

item_h = (CONTENT_BOT - CONTENT_TOP - 32) // 3
y = CONTENT_TOP + 32
for color, title, line1, line2 in left_items:
    draw.rounded_rectangle([32, y, LEFT_W, y + item_h - 8], radius=8, fill=(20, 24, 34))
    draw.rectangle([32, y, 38, y + item_h - 8], fill=color)
    draw.text((52, y + 10), title, font=bold(18), fill=color)
    draw.text((52, y + 40), line1, font=font(16), fill=WHITE)
    draw.text((52, y + 66), line2, font=font(14), fill=GRAY)
    y += item_h

# ── 세로 구분선 ──
draw.line([(610, 96), (610, CONTENT_BOT)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 투자 논점 ──
RIGHT_X = 630

draw.text((RIGHT_X, CONTENT_TOP), "투자 논점", font=bold(18), fill=GRAY)

total_right = CONTENT_BOT - CONTENT_TOP - 32
ritem_h = int(total_right * 0.30)
warn_h   = total_right - ritem_h * 2 - 16

right_top = [
    (GREEN, "Bull — 중국 내수 독점",
             "국산 DRAM 유일한 공급자  |  빅펀드·정부 전폭 지원"),
    (BLUE,  "Bull — 실적 모멘텀",
             "수익성 전환 완료  |  CSI STAR50 편입 수급 임박"),
]

ry = CONTENT_TOP + 32
for color, title, sub in right_top:
    draw.rounded_rectangle([RIGHT_X, ry, W - 32, ry + ritem_h - 8], radius=8, fill=(20, 24, 34))
    draw.rectangle([RIGHT_X, ry, RIGHT_X + 6, ry + ritem_h - 8], fill=color)
    draw.text((RIGHT_X + 20, ry + 12), title, font=bold(18), fill=color)
    draw.text((RIGHT_X + 20, ry + 48), sub, font=font(14), fill=GRAY)
    ry += ritem_h + 8

# Bear 리스크 박스
warn_y   = ry
warn_bot = warn_y + warn_h - 8
draw.rounded_rectangle([RIGHT_X, warn_y, W - 32, warn_bot], radius=8, fill=(28, 16, 16))
draw.rounded_rectangle([RIGHT_X, warn_y, W - 32, warn_bot], radius=8, outline=RED, width=1)
draw.text((RIGHT_X + 20, warn_y + 12),  "⚠  Bear 3가지",                                    font=bold(16), fill=RED)
draw.text((RIGHT_X + 20, warn_y + 46),  "① 미국 제재 — EUV 봉쇄, 추가 확대 리스크",         font=font(14), fill=GRAY)
draw.text((RIGHT_X + 20, warn_y + 74),  "② HBM 격차 — 삼성·하이닉스 대비 3년 뒤처짐",       font=font(14), fill=GRAY)
draw.text((RIGHT_X + 20, warn_y + 102), "③ DRAM 사이클 피크 IPO — 가격 하락 시 이중 타격",   font=font(14), fill=GRAY)

# ── 하단 바 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.09", font=font(15), fill=GRAY)
draw.text((W - 500, H - 30), "창신메모리 · CXMT · 중국 DRAM · 핵심압축", font=bold(15), fill=RED)

out = os.path.join(OUT_DIR, "2026-06-09_cxmt_핵심압축.png")
img.save(out)
print("Saved:", out)
