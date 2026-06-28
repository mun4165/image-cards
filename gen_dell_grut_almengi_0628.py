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

draw.text((32,22), "그릇과 알맹이 — 부활 구조 읽는 법", font=bold(36), fill=ACCENT)
draw.text((32,74), "DELL이 30년 만에 다시 어닝 서프라이즈를 낸 구조", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "낡은 하드웨어 회사가 새 연산 수요의 '그릇'이 되어 부활", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "구조를 읽는 자는 다음 후보를, 못 읽는 자는 이미 오른 것을 쫓는다", font=bold(24), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "그릇 · 얇은 마진",
     "델·인텔·서버 OEM(위탁생산)", "연산 수요를 담는 물리적 그릇 · 대체 가능")
band(by+step, bh, ORANGE, (38,24,8), "알맹이 · 두꺼운 마진",
     "엔비디아 가속기(GPU)", "표준을 쥠 · 대체 불가 → 진짜 마진은 여기")
band(by+step*2, bh, BLUE, (12,20,38), "수요 보증인",
     "정부 + 하이퍼스케일러", "칩워 '군이 만든 시장'과 같은 초기 마중물 패턴")

gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "다음 종목 찾는 3질문 (사후 정당화가 아니라 선행 발굴)", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "① 처음인가 반복인가   ② 첫 주자인가 막차인가   ③ 그릇인가 알맹이인가",
          font=bold(20), fill=CYAN)
draw.text((52,gy+76), "같은 서사라도 밸류체인 위치와 진입 순번이 수익을 가른다",
          font=font(15), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.28  |  종목을 점이 아니라 반복되는 구조로 읽으면, 아직 가격에 안 들어간 다음 그릇이 보인다", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-28_DELL_그릇과알맹이_부활구조.png")
img.save(out); print("Saved:", out)
