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

# ── AXTI 인듐인화물 계약 시점 구분 ──────────────────────────
img, draw = base_canvas(AMBER)
draw.text((32,22), "AXT 인듐인화물 계약, 7월 급등과 다른 재료다", font=bold(28), fill=AMBER)
draw.text((32,76), "6월 11일 발표 계약과 7월 21일 급등 트리거는 별개", font=bold(18), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, AMBER, (40,28,10), "계약 시점",
     "6/11 Beijing Tongmei-Nanjing Casela 체결", "2027년 인듐인화물 웨이퍼 공급, 약 2540만달러")
band(draw, by+step, bh, CYAN, (8,28,34), "계약 구조",
     "테이크오어페이 80%, 선지급 50%", "15영업일 내 50% 선지급, 잔금 26년말까지")
band(draw, by+step*2, bh, BLUE, (10,20,40), "7/21 급등 재료",
     "노스랜드캐피털 목표가 125달러 상향", "6월 계약과 무관한 별도 트리거, +15.73%")
band(draw, by+step*3, bh, GREEN, (10,30,22), "다음 확인",
     "2027년 매출 반영 규모, 80% 하한 초과 여부", "다음 실적발표에서 계약 기여분 확인 필요")
footer(draw, "2026.07.23  |  AXTI")
out = os.path.join(OUT_DIR, "2026-07-23_AXTI_인듐인화물계약시점구분.png")
img.save(out); print("Saved:", out)

# ── RKLB 8/10 2분기 실적 관전포인트 ──────────────────────────
img, draw = base_canvas(BLUE)
draw.text((32,22), "로켓랩 8월 10일 2분기 실적, 뭘 봐야 하나", font=bold(28), fill=BLUE)
draw.text((32,76), "가이던스 상단 도달·마진율·뉴트론 일정 세 가지", font=bold(18), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, BLUE, (10,20,40), "매출 가이던스",
     "2.25억~2.4억달러, 두 사업부 모두 전년比 증가 전망", "1분기 매출은 전년比 +64%")
band(draw, by+step, bh, CYAN, (8,28,34), "마진율 구간",
     "GAAP 33~35%, 비GAAP 38~40%", "제품믹스 변화로 압박 가능성 사전 언급")
band(draw, by+step*2, bh, AMBER, (40,28,10), "뉴트론 최대변수",
     "26년 1월 탱크시험 문제로 4분기 발사로 지연", "누적개발비 3.6억달러, 분기 인건비 약1500만달러")
band(draw, by+step*3, bh, GREEN, (10,30,22), "백로그 전환속도",
     "발사예약 70건 이상, 역대 최대치", "뉴트론向 계약은 최초발사 성공이 매출화 전제조건")
footer(draw, "2026.07.23  |  RKLB")
out = os.path.join(OUT_DIR, "2026-07-23_RKLB_8월10일실적관전포인트.png")
img.save(out); print("Saved:", out)

# ── SATL 8/5 실적 관전포인트 ──────────────────────────
img, draw = base_canvas(TEAL)
draw.text((32,22), "세틀로직 8월 5일 실적, Merlin 앞두고 뭘 보나", font=bold(27), fill=TEAL)
draw.text((32,76), "매출성장·현금흐름 지속성과 10월 발사일정이 관건", font=bold(18), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, TEAL, (8,32,28), "1분기 기준점",
     "매출 610만달러 전년比 +80%, 영업손실 33% 개선", "영업현금흐름 창사 첫 플러스 전환")
band(draw, by+step, bh, CYAN, (8,28,34), "RPO 잔고",
     "잔여수행의무 6480만달러, 1년내 2920만달러 인식예정", "1분기 국방고객向 1200만달러 별도계약 체결")
band(draw, by+step*2, bh, AMBER, (40,28,10), "Merlin 일정",
     "최초위성 10월 발사목표, 27년 상반기 초기전력화", "센티넬-2 정렬 10개밴드, AI 탑재처리")
band(draw, by+step*3, bh, GREEN, (10,30,22), "두 층위 구분",
     "기존 아를레프원 사업 vs Merlin 미래재료", "Merlin은 10월 발사 전까지 결과 아닌 일정 확인 수준")
footer(draw, "2026.07.23  |  SATL")
out = os.path.join(OUT_DIR, "2026-07-23_SATL_8월5일실적관전포인트.png")
img.save(out); print("Saved:", out)
