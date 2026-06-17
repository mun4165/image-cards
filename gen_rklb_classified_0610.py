from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-10"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (10, 12, 20)
GRID      = (255, 255, 255, 10)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 60, 75)
PURPLE    = (167, 139, 250)
BLUE      = (59, 130, 246)
CYAN      = (6, 182, 212)
GREEN     = (52, 211, 153)
AMBER     = (245, 158, 11)
RED       = (239, 68, 68)
ACCENT    = PURPLE

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
    draw.text((W - 440, H - 34), right, font=bold(17), fill=ACCENT)

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.text((60, 20), "RKLB  Rocket Lab — 비공개 미션의 실체", font=bold(38), fill=WHITE)
    draw.text((60, 72), "발사 기록에 숨어있는 것들  ·  PSN 인도네시아 확인  ·  아직 열리지 않은 미션들", font=font(20), fill=PURPLE)
    draw.line([(60, 108), (W - 60, 108)], fill=DARK_GRAY, width=1)

    CTOP = 122
    CBOT = H - 62
    DIV  = 560

    # ── 왼쪽: 확인된 사실 ──
    draw.text((60, CTOP), "확인된 패턴", font=bold(19), fill=GRAY)

    draw.rounded_rectangle([60, CTOP + 28, DIV - 16, CTOP + 130], radius=8, fill=(20, 16, 38))
    draw.rectangle([60, CTOP + 28, 66, CTOP + 130], fill=PURPLE)
    draw.text((80, CTOP + 38),  "PSN 인도네시아  —  2년 만에 밝혀진 비공개", font=bold(17), fill=PURPLE)
    draw.text((80, CTOP + 70),  "IoT·D2D 위성 6기  ·  적도 LEO  ·  Electron 발사", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 96),  "우주 주권 프로젝트 → 비공개 요청 → 2년 후 자체 공개", font=font(14), fill=GRAY)

    draw.rounded_rectangle([60, CTOP + 142, DIV - 16, CTOP + 244], radius=8, fill=(16, 24, 36))
    draw.rectangle([60, CTOP + 142, 66, CTOP + 244], fill=BLUE)
    draw.text((80, CTOP + 152), "미 국가정찰국(NRO)  —  이미 확인된 분류 미션", font=bold(17), fill=BLUE)
    draw.text((80, CTOP + 184), "NROL-199  ·  NROL-162  공식 확인", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 210), "추가 정보기관 미션 비공개 기록 내 존재 가능성", font=font(14), fill=GRAY)

    draw.rounded_rectangle([60, CTOP + 256, DIV - 16, CTOP + 356], radius=8, fill=(16, 28, 20))
    draw.rectangle([60, CTOP + 256, 66, CTOP + 356], fill=GREEN)
    draw.text((80, CTOP + 266), "Neutron 첫 번째 고객  —  이름 없음", font=bold(17), fill=GREEN)
    draw.text((80, CTOP + 298), "2026년 예정  ·  중형 로켓  ·  대형 미션", font=font(15), fill=WHITE)
    draw.text((80, CTOP + 324), "고객 공개 시점이 다음 변곡점", font=font(14), fill=GRAY)

    # ── 세로 구분선 ──
    draw.line([(DIV, 108), (DIV, CBOT)], fill=DARK_GRAY, width=1)

    # ── 오른쪽: 미공개 미션 현황 + 핵심 논리 ──
    RX = DIV + 22

    draw.text((RX, CTOP), "아직 열리지 않은 미션들", font=bold(19), fill=GRAY)

    missions = [
        (AMBER, "2025.08", "위성 5기  ·  웹캐스트 10분 만에 종료",   "E-Space 추정  —  미확인"),
        (CYAN,  "2026.03", "단일 위성  ·  470km 궤도  ·  고객 비공개", "BlackSky 추정  —  미확인"),
    ]
    my = CTOP + 28
    for color, date, line1, line2 in missions:
        draw.rounded_rectangle([RX, my, W - 60, my + 86], radius=8, fill=(18, 20, 30))
        draw.rectangle([RX, my, RX + 5, my + 86], fill=color)
        draw.text((RX + 18, my + 8),  date,  font=bold(16), fill=color)
        draw.text((RX + 18, my + 34), line1, font=font(15), fill=WHITE)
        draw.text((RX + 18, my + 60), line2, font=font(14), fill=GRAY)
        my += 96

    # 핵심 논리 박스
    lbox_y = my + 8
    lbox_b = CBOT - 4
    draw.rounded_rectangle([RX, lbox_y, W - 60, lbox_b], radius=8, fill=(24, 18, 40))
    draw.rounded_rectangle([RX, lbox_y, W - 60, lbox_b], radius=8, outline=PURPLE, width=1)

    draw.text((RX + 18, lbox_y + 12), "투자자 관점 핵심", font=bold(17), fill=PURPLE)
    draw.text((RX + 18, lbox_y + 46), "공개 수주잔고  $11억  →  비공개 파이프라인 미포함", font=font(15), fill=WHITE)
    draw.text((RX + 18, lbox_y + 76), "우주 주권 프로젝트일수록 조용히 시작한다", font=font(15), fill=GRAY)
    draw.text((RX + 18, lbox_y + 106),"비공개 미션이 열릴 때마다 새로운 고객이 나온다", font=font(15), fill=GRAY)
    draw.text((RX + 18, lbox_y + 140),"PSN처럼 — 2년 후", font=bold(18), fill=PURPLE)

    footer(draw, "2026.06.10", "Rocket Lab  ·  Space Intel Report  ·  SpaceNews")

    out = os.path.join(OUT_DIR, "2026-06-10_RKLB_비공개미션.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
