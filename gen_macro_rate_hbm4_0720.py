from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-20"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "기준금리 2.75%로 인상, 사유에 반도체 경기 명시", font=bold(28), fill=ACCENT)
draw.text((32,74), "같은 주 HBM4 가격은 2027년 배 이상 전망", font=bold(22), fill=GRAY)
draw.line([(32,120),(W-32,120)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(22), fill=color)
    draw.line([(240,y+18),(240,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((268, y+20), headline, font=bold(22), fill=WHITE)
    draw.text((268, y+58), d1, font=font(17), fill=color)
    draw.text((268, y+88), d2, font=font(15), fill=GRAY)

by = 138; bh = 160; step = 178
band(by, bh, AMBER, (36,26,8), "통화정책",
     "한은 기준금리 2.50%→2.75%, 위원 7명 전원 찬성(7/16)",
     "\"반도체 경기 호조 파급, 수출·내수 견조한 개선\" 인상 사유 명시",
     "물가는 \"상당 기간 목표 상회\" 전망, 인상 기조 지속 시사")
band(by+step, bh, CYAN, (8,28,34), "HBM4 가격",
     "Gb당 2026년 하반기 ~$2 → 2027년 $4~5+ 전망",
     "디지타임스, 업계 소식통 인용 · 베라루빈 출시 앞두고 수요 확대",
     "생산주기 4~6개월·낮은 초기수율·웨이퍼 소모량 3배가 근거")
band(by+step*2, bh, GREEN, (10,28,18), "연결",
     "반도체 실적 파급이 거시지표(금리)에 직접 반영된 한 주",
     "HBM 가격↑ = 공급사 매출·마진에 유리하게 작용하는 구조",
     "가격 전망치는 소스마다 편차 큼, 확정 실적과 구분해서 볼 것")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.20  |  MACRO  한국은행·HBM4  |  구독자용", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-20_MACRO_기준금리인상_HBM4가격전망.png")
img.save(out); print("Saved:", out)
