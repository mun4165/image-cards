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

draw.text((32,24), "#KimiK3  딥시크 모먼트 재현?", font=bold(22), fill=GRAY)
draw.text((32,58), "팩트체크 해봄", font=bold(28), fill=ACCENT)
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
band(by, bh, CYAN, (10,28,32), "딥시크 R1 (2025.1)",
     "충격 포인트 = 적은 자원으로 돌아간다",
     "엔비디아 하루만에 시총 5,900억 달러 증발(-17%대)",
     "컴퓨트 수요 감소 우려 → 실제론 이후 수요 더 늘어남")
band(by+step, bh, ORANGE, (36,24,10), "Kimi K3 (2026.7)",
     "충격 포인트 = 성능 추격 속도",
     "2.7~2.8조 매개변수, 로컬 구동 불가(최소 650GB+)",
     "돌리는 데 오히려 돈 더 듦 — 딥시크와 반대 방향")
band(by+step*2, bh, RED, (36,14,14), "7/17 시장 반응",
     "엔비디아 -2.21% TSMC -2.77% SMH -2.18%",
     "낙폭은 딥시크 때 근처도 안 감, 대신 넓고 얕게 퍼짐",
     "골드만삭스 \"컴퓨트 확장 시대 끝났을 수 있다\"")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.18  |  Kimi K3 vs DeepSeek R1", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-18_KIMIK3_X팩트체크.png")
img.save(out); print("Saved:", out)
