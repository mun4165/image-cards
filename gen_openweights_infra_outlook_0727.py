from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-27"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

def base_canvas(accent):
    img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    draw.rectangle([0,0,W,4], fill=accent); draw.rectangle([0,0,4,H], fill=accent)
    return img, draw

def band(draw, y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+14), label, font=bold(18), fill=color)
    draw.line([(228,y+14),(228,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((252, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((252, y+46), detail, font=font(15), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# ── 오픈웨이트 확산 전망: 인프라는 웃고 API매출은 운다 ──────────
img, draw = base_canvas(TEAL)
draw.text((32,22), "오픈웨이트 확산되면 누가 웃고 누가 우나", font=bold(28), fill=TEAL)
draw.text((32,74), "엔비디아는 곡괭이 장사, 오픈AI·구글은 딜레마", font=bold(19), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)
by, bh, step = 134, 128, 142
band(draw, by, bh, GREEN, (10,30,22), "인프라 회사 수혜",
     "엔비디아·MS·Dell, 누가 이기든 컴퓨팅 수요는 계속", "오픈웨이트는 최적화 덜 돼 컴퓨팅 더 먹음")
band(draw, by+step, bh, AMBER, (40,28,10), "클로즈드는 매출 압박",
     "오픈AI·구글, API매출 불리한데도 서한 서명", "중국발 생태계 이탈 우려가 매출논리 압도")
band(draw, by+step*2, bh, CYAN, (8,28,34), "끝까지 안 낀 클로드",
     "앤트로픽, 엔터프라이즈 매출+안전철학 두 축 모두 반대", "가중치 공개=안전장치 우회 가능 구조적 문제")
band(draw, by+step*3, bh, RED, (40,14,14), "이중구조 전망",
     "오픈웨이트=저변확대, 클로즈드=최정상성능·안전보증", "투자축은 결국 '누가 인프라를 파냐'")
footer(draw, "2026.07.27  |  NVDA · 오픈AI · 앤트로픽  |  오픈웨이트 전망")
out = os.path.join(OUT_DIR, "2026-07-27_오픈웨이트확산전망.png")
img.save(out); print("Saved:", out)
