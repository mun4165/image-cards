from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-29"
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
    draw.line([(268,y+14),(268,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((292, y+15), headline, font=bold(18), fill=WHITE)
    draw.text((292, y+45), detail, font=font(14), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# ── SK하이닉스 사상 최대 실적 vs 이틀 연속 서킷브레이커 ────
img, draw = base_canvas(RED)
draw.text((32,22), "사상 최대 실적 낸 날, 코스피는 이틀 연속 서킷브레이커", font=bold(25), fill=RED)
draw.text((32,74), "SK하이닉스 영업이익 +557%인데 주가는 -12.52%", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = 124, 106, 119
band(draw, by, bh, RED, (40,14,14), "7/28  |  1일차",
     "코스피 -10.84%(6,023) · 삼성전자 -13.39% · 하이닉스 -14.65%", "삼성전자 거의 20년 만의 최악 하루 낙폭")
band(draw, by+step, bh, ORANGE, (44,20,10), "7/29  |  2일차",
     "코스피 -5.98%(5,663) · 삼성전자 -7.84% · 하이닉스 -12.52%", "장중 +3.40%→-12.63% 급변, 매도사이드카+서킷브레이커 재발동")
band(draw, by+step*2, bh, GREEN, (10,30,22), "실적  |  역대 최대",
     "영업이익 60.5조원(+557.2%) · 매출 79.3조원(+256.8%)", "작년 한 해 영업이익(47.2조)을 이미 넘어선 분기 실적")
band(draw, by+step*3, bh, AMBER, (40,28,10), "괴리  |  기대치는 하회",
     "시장 예상 영업이익 64.1조원 대비 약 5.6% 낮게 발표", "역대 최대 실적 + 컨센서스 하회, 두 가지가 동시에 성립")
band(draw, by+step*4, bh, BLUE, (10,20,40), "배경  |  업종 전체 조정",
     "AI인프라 자금조달 우려 · 밸류에이션 재평가 · 중국 경쟁", "삼성전자도 실적발표 전인데 동반 낙폭, 개별기업 이슈 아님")
footer(draw, "2026.07.29  |  $SKHY  SK하이닉스 · 삼성전자")
out = os.path.join(OUT_DIR, "2026-07-29_SKHY_사상최대실적_이틀연속서킷브레이커.png")
img.save(out); print("Saved:", out)
