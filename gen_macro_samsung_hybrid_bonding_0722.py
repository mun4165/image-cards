from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-22"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = BLUE

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,22), "삼성전자, 평택 P5에 하이브리드 본딩 장비 50대 도입", font=bold(26), fill=ACCENT)
draw.text((32,70), "P5=차세대 D램·HBM4 거점(2028 가동목표) — 협력사 3사가 왜 다른가", font=bold(20), fill=GRAY)
draw.line([(32,114),(W-32,114)], fill=DARK_GRAY, width=1)

def band(y, h, color, fillbg, label, headline, d1, d2):
    draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
    draw.rectangle([32,y,38,y+h], fill=color)
    draw.text((58, y+h//2-14), label, font=bold(20), fill=color)
    draw.line([(232,y+16),(232,y+h-16)], fill=DARK_GRAY, width=1)
    draw.text((258, y+16), headline, font=bold(19), fill=WHITE)
    draw.text((258, y+52), d1, font=font(16), fill=color)
    draw.text((258, y+80), d2, font=font(14), fill=GRAY)

by = 132; bh = 152; step = 168
band(by, bh, AMBER, (36,26,8), "베시(BESI)",
     "원조 강자 — D2W 다이본더 첨단시장 점유율 70%대",
     "삼성이 채택하려는 D2W 하이브리드 본딩 양산장비 사실상 유일공급",
     "최우선 협력사 낙점, 가격(대당 ~60억원) 협상으로 최종발주 지연")
band(by+step, bh, CYAN, (8,28,34), "세메스",
     "내부 대안 — 삼성전자 계열 장비사",
     "전공정·후공정 장비를 폭넓게 만들어온 삼성 내재화 카드",
     "하이브리드 본더 자체 개발해 평가 중인 단계")
band(by+step*2, bh, GREEN, (10,28,18), "한화세미텍",
     "국내 대안 — W2W(웨이퍼 통째 접합) 방식",
     "SK하이닉스向 공급 임박 보도, 이미 타사에서 검증 진행형",
     "베시(D2W)와는 접합 방식 자체가 다름")

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.22  |  MACRO  삼성전자·하이브리드본딩  |  대규모 양산 2030년 전망 · 구독자용", font=font(14), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-22_MACRO_삼성전자_하이브리드본딩.png")
img.save(out); print("Saved:", out)
