from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-08-20"
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
    draw.line([(360,y+14),(360,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((384, y+15), headline, font=bold(18), fill=WHITE)
    draw.text((384, y+45), detail, font=font(14), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

BY, BH, STEP = 122, 98, 110

img, draw = base_canvas(GREEN)
draw.text((32,22), "블룸에너지, AI가 전기를 너무 많이 먹어서 뜨는 회사", font=bold(24), fill=GREEN)
draw.text((32,74), "데이터센터 옆에 놓는 발전기 상자, 연료전지 이야기", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, GREEN, (10,30,22), "무슨 회사  |  연료전지 제조사",
     "천연가스·수소 넣으면 전기 나오는 상자, 전력망 없이 즉시 발전", "AI 데이터센터의 전력망 연결 대기(수년) 문제를 우회")
band(draw, by+step, bh, BLUE, (10,20,40), "고객사  |  오라클과 대형 계약",
     "오라클에 최대 2.8GW 연료전지 공급, 뉴욕주 등 데이터센터向", "최근 90일간 데이터센터 관련 계약만 76.5억불 체결")
band(draw, by+step*2, bh, AMBER, (44,32,10), "실적  |  2026년 2분기 매출 10.7억불",
     "전년 동기 대비 +165%, 사상 첫 분기 매출 10억불 돌파", "회사는 올해 연간 매출 전망을 39~42억불로 상향")
band(draw, by+step*3, bh, RED, (44,16,16), "조심할 점  |  '20조 계약'의 실체 논란",
     "회사가 공개한 계약 잔량과 서류상 확정 계약 금액 차이가 큼", "주가는 이미 좋은 소식을 많이 반영, PER 200배 이상")
band(draw, by+step*4, bh, TEAL, (10,32,30), "정리  |  방향은 맞지만 숫자는 확인 필요",
     "AI 전력난이라는 진짜 문제를 푸는 회사인 건 사실", "다음 실적에서 확정 계약 물량이 얼마나 느는지가 관건")
footer(draw, "2026.08.20  |  블룸에너지(Bloom Energy) 기업 소개")
out = os.path.join(OUT_DIR, "2026-08-20_BE_블룸에너지_소개.png")
img.save(out); print("Saved:", out)
