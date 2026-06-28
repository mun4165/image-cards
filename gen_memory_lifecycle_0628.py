from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-28"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,22), "D램값 98% 폭등이 내 삶에 오는 경로", font=bold(36), fill=ACCENT)
draw.text((32,74), "물가·금리엔 소폭, 투자 신호로는 키스톤", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

# 핵심 메시지 박스
ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "생활비 걱정 → 추적 가능한 트리거로", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "막연한 고점 공포를 'HBM 수요' 하나로 좁힌다", font=bold(24), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "1단계 · 내 지갑",
     "전자제품값 ↑ (점진적)", "노트북·폰·SSD·서버·전장 · 원가 일부라 체감은 부분적")
band(by+step, bh, BLUE, (12,20,38), "2~3단계 · 거시",
     "물가·금리엔 제한적", "단일 공급쇼크 → 헤드라인 CPI·연준 경로 좌우 못 함")
band(by+step*2, bh, ORANGE, (38,24,8), "진짜 신호 · 키스톤",
     "HBM이 공급을 빨아들임", "일반 D램 생산 잠식 = 타이트의 원인 · 수요만 보면 됨")

gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "하이닉스·삼성 어닝 3체크 (숫자 가이던스 대신)", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "① 비트그로스 가이던스   ② Capex 방향(삼성 규율)   ③ HBM 완판·HBM4 램프",
          font=bold(20), fill=CYAN)
draw.text((52,gy+74), "한국 기업은 미국식 매출·이익 가이던스를 안 준다 — 이 세 줄이 더 중요",
          font=font(15), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.28  |  메모리값 인상 — 지갑엔 소폭, 포트폴리오엔 큰 신호. SK하이닉스 2Q 7/29 예정", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-28_메모리_생활경로_어닝3체크.png")
img.save(out); print("Saved:", out)
