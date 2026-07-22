from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-18"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(239,68,68)
PURPLE=(168,85,247)
ACCENT = PURPLE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "META  앤트로픽에 컴퓨트를 판다?", font=bold(22), fill=GRAY)
draw.text((32,58), "$100억 논의, 아직 계약은 아니다", font=bold(28), fill=ACCENT)
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
band(by, bh, GREEN, (10,32,22), "확인된 보도",
     "NYT, 앤트로픽-메타 컴퓨트 리스 초기협상",
     "2년간 최대 $100억, 매달 분납",
     "양측 조기종료 조항 · 6월 앤트로픽 제안으로 시작")
band(by+step, bh, ORANGE, (40,26,10), "규모 비교",
     "스페이스X 딜(5월)=3년 $450억",
     "메타안 연환산 $50억 vs 스페이스X 연 $150억",
     "메타 2026 AI capex 최대 $1,450억")
band(by+step*2, bh, PURPLE, (26,14,38), "해석",
     "이 거래에서 메타=컴퓨트 판매자(공급자)",
     "뉴클라우드 고객 아니라 경쟁 공급자로 등판",
     "'모델 검증'보다 TAM 잠식 리스크로 읽힐 수 있음")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.18  |  META  Meta x Anthropic Compute Talks", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-18_META_앤트로픽컴퓨트리스.png")
img.save(out); print("Saved:", out)
