from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-27"
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

# ── 키옥시아 폭락과 SK하이닉스 2대주주, 무슨 관계인가 ──────────
img, draw = base_canvas(CYAN)
draw.text((32,22), "키옥시아 폭락과 SK하이닉스 2대주주, 무슨 관계", font=bold(25), fill=CYAN)
draw.text((32,74), "시차 열흘, 원문 어디에도 인과관계는 없다", font=bold(19), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)
by, bh, step = 134, 128, 142
band(draw, by, bh, RED, (40,14,14), "키옥시아 폭락",
     "6/22 고점 대비 7/17까지 -52%, 원인은 특허소송 패소+메모리 조정", "7월 16~17일, SK하이닉스와 무관한 별개 사건")
band(draw, by+step, bh, AMBER, (40,28,10), "SK하이닉스 지분",
     "2018년 도시바메모리 인수 때 3950억엔 CB로 이미 보유, 의결권 없음", "새로 생긴 지분 아님, 15% 상한 합의 유효")
band(draw, by+step*2, bh, CYAN, (8,28,34), "7/26 바뀐 것",
     "베인캐피털 지분 매각(2.5조엔 회수)으로 SPC가 2대주주(14.17%)로 부상", "도시바(16.1%)와 격차 1.93%p, 순위만 재배열")
band(draw, by+step*3, bh, GREEN, (10,30,22), "다음 확인 지점",
     "도시바 추가매각 시 최대주주 전환 여부, CB 주식전환·경쟁당국 심사", "의결권 확보 전까지는 지분 순위 이슈에 그침")
footer(draw, "2026.07.27  |  SK하이닉스 · 키옥시아  |  지분구조 팩트체크")
out = os.path.join(OUT_DIR, "2026-07-27_SKHY_키옥시아_2대주주_팩트체크.png")
img.save(out); print("Saved:", out)
