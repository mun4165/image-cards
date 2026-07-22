from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-21"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); RED=(248,113,113); ORANGE=(249,115,22); BLUE=(59,130,246); TEAL=(20,184,166)

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
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(196,y+14),(196,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((220, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((220, y+46), detail, font=font(15), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

img, draw = base_canvas(BLUE)
draw.text((32,22), "테슬라 FSD는 왜 증류가 안 통하나", font=bold(32), fill=BLUE)
draw.text((32,76), "화이트박스 증류와 블랙박스 증류의 차이를 짚었다", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, BLUE, (10,20,40), "테슬라",
     "HW4 V14 지능을 HW3에 자체 증류 (화이트박스)", "교사모델 로짓·중간표현 전부 접근, 무제한 재질의 가능")
band(draw, by+step, bh, RED, (40,14,14), "중국 사례",
     "Claude API에 대량 질의로 증류 의혹 (블랙박스)", "알리바바 계정 2.5만개·질의 2,880만회, 앤트로픽 주장")
band(draw, by+step*2, bh, AMBER, (40,28,10), "결정적 차이",
     "FSD는 입력을 합성 불가, 실제 도로주행만 데이터", "롱테일 시나리오는 계측차량 관찰로 못 옮겨옴")
band(draw, by+step*3, bh, ORANGE, (40,22,10), "함의",
     "공변량 이동+모방학습 벽, 교정 피드백 루프 없음", "실주행 시간이 누적된 기업만 갖는 해자 구조")
footer(draw, "2026.07.21  |  TSLA  FSD v14 Lite")
out = os.path.join(OUT_DIR, "2026-07-21_TSLA_FSD증류.png")
img.save(out); print("Saved:", out)
