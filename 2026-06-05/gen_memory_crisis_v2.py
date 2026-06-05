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
    draw.line([(60, H - 46), (W - 60, H - 46)], fill=DARK_GRAY, width=1)
    draw.text((60, H - 32), f"{date_str}  |  {source_str}", font=font(15), fill=GRAY)

def section(draw, x, y, title, color=AMBER):
    draw.text((x, y), title, font=bold(17), fill=color)
    return y + 24

def divider(draw, x, y, width):
    draw.line([(x, y), (x + width, y)], fill=DARK_GRAY, width=1)
    return y + 8

def row(draw, x, y, label, value, val_color=WHITE, label_w=210):
    draw.text((x, y),            label, font=font(15), fill=GRAY)
    draw.text((x + label_w, y),  value, font=bold(16), fill=val_color)
    return y + 26

def bullet(draw, x, y, text, color=GRAY):
    draw.text((x, y), f"·  {text}", font=font(15), fill=color)
    return y + 22


img, draw = make_base(AMBER)

# ── 헤더 ──
draw.text((60, 16), "AI 수요가 닌텐도를 건드렸다", font=bold(34), fill=WHITE)
draw.text((60, 58), "메모리 완판 · 가격 인상 · CXMT 추격 — 2026년 반도체 시장 변화 정리", font=font(17), fill=GRAY)
draw.line([(60, 88), (W - 60, 88)], fill=DARK_GRAY, width=1)

# ════════════════ 왼쪽 ════════════════
lx, lw = 60, 555
y = 98

# ① 수급 구조
y = section(draw, lx, y, "① 수급 구조")
y = row(draw, lx, y, "SK하이닉스 2026년",  "DRAM · NAND · HBM  전량 완판",  GREEN)
y = row(draw, lx, y, "HBM 향후 수요",      "3년치 수요 > 공급 능력  (공식 발언)",  AMBER)
y = row(draw, lx, y, "서버 DRAM 가격",     "+60~70% QoQ  (빅테크 우선 공급)",     RED)
y = row(draw, lx, y, "HBM 판가",           "$60~100  vs  일반 DDR5  $5~10",        AMBER)
y = divider(draw, lx, y + 2, lw)

# ② 닌텐도 파급
y = section(draw, lx, y, "② 소비자 파급 — 닌텐도 Switch 2")
draw.rectangle([lx, y, lx + 3, y + 68], fill=ORANGE)
y = row(draw, lx + 12, y, "미국 가격",   "$449 → $499  (+$50,  9월 1일~)",    ORANGE)
y = row(draw, lx + 12, y, "일본 가격",   "¥10,000 인상  (5월 25일~)",         ORANGE)
y = row(draw, lx + 12, y, "수익성 압박", "약 1,000억 엔($6.4억)  재무 전망 반영", GRAY)
y = row(draw, lx + 12, y, "공식 원인",   "메모리 가격 상승 · 관세 · 환율 복합",  GRAY)
y = divider(draw, lx, y + 2, lw)

# ③ 역설
y = section(draw, lx, y, "③ 역설 — VRAM 줄었는데 메모리 기업 호재?")
y = row(draw, lx, y, "엔비디아 RTX 5060", "16GB 대신 8GB 출시  (메모리 수급 부족)",  WHITE)
y = row(draw, lx, y, "GDDR7 재배분",      "소비자 GPU → HBM · 서버 DRAM으로",       CYAN)
draw.rounded_rectangle([lx, y + 2, lx + lw, y + 30], radius=6, fill=(25, 30, 20))
draw.text((lx + 10, y + 8), "소비자 GPU에 덜 쓸수록  →  더 비싼 AI용으로 더 많이 팔린다", font=bold(15), fill=GREEN)

# ════════════════ 세로 구분선 ════════════════
draw.line([(648, 88), (648, H - 50)], fill=DARK_GRAY, width=1)

# ════════════════ 오른쪽 ════════════════
rx, rw = 668, W - 60 - 668
y2 = 98

# ④ CXMT 소비자 시장 진입
y2 = section(draw, rx, y2, "④ CXMT — 공백 채우기 시작")
y2 = bullet(draw, rx, y2, "Corsair DDR5에 CXMT DRAM 탑재 제품 시장 등장", CYAN)
y2 = bullet(draw, rx, y2, "기가바이트 등 메인보드 업체 QVL 등록",            CYAN)
y2 = bullet(draw, rx, y2, "한국 출신 엔지니어 200명+ 재직  (Digitimes 2026.06.05)", GRAY)
y2 = divider(draw, rx, y2 + 2, rw)

# ⑤ 기술 격차
y2 = section(draw, rx, y2, "⑤ CXMT 기술 격차")
y2 = row(draw, rx, y2, "한-중 HBM 격차",  "3년  (서울경제 2026.06)",    GREEN, 200)
y2 = row(draw, rx, y2, "일부 분석 전망",  "2년 이하 가능성",             AMBER, 200)
y2 = row(draw, rx, y2, "채택 공법",       "MR-MUF  (SK하이닉스와 동일)", CYAN, 200)
y2 = row(draw, rx, y2, "인재 이동",       "특허·역설계 아닌 직접 이동",  GRAY, 200)
draw.rounded_rectangle([rx, y2 + 2, rx + rw, y2 + 30], radius=6, fill=(10, 25, 15))
draw.text((rx + 10, y2 + 8), "HBM4 세대 격차 재확대 가능성  —  방향성은 좁혀지는 쪽", font=font(14), fill=GRAY)
y2 += 38
y2 = divider(draw, rx, y2, rw)

# ⑥ 리스크
y2 = section(draw, rx, y2, "⑥ 리스크 — 빅테크 자본지출 부담")
y2 = row(draw, rx, y2, "빅테크 5사 AI 자본지출", "~$7,000억  (2026년 예상)",           RED, 230)
y2 = row(draw, rx, y2, "Google 채권 발행",       "$200억  (100년 만기 포함,  2026.02)", RED, 230)
y2 = row(draw, rx, y2, "UBS 추산 차입 규모",     "$2,300~2,400억  (하이퍼스케일러)",   ORANGE, 230)
y2 = bullet(draw, rx, y2, "AI 투자를 현금흐름 아닌 차입으로 충당 시작", ORANGE)
y2 = bullet(draw, rx, y2, "메모리 가격 상승 → AI 투자 비용 증가 → 사이클 속도 변수", GRAY)

footer(draw, "2026.06.05", "TrendForce · Digitimes · Nintendo IR · FT · CNBC · UBS")

out = os.path.join(OUT_DIR, "2026-06-05_메모리대란_v2.png")
img.save(out)
print("Saved:", out)
