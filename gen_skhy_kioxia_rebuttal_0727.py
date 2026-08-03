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

# ── 키옥시아 안심논리·저가매수 논리 반박 ──────────
img, draw = base_canvas(RED)
draw.text((32,22), "키옥시아, 15% 약속 있으니 안심? 저가매수 기회?", font=bold(23), fill=RED)
draw.text((32,74), "두 논리 모두 검증하면 구멍이 있다", font=bold(19), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)
by, bh, step = 134, 128, 142
band(draw, by, bh, AMBER, (40,28,10), "15% 약속의 한계",
     "법적 강제 아닌 자율규제, 2028년까지라는 기한부", "의결권 안 써도 이해상충 우려는 이미 표면화")
band(draw, by+step, bh, RED, (40,14,14), "낙폭의 성격",
     "6/22 고점 대비 -52%, 삼성·마이크론보다 더 큰 낙폭", "특허배상 3400억원, 업황 회복돼도 안 사라짐")
band(draw, by+step*2, bh, CYAN, (8,28,34), "업황조정 vs 개별악재",
     "업종 동반하락은 매크로 회복되면 되돌지만", "개별악재는 재무제표에 그대로 남는 실제 비용")
band(draw, by+step*3, bh, GREEN, (10,30,22), "결론",
     "리스크는 낮음이지 없음이 아니고, 매수근거는 아직 약함", "다음 확인: 2028 기한 갱신 여부, 소송 항소 여부")
footer(draw, "2026.07.27  |  SK하이닉스 · 키옥시아  |  안심논리 팩트체크")
out = os.path.join(OUT_DIR, "2026-07-27_SKHY_키옥시아_안심논리_반박.png")
img.save(out); print("Saved:", out)
