from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-09"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (13, 17, 23)
GRID      = (255, 255, 255, 12)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (60, 70, 82)
AMBER     = (245, 158, 11)
BLUE      = (59, 130, 246)
CYAN      = (6, 182, 212)
GREEN     = (52, 211, 153)
PURPLE    = (167, 139, 250)
RED       = (239, 68, 68)

def font(size, index=0):
    return ImageFont.truetype(FONT_PATH, size, index=index)

def bold(size):
    return ImageFont.truetype(FONT_PATH, size, index=4)

def make_base(accent_color):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=GRID, width=1)
    draw.rectangle([0, 0, W, 4], fill=accent_color)
    return img, ImageDraw.Draw(img)

def footer(draw, date_str, source_str):
    draw.line([(60, H - 52), (W - 60, H - 52)], fill=DARK_GRAY, width=1)
    draw.text((60, H - 36), f"{date_str}  |  {source_str}",
              font=font(17), fill=GRAY)

def make_main():
    img, draw = make_base(AMBER)
    draw.rectangle([0, 0, 4, H], fill=AMBER)

    # 헤더
    draw.text((60, 44), "DRAM  Roundhill Memory ETF", font=bold(38), fill=AMBER)
    draw.text((60, 96), "세계 최초 메모리 반도체 ETF — 2026.04.02 상장  ·  AUM $138억", font=font(22), fill=GRAY)
    draw.line([(60, 134), (W - 60, 134)], fill=DARK_GRAY, width=1)

    # 좌측: ETF 현황
    lx = 60
    draw.text((lx, 150), "ETF 현황", font=bold(22), fill=GRAY)

    metrics = [
        ("주가 / NAV",  "$60.52  /  $65.59  (−8% 할인)",        RED),
        ("AUM",         "$138억  (상장 2개월)",                   AMBER),
        ("YTD 수익률",  "+150.7%  (SOXX +90%  /  SMH +68%)",     GREEN),
        ("운용보수",    "0.65%  (SOXX 0.34% 대비 2배)",           GRAY),
        ("집중도",      "15종목  /  삼성·하이닉스·마이크론 73%",  CYAN),
        ("Catalyst",    "마이크론 실적  6월 말  /  삼성 7월 초",  BLUE),
    ]
    y = 182
    for label, val, color in metrics:
        draw.text((lx,       y), label, font=font(18), fill=GRAY)
        draw.text((lx + 180, y), val,   font=bold(19), fill=color)
        y += 38

    # 구분선
    draw.line([(630, 134), (630, H - 60)], fill=DARK_GRAY, width=1)

    # 우측: 투자 포인트
    rx = 660
    draw.text((rx, 150), "왜 지금인가", font=bold(22), fill=GRAY)

    points = [
        (AMBER,  "HBM 공급 독점 — 빅3가 전 세계 95%+ 장악",
                 "서버 DRAM 계약가 +60~70% YoY  ·  TrendForce 확인",
                 "수요 +35% vs 공급 +16%  →  구조적 부족"),
        (CYAN,   "HBM 웨이퍼 23% 잠식 → 범용 DRAM 이중 수혜",
                 "삼성 영업이익 +755% YoY  /  마이크론 매출 +57%",
                 "ETF 1개로 HBM·범용 DRAM 동시 노출"),
        (PURPLE, "발주잔고 2027년까지 적체",
                 "하이퍼스케일러 선주문 구조  ·  취소 어려운 구조",
                 "삼성 HBM3E 엔비디아 퀄 통과가 단기 최대 변수"),
    ]

    y = 182
    for color, title, sub1, sub2 in points:
        draw.rectangle([rx, y, rx + 4, y + 80], fill=color)
        draw.text((rx + 16, y),      title, font=bold(21), fill=WHITE)
        draw.text((rx + 16, y + 32), sub1,  font=font(18), fill=GRAY)
        draw.text((rx + 16, y + 56), sub2,  font=font(18), fill=color)
        draw.line([(rx, y + 96), (W - 60, y + 96)], fill=DARK_GRAY, width=1)
        y += 116

    # 하단 핵심 테제
    draw.line([(60, 570), (W - 60, 570)], fill=DARK_GRAY, width=1)
    draw.rectangle([60, 588, W - 60, 642], fill=(35, 28, 10))
    draw.text((80, 600), "핵심 테제", font=bold(19), fill=AMBER)
    draw.text((220, 600),
              "메모리 슈퍼사이클 순수 베팅 — 빅3 독과점·HBM·범용 DRAM 이중 수혜를 단일 티커로",
              font=font(20), fill=WHITE)

    footer(draw, "2026.06.09", "TrendForce  ·  Roundhill  ·  Yahoo Finance")
    out = os.path.join(OUT_DIR, "2026-06-09_DRAM_ETF_메모리슈퍼사이클.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
