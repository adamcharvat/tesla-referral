#!/usr/bin/env python3
"""Generator for the tesla-referral landing page (CZ/SK/HU/EN/DE).

Edit REF_LINK below, then run:  python3 build/build_site.py
Outputs the static site into the repository root.
"""
import pathlib

REF_LINK = "https://ts.la/REPLACE_ME"  # <- put your real referral link here
BASE = "https://adamcharvat.github.io/tesla-referral"
UPDATED = "October 2026"

ROOT = pathlib.Path(__file__).resolve().parent.parent

LANGS = {
    "cs": {"dir": "",        "slug": "cs"},
    "sk": {"dir": "sk/",     "slug": "sk"},
    "en": {"dir": "en/",     "slug": "en"},
    "de": {"dir": "de/",     "slug": "de"},
    "hu": {"dir": "hu/",     "slug": "hu"},
}

LANG_NAMES = {"cs": "Čeština", "sk": "Slovenčina", "en": "English", "de": "Deutsch", "hu": "Magyar"}

T = {
"cs": {
 "html_lang": "cs",
 "title": "Tesla referral kód 2026 — 1 000 km Supercharging zdarma k nové Tesle",
 "description": "Objednej si novou Teslu (Model 3 / Model Y) přes tento referral odkaz a získej 1 000 km volného dobíjení na Superchargerech zdarma. Cena auta se nemění — využij oficiální Tesla Refer & Earn program.",
 "eyebrow": "Tesla referral program · 2026",
 "h1": "1 000 km Supercharging zdarma k&nbsp;nové Tesle",
 "sub": "Objednej si nový Model 3 nebo Model Y přes tento referral odkaz a Tesla ti po převzetí vozu připíše 1 000 km volného dobíjení. Nic tě to nestojí — cena auta je stejná, jako kdybys objednával bez odkazu.",
 "cta": "Získat 1 000 km zdarma",
 "cta_note": "Přesměrování na oficiální stránku Tesla · bez kódu, stačí kliknout",
 "anchor_how": "Jak to funguje",
 "anchor_faq": "Časté otázky",
 "stats": [("1 000 km", "volného Supercharging k novému vozu"), ("0 Kč navíc", "cena Tesly se odkazem nemění"), ("~500 €", "kredit pro doporučujícího majitele")],
 "how_label": "01 / Jak to funguje",
 "how_title": "Tři kroky a je to",
 "how_sub": "Celé to trvá asi tak dlouho jako kliknout na odkaz. Pozor jen na jedno — referral musíš použít předtím, než objednávku dokončíš.",
 "steps": [
   ("Klikni na referral odkaz", "Odkaz tě přenese na oficiální české stránky Tesla s předvyplněným referral kódem. Nic zapisovat nemusíš."),
   ("Nakonfiguruj si Teslu", "Vyber model, barvu a výbavu jako obvykle a objednávku dokonči. V souhrnu objednávky uvidíš potvrzení referralu."),
   ("Dobíjej zdarma", "Po převzetí vozu ti Tesla připíše 1 000 km volného Supercharging do aplikace. Kredit můžeš čerpat po celé Evropě."),
 ],
 "models_label": "02 / Co platí",
 "models_title": "Komu a na co se referral vztahuje",
 "models": [
   ("Model 3", "Nové objednávky Modelu 3 — 1 000 km volného Supercharging."),
   ("Model Y", "Nové objednávky Modelu Y — 1 000 km volného Supercharging."),
   ("Region ČR", "Odměna se řídí regionem objednávky a platnými podmínkami pro ČR."),
 ],
 "models_note": "Podmínky programu Tesla průběžně upravuje — přesnou aktuální odměnu vždy uvidíš v souhrnu objednávky na tesla.com ještě před zaplacením zálohy.",
 "faq_label": "03 / Časté otázky",
 "faq_title": "Než klikneš",
 "faq": [
   ("Co přesně získám přes referral odkaz?", "Při objednávce nového Modelu 3 nebo Modelu Y přes tento odkaz získáš 1 000 km volného dobíjení na Superchargerech. Přesný rozsah odměny se řídí aktuálními podmínkami Tesla pro tvůj region."),
   ("Změní se mi cena auta?", "Ne. Tesla prodává za pevné ceny přímo, bez dealerů — referral odkaz cenu vozu nijak neovlivní. Odměna je bonus navíc od Tesly."),
   ("Kdy musím odkaz použít?", "Před dokončením objednávky. Referral nelze přidat zpětně, už po odeslané objednávce. Proto klikni na odkaz ještě předtím, než začneš konfigurovat."),
   ("Na kterých Superchargerech kredit platí?", "Na všech Superchargerech Tesly v ČR i v zahraničí. Kilometry se počítají dle spotřeby tvého vozu."),
   ("Kdy se mi kredit připíše?", "Po převzetí (doručení) vozu. Do té doby bývá vidět ve stavu „pending“ ve tvém Tesla účtu a po převzetí se aktivuje v aplikaci."),
   ("Kolik referralů může majitel ročně získat?", "Tesla omezuje odměny za referral na 10 úspěšných doporučení za kalendářní rok na účet."),
 ],
 "final_title": "Jdeš do toho?",
 "final_sub": "Jeden klik před objednávkou = 1 000 km dobíjení zdarma. Auta si Tesla říká o stejné peníze, s odkazem nebo bez.",
 "final_cta": "Objednat s 1 000 km zdarma",
 "foot_updated": "Aktualizováno",
 "foot_note": "Neoficiální stránka majitele vozu Tesla. Není spojena se společností Tesla, Inc. Tesla a logo Tesla jsou ochranné známky Tesla, Inc.",
 "foot_lang": "Jazyk",
 "alt_check": "Ověř si aktuální podmínky programu",
},
"sk": {
 "html_lang": "sk",
 "title": "Tesla referral kód 2026 — 1 000 km Supercharging zdarma k novej Tesle",
 "description": "Objednaj si novú Teslu (Model 3 / Model Y) cez tento referral odkaz a získaj 1 000 km voľného nabíjania na Superchargeroch zadarmo. Cena auta sa nemení — využi oficiálny Tesla Refer & Earn program.",
 "eyebrow": "Tesla referral program · 2026",
 "h1": "1 000 km Supercharging zadarmo k&nbsp;novej Tesle",
 "sub": "Objednaj si nový Model 3 alebo Model Y cez tento referral odkaz a Tesla ti po prevzatí auta pripíše 1 000 km voľného nabíjania. Nestojí ťa to nič — cena auta je rovnaká ako bez odkazu.",
 "cta": "Získať 1 000 km zadarmo",
 "cta_note": "Presmerovanie na oficiálnu stránku Tesla · stačí kliknúť, bez kódu",
 "anchor_how": "Ako to funguje",
 "anchor_faq": "Časté otázky",
 "stats": [("1 000 km", "voľného Supercharging k novému autu"), ("0 € navyše", "cena Tesly sa odkazom nemení"), ("~500 €", "kredit pre odporúčajúceho majiteľa")],
 "how_label": "01 / Ako to funguje",
 "how_title": "Tri kroky a je to",
 "how_sub": "Celé to trvá približne tak dlho, ako kliknúť na odkaz. Jediné, na čo si daj pozor — referral treba použiť pred dokončením objednávky.",
 "steps": [
   ("Klikni na referral odkaz", "Odkaz ťa presmeruje na oficiálne slovenské stránky Tesla s predvyplneným referral kódom. Nič vypisovať nemusíš."),
   ("Nakonfiguruj si Teslu", "Vyber model, farbu a výbavu ako obvykle a dokonči objednávku. V súhrne uvidíš potvrdenie referralu."),
   ("Nabíjaj zadarmo", "Po prevzatí auta ti Tesla pripíše 1 000 km voľného Supercharging do aplikácie. Kredit môžeš čerpať po celej Európe."),
 ],
 "models_label": "02 / Čo platí",
 "models_title": "Komu a na čo sa referral vzťahuje",
 "models": [
   ("Model 3", "Nové objednávky Modelu 3 — 1 000 km voľného Supercharging."),
   ("Model Y", "Nové objednávky Modelu Y — 1 000 km voľného Supercharging."),
   ("Región SR", "Odmena sa riadi regiónom objednávky a platnými podmienkami pre SR."),
 ],
 "models_note": "Tesla podmienky programu priebežne upravuje — presnú aktuálnu odmenu vždy uvidíš v súhrne objednávky na tesla.com ešte pred zaplatením zálohy.",
 "faq_label": "03 / Časté otázky",
 "faq_title": "Predtým, ako klikneš",
 "faq": [
   ("Čo presne získam cez referral odkaz?", "Pri objednávke nového Modelu 3 alebo Modelu Y cez tento odkaz získaš 1 000 km voľného nabíjania na Superchargeroch. Presný rozsah odmeny sa riadi aktuálnymi podmienkami Tesla pre tvoj región."),
   ("Zmení sa mi cena auta?", "Nie. Tesla predáva za pevné ceny priamo, bez dealerov — referral odkaz cenu auta nijako neovplyvní. Odmena je bonus navyše od Tesly."),
   ("Kedy musím použiť odkaz?", "Pred dokončením objednávky. Referral nie je možné pridať spätne, už po odoslanej objednávke. Preto klikni na odkaz ešte predtým, ako začneš konfigurovať."),
   ("Na ktorých Superchargeroch kredit platí?", "Na všetkých Superchargeroch Tesly na Slovensku aj v zahraničí. Kilometre sa počítajú podľa spotreby tvojho auta."),
   ("Kedy sa mi kredit pripíše?", "Po prevzatí auta. Dovtedy býva vo stave „pending“ v tvojom Tesla účte a po prevzatí sa aktivuje v aplikácii."),
   ("Koľko referralov môže majiteľ ročne získať?", "Tesla odmeny za referral obmedzuje na 10 úspešných odporúčaní za kalendárny rok na účet."),
 ],
 "final_title": "Ideš do toho?",
 "final_sub": "Jeden klik pred objednávkou = 1 000 km nabíjania zadarmo. Tesla si pýta rovnaké peniaze s odkazom aj bez neho.",
 "final_cta": "Objednať s 1 000 km zadarmo",
 "foot_updated": "Aktualizované",
 "foot_note": "Neoficiálna stránka majiteľa auta Tesla. Nie je spojená so spoločnosťou Tesla, Inc. Tesla a logo Tesla sú ochranné známky Tesla, Inc.",
 "foot_lang": "Jazyk",
 "alt_check": "Over si aktuálne podmienky programu",
},
"en": {
 "html_lang": "en",
 "title": "Tesla Referral Code 2026 — 1,000 km Free Supercharging on a New Tesla",
 "description": "Order a new Tesla (Model 3 / Model Y) through this referral link and get 1,000 km of free Supercharging. The car price never changes — use Tesla's official Refer & Earn program.",
 "eyebrow": "Tesla referral program · 2026",
 "h1": "1,000 km of free Supercharging with&nbsp;your new Tesla",
 "sub": "Order a new Model 3 or Model Y through this referral link and Tesla will credit 1,000 km of free charging when you take delivery. It costs you nothing — the car's price is exactly the same as ordering without a link.",
 "cta": "Get 1,000 km free",
 "cta_note": "Takes you to the official Tesla site · one click, no code to type",
 "anchor_how": "How it works",
 "anchor_faq": "FAQ",
 "stats": [("1,000 km", "of free Supercharging with a new car"), ("€0 extra", "the Tesla price never changes"), ("~€500", "credit for the referring owner")],
 "how_label": "01 / How it works",
 "how_title": "Three steps, that's it",
 "how_sub": "It takes about as long as clicking a link. One thing to remember: the referral must be used before you complete your order.",
 "steps": [
   ("Click the referral link", "You're taken to the official Tesla site with the referral code already attached. Nothing to type in."),
   ("Configure your Tesla", "Pick your model, colour and options as usual and place the order. You'll see the referral confirmed in the order summary."),
   ("Charge for free", "After delivery, Tesla credits 1,000 km of free Supercharging to your app. Use it across Europe."),
 ],
 "models_label": "02 / What applies",
 "models_title": "Who and what the referral covers",
 "models": [
   ("Model 3", "New Model 3 orders — 1,000 km of free Supercharging."),
   ("Model Y", "New Model Y orders — 1,000 km of free Supercharging."),
   ("Your region", "The reward follows the region of your order and Tesla's current local terms."),
 ],
 "models_note": "Tesla adjusts the program terms from time to time — the exact current reward is always shown in your order summary on tesla.com before you pay the deposit.",
 "faq_label": "03 / FAQ",
 "faq_title": "Before you click",
 "faq": [
   ("What exactly do I get through the referral link?", "When you order a new Model 3 or Model Y through this link, you get 1,000 km of free Supercharging. The exact reward follows Tesla's current terms for your region."),
   ("Does the car price change?", "No. Tesla sells at fixed prices, directly, with no dealers — the referral link never changes what you pay. The reward is a bonus on top."),
   ("When do I need to use the link?", "Before you complete your order. A referral cannot be added retroactively after an order is placed — so click the link before you start configuring."),
   ("Which Superchargers does the credit work at?", "At all Tesla Superchargers at home and abroad. Kilometres are deducted based on your car's consumption."),
   ("When is the credit applied?", "After you take delivery of the car. Until then it usually shows as “pending” in your Tesla account and activates in the app after delivery."),
   ("How many referrals can an owner earn per year?", "Tesla caps referral rewards at 10 successful referrals per calendar year per account."),
 ],
 "final_title": "Ready to order?",
 "final_sub": "One click before ordering = 1,000 km of free charging. Tesla charges you the same price either way.",
 "final_cta": "Order with 1,000 km free",
 "foot_updated": "Last updated",
 "foot_note": "Unofficial page run by a Tesla owner. Not affiliated with Tesla, Inc. Tesla and the Tesla logo are trademarks of Tesla, Inc.",
 "foot_lang": "Language",
 "alt_check": "Check the current program terms",
},
"de": {
 "html_lang": "de",
 "title": "Tesla Empfehlungscode 2026 — 1.000 km Gratis-Supercharging zum neuen Tesla",
 "description": "Bestelle einen neuen Tesla (Model 3 / Model Y) über diesen Empfehlungslink und erhalte 1.000 km kostenloses Supercharging. Der Preis ändert sich nicht — nutze Teslas offizielles Empfehlungsprogramm.",
 "eyebrow": "Tesla-Empfehlungsprogramm · 2026",
 "h1": "1.000 km Gratis-Supercharging zum&nbsp;neuen Tesla",
 "sub": "Bestelle einen neuen Model 3 oder Model Y über diesen Empfehlungslink und Tesla schreibt dir nach Übergabe 1.000 km kostenloses Laden gut. Es kostet dich nichts — der Preis ist derselbe wie ohne Link.",
 "cta": "1.000 km gratis sichern",
 "cta_note": "Weiterleitung zur offiziellen Tesla-Seite · ein Klick, kein Code nötig",
 "anchor_how": "So funktioniert's",
 "anchor_faq": "Häufige Fragen",
 "stats": [("1.000 km", "Gratis-Supercharging zum Neuwagen"), ("0 € extra", "der Tesla-Preis bleibt gleich"), ("~500 €", "Guthaben für den Empfehlungsgeber")],
 "how_label": "01 / So funktioniert's",
 "how_title": "Drei Schritte, fertig",
 "how_sub": "Es dauert ungefähr so lange wie ein Klick. Einzige Regel: Die Empfehlung muss vor Abschluss der Bestellung verwendet werden.",
 "steps": [
   ("Empfehlungslink anklicken", "Der Link führt dich zur offiziellen Tesla-Seite, der Code ist bereits hinterlegt. Nichts eingeben, nichts kopieren."),
   ("Tesla konfigurieren", "Wähle Modell, Farbe und Ausstattung wie gewohnt und schließe die Bestellung ab. Die Empfehlung siehst du in der Bestellübersicht."),
   ("Kostenlos laden", "Nach Übergabe schreibt Tesla dir 1.000 km Gratis-Supercharging in die App gut — nutzbar an allen Superchargern in Europa."),
 ],
 "models_label": "02 / Was gilt",
 "models_title": "Für wen und für was gilt der Code",
 "models": [
   ("Model 3", "Neubestellungen des Model 3 — 1.000 km Gratis-Supercharging."),
   ("Model Y", "Neubestellungen des Model Y — 1.000 km Gratis-Supercharging."),
   ("Deine Region", "Die Prämie richtet sich nach der Region der Bestellung und den aktuellen Bedingungen von Tesla."),
 ],
 "models_note": "Tesla passt die Programmbedingungen regelmäßig an — die exakt aktuelle Prämie siehst du immer in der Bestellübersicht auf tesla.com, bevor du die Anzahlung zahlst.",
 "faq_label": "03 / Häufige Fragen",
 "faq_title": "Bevor du klickst",
 "faq": [
   ("Was genau bekomme ich über den Empfehlungslink?", "Bei Bestellung eines neuen Model 3 oder Model Y über diesen Link erhältst du 1.000 km kostenloses Supercharging. Die genaue Prämie richtet sich nach den aktuellen Bedingungen von Tesla für deine Region."),
   ("Ändert sich der Preis des Autos?", "Nein. Tesla verkauft zu Festpreisen, direkt, ohne Händler — der Empfehlungslink ändert nie den Preis. Die Prämie ist ein Bonus obendrauf."),
   ("Wann muss ich den Link nutzen?", "Vor Abschluss der Bestellung. Eine Empfehlung kann nicht nachträglich hinzugefügt werden — klicke den Link also, bevor du mit der Konfiguration beginnst."),
   ("An welchen Superchargern gilt das Guthaben?", "An allen Superchargern von Tesla — in Deutschland und im Ausland. Die Kilometer werden je nach Verbrauch deines Autos abgerechnet."),
   ("Wann wird das Guthaben gutgeschrieben?", "Nach Übergabe des Fahrzeugs. Bis dahin steht es meist als „pending“ in deinem Tesla-Konto und wird nach Lieferung in der App aktiviert."),
   ("Wie viele Empfehlungen kann ein Besitzer pro Jahr erhalten?", "Tesla begrenzt Prämien auf 10 erfolgreiche Empfehlungen pro Kalenderjahr und Konto."),
 ],
 "final_title": "Bereit?",
 "final_sub": "Ein Klick vor der Bestellung = 1.000 km gratis laden. Tesla verlangt in beiden Fällen denselben Preis.",
 "final_cta": "Mit 1.000 km gratis bestellen",
 "foot_updated": "Zuletzt aktualisiert",
 "foot_note": "Inoffizielle Seite eines Tesla-Besitzers. Nicht mit Tesla, Inc. verbunden. Tesla und das Tesla-Logo sind Marken der Tesla, Inc.",
 "foot_lang": "Sprache",
 "alt_check": "Aktuelle Programmbedingungen prüfen",
},
"hu": {
 "html_lang": "hu",
 "title": "Tesla referral kód 2026 — 1 000 km ingyenes Supercharging az új Tesládhoz",
 "description": "Rendelj új Teslát (Model 3 / Model Y) ezen a referral linken keresztül, és 1 000 km ingyenes Supercharging-ot kapsz. Az autó ára nem változik — használd a Tesla hivatalos ajánlóprogramját.",
 "eyebrow": "Tesla ajánlóprogram · 2026",
 "h1": "1 000 km ingyenes Supercharging az&nbsp;új Tesládhoz",
 "sub": "Rendelj új Model 3-at vagy Model Y-t ezen a referral linken keresztül, és az átvétel után a Tesla 1 000 km ingyenes töltést ír jóvá. Semmibe nem kerül — az autó ára ugyanannyi, mintha link nélkül rendelnéd.",
 "cta": "1 000 km ingyen",
 "cta_note": "A hivatalos Tesla oldalra visz · egy kattintás, kód nélkül",
 "anchor_how": "Így működik",
 "anchor_faq": "Gyakori kérdések",
 "stats": [("1 000 km", "ingyenes Supercharging az új autóhoz"), ("0 Ft többlet", "a Tesla ára nem változik"), ("~500 €", "kredit az ajánló tulajdonosnak")],
 "how_label": "01 / Így működik",
 "how_title": "Három lépés, ennyi",
 "how_sub": "Körülbelül annyi időbe telik, mint egy linkre kattintani. Egy dolgot ne felejts el: a referralt a rendelés véglegesítése előtt kell használni.",
 "steps": [
   ("Kattints a referral linkre", "A link a hivatalos Tesla oldalra visz, az ajánlókód már előre be van állítva. Semmit nem kell begépelned."),
   ("Konfiguráld a Teslát", "Válaszd ki a modellt, a színt és a felszereltséget a szokásos módon, majd fejezd be a rendelést. A rendelés összegzésében látod a referral visszaigazolását."),
   ("Tölts ingyen", "Átvétel után a Tesla 1 000 km ingyenes Supercharging-ot ír jóvá az alkalmazásodban. Európa-szerte használható."),
 ],
 "models_label": "02 / Mi érvényes",
 "models_title": "Kire és mire vonatkozik a referral",
 "models": [
   ("Model 3", "Új Model 3 rendelések — 1 000 km ingyenes Supercharging."),
   ("Model Y", "Új Model Y rendelések — 1 000 km ingyenes Supercharging."),
   ("Régiód", "A jutalom a rendelés régiójától és a Tesla aktuális helyi feltételeitől függ."),
 ],
 "models_note": "A Tesla időről időre módosítja a program feltételeit — a pontos aktuális jutalmat mindig a tesla.com-os rendelésösszegzésben látod az előleg kifizetése előtt.",
 "faq_label": "03 / Gyakori kérdések",
 "faq_title": "Mielőtt kattintasz",
 "faq": [
   ("Pontosan mit kapok a referral linken keresztül?", "Új Model 3 vagy Model Y rendelésekor ezen a linken keresztül 1 000 km ingyenes Supercharging-ot kapsz. A pontos jutalom a Tesla régiódra érvényes aktuális feltételeitől függ."),
   ("Megváltozik az autó ára?", "Nem. A Tesla fix áron, közvetlenül, kereskedők nélkül értékesít — a referral link sosem változtatja meg a fizetendő összeget. A jutalom azon felüli bónusz."),
   ("Mikor kell használnom a linket?", "A rendelés véglegesítése előtt. A referralt utólag nem lehet hozzáadni — ezért kattints a linkre, mielőtt elkezdenéd a konfigurálást."),
   ("Mely Superchargereken használható a kredit?", "A Tesla valamennyi Superchargerén, itthon és külföldön egyaránt. A kilométereket az autód fogyasztása alapján számolják le."),
   ("Mikor írják jóvá a kreditet?", "Az autó átvétele után. Addig általában „pending” állapotban látható a Tesla fiókodban, és átvétel után aktiválódik az alkalmazásban."),
   ("Hány referralt szerezhet egy tulajdonos évente?", "A Tesla évente legfeljebb 10 sikeres ajánlás után ad jutalmat fiókonként."),
 ],
 "final_title": "Belevágsz?",
 "final_sub": "Egy kattintás a rendelés előtt = 1 000 km ingyenes töltés. A Tesla mindkét esetben ugyanannyit kér az autóért.",
 "final_cta": "Rendelés 1 000 km-rel ingyen",
 "foot_updated": "Utoljára frissítve",
 "foot_note": "Egy Tesla-tulajdonos nem hivatalos oldala. Nincs kapcsolatban a Tesla, Inc.-vel. A Tesla és a Tesla logó a Tesla, Inc. védjegyei.",
 "foot_lang": "Nyelv",
 "alt_check": "Ellenőrizd a program aktuális feltételeit",
},
}

