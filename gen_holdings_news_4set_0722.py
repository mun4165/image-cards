from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-22"
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

# ── 1. AMD-MS 헬리오스 ──────────────────────────
img, draw = base_canvas(RED)
draw.text((32,22), "AMD 7.9% 급등, MS가 헬리오스를 애저에 넣었다", font=bold(28), fill=RED)
draw.text((32,76), "7/20 발표, 마이크로소프트가 4번째 헬리오스 대형 고객으로 확인", font=bold(18), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, RED, (40,14,14), "헬리오스란",
     "MI455X + EPYC 베니스 + 펜산도 + ROCm 통합 랙", "AMD 첫 랙스케일 AI 시스템, 엔비디아 대항마")
band(draw, by+step, bh, AMBER, (40,28,10), "이번 고객",
     "마이크로소프트, 메타·오픈AI·오라클 이어 4번째", "애저 데이터센터에 배치, 하반기 출하 시작")
band(draw, by+step*2, bh, BLUE, (10,20,40), "추가 계약",
     "EPYC 베니스 신규 VM 2종, HDv2·HXv2", "에이전틱 AI·데이터파이프라인 / 반도체설계용")
band(draw, by+step*3, bh, GREEN, (10,30,22), "주가 반응",
     "7/20 종가 543.10달러, +7.9%", "출하는 하반기부터, 매출 인식은 다음 분기 확인")
footer(draw, "2026.07.22  |  AMD")
out = os.path.join(OUT_DIR, "2026-07-22_AMD_MS_헬리오스.png")
img.save(out); print("Saved:", out)

# ── 2. 마이크론·샌디스크 메모리랠리 ──────────────────────────
img, draw = base_canvas(CYAN)
draw.text((32,22), "마이크론 12% 급등, 목표가 1,550달러가 말하는 79%", font=bold(28), fill=CYAN)
draw.text((32,76), "7/21, BofA 베스트픽 편입 + 모건스탠리 가격전망 동시 재료", font=bold(18), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, CYAN, (8,28,34), "마이크론(MU)",
     "7/20 865.46달러 → 7/21 970.82달러, +12.17%", "BofA 목표가 1,500→1,550달러, 베스트 아이디어 편입")
band(draw, by+step, bh, AMBER, (40,28,10), "BofA 논리",
     "저비용 오픈소스 AI모델 확산이 HBM 수요를 늘린다", "폐쇄형 모델 집중보다 추론 수요가 더 분산·확대")
band(draw, by+step*2, bh, GREEN, (10,30,22), "모건스탠리",
     "26년 2Q 대비 3Q 메모리 가격 최소 25% 상승 전망", "공급제약 + 데이터센터 수요 근거")
band(draw, by+step*3, bh, ORANGE, (40,22,10), "동반 상승",
     "샌디스크 +8%(1,504달러), 웨스턴디지털 +9%(531달러)", "메모리 밸류체인 전반 동반 반응")
footer(draw, "2026.07.22  |  MU  SNDK  WDC")
out = os.path.join(OUT_DIR, "2026-07-22_MU_SNDK_메모리랠리.png")
img.save(out); print("Saved:", out)

# ── 3. SIVE 락업만료 CEO매수 ──────────────────────────
img, draw = base_canvas(GREEN)
draw.text((32,22), "Sivers 락업 만료, CEO는 오히려 7만주를 더 샀다", font=bold(28), fill=GREEN)
draw.text((32,76), "7/16 락업 해제, 내부자 매도 우려와 반대로 간 사례", font=bold(18), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, GREEN, (10,30,22), "락업 배경",
     "4/16 약 7억 SEK 유상증자, 이사·경영진 매도제한", "약정 만료일 7월 16일")
band(draw, by+step, bh, CYAN, (8,28,34), "CEO 빅크람 바툴야",
     "락업 해제 직후 7만주 추가매수, 총 454만76주", "7/13 이사회 전원 매수 흐름도 이미 확인됨")
band(draw, by+step*2, bh, AMBER, (40,28,10), "의장 바스타니",
     "27.5만주 매도, 그중 6만주 기부·7만주 가족증여", "잔여 38.1만주 보유, 순수 현금화 아님")
band(draw, by+step*3, bh, BLUE, (10,20,40), "맥락",
     "나스닥 이중상장 추진 중, 최근 매출은 전년比 감소", "내부자 행동이 몇 안 되는 직접 신호")
footer(draw, "2026.07.22  |  SIVE")
out = os.path.join(OUT_DIR, "2026-07-22_SIVE_CEO매수.png")
img.save(out); print("Saved:", out)

# ── 4. IQE 매출 가이던스 상향 ──────────────────────────
img, draw = base_canvas(ORANGE)
draw.text((32,22), "IQE 28.96% 급등, 가이던스 20%에서 30%로", font=bold(28), fill=ORANGE)
draw.text((32,76), "7/21 트레이딩 업데이트, InP 수요가 이끈 상반기 41% 성장", font=bold(18), fill=GRAY)
draw.line([(32,116),(W-32,116)], fill=DARK_GRAY, width=1)
by, bh, step = 136, 130, 144
band(draw, by, bh, ORANGE, (40,22,10), "상반기 실적",
     "매출 최소 6,400만 파운드, 전년比 약 41% 성장", "예상치 상회, 은행부채 없음·현금 4,160만 파운드")
band(draw, by+step, bh, CYAN, (8,28,34), "가이던스 상향",
     "연간 매출성장률 20%↑ → 30%↑ 로 상향", "조정 EBITDA 낮은 두 자릿수 백만 파운드 전망")
band(draw, by+step*2, bh, GREEN, (10,30,22), "성장 축",
     "InP(인듐인화물) 기판, AI데이터센터 광학부품 수요", "항공우주·방산, 3D센싱·무선 부문도 동반 강세")
band(draw, by+step*3, bh, AMBER, (40,28,10), "주가 반응",
     "46.60펜스 마감, +28.96%", "정식 반기실적·하반기 가이던스 달성 여부가 다음 확인점")
footer(draw, "2026.07.22  |  IQE")
out = os.path.join(OUT_DIR, "2026-07-22_IQE_가이던스상향.png")
img.save(out); print("Saved:", out)
