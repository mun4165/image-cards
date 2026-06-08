from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-07"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
AMBER     = (245, 158, 11)
GREEN     = (52, 211, 153)
CYAN      = (6, 182, 212)
PURPLE    = (167, 139, 250)
RED       = (239, 68, 68)
GOLD      = (212, 175, 55)

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

draw.rectangle([0, 0, W, 4], fill=AMBER)
draw.rectangle([0, 0, 4, H], fill=AMBER)

# ── 헤더 ──
draw.text((32, 14), "반도체는 항상 같은 세 개의 문을 통과한다", font=bold(36), fill=WHITE)
draw.text((32, 62), "칩워(Chip War) 독서 메모  ·  2026.06.07", font=font(18), fill=AMBER)
draw.line([(32, 96), (W - 32, 96)], fill=DARK_GRAY, width=1)

CONTENT_TOP = 108
CONTENT_BOT = H - 44

# ── 상단: 3개의 문 ──
gate_w = (W - 64 - 32) // 3
gates = [
    (AMBER,  "① 발명",  "아이디어가 작동하는 것을 증명한다",     "트랜지스터 발명 — 1947"),
    (GREEN,  "② 양산",  "수천, 수만 개를 찍어낼 수 있어야 한다", "페어차일드 — 집적회로 양산"),
    (CYAN,   "③ 시장",  "소화해줄 소비처가 열려야 한다",         "미군 — 위성·어뢰·무기에 탑재"),
]
gx = 32
for color, title, desc, example in gates:
    draw.rounded_rectangle([gx, CONTENT_TOP, gx + gate_w, CONTENT_TOP + 148], radius=8, fill=(20, 22, 30))
    draw.rectangle([gx, CONTENT_TOP, gx + 6, CONTENT_TOP + 148], fill=color)
    draw.text((gx + 18, CONTENT_TOP + 10), title, font=bold(26), fill=color)
    draw.text((gx + 18, CONTENT_TOP + 52), desc, font=font(15), fill=WHITE)
    draw.text((gx + 18, CONTENT_TOP + 80), desc.replace(desc, ""), font=font(13), fill=GRAY)
    draw.rounded_rectangle([gx + 14, CONTENT_TOP + 106, gx + gate_w - 14, CONTENT_TOP + 138], radius=4, fill=(30, 30, 40))
    draw.text((gx + 22, CONTENT_TOP + 114), example, font=font(13), fill=GRAY)
    gx += gate_w + 16

draw.line([(32, CONTENT_TOP + 162), (W - 32, CONTENT_TOP + 162)], fill=DARK_GRAY, width=1)

# ── 중단: 과거 vs 현재 ──
MID_TOP = CONTENT_TOP + 172
MID_BOT = CONTENT_BOT - 58

# 과거
draw.rounded_rectangle([32, MID_TOP, 590, MID_BOT], radius=8, fill=(22, 18, 10))
draw.rectangle([32, MID_TOP, 38, MID_BOT], fill=GOLD)
draw.text((52, MID_TOP + 14), "1960년대", font=bold(20), fill=GOLD)
draw.text((52, MID_TOP + 46), "미군이 시장을 열었다", font=bold(24), fill=WHITE)
rows_past = [
    ("비싸도 가격 불문 매수",              "칩 한 개 가격 = 노동자 월급 수배"),
    ("위성·어뢰·음파탐지기 전 무기 탑재", "1960년대 중반 전 군종 도입 완료"),
    ("양산 학습곡선 하락 → 원가 절감",    "가격이 내려가며 민간 시장이 열림"),
    ("칩 없이 달 착륙도 없었다",           "아폴로 11호 — 칩 수요 최대 소비처"),
]
ry = MID_TOP + 86
for main, sub in rows_past:
    draw.text((52, ry), main, font=bold(16), fill=WHITE)
    draw.text((52, ry + 22), sub, font=font(13), fill=GRAY)
    ry += 54

# 화살표
ax = 608
ay = (MID_TOP + MID_BOT) // 2
draw.text((ax, ay - 24), "같은", font=bold(18), fill=AMBER)
draw.text((ax, ay + 2),  "패턴", font=bold(18), fill=AMBER)
draw.text((ax, ay + 28), "반복", font=bold(18), fill=AMBER)

# 현재
draw.rounded_rectangle([660, MID_TOP, W - 32, MID_BOT], radius=8, fill=(10, 20, 22))
draw.rectangle([660, MID_TOP, 666, MID_BOT], fill=CYAN)
draw.text((680, MID_TOP + 14), "지금", font=bold(20), fill=CYAN)
draw.text((680, MID_TOP + 46), "AI 빅테크가 시장을 열고 있다", font=bold(24), fill=WHITE)
rows_now = [
    ("구글 $847억 주식 팔아 capex 투입",   "자체 현금흐름도 모자란 속도"),
    ("MS · 아마존 · 메타 동일 방향",       "하이퍼스케일러 전체 캡엑스 확대"),
    ("HBM 수요 → DRAM 공급 감소",          "팹 capacity 전환 — 공급 병목"),
    ("마이크론 양산 학습곡선 진입 중",     "HBM3E 엔비디아 공식 인증 완료"),
]
ry = MID_TOP + 86
for main, sub in rows_now:
    draw.text((680, ry), main, font=bold(16), fill=WHITE)
    draw.text((680, ry + 22), sub, font=font(13), fill=GRAY)
    ry += 54

# 하단 인용구
draw.rounded_rectangle([32, MID_BOT + 8, W - 32, CONTENT_BOT], radius=6, fill=(20, 16, 8))
draw.text((52, MID_BOT + 18), "역사를 공부하는 것은 과거를 외우는 것이 아니라,  지금 어디쯤 와 있는지 좌표를 잡는 일이다.", font=bold(17), fill=AMBER)

# ── 하단 바 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.07", font=font(15), fill=GRAY)
draw.text((W - 340, H - 30), "칩워(Chip War)  |  Chris Miller", font=bold(15), fill=AMBER)

out = os.path.join(OUT_DIR, "2026-06-07_칩워_반도체패턴.png")
img.save(out)
print("Saved:", out)
