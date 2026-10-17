# tesla-referral

Multilingual landing page for the Tesla Refer & Earn program (CZ / SK / HU / EN / DE),
static HTML on GitHub Pages: https://adamcharvat.github.io/tesla-referral

## Setup your referral link

The referral link is defined once in `build/build_site.py` (`REF_LINK`).
After changing it, regenerate and push:

    python3 build/build_site.py

(Or simply find-and-replace `ts.la/REPLACE_ME` across the HTML files.)

## Structure

    index.html   – Czech (default, /)
    sk/index.html – Slovak (/sk/)
    en/index.html – English (/en/)
    de/index.html – German (/de/)
    hu/index.html – Hungarian (/hu/)
    assets/site.css
    sitemap.xml, robots.txt

Each language version has its own URL, canonical tag, hreflang cluster
and FAQPage JSON-LD schema for SEO.

## Updating the page

Conditions of the Tesla referral program change several times a year.
Keep the FAQ + "last updated" date current — freshness is a ranking factor.
