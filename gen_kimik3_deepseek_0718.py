from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-18"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(239,68,68)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "KIMI K3  문샷AI 오픈웨이트 모델 공개", font=bold(22), fill=GRAY)
draw.text((32,58), "딥시크 모먼트, 재현일까 재현이 아닐까", font=bold(28), fill=ACCENT)
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
band(by, bh, CYAN, (10,28,32), "성능",
     "Artificial Analysis 3위 — Fable 5·GPT-5.6 Sol 다음",
     "매개변수 약 2.7조~2.8조 개, 오픈웨이트 역대 최대",
     "코딩·에이전트 일부 벤치마크는 Opus 4.8 상회")
band(by+step, bh, ORANGE, (36,24,10), "구동 조건",
     "로컬 구동 사실상 불가 — \"서버랙 한 줄\"",
     "풀정밀도 약 1.7TB, 최소 양자화도 650GB 이상",
     "소비자용 기기는 어느 것도 자격이 안 된다(Modemguides)")
band(by+step*2, bh, RED, (36,14,14), "시장 반응",
     "7/17 엔비디아 -2.21% TSMC -2.77% SMH -2.18%",
     "골드만삭스 \"컴퓨트 확장 시대 끝났을 수 있다\"",
     "단, K3는 구동비용 더 비싼 모델 — 딥시크와 반대 방향")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.18  |  Kimi K3  Moonshot AI", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-18_KIMIK3_딥시크모먼트비교.png")
img.save(out); print("Saved:", out)
