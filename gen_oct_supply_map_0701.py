from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-01"
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

draw.text((32,22), "궤도 데이터센터, GPU 뒤 두 번째 부품", font=bold(40), fill=ACCENT)
draw.text((32,80), "위성끼리 잇는 레이저 링크(OCT) · 종목별 노출은 제각각", font=bold(21), fill=GRAY)
draw.line([(32,122),(W-32,122)], fill=DARK_GRAY, width=1)

ty = 138
draw.rounded_rectangle([32,ty,W-32,ty+92], radius=10, fill=(8,28,34))
draw.rectangle([32,ty,38,ty+92], fill=CYAN)
draw.text((60,ty+16), "GPU가 연산이면, OCT는 그 데이터를 나르는 통신", font=bold(18), fill=CYAN)
draw.text((60,ty+44), "Starlink · Kuiper · SDA(우주개발청) · Golden Dome · 궤도 데이터센터",
          font=bold(20), fill=WHITE)

def band(y, h, color, fillbg, label, headline, detail):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+16), label, font=bold(20), fill=color)
    draw.line([(360,y+16),(360,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((388, y+18), headline, font=bold(20), fill=WHITE)
    draw.text((388, y+52), detail, font=font(16), fill=color)

by = 250; bh = 84; step = 92
band(by, bh, TEAL, (8,30,30), "공급 측",
     "인증 공급사는 제한적", "Mynaric · Tesat · Skyloom · CACI — 미국 4곳 중심")
band(by+step, bh, BLUE, (12,20,38), "종목 노출",
     "함께 엮이는 이름, 결은 다름", "SPCX=내부용 · IONQ=양자통신 · CACI=대형 복합체 일부")
band(by+step*2, bh, AMBER, (40,30,8), "참고 변수",
     "설계보다 양산이 관건", "정밀 부품 대량 생산 실적을 함께 확인")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.01  |  키워드가 아니라 회사별 실제 사업 구성으로 구분", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-01_OCT_두번째부품.png")
img.save(out); print("Saved:", out)
