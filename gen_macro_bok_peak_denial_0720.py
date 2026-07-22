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

draw.text((32,24), "한은, 국회 서면답변서 \"반도체 고점론\" 선그어", font=bold(27), fill=ACCENT)
draw.text((32,74), "지난주 기준금리 인상 사유와 같은 판단 재확인", font=bold(22), fill=GRAY)
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
band(by, bh, AMBER, (36,26,8), "한은 판단(7/13)",
     "\"AI 수요 급증, 공급 확대는 더디다\" — 박성훈 의원실 서면답변",
     "\"HBM 등 주문형 제품이 시장 주도, 공급확대 과거보다 제한적\"",
     "반도체 경기 \"상당 기간 확장세 이어갈 것\" 전망")
band(by+step, bh, CYAN, (8,28,34), "연결고리",
     "7/16 기준금리 인상 사유 \"반도체 경기 호조 파급\"과 동일 판단",
     "서로 다른 공식문서 2건에서 같은 진단 반복",
     "일회성 코멘트가 아니라 기관 차원의 지속 진단 신호")
band(by+step*2, bh, GREEN, (10,28,18), "시장",
     "SK하이닉스 ADR(SKHY) 7/17 종가 $154.03(+1.13%)",
     "7/10 상장 후 변동성 구간, 공모가 $149 대비 완만한 상승",
     "\"고점론\"과 \"장기호황론\"은 관점 차이 — 확정된 결과 아님")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.20  |  MACRO  한국은행·반도체고점론  |  구독자용", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-20_MACRO_한은반도체고점론.png")
img.save(out); print("Saved:", out)
