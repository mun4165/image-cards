from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-23"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = AMBER

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "점도표는 매파로 뒤집혔는데, 의장은 점을 안 찍었다", font=bold(33), fill=ACCENT)
draw.text((32,72), "6월 FOMC — 금리는 동결, 점도표만 매파 전환", font=bold(20), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)

# 좌측 핵심 수치
def stat(y, label, value, vcolor, sub=""):
    draw.text((52, y), label, font=font(18), fill=GRAY)
    draw.text((52, y+28), value, font=bold(38), fill=vcolor)
    if sub:
        draw.text((54, y+78), sub, font=font(16), fill=GRAY)

stat(140, "기준금리", "3.50 ~ 3.75% 동결", WHITE)
stat(244, "점도표 인상 전망", "9명 (6명은 복수 인상)", AMBER, "3명 0.25%p · 5명 0.5%p")
stat(372, "2026 금리 중앙값", "3.8%", AMBER, "3월엔 인하를 그리던 그림")
stat(476, "연말 PCE 물가 전망", "3.6%", ORANGE, "3월 2.7% → 큰 폭 상향, 10년물 4.54%")

# 가운데 세로 구분선
draw.line([(630,134),(630,600)], fill=DARK_GRAY, width=1)

# 우측 패널 — 의장의 침묵
draw.rounded_rectangle([658,134,W-32,600], radius=12, fill=(32,25,12))
draw.rectangle([658,134,664,600], fill=AMBER)
draw.text((686,160), "그런데 의장은 점을 안 찍었다", font=bold(26), fill=AMBER)

# 인용 박스
draw.rounded_rectangle([686,214,W-56,330], radius=10, fill=(20,16,8))
draw.text((706,232), "“동료들에겐 전망 제출을 권했지만,", font=font(20), fill=WHITE)
draw.text((706,262), "나는 오랜 소신에 따라 내 전망은", font=font(20), fill=WHITE)
draw.text((706,292), "내놓지 않았다”  — Kevin Warsh", font=font(20), fill=WHITE)

# 해석
draw.text((686,356), "· 매파 점도표 = '나머지 위원들'의 그림", font=bold(20), fill=WHITE)
draw.text((686,392), "· 키를 쥔 의장은 자기 패를 안 깠다", font=bold(20), fill=WHITE)
draw.text((686,428), "· 헤드라인은 '매파 전환'이라 쓰지만", font=font(19), fill=GRAY)
draw.text((686,458), "  정확히는 '위원들은 매파, 의장은 침묵'", font=bold(20), fill=CYAN)
draw.text((686,512), "시장은 앞의 숫자에 놀라 빠졌지만,", font=font(19), fill=GRAY)
draw.text((686,542), "정작 의장은 아직 패를 까지 않았다.", font=bold(20), fill=AMBER)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.23  |  FOMC · 점도표(SEP)", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-23_연준점도표_워시침묵.png")
img.save(out); print("Saved:", out)
