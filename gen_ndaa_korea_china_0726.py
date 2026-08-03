from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-26"
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

# ── NDAA 2027: 한국 내 중국 공산당 영향력 평가 조항 팩트체크 ──────────
img, draw = base_canvas(AMBER)
draw.text((32,22), "NDAA에 한국 내 중국 영향력 평가 조항, 팩트체크", font=bold(28), fill=AMBER)
draw.text((32,74), "하원 7/22 통과는 사실, 다만 상원 조율 남은 하원 단독 버전", font=bold(19), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)
by, bh, step = 134, 128, 142
band(draw, by, bh, AMBER, (40,28,10), "하원 통과",
     "7/22(수) 216-212 표결, $1.15조 규모 NDAA", "로니 잭슨(공화, 텍사스) 발의, 6월 마크업서 삽입")
band(draw, by+step, bh, RED, (40,14,14), "조항 내용",
     "국방장관에 한국 내 中 '악의적 영향력' 평가 요구", "주한미군 HUMINT 위험 + 中 기술기업 위협 여부, 기한 11월 말")
band(draw, by+step*2, bh, CYAN, (8,28,34), "상원은 별도 트랙",
     "법안 본문 아닌 위원회 보고서로 유사 요구", "국방장관 브리핑 기한 2027.5.1, 하원과 형식 다름")
band(draw, by+step*3, bh, GREEN, (10,30,22), "다음 확인 지점",
     "양원 조율(conference) 최종안에 조항 존속 여부", "상원 본회의 처리 시점 + 11월 말 국방부 보고서 실제 내용")
footer(draw, "2026.07.26  |  NDAA 2027  |  한미동맹 · 주한미군")
out = os.path.join(OUT_DIR, "2026-07-26_NDAA_한국중국영향력.png")
img.save(out); print("Saved:", out)
