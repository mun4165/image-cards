from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-27"
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

draw.text((32,22), "LPTH — 방산 인수합병 신호에 술렁인다", font=bold(36), fill=ACCENT)
draw.text((32,74), "그런데 '인수될 회사' 찾기가 왜 함정인가", font=bold(20), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

# 핵심 메시지 박스
ty = 132
draw.rounded_rectangle([32,ty,W-32,ty+96], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+96], fill=CYAN)
draw.text((60,ty+16), "질문을 바꿔야 한다", font=bold(18), fill=GRAY)
draw.text((60,ty+46), "'누가 사줄까'가 아니라 '혼자 클 자격을 증명했나'", font=bold(24), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(560,y+16),(560,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((588, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((588, y+52), detail, font=font(16), fill=color)

by = 248; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "인수는 천장 아님",
     "프리미엄은 일회성 30~50%", "인수 기대는 바닥(보험)일 뿐 · 진짜 상방은 자력 성장")
band(by+step, bh, BLUE, (12,20,38), "독립의 조건",
     "독립은 그 자체로 가치 아님", "자금조달 능력과 짝일 때만 프리미엄 · 돈 없으면 로망")
band(by+step*2, bh, ORANGE, (38,24,8), "LPTH 진단 (판단)",
     "수년째 서브스케일", "자력 흑자·규모 증명 아직 · 독립 자격 시험 미통과 의심")

gy = 524
draw.rounded_rectangle([32,gy,W-32,gy+96], radius=10, fill=(8,28,34))
draw.text((52,gy+14), "한 줄 요약", font=bold(18), fill=GRAY)
draw.text((52,gy+44), "M&A 흐름 = LPTH가 팔린다는 신호가 아니다",
          font=bold(22), fill=CYAN)
draw.text((52,gy+74), "적외선 광학 IP의 희소가치가 비싸게 거래되기 시작했다는 신호다",
          font=font(15), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.27  |  Safran-Exail 인수 협상 — LPTH를 '인수 후보'로 읽으면 안 되는 이유", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-27_LPTH_인수합병프레임.png")
img.save(out); print("Saved:", out)
