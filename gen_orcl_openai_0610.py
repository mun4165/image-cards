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
    draw.text((W-500,H-30), right, font=bold(16), fill=ACCENT)

def arrow(draw, x1, y1, x2, y2, color, width=2):
    draw.line([(x1,y1),(x2,y2)], fill=color, width=width)
    # arrowhead
    draw.polygon([(x2,y2),(x2-8,y2-5),(x2-8,y2+5)], fill=color)

def make_main():
    img, draw = make_base()

    # ── 헤더 ──
    draw.rectangle([0, 4, W, 56], fill=(12, 16, 28))
    draw.text((16, 10), "ORCL  오라클 실적에서 OpenAI까지", font=bold(32), fill=WHITE)
    draw.text((16, 46), "AI 인프라 먹이사슬  —  2026.06.10  장 마감 후 발표  /  OpenAI S-1  6.08 제출", font=font(15), fill=GRAY)
    draw.line([(0,56),(W,56)], fill=DARK_GRAY, width=1)

    # ── 체인 노드 (5개, 가로) ──
    CHAIN_Y = 100
    NODE_H  = 88
    nodes = [
        (BLUE,   "ORCL",        "-7%",        "주가 하락"),
        (RED,    "Capex",       "$70B",       "FY2027 가이던스"),
        (AMBER,  "Stargate",    "$300B",      "오라클이 버는 계약"),
        (PURPLE, "OpenAI",      "S-1  6.08",  "IPO 준비 중"),
        (GREEN,  "RPO",         "$638B",      "질이 달라진다"),
    ]
    n = len(nodes)
    total_w = W - 32
    node_w  = total_w // n
    nx_list = []

    for i, (color, label, val, sub) in enumerate(nodes):
        x1 = 16 + i * node_w
        x2 = x1 + node_w - 8
        nx_list.append((x1, x2))
        cx = (x1 + x2) // 2

        box(draw, x1, CHAIN_Y, x2, CHAIN_Y + NODE_H, (14,16,26), outline=color)
        draw.text((cx - len(label)*5, CHAIN_Y + 6), label, font=bold(14), fill=color)
        # center val
        tw = len(val) * 9
        draw.text((cx - tw//2, CHAIN_Y + 30), val, font=bold(22), fill=WHITE)
        draw.text((cx - len(sub)*4, CHAIN_Y + 60), sub, font=font(12), fill=GRAY)

        # 화살표
        if i < n - 1:
            ax = x2 + 4
            ay = CHAIN_Y + NODE_H // 2
            draw.text((ax, ay - 8), "→", font=bold(16), fill=DARK_GRAY)

    # ── 하단 2분할 ──
    PAD = 8
    TOP2 = CHAIN_Y + NODE_H + 12
    BOT  = H - 50
    DIV  = 630

    # ── 왼쪽: 오라클 팩트 ──
    box(draw, PAD, TOP2, DIV-PAD, BOT, (12,16,26))
    draw.rectangle([PAD, TOP2, PAD+4, BOT], fill=BLUE)
    draw.text((PAD+14, TOP2+8), "오라클 팩트", font=bold(16), fill=BLUE)

    orcl_rows = [
        ("Q4 매출",        "$19.2B",   "+21% YoY",              WHITE),
        ("OCI 클라우드",   "$5.8B",    "+93% YoY",              GREEN),
        ("RPO 수주잔고",   "$638B",    "+$85B 단일 분기",        GREEN),
        ("FY2026 Capex",   "$55.7B",   "가이던스 $50B 초과",     AMBER),
        ("FY2027 Capex",   "$70B",     "시장 예상 초과 → -7%",   RED),
        ("총 부채",        "$134.6B",  "D/E 344%  순부채 ~$95B", RED),
    ]
    ry = TOP2 + 42
    for label, val, note, color in orcl_rows:
        draw.text((PAD+14,  ry), label, font=font(13), fill=GRAY)
        draw.text((PAD+150, ry), val,   font=bold(16), fill=color)
        draw.text((PAD+295, ry), note,  font=font(12), fill=GRAY)
        ry += 32

    # BYOH 한줄 설명
    draw.line([(PAD+14, ry+2),(DIV-PAD-8, ry+2)], fill=DARK_GRAY, width=1)
    draw.text((PAD+14, ry+10), "BYOH — 고객 선불·GPU 공급 후 짓는 구조  수요 리스크 없음", font=font(13), fill=CYAN)

    # ── 오른쪽: OpenAI + 연결고리 ──
    RX = DIV + PAD
    box(draw, RX, TOP2, W-PAD, TOP2 + (BOT-TOP2)//2 - 4, (16,14,26))
    draw.rectangle([RX, TOP2, RX+4, TOP2 + (BOT-TOP2)//2 - 4], fill=PURPLE)
    draw.text((RX+14, TOP2+8), "OpenAI 재무 실상", font=bold(16), fill=PURPLE)

    openai_rows = [
        ("밸류에이션",  "$852B",      PURPLE),
        ("월 매출",     "$2B/월",     WHITE),
        ("월 지출",     "$2.44B+/월", RED),
        ("$1 벌 때",    "$1.22 지출", RED),
        ("IPO 예상",    "2026 Q3~Q4", AMBER),
    ]
    oy = TOP2 + 42
    for label, val, color in openai_rows:
        draw.text((RX+14,  oy), label, font=font(13), fill=GRAY)
        draw.text((RX+160, oy), val,   font=bold(15), fill=color)
        oy += 26

    # ── 연결고리 박스 ──
    CY = TOP2 + (BOT-TOP2)//2
    box(draw, RX, CY, W-PAD, BOT, (16,22,16), outline=GREEN)
    draw.text((RX+14, CY+8), "연결고리", font=bold(15), fill=GREEN)
    draw.line([(RX+14, CY+34),(W-PAD-8, CY+34)], fill=DARK_GRAY, width=1)

    chain_lines = [
        ("OpenAI IPO 성공",  "→  오라클 RPO $638B 현실화", GREEN),
        ("OpenAI IPO 지연",  "→  계약 이행 속도 둔화",      RED),
    ]
    cy2 = CY + 42
    for left, right, color in chain_lines:
        draw.text((RX+14, cy2), left,  font=bold(13), fill=color)
        draw.text((RX+160,cy2), right, font=font(13), fill=WHITE)
        cy2 += 26

    draw.text((RX+14, cy2+4),  "두 회사는 하나로 묶여있다", font=bold(14), fill=CYAN)
    draw.text((RX+14, cy2+30), "다음 확인 →  OpenAI S-1 공개  /  2026.09 Q1 FY2027", font=font(13), fill=GRAY)

    footer(draw, "2026.06.10  Oracle Q4 FY2026  ×  OpenAI S-1", "ORCL  ·  OpenAI  ·  Stargate  ·  RPO")

    out = os.path.join(OUT_DIR, "2026-06-10_ORCL_OpenAI_먹이사슬.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
