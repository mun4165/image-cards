from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-09"
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

draw.text((32,24), "MU 마진 84.9%, D램이 기술주 실적 선행지표?", font=bold(30), fill=ACCENT)
draw.text((32,80), "정점 날짜는 단정 안 함 — 확인된 숫자와 체크포인트만", font=bold(22), fill=GRAY)
draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
    draw.line([(250,y+18),(250,y+h-18)], fill=DARK_GRAY, width=1)
    draw.text((278, y+22), headline, font=bold(25), fill=WHITE)
    draw.text((278, y+64), d1, font=font(19), fill=color)
    draw.text((278, y+96), d2, font=font(17), fill=GRAY)

by = 150; bh = 152; step = 170
band(by, bh, BLUE, (10,20,34), "확인된 실적",
     "마이크론 6/24 매출 415억달러, 마진 84.9% 사상 최고",
     "D램 고정거래가 4월 16달러 → 6월 21달러, 31.25% 상승(7/6 보도)",
     "두 지표 모두 D램익스체인지·마이크론 공식 발표 기준")
band(by+step, bh, RED, (40,15,15), "단정 안 함",
     "\"기술주 실적 정점 몇 년 몇 분기\" 식 계산은 원문 미확인",
     "사이클 평균 기간·바닥 시점 등 근거를 1차 자료로 못 찾음",
     "확인 안 된 날짜는 옮기지 않는다")
band(by+step*2, bh, CYAN, (8,28,34), "체크포인트 3",
     "D램익스체인지 월간가 · 삼성·하이닉스 가이던스 · MU 다음분기",
     "삼성·하이닉스 2분기 실적 7월 말 발표",
     "MU 4분기 가이던스: 매출 500억달러·마진 약86%")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.09  |  MU  Micron / DRAM", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-09_MU_D램사이클선행지표.png")
img.save(out); print("Saved:", out)
