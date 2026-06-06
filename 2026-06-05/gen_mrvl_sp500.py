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
AMBER     = (245, 158, 11)
GREEN     = (52, 211, 153)
CYAN      = (6, 182, 212)
RED       = (239, 68, 68)
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

img, draw = base_canvas()

# ── 헤더 ──
draw.text((32, 14), "MRVL", font=bold(40), fill=AMBER)
draw.text((172, 18), "S&P 500 편입 확정 — 6월 22일 발효", font=bold(26), fill=WHITE)
draw.text((172, 56), "Marvell Technology  |  분기 리밸런싱  |  2026.06.05 발표", font=font(16), fill=GRAY)
draw.line([(32, 86), (W - 32, 86)], fill=DARK_GRAY, width=1)

# ── 왼쪽: 편입 핵심 팩트 ──
C1 = 32
draw.text((C1, 100), "편입 핵심 팩트", font=bold(18), fill=AMBER)
draw.line([(C1, 124), (590, 124)], fill=DARK_GRAY, width=1)

facts = [
    (AMBER, "발효일",       "2026년 6월 22일 장 시작 전"),
    (GRAY,  "대체 종목",    "PoolCorp (POOL) 퇴출"),
    (GREEN, "시가총액",     "$254B+  편입 전 S&P 500 미편입 최대 기업"),
    (GREEN, "주가 YTD",    "+200%+  6월 4일 종가 $301.65 역대 최고"),
    (CYAN,  "편입 조건",    "GAAP 흑자 — 최근 4분기 합산 첫 충족"),
    (AMBER, "젠슨 황 발언", "컴퓨텍스 타이베이 2026  트리거"),
]
y = 132
for color, label, val in facts:
    draw.rectangle([C1, y + 5, C1 + 4, y + 20], fill=color)
    draw.text((C1 + 12, y), label, font=font(14), fill=GRAY)
    draw.text((C1 + 12, y + 20), val, font=bold(17), fill=color)
    y += 56

# ── 왼쪽 하단: 인사이트 박스 ──
draw.rounded_rectangle([C1, y + 8, 590, y + 108], radius=6, fill=(28, 20, 4))
draw.text((C1 + 16, y + 18), "핵심 구도", font=bold(16), fill=AMBER)
draw.text((C1 + 16, y + 44), "AI 수혜  →  GAAP 흑자 전환  →  S&P 500 입성", font=font(15), fill=WHITE)
draw.text((C1 + 16, y + 68), "젠슨 황이 열어주고, 수익성이 잠금 해제했다", font=font(15), fill=GRAY)

# ── 중앙 구분선 ──
draw.line([(610, 86), (610, H - 46)], fill=DARK_GRAY, width=1)
C2 = 630

# ── 오른쪽 상단: 젠슨 황 발언 ──
draw.text((C2, 100), "왜 지금 터졌나", font=bold(18), fill=CYAN)
draw.line([(C2, 124), (W - 32, 124)], fill=DARK_GRAY, width=1)

draw.rounded_rectangle([C2, 132, W - 32, 232], radius=6, fill=(18, 22, 40))
draw.text((C2 + 16, 142), "젠슨 황  @  컴퓨텍스 타이베이 2026", font=bold(15), fill=CYAN)
draw.text((C2 + 16, 170), '"마벨은 조 달러짜리 기업 후보다"', font=font(17), fill=WHITE)
draw.text((C2 + 16, 198), "→ 당일 +25%  수일간 누적 +50%+", font=bold(15), fill=AMBER)

# ── 오른쪽 중단: GAAP 흑자 전환 배경 ──
draw.text((C2, 248), "왜 4년 동안 못 들어왔나", font=bold(18), fill=CYAN)
draw.line([(C2, 272), (W - 32, 272)], fill=DARK_GRAY, width=1)

draw.rounded_rectangle([C2, 280, W - 32, 358], radius=6, fill=(14, 24, 36))
draw.text((C2 + 16, 290), "S&P 500 편입 4대 조건 중 수익성이 걸림돌", font=font(15), fill=GRAY)
draw.text((C2 + 16, 314), "4분기 연속 GAAP 흑자  →  AI 수혜 전까지 미충족", font=bold(15), fill=CYAN)
draw.text((C2 + 16, 338), "12월 마감 분기 첫 GAAP 흑자  →  4분기 합산 통과", font=font(15), fill=GRAY)

# ── 오른쪽 중하단: 패시브 수급 ──
draw.text((C2, 372), "패시브 수급 유입", font=bold(18), fill=GREEN)
draw.line([(C2, 396), (W - 32, 396)], fill=DARK_GRAY, width=1)

passive = [
    (GREEN, "S&P 500 추종 ETF·펀드 의무 매수 발생"),
    (GREEN, "발표(6/5) ~ 발효(6/22) 집중 유입 구간"),
    (AMBER, "지수 비중 약 0.5%  →  추종 자산 ~$5T 기준 수십조 원"),
]
y2 = 404
for color, text in passive:
    draw.rectangle([C2, y2 + 5, C2 + 4, y2 + 19], fill=color)
    draw.text((C2 + 12, y2), text, font=font(16), fill=GRAY)
    y2 += 30

# ── 오른쪽 하단: 체크포인트 ──
draw.line([(C2, y2 + 6), (W - 32, y2 + 6)], fill=DARK_GRAY, width=1)
y2 += 18
draw.text((C2, y2), "편입 이후 체크포인트", font=bold(18), fill=PURPLE)
y2 += 26

checks = [
    (PURPLE, '"편입 확정 매수 → 발효일 매도" 패턴 주의'),
    (PURPLE, "다음 분기 GAAP 흑자 지속 여부 확인"),
    (AMBER,  "AI 수주 실적이 계속 받쳐주는지가 관건"),
]
for color, text in checks:
    draw.rectangle([C2, y2 + 5, C2 + 4, y2 + 19], fill=color)
    draw.text((C2 + 12, y2), text, font=font(16), fill=GRAY)
    y2 += 30

# ── 하단 배너 ──
draw.rounded_rectangle([32, H - 72, W - 32, H - 10], radius=6, fill=(28, 20, 4))
draw.text((52, H - 62), "S&P 500 편입 = 패시브 강제 매수  |  GAAP 흑자 전환이 4년 만에 열어준 문  |  발효일 6월 22일", font=bold(16), fill=AMBER)
draw.text((52, H - 34), "2026.06.05  |  S&P Dow Jones Indices · CNBC · MarketScreener", font=font(14), fill=GRAY)

out_path = os.path.join(OUT_DIR, "2026-06-05_MRVL_SP500편입.png")
img.save(out_path)
print(f"Saved: {out_path}")
