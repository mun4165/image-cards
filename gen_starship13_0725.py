from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-25"
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
    draw.line([(240,y+14),(240,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((264, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((264, y+46), detail, font=font(15), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# ── 스타십 13차 비행, 준궤도 검증 3가지 ────────────
img, draw = base_canvas(ORANGE)
draw.text((32,22), "스타십 13차, 지구 안 돌았는데 왜 성공인가", font=bold(28), fill=ORANGE)
draw.text((32,76), "궤도 대신 준궤도로 검증한 세 가지, 14차 궤도비행의 조건", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, ORANGE, (40,24,8), "위성 배치 · 최초",
     "스타링크 V3 위성 20기, 처음으로 실제 양산 위성 전개", "태양광 패널·안테나 전개 및 레이저 통신 연결 시도")
band(draw, by+step, bh, CYAN, (8,26,32), "우주 재점화",
     "랩터 엔진, 우주공간에서 재점화 테스트", "궤도 진입·이탈에 필수인 능력 검증")
band(draw, by+step*2, bh, BLUE, (10,18,34), "열차폐 검증",
     "신형 타일 부착방식 + 응력센서 내장 타일", "일부 타일 흰색 도색, 손상 시뮬레이션 및 감지기법 테스트")
band(draw, by+step*3, bh, GREEN, (10,30,22), "부스터 착수",
     "걸프만 해상 착수는 성공, 엔진 전부 점화는 실패", "13개 중 일부 미점화로 예상보다 강하게 충돌")
footer(draw, "2026.07.25  |  SpaceX  Starship Flight 13")
out = os.path.join(OUT_DIR, "2026-07-25_스타십13차_준궤도검증.png")
img.save(out); print("Saved:", out)
