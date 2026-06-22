from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-22"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

def base(accent):
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): d.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): d.line([(0,y),(W,y)], fill=GRID, width=1)
    d.rectangle([0,0,W,4], fill=accent); d.rectangle([0,0,4,H], fill=accent)
    return img, d

def footer(d, txt):
    d.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    d.text((32,H-22), txt, font=font(15), fill=GRAY)

# ===== 카드 1 — 버핏 복제 (서평) =====
img, d = base(GREEN)
d.text((32,22), "버핏의 종목을 따라 사면 안 되는 이유", font=bold(38), fill=GREEN)
d.text((32,78), "복제할 것은 종목이 아니라, 가치를 정의하는 행위다", font=bold(22), fill=GRAY)
d.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

# 좌 박스 — 따라 사기
LX0, RX0 = 50, 660
BOXW = 570
d.rounded_rectangle([LX0,156,LX0+BOXW,560], radius=10, fill=(34,16,16))
d.text((LX0+24,176), "✕  따라 사기 = 부분 복제", font=bold(24), fill=RED)
left = [
    "결과만 베끼고 과정은 건너뛴다",
    "재현성이 없다",
    "다음 종목은 또 남에게 의존한다",
]
for i,t in enumerate(left):
    d.text((LX0+24,234+i*52), "·  "+t, font=font(21), fill=WHITE)
d.line([(LX0+24,406),(LX0+BOXW-24,406)], fill=DARK_GRAY, width=1)
d.text((LX0+24,430), "= 물고기 한 마리를", font=bold(24), fill=RED)
d.text((LX0+24,470), "   얻는 것", font=bold(24), fill=RED)

# 우 박스 — 기준 세우기
d.rounded_rectangle([RX0,156,RX0+BOXW,560], radius=10, fill=(8,32,26))
d.text((RX0+24,176), "○  기준 세우기 = 입법 행위", font=bold(24), fill=GREEN)
right = [
    "무엇이 좋은 기업인가를 스스로 정의",
    "어떤 가격이면 싼가를 스스로 결정",
    "종목이 바뀌어도 같은 잣대로 작동",
]
for i,t in enumerate(right):
    d.text((RX0+24,234+i*52), "·  "+t, font=font(20), fill=WHITE)
d.line([(RX0+24,406),(RX0+BOXW-24,406)], fill=DARK_GRAY, width=1)
d.text((RX0+24,430), "= 낚시를", font=bold(24), fill=GREEN)
d.text((RX0+24,470), "   배우는 것", font=bold(24), fill=GREEN)

by = 588
d.rounded_rectangle([32,by,W-32,by+62], radius=8, fill=(8,32,26))
d.text((50,by+10), "진짜 주인은 무엇을 살지 남에게 묻지 않고,", font=bold(21), fill=GREEN)
d.text((50,by+37), "스스로 정한 기준에 묻는다", font=bold(21), fill=GREEN)
footer(d, "2026.06.22  |  서평 · 투자자의 마음")
out1 = os.path.join(OUT_DIR, "2026-06-22_서평_버핏복제.png")
img.save(out1); print("Saved:", out1)

# ===== 카드 2 — 두 종류의 비쌈 (MU vs RKLB) =====
img, d = base(CYAN)
d.text((32,22), "비싼 주식에도 두 종류가 있다", font=bold(40), fill=CYAN)
d.text((32,80), "같은 '비싸다'라도 깨지는 방식이 다르다 — Micron vs Rocket Lab", font=bold(22), fill=GRAY)
d.line([(32,124),(W-32,124)], fill=DARK_GRAY, width=1)

MIDX = 648
d.line([(MIDX,158),(MIDX,556)], fill=DARK_GRAY, width=1)

# 좌 — A형 Micron
d.text((50,160), "A형 · Micron", font=bold(28), fill=BLUE)
d.text((50,200), "주가매출비율(PSR) 약 15배", font=bold(19), fill=GRAY)
rowsA = [
    ("무엇에 거나", "지금 실제로 찍히는 매출·이익"),
    ("베팅 대상", "AI 메모리 호황의 '지속성'"),
    ("깨지면", "숫자로 — 다음 분기 실적·가이던스"),
    ("추적 도구", "채점표 (매분기 마진 확인)"),
]
for i,(k,v) in enumerate(rowsA):
    y = 250+i*72
    d.text((50,y), k, font=bold(19), fill=BLUE)
    d.text((50,y+26), v, font=font(19), fill=WHITE)

# 우 — B형 Rocket Lab
RX = 684
d.text((RX,160), "B형 · Rocket Lab", font=bold(28), fill=AMBER)
d.text((RX,200), "주가매출비율(PSR) 약 75배+", font=bold(19), fill=GRAY)
rowsB = [
    ("무엇에 거나", "아직 일어나지 않은 미래"),
    ("베팅 대상", "Neutron 성공 · 플랫폼 전환"),
    ("깨지면", "시간으로 — 발사 지연·실패 시점"),
    ("추적 도구", "달력 (사건 시점 추적)"),
]
for i,(k,v) in enumerate(rowsB):
    y = 250+i*72
    d.text((RX,y), k, font=bold(19), fill=AMBER)
    d.text((RX,y+26), v, font=font(19), fill=WHITE)

by = 580
d.rounded_rectangle([32,by,W-32,by+62], radius=8, fill=(8,30,36))
d.text((50,by+10), "전자는 숫자로 깨지고, 후자는 시간으로 깨진다", font=bold(21), fill=CYAN)
d.text((50,by+38), "같은 '비싸다'를 같은 방식으로 보면 한쪽은 반드시 놓친다", font=font(16), fill=GRAY)
footer(d, "2026.06.22  |  Micron vs Rocket Lab")
out2 = os.path.join(OUT_DIR, "2026-06-22_두종류의비쌈_MU_RKLB.png")
img.save(out2); print("Saved:", out2)