CSS = r"""
:root{
  --bg:#0c0c0e; --panel:#141416; --line:rgba(255,255,255,.08);
  --text:#f4f4f5; --muted:#9d9da6; --red:#e82127; --red-d:#c11418;
  --max:1080px;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased;line-height:1.6;font-size:17px}
a{color:inherit;text-decoration:none}
.wrap{max-width:var(--max);margin:0 auto;padding:0 28px}

/* nav */
nav{position:sticky;top:0;z-index:10;background:rgba(12,12,14,.85);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.nav-in{display:flex;align-items:center;justify-content:space-between;height:64px}
.brand{display:flex;align-items:center;gap:10px;font-weight:650;letter-spacing:.14em;font-size:14px;text-transform:uppercase}
.brand svg{display:block}
.nav-links{display:flex;gap:28px;font-size:14px;color:var(--muted)}
.nav-links a:hover{color:var(--text)}
.langs{display:flex;gap:4px;font-size:12.5px}
.langs a{padding:5px 9px;border-radius:6px;color:var(--muted)}
.langs a:hover{color:var(--text)}
.langs a.on{color:var(--text);background:var(--panel);border:1px solid var(--line)}
@media(max-width:760px){.nav-links{display:none}}

/* hero */
header{padding:96px 0 72px;position:relative;overflow:hidden}
header::before{content:"";position:absolute;inset:0;pointer-events:none;
  background:radial-gradient(720px 380px at 78% -10%,rgba(232,33,39,.10),transparent 60%)}
.eyebrow{font-size:12.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--red);font-weight:600;margin-bottom:22px}
h1{font-size:clamp(38px,5.6vw,64px);line-height:1.06;letter-spacing:-.02em;font-weight:700;max-width:15ch}
.sub{margin-top:24px;max-width:58ch;color:var(--muted);font-size:18.5px}
.cta-row{margin-top:40px;display:flex;align-items:center;gap:22px;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;gap:10px;background:var(--red);color:#fff;font-weight:600;
  padding:16px 30px;border-radius:999px;font-size:16px;transition:.18s;border:1px solid transparent}
.btn:hover{background:var(--red-d);transform:translateY(-1px)}
.btn svg{transition:.18s}
.btn:hover svg{transform:translateX(3px)}
.cta-note{font-size:13px;color:var(--muted);max-width:26ch}
.scroll-link{font-size:14px;color:var(--muted);border-bottom:1px solid var(--line);padding-bottom:2px}
.scroll-link:hover{color:var(--text)}

/* stats */
.stats{border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats-in{display:grid;grid-template-columns:repeat(3,1fr);gap:0}
.stat{padding:34px 28px;border-left:1px solid var(--line)}
.stat:first-child{border-left:none;padding-left:0}
.stat b{display:block;font-size:30px;font-weight:700;letter-spacing:-.01em}
.stat span{font-size:13.5px;color:var(--muted)}
@media(max-width:760px){.stats-in{grid-template-columns:1fr}.stat{border-left:none;border-top:1px solid var(--line);padding-left:28px}.stat:first-child{border-top:none}}

section{padding:88px 0}
.label{font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);font-weight:600;margin-bottom:18px}
h2{font-size:clamp(28px,3.6vw,42px);letter-spacing:-.015em;line-height:1.12;font-weight:700;max-width:22ch}
.section-sub{margin-top:16px;color:var(--muted);max-width:56ch}

/* steps */
.steps{margin-top:56px;display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.step{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:32px 28px}
.step-num{font-size:12px;letter-spacing:.18em;color:var(--red);font-weight:600;margin-bottom:38px}
.step h3{font-size:19px;font-weight:650;margin-bottom:10px;letter-spacing:-.01em}
.step p{font-size:14.5px;color:var(--muted)}
@media(max-width:860px){.steps{grid-template-columns:1fr}}

/* models */
.models-list{margin-top:52px;border-top:1px solid var(--line)}
.mrow{display:flex;justify-content:space-between;gap:24px;padding:26px 4px;border-bottom:1px solid var(--line);align-items:baseline}
.mrow b{font-size:19px;font-weight:650;white-space:nowrap}
.mrow span{color:var(--muted);font-size:15px;text-align:right}
@media(max-width:640px){.mrow{flex-direction:column;gap:6px}.mrow span{text-align:left}}
.note{margin-top:26px;font-size:13.5px;color:var(--muted);display:flex;gap:10px;align-items:flex-start;max-width:68ch}

/* faq */
.faq-list{margin-top:52px;border-top:1px solid var(--line)}
details{border-bottom:1px solid var(--line)}
summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:20px;
  padding:24px 4px;font-size:17.5px;font-weight:550}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";font-size:22px;color:var(--muted);font-weight:300;transition:.2s;flex-shrink:0}
details[open] summary::after{transform:rotate(45deg);color:var(--red)}
details p{padding:0 4px 26px;color:var(--muted);max-width:72ch;font-size:15.5px}

/* final */
.final{background:var(--panel);border-top:1px solid var(--line);border-bottom:1px solid var(--line);text-align:center}
.final h2{margin:0 auto}
.final .section-sub{margin:18px auto 0}
.final .btn{margin-top:36px}

footer{padding:52px 0 64px;font-size:13px;color:var(--muted)}
.foot-grid{display:flex;justify-content:space-between;gap:32px;flex-wrap:wrap}
.foot-note{max-width:52ch}
.foot-langs b{color:var(--text);font-weight:600}
.foot-langs a{border-bottom:1px solid transparent}
.foot-langs a:hover{border-color:var(--muted)}
.foot-updated{margin-top:28px;padding-top:22px;border-top:1px solid var(--line);display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
"""

