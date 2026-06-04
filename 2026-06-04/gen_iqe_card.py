from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-04"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 72)
AMBER     = (245, 158, 11)
AMBER_DIM = (120, 76, 5)
GREEN     = (52, 211, 153)
RED       = (239, 68, 68)
CYAN      = (6, 182, 212)
ORANGE    = (249, 115, 22)
PURPLE    = (167, 139, 250)

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

def base_canvas():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=GRID, width=1)
    draw.rectangle([0, 0, W, 4], fill=CYAN)
    draw.rectangle([0, 0, 4, H], fill=CYAN)
    return img, draw

def footer(draw, source):
    draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
    draw.text((32, H - 30), f"2026.06.04  |  {source}  |  개인 공부 기록", font=font(15), fill=GRAY)

img, draw = base_canvas()

# 헤더
draw.text((32, 14), "IQE", font=bold(40), fill=CYAN)
draw.text((118, 18), "에피웨이퍼 독점 소재업체 — 공급망의 숨은 병목", font=bold(26), fill=WHITE)
draw.text((118, 56), "LSE:AIM  |  화합물반도체 업스트림  |  2026.06.04 정리", font=font(16), fill=GRAY)
draw.line([(32, 86), (W - 32, 86)], fill=DARK_GRAY, width=1)

# ── 컬럼 1: 공급망 구조 + 제품 ──
C1 = 32
draw.text((C1, 96), "공급망 위치", font=bold(18), fill=CYAN)
draw.line([(C1, 120), (400, 120)], fill=DARK_GRAY, width=1)

chain = [
    (GRAY,   "[AXT]",   "InP·GaAs 기판 제조"),
    (AMBER,  "[IQE]",   "에피택셜 층 증착  ←  여기"),
    (GRAY,   "[MACOM]", "칩 가공 → 완성품"),
]
y = 128
for color, ticker, desc in chain:
    draw.rectangle([C1, y + 5, C1 + 4, y + 19], fill=color)
    draw.text((C1 + 12, y), ticker, font=bold(16), fill=color)
    draw.text((C1 + 12, y + 20), desc, font=font(14), fill=GRAY)
    if ticker == "[AXT]" or ticker == "[IQE]":
        draw.text((C1 + 18, y + 42), "↓", font=bold(16), fill=DARK_GRAY)
    y += 58

draw.line([(C1, y), (400, y)], fill=DARK_GRAY, width=1)
y += 12
draw.text((C1, y), "제품별 고객", font=bold(18), fill=CYAN)
y += 26

products = [
    (CYAN,   "InP 에피웨이퍼",   "MACOM·Lumentum → 데이터센터 광통신"),
    (AMBER,  "GaN 에피웨이퍼",   "MACOM → 방산 레이더·위성 RF"),
    (GREEN,  "GaAs 에피웨이퍼",  "Qorvo·Skyworks → 스마트폰 5G RF"),
    (PURPLE, "VCSEL 에피웨이퍼", "Apple 공급망 → Face ID·ToF"),
]
for color, product, desc in products:
    draw.rectangle([C1, y + 5, C1 + 4, y + 19], fill=color)
    draw.text((C1 + 12, y), product, font=bold(15), fill=WHITE)
    draw.text((C1 + 12, y + 20), desc, font=font(13), fill=GRAY)
    y += 44

# 컬럼 구분선
draw.line([(416, 86), (416, H - 46)], fill=DARK_GRAY, width=1)

# ── 컬럼 2: 핵심 thesis ──
C2 = 434
draw.text((C2, 96), "핵심 thesis", font=bold(18), fill=AMBER)
draw.line([(C2, 120), (826, 120)], fill=DARK_GRAY, width=1)

