from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-06"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

def make_card(filename, accent, title, subtitle, bands, footer):
    img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
    draw.rectangle([0,0,W,4], fill=accent); draw.rectangle([0,0,4,H], fill=accent)

    draw.text((32,24), title, font=bold(36), fill=accent)
    draw.text((32,80), subtitle, font=bold(24), fill=GRAY)
    draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)

    def band(y, h, color, fillbg, label, headline, d1, d2):
        draw.rounded_rectangle([32,y,W-32,y+h], radius=10, fill=fillbg)
        draw.rectangle([32,y,38,y+h], fill=color)
        draw.text((60, y+h//2-14), label, font=bold(23), fill=color)
        draw.line([(240,y+18),(240,y+h-18)], fill=DARK_GRAY, width=1)
        draw.text((268, y+20), headline, font=bold(24), fill=WHITE)
        draw.text((268, y+62), d1, font=font(18), fill=color)
        draw.text((268, y+92), d2, font=font(16), fill=GRAY)

    by, bh, step = 146, 148, 164
    for i, b in enumerate(bands):
        band(by+step*i, bh, b["color"], b["fillbg"], b["label"], b["headline"], b["d1"], b["d2"])

    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), footer, font=font(15), fill=GRAY)

    out = os.path.join(OUT_DIR, filename)
    img.save(out); print("Saved:", out)

FOOTER = "2026.07.06  |  $MU  Micron Technology"

# 1. 착공 팩트
make_card(
    "2026-07-06_히로시마착공팩트.png", BLUE,
    "마이크론 히로시마 93억 달러 착공",
    "2026년 7월 4일 착공식 — 무엇을 짓나",
    [
        dict(color=BLUE, fillbg=(14,24,44), label="투자규모",
             headline="1.5조 엔 (약 93억 달러)",
             d1="신규 클린룸 약 2만 8천㎡ — 기존 부지 증축",
             d2="생산 품목: HBM4 + 차세대 D램(1γ)"),
        dict(color=TEAL, fillbg=(10,32,30), label="일정",
             headline="첫 출하 2028년 여름 · 완전가동 2030년 봄",
             d1="착공~첫출하 2년 — 그린필드 신축(3~4년)보다 빠름",
             d2="완전가동 목표 캐파 월 4만 장(스코프 불명확)"),
        dict(color=AMBER, fillbg=(40,28,10), label="보조금",
             headline="이번 라운드 최대 5,360억 엔 (약 35억 달러)",
             d1="설비투자 5,000억 엔 + R&D 360억 엔",
             d2="히로시마 누적 보조금 최대 7,745억 엔(약 50억 달러)"),
    ], FOOTER,
)

# 2. 엘피다 유산
make_card(
    "2026-07-06_엘피다유산.png", AMBER,
    "25억 vs 93억 vs 50억 — 엘피다의 유산",
    "파산한 일본 회사의 팹이 14년 만에 HBM 심장이 되다",
    [
        dict(color=BLUE, fillbg=(14,24,44), label="2013",
             headline="마이크론, 엘피다 인수 — 약 25억 달러",
             d1="일본 마지막 D램 제조사, 2012년 파산(JAL 이후 최대)",
             d2="히로시마 300mm 팹 포함해 인수"),
        dict(color=TEAL, fillbg=(10,32,30), label="2026",
             headline="이번 증설 투자액 — 약 93억 달러",
             d1="인수가의 약 3.7배 규모 재투자",
             d2="HBM4 + 1γ D램 신규 클린룸"),
        dict(color=AMBER, fillbg=(40,28,10), label="누적",
             headline="일본 정부 지원 총액 — 약 50억 달러",
             d1="엘피다 인수가의 약 2배를 정부가 지원",
             d2="자국 회사 아닌 미국 회사에 반복 베팅"),
    ], FOOTER,
)

