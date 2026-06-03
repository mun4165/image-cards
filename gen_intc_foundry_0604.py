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
DARK_GRAY = (60, 70, 82)
BLUE      = (59, 130, 246)
CYAN      = (6, 182, 212)
GREEN     = (52, 211, 153)
AMBER     = (245, 158, 11)
PURPLE    = (167, 139, 250)

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

def text_w(draw, text, f):
    bbox = draw.textbbox((0, 0), text, font=f)
    return bbox[2] - bbox[0]

def footer(draw, date_str, source_str):
    draw.line([(60, H - 52), (W - 60, H - 52)], fill=DARK_GRAY, width=1)
    draw.text((60, H - 36), f"{date_str}  |  {source_str}",
              font=font(17), fill=GRAY)


def make_main():
    img, draw = make_base(BLUE)
    draw.rectangle([0, 0, 4, H], fill=BLUE)

    # 헤더
    draw.text((60, 44), "INTC  파운드리 전략", font=bold(40), fill=BLUE)
    draw.text((60, 96), "인텔은 왜 공장을 포기하지 않는가 — 18A·14A와 TSMC 대항마 테제", font=font(22), fill=GRAY)
    draw.line([(60, 132), (W - 60, 132)], fill=DARK_GRAY, width=1)

    # 좌측: 공정 현황
    lx = 60
    draw.text((lx, 148), "공정 세대", font=bold(22), fill=GRAY)

    nodes = [
        ("18A",  "양산 시작   ↔  TSMC N3급",  GREEN),
        ("14A",  "2027년 목표  ↔  TSMC N2급",  AMBER),
    ]
    y = 178
    for node, desc, color in nodes:
        draw.rectangle([lx, y, lx + 4, y + 52], fill=color)
        draw.text((lx + 16, y),      node, font=bold(28), fill=color)
        draw.text((lx + 16, y + 34), desc, font=font(19), fill=GRAY)
        y += 72

    draw.line([(lx, y + 4), (lx + 520, y + 4)], fill=DARK_GRAY, width=1)

    # 지정학 맥락
    y += 20
    draw.text((lx, y), "지정학 맥락", font=bold(22), fill=GRAY)
    y += 34
    lines = [
        ("설계", "미국 (NVIDIA·AMD·Apple·Qualcomm)", WHITE),
        ("생산", "대만 TSMC 의존", AMBER),
        ("목표", "미국 내 첨단 파운드리 확보", CYAN),
    ]
    for label, val, color in lines:
        draw.text((lx,       y), label, font=font(19), fill=GRAY)
        draw.text((lx + 100, y), val,   font=bold(19), fill=color)
        y += 36

    # 구분선
    draw.line([(620, 132), (620, H - 60)], fill=DARK_GRAY, width=1)

    # 우측: 시나리오 + 핵심 촉매
    rx = 650
    draw.text((rx, 148), "투자 시나리오", font=bold(22), fill=GRAY)

    scenarios = [
        (GREEN,  "① 14A 성공 + 외부 고객 수주",
                 "미국 정부 지원 확대",
                 "주가 재평가 — 현재 구간 아닐 것"),
        (GRAY,   "② 현상 유지",
                 "CPU 압박 지속 (AMD·ARM·NVIDIA)",
                 "파운드리 느린 성장, 횡보"),
        (AMBER,  "③ 파운드리 포기·분사",
                 "투자 부담 + 수율 실패",
                 "추가 하락 가능"),
    ]

    y = 178
    for color, title, sub1, sub2 in scenarios:
        draw.rectangle([rx, y, rx + 4, y + 72], fill=color)
        draw.text((rx + 16, y),      title, font=bold(21), fill=WHITE)
        draw.text((rx + 16, y + 30), sub1,  font=font(18), fill=GRAY)
        draw.text((rx + 16, y + 52), sub2,  font=font(18), fill=color)
        draw.line([(rx, y + 86), (W - 60, y + 86)], fill=DARK_GRAY, width=1)
        y += 100

    # 핵심 촉매
    draw.text((rx, y + 6),  "핵심 촉매 하나", font=bold(20), fill=GRAY)
    draw.text((rx, y + 36), "외부 고객 첫 대형 수주 발표", font=bold(26), fill=CYAN)
    draw.text((rx, y + 72), "그 발표가 나오는 순간 내러티브가 바뀐다", font=font(19), fill=GRAY)

    footer(draw, "2026.06.04", "개인 공부 기록 · 투자 추천 아님")
    out = os.path.join(OUT_DIR, "2026-06-04_INTC_파운드리전략.png")
    img.save(out)
    print(f"Saved: {out}")


make_main()
print("Done.")
