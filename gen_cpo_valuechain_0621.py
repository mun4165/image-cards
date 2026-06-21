from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-06-21"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

# 헤더
draw.text((32,22), "CPO · 실리콘 포토닉스 밸류체인 지도", font=bold(40), fill=ACCENT)
draw.text((32,78), "기판부터 CPO 스위치까지 — 8개 칸에 누가 서 있나", font=bold(22), fill=GRAY)
draw.line([(32,120),(W-32,120)], fill=DARK_GRAY, width=1)

# 사다리 (위=업스트림 부족=방패 / 아래=다운스트림 단가노출)
NODE_X = 70
rungs = [
    ("1  기판 · InP 웨이퍼",      "AXT · 스미토모 · 코히런트",        TEAL),
    ("2  에피웨이퍼",            "IQE",                              TEAL),
    ("3  광원 · CW 레이저",      "루멘텀 · 코히런트 · POET",         CYAN),
    ("4  SiPho 통합 · 광DSP",    "브로드컴 · 마벨 · 인텔 · 시버스",   BLUE),
    ("5  광학 · 파이버 · 조립",  "라이트패스 · 코닝 · 패브리넷",     BLUE),
    ("6  트랜시버 모듈",         "AAOI · 이노라이트 · 이오플링크",   AMBER),
    ("7  스위치 + CPO 통합",     "브로드컴 · 엔비디아 · 시스코",      ORANGE),
    ("8  파운드리 기반",         "TSMC · 글로벌파운드리 · 타워",      GRAY),
]
top, step = 162, 58
draw.line([(NODE_X, top),(NODE_X, top+step*(len(rungs)-1))], fill=DARK_GRAY, width=3)
for i,(head,sub,color) in enumerate(rungs):
    y = top + step*i
    hl = i in (0, 6)  # 최상단 업스트림 · 최종 CPO 강조
    r = 11 if hl else 8
    draw.ellipse([NODE_X-r,y-r,NODE_X+r,y+r], fill=color)
    if hl:
        draw.ellipse([NODE_X-r-5,y-r-5,NODE_X+r+5,y+r+5], outline=color, width=2)
    draw.text((NODE_X+34,y-13), head, font=bold(22), fill=WHITE)
    draw.text((480,y-11), sub, font=font(19), fill=color)

# 우측 방향 표식
draw.text((W-250,150), "▲  업스트림", font=bold(17), fill=TEAL)
draw.text((W-250,176), "공급부족 = 가격 방패", font=font(15), fill=GRAY)
draw.text((W-250,560), "▼  다운스트림", font=bold(17), fill=AMBER)
draw.text((W-250,586), "단가에 직접 노출", font=font(15), fill=GRAY)

# 하단 핵심 박스
by = 622
draw.rounded_rectangle([32,by,W-32,by+58], radius=8, fill=(8,30,36))
draw.text((50,by+9), "가격은 늘 사다리 위쪽, 공급이 부족한 칸에서 더 잘 지켜진다", font=bold(20), fill=CYAN)
draw.text((50,by+34), "같은 CPO 붐이라도 부족이 방패인 칸과 증설이 곧 글럿인 칸은 다르다", font=font(16), fill=GRAY)

# 푸터
draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.06.21  |  CPO · Silicon Photonics", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-06-21_CPO_밸류체인지도.png")
img.save(out); print("Saved:", out)
