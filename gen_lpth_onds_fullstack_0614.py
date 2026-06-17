from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR   = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-14"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (10, 12, 18)
GRID      = (255, 255, 255, 10)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 56, 70)
BLUE      = (59, 130, 246)
GREEN     = (52, 211, 153)
AMBER     = (245, 158, 11)
CYAN      = (6, 182, 212)
PURPLE    = (167, 139, 250)
RED       = (239, 68, 68)
ACCENT    = CYAN

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
    draw.text((W-420,H-30), right, font=bold(16), fill=ACCENT)

def arrow_h(draw, x1, x2, y, color):
    draw.line([(x1, y), (x2-8, y)], fill=color, width=2)
    draw.polygon([(x2-8, y-5), (x2, y), (x2-8, y+5)], fill=color)

def arrow_v(draw, x, y1, y2, color):
    draw.line([(x, y1), (x, y2-8)], fill=color, width=2)
    draw.polygon([(x-5, y2-8), (x, y2), (x+5, y2-8)], fill=color)

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.rectangle([0, 4, W, 58], fill=(10, 16, 24))
    draw.text((16, 10), "LPTH · ONDS · UMAC · Palantir · Anduril — 드론 ISR 풀스택", font=bold(26), fill=WHITE)
    draw.text((16, 42), "지분이 먼저 묶이고, 소프트웨어가 마지막을 닫았다", font=font(15), fill=GRAY)
    draw.line([(0, 58), (W, 58)], fill=DARK_GRAY, width=1)

    PAD = 8
    TOP = 66
    BOT = H - 52
    DIV = 500   # 왼쪽 패널 끝

    # ═══════════════════════════════
    # 왼쪽 — 지분 구조
    # ═══════════════════════════════
    box(draw, PAD, TOP, DIV-PAD, TOP+34, (12,18,28), outline=CYAN)
    draw.text((PAD+12, TOP+8), "지분 구조 — 하드웨어 클러스터", font=bold(15), fill=CYAN)

    # ONDS + UMAC → LPTH
    ey = TOP + 52
    box(draw, PAD+10, ey, DIV//2-6, ey+48, (14,20,14), outline=GREEN)
    draw.text((PAD+22, ey+8),  "ONDS",      font=bold(18), fill=GREEN)
    draw.text((PAD+22, ey+30), "자율드론·지상로봇", font=font(12), fill=GRAY)

    box(draw, DIV//2+6, ey, DIV-PAD-10, ey+48, (20,16,10), outline=AMBER)
    draw.text((DIV//2+18, ey+8),  "UMAC",   font=bold(18), fill=AMBER)
    draw.text((DIV//2+18, ey+30), "FPV드론", font=font(12), fill=GRAY)

    # 화살표 ↓
    arrow_v(draw, DIV//4+8,    ey+48, ey+82, GREEN)
    draw.text((PAD+22, ey+52), "$400만", font=bold(12), fill=GREEN)

    arrow_v(draw, DIV*3//4-14, ey+48, ey+82, AMBER)
    draw.text((DIV//2+18, ey+52), "$400만", font=bold(12), fill=AMBER)

    # 화살 합류 라인
    mid_x = (DIV//4+8 + DIV*3//4-14) // 2
    draw.line([(DIV//4+8, ey+82), (DIV*3//4-14, ey+82)], fill=GRAY, width=2)
    arrow_v(draw, mid_x, ey+82, ey+110, WHITE)
    draw.text((mid_x-30, ey+84), "총 $800만  2025.09", font=font(11), fill=GRAY)

    # LPTH 박스
    ly = ey + 110
    box(draw, PAD+10, ly, DIV-PAD-10, ly+56, (10,18,26), outline=CYAN)
    draw.text((PAD+22, ly+8),  "LPTH",                       font=bold(20), fill=CYAN)
    draw.text((PAD+22, ly+32), "열화상 렌즈·IR 카메라  /  BlackDiamond 소재", font=font(12), fill=GRAY)

    # ONDS → UMAC 유증 참여 표시
    cross_y = ey + 20
    draw.line([(DIV//2+6, cross_y), (DIV//2+6-40, cross_y)], fill=(100,100,120), width=1)
    draw.line([(DIV//2+6-40, cross_y), (DIV//2+6-40, cross_y-10)], fill=(100,100,120), width=1)
    draw.text((PAD+10, ey-14), "ONDS, UMAC 유증 핵심 전략투자자 참여", font=font(11), fill=(100,110,130))

    # 지분 정리 라벨
    sum_y = ly + 66
    box(draw, PAD+10, sum_y, DIV-PAD-10, sum_y+34, (12,14,20))
    draw.text((PAD+22, sum_y+6),  "눈(LPTH)  ·  몸(UMAC)  ·  두뇌(ONDS)", font=bold(13), fill=CYAN)
    draw.text((PAD+22, sum_y+22), "세 회사, 자본으로 연결된 하드웨어 클러스터",  font=font(12), fill=WHITE)

    # 소프트웨어 연결 타임라인 (왼쪽 하단)
    sw_y = sum_y + 44
    box(draw, PAD, sw_y, DIV-PAD, sw_y+30, (12,18,28), outline=PURPLE)
    draw.text((PAD+12, sw_y+6), "소프트웨어 연결 타임라인", font=bold(14), fill=PURPLE)

    timeline = [
        (GREEN,  "2025.03", "ONDS ↔ Palantir",         "Foundry → Optimus·Iron Drone Raider 통합"),
        (BLUE,   "2025.05", "Anduril ↔ Palantir",       "Menace = Palantir Edge preferred hardware"),
        (AMBER,  "2025.09", "ONDS·UMAC → LPTH",         "$800만 전략 투자  /  지분 취득 동시 진행"),
        (PURPLE, "2026.03", "ONDS·Palantir·World View", "성층권 발룬 추가 — 멀티도메인 ISR 확장"),
    ]
    ty = sw_y + 38
    for color, date, title_t, desc in timeline:
        box(draw, PAD+6, ty, DIV-PAD-6, ty+46, (13,13,20))
        draw.rectangle([PAD+6, ty, PAD+10, ty+46], fill=color)
        draw.text((PAD+18, ty+4),  date,    font=bold(12),  fill=color)
        draw.text((PAD+18, ty+20), title_t, font=bold(13),  fill=WHITE)
        draw.text((PAD+18, ty+36), desc,    font=font(11),  fill=GRAY)
        ty += 52

    # ═══════════════════════════════
    # 오른쪽 — 풀스택 4레이어
    # ═══════════════════════════════
    RX = DIV + PAD
    box(draw, RX, TOP, W-PAD, TOP+34, (12,18,28), outline=PURPLE)
    draw.text((RX+12, TOP+8), "풀스택 — 4개 레이어", font=bold(15), fill=PURPLE)

    layers = [
        (GREEN,  "1단계  탐지",         "LPTH BlackDiamond 렌즈·IR 카메라",          "열원 포착  /  야간·악천후 전천후"),
        (BLUE,   "2단계  플랫폼",       "UMAC FPV 드론  +  ONDS 자율 드론·지상 로봇", "운용 플랫폼  /  자율화 OS"),
        (PURPLE, "3단계  인텔리전스",   "Palantir Foundry · AIP",                    "데이터 융합  /  실시간 의사결정"),
        (AMBER,  "4단계  엣지 C2",      "Anduril Menace  +  Palantir Edge",          "전장 지휘통제  /  서버 인프라 불필요"),
    ]

    lh = 78  # 고정 컴팩트 높이
    for i, (color, title, main, sub) in enumerate(layers):
        ly2 = TOP + 44 + i * (lh + 8)
        box(draw, RX+4, ly2, W-PAD-4, ly2+lh, (14,14,20), outline=color)
        draw.rectangle([RX+4, ly2, RX+8, ly2+lh], fill=color)
        draw.text((RX+16, ly2+6),  title, font=bold(14), fill=color)
        draw.text((RX+16, ly2+26), main,  font=bold(13), fill=WHITE)
        draw.text((RX+16, ly2+50), sub,   font=font(12), fill=GRAY)
        if i < 3:
            arrow_v(draw, RX+20, ly2+lh, ly2+lh+8, color)

    # 레이어 끝 위치 계산 후 하단 박스 균등 분할
    layer_end = TOP + 44 + 4 * (lh + 8)       # 454
    missing_y = BOT - 34                        # 634
    gap = 8
    bottom_h = (missing_y - layer_end - gap * 3) // 2  # 두 박스 동일 높이

    # ONDS = 허브 설명
    hub_y = layer_end + gap
    box(draw, RX+4, hub_y, W-PAD-4, hub_y+bottom_h, (16,14,26), outline=PURPLE)
    draw.rectangle([RX+4, hub_y, RX+8, hub_y+bottom_h], fill=PURPLE)
    draw.text((RX+16, hub_y+6),            "ONDS = 허브",                                        font=bold(14), fill=PURPLE)
    draw.text((RX+16, hub_y+26),           "하드웨어(LPTH·UMAC) ↔ 소프트웨어(Palantir) 연결 거점", font=font(12), fill=GRAY)
    draw.text((RX+16, hub_y+44),           "전통 prime(록히드·레이시온) 없이 지분·파트너십으로 수직 통합", font=font(12), fill=WHITE)
    if bottom_h > 66:
        draw.text((RX+16, hub_y+62), "드론·광학·AI·엣지C2 — 네 레이어가 한 생태계 안에 있다", font=font(11), fill=GRAY)

    # Golden Dome
    gd_y = hub_y + bottom_h + gap
    box(draw, RX+4, gd_y, W-PAD-4, gd_y+bottom_h, (20,14,12), outline=AMBER)
    draw.rectangle([RX+4, gd_y, RX+8, gd_y+bottom_h], fill=AMBER)
    draw.text((RX+16, gd_y+6),  "Golden Dome",                                                    font=bold(14), fill=AMBER)
    draw.text((RX+16, gd_y+26), "Anduril·Palantir 컨소시엄  —  미 정부 미사일 방어 소프트웨어",    font=font(12), fill=GRAY)
    draw.text((RX+16, gd_y+44), "ONDS-Palantir 연결이 확장되는 방향과 같은 궤도",                  font=font(12), fill=WHITE)
    if bottom_h > 66:
        draw.text((RX+16, gd_y+62), "국방 자율화 풀스택이 소프트웨어 레이어에서도 닫히고 있다", font=font(11), fill=GRAY)

    # 아직 없는 것 — 하단 풀 위드
    missing_y = BOT - 34
    box(draw, PAD, missing_y, W-PAD, BOT-4, (18,12,12), outline=RED)
    draw.text((PAD+14, missing_y+8),
              "미확정  ·  LPTH↔Anduril 직접 파트너십 공시 없음  /  UMAC↔Palantir 직접 계약 없음  →  두 연결 추가 시 풀스택 완성",
              font=font(12), fill=(200, 120, 120))

    footer(draw, "2026.06.14  LPTH·ONDS·UMAC·Palantir·Anduril", "$LPTH · $ONDS · $PLTR  ·  개인 공부 기록")

    out = os.path.join(OUT_DIR, "2026-06-14_LPTH_ONDS_풀스택_ISR.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
