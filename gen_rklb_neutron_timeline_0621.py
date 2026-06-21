from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-21"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); RED=(239,68,68); ORANGE=(249,115,22)
ACCENT = BLUE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,18), "로켓랩 뉴트론, 왜 자꾸 미뤄지나", font=bold(38), fill=ACCENT)
draw.text((32,70), "첫 발사 일정 변천 — 2021년 약속부터 2026년 4분기까지", font=bold(23), fill=WHITE)
draw.text((32,104), "2024년 목표가 2년 넘게 밀렸고, 결정타는 1월 탱크 파열이었다", font=font(17), fill=GRAY)
draw.line([(32,138),(W-32,138)], fill=DARK_GRAY, width=1)

# 좌측 타임라인
NODE_X = 56
events = [
    ("2021.03", "뉴트론 공개 · 첫 발사 목표 \"2024\"",        "중형 재사용 로켓 프로그램 시작",        GRAY),
    ("2024",    "첫 아르키메데스 엔진 조립",                  "→ 일정 \"빨라야 2025년 중반\"으로",     BLUE),
    ("2025",    "목표 \"2025년 하반기\"",                     "발사장 LC-3 · 급수탑 · 인프라 진척",    CYAN),
    ("2025 말", "\"2026년 1분기 발사대 거치\"",                "발사일은 끝까지 미명시",                TEAL),
    ("2026.01.21","1단 탱크 수압시험 중 파열",                "한계 시험에서 예상보다 일찍 터짐",      RED),
    ("현재",    "첫 발사 \"빨라야 2026년 4분기\"",            "탱크를 자동제조로 전환 · 재인증",       AMBER),
]
top, step = 162, 86
# 세로 연결선
draw.line([(NODE_X, top+6),(NODE_X, top+step*(len(events)-1)+6)], fill=DARK_GRAY, width=3)
for i,(date,head,sub,color) in enumerate(events):
    y = top + step*i
    highlight = (color == RED)
    r = 13 if highlight else 9
    draw.ellipse([NODE_X-r,y+6-r,NODE_X+r,y+6+r], fill=color)
    if highlight:
        draw.ellipse([NODE_X-r-5,y+6-r-5,NODE_X+r+5,y+6+r+5], outline=color, width=2)
    tx = NODE_X+34
    draw.text((tx,y-6), date, font=bold(19), fill=color)
    draw.text((tx+138,y-4), head, font=bold(19), fill=WHITE)
    draw.text((tx+138,y+22), sub, font=font(16), fill=GRAY)

# 가운데 구분선
draw.line([(740,150),(740,H-58)], fill=DARK_GRAY, width=1)

# 우측 — 원인 / 현재 / 핵심
draw.text((764,160), "지연의 진짜 원인", font=bold(22), fill=WHITE)
draw.line([(764,192),(W-32,192)], fill=DARK_GRAY, width=1)
cause = [
    "설계 결함이 아니라 제조 결함",
    "하청 수작업 복합재 적층 과정에서",
    "구조상 중요한 이음매 강도가 부족",
]
y=204
for line in cause:
    draw.text((764,y), "·", font=bold(18), fill=RED)
    draw.text((782,y), line, font=font(18), fill=GRAY); y+=30

y+=16
draw.text((764,y), "지금 상태", font=bold(22), fill=WHITE); y+=34
draw.line([(764,y),(W-32,y)], fill=DARK_GRAY, width=1); y+=14
status = [
    (GREEN, "엔진 · 발사장", "스테니스 연소 시험 · LC-3 거의 완성"),
    (AMBER, "남은 건 탱크 하나", "새 탱크 강도·인증 시험 재진행 중"),
]
for color,title,desc in status:
    draw.rectangle([760,y+3,764,y+30], fill=color)
    draw.text((778,y), title, font=bold(19), fill=WHITE)
    draw.text((778,y+27), desc, font=font(16), fill=GRAY); y+=62

y+=8
draw.rounded_rectangle([764,y,W-32,y+66], radius=8, fill=(10,28,52))
draw.text((780,y+13), "봐야 할 건 화려한 수주 뉴스가 아니라", font=bold(18), fill=BLUE)
draw.text((780,y+38), "새 탱크의 한계 시험 통과 소식이다", font=bold(18), fill=BLUE)

# 푸터
draw.line([(32,H-44),(W-32,H-44)], fill=DARK_GRAY, width=1)
draw.text((32,H-30), "2026.06.21  |  RKLB · Neutron 첫 발사 일정 타임라인", font=font(16), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-21_RKLB_뉴트론타임라인.png")
img.save(out); print("Saved:", out)
