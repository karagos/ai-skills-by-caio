#!/usr/bin/env python3
"""
CAIO LinkedIn Carousel Renderer

Takes a content JSON + brand config, renders the chosen Jinja2 template,
and outputs a multi-page PDF (1080x1350 per page) ready for LinkedIn
document posts.

Usage:
  python3 render.py \
    --content /path/to/content.json \
    --brand-config /path/to/brand-config.yaml \
    --template executive-minimal \
    --palette brand \
    --output /path/to/output.pdf

If --template or --palette are in the content JSON, CLI flags override them.
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import json
import re
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATE_NAMES = [
    "executive-minimal",
    "training-breakdown",
    "quote-forward",
    "mobile-optimized",
]
PALETTES = ["brand", "mobile"]

# ------------ Copy hygiene -------------------------------------------------

FORBIDDEN_PHRASE_REGEX = None  # built at runtime from brand config


def scrub_text(text: str, copy_rules: dict) -> tuple[str, list[str]]:
    """Remove em dashes and warn about forbidden phrases. Returns (cleaned, warnings)."""
    if not isinstance(text, str):
        return text, []
    warnings: list[str] = []

    # Em dash auto-fix: replace with period + space or colon based on context.
    # Simple heuristic: after a word and before a lowercase word, use colon. Else period.
    if "—" in text:
        def replace_em(match: re.Match) -> str:
            return ": "
        text = re.sub(r"\s*—\s*", ": ", text)
        warnings.append("em dash auto-replaced with colon")

    for phrase in copy_rules.get("forbidden_phrases", []):
        if re.search(rf"\b{re.escape(phrase)}\b", text, flags=re.IGNORECASE):
            warnings.append(f"forbidden phrase detected: {phrase!r}")

    return text, warnings


def scrub_content(content: dict, copy_rules: dict) -> tuple[dict, list[str]]:
    warnings: list[str] = []

    def walk(value):
        if isinstance(value, dict):
            return {k: walk(v) for k, v in value.items()}
        if isinstance(value, list):
            return [walk(v) for v in value]
        if isinstance(value, str):
            cleaned, w = scrub_text(value, copy_rules)
            warnings.extend(w)
            return cleaned
        return value

    cleaned = walk(content)
    return cleaned, warnings


# ------------ Rendering ----------------------------------------------------


def load_inputs(content_path: Path, brand_config_path: Path) -> tuple[dict, dict]:
    with content_path.open() as f:
        content = json.load(f)
    with brand_config_path.open() as f:
        brand_config = yaml.safe_load(f)
    return content, brand_config


def render_html(
    template_name: str,
    content: dict,
    brand_config: dict,
    palette_name: str,
    skill_root: Path,
) -> str:
    template_dir = skill_root / "templates"
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(["html"]),
    )
    template = env.get_template(f"{template_name}.html")

    palette = brand_config["palettes"][palette_name]
    typography = brand_config["typography"]
    canvas = brand_config["canvas"]
    brand = brand_config["brand"]

    # Resolve headshot as a base64 data URI so it works with page.set_content()
    headshot_rel = brand_config["assets"].get("headshot")
    headshot_abs = skill_root / headshot_rel if headshot_rel else None
    headshot_path = None
    if headshot_abs and headshot_abs.exists():
        suffix = headshot_abs.suffix.lower().lstrip(".")
        mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}.get(suffix, "image/png")
        b64 = base64.b64encode(headshot_abs.read_bytes()).decode("ascii")
        headshot_path = f"data:{mime};base64,{b64}"

    # Derive initials from owner_name for placeholder fallback.
    owner_name = brand.get("owner_name", "")
    parts = [p for p in owner_name.split() if p]
    brand = {**brand, "initials": ("".join(p[0] for p in parts[:2]).upper() or "??")}

    return template.render(
        cover=content.get("cover", {}),
        slides=content.get("slides", []),
        takeaway=content.get("takeaway", {}),
        cta=content.get("cta", {}),
        palette=palette,
        typography=typography,
        canvas=canvas,
        brand=brand,
        headshot_path=headshot_path,
    )


async def html_to_pdf(html: str, output_path: Path) -> None:
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={"width": 1080, "height": 1350})
        page = await context.new_page()
        await page.set_content(html, wait_until="networkidle")

        # Ensure web fonts are loaded before export.
        await page.evaluate("document.fonts.ready")

        await page.pdf(
            path=str(output_path),
            width="1080px",
            height="1350px",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            prefer_css_page_size=True,
        )
        await browser.close()


# ------------ CLI ----------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="CAIO LinkedIn Carousel Renderer")
    parser.add_argument("--content", required=True, type=Path, help="Path to content JSON")
    parser.add_argument(
        "--brand-config",
        required=True,
        type=Path,
        help="Path to brand-config.yaml",
    )
    parser.add_argument(
        "--template",
        choices=TEMPLATE_NAMES,
        default=None,
        help="Template name (overrides content JSON)",
    )
    parser.add_argument(
        "--palette",
        choices=PALETTES,
        default=None,
        help="Palette variant (overrides content JSON)",
    )
    parser.add_argument("--output", required=True, type=Path, help="Output PDF path")
    parser.add_argument(
        "--debug-html",
        type=Path,
        default=None,
        help="Optional path to also write the rendered HTML for inspection",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    skill_root = Path(__file__).resolve().parent.parent
    content, brand_config = load_inputs(args.content, args.brand_config)

    template_name = args.template or content.get("template", "executive-minimal")
    palette_name = args.palette or content.get("palette", "brand")

    if template_name not in TEMPLATE_NAMES:
        print(f"ERROR: Unknown template {template_name!r}", file=sys.stderr)
        return 2
    if palette_name not in PALETTES:
        print(f"ERROR: Unknown palette {palette_name!r}", file=sys.stderr)
        return 2

    copy_rules = brand_config.get("copy_rules", {})
    content, warnings = scrub_content(content, copy_rules)
    if warnings:
        print("Copy hygiene notes:", file=sys.stderr)
        for w in warnings:
            print(f"  - {w}", file=sys.stderr)

    html = render_html(template_name, content, brand_config, palette_name, skill_root)

    if args.debug_html:
        args.debug_html.write_text(html, encoding="utf-8")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    asyncio.run(html_to_pdf(html, args.output))

    print(f"Rendered: {args.output}")
    print(f"Template: {template_name}   Palette: {palette_name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
