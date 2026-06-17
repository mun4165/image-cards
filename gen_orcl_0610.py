from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-10"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (10, 12, 18)
GRID      = (255, 255, 255, 10)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 56, 70)
BLUE      = (59, 130, 246)
GREEN     = (52, 211, 153)
RED       = (239, 68, 68)
AMBER     = (245, 158, 11)
CYAN      = (6, 182, 212)
PURPLE    = (167, 139, 250)
ACCENT    = BLUE

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

def box(draw, x1, y1, x2, y2, fill, outline=None, radius=7):
    draw.rounded_rectangle([x1,y1,x2,y2], radius=radius, fill=fill)
    if outline:
        draw.rounded_rectangle([x1,y1,x2,y2], radius=radius, outline=outline, width=1)

def footer(draw, left, right):
    draw.line([(8, H-46), (W-8, H-46)], fill=DARK_GRAY, width=1)
    draw.text((16,   H-30), left,  font=font(16), fill=GRAY)
    draw.text((W-480,H-30), right, font=bold(16), fill=ACCENT)

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.rectangle([0, 4, W, 54], fill=(12, 16, 26))
    draw.text((16, 10), "ORCL  Oracle — Q4 FY2026  역대 최고 실적, 주가 -7%", font=bold(30), fill=WHITE)
    draw.text((16, 44), "FY2026 = 2025.06~2026.05  /  Q4 = 2026년 3~5월  /  오늘 장 마감 후 발표", font=font(15), fill=GRAY)
    draw.line([(0,54),(W,54)], fill=DARK_GRAY, width=1)

    PAD = 6
    TOP = 60
    BOT = H - 50
    DIV = 620

    # ════════════════════════
    # 왼쪽 — 실적 + 수주잔고
    # ════════════════════════

    # 실적 박스
    box(draw, PAD, TOP, DIV-PAD, TOP+188, (12,18,28))
    draw.text((PAD+14, TOP+8), "Q4 FY2026 실적", font=bold(16), fill=BLUE)

    results = [
        ("분기 매출",       "$19.2B",   "+21% YoY",   GREEN),
        ("OCI 클라우드",    "$5.8B",    "+93% YoY",   GREEN),
        ("SaaS",            "$4.1B",    "+10% YoY",   CYAN),
        ("Non-GAAP EPS",    "$2.11",    "+24% YoY",   GREEN),
    ]
    ry = TOP + 40
    for label, val, note, color in results:
        draw.text((PAD+14,  ry),  label, font=font(13), fill=GRAY)
        draw.text((PAD+150, ry),  val,   font=bold(17), fill=color)
        draw.text((PAD+270, ry),  note,  font=font(13), fill=GRAY)
        ry += 34

    # 왜 빠졌나
    box(draw, PAD, TOP+194, DIV-PAD, TOP+310, (22,14,14))
    draw.rectangle([PAD, TOP+194, PAD+5, TOP+310], fill=RED)
    draw.text((PAD+14, TOP+202), "주가 -7% 이유", font=bold(15), fill=RED)
    bear = [
        "FY2026 Capex  $55.7B  (가이던스 $50B 초과)",
        "FY2027 Capex 가이던스  $70B",
        "$40B 추가 자본조달  ($20B 주식발행 포함)",
    ]
    by = TOP + 228
    for b in bear:
        draw.text((PAD+14, by), f"· {b}", font=font(14), fill=WHITE)
        by += 26

    # 수주잔고 RPO 박스
    box(draw, PAD, TOP+316, DIV-PAD, BOT-4, (12,20,14), outline=GREEN)
    draw.text((PAD+14, TOP+326), "수주잔고 (RPO)", font=bold(16), fill=GREEN)
    draw.text((PAD+14, TOP+352), "$553B", font=bold(14), fill=GRAY)
    draw.text((PAD+100,TOP+352), "→", font=bold(16), fill=DARK_GRAY)
    draw.text((PAD+126,TOP+350), "$638B", font=bold(22), fill=GREEN)
    draw.text((PAD+270,TOP+352), "+$85B (단일 분기)", font=font(14), fill=GRAY)
    draw.line([(PAD+14, TOP+382),(DIV-PAD-10, TOP+382)], fill=DARK_GRAY, width=1)
    rpo = [
        ("12개월 인식 예정",  "12%",  "~$76.6B",  CYAN),
        ("36개월 인식 예정",  "46%",  "~$293B",   BLUE),
        ("고객선불·공급 GPU", "$75B", "오라클 Capex 없이 인식", AMBER),
    ]
    rrr = TOP + 390
    for label, pct, note, color in rpo:
        draw.text((PAD+14,  rrr), label, font=font(13), fill=GRAY)
        draw.text((PAD+190, rrr), pct,   font=bold(15), fill=color)
        draw.text((PAD+250, rrr), note,  font=font(13), fill=GRAY)
        rrr += 30

    # FY2030 목표
    draw.line([(PAD+14, rrr+4),(DIV-PAD-10, rrr+4)], fill=DARK_GRAY, width=1)
    draw.text((PAD+14, rrr+12), "FY2030 OCI 목표", font=font(13), fill=GRAY)
    draw.text((PAD+190,rrr+10), "$1,440억",        font=bold(16), fill=BLUE)
    draw.text((PAD+330,rrr+12), "현재 $200억 → 7배", font=font(13), fill=GRAY)
    draw.text((PAD+14, rrr+42), "FY2027 매출 가이던스", font=font(13), fill=GRAY)
    draw.text((PAD+190,rrr+40), "$90B",            font=bold(16), fill=CYAN)
    draw.text((PAD+270,rrr+42), "Non-GAAP EPS $8.05", font=font(13), fill=GRAY)

    # ════════════════════════
    # 오른쪽 — 부채 + 베팅
    # ════════════════════════
    RX = DIV + PAD

    # 부채 현황
    box(draw, RX, TOP, W-PAD, TOP+256, (20,16,10))
    draw.text((RX+14, TOP+8), "부채 현황", font=bold(16), fill=AMBER)
    debt = [
        ("총 부채",          "$134.6B",  RED),
        ("현금",             "$39.1B",   GREEN),
        ("순부채",           "~$95B+",   RED),
        ("D/E 비율",         "344%",     RED),
        ("영업현금흐름",     "$32B",     GREEN),
        ("잉여현금흐름",     "-$23.7B",  RED),
    ]
    dy = TOP + 40
    for label, val, color in debt:
        draw.text((RX+14,  dy), label, font=font(13), fill=GRAY)
        draw.text((RX+175, dy), val,   font=bold(16), fill=color)
        dy += 34

    # 핵심 베팅 박스
    by2 = TOP + 262
    box(draw, RX, by2, W-PAD, BOT-4, (16,14,28), outline=PURPLE)
    draw.text((RX+14, by2+10), "오라클이 걸고 있는 베팅", font=bold(16), fill=PURPLE)
    draw.line([(RX+14, by2+38),(W-PAD-10, by2+38)], fill=DARK_GRAY, width=1)
    draw.text((RX+14, by2+48),  "RPO 전환 속도  >  부채 비용",    font=bold(17), fill=WHITE)
    draw.text((RX+14, by2+78),  "맞으면  →  제2의 AWS",           font=font(15), fill=GREEN)
    draw.text((RX+14, by2+104), "틀리면  →  레버리지가 수익성 잠식", font=font(15), fill=RED)
    draw.line([(RX+14, by2+132),(W-PAD-10, by2+132)], fill=DARK_GRAY, width=1)
    draw.text((RX+14, by2+142), "참고: 아마존도 2013~16년 FCF 마이너스였다", font=font(13), fill=GRAY)
    draw.text((RX+14, by2+170), "다음 확인  →  2026.09  Q1 FY2027", font=bold(14), fill=PURPLE)
    draw.text((RX+14, by2+196), "OCI 성장률 유지 여부  /  RPO 추가 증가", font=font(13), fill=GRAY)

    footer(draw, "2026.06.10  Oracle Q4 FY2026 Earnings", "ORCL  ·  OCI  ·  RPO  ·  Capex")

    out = os.path.join(OUT_DIR, "2026-06-10_ORCL_실적분석.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
