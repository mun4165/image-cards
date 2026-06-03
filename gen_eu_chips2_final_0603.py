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

# 강조선
draw.rectangle([0, 0, W, 4], fill=BLUE)
draw.rectangle([0, 0, 4, H], fill=BLUE)

# ── 헤더 ──
draw.text((32, 18), "EU CHIPS Act 2.0 — 2026.06.03 공식 발표", font=bold(36), fill=BLUE)
draw.text((32, 66), "공급 유치 → 수요 창출  /  포토닉스, 전략 인프라로 공식 지정", font=bold(22), fill=WHITE)
draw.text((32, 100), "목표: 기술적 불가결성 — 전 세계 공급망이 유럽 기술 없이 기능할 수 없는 구조", font=font(17), fill=GRAY)
draw.line([(32, 132), (W - 32, 132)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 수혜 기대 유럽 상장사 ──
draw.text((32, 144), "수혜 기대 유럽 상장사", font=bold(21), fill=WHITE)
draw.line([(32, 172), (590, 172)], fill=DARK_GRAY, width=1)

companies = [
    (AMBER,  "Soitec  (프랑스 / Euronext)",              "SOI 웨이퍼  —  SiPH 칩 기반 소재  /  52주 저점 대비 +600%+"),
    (GREEN,  "IQE  (영국 / 런던 AIM)",                   "화합물 반도체 웨이퍼  —  레이저 원재료  /  YTD +900%+"),
    (CYAN,   "Aixtron  (독일 / 프랑크푸르트)",            "광부품 제조 장비  /  YTD +195%"),
    (BLUE,   "STMicroelectronics  (FR·IT / NYSE)",       "SiPH 기술·CPO  —  유럽 최대 반도체"),
    (TEAL,   "X-FAB  (독일·벨기에 / Euronext)",          "SiPH 파운드리  —  photonixFAB 컨소시엄 주도"),
    (ORANGE, "Sivers Semiconductors  (스웨덴 / Nasdaq)", "AI DC용 CW 레이저  /  2027 대량생산 목표"),
    (GRAY,   "Nokia  (핀란드 / Nasdaq Helsinki)",        "photonixFAB 파트너  —  광트랜시버 응용  /  대형 복합기업"),
    (GRAY,   "Thales  (프랑스 / Euronext)",              "photonixFAB 파트너  —  방산·센서 응용  /  대형 복합기업"),
]
y = 182
for color, name, desc in companies:
    draw.rectangle([28, y + 4, 32, y + 24], fill=color)
    draw.text((44, y), name, font=bold(16), fill=WHITE)
    draw.text((44, y + 22), desc, font=font(14), fill=GRAY)
    y += 56

# 세로 구분선
draw.line([(620, 132), (620, H - 46)], fill=DARK_GRAY, width=1)

# ── 오른쪽 상단: CHIPS Act 2.0 핵심 변화 ──
draw.text((644, 144), "CHIPS Act 2.0 핵심 변화", font=bold(21), fill=WHITE)
draw.line([(644, 172), (W - 32, 172)], fill=DARK_GRAY, width=1)

changes = [
    (BLUE,  "전략 전환",   "공장 유치(공급)  →  수요 창출·공공 조달 우선"),
    (CYAN,  "목표 재설정", "20% 자급자족  →  기술적 불가결성"),
    (GREEN, "포토닉스 지정", "SiPH·CPO를 전략 인프라로 공식 분류"),
]
y = 182
for color, title, desc in changes:
    draw.rectangle([640, y + 4, 644, y + 26], fill=color)
    draw.text((656, y), title, font=bold(18), fill=WHITE)
    draw.text((656, y + 24), desc, font=font(16), fill=GRAY)
    y += 60

# ── 오른쪽 중단: 리스크 ──
draw.line([(644, y + 4), (W - 32, y + 4)], fill=DARK_GRAY, width=1)
draw.text((644, y + 14), "리스크", font=bold(20), fill=RED)
y += 44

risks = [
    "Lab-to-Fab 갭  —  연구는 강하나 대량생산 전환 역사적 약점",
    "집행 지연  —  실제 자금 도달까지 통상 2~3년 소요",
    "경쟁 가속  —  GF·Intel·TSMC 이미 SiPH 대규모 투자 중",
    "EU 감사원  —  '20% 목표 달성 가능성 매우 낮음' 공식 지적",
]
for line in risks:
    draw.text((644, y), "•  " + line, font=font(15), fill=GRAY)
    y += 26

# ── 오른쪽 하단: 요약 박스 ──
draw.rounded_rectangle([644, y + 10, W - 32, y + 52], radius=8, fill=(10, 18, 35))
draw.text((658, y + 20), "방향은 맞다  —  실적 반영은 2027~2028년 이후가 현실적", font=bold(17), fill=BLUE)

# ── 푸터 ──
draw.line([(32, H - 44), (W - 32, H - 44)], fill=DARK_GRAY, width=1)
draw.text((32, H - 30), "2026.06.03  |  Euronews · EE Times · photonixfab.eu · StockAnalysis", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-03_EU_CHIPS2_유럽포토닉스지도.png")
img.save(out)
print("Saved:", out)
