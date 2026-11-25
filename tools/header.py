"""Generate the profile header as two SVGs (light + dark).

Edit the CONFIG block, then run:  python tools/header.py
Output: assets/header-light.svg, assets/header-dark.svg
"""
import math
import random
from xml.sax.saxutils import escape
from pathlib import Path

CONFIG = {
    "name": "Magdi Waleed",
    "role": "AI / ML Engineer · Speech & Voice AI · Riyadh",
    # Words under the waveform, like an ASR alignment. Mix Arabic and English
    # on purpose: code-switching is the hard part of the job.
    "tokens": ["مرحبا", "I'd", "like", "to", "book", "موعد", "بكرة", "لو", "سمحت"],
    "seed": 7,
}

THEMES = {
    "light": {"bg": "#FFFFFF", "ink": "#0B1F1C", "muted": "#5B6B68",
              "rule": "#E3E8E7", "wave": "#C9D6D3", "accent": "#0E7A6B"},
    "dark":  {"bg": "#0D1117", "ink": "#E8EEED", "muted": "#8C9A98",
              "rule": "#21262D", "wave": "#2A3533", "accent": "#3CCFB5"},
}

W, H = 900, 240
SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def waveform(n_bars, x0, x1, n_segments, rng):
    """Bar heights shaped like speech: syllable bursts with short pauses."""
    seg_w = (x1 - x0) / n_segments
    bars = []
    step = (x1 - x0) / n_bars
    for i in range(n_bars):
        x = x0 + i * step
        seg = min(int((x - x0) / seg_w), n_segments - 1)
        local = ((x - x0) - seg * seg_w) / seg_w  # 0..1 inside the word
        envelope = math.sin(math.pi * local) ** 0.8
        h = 4 + envelope * (10 + rng.random() * 34)
        bars.append((x, h, seg))
    return bars, seg_w, step


def render(theme):
    cfg = {k: escape(v) if isinstance(v, str) else [escape(x) for x in v]
           for k, v in CONFIG.items() if k != "seed"}
    t = THEMES[theme]
    rng = random.Random(CONFIG["seed"])
    tokens = cfg["tokens"]
    x0, x1, mid = 40, 860, 150
    bars, seg_w, step = waveform(150, x0, x1, len(tokens), rng)
    active = {1, 2, 3, 4}  # highlighted span: the English run inside Arabic

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'viewBox="0 0 {W} {H}" role="img" aria-label="{cfg["name"]}">',
           f'<rect width="{W}" height="{H}" fill="{t["bg"]}"/>',
           f'<text x="{x0}" y="62" font-family="{SANS}" font-size="40" '
           f'font-weight="650" fill="{t["ink"]}" letter-spacing="-0.5">{cfg["name"]}</text>',
           f'<text x="{x0 + 2}" y="92" font-family="{MONO}" font-size="16" '
           f'fill="{t["muted"]}">{cfg["role"]}</text>']

    bw = step * 0.55
    for x, h, seg in bars:
        color = t["accent"] if seg in active else t["wave"]
        out.append(f'<rect x="{x:.1f}" y="{mid - h / 2:.1f}" width="{bw:.1f}" '
                   f'height="{h:.1f}" rx="{bw / 2:.1f}" fill="{color}"/>')

    out.append(f'<line x1="{x0}" y1="186" x2="{x1}" y2="186" stroke="{t["rule"]}"/>')
    for i, tok in enumerate(tokens):
        cx = x0 + seg_w * (i + 0.5)
        color = t["accent"] if i in active else t["muted"]
        out.append(f'<line x1="{x0 + seg_w * i:.1f}" y1="180" x2="{x0 + seg_w * i:.1f}" '
                   f'y2="192" stroke="{t["rule"]}"/>')
        out.append(f'<text x="{cx:.1f}" y="212" text-anchor="middle" font-family="{SANS}" '
                   f'font-size="17" fill="{color}">{tok}</text>')
    out.append(f'<line x1="{x1}" y1="180" x2="{x1}" y2="192" stroke="{t["rule"]}"/>')
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    assets = Path(__file__).resolve().parent.parent / "assets"
    assets.mkdir(exist_ok=True)
    for theme in THEMES:
        (assets / f"header-{theme}.svg").write_text(render(theme), encoding="utf-8")
        print(f"wrote assets/header-{theme}.svg")
