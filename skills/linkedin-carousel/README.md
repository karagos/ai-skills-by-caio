# LinkedIn Carousel

Generate on-brand LinkedIn carousel PDFs (1080x1350) from raw text, URLs, or uploaded documents. Four templates, fully brandable through a single YAML config.

Built by [Stefanos Karagos](https://www.linkedin.com/in/karagos/), Lead Instructor & Senior GenAI Consultant at [CAIO Group](https://wearecaio.com).

---

## What it does

Turns a content brief into a 7-page PDF ready to upload as a LinkedIn document post. Four layout templates are available, all driven by the same content JSON and brand config.

- **executive-minimal**: clean typography, orange accent, for strategic takes
- **training-breakdown**: numbered step cards, dual-purpose for in-room training
- **quote-forward**: alternating full-bleed slides with big pull quotes
- **mobile-optimized**: oversized type with highlighted keywords, tuned for phone reading

All four share the brand palette from `brand-config.yaml`. Edit that one file and every carousel you generate matches your personal or company brand.

## How to trigger (once installed)

Say any of:

- "make a LinkedIn carousel about X"
- "build a 7-slide LinkedIn post on X"
- "turn this article into a carousel"
- "create a training breakdown on X"

## First-time setup

**1. Personalize your brand**

Edit `brand-config.yaml`:

```yaml
brand:
  owner_name: "Your Name"
  company: "Your Company"
  website: "yourwebsite.com"
  positioning: "Your Role / Tagline"
  footer_line: "your name | yourwebsite.com"

palettes:
  brand:
    primary: "#d97757"     # swap for your brand color
    ...
```

**2. Drop in your assets** (optional but recommended)

- `assets/logo.svg` (or `.png`): your brand logo
- `assets/headshot.png`: square headshot, 500x500 minimum

If `headshot.png` is missing, the CTA slide falls back to your initials on a colored circle.

**3. Install dependencies**

One-time:

```bash
pip install playwright jinja2 pyyaml --break-system-packages
python3 -m playwright install chromium
```

## Test it

```bash
python3 scripts/render.py \
  --content examples/sample-content.json \
  --brand-config brand-config.yaml \
  --template executive-minimal \
  --output /tmp/test-carousel.pdf
```

Open `/tmp/test-carousel.pdf`. You should see a 7-page carousel with your brand applied.

## Content structure

Carousels follow a standard arc:

1. **Cover**: bold hook sentence that stops the scroll
2. **Body slides (3-7)**: one idea per slide, no crowding
3. **Takeaway**: the one thing to remember
4. **CTA**: simple ask plus your website

Templates render the arc automatically. You just provide the content.

## Files in this skill

```
linkedin-carousel/
├── SKILL.md              # Triggers and workflow for Claude
├── brand-config.yaml     # Your brand: colors, fonts, footer, assets
├── templates/            # 4 Jinja2 HTML templates
├── scripts/render.py     # HTML to PDF renderer (Playwright)
├── assets/               # Drop logo.svg and headshot.png here
└── examples/             # Sample content JSON
```

## Design rules

The skill enforces three rules before every render:

1. **No em dashes.** Auto-replaced with colons.
2. **No AI filler phrases.** "delve into", "navigate", "landscape", "leverage", "moreover", "furthermore", "additionally" get flagged.
3. **No hedging words.** "somewhat", "relatively", "fairly", "quite" get flagged.

The goal is executive-grade copy that reads naturally when spoken out loud.

## License

MIT. See the root repo LICENSE.
