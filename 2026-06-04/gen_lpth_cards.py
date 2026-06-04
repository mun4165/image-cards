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
    draw.rectangle([0, 0, W, 4], fill=AMBER)
    draw.rectangle([0, 0, 4, H], fill=AMBER)
    return img, draw

def footer(draw, source):
    draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
    draw.text((32, H - 30), f"2026.06.04  |  {source}  |  개인 공부 기록", font=font(15), fill=GRAY)


# ────────────────────────────────────────────────
# 카드 1: 전체 thesis 요약 (표지)
# ────────────────────────────────────────────────
img, draw = base_canvas()

draw.text((32, 14), "$LPTH", font=bold(40), fill=AMBER)
draw.text((168, 20), "부품사 탈피를 선언한 방산 광학 기업", font=bold(28), fill=WHITE)
draw.text((168, 58), "LightPath Technologies  |  자본 조달 이후 달라진 것들", font=font(18), fill=GRAY)
draw.line([(32, 92), (W - 32, 92)], fill=DARK_GRAY, width=1)

# 왼쪽: 핵심 thesis
draw.text((32, 104), "이번 딜에서 읽어야 할 것", font=bold(19), fill=GRAY)
draw.line([(32, 130), (610, 130)], fill=DARK_GRAY, width=1)

thesis = [
    (AMBER,  "M&A 공식화",
             "공시에 인수 목적 명시 — 운영자금 조달 아님",
             "EO/IR 시스템 통합 방향으로 실탄 확보"),
    (GREEN,  "Ryan Workman 영입",
             "Silent Sentinel: $500K → $2,700만 매출 성장",
             "DHS 국경감시 계약 수주 이력의 방산 영업 전문가"),
    (CYAN,   "수급 구조 변화",
             "North Run 보통주 재고 이번 딜로 사실상 소진",
             "상단 누르던 산발적 매도 패턴 구조적 해소 가능성"),
]
y = 140
for color, title, line1, line2 in thesis:
    draw.rectangle([28, y + 4, 32, y + 28], fill=color)
    draw.text((44, y), title, font=bold(20), fill=WHITE)
    draw.text((44, y + 28), line1, font=font(15), fill=GRAY)
    draw.text((44, y + 50), line2, font=font(15), fill=GRAY)
    y += 84

# 오른쪽: 리스크 + 체크포인트
draw.line([(628, 92), (628, H - 46)], fill=DARK_GRAY, width=1)
COL2 = 648

draw.text((COL2, 104), "리스크", font=bold(19), fill=RED)
draw.line([(COL2, 130), (W - 32, 130)], fill=DARK_GRAY, width=1)

risks = [
    "잔여 전환우선주 약 669만 주 오버행 미해소",
    "North Run 10% 이하 → 공시 의무 감소, 추적 어려워짐",
    "$50M으로 의미 있는 시스템 기업 인수 가능 여부",
    "파이프라인 → 매출 전환 타임라인 불확실",
    "수급 수치는 SEC 원문 확인 전까지 추정",
]
y = 140
for r in risks:
    draw.rectangle([COL2, y + 6, COL2 + 4, y + 20], fill=RED)
    draw.text((COL2 + 12, y), r, font=font(16), fill=GRAY)
    y += 34

draw.line([(COL2, y + 8), (W - 32, y + 8)], fill=DARK_GRAY, width=1)
draw.text((COL2, y + 18), "체크포인트", font=bold(19), fill=AMBER)
y += 46

checks = [
    (AMBER, "424B4 최종 프로스펙터스",  "잔여 물량 락업 조항 확인"),
    (GREEN, "NGSRI / C-UAS 파이프라인", "실제 수주 전환 신호 포착"),
]
for color, title, desc in checks:
    draw.rectangle([COL2, y + 4, COL2 + 4, y + 24], fill=color)
    draw.text((COL2 + 12, y), title, font=bold(17), fill=WHITE)
    draw.text((COL2 + 12, y + 24), desc, font=font(15), fill=GRAY)
    y += 56

