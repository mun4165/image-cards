from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-10"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (10, 11, 16)
GRID      = (255, 255, 255, 10)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (52, 56, 68)
AMBER     = (245, 158, 11)
GREEN     = (52, 211, 153)
BLUE      = (59, 130, 246)
PURPLE    = (167, 139, 250)
RED       = (239, 68, 68)
CYAN      = (6, 182, 212)
ACCENT    = AMBER

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
    draw.text((W-520,   H-34), right, font=bold(17), fill=ACCENT)

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.text((60, 20), "이번 주 매크로 시퀀스 — CPI · PPI · SpaceX IPO · FOMC", font=bold(34), fill=WHITE)
    draw.text((60, 68), "닷새 안에 4개  ·  각각이 아니라 흐름으로 읽어야 한다", font=font(19), fill=AMBER)
    draw.line([(60, 104), (W-60, 104)], fill=DARK_GRAY, width=1)

    CTOP = 116
    CBOT = H - 60
    DIV  = 570

    # ── 왼쪽: 이벤트 타임라인 ──
    events = [
        (GREEN,  "V",  "6.10 오늘  21:30",  "5월 CPI 발표  —  완료",
                       "헤드라인 +4.2% (예상치)  ·  코어 MoM +0.2% (둔화)"),
        (BLUE,   " ",  "6.11 내일  21:30",  "5월 PPI 발표  —  대기 중",
                       "CPI 이어 코어 방향 확인  ·  FOMC 직전 마지막 물가"),
        (PURPLE, " ",  "6.11 내일  장중",   "SpaceX IPO 가격 확정",
                       "$1.75T 밸류  ·  우주섹터 수급 변동성"),
        (RED,    " ",  "6.18 목  새벽 3시", "FOMC 결과 + 점도표",
                       "워시 체제 첫 SEP  ·  연내 인하 횟수 중위값 확인"),
    ]

    item_h = (CBOT - CTOP - 4) // 4
    y = CTOP
    for color, check, date, title, sub in events:
        is_done = check == "V"
        bg_col = (14, 24, 16) if is_done else (16, 18, 26)
        draw.rounded_rectangle([60, y+4, DIV-20, y+item_h-4], radius=8, fill=bg_col)
        draw.rectangle([60, y+4, 66, y+item_h-4], fill=color)

        # 체크/미체크 뱃지
        badge_bg = (20, 40, 24) if is_done else (30, 30, 40)
        draw.rounded_rectangle([74, y+12, 108, y+34], radius=4, fill=badge_bg)
        badge_text = "완료" if is_done else "대기"
        draw.text((78, y+14), badge_text, font=font(13), fill=color)

        draw.text((118, y+10),  date,  font=font(14), fill=GRAY)
        draw.text((118, y+32),  title, font=bold(18), fill=color)
        draw.text((82,  y+60),  sub,   font=font(14), fill=WHITE if is_done else GRAY)
        y += item_h

    # ── 세로 구분선 ──
    draw.line([(DIV, 104), (DIV, CBOT)], fill=DARK_GRAY, width=1)

    # ── 오른쪽 ──
    RX = DIV + 22

    # CPI 실제 결과 박스
    draw.rounded_rectangle([RX, CTOP, W-60, CTOP+230], radius=8, fill=(14, 20, 14))
    draw.rounded_rectangle([RX, CTOP, W-60, CTOP+230], radius=8, outline=GREEN, width=1)
    draw.text((RX+16, CTOP+10), "5월 CPI  —  실제 결과", font=bold(17), fill=GREEN)

    cpi_rows = [
        ("헤드라인 YoY",  "+4.2%",   "예상치 정확히 일치",  AMBER),
        ("헤드라인 MoM",  "+0.5%",   "4월 +0.6%에서 둔화",  GREEN),
        ("코어 YoY",      "+2.9%",   "2025.09 이후 최고",    RED),
        ("코어 MoM",      "+0.2%",   "4월 +0.4%에서 급둔화", GREEN),
    ]
    ry = CTOP + 46
    for label, val, note, color in cpi_rows:
        draw.text((RX+16, ry),     label, font=font(14),  fill=GRAY)
        draw.text((RX+155, ry),    val,   font=bold(17),  fill=color)
        draw.text((RX+255, ry),    note,  font=font(13),  fill=GRAY)
        ry += 38

    # 해석 한줄
    draw.line([(RX+16, CTOP+198), (W-76, CTOP+198)], fill=DARK_GRAY, width=1)
    draw.text((RX+16, CTOP+206),
              "에너지가 MoM 상승분 60%+  ·  코어 MoM 둔화 = 방향은 잡혀간다",
              font=font(13), fill=GRAY)

    # FOMC 핵심 관전포인트 박스
    fy = CTOP + 244
    fb = CBOT - 4
    draw.rounded_rectangle([RX, fy, W-60, fb], radius=8, fill=(22, 12, 12))
    draw.rounded_rectangle([RX, fy, W-60, fb], radius=8, outline=RED, width=1)
    draw.text((RX+16, fy+10),  "FOMC 핵심 관전 포인트", font=bold(17), fill=RED)
    draw.text((RX+16, fy+44),  "점도표 연내 인하 중위값  :  2회 -> 1회 가능성", font=font(15), fill=WHITE)
    draw.text((RX+16, fy+72),  "3월 기준 2회  /  그 이후 CPI 3.8% -> 4.2% 상승", font=font(14), fill=GRAY)
    draw.text((RX+16, fy+100), "코어 MoM 둔화가 명분 축소 압력을 일부 상쇄",    font=font(14), fill=GRAY)
    draw.text((RX+16, fy+130), "6.18 새벽 3:00 KST",                             font=bold(15), fill=RED)

    footer(draw, "2026.06.10", "BLS CPI  ·  Fed FOMC Calendar  ·  SpaceX IPO")

    out = os.path.join(OUT_DIR, "2026-06-10_매크로시퀀스.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