ICONS = {
 "bolt": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h7l-1 8 11-13h-8l1-7z"/></svg>',
 "wordmark": '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M4 13c2.5 0 4-1.6 8-1.6s5.5 1.6 8 1.6c-2.5 0-4-1.6-8-1.6S6.5 13 4 13zm8-9c3.5 0 5.6.6 7.5 1.3C18.6 4 15.9 3 12 3S5.4 4 4.5 5.3C6.4 4.6 8.5 4 12 4zm0 16c-3.5 0-5.6-.6-7.5-1.3C5.4 20 8.1 21 12 21s6.6-1 7.5-2.3C17.6 19.4 15.5 20 12 20z"/></svg>',
 "arrow": '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "info": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" style="flex-shrink:0;margin-top:2px"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></svg>',
}

def page_url(lang):
    d = LANGS[lang]["dir"]
    return f"{BASE}/{d}" if d else f"{BASE}/"

def render(lang):
    t = T[lang]
    cur = LANGS[lang]["dir"]
    def href(other):
        od = LANGS[other]["dir"]
        pre = "../" if cur else ""
        return pre + (od if od else "") + "index.html"

    # relative prefix for assets
    pre = "../" if cur else ""

    hreflang = "\n".join(
        f'    <link rel="alternate" hreflang="{T[l]["html_lang"]}" href="{page_url(l)}">' for l in LANGS
    ) + f'\n    <link rel="alternate" hreflang="x-default" href="{page_url("en")}">'

    steps_html = "\n".join(f'''
      <div class="step">
        <div class="step-num">{i+1:02d}</div>
        <h3>{s[0]}</h3>
        <p>{s[1]}</p>
      </div>''' for i, s in enumerate(t["steps"]))

    stats_html = "\n".join(f'''
      <div class="stat"><b>{a}</b><span>{b}</span></div>''' for a, b in t["stats"])

    models_html = "\n".join(f'''
      <div class="mrow"><b>{a}</b><span>{b}</span></div>''' for a, b in t["models"])

    faq_html = "\n".join(f'''
      <details>
        <summary>{q}</summary>
        <p>{a}</p>
      </details>''' for q, a in t["faq"])

    faq_schema = {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]],
    }
    import json
    faq_json = json.dumps(faq_schema, ensure_ascii=False, indent=2)

    lang_links = " ".join(
        f'<a href="{href(l)}"{" class=\"on\"" if l == lang else ""}>{l.upper()}</a>' for l in LANGS
    )
    foot_langs = " · ".join(
        f'<a href="{href(l)}">{l.upper()}</a>' for l in LANGS
    )

    site_schema = {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "tesla-referral",
      "url": page_url(lang),
      "inLanguage": t["html_lang"],
    }

    return f"""<!DOCTYPE html>
<html lang="{t["html_lang"]}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{t["title"]}</title>
    <meta name="description" content="{t["description"]}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{page_url(lang)}">
{hreflang}
    <meta property="og:type" content="website">
    <meta property="og:title" content="{t["title"]}">
    <meta property="og:description" content="{t["description"]}">
    <meta property="og:url" content="{page_url(lang)}">
    <meta property="og:locale" content="{t["html_lang"]}">
    <meta name="theme-color" content="#0c0c0e">
    <link rel="stylesheet" href="{pre}assets/site.css">
    <script type="application/ld+json">
{json.dumps(site_schema, ensure_ascii=False)}
    </script>
    <script type="application/ld+json">
{faq_json}
    </script>
</head>
<body>

<nav>
  <div class="wrap nav-in">
    <a class="brand" href="{pre}index.html">{ICONS["wordmark"]} tesla-referral</a>
    <div class="nav-links">
      <a href="#how">{t["anchor_how"]}</a>
      <a href="#faq">{t["anchor_faq"]}</a>
    </div>
    <div class="langs">{lang_links}</div>
  </div>
</nav>

<header>
  <div class="wrap">
    <div class="eyebrow">{t["eyebrow"]}</div>
    <h1>{t["h1"]}</h1>
    <p class="sub">{t["sub"]}</p>
    <div class="cta-row">
      <a class="btn" href="{REF_LINK}" rel="sponsored noopener" target="_blank">{t["cta"]} {ICONS["arrow"]}</a>
      <span class="cta-note">{t["cta_note"]}</span>
      <a class="scroll-link" href="#how">{t["anchor_how"]} ↓</a>
    </div>
  </div>
</header>

<div class="stats">
  <div class="wrap stats-in">{stats_html}
  </div>
</div>

<section id="how">
  <div class="wrap">
    <div class="label">{t["how_label"]}</div>
    <h2>{t["how_title"]}</h2>
    <p class="section-sub">{t["how_sub"]}</p>
    <div class="steps">{steps_html}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="label">{t["models_label"]}</div>
    <h2>{t["models_title"]}</h2>
    <div class="models-list">{models_html}
    </div>
    <p class="note">{ICONS["info"]}<span>{t["models_note"]}</span></p>
  </div>
</section>

<section id="faq">
  <div class="wrap">
    <div class="label">{t["faq_label"]}</div>
    <h2>{t["faq_title"]}</h2>
    <div class="faq-list">{faq_html}
    </div>
  </div>
</section>

<section class="final">
  <div class="wrap">
    <h2>{t["final_title"]}</h2>
    <p class="section-sub">{t["final_sub"]}</p>
    <a class="btn" href="{REF_LINK}" rel="sponsored noopener" target="_blank">{t["final_cta"]} {ICONS["arrow"]}</a>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="foot-grid">
      <p class="foot-note">{t["foot_note"]}</p>
      <p class="foot-langs"><b>{t["foot_lang"]}:</b> {foot_langs}</p>
    </div>
    <div class="foot-updated">
      <span>{t["foot_updated"]}: {UPDATED}</span>
      <a href="https://www.tesla.com/support/referral-program" target="_blank" rel="noopener">{t["alt_check"]} →</a>
    </div>
  </div>
</footer>

</body>
</html>
"""