draw.rounded_rectangle([32, H - 78, W - 32, H - 46], radius=6, fill=(30, 22, 4))
draw.text((48, H - 68), "방향은 맞다  —  수급 원문 확인 + 파이프라인 전환 신호가 리레이팅의 시작", font=bold(17), fill=AMBER)

footer(draw, "LightPath Technologies IR · SEC EDGAR")
img.save(os.path.join(OUT_DIR, "2026-06-04_LPTH_00_표지.png"))
print("Saved: 표지")


# ────────────────────────────────────────────────
# 카드 2: M&A 전략 + Ryan Workman
# ────────────────────────────────────────────────
img, draw = base_canvas()

draw.text((32, 14), "$LPTH", font=bold(40), fill=AMBER)
draw.text((168, 20), "M&A 실탄 확보  —  어디로 향하는가", font=bold(28), fill=WHITE)
draw.text((168, 58), "공시에 명시된 인수 목적  +  Ryan Workman 영입 시그널", font=font(18), fill=GRAY)
draw.line([(32, 92), (W - 32, 92)], fill=DARK_GRAY, width=1)

# 왼쪽: M&A 타깃 섹터
draw.text((32, 104), "추론되는 M&A 타깃 섹터", font=bold(19), fill=GRAY)
draw.line([(32, 130), (590, 130)], fill=DARK_GRAY, width=1)

sectors = [
    (AMBER,  "1순위  EO/IR 시스템 통합",
             "안티드론 · 국경감시 · 장거리 추적 시스템",
             "QuickSet · OpenWorks 류 팬틸트 기반 기업"),
    (CYAN,   "2순위  IR 코팅 · 필터 전문",
             "MWIR/LWIR 코팅 · 밴드패스 · DLC 기술 보유",
             "Andover · Reynard 류  —  BlackDiamond 수직통합 시너지"),
    (PURPLE, "3순위  초소형 열화상 모듈",
             "FPV 드론용 열화상 · 군용 조준경 기술 라인",
             "소규모 흡수로 제품군 확장"),
]
y = 140
for color, title, line1, line2 in sectors:
    draw.rounded_rectangle([32, y, 596, y + 86], radius=6, fill=(20, 22, 30))
    draw.rectangle([32, y, 36, y + 86], fill=color)
    draw.text((50, y + 8), title, font=bold(18), fill=WHITE)
    draw.text((50, y + 34), line1, font=font(15), fill=GRAY)
    draw.text((50, y + 56), line2, font=font(14), fill=GRAY)
    y += 98

# 오른쪽: Ryan Workman
draw.line([(618, 92), (618, H - 46)], fill=DARK_GRAY, width=1)
COL2 = 638

draw.text((COL2, 104), "Ryan Workman 영입이 말하는 것", font=bold(19), fill=GRAY)
draw.line([(COL2, 130), (W - 32, 130)], fill=DARK_GRAY, width=1)

draw.text((COL2, 144), "Silent Sentinel 재직 실적", font=bold(17), fill=AMBER)

metrics = [
    ("매출 성장", "$500K  →  $2,700만", GREEN),
    ("핵심 계약", "DHS CBP 국경감시(RVSSU)", CYAN),
    ("전문 영역", "안티드론  ·  EO/IR 감시", AMBER),
]
y = 172
for label, val, color in metrics:
    draw.text((COL2, y), label, font=font(14), fill=GRAY)
    draw.text((COL2, y + 18), val, font=bold(20), fill=color)
    y += 56

draw.line([(COL2, y), (W - 32, y)], fill=DARK_GRAY, width=1)
y += 14

