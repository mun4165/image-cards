from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-21"
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

# ── RKLB HASTE $266M 확정계약 ──────────────────────────
img, draw = base_canvas(GREEN)
draw.text((32,22), "로켓랩, HASTE 2.66억달러 확정계약 단독 낙찰", font=bold(28), fill=GREEN)
draw.text((32,76), "오전 한도증액과 달리 실제 임무 배정, 발표 원문 기준 확인", font=bold(18), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, GREEN, (10,30,22), "계약 개요",
     "7/21 우주시스템사령부 발주, 3개사 경쟁서 낙찰", "확정고정가 계약, 총액 2.66억 달러")
band(draw, by+step, bh, CYAN, (8,28,34), "발사 규모",
     "확정 12회 + 옵션 6회, 최대 18회", "알래스카 퍼시픽 스페이스포트, 2028년말까지")
band(draw, by+step*2, bh, AMBER, (40,28,10), "매출인식은",
     "공시엔 방식 미명시, 발사서비스는 대부분 포인트인타임", "12회 분산발사면 매출도 26~28년 여러분기 분산 가능성")
band(draw, by+step*3, bh, BLUE, (10,20,40), "오전 소식과 구분",
     "NSSL 한도증액=자격확대, 이번=실제 배정", "최종 수요기관은 공시에 명시 안 됨")
footer(draw, "2026.07.21  |  RKLB")
out = os.path.join(OUT_DIR, "2026-07-21_RKLB_HASTE2.66억달러계약.png")
img.save(out); print("Saved:", out)
