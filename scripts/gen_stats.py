#!/usr/bin/env python3
"""Build profile stat cards that include private contributions.

Hosted widgets (github-readme-stats and similar) only see public repositories,
so most of this account's work is invisible to them. This script reads the
contribution calendar with the owner's own token, which reports private
contribution counts (never repository names), and writes light and dark SVGs.

Usage: GH_TOKEN=<token with repo + read:org> python3 scripts/gen_stats.py
Optional: --languages data.json   (static language mix, written once by hand)
"""

import argparse
import datetime as dt
import json
import os
import subprocess

USER = "heman4t"
OUT = os.path.join(os.path.dirname(__file__), "..", "assets")

THEMES = {
    "light": {"bg": "#ffffff", "border": "#d0d7de", "title": "#1f2328", "text": "#59636e", "num": "#0969da", "bar": "#0969da", "bar2": "#54aeff", "track": "#eff2f5"},
    "dark": {"bg": "#0d1117", "border": "#30363d", "title": "#e6edf3", "text": "#9198a1", "num": "#58a6ff", "bar": "#2f81f7", "bar2": "#1f6feb", "track": "#161b22"},
}
LANG_COLORS = {
    "Python": "#3572A5", "TypeScript": "#3178c6", "Dart": "#00B4AB", "PHP": "#4F5D95", "JavaScript": "#f1e05a",
    "Jinja": "#a52a22", "Shell": "#89e051", "HTML": "#e34c26", "Kotlin": "#A97BFF", "C#": "#178600", "C++": "#f34b7d",
    "CSS": "#663399", "SCSS": "#c6538c", "Java": "#b07219", "PLpgSQL": "#336790", "Makefile": "#427819", "Other": "#8b949e",
}


def graphql(query: str) -> dict:
    out = subprocess.run(["gh", "api", "graphql", "-f", f"query={query}"], check=True, capture_output=True, text=True).stdout
    return json.loads(out)["data"]


def yearly_totals(first_year: int, last_year: int) -> dict[int, dict]:
    years = {}
    for y in range(first_year, last_year + 1):
        q = (
            f'query{{user(login:"{USER}"){{contributionsCollection(from:"{y}-01-01T00:00:00Z",to:"{y}-12-31T23:59:59Z")'
            "{contributionCalendar{totalContributions} restrictedContributionsCount}}}"
        )
        c = graphql(q)["user"]["contributionsCollection"]
        years[y] = {"total": c["contributionCalendar"]["totalContributions"], "private": c["restrictedContributionsCount"]}
    return years


def fmt(n: int) -> str:
    return f"{n:,}"


