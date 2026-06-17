from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-15"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (8, 12, 22)
GRID      = (255, 255, 255, 8)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (45, 55, 72)
CYAN      = (6, 182, 212)
BLUE      = (59, 130, 246)
GREEN     = (52, 211, 153)
AMBER     = (245, 158, 11)
PURPLE    = (167, 139, 250)
ACCENT    = CYAN

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)
def make_base():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=GRID, width=1)
    draw.rectangle([0, 0, W, 4], fill=ACCENT)
    draw.rectangle([0, 0, 4, H], fill=ACCENT)
    return img, ImageDraw.Draw(img)
def footer(draw, left, right):
    draw.line([(60, H - 50), (W - 60, H - 50)], fill=DARK_GRAY, width=1)
    draw.text((60,      H - 34), left,  font=font(17), fill=GRAY)
    draw.text((W - 500, H - 34), right, font=bold(17), fill=ACCENT)

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.text((60, 18), "RKLB × Mynaric  —  우주 광통신, 실험에서 산업화로", font=bold(36), fill=WHITE)
    draw.text((60, 68), "SDA OISL 표준 인증 완료  ·  Rocket Lab 수직계열화 완성  ·  HASTE Curveball 궤도 검증", font=font(19), fill=CYAN)
    draw.line([(60, 104), (W - 60, 104)], fill=DARK_GRAY, width=1)

    CTOP = 118
    CBOT = H - 62
    DIV  = 570

    # ── 왼쪽: Mynaric / 광통신 ──
    draw.text((60, CTOP), "Mynaric 포지셔닝", font=bold(18), fill=GRAY)

    # 카드 1 — SDA
    draw.rounded_rectangle([60, CTOP + 28, DIV - 16, CTOP + 148], radius=8, fill=(10, 28, 38))
    draw.rectangle([60, CTOP + 28, 66, CTOP + 148], fill=CYAN)
    draw.text((80, CTOP + 36),  "CONDOR Mk3  —  SDA OISL 표준 인증", font=bold(17), fill=CYAN)
    draw.text((80, CTOP + 68),  "SDA 트란셰 2·3 위성에 이미 탑재 중", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 96),  "골든돔 5대 병목 1번 = OISL 단말", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 122), "HydRON·IRIS²보다 SDA가 먼저다", font=font(14), fill=GRAY)

    # 카드 2 — 수직계열화
    draw.rounded_rectangle([60, CTOP + 162, DIV - 16, CTOP + 282], radius=8, fill=(10, 22, 36))
    draw.rectangle([60, CTOP + 162, 66, CTOP + 282], fill=BLUE)
    draw.text((80, CTOP + 170), "Rocket Lab 수직계열화 완성", font=bold(17), fill=BLUE)
    draw.text((80, CTOP + 202), "Pioneer 버스  +  Mynaric OISL 터미널", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 228), "위성 제조 + 위성간 통신 = 동시 공급", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 254), "SDA 트란셰 3  18기  수주  —  양산 진입", font=font(14), fill=GRAY)

    # 카드 3 — 산업화 신호
    draw.rounded_rectangle([60, CTOP + 296, DIV - 16, CTOP + 396], radius=8, fill=(14, 24, 14))
    draw.rectangle([60, CTOP + 296, 66, CTOP + 396], fill=GREEN)
    draw.text((80, CTOP + 304), "산업화 단계 진입의 근거", font=bold(17), fill=GREEN)
    draw.text((80, CTOP + 336), "scalable  ·  interoperability  ·  industrialized", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 362), "수천 기 규모 네트워크 공급 표준이 목표", font=font(14), fill=GRAY)

    # ── 구분선 ──
    draw.line([(DIV, 104), (DIV, CBOT)], fill=DARK_GRAY, width=1)

    # ── 오른쪽 ──
    RX = DIV + 22

    draw.text((RX, CTOP), "이번 주 확인된 것들", font=bold(18), fill=GRAY)

    # 카드 1 — HASTE Curveball
    draw.rounded_rectangle([RX, CTOP + 28, W - 60, CTOP + 148], radius=8, fill=(24, 18, 10))
    draw.rectangle([RX, CTOP + 28, RX + 5, CTOP + 148], fill=AMBER)
    draw.text((RX + 18, CTOP + 36),  "HASTE Curveball  —  궤도 도달 확인", font=bold(17), fill=AMBER)
    draw.text((RX + 18, CTOP + 68),  "200km / 40° 경사각  상단 스테이지 궤도 삽입", font=font(15), fill=WHITE)
    draw.text((RX + 18, CTOP + 96),  "탑재체 임무 완료  →  통제 재진입 성공", font=font(15), fill=WHITE)
    draw.text((RX + 18, CTOP + 122), "Electron = 극초음속 테스트 플랫폼 반복 검증 완료", font=font(14), fill=GRAY)

    # 카드 2 — 유럽 파이프라인
    draw.rounded_rectangle([RX, CTOP + 162, W - 60, CTOP + 262], radius=8, fill=(20, 14, 36))
    draw.rectangle([RX, CTOP + 162, RX + 5, CTOP + 262], fill=PURPLE)
    draw.text((RX + 18, CTOP + 170), "유럽 파이프라인  —  SDA 다음 타자", font=bold(17), fill=PURPLE)
    draw.text((RX + 18, CTOP + 202), "ESA ScyLight / HydRON  —  유럽판 광통신 백본", font=font(15), fill=WHITE)
    draw.text((RX + 18, CTOP + 228), "IRIS²  —  EU 주권 위성망  ·  CONDOR 채택 가능", font=font(15), fill=WHITE)
    draw.text((RX + 18, CTOP + 252), "근거리 매출은 SDA  ·  유럽은 3~5년 뒤", font=font(13), fill=GRAY)

    # 핵심 인사이트 박스
    lbox_y = CTOP + 276
    lbox_b = CBOT - 4
    draw.rounded_rectangle([RX, lbox_y, W - 60, lbox_b], radius=8, fill=(14, 18, 32))
    draw.rounded_rectangle([RX, lbox_y, W - 60, lbox_b], radius=8, outline=CYAN, width=1)

    draw.text((RX + 18, lbox_y + 14),  "투자자 시사점", font=bold(17), fill=CYAN)
    draw.text((RX + 18, lbox_y + 48),  "Mynaric 인수 = 광통신 시장 진입이 아님", font=font(15), fill=WHITE)
    draw.text((RX + 18, lbox_y + 74),  "SDA 표준 공급업체 지위를 이미 갖춘 회사를 들여온 것", font=font(14), fill=GRAY)
    draw.text((RX + 18, lbox_y + 106), "수직계열화 완성이 조달 경쟁력 자체를 바꾼다", font=font(15), fill=WHITE)
    draw.text((RX + 18, lbox_y + 132), "두 뉴스가 같은 날 — 모멘텀이 여러 레이어에서 동시에", font=font(14), fill=GRAY)
    draw.text((RX + 18, lbox_y + 162), "CONDOR 공시 반영 시점이 다음 변곡점", font=font(15), fill=WHITE)
    draw.line([(RX + 18, lbox_y + 196), (W - 78, lbox_y + 196)], fill=DARK_GRAY, width=1)
    draw.text((RX + 18, lbox_y + 210), "개인 공부 기록  ·  투자 권유 아님", font=font(13), fill=DARK_GRAY)

    footer(draw, "2026.06.15", "$RKLB  ·  SDA  ·  Mynaric  ·  HASTE")

    out = os.path.join(OUT_DIR, "2026-06-15_RKLB_Mynaric_광통신.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
