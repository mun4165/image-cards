from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-25"
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

# ── 삼성전자 브로드컴 2000억달러 계약 vs 같은날 주가 폭락 ────────────
img, draw = base_canvas(BLUE)
draw.text((32,22), "삼성 브로드컴 2000억달러 계약, 주가는 폭락", font=bold(30), fill=BLUE)
draw.text((32,76), "5년·2030년까지 메모리·파운드리 동맹, 같은 날 급락 이유는 따로 있다", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, BLUE, (10,18,34), "계약 규모",
     "2,000억달러 이상, 5년(2030년까지)", "7월24일 샌프란시스코 AI 서밋에서 발표")
band(draw, by+step, bh, TEAL, (8,28,28), "포함 기술",
     "2나노 이하 파운드리 + HBM4·HBM4E + 2.3D·2.5D 패키징", "설계-공정-패키징 원스톱 턴키 구조")
band(draw, by+step*2, bh, RED, (40,14,14), "같은 날 주가",
     "삼성전자 -7.59%, 249,500원 마감", "코스피 5%대 급락, SK하이닉스도 동반 -7%")
band(draw, by+step*3, bh, AMBER, (40,28,10), "급락 진짜 원인",
     "중동 지정학·유가급등 + 레버리지ETF 증거금 상향", "브로드컴 계약과는 무관, 시점만 겹친 것")
footer(draw, "2026.07.25  |  005930  Samsung Electronics x AVGO Broadcom")
out = os.path.join(OUT_DIR, "2026-07-25_삼성전자_브로드컴_계약.png")
img.save(out); print("Saved:", out)