def contributions_svg(years: dict[int, dict], t: dict, today: dt.date) -> str:
    total = sum(v["total"] for v in years.values())
    private = sum(v["private"] for v in years.values())
    this_year = years[today.year]["total"]
    shown = [y for y in years if y >= 2015]
    peak = max(years[y]["total"] for y in shown) or 1
    w, h = 495, 195
    chart_x, chart_y, chart_w, chart_h = 250, 52, 225, 110
    bw = chart_w / len(shown)
    bars = []
    for i, y in enumerate(shown):
        v = years[y]["total"]
        bh = max(2, chart_h * v / peak) if v else 0
        x = chart_x + i * bw + 2
        bars.append(f'<rect x="{x:.1f}" y="{chart_y + chart_h - bh:.1f}" width="{bw - 4:.1f}" height="{bh:.1f}" rx="2" fill="{t["bar"] if y == today.year else t["bar2"]}"><title>{y}: {fmt(v)}</title></rect>')
        if y % 2 == 0 or y == today.year:
            bars.append(f'<text x="{x + (bw - 4) / 2:.1f}" y="{chart_y + chart_h + 14}" text-anchor="middle" class="s">{str(y)[2:]}’</text>')
    pct = round(100 * private / total) if total else 0
    stats = [
        (fmt(total), "contributions since 2011"),
        (f"{pct}%", "in private client and product repos"),
        (fmt(this_year), f"contributions in {today.year} so far"),
    ]
    rows = "".join(
        f'<text x="25" y="{70 + i * 40}" class="n">{n}</text><text x="25" y="{86 + i * 40}" class="s">{label}</text>'
        for i, (n, label) in enumerate(stats)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{fmt(total)} GitHub contributions since 2011, {pct}% private">
<style>.t{{font:600 15px 'Segoe UI',Ubuntu,Helvetica,Arial,sans-serif;fill:{t["title"]}}}.n{{font:700 20px 'Segoe UI',Ubuntu,Helvetica,Arial,sans-serif;fill:{t["num"]}}}.s{{font:400 11px 'Segoe UI',Ubuntu,Helvetica,Arial,sans-serif;fill:{t["text"]}}}</style>
<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="6" fill="{t["bg"]}" stroke="{t["border"]}"/>
<text x="25" y="32" class="t">Contributions, all repositories</text>
<text x="{chart_x}" y="32" class="s">per year, 2015–{today.year}</text>
{rows}
{"".join(bars)}
</svg>'''


def languages_svg(langs: dict[str, float], t: dict, note: str) -> str:
    top = sorted(langs.items(), key=lambda kv: -kv[1])
    head, rest = top[:8], sum(v for _, v in top[8:])
    if rest:
        head.append(("Other", rest))
    total = sum(v for _, v in head) or 1
    w, h = 300, 195
    x, bar_w = 25, 250
    segs, cx = [], x
    for name, v in head:
        sw = bar_w * v / total
        segs.append(f'<rect x="{cx:.2f}" y="48" width="{max(sw, 0.5):.2f}" height="8" fill="{LANG_COLORS.get(name, "#8b949e")}"/>')
        cx += sw
    items = []
    for i, (name, v) in enumerate(head):
        col, row = i % 2, i // 2
        ix, iy = x + col * 130, 82 + row * 22
        items.append(
            f'<circle cx="{ix + 5}" cy="{iy - 4}" r="5" fill="{LANG_COLORS.get(name, "#8b949e")}"/>'
            f'<text x="{ix + 16}" y="{iy}" class="l">{name}</text><text x="{ix + 115}" y="{iy}" text-anchor="end" class="s">{100 * v / total:.0f}%</text>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Languages weighted by commits">
<style>.t{{font:600 15px 'Segoe UI',Ubuntu,Helvetica,Arial,sans-serif;fill:{t["title"]}}}.l{{font:400 12px 'Segoe UI',Ubuntu,Helvetica,Arial,sans-serif;fill:{t["title"]}}}.s{{font:400 11px 'Segoe UI',Ubuntu,Helvetica,Arial,sans-serif;fill:{t["text"]}}}</style>
<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="6" fill="{t["bg"]}" stroke="{t["border"]}"/>
<text x="25" y="32" class="t">Languages I commit in</text>
<clipPath id="c"><rect x="{x}" y="48" width="{bar_w}" height="8" rx="4"/></clipPath><g clip-path="url(#c)">{"".join(segs)}</g>
{"".join(items)}
<text x="25" y="{h - 14}" class="s">{note}</text>
</svg>'''


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--languages", help="JSON object {language: weight}")
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    today = dt.date.today()
    years = yearly_totals(2011, today.year)
    for name, t in THEMES.items():
        with open(os.path.join(OUT, f"contributions-{name}.svg"), "w") as f:
            f.write(contributions_svg(years, t, today))
    if args.languages:
        langs = json.load(open(args.languages))
        for name, t in THEMES.items():
            with open(os.path.join(OUT, f"languages-{name}.svg"), "w") as f:
                f.write(languages_svg(langs, t, "Weighted by my commits, all repositories"))
    print(json.dumps({"total": sum(v["total"] for v in years.values()), "years": years}))


if __name__ == "__main__":
    main()
