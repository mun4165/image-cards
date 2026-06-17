from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-14"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (10, 12, 18)
GRID      = (255, 255, 255, 10)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 56, 70)
GREEN     = (52, 211, 153)
RED       = (239, 68, 68)
AMBER     = (245, 158, 11)
CYAN      = (6, 182, 212)

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size):          return ImageFont.truetype(FONT_PATH, size, index=4)

def make_base():
    img  = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    # 좌측 GREEN, 우측 RED 상단 바
    draw.rectangle([0, 0, 636, 4], fill=GREEN)
    draw.rectangle([644, 0, W, 4], fill=RED)
    draw.rectangle([0, 0, 4, H], fill=GREEN)
    draw.rectangle([W-4, 0, W, H], fill=RED)
    return img, ImageDraw.Draw(img)

def box(draw, x1, y1, x2, y2, fill, outline=None, radius=6):
    draw.rounded_rectangle([x1,y1,x2,y2], radius=radius, fill=fill)
    if outline:
        draw.rounded_rectangle([x1,y1,x2,y2], radius=radius, outline=outline, width=1)

def make_card():
    img, draw = make_base()

    # ── 헤더 ──
    draw.rectangle([0, 4, W, 56], fill=(12, 14, 20))
    draw.text((16, 10),  "SpaceX (SPCX)", font=bold(26), fill=WHITE)
    draw.text((248, 13), "—  살 이유 10가지 vs 팔 이유 10가지", font=font(20), fill=GRAY)
    draw.text((16, 40),  "조급함보다 균형 잡힌 시각  /  2026.06.14", font=font(13), fill=GRAY)
    draw.line([(0,56),(W,56)], fill=DARK_GRAY, width=1)

    PAD  = 7
    TOP  = 62
    BOT  = H - 44
    MID  = 638
    ITEM_H = 53

    # ══ 왼쪽 — Bull ══
    box(draw, PAD, TOP, MID-PAD, TOP+32, (10,24,16), outline=GREEN)
    draw.rectangle([PAD, TOP, PAD+4, TOP+32], fill=GREEN)
    draw.text((PAD+12, TOP+6), "Bull Case  —  살 이유 10", font=bold(15), fill=GREEN)

    bulls = [
        ("①", "Starlink 1,200만 가입자",       "이미 작동하는 사업  /  해양·항공·정부망 확대 중"),
        ("②", "발사 비용 자체 통제",             "Starship 완성 시 1kg 발사 비용 1/10 수준"),
        ("③", "재사용 대형 발사체 경쟁자 없음",  "ULA·Ariane·Kuiper 모두 격차 큼"),
        ("④", "골든돔 핵심 플레이어",            "우주 기반 미사일 방어  /  국방 예산 우주 집중"),
        ("⑤", "Starlink v3  처리량 대폭 증가",  "동일 위성 수로 더 많은 가입자·프리미엄 요금 여지"),
        ("⑥", "발사체·위성·안테나 수직계열화",   "외부 의존 없음  /  마진 외부 유출 없음"),
        ("⑦", "AI 임대 수익화  확장 가능",       "Anthropic 외 MS·Google·Meta 등 추가 임대 가능"),
        ("⑧", "화성 옵션  주가에 미반영",        "실현 시 규모가 너무 커서 현재가에 반영 불가"),
        ("⑨", "머스크 정부 접근성",              "발사 허가 속도·DoD 계약 우선순위 우위"),
        ("⑩", "나스닥 100 편입 가능성",          "편입 시 QQQ $3,000억 패시브 강제 매수 유입"),
    ]

    by = TOP + 36
    for num, title, desc in bulls:
        box(draw, PAD+4, by, MID-PAD-4, by+ITEM_H-2, (10,20,14))
        draw.rectangle([PAD+4, by, PAD+8, by+ITEM_H-2], fill=GREEN)
        draw.text((PAD+14, by+5),  f"{num} {title}", font=bold(13), fill=GREEN)
        draw.text((PAD+14, by+26), desc,              font=font(12), fill=GRAY)
        by += ITEM_H

    # ══ 오른쪽 — Bear ══
    RX = MID + PAD
    box(draw, RX, TOP, W-PAD, TOP+32, (24,10,10), outline=RED)
    draw.rectangle([RX, TOP, RX+4, TOP+32], fill=RED)
    draw.text((RX+12, TOP+6), "Bear Case  —  팔 이유 10", font=bold(15), fill=RED)

    bears = [
        ("①", "$160  =  모든 시나리오 선반영",   "CFRA 목표가 $115  /  하방 약 30%"),
        ("②", "Starship 상업 발사 계속 지연",     "시험 비행 반복 중  /  수익 전환 시점 불확실"),
        ("③", "ARPU $99 → $66  단가 하락 중",    "저가 시장 확장 효과  /  가입자 증가가 상쇄 못할 수 있음"),
        ("④", "AI 데이터센터 실행 리스크 노출",   "Colossus 최적화 실패  →  외부 임대로 해결"),
        ("⑤", "경쟁자 추격 중",                  "Kuiper·OneWeb·중국 메가콘스텔레이션"),
        ("⑥", "머스크 멀티태스킹 + 평판 리스크", "Tesla·X·xAI·Neuralink  관심 분산"),
        ("⑦", "FAA·FCC 규제 리스크 지속",        "발사 허가 지연  /  주파수 간섭 분쟁 반복"),
        ("⑧", "GAAP 흑자 미전환",                "S&P 500 편입 불가  /  패시브 유입 없음"),
        ("⑨", "IPO 후 보호예수 해제 물량",        "초기 투자자·스톡옵션 유통 압력 예정"),
        ("⑩", "Kessler Syndrome 리스크",         "위성 연쇄 충돌 시 Starlink 전체 위험"),
    ]

    ry = TOP + 36
    for num, title, desc in bears:
        box(draw, RX+4, ry, W-PAD-4, ry+ITEM_H-2, (22,10,10))
        draw.rectangle([RX+4, ry, RX+8, ry+ITEM_H-2], fill=RED)
        draw.text((RX+14, ry+5),  f"{num} {title}", font=bold(13), fill=RED)
        draw.text((RX+14, ry+26), desc,              font=font(12), fill=GRAY)
        ry += ITEM_H

    # ── 중앙 구분선 ──
    draw.line([(MID, TOP), (MID, BOT)], fill=DARK_GRAY, width=1)

    # ── 푸터 ──
    draw.line([(8, BOT-2), (W-8, BOT-2)], fill=DARK_GRAY, width=1)
    draw.text((16,   BOT+6), "2026.06.14  SpaceX(SPCX) Bull·Bear 정리", font=font(14), fill=GRAY)
    draw.text((W-270,BOT+6), "개인 공부 기록", font=bold(14), fill=AMBER)

    out = os.path.join(OUT_DIR, "2026-06-14_SPCX_BullBear10.png")
    img.save(out)
    print(f"Saved: {out}")

make_card()
print("Done.")