draw.text((COL2, y), "CEO Sam Rubin의 코멘트", font=bold(17), fill=GRAY)
y += 28
quote_lines = [
    '"백로그를 실제 매출로 전환하고',
    ' 신규 고객을 확보하는 데',
    ' 핵심적인 역할을 할 것"',
]
for line in quote_lines:
    draw.text((COL2, y), line, font=font(16), fill=WHITE)
    y += 26

y += 12
draw.line([(COL2, y), (W - 32, y)], fill=DARK_GRAY, width=1)
y += 14
draw.text((COL2, y), "단순 세일즈 영입이 아니다.", font=bold(17), fill=AMBER)
y += 28
draw.text((COL2, y), "렌즈 부품사가 국경감시·안티드론", font=font(16), fill=GRAY)
y += 24
draw.text((COL2, y), "영업 전문가를 데려올 이유가 없다.", font=font(16), fill=GRAY)
y += 24
draw.text((COL2, y), "방향을 사람으로 보여준 것이다.", font=bold(16), fill=WHITE)

footer(draw, "LightPath Technologies IR · Silent Sentinel 공개 자료")
img.save(os.path.join(OUT_DIR, "2026-06-04_LPTH_01_MA전략.png"))
print("Saved: M&A 전략")


# ────────────────────────────────────────────────
# 카드 3: North Run 수급 구조 변화
# ────────────────────────────────────────────────
img, draw = base_canvas()

draw.text((32, 14), "$LPTH", font=bold(40), fill=AMBER)
draw.text((168, 20), "North Run 오버행  —  구조가 바뀌고 있다", font=bold(26), fill=WHITE)
draw.text((168, 58), "단순 희석이 아닌 수급 패턴의 변화  |  단, SEC 원문 확인 필수", font=font(18), fill=GRAY)
draw.line([(32, 92), (W - 32, 92)], fill=DARK_GRAY, width=1)

# 왼쪽: 수급 흐름
draw.text((32, 104), "블록딜 수급 구조 (추정 — 원문 확인 필요)", font=bold(17), fill=GRAY)
draw.line([(32, 130), (590, 130)], fill=DARK_GRAY, width=1)

flow = [
    (GRAY,   "North Run 보통주 잔고",   "약 293만 주"),
    (AMBER,  "이번 블록딜 매각 수량",   "357만 주"),
    (RED,    "갭 (부족분)",             "약 64만 주  →  우선주 강제 전환"),
    (GREEN,  "딜 완료 후 보통주 재고",   "사실상 소진"),
    (CYAN,   "잔여 전환우선주 오버행",  "약 669만 주  (주의 영역)"),
]
y = 140
for color, label, val in flow:
    draw.rectangle([32, y + 4, 36, y + 26], fill=color)
    draw.text((48, y), label, font=font(16), fill=GRAY)
    draw.text((48, y + 22), val, font=bold(20), fill=color)
    y += 60

# 중앙 구분선
draw.line([(610, 92), (610, H - 46)], fill=DARK_GRAY, width=1)
COL2 = 630

# 오른쪽: Before/After
draw.text((COL2, 104), "수급 패턴 변화", font=bold(19), fill=GRAY)
draw.line([(COL2, 130), (W - 32, 130)], fill=DARK_GRAY, width=1)

draw.rounded_rectangle([COL2, 140, W - 32, 258], radius=6, fill=(35, 15, 15))
draw.text((COL2 + 16, 150), "Before  —  North Run", font=bold(17), fill=RED)
before_lines = [
    "낮은 원가 보유 대주주",
    "주가 오를 때마다 조금씩 매도",
    "구조적 천장 형성  →  주가 상단 지속 압박",
]
y2 = 178
for line in before_lines:
    draw.text((COL2 + 16, y2), "•  " + line, font=font(15), fill=GRAY)
    y2 += 24

