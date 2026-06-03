from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-03"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (60, 70, 82)
AMBER     = (245, 158, 11)
TEAL      = (20, 184, 166)
BLUE      = (59, 130, 246)
CYAN      = (6, 182, 212)
GREEN     = (52, 211, 153)
RED       = (239, 68, 68)
ORANGE    = (249, 115, 22)

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

# 상단·좌측 강조선
draw.rectangle([0, 0, W, 4], fill=AMBER)
draw.rectangle([0, 0, 4, H], fill=AMBER)

# ── 헤더 ──
draw.text((32, 18), "하모닉드라이브시스템 (6324.T)", font=bold(40), fill=AMBER)
draw.text((32, 72), "인간형 로봇 관절 속 감속기, 그 원조 회사", font=bold(26), fill=WHITE)
draw.text((32, 108), "전 세계 대량 생산 가능 기업 5개 미만 · 휴머노이드 1대당 14~20개 탑재", font=font(18), fill=GRAY)
draw.line([(32, 142), (W - 32, 142)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 핵심 수치 ──
metrics = [
    ("주가 (2026.06.02)",  "7,110엔",   "1년 수익률 +124%  /  PER 120배",        AMBER),
    ("FY2026 매출",        "596억 엔",  "+7.0% YoY  /  순이익 -53.7% 급감",     BLUE),
    ("FY2027 가이던스",    "영업이익 62억 엔", "+141% YoY  /  영업이익률 9% 목표", GREEN),
    ("수주 총액",          "295억 엔",  "+14.3% YoY  /  다음 실적 8월 11일",     CYAN),
]
y = 158
for label, value, sub, color in metrics:
    draw.text((32, y), label, font=font(17), fill=GRAY)
    draw.text((32, y + 22), value, font=bold(28), fill=color)
    draw.text((32, y + 56), sub, font=font(16), fill=GRAY)
    draw.line([(32, y + 80), (590, y + 80)], fill=DARK_GRAY, width=1)
    y += 92

# 세로 구분선
draw.line([(620, 140), (620, H - 46)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 투자 포인트 ──
draw.text((644, 158), "투자 포인트 & 리스크", font=bold(24), fill=WHITE)
draw.line([(644, 192), (W - 32, 192)], fill=DARK_GRAY, width=1)

points = [
    (AMBER,  "병목 포지션",
     "감속기 대량 생산 전 세계 5개 미만  —  비중국 독점 후보"),
    (GREEN,  "FY2027 이익 레버리지",
     "매출 +14%  →  영업이익 +141%  /  고정비 구조 작동"),
    (RED,    "테슬라 리스크",
     "옵티머스, 中 Green Harmonic 공급사 채택 확정"),
    (BLUE,   "밸류에이션 부담",
     "컨센 목표가 5,416엔  —  현재가 대비 -24%"),
]
y = 204
for color, title, desc in points:
    draw.rectangle([640, y + 3, 644, y + 30], fill=color)
    draw.text((656, y), title, font=bold(20), fill=WHITE)
    draw.text((656, y + 28), desc, font=font(17), fill=GRAY)
    y += 62

# ── 체크포인트 박스 ──
draw.line([(644, y + 4), (W - 32, y + 4)], fill=DARK_GRAY, width=1)
draw.text((644, y + 14), "8월 11일 체크포인트", font=bold(20), fill=ORANGE)
y += 46

checks = [
    "① 수주잔고 증가 전환 여부  (현재 -7.5% YoY)",
    "② 비중국 휴머노이드 공급 계약 공식 발표",
    "③ 영업이익률 가이던스 유지 여부",
]
for line in checks:
    draw.text((644, y), line, font=font(17), fill=GRAY)
    y += 30

# 판단 요약 박스
draw.rounded_rectangle([644, y + 8, W - 32, y + 50], radius=8, fill=(40, 28, 10))
draw.text((658, y + 18), "기대 선반영 구간  —  실적 확인 후 판단", font=bold(18), fill=AMBER)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.03  |  HDSI IR · ainvest · alphabiz  |  개인 공부 기록, 투자 추천 아님", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-03_하모닉드라이브_6324.png")
img.save(out)
print("Saved:", out)
