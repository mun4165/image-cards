from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-23"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

def base_canvas(accent):
    img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    draw.rectangle([0,0,W,4], fill=accent); draw.rectangle([0,0,4,H], fill=accent)
    return img, draw

def band(draw, y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(18), fill=color)
    draw.line([(228,y+14),(228,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((252, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((252, y+46), detail, font=font(15), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# ── TSLA 2분기 실적 + 스페이스X 합병 시그널 ──────────────────────────
img, draw = base_canvas(ORANGE)
draw.text((32,22), "테슬라 이익은 놓쳤는데, 스페이스X는 안 부인했다", font=bold(26), fill=ORANGE)
draw.text((32,76), "로보택시·옵티머스 지연, 그리고 머스크 제국의 결합", font=bold(18), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, RED, (40,16,14), "이익 미스",
     "비GAAP EPS 0.33달러, 컨센서스 0.53달러", "영업이익 -57%, FCF -10.9억 달러 적자전환")
band(draw, by+step, bh, AMBER, (40,28,10), "로보택시",
     "오스틴 사고율, 자체지표로 평균의 4배", "대규모 무감독 배치 FSD v15로 재연기")
band(draw, by+step*2, bh, CYAN, (8,28,34), "옵티머스",
     "생산라인 설치 중, 초기물량은 데이터수집용", "머스크 \"기존 공급망 자체가 없다\"")
band(draw, by+step*3, bh, ORANGE, (38,22,10), "스페이스X",
     "합병 질문에 \"오버랩이 커진다\", 부인 안함", "법무팀 \"프레임워크 협약 체결\" 확인")
footer(draw, "2026.07.23  |  Tesla · SpaceX · xAI")
out = os.path.join(OUT_DIR, "2026-07-23_TSLA_스페이스X합병시그널.png")
img.save(out); print("Saved:", out)
