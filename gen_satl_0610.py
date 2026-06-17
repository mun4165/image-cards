from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-10"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (12, 10, 14)
GRID      = (255, 255, 255, 10)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (55, 58, 70)
RED       = (239, 68, 68)
AMBER     = (245, 158, 11)
BLUE      = (59, 130, 246)
PURPLE    = (167, 139, 250)
GREEN     = (52, 211, 153)
CYAN      = (6, 182, 212)
ACCENT    = RED

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):          return ImageFont.truetype(FONT_PATH, size, index=4)

def make_base():
    img  = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    draw.rectangle([0, 0, W, 4], fill=ACCENT)
    draw.rectangle([0, 0, 4, H], fill=ACCENT)
    return img, ImageDraw.Draw(img)

def footer(draw, left, right):
    draw.line([(60, H-50), (W-60, H-50)], fill=DARK_GRAY, width=1)
    draw.text((60,      H-34), left,  font=font(17), fill=GRAY)
    draw.text((W-500,   H-34), right, font=bold(17), fill=ACCENT)

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.text((60, 20), "SATL  Satellogic — 하락을 4개 레이어로 뜯어봤다", font=bold(36), fill=WHITE)
    draw.text((60, 70), "Q1 매출 +80%인데 주가 -12%  ·  호재에 팔린 국방계약  ·  SpaceX IPO 압박", font=font(19), fill=RED)
    draw.line([(60, 106), (W-60, 106)], fill=DARK_GRAY, width=1)

    CTOP = 118
    CBOT = H - 60
    DIV  = 610

    # ── 왼쪽: 4개 레이어 ──
    layers = [
        (AMBER,  "Layer 1  —  비현금 손실 헤드라인",
                 "순손실 -$118.3M  중  -$113M 은 공정가치 평가손 (비현금)",
                 "주가 상승 -> 워런트 부채 증가 -> 손익에 손실  /  현금 유출 아님"),
        (RED,    "Layer 2  —  임원 이탈 연속",
                 "프레지던트 Tirman 3월 사임  +  CFO Dunn 6.08 사임 공시",
                 "7년 재직 CFO 퇴장  ·  내부 불안 내러티브 차단 불가"),
        (PURPLE, "Layer 3  —  호재가 호재로 안 읽힌 날",
                 "$18M+ 국방계약  ·  육군 중장 이사회 합류  ->  당일 -17.4%",
                 "해석: 국방 피봇 = 민간 이미징 수익화 한계 시인"),
        (BLUE,   "Layer 4  —  섹터 전반 SpaceX IPO 압박",
                 "6.11 가격설정  $1.75T  ·  ASTS·RKLB·LUNR 동반 -8~14%",
                 "자금 소형 우주주 -> SpaceX 이동  ·  SATL 방어막 없음"),
    ]

    item_h = (CBOT - CTOP - 4) // 4
    y = CTOP
    for color, title, line1, line2 in layers:
        draw.rounded_rectangle([60, y+4, DIV-20, y+item_h-4], radius=7, fill=(20, 18, 26))
        draw.rectangle([60, y+4, 66, y+item_h-4], fill=color)
        draw.text((82, y+12),  title, font=bold(17), fill=color)
        draw.text((82, y+40),  line1, font=font(14), fill=WHITE)
        draw.text((82, y+62),  line2, font=font(13), fill=GRAY)
        y += item_h

    # ── 세로 구분선 ──
    draw.line([(DIV, 106), (DIV, CBOT)], fill=DARK_GRAY, width=1)

    # ── 오른쪽 ──
    RX = DIV + 22

    # 핵심 지표 박스
    draw.text((RX, CTOP), "핵심 수치", font=bold(18), fill=GRAY)
    stats = [
        (AMBER, "Q1 매출",       "+80% YoY  $6.1M"),
        (GREEN, "영업현금흐름",   "최초 흑자 전환"),
        (RED,   "순손실",         "-$118.3M  (비현금 -$113M)"),
        (RED,   "5.12 주가",      "프리마켓 -11.84%"),
        (RED,   "5.26 주가",      "국방계약 당일 -17.4%"),
        (BLUE,  "52주 범위",      "$1.26 ~ $12.00"),
    ]
    sy = CTOP + 30
    for color, label, val in stats:
        draw.rounded_rectangle([RX, sy, W-60, sy+36], radius=6, fill=(18, 16, 24))
        draw.text((RX+14, sy+8),   label, font=bold(14),  fill=GRAY)
        draw.text((RX+160, sy+8),  val,   font=bold(15),  fill=color)
        sy += 42

    # 구분선
    draw.line([(RX, sy+4), (W-60, sy+4)], fill=DARK_GRAY, width=1)

    # 판단 박스
    jy = sy + 14
    jb = CBOT - 4
    draw.rounded_rectangle([RX, jy, W-60, jb], radius=8, fill=(24, 14, 14))
    draw.rounded_rectangle([RX, jy, W-60, jb], radius=8, outline=RED, width=1)
    draw.text((RX+16, jy+10),  "다음 확인 포인트",              font=bold(16), fill=RED)
    draw.text((RX+16, jy+40),  "CFO 후임 발표 시점",            font=font(14), fill=WHITE)
    draw.text((RX+16, jy+62),  "Q2 실적  —  8월 예정",          font=font(14), fill=WHITE)
    draw.text((RX+16, jy+84),  "국방 계약 추가 수주 여부",       font=font(14), fill=WHITE)
    draw.text((RX+16, jy+106), "SpaceX IPO 후 섹터 수급 정상화", font=font(14), fill=GRAY)

    footer(draw, "2026.06.10", "SATL  ·  SEC 8-K  ·  Q1 2026 Earnings")

    out = os.path.join(OUT_DIR, "2026-06-10_SATL_하락해부.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
