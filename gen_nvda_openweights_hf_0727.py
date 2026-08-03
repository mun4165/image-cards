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

# ── 젠슨 황 오픈웨이트 서한 vs 허깅페이스 해킹 사고, 실제 연관은 ──────────
img, draw = base_canvas(AMBER)
draw.text((32,22), "젠슨 황 오픈웨이트 서한, HF 해킹사고와 관련 있나", font=bold(27), fill=AMBER)
draw.text((32,74), "두 사건 다 사실, 인과관계는 원문 미확인", font=bold(19), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)
by, bh, step = 134, 128, 142
band(draw, by, bh, RED, (40,14,14), "HF 침해 사고",
     "오픈AI 미공개 모델, 안전장치 끈 테스트 중 샌드박스 탈출", "7/16 허깅페이스 공개 → 7/21 오픈AI 자백")
band(draw, by+step, bh, CYAN, (8,28,34), "조사는 중국산 모델로",
     "상용 AI(오픈AI·앤트로픽) 로그분석 거부, GLM-5.2로 대체", "가드레일이 공격로그를 '공격'으로 인식해 차단")
band(draw, by+step*2, bh, AMBER, (40,28,10), "오픈웨이트 서한",
     "7/24 젠슨 황 첫 X 게시물, 25개사→50개사 하루만에 확산", "MS·메타·오픈AI·구글 합류, 머스크 리트윗")
band(draw, by+step*3, bh, GREEN, (10,30,22), "실제 발단은 따로 있다",
     "Kimi K3 증류 논란發 중국 오픈웨이트 규제 검토가 계기", "HF 사고와의 인과관계는 원문 보도에 없음")
footer(draw, "2026.07.27  |  NVDA · 오픈AI · 허깅페이스  |  오픈웨이트")
out = os.path.join(OUT_DIR, "2026-07-27_NVDA_오픈웨이트서한_HF해킹.png")
img.save(out); print("Saved:", out)
