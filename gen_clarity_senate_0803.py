from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-08-03"
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

img, draw = base_canvas(CYAN)
draw.text((32,22), "CLARITY 법안, 월요일 상원 일정에서 사라졌다", font=bold(25), fill=CYAN)
draw.text((32,74), "자격은 갖췄는데 표가 안 모인 8월 10일 데드라인", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, GREEN, (10,30,22), "자격  |  Calendar No. 423",
     "하원 통과, 상원 은행위 통과, 본회의 등재 완료", "7/22 은행위·농업위 통합안 + 윤리조항 공개")
band(draw, by+step, bh, ORANGE, (44,20,10), "결원  |  플로어 플랜에 없음",
     "8월 3일(월) 발표된 이번 주 상원 일정 미포함", "튠 대표 \"휴회 전 상정 어렵다\" 취지 언급")
band(draw, by+step*2, bh, AMBER, (40,30,8), "문턱  |  클로처 60표",
     "민주당 크로스오버 7~9표 필요, 미확보", "SEC·CFTC 관할, 위원회 통합, 윤리조항 이견")
band(draw, by+step*3, bh, RED, (40,14,14), "데드라인  |  8월 10일",
     "상원 지역구 근무기간(recess) 시작일", "놓치면 가을 이후로 처리 동력 이월")
band(draw, by+step*4, bh, TEAL, (10,32,30), "다음  |  클로처 표결 상정 여부",
     "8/10 전 세 쟁점이 정리되는지가 관건", "법안 폐기 아님 — 협상 시한이 닫히는 구조")
footer(draw, "2026.08.03  |  CLARITY Act·상원·디지털자산 시장구조법")
out = os.path.join(OUT_DIR, "2026-08-03_CLARITY법안_상원일정.png")
img.save(out); print("Saved:", out)
