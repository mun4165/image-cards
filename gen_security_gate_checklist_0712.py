from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-12"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); BLUE=(59,130,246); PURPLE=(167,139,250)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,22), "같은 중국 배제라도 근거는 다르다", font=bold(20), fill=GRAY)
draw.text((32,56), "국가안보 규정 판별 체크리스트 4문항", font=bold(28), fill=ACCENT)
draw.line([(32,104),(W-32,104)], fill=DARK_GRAY, width=1)

def band(y, h, num, color, fillbg, question, answer):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((60, y+h//2-18), num, font=bold(30), fill=color)
    draw.line([(140,y+14),(140,y+h-14)], fill=DARK_GRAY, width=1)
    block_h = 28+14+24
    ty = y + (h-block_h)//2
    draw.text((166, ty), question, font=bold(20), fill=WHITE)
    draw.text((166, ty+38), answer, font=font(16), fill=color)

by = 122
avail = (H-30) - by - 16
step = avail // 4
bh = step - 12

band(by, bh, "①", ORANGE, (40,24,10),
     "어느 부처가 관할하는가",
     "국무부=ITAR / 의회=NDAA / 국방부=FOCI / 재무부=CFIUS / 상무부=Entity List")
band(by+step, bh, "②", GREEN, (10,28,20),
     "국가 단위로 막는가, 특정 회사만 막는가",
     "ITAR·FOCI=국가·지배구조 단위 / NDAA·Entity List=이름 찍힌 회사 지정")
band(by+step*2, bh, "③", BLUE, (10,20,34),
     "어느 산업 카테고리에 적용되는가",
     "반도체=NDAA 5949 / 통신·영상감시=NDAA 889 / 그 외 방산물자=ITAR")
band(by+step*3, bh, "④", PURPLE, (26,18,38),
     "조달인가, 투자인가, 지배구조인가",
     "조달=NDAA·Entity List / 인수거래=CFIUS / 지분·이사회=FOCI")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.12  |  LPTH  RKLB  국가안보 게이트 판별 체크리스트", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-12_국가안보게이트_판별체크리스트.png")
img.save(out); print("Saved:", out)
