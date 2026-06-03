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
draw.rectangle([0, 0, W, 4], fill=BLUE)
draw.rectangle([0, 0, 4, H], fill=BLUE)

# ── 헤더 ──
draw.text((32, 18), "$HPE", font=bold(44), fill=BLUE)
draw.text((32, 70), "익절이냐, Q3 홀드냐", font=bold(30), fill=WHITE)
draw.text((32, 110), "Q2 FY2026 실적 이후 판단 포인트", font=font(20), fill=GRAY)
draw.line([(32, 146), (W - 32, 146)], fill=DARK_GRAY, width=1)

# ── 왼쪽: Q2 핵심 수치 ──
metrics = [
    ("매출",          "$10.7B",  "+40% YoY  /  컨센 +9.6% 상회",       BLUE),
    ("EPS",           "$0.79",   "컨센 $0.53 → 49% 어닝 서프라이즈",    GREEN),
    ("주가 반응",     "+19%",    "역대 단일일 최고 상승",                AMBER),
    ("컨센서스 목표가", "$64",   "현재 ~$54  →  추가 업사이드 +18%",    CYAN),
]
y = 162
for label, value, sub, color in metrics:
    draw.text((32, y), label, font=font(17), fill=GRAY)
    draw.text((32, y + 22), value, font=bold(30), fill=color)
    draw.text((32, y + 58), sub, font=font(16), fill=GRAY)
    draw.line([(32, y + 82), (590, y + 82)], fill=DARK_GRAY, width=1)
    y += 96

# 세로 구분선
draw.line([(620, 143), (620, H - 46)], fill=DARK_GRAY, width=1)

# ── 오른쪽: 주니퍼 현황 ──
draw.text((644, 162), "주니퍼 통합 현황", font=bold(24), fill=WHITE)
draw.line([(644, 196), (W - 32, 196)], fill=DARK_GRAY, width=1)

juniper_items = [
    (AMBER,  "정규화 네트워킹 성장",  "+10%  (헤드라인 +148% ≠ 실체)"),
    (GREEN,  "데이터센터 네트워킹",   "$320M  /  +233% YoY"),
    (CYAN,   "Networks for AI 목표", "연말 $2B  —  전체 네트워킹의 ~20%"),
    (BLUE,   "통합 속도",            "계획보다 빠름  /  수요 pull-in 없음"),
]
y = 208
for color, title, desc in juniper_items:
    draw.rectangle([640, y + 3, 644, y + 30], fill=color)
    draw.text((656, y), title, font=bold(19), fill=WHITE)
    draw.text((656, y + 26), desc, font=font(17), fill=GRAY)
    y += 56

# ── Q3 체크포인트 ──
draw.line([(644, y + 4), (W - 32, y + 4)], fill=DARK_GRAY, width=1)
draw.text((644, y + 14), "Q3 확인 포인트  (2026년 8~9월)", font=bold(21), fill=ORANGE)
y += 46

checks = [
    "① 정규화 네트워킹 성장 두 자릿수 진입",
    "② Networks for AI 주문 가속 여부",
    "③ Aruba + 주니퍼 교차판매 구체화",
]
for line in checks:
    draw.text((644, y), line, font=font(18), fill=GRAY)
    y += 32

# 판단 요약 박스
draw.rounded_rectangle([644, y + 10, W - 32, y + 56], radius=8, fill=(18, 38, 68))
draw.text((658, y + 22), "두 개 이상 확인 → '기대 → 실적' 전환  =  홀드", font=bold(18), fill=CYAN)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.03  |  HPE IR · 어닝콜 · TipRanks", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-03_HPE_홀드판단.png")
img.save(out)
print("Saved:", out)