thesis = [
    (AMBER,  "MACOM 캡티브 구조",
             "£4,500만 투자 + 독점 공급 계약 + 이사회 입성",
             "단순 투자 아님 — 수직통합 선행 작업"),
    (GREEN,  "미국 방산 이미 탑승",
             "미국 공장 3곳 운영, 2025 H2 미 군 프로그램 실적 반등",
             "Five Eyes 동맹 → ITAR 가장 유연한 파트너"),
    (CYAN,   "SIVE와 실제 공급망 연결",
             "IQE InP 웨이퍼 → SIVE 레이저 소자 제조",
             "포트폴리오 내 공급자-고객 관계 실존"),
    (PURPLE, "EU 칩스액트 1.0 직접 수혜 가능",
             "GaN 팹 증설 보조금 신청 검토 중",
             "2.0(수요 창출)은 IQE엔 간접 수혜에 그침"),
]
y = 128
for color, title, line1, line2 in thesis:
    draw.rounded_rectangle([C2, y, 822, y + 82], radius=5, fill=(20, 22, 30))
    draw.rectangle([C2, y, C2 + 4, y + 82], fill=color)
    draw.text((C2 + 14, y + 8), title, font=bold(16), fill=WHITE)
    draw.text((C2 + 14, y + 32), line1, font=font(13), fill=GRAY)
    draw.text((C2 + 14, y + 52), line2, font=font(13), fill=GRAY)
    y += 92

# 컬럼 구분선
draw.line([(838, 86), (838, H - 46)], fill=DARK_GRAY, width=1)

# ── 컬럼 3: 리스크 + 체크포인트 ──
C3 = 856
draw.text((C3, 96), "리스크", font=bold(18), fill=RED)
draw.line([(C3, 120), (W - 32, 120)], fill=DARK_GRAY, width=1)

risks = [
    "MACOM 의존도 심화 — 단일 고객 리스크",
    "무선(스마트폰) 부문 침체 지속",
    "6/1 신규 3.3억 주 발행 희석",
    "헐값 인수 가능성",
]
y = 128
for r in risks:
    draw.rectangle([C3, y + 5, C3 + 4, y + 19], fill=RED)
    draw.text((C3 + 12, y), r, font=font(14), fill=GRAY)
    y += 30

draw.line([(C3, y + 6), (W - 32, y + 6)], fill=DARK_GRAY, width=1)
y += 18
draw.text((C3, y), "인수 시나리오", font=bold(17), fill=AMBER)
y += 26

acq = [
    (AMBER, "2025.09  전체 매각 협상 공식화"),
    (AMBER, "2026.04  MACOM 이사회 입성"),
    (GREEN, "성공 시 현재가 +20~40% 프리미엄"),
    (RED,   "상장 폐지 → 텐배거 종료"),
]
for color, text in acq:
    draw.rectangle([C3, y + 5, C3 + 4, y + 19], fill=color)
    draw.text((C3 + 12, y), text, font=font(14), fill=GRAY)
    y += 26

draw.line([(C3, y + 6), (W - 32, y + 6)], fill=DARK_GRAY, width=1)
y += 18
draw.text((C3, y), "체크포인트", font=bold(17), fill=CYAN)
y += 26

checks = [
    (CYAN,  "인수가 확정 공시"),
    (GREEN, "방산·AI 포토닉스 매출 비중 상승"),
    (GREEN, "SIVE 나스닥 이중상장 완료"),
    (AMBER, "EU 칩스액트 1.0 보조금 확정"),
]
for color, text in checks:
    draw.rectangle([C3, y + 5, C3 + 4, y + 19], fill=color)
    draw.text((C3 + 12, y), text, font=font(14), fill=GRAY)
    y += 26

# 하단 배너
draw.rounded_rectangle([32, H - 76, W - 32, H - 46], radius=6, fill=(4, 22, 30))
draw.text((48, H - 66), "텐배거를 원한다면 독립 상장 유지가 답  —  인수는 단기 프리미엄, 성장은 독립이 전제", font=bold(16), fill=CYAN)

footer(draw, "IQE Corporate IR · LSE Announcements")
img.save(os.path.join(OUT_DIR, "2026-06-04_IQE_정리.png"))
print("Saved: IQE 정리 카드")
