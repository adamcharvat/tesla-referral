#!/usr/bin/env python3
"""Build every language version of the referral page from one template.

    python3 generate.py                      # uses base_url from src/site.json
    python3 generate.py --base-url https://referral.example.org/

Inputs:   src/template.html, src/site.json, src/i18n/<lang>.json
Outputs:  index.html (default language), <lang>/index.html, sitemap.xml, robots.txt

Standard library only. The build fails loudly on missing translation keys,
unresolved placeholders, invalid JSON-LD, broken asset paths or a reward
value other than the configured one.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"

DOC_COMMENT_RE = re.compile(r"<!--#.*?-->[ \t]*\n?", re.S)
SECTION_RE = re.compile(r"{{#(\w+)}}(.*?){{/\1}}", re.S)
RAW_RE = re.compile(r"{{{(\w+)}}}")
VAR_RE = re.compile(r"{{(\w+)}}")
TOKEN_RE = re.compile(r"{(\w+)}")
# Czech and Slovak typography: no line break after a one-letter preposition or conjunction.
ONE_LETTER_RE = re.compile(r"(?<![\w\u00a0])([KkSsVvZzOoUuAaIi]) (?=\S)")
ONE_LETTER_LANGS = {"cs", "sk"}
# "Supercharger-hálózaton", "Tesla-Konto": a WORD JOINER after the hyphen stops the
# browser from breaking the line there. Applied to visible text, not to meta or JSON-LD.
INNER_HYPHEN_RE = re.compile(r"(?<=\w)-(?=\w)")
NO_JOIN_KEYS = {"title", "meta_description"}


class BuildError(Exception):
    pass


# --------------------------------------------------------------------------- template

def render(template: str, context: dict) -> str:
    """Mustache-lite: sections, raw and escaped variables. Unknown names fail."""

    def lookup(name: str):
        if name not in context:
            raise BuildError(f"unknown placeholder '{name}'")
        return context[name]

    def section(match: re.Match) -> str:
        value = lookup(match.group(1))
        inner = match.group(2)
        if isinstance(value, list):
            return "".join(render(inner, {**context, **item}) for item in value)
        return render(inner, context) if value else ""

    out = SECTION_RE.sub(section, template)
    out = RAW_RE.sub(lambda m: str(lookup(m.group(1))), out)
    return VAR_RE.sub(lambda m: html.escape(str(lookup(m.group(1))), quote=True), out)


# --------------------------------------------------------------------------- translations

def shape(value):
    """Structural fingerprint used to compare translation files."""
    if isinstance(value, dict):
        return {key: shape(item) for key, item in value.items()}
    if isinstance(value, list):
        return [shape(item) for item in value]
    return "str"


def resolve_tokens(value, tokens: dict, lang: str):
    if isinstance(value, dict):
        return {key: resolve_tokens(item, tokens, lang) for key, item in value.items()}
    if isinstance(value, list):
        return [resolve_tokens(item, tokens, lang) for item in value]

    def replace(match: re.Match) -> str:
        if match.group(1) not in tokens:
            raise BuildError(f"[{lang}] unknown token '{{{match.group(1)}}}' in: {value}")
        return tokens[match.group(1)]

    text = TOKEN_RE.sub(replace, value)
    if lang in ONE_LETTER_LANGS:
        text = ONE_LETTER_RE.sub("\\1\u00a0", text)
    return text


def join_hyphens(value):
    if isinstance(value, dict):
        return {key: item if key in NO_JOIN_KEYS else join_hyphens(item) for key, item in value.items()}
    if isinstance(value, list):
        return [join_hyphens(item) for item in value]
    return INNER_HYPHEN_RE.sub("-\u2060", value)


def wrap_reward(text: str, reward: str) -> str:
    escaped = html.escape(text, quote=False)
    return escaped.replace(reward, f'<span class="figure">{reward}</span>')


# --------------------------------------------------------------------------- build

def relative_href(from_path: str, to_path: str) -> str:
    depth = from_path.count("/")
    return ("../" * depth + to_path) or "./"


def build_context(site: dict, lang_cfg: dict, strings: dict, base_url: str) -> dict:
    code = lang_cfg["code"]
    path = lang_cfg["path"]
    reward = strings["reward"]
    languages = site["languages"]
    by_code = {item["code"]: item for item in languages}

    alternates = [{"hreflang": item["code"], "url": base_url + item["path"]} for item in languages]
    alternates.append({"hreflang": "x-default", "url": base_url + by_code[site["x_default_language"]]["path"]})

    faq_jsonld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "inLanguage": code,
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["question"],
                "acceptedAnswer": {"@type": "Answer", "text": item["answer"]},
            }
            for item in strings["faq_items"]
        ],
    }

    visible = join_hyphens(strings)
    context = dict(visible)
    context.update(
        lang=code,
        og_locale=lang_cfg["locale"],
        og_alternates=[{"locale": item["locale"]} for item in languages if item["code"] != code],
        asset_base="../" * path.count("/"),
        canonical_url=base_url + path,
        og_image_url=base_url + "assets/img/og-image.jpg",
        referral_url=site["referral_url"],
        referral_display=site["referral_display"],
        updated_iso=site["updated"],
        theme_color_light=site["theme_color"]["light"],
        theme_color_dark=site["theme_color"]["dark"],
        photo_credits=site["photo_credits"],
        alternates=alternates,
        languages=[
            {
                "code": item["code"],
                "label": item["label"],
                "href": relative_href(path, item["path"]),
                "current_attr": ' aria-current="page"' if item["code"] == code else "",
            }
            for item in languages
        ],
        h1_html=wrap_reward(visible["h1"], reward),
        steps=[dict(step, number=f"{index:02d}") for index, step in enumerate(visible["steps"], 1)],
        terms=[dict(term, detail_html=wrap_reward(term["detail"], reward)) for term in visible["terms"]],
        faq_jsonld=json.dumps(faq_jsonld, ensure_ascii=False, indent=2).replace("</", "<\\/"),
    )
    return context


def verify(page: str, lang: str, site: dict, strings: dict, out_dir: Path, asset_base: str) -> None:
    def fail(message: str) -> None:
        raise BuildError(f"[{lang}] {message}")

    if "{{" in page or "}}" in page:
        fail("unresolved template placeholder")
    if re.search(r"{[a-z_]+}", page):
        fail("unresolved translation token")
    if page.count("<h1") != 1:
        fail("expected exactly one <h1>")

    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', page, re.S)
    if len(blocks) != 1:
        fail("expected one JSON-LD block")
    data = json.loads(blocks[0])
    if data.get("@type") != "FAQPage" or len(data["mainEntity"]) != len(strings["faq_items"]):
        fail("FAQPage JSON-LD does not mirror the FAQ")

    for href in re.findall(r'href="(https?://ts\.la[^"]*)"', page):
        if href != site["referral_url"]:
            fail(f"unexpected referral link {href}")
    if page.count(f'href="{site["referral_url"]}"') < 3:
        fail("referral link missing from a call to action")

    if re.sub(r"\D", "", strings["reward"]) != str(site["reward_km"]):
        fail(f"reward '{strings['reward']}' differs from reward_km {site['reward_km']}")
    if re.search(r"\b500\b", page):
        fail("forbidden value 500 found")

    for ref in set(re.findall(r'(?:src|href|srcset|imagesrcset)="([^"]+)"', page)):
        for candidate in ref.split(","):
            url = candidate.strip().split(" ")[0]
            if url.startswith(asset_base + "assets/"):
                target = (out_dir / url).resolve()
                if not target.is_file():
                    fail(f"missing asset {url}")


def write_sitemap(site: dict, base_url: str) -> None:
    rows = []
    for item in site["languages"]:
        links = "".join(
            f'\n    <xhtml:link rel="alternate" hreflang="{alt["code"]}" href="{base_url}{alt["path"]}"/>'
            for alt in site["languages"]
        )
        rows.append(
            f"  <url>\n    <loc>{base_url}{item['path']}</loc>\n    <lastmod>{site['updated']}</lastmod>{links}\n  </url>"
        )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(rows)
        + "\n</urlset>\n",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {base_url}sitemap.xml\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--base-url", help="absolute site URL with trailing slash (overrides src/site.json)")
    args = parser.parse_args()

    site = json.loads((SRC / "site.json").read_text(encoding="utf-8"))
    base_url = (args.base_url or site["base_url"]).rstrip("/") + "/"
    template = DOC_COMMENT_RE.sub("", (SRC / "template.html").read_text(encoding="utf-8"))

    raw = {item["code"]: json.loads((SRC / "i18n" / f"{item['code']}.json").read_text(encoding="utf-8")) for item in site["languages"]}
    reference = shape(raw[site["default_language"]])
    for code, strings in raw.items():
        if shape(strings) != reference:
            missing = set(raw[site["default_language"]]) ^ set(strings)
            raise BuildError(f"[{code}] translation structure differs from {site['default_language']}.json {sorted(missing) or ''}")

    for lang_cfg in site["languages"]:
        code = lang_cfg["code"]
        strings = raw[code]
        tokens = {"reward": strings["reward"], "referral_display": site["referral_display"]}
        strings = resolve_tokens({k: v for k, v in strings.items() if k != "reward"}, tokens, code)
        strings["reward"] = tokens["reward"]

        context = build_context(site, lang_cfg, strings, base_url)
        page = render(template, context)
        out_dir = ROOT / lang_cfg["path"]
        verify(page, code, site, strings, out_dir, context["asset_base"])
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(page, encoding="utf-8")
        print(f"  {code}  /{lang_cfg['path']:<4} {len(page):>7,} bytes")

    write_sitemap(site, base_url)
    print(f"  sitemap.xml, robots.txt  ({base_url})")
    if "example." in base_url:
        print("  note: base_url is still a placeholder; set it in src/site.json or pass --base-url")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BuildError as error:
        print(f"build failed: {error}", file=sys.stderr)
        sys.exit(1)
