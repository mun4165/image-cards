from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-23"
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

# ── CXL, D램 수요를 견인할 새로운 축이 될까 ──────────────────────────
img, draw = base_canvas(CYAN)
draw.text((32,22), "CXL, D램 수요를 견인할 새로운 축이 될까", font=bold(28), fill=CYAN)
draw.text((32,76), "HBM 다음 세계, PCIe 통로로 D램을 더 꽂고 여러 서버가 나눠쓴다", font=bold(18), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, CYAN, (8,28,34), "CXL이 하는 일",
     "PCIe 슬롯이라는 새 통로로 D램을 물리적으로 더 꽂음", "메모리채널 한계 우회, 여러 서버가 풀링해서 나눠씀")
band(draw, by+step, bh, AMBER, (40,28,10), "HBM과 차이",
     "HBM=짧은거리·속도, CXL=먼거리·용량, 역할분담", "칩적층 면적한계(HBM) vs PCIe우회로 큰용량(CXL)")
band(draw, by+step*2, bh, GREEN, (10,30,22), "왜 컨트롤러 접었나",
     "표준컨트롤러 확산→저가 범용D램 재활용 우려", "자기잠식 방향성만 확인, 정량 근거는 미공개")
band(draw, by+step*3, bh, BLUE, (10,20,40), "시장 규모",
     "욜그룹 전망 CXL생태계 전체 2026년 21억→2028년 160억달러", "컨트롤러 아닌 D램칩·모듈 포함 전체 기준")
footer(draw, "2026.07.23  |  삼성전자·SK하이닉스·MU")
out = os.path.join(OUT_DIR, "2026-07-23_CXL_D램수요견인할까.png")
img.save(out); print("Saved:", out)
