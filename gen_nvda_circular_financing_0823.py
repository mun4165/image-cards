from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-08-23"
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

img, draw = base_canvas(BLUE)
draw.text((32,22), "엔비디아 5000억달러 MOU, 왜 순환금융 논란이 다시 나오나", font=bold(24), fill=BLUE)
draw.text((32,74), "8월 10일 컴퓨팅 금융 플랫폼 발표, 구조와 쟁점 정리", font=bold(18), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)
by, bh, step = BY, BH, STEP
band(draw, by, bh, BLUE, (10,20,40), "구조  |  아폴로·블랙록·KKR 등 6곳과 MOU",
     "엔비디아가 직접 대는 게 아니라 제3자 자본을 모아 GPU 담보 대출", "5,000억달러 이상 규모, 시간을 두고 채워갈 목표치")
band(draw, by+step, bh, AMBER, (44,32,10), "조건  |  엔비디아가 최대 25% 잔존가치 보증",
     "GPU 재판매 가치가 예상보다 낮으면 차액 일부를 엔비디아가 보전", "금융사 리스크를 줄여주는 장치, 계약 세부조건은 비공개")
band(draw, by+step*2, bh, RED, (44,16,16), "전례  |  오픈AI 오하이오 건, 8/17 규모 축소",
     "백스톱 최대 2,500억달러 → 1,200억달러 미만으로 줄어듦", "투자자 반발: 엔비디아가 자기 매출을 자기 대차대조표로 떠받친다")
band(draw, by+step*3, bh, ORANGE, (44,26,10), "논란  |  순환금융이 왜 문제되나",
     "칩 파는 회사가 사는 회사 자금까지 보증하면 최종수요 구분 불가", "25% 보증이 남아있는 한 엔비디아 리스크가 완전히 빠진 건 아님")
band(draw, by+step*4, bh, TEAL, (10,32,30), "체크포인트  |  최종계약 전환 여부",
     "잔존가치 보증 실제 사용 규모, 오하이오 건 확장분 집행 여부", "시장이 실수요 확대로 볼지 인위적 수요로 볼지가 관건")
footer(draw, "2026.08.23  |  엔비디아(NVDA) 컴퓨팅 금융 플랫폼 MOU 정리")
out = os.path.join(OUT_DIR, "2026-08-23_NVDA_순환금융_MOU정리.png")
img.save(out); print("Saved:", out)