# 3. 타임라인 비교
make_card(
    "2026-07-06_팹건설기간비교.png", TEAL,
    "착공~완전가동, 남들보다 빠른가",
    "그린필드 신축 팹과 비교",
    [
        dict(color=TEAL, fillbg=(10,32,30), label="히로시마",
             headline="증축 · 첫출하 2년 / 완전가동 4년",
             d1="기존 부지 — 전력·용수·물류 인프라 재활용",
             d2="착공 2026 → 출하 2028 여름 → 완가 2030 봄"),
        dict(color=BLUE, fillbg=(14,24,44), label="TSMC 애리조나",
             headline="신축 · 착공~양산 약 3~4년",
             d1="1공장 착공(2021년경) → 양산(2024)",
             d2="그린필드 — 인프라부터 구축"),
        dict(color=GRAY, fillbg=(28,30,34), label="삼성 테일러",
             headline="신축 · 착공~가동 약 4년",
             d1="텍사스 착공(2022) → 가동목표(2026)",
             d2="히로시마는 증축이라 상대적으로 빠른 편"),
    ], FOOTER,
)

# 4. 웨이퍼 역산
make_card(
    "2026-07-06_웨이퍼단가역산.png", GREEN,
    "역산: 웨이퍼 한 장에 얼마?",
    "공시된 숫자 두 개로 단가를 거꾸로 구한다",
    [
        dict(color=BLUE, fillbg=(14,24,44), label="매출",
             headline="HBM 분기 매출 약 20억 달러 (FY25 4분기)",
             d1="연환산 약 80억 달러 run-rate",
             d2="이후 FY26 1~3분기는 HBM 단독 매출 미공시"),
        dict(color=TEAL, fillbg=(10,32,30), label="캐파",
             headline="HBM 웨이퍼 캐파 약 월 6만 장 (2025년말)",
             d1="분기 생산량 = 6만 장 × 3개월 = 18만 장",
             d2="TrendForce 계열 추정"),
        dict(color=GREEN, fillbg=(10,34,26), label="역산",
             headline="웨이퍼당 매출 약 1만 1천 달러",
             d1="20억 달러 ÷ 18만 장 = 약 $11,000/장",
             d2="업계 통설(D램 대비 3~5배)과 부합"),
    ], FOOTER,
)

# 5. 매출 시나리오 + 비중
make_card(
    "2026-07-06_신공장매출비중.png", CYAN,
    "신공장 매출, 전체의 몇 %인가",
    "캐파 시나리오 2개 → 전체 매출 대비",
    [
        dict(color=GRAY, fillbg=(28,30,34), label="보수적",
             headline="월 2.5만 장 → 연환산 약 33억 달러",
             d1="히로시마 신규 라인 HBM 순증분 기준",
             d2="TrendForce 추정"),
        dict(color=BLUE, fillbg=(14,24,44), label="낙관적",
             headline="월 4만 장 → 연환산 약 53억 달러",
             d1="보도된 완전가동 목표 캐파 기준",
             d2="1γ D램 포함 가능성 있어 상한으로 취급"),
        dict(color=CYAN, fillbg=(8,28,34), label="비중",
             headline="전체 매출의 약 2~3%대",
             d1="최근분기 연환산 1,660억 기준 2.0~3.2%",
             d2="가이던스 연환산 2,000억 기준 1.65~2.65%"),
    ], FOOTER,
)

# 6. 회수기간
make_card(
    "2026-07-06_투자회수기간.png", ORANGE,
    "93억 걸고 몇 년 만에 회수하나",
    "봉투 뒷면 계산 — 정밀 모델 아님",
    [
        dict(color=AMBER, fillbg=(40,28,10), label="실부담",
             headline="93억 − 보조금 35억 = 약 58억 달러",
             d1="일본 정부가 투자액의 상당 부분을 대납",
             d2="자기자본 부담을 줄이는 효율적인 딜"),
        dict(color=GREEN, fillbg=(10,34,26), label="연매출",
             headline="신공장 연매출 추정 33억~53억 달러",
             d1="HBM은 마진이 가장 높은 제품군",
             d2="회사 전체 GM 가이던스 사이클 정점 80%대"),
        dict(color=ORANGE, fillbg=(40,22,10), label="회수기간",
             headline="매출 기준 약 1~2년",
             d1="매출 비중은 작아도(2~3%) 회수는 빠른 편",
             d2="이익 기준 회수는 매출 기준보다 더 걸림"),
    ], FOOTER,
)
