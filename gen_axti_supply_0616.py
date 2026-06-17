from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR   = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-16"
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
    draw.text((W-440,H-30), right, font=bold(16), fill=ACCENT)

def arrow_v(draw, x, y1, y2, color):
    draw.line([(x, y1), (x, y2-7)], fill=color, width=2)
    draw.polygon([(x-5, y2-7), (x, y2), (x+5, y2-7)], fill=color)

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.rectangle([0, 4, W, 62], fill=(10, 16, 24))
    draw.text((16, 10), "AXT($AXTI)  —  병목이 아니라, 수요가 공급을 압도하는 시장의 주요 플레이어", font=bold(24), fill=WHITE)
    draw.text((16, 44), "InP 웨이퍼 upstream 공급사  ·  6인치에서 Coherent·Sumitomo가 앞서 있다  ·  그래도 공급이 70% 부족하다", font=font(14), fill=GRAY)
    draw.line([(0, 62), (W, 62)], fill=DARK_GRAY, width=1)

    PAD = 8
    TOP = 70
    BOT = H - 52
    DIV1 = 410   # 왼쪽 패널 끝
    DIV2 = 780   # 중간 패널 끝

    # ═══════════════════════════════
    # 왼쪽 — 공급망 위치
    # ═══════════════════════════════
    box(draw, PAD, TOP, DIV1-PAD, TOP+30, (12,18,28), outline=CYAN)
    draw.text((PAD+12, TOP+7), "InP 공급망 — AXT는 어디에 있나", font=bold(14), fill=CYAN)

    chain = [
        ("인듐 원재료",         GRAY,  False),
        ("InP 단결정 웨이퍼",   CYAN,  True),   # AXT
        ("에피택셜 성장",       GRAY,  False),
        ("레이저칩 제조",       GRAY,  False),
        ("트랜시버 모듈 납품",  GRAY,  False),
    ]
    labels = [
        "",
        "← AXT / Tongmei  (35% 점유율)",
        "",
        "← Coherent, Lumentum, AAOI",
        "← 데이터센터",
    ]

    cy = TOP + 42
    for i, (name, color, highlight) in enumerate(chain):
        bg_fill = (10, 22, 30) if highlight else (13, 13, 20)
        out_col = color if highlight else DARK_GRAY
        box(draw, PAD+10, cy, DIV1-PAD-10, cy+36, bg_fill, outline=out_col)
        draw.text((PAD+20, cy+9), name, font=bold(14) if highlight else font(13), fill=color)
        if labels[i]:
            draw.text((PAD+20+140, cy+12), labels[i], font=font(11), fill=AMBER if highlight else GRAY)
        if i < len(chain)-1:
            arrow_v(draw, DIV1//2, cy+36, cy+50, color if highlight else DARK_GRAY)
        cy += 50

    # 공급망 요약
    sum_y = cy + 4
    box(draw, PAD+10, sum_y, DIV1-PAD-10, sum_y+42, (10,20,14), outline=GREEN)
    draw.text((PAD+20, sum_y+6),  "AXT = upstream 순수 공급자", font=bold(13), fill=GREEN)
    draw.text((PAD+20, sum_y+24), "웨이퍼만 판다  /  디바이스·모듈 없음", font=font(12), fill=GRAY)

    # ═══════════════════════════════
    # 중간 — 6인치 현황
    # ═══════════════════════════════
    MX = DIV1 + PAD
    box(draw, MX, TOP, DIV2-PAD, TOP+30, (12,18,28), outline=AMBER)
    draw.text((MX+12, TOP+7), "6인치 InP — 누가 어디까지 왔나", font=bold(14), fill=AMBER)

    players = [
        ("Coherent",   GREEN,  "풀 양산 돌입",     "예정보다 1년 앞당김",          "캐파 4배 / 다이비용 60%↓",   "자체 소비 목적 (외판 아님)"),
        ("Sumitomo",   AMBER,  "양산 중",          "2026년까지 40% 증설",           "InP 시장 점유 ~30%",          "퀄리티 리더십 보유"),
        ("AXT/Tongmei",CYAN,   "R&D 투자 단계",    "$6억3250만 조달 (2026.04)",     "현재 2·3·4인치 양산",        "6인치는 추격 중"),
    ]

    py = TOP + 44
    for name, color, status, detail1, detail2, note in players:
        box(draw, MX+4, py, DIV2-PAD-4, py+88, (13,13,20), outline=color)
        draw.rectangle([MX+4, py, MX+8, py+88], fill=color)
        draw.text((MX+16, py+6),  name,    font=bold(16), fill=color)
        draw.text((MX+16, py+28), status,  font=bold(13), fill=WHITE)
        draw.text((MX+16, py+48), detail1, font=font(12), fill=GRAY)
        draw.text((MX+16, py+64), detail2, font=font(12), fill=GRAY)
        draw.text((MX+16, py+78), note,    font=font(11), fill=(100,110,130))
        py += 96

    # 결론
    conc_y = py + 6
    box(draw, MX+4, conc_y, DIV2-PAD-4, conc_y+52, (16,14,10), outline=AMBER)
    draw.text((MX+16, conc_y+6),  "AXT는 6인치에서 추격자",              font=bold(13), fill=AMBER)
    draw.text((MX+16, conc_y+24), "그러나 공급이 워낙 부족해",           font=font(12), fill=WHITE)
    draw.text((MX+16, conc_y+40), "추격자도 다 팔리는 시장이다",         font=bold(12), fill=GREEN)

    # ═══════════════════════════════
    # 오른쪽 — 수급 + 가이던스
    # ═══════════════════════════════
    RX = DIV2 + PAD

    # 수급 빅넘버
    box(draw, RX, TOP, W-PAD, TOP+30, (12,18,28), outline=GREEN)
    draw.text((RX+12, TOP+7), "InP 수급 현황 (2025 기준)", font=bold(14), fill=GREEN)

    num_y = TOP + 44
    box(draw, RX+4, num_y, W-PAD-4, num_y+110, (10,20,10), outline=GREEN)

    # 왼쪽: 수요/공급 숫자
    draw.text((RX+14, num_y+6),  "수요",     font=bold(12), fill=GRAY)
    draw.text((RX+14, num_y+24), "200만 개", font=bold(24), fill=GREEN)
    draw.text((RX+14, num_y+62), "공급",     font=bold(12), fill=GRAY)
    draw.text((RX+14, num_y+80), "60만 개",  font=bold(24), fill=RED)

    # 오른쪽: 70% 강조 박스
    box(draw, RX+210, num_y+10, W-PAD-14, num_y+100, (22,10,10), outline=RED)
    draw.text((RX+226, num_y+14), "공급 부족",  font=bold(13), fill=GRAY)
    draw.text((RX+222, num_y+34), "70%",        font=bold(42), fill=RED)

    # 주문 매진
    sold_y = num_y + 118
    box(draw, RX+4, sold_y, W-PAD-4, sold_y+30, (18,14,10), outline=AMBER)
    draw.text((RX+16, sold_y+7), "전체 주요 공급사 주문  →  2026년까지 꽉 참", font=bold(13), fill=AMBER)

    # AXT 포지션
    pos_y = sold_y + 40
    box(draw, RX+4, pos_y, W-PAD-4, pos_y+44, (10,18,26), outline=CYAN)
    draw.text((RX+16, pos_y+6),  "AXT 시장 점유율",              font=bold(13), fill=CYAN)
    draw.text((RX+16, pos_y+24), "35%  —  공급 부족 시장의 주요 플레이어", font=bold(14), fill=WHITE)

    # Q2 가이던스
    g_y = pos_y + 54
    box(draw, RX+4, g_y, W-PAD-4, g_y+30, (12,18,28), outline=PURPLE)
    draw.text((RX+16, g_y+7), "Q2 2026 가이던스", font=bold(14), fill=PURPLE)

    g_items = [
        ("매출",      "$34M+",           WHITE),
        ("GAAP EPS",  "+$0.05~0.07",     GREEN),
        ("InP 백로그","$100M+ (사상 최대)", CYAN),
    ]
    gi_y = g_y + 38
    for label, val, color in g_items:
        box(draw, RX+4, gi_y, W-PAD-4, gi_y+32, (13,13,20))
        draw.text((RX+16, gi_y+8),   label, font=font(13), fill=GRAY)
        draw.text((RX+180, gi_y+6),  val,   font=bold(14), fill=color)
        gi_y += 38

    # GAAP 흑자 강조
    first_y = gi_y + 4
    box(draw, RX+4, first_y, W-PAD-4, first_y+28, (10,20,14), outline=GREEN)
    draw.text((RX+16, first_y+6), "GAAP 기준 첫 흑자 가이던스  —  이번이 처음이다", font=bold(13), fill=GREEN)

    # 리스크
    risk_y = first_y + 38
    box(draw, RX+4, risk_y, W-PAD-4, risk_y+26, (18,12,12), outline=RED)
    draw.text((RX+16, risk_y+5), "리스크", font=bold(13), fill=RED)

    risks = [
        "중국 베이징 생산  →  수출허가 지연 시 매출 직격",
        "Coherent 자체 6인치 생산  →  AXT 주문 축소 가능성",
    ]
    ri_y = risk_y + 32
    for r in risks:
        box(draw, RX+4, ri_y, W-PAD-4, ri_y+26, (15,12,12))
        draw.rectangle([RX+4, ri_y, RX+7, ri_y+26], fill=RED)
        draw.text((RX+14, ri_y+6), r, font=font(12), fill=(200,120,120))
        ri_y += 31

    footer(draw, "2026.06.16  AXT($AXTI) — InP 수급 분석", "$AXTI  ·  개인 공부 기록")

    out = os.path.join(OUT_DIR, "2026-06-16_AXTI_공급부족_주요플레이어.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
