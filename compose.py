#!/usr/bin/env python3
"""Build entry.png for make.fun news-image-20261121.

A newspaper front page summing up Saturday 21 November 2026. The lead story
— Russian missiles landing in NATO member Poland during the war's biggest
barrage on Ukraine — gets the hero illustration and a full-width lead card;
five more stories from five other regions/fields fill the cards below, so the
page reads as the whole day, not one beat. All text is rendered with PIL for
crisp, legible type; the hero is an AI illustration with no text in it.

Run: python3 compose.py  -> writes entry.png next to this file.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

NAVY = (20, 33, 61)
GOLD = (198, 160, 38)
CREAM = (246, 242, 233)
PAPER = (255, 253, 247)
INK = (22, 26, 36)
MUTED = (88, 94, 108)
RULE = (208, 203, 188)
RED = (158, 32, 32)

HERO_PATH = "assets/media-generation-hero-poland-missiles-0-1008dfe1-8fe2-467b-8c4b-5a74cf881553.png"

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def load(path, size):
    return ImageFont.truetype(path, size)


def wrap_lines(draw, text, font, max_width):
    """Greedy word wrap returning a list of lines fitting max_width."""
    lines, current = [], ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def centred(draw, text, font, y, colour, cx=W // 2):
    draw.text((cx - draw.textlength(text, font=font) / 2, y), text,
              font=font, fill=colour)


def story_card(draw, x, y, w, h, tag, colour, headline, summary,
               tag_size=15, head_size=24, sum_size=17, numbered=None):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10,
                           fill=PAPER, outline=RULE, width=1)
    draw.rectangle([x, y + 8, x + 6, y + h - 8], fill=colour)
    tx = x + 20
    if numbered is not None:
        num_font = load(SANS_BOLD, 18)
        draw.ellipse([x + w - 42, y + 12, x + w - 12, y + 42], fill=colour)
        label = str(numbered)
        draw.text((x + w - 27 - draw.textlength(label, font=num_font) / 2,
                   y + 15), label, font=num_font, fill=(255, 255, 255))
    draw.text((tx, y + 12), tag, font=load(SANS_BOLD, tag_size), fill=colour)
    head_font = load(SANS_BOLD, head_size)
    for i, line in enumerate(wrap_lines(draw, headline, head_font, w - 40)[:1]):
        draw.text((tx, y + 38 + i * 30), line, font=head_font, fill=INK)
    sum_font = load(SANS, sum_size)
    sy = y + 70
    for line in wrap_lines(draw, summary, sum_font, w - 40)[:2]:
        draw.text((tx, sy), line, font=sum_font, fill=MUTED)
        sy += 23


LEAD = (
    "WAR · POLAND / UKRAINE",
    "RUSSIAN MISSILES LAND IN NATO POLAND",
    "Kh-101 missiles crash in south-east Poland during Russia's "
    "400-drone, 110-missile barrage on Ukraine; 8 killed. Tusk calls it "
    "a provocation; NATO's Rutte calls it a \u201cgrave violation\u201d.",
)

SUPPORTING = [
    ("MIDDLE EAST · HORMUZ", (31, 93, 140), "TANKERS HIT IN HORMUZ",
     "Bahrain blames Iran for a strike on an industrial site; two tankers "
     "are hit and oil shipments through the strait fall 15%."),
    ("MARKETS · NEW YORK", (176, 84, 24), "NASDAQ ERASES 2026 GAINS",
     "A tech sell-off pushes the S&P 500 into correction; Anthropic shares "
     "slide days after its Nasdaq debut."),
    ("SOUTH AMERICA · PERU", (46, 110, 58), "EARTHQUAKE STRIKES PERU",
     "A strong quake shakes central Peru; residents rush outdoors as "
     "tremors roll through the Andes."),
    ("NORTH AMERICA · MEXICO", (90, 60, 120), "CARTEL BOSS CAPTURED",
     "Mexico's army seizes FBI most-wanted fugitive \u201cEl Chapo "
     "Isidro\u201d after a deadly firefight in Sinaloa."),
    ("TRADE · BRUSSELS", (14, 122, 102), "EU\u2013INDONESIA TRADE DEAL",
     "After a decade of talks, the EU and Indonesia sign a deal removing "
     "98.5% of tariffs between them."),
]


def main():
    page = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(page)

    # Masthead.
    draw.rectangle([0, 0, W, 96], fill=NAVY)
    draw.rectangle([0, 96, W, 100], fill=GOLD)
    centred(draw, "THE WORLD IN ONE DAY", load(SERIF_BOLD, 46), 10,
            (247, 243, 234))
    centred(draw, "SATURDAY \u00b7 21 NOVEMBER 2026", load(SANS_BOLD, 25),
            62, (216, 178, 74))

    # Hero: centre-crop the wide illustration to the 1024x280 banner.
    hero = Image.open(HERO_PATH).convert("RGB")
    hw, hh = hero.size
    target = 1024 / 280
    if hw / hh > target:
        new_w = int(hh * target)
        left = (hw - new_w) // 2
        hero = hero.crop((left, 0, left + new_w, hh))
    else:
        new_h = int(hw / target)
        top = (hh - new_h) // 2
        hero = hero.crop((0, top, hw, top + new_h))
    hero = hero.resize((1024, 280), Image.LANCZOS)
    page.paste(hero, (0, 100))
    draw = ImageDraw.Draw(page)
    draw.rectangle([0, 380, W, 384], fill=GOLD)

    # Lead story, full width.
    margin = 24
    lx, ly, lw, lh = margin, 396, W - 2 * margin, 144
    draw.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=10,
                           fill=PAPER, outline=RULE, width=1)
    draw.rectangle([lx, ly + 8, lx + 6, ly + lh - 8], fill=RED)
    num_font = load(SANS_BOLD, 18)
    draw.ellipse([lx + lw - 42, ly + 12, lx + lw - 12, ly + 42], fill=RED)
    draw.text((lx + lw - 27 - draw.textlength("1", font=num_font) / 2,
               ly + 15), "1", font=num_font, fill=(255, 255, 255))
    tag, headline, summary = LEAD
    tx = lx + 20
    draw.text((tx, ly + 12), tag, font=load(SANS_BOLD, 16), fill=RED)
    head_font = load(SANS_BOLD, 30)
    draw.text((tx, ly + 38), headline, font=head_font, fill=INK)
    sum_font = load(SANS, 18)
    sy = ly + 80
    for line in wrap_lines(draw, summary, sum_font, lw - 40)[:2]:
        draw.text((tx, sy), line, font=sum_font, fill=MUTED)
        sy += 24

    # Supporting stories: two rows of two, then one full-width card.
    card_w = (W - 2 * margin - 16) // 2
    card_h = 132
    top = 552
    for i, (tag, colour, headline, summary) in enumerate(SUPPORTING[:4]):
        col, row = i % 2, i // 2
        story_card(draw, margin + col * (card_w + 16), top + row * (card_h + 12),
                   card_w, card_h, tag, colour, headline, summary,
                   numbered=i + 2)
    tag, colour, headline, summary = SUPPORTING[4]
    story_card(draw, margin, top + 2 * (card_h + 12), W - 2 * margin, card_h,
               tag, colour, headline, summary, numbered=6)

    # Footer.
    foot = ("Six stories that defined the day \u2014 reported 21 November 2026 "
            "\u00b7 Reuters \u00b7 AP \u00b7 France 24")
    centred(draw, foot, load(SANS, 15), 992, MUTED)

    page.save("entry.png", optimize=True)
    print("wrote entry.png", page.size)


if __name__ == "__main__":
    main()
