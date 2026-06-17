from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-10"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (10, 13, 18)
GRID      = (255, 255, 255, 10)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (52, 58, 72)
CYAN      = (6, 182, 212)
GREEN     = (52, 211, 153)
BLUE      = (59, 130, 246)
AMBER     = (245, 158, 11)
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

def footer(draw, left, right):
    draw.line([(60, H-50), (W-60, H-50)], fill=DARK_GRAY, width=1)
    draw.text((60,      H-34), left,  font=font(17), fill=GRAY)
    draw.text((W-500,   H-34), right, font=bold(17), fill=ACCENT)

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.text((60, 20), "엔비디아 SVP와 루멘텀이 같은 날 말한 것", font=bold(36), fill=WHITE)
    draw.text((60, 70), "미즈호 테크 컨퍼런스  ·  CPO 타임라인 지연 없음  ·  두 회사 동시 확인", font=font(19), fill=CYAN)
    draw.line([(60, 106), (W-60, 106)], fill=DARK_GRAY, width=1)

    CTOP = 118
    CBOT = H - 60
    DIV  = 590

    # ── 왼쪽: NVDA + LITE 카드 ──
    MID = CTOP + (CBOT - CTOP) // 2

    # NVDA 카드
    draw.rounded_rectangle([60, CTOP+4, DIV-20, MID-8], radius=8, fill=(12, 22, 16))
    draw.rounded_rectangle([60, CTOP+4, DIV-20, MID-8], radius=8, outline=GREEN, width=1)
    draw.text((82, CTOP+14), "NVDA  엔비디아", font=bold(15), fill=GRAY)
    draw.text((82, CTOP+36), "CPO Scale-Out", font=bold(26), fill=GREEN)
    draw.line([(82, CTOP+72), (DIV-36, CTOP+72)], fill=DARK_GRAY, width=1)
    draw.text((82, CTOP+82),  "타임라인",  font=font(14), fill=GRAY)
    draw.text((200, CTOP+80), "2026 H2  양산 시작", font=bold(18), fill=WHITE)
    draw.text((82, CTOP+116), "지연 여부", font=font(14), fill=GRAY)
    draw.text((200, CTOP+114),"없음  —  SVP 직접 확인", font=bold(18), fill=GREEN)
    draw.text((82, CTOP+148), "서버-서버 사이  노드 간 광학 연결", font=font(14), fill=GRAY)

    # LITE 카드
    draw.rounded_rectangle([60, MID+4, DIV-20, CBOT-4], radius=8, fill=(12, 18, 28))
    draw.rounded_rectangle([60, MID+4, DIV-20, CBOT-4], radius=8, outline=BLUE, width=1)
    draw.text((82, MID+14), "LITE  루멘텀", font=bold(15), fill=GRAY)
    draw.text((82, MID+36), "CPO Scale-Up", font=bold(26), fill=BLUE)
    draw.line([(82, MID+72), (DIV-36, MID+72)], fill=DARK_GRAY, width=1)
    draw.text((82, MID+82),  "출하 시작", font=font(14), fill=GRAY)
    draw.text((200, MID+80), "2027 H2", font=bold(18), fill=WHITE)
    draw.text((82, MID+116), "본격 램프", font=font(14), fill=GRAY)
    draw.text((200, MID+114),"2028", font=bold(18), fill=WHITE)
    draw.text((82, MID+148), "이전 타임라인 대비 지연 없음  —  경영진 확인", font=font(14), fill=BLUE)

    # ── 세로 구분선 ──
    draw.line([(DIV, 106), (DIV, CBOT)], fill=DARK_GRAY, width=1)

    # ── 오른쪽 ──
    RX = DIV + 22

    # Scale 구분 박스
    draw.text((RX, CTOP), "두 제품은 다르다", font=bold(19), fill=GRAY)

    rows = [
        ("Scale-Out", "노드 간  (서버 ↔ 서버)", "H2 2026", GREEN),
        ("Scale-Up",  "노드 내  (칩 ↔ 광 직접)", "H2 2027~2028", BLUE),
    ]
    sy = CTOP + 34
    for title, desc, timeline, color in rows:
        draw.rounded_rectangle([RX, sy, W-60, sy+72], radius=7, fill=(16, 20, 28))
        draw.rectangle([RX, sy, RX+5, sy+72], fill=color)
        draw.text((RX+18, sy+8),  title,    font=bold(18), fill=color)
        draw.text((RX+18, sy+36), desc,     font=font(14), fill=WHITE)
        draw.text((RX+18, sy+56), timeline, font=bold(14), fill=GRAY)
        sy += 82

    # 핵심 메시지 박스
    my = sy + 10
    mb = CBOT - 4
    draw.rounded_rectangle([RX, my, W-60, mb], radius=8, fill=(18, 20, 30))
    draw.rounded_rectangle([RX, my, W-60, mb], radius=8, outline=CYAN, width=1)
    draw.text((RX+16, my+12), "오늘 발언의 의미", font=bold(17), fill=CYAN)
    draw.text((RX+16, my+46), "자사 타임라인을 가장 잘 아는 건", font=font(15), fill=GRAY)
    draw.text((RX+16, my+70), "그 회사 경영진이다", font=bold(18), fill=WHITE)
    draw.line([(RX+16, my+100), (W-76, my+100)], fill=DARK_GRAY, width=1)
    draw.text((RX+16, my+110), "두 회사 모두 TAM·기회에 강한 낙관론 표명", font=font(14), fill=GRAY)

    footer(draw, "2026.06.10  Mizuho Technology Conference", "NVDA  ·  LITE  ·  CPO")

    out = os.path.join(OUT_DIR, "2026-06-10_LITE_NVDA_CPO.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
