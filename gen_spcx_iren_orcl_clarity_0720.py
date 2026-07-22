from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-20"
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
    draw.text((60, y+14), label, font=bold(19), fill=color)
    draw.line([(196,y+14),(196,y+h-14)], fill=DARK_GRAY, width=1)
    draw.text((220, y+15), headline, font=bold(19), fill=WHITE)
    draw.text((220, y+46), detail, font=font(15), fill=color)

def footer(draw, text):
    draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
    draw.text((32,H-22), text, font=font(15), fill=GRAY)

# ── 1. 스페이스X 상장 정정 ──────────────────────────
img, draw = base_canvas(BLUE)
draw.text((32,22), "스페이스X, 이미 상장한 지 한 달 지났다", font=bold(34), fill=BLUE)
draw.text((32,76), "\"비상장이라 락업 풀리면 산다\"는 전제가 6월 12일에 깨졌다", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, GREEN, (10,30,22), "상장",
     "2026.6.12 나스닥 SPCX 상장, 공모가 135달러", "첫날 종가 160.95달러, 시총 약 2.1조 달러")
band(draw, by+step, bh, CYAN, (8,28,34), "밸류 연혁",
     "24.12 3,500억 → 25.12 8,000억 → 26.2 1.25조 달러", "xAI 합병 후 26.6 상장 시 1.77조 달러")
band(draw, by+step*2, bh, AMBER, (40,28,10), "락업",
     "2분기 실적 발표 후 보호예수 20% 해제 예정", "시점은 7월 말 거론, 1차 공시 대조는 미확인")
band(draw, by+step*3, bh, RED, (40,14,14), "핵심",
     "지금 매매 안 되는 게 아니라 이미 상장주다", "해제 물량발 단기 변동성을 기다리는 것뿐")
footer(draw, "2026.07.20  |  SPCX")
out = os.path.join(OUT_DIR, "2026-07-20_스페이스X_상장정정.png")
img.save(out); print("Saved:", out)

# ── 2. IREN×뉴욕 데이터센터 ──────────────────────────
img, draw = base_canvas(TEAL)
draw.text((32,22), "뉴욕 데이터센터 전면 동결, 근데 아이렌은 없다", font=bold(34), fill=TEAL)
draw.text((32,76), "행정명령 62호는 실재, 아이렌 자산과의 연결고리는 실재하지 않는다", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, RED, (40,14,14), "뉴욕주",
     "7/14 행정명령 62호, 50MW 이상 인허가 최대 1년 동결", "전국 최초 주 단위 데이터센터 모라토리엄")
band(draw, by+step, bh, AMBER, (40,28,10), "시위",
     "7/18 125개 도시 동시다발 반대시위(HumansFirst)", "누적 980억 달러 규모 프로젝트 저지 주장")
band(draw, by+step*2, bh, GREEN, (10,30,22), "아이렌 자산",
     "텍사스 2곳·오클라호마·캐나다 3곳, 총 6곳", "뉴욕주 소재 자산 0곳 — 직접 연결 근거 없음")
band(draw, by+step*3, bh, CYAN, (8,28,34), "관전포인트",
     "섹터 전체 정치 리스크 프리미엄 확대 여부", "특정 회사와 특정 지역, 자산 소재지부터 확인")
footer(draw, "2026.07.20  |  IREN")
out = os.path.join(OUT_DIR, "2026-07-20_아이렌_뉴욕무관.png")
img.save(out); print("Saved:", out)

# ── 3. 오라클 RPO·부채 팩트체크 ──────────────────────────
img, draw = base_canvas(ORANGE)
draw.text((32,22), "오라클 RPO 638억 달러, '최대 부채'는 근거 미확인", font=bold(32), fill=ORANGE)
draw.text((32,76), "수주 잔고 증가는 공식 확인, 부채 순위 1위 주장은 출처가 안 나왔다", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, GREEN, (10,30,22), "RPO",
     "26FY 4Q 기준 638억 달러, 전년비 +363%", "GPU 인프라 선불 750억 달러 포함, 12개월내 12% 인식")
band(draw, by+step, bh, AMBER, (40,28,10), "부채 주장",
     "\"미국 상장사 중 부채 최대\" — 순위 근거 못 찾음", "빅테크 내 비교(MS·AMZN)를 전체 시장으로 과장 가능성")
band(draw, by+step*2, bh, RED, (40,14,14), "총부채",
     "소스마다 1,223억~1,622억 달러로 상이", "10-K 원문 대조 필요, 시점 기준 불일치")
band(draw, by+step*3, bh, CYAN, (8,28,34), "버리 숏 정리설",
     "13F 아님 — 사이언운용 25.11 SEC 등록 자진해지", "개인 서브스택 자발적 공개, 법적 공시 아님")
footer(draw, "2026.07.20  |  ORCL")
out = os.path.join(OUT_DIR, "2026-07-20_오라클_RPO팩트체크.png")
img.save(out); print("Saved:", out)

# ── 4. CLARITY Act 청문회 ──────────────────────────
img, draw = base_canvas(RED)
draw.text((32,22), "스테이블코인법 청문회, 민주당 의원 0명 참석", font=bold(34), fill=RED)
draw.text((32,76), "하원은 이미 통과, 문제는 상원 — 통과 확률 34~43%로 하락", font=bold(19), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, RED, (40,14,14), "청문회",
     "7/17 뉴욕 필드 청문회, 민주당 의원 전원 불참", "\"No Democrats Show Up\" — 조직적 보이콧 여부는 불명")
band(draw, by+step, bh, GREEN, (10,30,22), "하원",
     "25.7.17 294:134 통과, 민주당 78명 찬성 포함", "초당적 지지로 이미 하원 문턱은 넘은 상태")
band(draw, by+step*2, bh, AMBER, (40,28,10), "상원",
     "은행위 5/14 15:9 가결, 본회의 상정은 계속 지연", "8/8 휴회 전 처리 목표, 예측시장 확률 34~43%")
band(draw, by+step*3, bh, CYAN, (8,28,34), "서클 영향",
     "규제 명확성 지연 = 불확실성 장기화", "연내 통과 낙관론은 이번 청문회로 근거 약해짐")
footer(draw, "2026.07.20  |  CLARITY Act / CIRCLE")
out = os.path.join(OUT_DIR, "2026-07-20_CLARITY_ACT_청문회.png")
img.save(out); print("Saved:", out)
