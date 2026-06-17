from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-12"
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

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.rectangle([0, 4, W, 56], fill=(10, 16, 24))
    draw.text((16, 10), "$LPTH  백로그 $110.6M 해부 — 수주처와 경향성", font=bold(28), fill=WHITE)
    draw.text((16, 44), "FY2026 Q3 기준  /  YoY +196%  /  85% 국방·감시·보안", font=font(14), fill=GRAY)
    draw.line([(0,56),(W,56)], fill=DARK_GRAY, width=1)

    PAD = 6
    TOP = 62
    BOT = H - 52
    DIV = 560

    # ══════════════════════
    # 왼쪽 — 백로그 구조 + 확정 백로그
    # ══════════════════════

    # 백로그 구조 박스
    box(draw, PAD, TOP, DIV-PAD, TOP+108, (12,18,28), outline=CYAN)
    draw.text((PAD+14, TOP+8), "백로그 구성  $110.6M", font=bold(15), fill=CYAN)
    draw.line([(PAD+14, TOP+30),(DIV-PAD-8, TOP+30)], fill=DARK_GRAY, width=1)

    segs = [
        ("어셈블리·카메라",       "$75M",  "68%", GREEN),
        ("Counter-UAS / SUADS",  "$30M",  "27%", AMBER),
        ("렌즈 컴포넌트·서비스", " $5M",   "5%",  GRAY),
    ]
    sy = TOP + 38
    for label, amt, pct, color in segs:
        bar_w = int((DIV - PAD*2 - 28) * int(pct.rstrip('%')) / 100)
        draw.rounded_rectangle([PAD+14, sy+2, PAD+14+bar_w, sy+16], radius=3, fill=(*color[:3], 60))
        draw.text((PAD+14, sy), label, font=font(13), fill=GRAY)
        draw.text((DIV-PAD-80, sy), amt,  font=bold(13), fill=color)
        draw.text((DIV-PAD-28, sy), pct,  font=bold(13), fill=color)
        sy += 24

    # 확정 백로그 리스트
    box(draw, PAD, TOP+114, DIV-PAD, BOT, (12,20,16), outline=GREEN)
    draw.rectangle([PAD, TOP+114, PAD+4, BOT], fill=GREEN)
    draw.text((PAD+14, TOP+122), "확정 백로그", font=bold(15), fill=GREEN)
    draw.line([(PAD+14, TOP+144),(DIV-PAD-8, TOP+144)], fill=DARK_GRAY, width=1)

    confirmed = [
        (GREEN,  "SPEIR",              "해군 파노라믹 열화상  /  L3Harris→G5→해군",   "연간 $10~20M 잠재  /  현재 분기 3~5%"),
        (AMBER,  "Counter-UAS/SUADS", "공군 드론 대응  /  탐지→식별→타격 광학",      "$30M 백로그  /  분기 기여 13~20%"),
        (BLUE,   "Tier-1 방산 PO",    "고객명 미공개 냉각형 카메라  /  2026년 분산", "$9.6M  /  분기 $2.4M (약 13%)"),
        (PURPLE, "공공안전 PO",       "소방·재난·경찰 추정  /  고객명 미공개",       "$4.8M  /  분기 $1.2M (약 6%)"),
    ]
    cy = TOP + 152
    for color, title, desc1, desc2 in confirmed:
        box(draw, PAD+10, cy, DIV-PAD-8, cy+64, (14,18,14))
        draw.rectangle([PAD+10, cy, PAD+14, cy+64], fill=color)
        draw.text((PAD+22, cy+6),  title, font=bold(14), fill=color)
        draw.text((PAD+22, cy+26), desc1, font=font(12), fill=GRAY)
        draw.text((PAD+22, cy+44), desc2, font=bold(12), fill=WHITE)
        cy += 70

    # ══════════════════════
    # 오른쪽 — 미확정 + NGSRI + 경향성
    # ══════════════════════
    RX = DIV + PAD

    # 미확정 포지션 박스
    box(draw, RX, TOP, W-PAD, TOP+220, (20,16,12), outline=AMBER)
    draw.rectangle([RX, TOP, RX+4, TOP+220], fill=AMBER)
    draw.text((RX+14, TOP+8), "공급 포지션 — 확정 PO 미공시", font=bold(15), fill=AMBER)
    draw.line([(RX+14, TOP+30),(W-PAD-8, TOP+30)], fill=DARK_GRAY, width=1)

    pending = [
        ("Border Surveillance", "DHS 예산 배정 대기 중  /  배정 후 PO 공시 예상"),
        ("Apache AH-64",        "납품 완료  /  예산 배정 대기 중 (Q3 콜 언급)"),
        ("미공개 항공 시스템",  "자격인증 완료  /  여름말~초가을 수주 예상"),
        ("유럽 방산 고객",      "BlackDiamond 초도 발주  /  NATO 공급망 첫 진입"),
    ]
    py = TOP + 38
    for title, desc in pending:
        draw.text((RX+14, py),    f"· {title}", font=bold(13), fill=AMBER)
        draw.text((RX+14, py+18), f"  {desc}",  font=font(12), fill=GRAY)
        py += 46

    # NGSRI 박스
    box(draw, RX, TOP+226, W-PAD, TOP+404, (16,12,26), outline=PURPLE)
    draw.rectangle([RX, TOP+226, RX+4, TOP+404], fill=PURPLE)
    draw.text((RX+14, TOP+234), "NGSRI — 아직 백로그에 없는 숫자", font=bold(15), fill=PURPLE)
    draw.line([(RX+14, TOP+256),(W-PAD-8, TOP+256)], fill=DARK_GRAY, width=1)

    draw.text((RX+14, TOP+264), "스팅어 10만발 교체  /  LM vs Raytheon 경쟁", font=font(13), fill=WHITE)
    draw.text((RX+14, TOP+284), "VISIMID(LPTH 자회사, 2023.07 인수) → LM팀 광학헤드", font=font(13), fill=GRAY)
    draw.text((RX+14, TOP+310), "잠재 규모", font=font(12), fill=GRAY)
    draw.text((RX+100, TOP+310), "연간 최대 $100M", font=bold(14), fill=PURPLE)
    draw.text((RX+14, TOP+332), "선정 시기", font=font(12), fill=GRAY)
    draw.text((RX+100, TOP+332), "FY2028 (아직 백로그 미포함)", font=bold(13), fill=GRAY)

    draw.line([(RX+14, TOP+354),(W-PAD-8, TOP+354)], fill=DARK_GRAY, width=1)
    draw.text((RX+14, TOP+360), "LM  2026.01 비행시험 ✓  /  2026.04 조립시연 ✓", font=font(13), fill=GREEN)
    draw.text((RX+14, TOP+380), "RTX  2026.02 탄도시험 ✓  /  비행시험 미완",     font=font(13), fill=RED)

    # 경향성 박스
    box(draw, RX, TOP+410, W-PAD, BOT, (12,18,22), outline=CYAN)
    draw.rectangle([RX, TOP+410, RX+4, BOT], fill=CYAN)
    draw.text((RX+14, TOP+418), "백로그 경향성", font=bold(15), fill=CYAN)
    draw.line([(RX+14, TOP+440),(W-PAD-8, TOP+440)], fill=DARK_GRAY, width=1)

    trends = [
        "해군 현대화  ·  Counter-UAS  ·  국경 광학  ·  NATO",
        "→ 전부 미 국방 예산이 집중되는 방향",
        "BlackDiamond 소재가 수요처를 먼저 만들었다",
        "SPEIR 풀레이트 전환 = 첫 번째 변곡점",
    ]
    ty = TOP + 448
    for i, t in enumerate(trends):
        color = WHITE if i < 2 else GRAY
        if i == 3: color = CYAN
        draw.text((RX+14, ty), t, font=font(13) if i != 1 else bold(13), fill=color)
        ty += 22

    footer(draw, "2026.06.12  LPTH 백로그 해부", "$LPTH  ·  FY2026 Q3  ·  개인 공부 기록")

    out = os.path.join(OUT_DIR, "2026-06-12_LPTH_백로그해부.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