ROBOTS = f"""User-agent: *
Allow: /
Sitemap: {BASE}/sitemap.xml
"""

SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
""" + "\n".join(f"""  <url>
    <loc>{page_url(l)}</loc>
{chr(10).join(f'    <xhtml:link rel="alternate" hreflang="{T[o]["html_lang"]}" href="{page_url(o)}"/>' for o in LANGS)}
    <xhtml:link rel="alternate" hreflang="x-default" href="{page_url("en")}"/>
  </url>""" for l in LANGS) + "\n</urlset>\n"

README = f"""# tesla-referral

Multilingual landing page for the Tesla Refer & Earn program (CZ / SK / HU / EN / DE),
static HTML on GitHub Pages: {BASE}

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
"""

def main():
    (ROOT / "assets").mkdir(parents=True, exist_ok=True)
    (ROOT / "assets" / "site.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    for lang in LANGS:
        d = LANGS[lang]["dir"]
        outdir = ROOT / d if d else ROOT
        outdir.mkdir(parents=True, exist_ok=True)
        (outdir / "index.html").write_text(render(lang), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(SITEMAP, encoding="utf-8")
    (ROOT / "robots.txt").write_text(ROBOTS, encoding="utf-8")
    (ROOT / "README.md").write_text(README, encoding="utf-8")
    print("Generated:", ", ".join(LANGS))

if __name__ == "__main__":
    main()
