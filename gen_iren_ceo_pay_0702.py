from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-02"
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

draw.text((32,22), "IREN 공동대표, 호주 최고연봉이었다", font=bold(36), fill=ACCENT)
draw.text((32,80), "2025 회계연도 공시, 지금 다시 보는 이유", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

# 핵심 밴드 — 보상 규모
ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "FY 보상", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "1인당 $72M (96%가 주식)   ·   합산 $144M",
          font=bold(20), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, GREEN, (10,32,24), "①  구조는 공개",
     "테슬라식 마일스톤, SEC 위임장에 가격구간 공시", "기준가 $12.62 · 30일 평균가 7단계 · 2027.7 시한")
band(by+step, bh, ORANGE, (40,24,10), "②  걸리는 지점",
     "이사회, 원 설계 밖 outperformance 추가 지급", "각 240만 주 별도 부여(2025.5) — 트랜치 관대화 패턴")
band(by+step*2, bh, BLUE, (12,20,38), "③  시차 구분",
     "보상 2025.10 · 증자 2026.3 · 메타·SB는 이번 주", "세 뉴스는 동시 발생 아님 — 재조명 vs 신규 구분 필요")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.02  |  보상 공시 2025.10 · 출처 SEC DEF 14A, Bloomberg", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-02_IREN_보상안_호주최고연봉.png")
img.save(out); print("Saved:", out)
