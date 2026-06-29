from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-29"
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

draw.text((32,22), "IREN, NBA 워리어스에 북미 최대 스폰서", font=bold(36), fill=ACCENT)
draw.text((32,74), "연 5천만 달러 — 농구 광고가 아니라 '이름표'를 산 것이다", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "IREN은 농구 팬에게 팔 물건이 없다 — 고객은 클라우드·AI 연구소", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "채굴주 → AI 인프라 기업으로 '재분류'를 노린 한 수", font=bold(24), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "노림수 1 · 재평가",
     "채굴주 이름표 갈아끼우기", "낮은 밸류에이션 탈출 → AI 인프라 멀티플로 re-rating")
band(by+step, bh, ORANGE, (38,24,8), "노림수 2 · 신뢰",
     "B2B 재무 체력 시그널", "5천만 달러 태울 체력 = 다년 인프라 맡겨도 되는 회사")
band(by+step*2, bh, BLUE, (12,20,38), "노림수 3 · 돈·사람",
     "자본조달 비용 ↓ + 인재", "반복 노출로 기관 인지도 · 베이에어리어 AI 채용 포석")

gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "확인 지점 — 광고는 인지도까지, 수주는 숫자가 증명한다", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "① 다음 분기 AI 클라우드 매출 비중   ② 확보 전력 중 AI 전환 비율(MW)",
          font=bold(20), fill=CYAN)
draw.text((52,gy+76), "인지도·재분류 효과는 확실 / 직접 수주 효과는 아직 미검증",
          font=font(15), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.29  |  거액 스폰서십을 볼 땐 '왜 저 돈을' 이 아니라 '무슨 이름표를 갈아끼우려는가' 를 묻는다", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-29_IREN_워리어스스폰서_재분류.png")
img.save(out); print("Saved:", out)
