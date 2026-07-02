from PIL import Image, ImageDraw, ImageFont
import os, math

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-02"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); AMBER=(245,158,11); TEAL=(20,184,166); BLUE=(59,130,246)
CYAN=(6,182,212); GREEN=(52,211,153); ORANGE=(249,115,22); RED=(248,113,113)
ACCENT = CYAN

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG); draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=ACCENT); draw.rectangle([0,0,4,H], fill=ACCENT)

draw.text((32,22), "스마일 커브 — 픽셀은 왜 가장 적게 버는가", font=bold(36), fill=ACCENT)
draw.text((32,74), "가치사슬의 양 끝은 높고, 가운데(제조)만 낮다 — 세틀로직은 정확히 그 가운데다", font=bold(19), fill=GRAY)
draw.line([(32,112),(W-32,112)], fill=DARK_GRAY, width=1)

# --- Smile curve plot area ---
plot_x0, plot_x1 = 140, W-140
plot_y_top, plot_y_bottom = 175, 460   # top = high margin, bottom = low margin

def curve_y2(t):
    # smile shape: high margin (small y, near top) at both ends, low margin (large y, near bottom) at center
    depth = plot_y_bottom - plot_y_top
    return plot_y_bottom - depth * (4*(t-0.5)**2)

# axis baseline
draw.line([(plot_x0-20, plot_y_bottom+30),(plot_x1+20, plot_y_bottom+30)], fill=DARK_GRAY, width=2)
draw.text((plot_x0-20, plot_y_bottom+40), "가치사슬 위치 (왼쪽=설계 · 가운데=제조 · 오른쪽=브랜드/서비스)", font=font(15), fill=GRAY)
draw.text((plot_x0-115, plot_y_top-10), "높은\n부가가치", font=font(14), fill=GRAY)
draw.text((plot_x0-115, plot_y_bottom-14), "낮은\n부가가치", font=font(14), fill=GRAY)

# draw smile curve as smooth polyline
pts = []
N = 200
for i in range(N+1):
    t = i/N
    x = plot_x0 + t*(plot_x1-plot_x0)
    y = curve_y2(t)
    pts.append((x,y))
for i in range(len(pts)-1):
    draw.line([pts[i], pts[i+1]], fill=ACCENT, width=5)

# shade under curve
poly = pts + [(plot_x1, plot_y_bottom+30), (plot_x0, plot_y_bottom+30)]
draw.polygon(poly, fill=(6,182,212,22))

def marker(t, color, label_lines, label_color, above=True):
    x = plot_x0 + t*(plot_x1-plot_x0)
    y = curve_y2(t)
    r = 9
    draw.ellipse([x-r,y-r,x+r,y+r], fill=color, outline=WHITE, width=2)
    ly = y - 78 if above else y + 22
    lx = x - 90 if t < 0.5 else (x - 180 if t > 0.6 else x - 90)
    for i, line in enumerate(label_lines):
        f = bold(19) if i == 0 else font(16)
        c = WHITE if i == 0 else label_color
        draw.text((lx, ly + i*26), line, font=f, fill=c)

# left end: design / core tech (generic, low SATL relevance)
marker(0.03, GRAY, ["설계·핵심기술", "고부가가치 구간"], GRAY, above=True)

# center: manufacturing = pixel capture = SATL
marker(0.5, RED, ["세틀로직  매출 $17.7M", "가장 싸게 찍지만 가장 적게 번다"], RED, above=False)

# right end: brand/service = analytics = BlackSky
marker(0.97, GREEN, ["BlackSky  매출 $106.6M", "Spectra AI로 해석을 팔아 6배"], GREEN, above=True)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.02  |  FY2025 매출, stockanalysis.com  |  스탠 시(1992) 스마일 커브 · 픽셀의 파운드리 관점", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-02_SATL_스마일커브.png")
img.save(out); print("Saved:", out)
