from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-31"
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
    draw.text((60, y+14), label, font=bold(17), fill=color)
    draw.line([(268,y+14),(268,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((292, y+15), headline, font=bold(18), fill=WHITE)
    draw.text((292, y+45), detail, font=font(14), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

BY, BH, STEP = 122, 98, 110

img, draw = base_canvas(TEAL)
draw.text((32,22), "애플의 성장 카드 세 장, 두 장은 탈락", font=bold(25), fill=TEAL)
draw.text((32,74), "남는 건 서비스 매출 재가속 하나뿐인 이유", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, RED, (40,14,14), "카드1  |  하드웨어 확대",
     "아이폰 +21.7% · 맥 +28.7%, 관세환급 2%p 견인", "가격전가 의존, 반복 가능한 성장카드 아님")
band(draw, by+step, bh, ORANGE, (44,20,10), "카드2  |  온디바이스 AI",
     "시리·애플인텔리전스 진척 언급 없음", "제품 먼저 나와야 성립하는 가설 단계")
band(draw, by+step*2, bh, GREEN, (10,30,22), "카드3  |  서비스 재가속",
     "매출 307억달러(컨센 314억) · 성장률 12.1%", "마진 70%대, 유일하게 남은 진짜 카드")
band(draw, by+step*3, bh, BLUE, (10,20,40), "역설  |  하드웨어 vs 마진",
     "하드웨어 마진 30%대, 서비스 마진 70%대", "하드웨어 더 팔수록 총마진은 눌리는 구조")
band(draw, by+step*4, bh, TEAL, (10,32,30), "확인지점  |  다음분기 성장률 역전",
     "서비스 성장률이 아이폰을 다시 앞서는지", "TAC 아닌 앱스토어·광고 자체성장 여부")
footer(draw, "2026.07.31  |  AAPL 애플  성장 카드 점검")
out = os.path.join(OUT_DIR, "2026-07-31_AAPL_성장카드점검_서비스재가속.png")
img.save(out); print("Saved:", out)
