from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-18"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(239,68,68)
ACCENT = RED

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "SIVE  2년치 실적 재작성", font=bold(22), fill=GRAY)
draw.text((32,58), "감사인, 계속기업 존속 의문 명시", font=bold(28), fill=ACCENT)
draw.line([(32,110),(W-32,110)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-14), label, font=bold(20), fill=color)
    draw.line([(280,y+16),(280,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((306, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((306, y+56), d1, font=font(16), fill=color)
    draw.text((306, y+84), d2, font=font(15), fill=GRAY)

by = 130; bh = 168; step = 186
band(by, bh, RED, (36,14,14), "재작성",
     "2024·2025 실적 PCAOB 기준 재작성",
     "2024 순손실 SEK 1.16억→1.84억으로 확대",
     "2분기 실적발표 8/27로 연기")
band(by+step, bh, RED, (36,14,14), "감사의견",
     "외부감사인 'going concern' 중대의문 표명",
     "52주 고점 대비 주가 -70%",
     "7월 증자+전환사채 강제전환에 이어 재작성까지")
band(by+step*2, bh, GREEN, (10,32,22), "반대 신호",
     "락업해제 3일 전 CEO 개인자금으로 자사주 매입",
     "이사회 의장 등도 동반 매입, 매도물량은 없었음",
     "단, CW레이저 병목 논지와는 별개 축의 리스크")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.18  |  SIVE  Sivers Restatement & Going Concern", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-18_SIVE_재무재작성계속기업의문.png")
img.save(out); print("Saved:", out)
