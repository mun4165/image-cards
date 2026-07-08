from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT_DIR = "/Users/munjinhyeok/Desktop/Think-Tank/04_output/이미지사용/2026-07-06"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1280, 720
BG=(13,17,23); GRID=(255,255,255,12); WHITE=(255,255,255); GRAY=(140,150,165)
DARK_GRAY=(60,70,82); ROW_A=(18,23,30); ROW_B=(24,30,39); HILITE=(20,32,30)
BLUE=(59,130,246); TEAL=(20,184,166)

def font(size, index=0): return ImageFont.truetype(FONT_PATH, size, index=index)
def bold(size): return ImageFont.truetype(FONT_PATH, size, index=4)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")
for x in range(0, W, 80): draw.line([(x,0),(x,H)], fill=GRID, width=1)
for y in range(0, H, 80): draw.line([(0,y),(W,y)], fill=GRID, width=1)
draw.rectangle([0,0,W,4], fill=TEAL); draw.rectangle([0,0,4,H], fill=TEAL)

draw.text((32,24), "메모리는 셋뿐? 디램 얘기다", font=bold(36), fill=TEAL)
draw.text((32,80), "회사별 점유율 — 디램 · 낸드 · HBM", font=bold(24), fill=GRAY)
draw.line([(32,128),(W-32,128)], fill=DARK_GRAY, width=1)

cols = [("회사", 32, 280), ("디램\n(2026 1Q)", 312, 300), ("낸드\n(2025 3Q)", 612, 300), ("HBM\n(2026)", 912, 336)]
rows = [
    ("삼성",        "38.6%",            "32.3%",             "약 25~30%(2위)", False),
    ("SK하이닉스",   "28.8%",            "약 19%(솔리다임 포함)", "약 50%(1위)",    False),
    ("마이크론",     "22.4%",            "약 13%(4위)",         "약 15~20%(3위)", True),
    ("키옥시아",     "—",                "약 15%",             "—",             False),
    ("샌디스크",     "—",                "약 12%",             "—",             False),
    ("CXMT 등 기타", "약 10%",           "—",                  "—",             False),
]

header_y, header_h = 150, 56
for label, x, w in cols:
    draw.text((x, header_y+8), label, font=bold(19), fill=GRAY)
draw.line([(32, header_y+header_h), (W-32, header_y+header_h)], fill=DARK_GRAY, width=1)

row_y = header_y + header_h + 6
row_h = 70
for i, (name, dram, nand, hbm, hilite) in enumerate(rows):
    y0 = row_y + i*row_h
    bg = HILITE if hilite else (ROW_A if i % 2 == 0 else ROW_B)
    draw.rectangle([32, y0, W-32, y0+row_h-6], fill=bg)
    if hilite:
        draw.rectangle([32, y0, 38, y0+row_h-6], fill=TEAL)
    name_font = bold(26) if hilite else font(24)
    name_color = TEAL if hilite else WHITE
    draw.text((60 if hilite else 32+16, y0+row_h//2-18), name, font=name_font, fill=name_color)
    val_font = bold(23) if hilite else font(22)
    val_color = WHITE if hilite else (GRAY if dram == "—" else WHITE)
    draw.text((312+8, y0+row_h//2-14), dram, font=val_font, fill=(GRAY if dram=="—" else val_color))
    draw.text((612+8, y0+row_h//2-14), nand, font=val_font, fill=(GRAY if nand=="—" else val_color))
    draw.text((912+8, y0+row_h//2-14), hbm, font=val_font, fill=(GRAY if hbm=="—" else val_color))

note_y = row_y + row_h*len(rows) + 14
draw.text((32, note_y), "HBM 점유율은 집계마다 편차가 크고, 분기에 따라 삼성·마이크론 순위가 뒤바뀌기도 한다.", font=font(16), fill=GRAY)

draw.line([(32,H-30),(W-32,H-30)], fill=DARK_GRAY, width=1)
draw.text((32,H-22), "2026.07.06  |  $MU  Micron Technology", font=font(15), fill=GRAY)

out = os.path.join(OUT_DIR, "2026-07-06_메모리3사점유율표.png")
img.save(out)
print("Saved:", out)
