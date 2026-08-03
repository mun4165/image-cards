from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-28"
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
    draw.text((60, y+14), label, font=bold(17), fill=color)
    draw.line([(272,y+14),(272,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((296, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((296, y+46), detail, font=font(15), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# ── RKLB × Eutelsat: 확정 물량과 옵션 분리 ────────────
img, draw = base_canvas(CYAN)
draw.text((32,22), "RKLB 유텔샛 528기, 실제로 받은 건 100기분", font=bold(28), fill=CYAN)
draw.text((32,74), "GEO방송 유텔샛 + LEO 원웹 합병사 · 확정은 패널 200장뿐", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = 124, 98, 111
band(draw, by, bh, BLUE, (10,20,40), "구조  |  GEO+LEO 합병사",
     "유텔샛=GEO 방송(채널 6,500개+) · 2023.9 원웹(LEO) 합병", "528기는 원웹과 별도로 신설하는 3세대 LEO망")
band(draw, by+step, bh, GREEN, (10,30,22), "확정  |  위성 100기",
     "태양광 패널 200장 · 약 80kW · 앨버커키 생산", "2025.03.12 Airbus 발주, 계약금액은 미공시")
band(draw, by+step*2, bh, AMBER, (40,28,10), "미확인  |  추가 340기",
     "2026.01.12 발주, 인도 개시는 2026년 말", "440기 총 22억유로는 위성 전체 제조비, RKLB 몫 아님")
band(draw, by+step*3, bh, ORANGE, (44,20,10), "신청 단계  |  528기",
     "FCC 신청, 고도 1,220km · 제조사 미정", "원웹과 궤도·주파수 분리 운용, 발사일정도 미정")
band(draw, by+step*4, bh, RED, (42,14,16), "자금  |  440기에만 3차례",
     "증자 8.28억 + 6.7억 + 수출신용 9.75억 유로", "조달액이 440기 규모에 부합, 528기는 자금 미확인")
footer(draw, "2026.07.28  |  $RKLB  Rocket Lab × Eutelsat")
out = os.path.join(OUT_DIR, "2026-07-28_RKLB_유텔샛528기_확정과옵션.png")
img.save(out); print("Saved:", out)
