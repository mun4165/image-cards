from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-18"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(239,68,68)
ACCENT = ORANGE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,24), "AAOI  분기매출 $14억설", font=bold(22), fill=GRAY)
draw.text((32,58), "지금 매출의 11배 규모다", font=bold(28), fill=ACCENT)
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
band(by, bh, GRAY, (30,32,36), "SNS발 주장",
     "2027 3Q 분기매출 $14억 전망 확산",
     "연환산 $56억, 시총 $80억 대비 저평가 주장",
     "회사 공식 가이던스 근거는 확인 안 됨")
band(by+step, bh, CYAN, (10,28,32), "실제 숫자",
     "TTM 매출 $5.07억 (YoY +64.3%)",
     "2025 연간매출 $4.56억 (YoY +82.75%)",
     "시총 $82.2억, 7/17 종가 $102.41")
band(by+step*2, bh, ORANGE, (40,26,10), "격차",
     "$14억 도달하려면 5개 분기 내 10배+ 성장 필요",
     "캐파투자 뉴스 ≠ 확정 가이던스",
     "다음 확인=분기별 가이던스 상향폭·백로그 증가")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.18  |  AAOI  Applied Optoelectronics Valuation Check", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-18_AAOI_분기매출14억달러설.png")
img.save(out); print("Saved:", out)
