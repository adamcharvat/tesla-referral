# tesla-referral

Multilingual landing page for the Tesla Refer & Earn program (CZ / SK / HU / EN / DE),
static HTML on GitHub Pages: https://adamcharvat.github.io/tesla-referral

## Setup your referral link

The referral link is defined once in `build/build_site.py`:

    REF_LINK = "https://ts.la/REPLACE_ME"   # full URL the buttons point to
    REF_CODE = "ts.la/REPLACE_ME"           # short form shown in the copy field

After changing them, regenerate and push:

    python3 build/build_site.py

## Structure

    index.html    – Czech (default, /)
    sk/index.html – Slovak (/sk/)
    en/index.html – English (/en/)
    de/index.html – German (/de/)
    hu/index.html – Hungarian (/hu/)
    assets/site.css, assets/site.js, assets/img/
    sitemap.xml, robots.txt

Every language has its own URL, canonical tag, hreflang cluster and
FAQPage JSON-LD schema. Light/dark theme follows the visitor's system
preference and can be toggled in the navbar (choice is remembered).

## Updating the page

Conditions of the Tesla referral program change several times a year.
Keep the FAQ and the "last updated" date current — freshness is a
ranking factor, and outdated numbers erode trust (and conversions).