draw.rounded_rectangle([COL2, 268, W - 32, 400], radius=6, fill=(10, 30, 20))
draw.text((COL2 + 16, 278), "After  —  신규 기관", font=bold(17), fill=GREEN)
after_lines = [
    "14달러 수준에서 포지션 구축",
    "단기 이익실현 동기 상대적으로 약함",
    "물량 소화 후 홀드 경향",
    "산발적 천장 패턴과 다른 구조",
]
y2 = 306
for line in after_lines:
    draw.text((COL2 + 16, y2), "•  " + line, font=font(15), fill=GRAY)
    y2 += 24

draw.rounded_rectangle([COL2, 412, W - 32, 490], radius=6, fill=(25, 20, 5))
draw.text((COL2 + 16, 422), "주의", font=bold(17), fill=AMBER)
warn_lines = [
    "669만주 잔여 우선주 — North Run 향후 행보 불확실",
    "10% 이하 주주 전환 시 공시 의무 감소",
]
y2 = 448
for line in warn_lines:
    draw.text((COL2 + 16, y2), "•  " + line, font=font(14), fill=GRAY)
    y2 += 22

draw.rounded_rectangle([32, H - 78, W - 32, H - 46], radius=6, fill=(30, 22, 4))
draw.text((48, H - 68), "수치 기반 확신은 424B4 · SC 13D 원문 확인 후에  —  방향성은 구조적 개선", font=bold(16), fill=AMBER)

footer(draw, "SEC EDGAR 424B4 · SC 13D 기준 (원문 확인 필요)")
img.save(os.path.join(OUT_DIR, "2026-06-04_LPTH_02_수급구조.png"))
print("Saved: 수급구조")

print("\n전체 완료.")


# ────────────────────────────────────────────────
# 카드 통합: 1장 압축 요약
# ────────────────────────────────────────────────
img, draw = base_canvas()

# 헤더
draw.text((32, 14), "$LPTH", font=bold(40), fill=AMBER)
draw.text((168, 18), "희석 악재가 아니다  —  부품사에서 방산 시스템으로", font=bold(26), fill=WHITE)
draw.text((168, 56), "자본 조달 이후 달라진 3가지  |  LightPath Technologies", font=font(16), fill=GRAY)
draw.line([(32, 86), (W - 32, 86)], fill=DARK_GRAY, width=1)

# ── 컬럼 1: M&A + Workman ──
C1 = 32
draw.text((C1, 96), "① M&A 공식화", font=bold(18), fill=AMBER)
draw.line([(C1, 120), (400, 120)], fill=DARK_GRAY, width=1)

ma = [
    (AMBER, "공시에 인수 목적 명시"),
    (CYAN,  "1순위  EO/IR 시스템 통합 (안티드론·국경감시)"),
    (CYAN,  "2순위  IR 코팅·필터 전문 (수직통합 시너지)"),
    (PURPLE,"3순위  초소형 열화상 모듈 흡수"),
]
y = 128
for color, text in ma:
    draw.rectangle([C1, y + 5, C1 + 4, y + 19], fill=color)
    draw.text((C1 + 12, y), text, font=font(15), fill=GRAY)
    y += 28

y += 8
draw.text((C1, y), "② Ryan Workman 영입", font=bold(18), fill=GREEN)
draw.line([(C1, y + 24), (400, y + 24)], fill=DARK_GRAY, width=1)
y += 32

workman = [
    (GREEN, "Silent Sentinel  $500K → $2,700만 매출"),
    (GREEN, "DHS CBP 국경감시 계약 직접 수주"),
    (AMBER, "렌즈 부품사가 이 경력의 영업 책임자를"),
    (AMBER, "데려올 이유 없다  →  방향을 사람으로 선언"),
]
for color, text in workman:
    draw.rectangle([C1, y + 5, C1 + 4, y + 19], fill=color)
    draw.text((C1 + 12, y), text, font=font(15), fill=GRAY)
    y += 26

# 컬럼 구분선
draw.line([(416, 86), (416, H - 46)], fill=DARK_GRAY, width=1)

