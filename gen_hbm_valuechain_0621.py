from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-21"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22)
ACCENT = GREEN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "HBM 밸류체인 지도", font=bold(40), fill=ACCENT)
draw.text((32,78), "메모리부터 적층 본딩·검사·테스트까지 — AI 메모리 사슬 8칸", font=bold(22), fill=GRAY)
draw.line([(32,120),(W-32,120)], fill=DARK_GRAY, width=1)

NODE_X = 70
rungs = [
    ("1  HBM 메모리 제조",     "SK하이닉스 62 · 마이크론 21 · 삼성 17",  TEAL),
    ("2  베이스 다이",         "TSMC · 삼성 · 마이크론(내재화)",          TEAL),
    ("3  적층 본딩 장비 · TC본더","한미 · ASMPT · BESI   ← 병목",          ORANGE),
    ("4  전공정 · 패키징 장비", "램리서치 · AMAT · KLA",                   BLUE),
    ("5  검사 · 계측",         "캠텍 · 온토 이노베이션",                  BLUE),
    ("6  테스트",              "어드반테스트 · 테러다인",                 BLUE),
    ("7  소재",                "엔테그리스 등",                           TEAL),
    ("8  최종 수요 · AI 가속기","엔비디아 · AMD",                          AMBER),
]
top, step = 162, 58
draw.line([(NODE_X, top),(NODE_X, top+step*(len(rungs)-1))], fill=DARK_GRAY, width=3)
for i,(head,sub,color) in enumerate(rungs):
    y = top + step*i
    hl = i in (0, 2)  # 메모리 제조 · 본딩 병목 강조
    r = 11 if hl else 8
    draw.ellipse([NODE_X-r,y-r,NODE_X+r,y+r], fill=color)
    if hl:
        draw.ellipse([NODE_X-r-5,y-r-5,NODE_X+r+5,y+r+5], outline=color, width=2)
    draw.text((NODE_X+34,y-13), head, font=bold(22), fill=WHITE)
    draw.text((520,y-11), sub, font=font(18), fill=color)

# 우측 표식
draw.text((W-235,150), "가장 큰 칸이", font=bold(16), fill=GRAY)
draw.text((W-235,174), "가장 안전한 칸은 아니다", font=bold(16), fill=TEAL)
draw.text((W-235,300), "▶ 대체 어려운 칸", font=bold(16), fill=ORANGE)
draw.text((W-235,324), "(본딩·검사)이 오래 간다", font=font(15), fill=GRAY)

# 하단 핵심 박스
by = 622
draw.rounded_rectangle([32,by,W-32,by+58], radius=8, fill=(8,32,24))
draw.text((50,by+9), "진짜 병목은 메모리 3사가 아니라 적층 본딩·검사 장비 칸이다", font=bold(20), fill=GREEN)
draw.text((50,by+34), "메모리는 점유율 싸움, 장비는 표준을 잡으면 오래 가는 자리", font=font(16), fill=GRAY)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.21  |  HBM Value Chain", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-21_HBM_밸류체인지도.png")
img.save(out); print("Saved:", out)
