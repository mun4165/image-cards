from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-23"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = RED

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "SpaceX 첫 채권 발행에 우주주 동반 급락", font=bold(37), fill=ACCENT)
draw.text((32,74), "1등의 호재가 경쟁사를 끌어내린 하루 — 미국 6월 22일 종가", font=bold(21), fill=GRAY)
draw.line([(32,118),(W-32,118)], fill=DARK_GRAY, width=1)

def row(y, h, color, ticker, name, pct, price, note):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=(28,20,22))
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), ticker, font=bold(28), fill=WHITE)
    draw.text((60, y+54), name, font=font(16), fill=GRAY)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+22), pct, font=bold(34), fill=color)
    if price:
        draw.text((560, y+30), price, font=font(18), fill=GRAY)
    draw.line([(700,y+16),(700,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((724, y+30), note, font=bold(19), fill=color)

row(132, 80, RED,    "RKLB", "Rocket Lab",  "-6.48%", "$100.29", "나스닥100 편입에도 같이 하락")
row(220, 80, RED,    "RDW",  "Redwire",     "-9.27%", "$13.02",  "자본조달 의존 커 최대 낙폭")
row(308, 80, RED,    "SATL", "Satellogic",  "-5.89%", "$5.68",   "섹터 동반 매도에 휩쓸림")
row(396, 80, ORANGE, "SPCX", "SpaceX 본주", "-16.4%", "",        "IPO 데뷔 후 상승분 대부분 반납")

# 하단 핵심 박스
by = 496
draw.rounded_rectangle([32,by,W-32,by+96], radius=10, fill=(8,26,34))
draw.text((52,by+14), "첫 회사채 약 200억 달러 · 투자등급(IG) · 현금 1008억 깔고도 발행 = 자본 구조 강화", font=bold(20), fill=CYAN)
draw.text((52,by+52), "한 곳이 우주의 자본을 독식한다는 우려가 섹터를 눌렀다 — 결국 한 바구니, 차이는 낙폭과 회복 탄력", font=bold(20), fill=WHITE)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.23  |  RKLB · RDW · SATL · SPCX", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-23_우주주_SpaceX채권_동반급락.png")
img.save(out); print("Saved:", out)
