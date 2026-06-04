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

def footer(draw, date_str, source_str):
    draw.line([(60, H - 52), (W - 60, H - 52)], fill=DARK_GRAY, width=1)
    draw.text((60, H - 36), f"{date_str}  |  {source_str}",
              font=font(17), fill=GRAY)


def make_main():
    img, draw = make_base(CYAN)
    draw.rectangle([0, 0, 4, H], fill=CYAN)

    # 헤더
    draw.text((60, 44), "NASA GDC", font=bold(40), fill=CYAN)
    draw.text((60, 96), "우주기상 위성 군집 — Geospace Dynamics Constellation", font=font(22), fill=GRAY)
    draw.line([(60, 132), (W - 60, 132)], fill=DARK_GRAY, width=1)

    # 좌측: 프로그램 개요
    lx = 60
    draw.text((lx, 148), "프로그램 개요", font=bold(22), fill=GRAY)

    items = [
        ("주관",   "NASA 헬리오피직스 / Living With a Star",  WHITE),
        ("단계",   "Phase A — 개념 설계 진행 중",             AMBER),
        ("구성",   "6기 이상 위성 군집 동시 다점 관측",        CYAN),
        ("고도",   "약 215~250마일 (ISS 궤도 유사)",           GRAY),
        ("목적",   "우주기상·자기권·전리층 글로벌 관측",        WHITE),
    ]

    y = 182
    for label, val, color in items:
        draw.text((lx,       y), label, font=font(19), fill=GRAY)
        draw.text((lx + 90,  y), val,   font=bold(19), fill=color)
        y += 38

    draw.line([(lx, y + 6), (lx + 540, y + 6)], fill=DARK_GRAY, width=1)

    # 우주기상 영향
    y += 22
    draw.text((lx, y), "우주기상이 위협하는 것", font=bold(20), fill=GRAY)
    y += 32
    risks = ["GPS 오작동", "위성 궤도 이탈", "통신 두절", "전력망 장애"]
    for risk in risks:
        draw.rectangle([lx, y + 6, lx + 6, y + 22], fill=AMBER)
        draw.text((lx + 18, y), risk, font=font(19), fill=WHITE)
        y += 34

    # 구분선
    draw.line([(630, 132), (630, H - 60)], fill=DARK_GRAY, width=1)

    # 우측: 시장 + 참여 업체
    rx = 660

    # 시장 규모
    draw.text((rx, 148), "시장 규모", font=bold(22), fill=GRAY)

    draw.text((rx, 184), "$1.96B", font=bold(36), fill=GREEN)
    draw.text((rx, 228), "2025년 우주기상 모니터링 위성 시장", font=font(19), fill=GRAY)

    draw.text((rx, 268), "→  $2.17B  (2026)", font=bold(24), fill=CYAN)
    draw.text((rx, 300), "CAGR  10.7%", font=bold(22), fill=AMBER)

    draw.line([(rx, 338), (W - 60, 338)], fill=DARK_GRAY, width=1)

    # 참여 가능 업체
    draw.text((rx, 352), "본사업 경쟁 가능 업체", font=bold(22), fill=GRAY)

    companies = [
        ("Rocket Lab",        "소형 위성 버스 · NASA 계약 다수",  BLUE),
        ("Northrop Grumman",  "전통 NASA 위성 제작사",             PURPLE),
        ("Ball Aerospace",    "헬리오피직스 위성 경험",             GREEN),
        ("York Space",        "신흥 소형 위성 전문",                GRAY),
    ]

    y = 386
    for name, desc, color in companies:
        draw.rectangle([rx, y, rx + 4, y + 48], fill=color)
        draw.text((rx + 16, y),      name, font=bold(20), fill=color)
        draw.text((rx + 16, y + 26), desc, font=font(17), fill=GRAY)
        y += 64

    # 유의사항
    draw.text((rx, y + 2), "※ 본계약 미확정 · 예산 변수 존재", font=font(17), fill=AMBER)

    footer(draw, "2026.06.04", "NASA Science · Research and Markets · 개인 공부 기록")
    out = os.path.join(OUT_DIR, "2026-06-04_NASA_GDC.png")
    img.save(out)
    print(f"Saved: {out}")


make_main()
print("Done.")
