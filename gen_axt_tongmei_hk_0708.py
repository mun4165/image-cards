from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-08"
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

draw.text((32,24), "AXT 자회사 통메이, 상해 IPO 철회", font=bold(32), fill=ACCENT)
draw.text((32,80), "홍콩거래소로 갈아탄 진짜 이유", font=bold(24), fill=GRAY)
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
band(by, bh, BLUE, (10,20,34), "철회",
     "6/26 SSE에 통보, 7/8 상하이거래소 공식 접수",
     "과창판(STAR Market) IPO — 2021년 신청, 3년째 정체",
     "AXT 나스닥 상장(AXTI)과는 무관, 자회사 건")
band(by+step, bh, CYAN, (8,28,34), "전환",
     "홍콩거래소(HKEX)로, GaAs에서 InP로",
     "AI 데이터센터 광통신용 인화인듐(InP) 기판 중심 재편",
     "더 넓은 기관·개인 투자자 기반 노림")
band(by+step*2, bh, ORANGE, (40,25,10), "체크포인트",
     "PE펀드 11곳 상환청구권, 약 4900만 달러",
     "AXT: 전액 상환 자금 충분 — 채무불이행 아님",
     "다음 확인: 홍콩 신청 시점, 7/30 2분기 실적")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.08  |  AXT  AXTI · Tongmei", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-08_AXT_통메이홍콩전환.png")
img.save(out); print("Saved:", out)
