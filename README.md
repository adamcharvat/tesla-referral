# Referral landing page · 1 000 km na Superchargerech

Statická stránka pro doporučující odkaz `https://ts.la/adam506840` v pěti jazycích na https://free1000km.com: angličtina na rootu (`x-default`), ostatní jazyky v `/cs/`, `/sk/`, `/hu/`, `/de/`.
Obsahuje jen HTML, CSS a vanilla JS. Nemá build step, balíčky ani runtime závislosti, z externích zdrojů načítá jen Google Fonts.

```
python3 generate.py                                  # vygeneruje všech 5 jazyků
python3 generate.py --base-url https://free1000km.com/
python3 -m http.server 4173                          # lokální preview → http://localhost:4173/
```

Před nasazením nastav `base_url` v `src/site.json` (nebo `--base-url`). Používá se pro canonical, hreflang, og:image a sitemap.

## Struktura

| Cesta | Co to je |
|---|---|
| `src/template.html` | **jediná** HTML šablona; dokumentace placeholderů je v hlavičce souboru |
| `src/i18n/{cs,sk,hu,en,de}.json` | veškerý viditelný text; všechny soubory musí mít stejnou strukturu |
| `src/site.json` | sdílená konfigurace: odkaz, `reward_km`, datum aktualizace, jazyky, base URL |
| `generate.py` | generátor (jen standardní knihovna) a kontroly |
| `index.html` (EN, x-default), `cs/`, `sk/`, `hu/`, `de/` | **generovaný výstup, needitovat ručně** |
| `assets/site.css`, `assets/site.js` | společné styly a skripty |
| `assets/img/` | ořezy fotografií (WebP + JPEG), `og-image.jpg`, `CREDITS.md` |
| `tools/prepare_images.py` | volitelný jednorázový pipeline ořezů (Pillow + cwebp) |
| `sitemap.xml`, `robots.txt` | generuje `generate.py` |
| `CNAME`, `.nojekyll` | GitHub Pages: vlastní doména, vypnutý Jekyll |

## Placeholdery

| Zápis | Význam |
|---|---|
| `{{name}}` | text, HTML-escapovaný (klíč z překladu nebo kontext generátoru) |
| `{{{name}}}` | připravené HTML/JSON z generátoru (`h1_html`, `terms[].detail_html`, `faq_jsonld`, `current_attr`) |
| `{{#list}} … {{/list}}` | opakovaný blok (`steps`, `terms`, `faq_items`, `languages`, `alternates`, `og_alternates`) |
| `{reward}` | token **uvnitř překladů**, nahradí se hodnotou `reward` daného jazyka (`1 000 km`, `1.000 km`…) |
| `<!--# … -->` | komentář šablony, do výstupu se nedostane |

Generátor sestavení zastaví, když:
- překladům chybí nebo přebývá klíč,
- zůstane nevyřešený placeholder nebo token,
- je víc než jedno `<h1>`,
- JSON-LD neodpovídá FAQ,
- nějaký `ts.la` odkaz není přesně referral URL,
- `reward` neodpovídá `reward_km`,
- se ve výstupu objeví hodnota 500,
- chybí referencovaný asset.

Na `x-default` stránce generátor vloží data pro lištu „stránka je dostupná také v…“. `site.js` ji ukáže podle jazyka prohlížeče, nikdy automaticky nepřesměruje a volbu si pamatuje v `localStorage.lang-choice`.

Automaticky dělá i typografii: v CZ/SK vkládá nezlomitelnou mezeru za jednopísmenné předložky a spojky. Za spojovník uvnitř slova (`Supercharger-hálózaton`, `Tesla-Konto`) vkládá word joiner, takže se tam řádek nikdy nezlomí. Slova se nikdy nedělí (`hyphens: none`).

## Design

**Art direction „Horizon“:** dlouhé, klidné, horizontální kompozice. Každý blok začíná hairline linkou jako horizontem, fotografie jsou panoramatické a vzdálenost odměny je jediný měděný text na stránce. Stránka začíná ve dne (hero) a končí v noci (závěr a footer).

- **Typografie:** Archivo (display, variabilní šířka 100–125 %: na mobilu 100 %, na desktopu 108 %) a Source Sans 3 (text). Plynulá stupnice 360→1440 px: label 12, small 14, body 16→17, lead 17→20, h3 18→21, h2 26→40, h1 30→56.
- **Grid:** 12 sloupců, max. šířka obsahu 1320 px, okraj `clamp(16px, 4vw, 64px)`, gutter 16→24 px. Pojmenované linky `full-start / content-start / col N / content-end / full-end` umožňují fotkám přesahovat k okraji obrazovky. Vertikální rytmus je po 8 px.
- **Barvy:** teplý papír a grafitový inkoust, akcent jediná měď (`#9a4a22` světlý, `#d68c5f` tmavý). Měď je vyhrazená pro odměnu, focus a výběr. Tmavý režim není inverze: má grafit místo černé, světlejší měď, o 40 jednotek lehčí řez písma a ztlumené fotky. Blok `.is-night` přemapuje tokeny, takže tlačítka a pole uvnitř se přizpůsobí samy.

## CSS tokeny

| Skupina | Tokeny |
|---|---|
| Písmo | `--font-display`, `--font-text`, `--fs-label`, `--fs-small`, `--fs-body`, `--fs-lead`, `--fs-h3`, `--fs-h2`, `--fs-h1`, `--fs-numeral`, `--lh-display`, `--lh-heading`, `--lh-body`, `--tracking-display`, `--tracking-heading`, `--tracking-label`, `--wght-display`, `--wght-body` |
| Prostor | `--space-1` … `--space-9` (4–96 px), `--section-space` |
| Grid | `--max`, `--margin`, `--gutter`, `--layout-columns`, `--header-h` |
| Tvar a pohyb | `--radius`, `--ease-out`, `--dur-fast` (160 ms), `--dur-base` (300 ms, i přechod tématu), `--dur-slow` (700 ms, reveal) |
| Barvy | `--color-bg`, `--color-surface`, `--color-ink`, `--color-ink-2`, `--color-ink-3`, `--color-line`, `--color-line-strong`, `--color-accent`, `--color-cta`, `--color-cta-hover`, `--color-cta-active`, `--color-on-cta`, `--color-field`, `--color-field-border`, `--color-hover`, `--color-selection`, `--color-selection-ink`, `--color-photo`, `--photo-filter` |
| Noc | `--night-bg`, `--night-surface`, `--night-ink`, `--night-ink-2`, `--night-ink-3`, `--night-line`, `--night-line-strong`, `--night-accent` |

Témata: `html[data-theme="light"|"dark"]`. Volbu nastaví inline skript v `<head>` ještě před prvním vykreslením (uložená volba, jinak `prefers-color-scheme`) a ukládá se do `localStorage.theme`. Bez JS stránka přebírá systémové téma přes media query.

## Kontrast (WCAG AA)

Text: nejnižší poměr je 5,03 : 1 (`--color-ink-3` na papíře). Měď na papíře má 5,51 : 1, v tmavém režimu 6,94 : 1. Rámeček kopírovacího pole má ≥ 3,29 : 1 (požadavek 3 : 1 pro UI prvky).
