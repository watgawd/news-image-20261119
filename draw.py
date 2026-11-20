#!/usr/bin/env python3
"""Draw entry.png for news-image-20261119: a newspaper front page summing up
Thursday 19 November 2026, rendered with Pillow only. Run: python3 draw.py
Writes entry.png (1024x1024, under 1 MiB) next to this file."""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (246, 241, 231)
INK = (20, 28, 46)
NAVY = (30, 58, 95)
RED = (185, 28, 28)
GOLD = (201, 162, 39)
GREY = (90, 92, 98)
CARD = (255, 255, 255)
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

DATE = "THURSDAY 19 NOVEMBER 2026"
KICKER = "THE WORLD IN ONE DAY  •  WORLD NEWS"
HERO_TAG = "THE HAGUE  •  WORLD COURT"
HERO_HEAD = "WORLD COURT: MYANMAR GUILTY OF GENOCIDE"
HERO_SUB = "ICJ rules 9-6: the army acted with genocidal intent against the Rohingya in Rakhine"
CARDS = [
    ("SHENZHEN", (30, 58, 95), "Trump, Xi and Putin hold first three-way summit",
     "Leaders sign a joint peace declaration; Ukraine and Iran go unmentioned"),
    ("THE GULF", (185, 28, 28), "Iran widens attacks across the Gulf",
     "Strikes hit Kuwait and Bahrain; a tanker is attacked in the Strait of Hormuz"),
    ("ANTALYA", (46, 125, 50), "COP31 talks race to unblock climate deal",
     "Ministers meet late into the night to bridge gaps on a final text"),
    ("BRUSSELS", (30, 58, 95), "EU proposes a \u20ac45bn loan to Ukraine",
     "New funding to keep Kyiv supplied through the war"),
    ("DHAKA", (185, 28, 28), "Violence spreads across Bangladesh",
     "Yunus's ancestral home is torched; unrest hits 28 districts"),
    ("SPACE", (90, 60, 140), "Voyager 1 reaches one light-day from Earth",
     "The first craft ever to fly a light-day from home"),
]
FOOTER = ("ALSO: Van Gogh sells for a record $190.4m  •  US Senate rejects Iran "
          "war-powers measure 51-48  •  Migrant boat sinks off Senegal")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def globe(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255), width=4)
    for k in (-0.55, 0.0, 0.55):
        w = int(r * abs(k) * 2) if k else 6
        draw.ellipse([cx - w // 2, cy - r, cx + w // 2, cy + r],
                     outline=(255, 255, 255), width=3)
    draw.line([cx - r, cy, cx + r, cy], fill=(255, 255, 255), width=3)
    draw.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 200, 340,
             fill=GOLD, width=4)


def fit_font(path, text, size, max_w):
    d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    f = font(path, size)
    while d.textlength(text, font=f) > max_w and size > 10:
        size -= 1
        f = font(path, size)
    return f


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # Masthead
    d.line([36, 26, W - 36, 26], fill=INK, width=3)
    f_kick = font(SANSB, 23)
    d.text((W // 2, 44), KICKER, font=f_kick, fill=RED, anchor="ma")
    f_date = fit_font(SERIF, DATE, 56, W - 72)
    d.text((W // 2, 84), DATE, font=f_date, fill=INK, anchor="ma")
    d.line([36, 158, W - 36, 158], fill=INK, width=3)
    # Hero panel
    d.rounded_rectangle([36, 176, W - 36, 412], radius=10, fill=NAVY)
    f_tag = font(SANSB, 21)
    d.text((64, 196), HERO_TAG, font=f_tag, fill=GOLD)
    f_head = font(SERIF, 40)
    lines = wrap(d, HERO_HEAD, f_head, 660)
    y = 226
    for ln in lines:
        d.text((64, y), ln, font=f_head, fill=(255, 255, 255))
        y += 48
    f_sub = font(SANS, 23)
    for ln in wrap(d, HERO_SUB, f_sub, 660):
        d.text((64, y + 6), ln, font=f_sub, fill=(205, 210, 220))
        y += 30
    globe(d, 852, 294, 88)
    # Story grid: 2 columns x 3 rows
    gx, gy, gw, gh, gap = 36, 424, 466, 160, 18
    f_ctag = font(SANSB, 19)
    f_chead = font(SANSB, 27)
    f_csub = font(SANS, 19)
    for i, (tag, color, head, sub) in enumerate(CARDS):
        x = gx + (i % 2) * (gw + gap)
        y = gy + (i // 2) * (gh + gap)
        d.rounded_rectangle([x, y, x + gw, y + gh], radius=8, fill=CARD,
                            outline=(200, 195, 180), width=1)
        d.rectangle([x, y + 10, x + 8, y + gh - 10], fill=color)
        d.text((x + 24, y + 12), tag, font=f_ctag, fill=color)
        ly = y + 40
        for ln in wrap(d, head, f_chead, gw - 44)[:2]:
            d.text((x + 24, ly), ln, font=f_chead, fill=INK)
            ly += 31
        for ln in wrap(d, sub, f_csub, gw - 44)[:2]:
            d.text((x + 24, ly + 4), ln, font=f_csub, fill=GREY)
            ly += 23
    # Footer
    d.line([36, 958, W - 36, 958], fill=INK, width=2)
    f_foot = font(SANS, 19)
    fy = 970
    for ln in wrap(d, FOOTER, f_foot, W - 72):
        d.text((W // 2, fy), ln, font=f_foot, fill=INK, anchor="ma")
        fy += 24
    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
