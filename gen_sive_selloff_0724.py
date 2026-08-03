from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-24"
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

# ── SIVE 전거래일 -10.86%, 락업 공시는 며칠 전인데 뒤늦게 반영 ────────────
img, draw = base_canvas(RED)
draw.text((32,22), "SIVE 전거래일 10.86% 급락", font=bold(30), fill=RED)
draw.text((32,76), "락업·내부자 매도 공시는 7/21인데 며칠 뒤 뒤늦게 반영", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, RED, (40,14,14), "이번 거래일",
     "스톡홀름 33.66 SEK 마감, 전일比 -10.86%", "새 악재 아닌 기존 공시 물량이 시차 두고 소화")
band(draw, by+step, bh, AMBER, (40,28,10), "7/21 공시 재확인",
     "의장 바스타니 27.5만주 매도(+기부6만·증여7만)", "CEO 바툴야는 반대로 7만주 추가매수, 보유 454만76주")
band(draw, by+step*2, bh, CYAN, (8,28,34), "매도 후 잔여",
     "의장 잔여 38.1만주 + 임직원옵션 62.5만주 보유", "완전 정리 아닌 부분 매도, 스웨덴 금감원 신고 대상")
band(draw, by+step*3, bh, GREEN, (10,30,22), "다음 확인 지점",
     "매도 물량 소화 완료 여부, 8/27 2분기 실적 매출반등", "락업발 수급 vs 실적 펀더멘털 구분해서 볼 것")
footer(draw, "2026.07.24  |  SIVE")
out = os.path.join(OUT_DIR, "2026-07-24_SIVE_전거래일11퍼센트급락.png")
img.save(out); print("Saved:", out)
