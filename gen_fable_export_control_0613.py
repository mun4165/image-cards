from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/이미지사용/2026-06-13"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG        = (10, 12, 18)
GRID      = (255, 255, 255, 10)
WHITE     = (255, 255, 255)
GRAY      = (140, 150, 165)
DARK_GRAY = (50, 56, 70)
RED       = (239, 68, 68)
AMBER     = (245, 158, 11)
CYAN      = (6, 182, 212)
GREEN     = (52, 211, 153)
ACCENT    = RED

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
    draw.rectangle([0, 4, W, 62], fill=(20, 10, 10))
    draw.text((16, 10), "미국이 AI 모델을 수출 통제했다", font=bold(30), fill=WHITE)
    draw.text((16, 46), "2026.06.12  미 상무부 → Anthropic 서한  /  Fable 5 · Mythos 5 전 세계 접근 차단", font=font(14), fill=GRAY)
    draw.line([(0,62),(W,62)], fill=DARK_GRAY, width=1)

    PAD = 8
    TOP = 68
    BOT = H - 52
    DIV = 580

    # ══════════════════
    # 왼쪽 — 무슨 일 + 차단 범위
    # ══════════════════

    # 사건 박스
    box(draw, PAD, TOP, DIV-PAD, TOP+200, (20,10,10), outline=RED)
    draw.rectangle([PAD, TOP, PAD+4, TOP+200], fill=RED)
    draw.text((PAD+14, TOP+10), "무슨 일이 있었나", font=bold(15), fill=RED)
    draw.line([(PAD+14, TOP+32),(DIV-PAD-8, TOP+32)], fill=DARK_GRAY, width=1)

    events = [
        ("트리거",   "어떤 회사가 Mythos 5 탈옥 → 취약점 발견 주장"),
        ("명령",     "미 상무장관 루트닉 → 앤트로픽 CEO 서한 발송"),
        ("근거",     "국가 안보 권한 발동"),
        ("앤트로픽", "\"오해\" 반박 + 명령에는 일단 따름"),
        ("실질효과", "외국인 실시간 구분 불가 → 사실상 전 세계 차단"),
    ]
    ey = TOP + 40
    for label, desc in events:
        draw.text((PAD+14, ey), f"{label}", font=bold(13), fill=AMBER)
        draw.text((PAD+14+80, ey), desc, font=font(13), fill=WHITE)
        ey += 30

    # 차단 범위 박스
    box(draw, PAD, TOP+206, DIV-PAD, BOT, (10,10,10), outline=DARK_GRAY)
    draw.rectangle([PAD, TOP+206, PAD+4, BOT], fill=DARK_GRAY)
    draw.text((PAD+14, TOP+214), "차단 범위", font=bold(15), fill=GRAY)
    draw.line([(PAD+14, TOP+236),(DIV-PAD-8, TOP+236)], fill=DARK_GRAY, width=1)

    box(draw, PAD+10, TOP+244, DIV-PAD-8, TOP+294, (30,10,10))
    draw.text((PAD+22, TOP+250), "차단", font=bold(14), fill=RED)
    draw.text((PAD+70, TOP+250), "Fable 5  ·  Mythos 5", font=bold(16), fill=WHITE)
    draw.text((PAD+22, TOP+274), "외국인 전원 (미국 내 외국인 직원 포함)", font=font(13), fill=GRAY)

    box(draw, PAD+10, TOP+302, DIV-PAD-8, TOP+352, (10,22,10))
    draw.text((PAD+22, TOP+308), "유지", font=bold(14), fill=GREEN)
    draw.text((PAD+70, TOP+308), "Sonnet  ·  Opus  ·  Haiku", font=bold(16), fill=WHITE)
    draw.text((PAD+22, TOP+332), "기존 라인업 영향 없음", font=font(13), fill=GRAY)

    # ══════════════════
    # 오른쪽 — 의미 + 선례
    # ══════════════════
    RX = DIV + PAD

    # 첫 번째 사례 박스
    box(draw, RX, TOP, W-PAD, TOP+140, (20,14,6), outline=AMBER)
    draw.rectangle([RX, TOP, RX+4, TOP+140], fill=AMBER)
    draw.text((RX+14, TOP+10), "왜 중요한가 — 선례가 생겼다", font=bold(15), fill=AMBER)
    draw.line([(RX+14, TOP+32),(W-PAD-8, TOP+32)], fill=DARK_GRAY, width=1)

    draw.text((RX+14, TOP+42),  "칩(H100) 수출 통제", font=font(13), fill=GRAY)
    draw.text((RX+14, TOP+62),  "↓", font=bold(16), fill=AMBER)
    draw.text((RX+14, TOP+82),  "모델 자체 수출 통제 — 최초 사례", font=bold(14), fill=WHITE)
    draw.text((RX+14, TOP+108), "하드웨어 → 소프트웨어로 통제 범위 확장", font=font(13), fill=GRAY)

    # 시사점 박스
    box(draw, RX, TOP+146, W-PAD, BOT, (10,14,20), outline=CYAN)
    draw.rectangle([RX, TOP+146, RX+4, BOT], fill=CYAN)
    draw.text((RX+14, TOP+154), "시사점", font=bold(15), fill=CYAN)
    draw.line([(RX+14, TOP+176),(W-PAD-8, TOP+176)], fill=DARK_GRAY, width=1)

    points = [
        "한 번 쓴 수단은 더 낮은 임계치로 또 쓸 수 있음",
        "GPT-5·Gemini Ultra도 같은 방식으로 차단 가능",
        "미국 모델 의존 국가 — 언제든 스위치 꺼질 수 있음",
        "→ 자국 AI 모델 개발 = 기술 주권의 문제",
    ]
    py = TOP + 184
    for i, pt in enumerate(points):
        color = CYAN if i == 3 else WHITE
        f = bold(13) if i == 3 else font(13)
        draw.text((RX+14, py), f"· {pt}", font=f, fill=color)
        py += 30

    footer(draw, "2026.06.13  AI 수출통제 분석", "Fable 5 · Mythos 5  ·  개인 공부 기록")

    out = os.path.join(OUT_DIR, "2026-06-13_Fable_수출통제.png")
    img.save(out)
    print(f"Saved: {out}")

make_main()
print("Done.")
