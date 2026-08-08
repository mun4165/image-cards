from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-08-08"
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
    draw.line([(360,y+14),(360,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((384, y+15), headline, font=bold(18), fill=WHITE)
    draw.text((384, y+45), detail, font=font(14), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

BY, BH, STEP = 122, 98, 110

img, draw = base_canvas(CYAN)
draw.text((32,22), "AAOI·AXTI, 중국산 광트랜시버 수입금지 검토에 함께 올랐다", font=bold(24), fill=CYAN)
draw.text((32,74), "완제품과 소재, 다른 트리거로 같은 날 급등", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, AMBER, (44,32,10), "뉴스  |  FCC 초안, 8/4 로이터 단독",
     "중국산 신형 광트랜시버 수입 금지 추진, 기존 물량은 제외", "올해 안 공표·시행 목표, 아직 초안 단계")
band(draw, by+step, bh, GREEN, (10,30,22), "AAOI  |  8/7 +9.19%, $135.63",
     "완제품(트랜시버) 단에서 중국 경쟁자 직접 대체 수혜", "8/6 실적 매출 YoY +86%, GAAP 손실은 확대")
band(draw, by+step*2, bh, BLUE, (10,20,40), "AXTI  |  8/7 +17.84%, $88.58",
     "소재(인듐인화물) 공급자, 1차 트리거는 7/30 실적 서프라이즈", "매출 컨센 37~40% 상회, 백로그 $1억+ 유지")
band(draw, by+step*3, bh, ORANGE, (44,20,10), "공급망 역설  |  대체재도 중국 인듐 필요",
     "이노라이트+이옵토링크 800G+ 시장 60%+ 점유", "서방 대체 램프업 12~24개월, InP 가격 250%↑(2025)")
band(draw, by+step*4, bh, TEAL, (10,32,30), "watch  |  정식 입법예고·시행일",
     "규정 확정 시점과 중국의 대응(추가 수출통제 여부)", "AAOI·AXTI 급등은 실적·뉴스 중첩 구간 — 조정 가능성 상존")
footer(draw, "2026.08.08  |  AAOI·AXTI 중국산 광트랜시버 수입금지 검토")
out = os.path.join(OUT_DIR, "2026-08-08_AAOI_AXTI_FCC광트랜시버.png")
img.save(out); print("Saved:", out)