# ── 컬럼 2: North Run 수급 ──
C2 = 434
draw.text((C2, 96), "③ 수급 구조 변화", font=bold(18), fill=CYAN)
draw.line([(C2, 120), (810, 120)], fill=DARK_GRAY, width=1)

flow = [
    (GRAY,   "North Run 보통주 잔고",  "약 293만 주"),
    (AMBER,  "블록딜 매각 수량",       "357만 주"),
    (RED,    "갭 → 우선주 강제 전환",  "약 64만 주"),
    (GREEN,  "딜 후 보통주 재고",      "사실상 소진"),
    (RED,    "잔여 우선주 오버행",     "약 669만 주 (주의)"),
]
y = 128
for color, label, val in flow:
    draw.rectangle([C2, y + 5, C2 + 4, y + 19], fill=color)
    draw.text((C2 + 12, y), label, font=font(14), fill=GRAY)
    draw.text((C2 + 12, y + 18), val, font=bold(17), fill=color)
    y += 48

draw.line([(C2, y + 4), (810, y + 4)], fill=DARK_GRAY, width=1)
y += 14
draw.text((C2, y), "Before  →  After", font=bold(16), fill=WHITE)
y += 24

before_after = [
    (RED,   "North Run: 낮은 원가, 오를 때마다 매도"),
    (GREEN, "신규 기관: 14달러 매입, 홀드 경향"),
    (GRAY,  "산발적 천장 패턴  →  구조적 해소 가능"),
    (AMBER, "단, 수치는 SEC 원문 확인 필수"),
]
for color, text in before_after:
    draw.rectangle([C2, y + 5, C2 + 4, y + 19], fill=color)
    draw.text((C2 + 12, y), text, font=font(14), fill=GRAY)
    y += 26

# 컬럼 구분선
draw.line([(826, 86), (826, H - 46)], fill=DARK_GRAY, width=1)

# ── 컬럼 3: 리스크 + 체크포인트 ──
C3 = 844
draw.text((C3, 96), "리스크", font=bold(18), fill=RED)
draw.line([(C3, 120), (W - 32, 120)], fill=DARK_GRAY, width=1)

risks = [
    "잔여 우선주 669만 주 오버행",
    "North Run 10% 이하 → 공시 추적 어려움",
    "$50M으로 의미 있는 기업 인수 빠듯",
    "파이프라인 → 매출 전환 타임라인 불확실",
    "수급 수치 — SEC 원문 확인 전까지 추정",
]
y = 128
for r in risks:
    draw.rectangle([C3, y + 5, C3 + 4, y + 19], fill=RED)
    draw.text((C3 + 12, y), r, font=font(14), fill=GRAY)
    y += 28

draw.line([(C3, y + 6), (W - 32, y + 6)], fill=DARK_GRAY, width=1)
y += 18
draw.text((C3, y), "체크포인트", font=bold(18), fill=AMBER)
y += 26

checks = [
    (AMBER, "424B4 락업 조항 확인"),
    (AMBER, "SC 13D 잔여 물량 확인"),
    (GREEN, "NGSRI / C-UAS 수주 전환 신호"),
    (GREEN, "LRIP 단계 진입 공시"),
]
for color, text in checks:
    draw.rectangle([C3, y + 5, C3 + 4, y + 19], fill=color)
    draw.text((C3 + 12, y), text, font=font(14), fill=GRAY)
    y += 26

# 하단 배너
draw.rounded_rectangle([32, H - 76, W - 32, H - 46], radius=6, fill=(30, 22, 4))
draw.text((48, H - 66), "방향은 맞다  —  수급 원문 확인 + 파이프라인 수주 신호가 리레이팅의 시작  |  개인 공부 기록", font=bold(16), fill=AMBER)

footer(draw, "LightPath Technologies IR · SEC EDGAR")
img.save(os.path.join(OUT_DIR, "2026-06-04_LPTH_통합.png"))
print("Saved: 통합 1장")
