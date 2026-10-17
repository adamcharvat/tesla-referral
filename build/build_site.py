#!/usr/bin/env python3
"""Generator for the tesla-referral landing page (CZ/SK/HU/EN/DE).

Edit REF_LINK below, then run:  python3 build/build_site.py
Outputs the static site into the repository root.
"""
import json
import pathlib

REF_LINK = "https://ts.la/REPLACE_ME"  # <- put your real referral link here
REF_CODE = "ts.la/REPLACE_ME"          # <- short form shown in the copy field
BASE = "https://adamcharvat.github.io/tesla-referral"
UPDATED = "October 2026"

ROOT = pathlib.Path(__file__).resolve().parent.parent

LANGS = ["cs", "sk", "en", "de", "hu"]
LANG_DIR = {"cs": "", "sk": "sk/", "en": "en/", "de": "de/", "hu": "hu/"}

T = {
"cs": {
 "html_lang": "cs",
 "title": "Tesla referral kód 2026 — 1 000 km Supercharging zdarma k nové Tesle",
 "description": "Objednej si novou Teslu (Model 3 / Model Y) přes tento referral odkaz a získej 1 000 km volného dobíjení na Superchargerech zdarma. Cena auta se nemění — využij oficiální Tesla Refer & Earn program.",
 "eyebrow": "Tesla referral program · 2026",
 "h1a": "1 000 km",
 "h1b": "Supercharging zdarma",
 "h1c": "k nové Tesle",
 "sub": "Objednej si nový Model 3 nebo Model Y přes tento referral odkaz a Tesla ti po převzetí vozu připíše 1 000 km volného dobíjení. Nic tě to nestojí — cena auta je stejná, jako kdybys objednával bez odkazu.",
 "cta": "Získat 1 000 km zdarma",
 "cta_note": "Přesměrování na oficiální stránku Tesla · bez kódu, stačí kliknout",
 "copy_label": "Nebo si odkaz zkopíruj",
 "copy_btn": "Kopírovat",
 "copy_done": "Zkopírováno",
 "anchor_how": "Jak to funguje",
 "anchor_faq": "Časté otázky",
 "theme_aria": "Přepnout světlý a tmavý režim",
 "stats": [("1 000 km", "volného Supercharging k novému vozu"), ("0 Kč navíc", "cena Tesly se odkazem nemění"), ("~500 €", "kredit pro doporučujícího majitele")],
 "how_label": "Jak to funguje",
 "how_title": "Tři kroky a je to",
 "how_sub": "Celé to trvá asi tak dlouho jako kliknout na odkaz. Pozor jen na jedno — referral musíš použít předtím, než objednávku dokončíš.",
 "steps": [
   ("Klikni na referral odkaz", "Odkaz tě přenese na oficiální české stránky Tesla s předvyplněným referral kódem. Nic zapisovat nemusíš."),
   ("Nakonfiguruj si Teslu", "Vyber model, barvu a výbavu jako obvykle a objednávku dokonči. V souhrnu objednávky uvidíš potvrzení referralu."),
   ("Dobíjej zdarma", "Po převzetí vozu ti Tesla připíše 1 000 km volného Supercharging do aplikace. Kredit můžeš čerpat po celé Evropě."),
 ],
 "models_label": "Co platí",
 "models_title": "Komu a na co se referral vztahuje",
 "models": [
   ("Model 3", "Nové objednávky Modelu 3 — 1 000 km volného Supercharging."),
   ("Model Y", "Nové objednávky Modelu Y — 1 000 km volného Supercharging."),
   ("Region ČR", "Odměna se řídí regionem objednávky a platnými podmínkami pro ČR."),
 ],
 "models_note": "Podmínky programu Tesla průběžně upravuje — přesnou aktuální odměnu vždy uvidíš v souhrnu objednávky na tesla.com ještě před zaplacením zálohy.",
 "faq_label": "Časté otázky",
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
 "h1a": "1 000 km",
 "h1b": "Supercharging zadarmo",
 "h1c": "k novej Tesle",
 "sub": "Objednaj si nový Model 3 alebo Model Y cez tento referral odkaz a Tesla ti po prevzatí auta pripíše 1 000 km voľného nabíjania. Nestojí ťa to nič — cena auta je rovnaká ako bez odkazu.",
 "cta": "Získať 1 000 km zadarmo",
 "cta_note": "Presmerovanie na oficiálnu stránku Tesla · stačí kliknúť, bez kódu",
 "copy_label": "Alebo si odkaz skopíruj",
 "copy_btn": "Kopírovať",
 "copy_done": "Skopírované",
 "anchor_how": "Ako to funguje",
 "anchor_faq": "Časté otázky",
 "theme_aria": "Prepnúť svetlý a tmavý režim",
 "stats": [("1 000 km", "voľného Supercharging k novému autu"), ("0 € navyše", "cena Tesly sa odkazom nemení"), ("~500 €", "kredit pre odporúčajúceho majiteľa")],
 "how_label": "Ako to funguje",
 "how_title": "Tri kroky a je to",
 "how_sub": "Celé to trvá približne tak dlho, ako kliknúť na odkaz. Jediné, na čo si daj pozor — referral treba použiť pred dokončením objednávky.",
 "steps": [
   ("Klikni na referral odkaz", "Odkaz ťa presmeruje na oficiálne slovenské stránky Tesla s predvyplneným referral kódom. Nič vypisovať nemusíš."),
   ("Nakonfiguruj si Teslu", "Vyber model, farbu a výbavu ako obvykle a dokonči objednávku. V súhrne uvidíš potvrdenie referralu."),
   ("Nabíjaj zadarmo", "Po prevzatí auta ti Tesla pripíše 1 000 km voľného Supercharging do aplikácie. Kredit môžeš čerpať po celej Európe."),
 ],
 "models_label": "Čo platí",
 "models_title": "Komu a na čo sa referral vzťahuje",
 "models": [
   ("Model 3", "Nové objednávky Modelu 3 — 1 000 km voľného Supercharging."),
   ("Model Y", "Nové objednávky Modelu Y — 1 000 km voľného Supercharging."),
   ("Región SR", "Odmena sa riadi regiónom objednávky a platnými podmienkami pre SR."),
 ],
 "models_note": "Tesla podmienky programu priebežne upravuje — presnú aktuálnu odmenu vždy uvidíš v súhrne objednávky na tesla.com ešte pred zaplatením zálohy.",
 "faq_label": "Časté otázky",
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
 "h1a": "1,000 km",
 "h1b": "Free Supercharging",
 "h1c": "with your new Tesla",
 "sub": "Order a new Model 3 or Model Y through this referral link and Tesla will credit 1,000 km of free charging when you take delivery. It costs you nothing — the car's price is exactly the same as ordering without a link.",
 "cta": "Get 1,000 km free",
 "cta_note": "Takes you to the official Tesla site · one click, no code to type",
 "copy_label": "Or copy the link",
 "copy_btn": "Copy",
 "copy_done": "Copied",
 "anchor_how": "How it works",
 "anchor_faq": "FAQ",
 "theme_aria": "Toggle light and dark mode",
 "stats": [("1,000 km", "of free Supercharging with a new car"), ("€0 extra", "the Tesla price never changes"), ("~€500", "credit for the referring owner")],
 "how_label": "How it works",
 "how_title": "Three steps, that's it",
 "how_sub": "It takes about as long as clicking a link. One thing to remember: the referral must be used before you complete your order.",
 "steps": [
   ("Click the referral link", "You're taken to the official Tesla site with the referral code already attached. Nothing to type in."),
   ("Configure your Tesla", "Pick your model, colour and options as usual and place the order. You'll see the referral confirmed in the order summary."),
   ("Charge for free", "After delivery, Tesla credits 1,000 km of free Supercharging to your app. Use it across Europe."),
 ],
 "models_label": "What applies",
 "models_title": "Who and what the referral covers",
 "models": [
   ("Model 3", "New Model 3 orders — 1,000 km of free Supercharging."),
   ("Model Y", "New Model Y orders — 1,000 km of free Supercharging."),
   ("Your region", "The reward follows the region of your order and Tesla's current local terms."),
 ],
 "models_note": "Tesla adjusts the program terms from time to time — the exact current reward is always shown in your order summary on tesla.com before you pay the deposit.",
 "faq_label": "FAQ",
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
 "h1a": "1.000 km",
 "h1b": "Gratis-Supercharging",
 "h1c": "zum neuen Tesla",
 "sub": "Bestelle einen neuen Model 3 oder Model Y über diesen Empfehlungslink und Tesla schreibt dir nach Übergabe 1.000 km kostenloses Laden gut. Es kostet dich nichts — der Preis ist derselbe wie ohne Link.",
 "cta": "1.000 km gratis sichern",
 "cta_note": "Weiterleitung zur offiziellen Tesla-Seite · ein Klick, kein Code nötig",
 "copy_label": "Oder kopiere den Link",
 "copy_btn": "Kopieren",
 "copy_done": "Kopiert",
 "anchor_how": "So funktioniert's",
 "anchor_faq": "Häufige Fragen",
 "theme_aria": "Helles und dunkles Design wechseln",
 "stats": [("1.000 km", "Gratis-Supercharging zum Neuwagen"), ("0 € extra", "der Tesla-Preis bleibt gleich"), ("~500 €", "Guthaben für den Empfehlungsgeber")],
 "how_label": "So funktioniert's",
 "how_title": "Drei Schritte, fertig",
 "how_sub": "Es dauert ungefähr so lange wie ein Klick. Einzige Regel: Die Empfehlung muss vor Abschluss der Bestellung verwendet werden.",
 "steps": [
   ("Empfehlungslink anklicken", "Der Link führt dich zur offiziellen Tesla-Seite, der Code ist bereits hinterlegt. Nichts eingeben, nichts kopieren."),
   ("Tesla konfigurieren", "Wähle Modell, Farbe und Ausstattung wie gewohnt und schließe die Bestellung ab. Die Empfehlung siehst du in der Bestellübersicht."),
   ("Kostenlos laden", "Nach Übergabe schreibt Tesla dir 1.000 km Gratis-Supercharging in die App gut — nutzbar an allen Superchargern in Europa."),
 ],
 "models_label": "Was gilt",
 "models_title": "Für wen und für was gilt der Code",
 "models": [
   ("Model 3", "Neubestellungen des Model 3 — 1.000 km Gratis-Supercharging."),
   ("Model Y", "Neubestellungen des Model Y — 1.000 km Gratis-Supercharging."),
   ("Deine Region", "Die Prämie richtet sich nach der Region der Bestellung und den aktuellen Bedingungen von Tesla."),
 ],
 "models_note": "Tesla passt die Programmbedingungen regelmäßig an — die exakt aktuelle Prämie siehst du immer in der Bestellübersicht auf tesla.com, bevor du die Anzahlung zahlst.",
 "faq_label": "Häufige Fragen",
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
 "h1a": "1 000 km",
 "h1b": "Ingyenes Supercharging",
 "h1c": "az új Tesládhoz",
 "sub": "Rendelj új Model 3-at vagy Model Y-t ezen a referral linken keresztül, és az átvétel után a Tesla 1 000 km ingyenes töltést ír jóvá. Semmibe nem kerül — az autó ára ugyanannyi, mintha link nélkül rendelnéd.",
 "cta": "1 000 km ingyen",
 "cta_note": "A hivatalos Tesla oldalra visz · egy kattintás, kód nélkül",
 "copy_label": "Vagy másold ki a linket",
 "copy_btn": "Másolás",
 "copy_done": "Másolva",
 "anchor_how": "Így működik",
 "anchor_faq": "Gyakori kérdések",
 "theme_aria": "Váltás világos és sötét mód között",
 "stats": [("1 000 km", "ingyenes Supercharging az új autóhoz"), ("0 Ft többlet", "a Tesla ára nem változik"), ("~500 €", "kredit az ajánló tulajdonosnak")],
 "how_label": "Így működik",
 "how_title": "Három lépés, ennyi",
 "how_sub": "Körülbelül annyi időbe telik, mint egy linkre kattintani. Egy dolgot ne felejts el: a referralt a rendelés véglegesítése előtt kell használni.",
 "steps": [
   ("Kattints a referral linkre", "A link a hivatalos Tesla oldalra visz, az ajánlókód már előre be van állítva. Semmit nem kell begépelned."),
   ("Konfiguráld a Teslát", "Válaszd ki a modellt, a színt és a felszereltséget a szokásos módon, majd fejezd be a rendelést. A rendelés összegzésében látod a referral visszaigazolását."),
   ("Tölts ingyen", "Átvétel után a Tesla 1 000 km ingyenes Supercharging-ot ír jóvá az alkalmazásodban. Európa-szerte használható."),
 ],
 "models_label": "Mi érvényes",
 "models_title": "Kire és mire vonatkozik a referral",
 "models": [
   ("Model 3", "Új Model 3 rendelések — 1 000 km ingyenes Supercharging."),
   ("Model Y", "Új Model Y rendelések — 1 000 km ingyenes Supercharging."),
   ("Régiód", "A jutalom a rendelés régiójától és a Tesla aktuális helyi feltételeitől függ."),
 ],
 "models_note": "A Tesla időről időre módosítja a program feltételeit — a pontos aktuális jutalmat mindig a tesla.com-os rendelésösszegzésben látod az előleg kifizetése előtt.",
 "faq_label": "Gyakori kérdések",
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
/* ---------- theme tokens ---------- */
:root{
  --bg:#f7f6f3; --panel:#ffffff; --ink:#131315; --muted:#63636b;
  --line:#e5e3dc; --accent:#c8102e; --accent-d:#a50d26;
  --hero-img:url("img/hero.jpg"); --chip-bg:rgba(255,255,255,.14); --chip-line:rgba(255,255,255,.35);
  --shadow:0 20px 50px -20px rgba(0,0,0,.18);
  --max:1140px;
}
html[data-theme="dark"]{
  --bg:#0b0b0d; --panel:#151517; --ink:#f4f4f3; --muted:#9c9ca4;
  --line:rgba(255,255,255,.09); --accent:#e82127; --accent-d:#c11418;
  --hero-img:url("img/hero-night.jpg"); --chip-bg:rgba(10,10,12,.45); --chip-line:rgba(255,255,255,.28);
  --shadow:0 20px 50px -20px rgba(0,0,0,.6);
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);
  font-family:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased;line-height:1.6;font-size:17px;
  transition:background .35s ease,color .35s ease}
a{color:inherit;text-decoration:none}
.wrap{max-width:var(--max);margin:0 auto;padding:0 28px}
.serif{font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-weight:400;letter-spacing:0}

/* ---------- nav ---------- */
nav{position:fixed;top:0;left:0;right:0;z-index:20;transition:background .3s,border-color .3s;border-bottom:1px solid transparent}
nav.scrolled{background:color-mix(in srgb,var(--bg) 82%,transparent);backdrop-filter:blur(16px);border-color:var(--line)}
.nav-in{display:flex;align-items:center;justify-content:space-between;height:72px}
.brand{display:flex;align-items:center;gap:10px;font-weight:600;letter-spacing:.16em;font-size:13px;text-transform:uppercase;color:#fff}
nav.scrolled .brand,nav.solid .brand{color:var(--ink)}
.nav-cta{display:flex;align-items:center;gap:14px}
.theme-btn{width:38px;height:38px;border-radius:50%;border:1px solid rgba(255,255,255,.35);background:transparent;color:#fff;
  display:inline-flex;align-items:center;justify-content:center;cursor:pointer;transition:.2s}
nav.scrolled .theme-btn,nav.solid .theme-btn{border-color:var(--line);color:var(--ink)}
.theme-btn:hover{transform:rotate(15deg)}
html[data-theme="dark"] .icon-moon{display:none}
html[data-theme="light"] .icon-sun{display:none}
.langs{display:flex;gap:2px;font-size:12.5px}
.langs a{padding:5px 8px;border-radius:99px;color:rgba(255,255,255,.75);transition:.15s}
nav.scrolled .langs a,nav.solid .langs a{color:var(--muted)}
.langs a:hover{color:#fff}
nav.scrolled .langs a:hover,nav.solid .langs a:hover{color:var(--ink)}
.langs a.on{color:#fff;background:var(--chip-bg);border:1px solid var(--chip-line)}
nav.scrolled .langs a.on,nav.solid .langs a.on{color:var(--ink);border-color:var(--line);background:var(--panel)}

/* ---------- hero ---------- */
.hero{position:relative;min-height:94vh;display:flex;align-items:flex-end;
  background-image:linear-gradient(to top,rgba(0,0,0,.82) 0%,rgba(0,0,0,.35) 42%,rgba(0,0,0,.12) 70%),var(--hero-img);
  background-size:cover;background-position:center 62%;transition:background-image .4s}
.hero-in{width:100%;padding-bottom:84px}
.hero .eyebrow{color:rgba(255,255,255,.85);font-size:12.5px;letter-spacing:.24em;text-transform:uppercase;font-weight:600;margin-bottom:20px}
.hero h1{color:#fff;font-size:clamp(44px,6.4vw,84px);line-height:1.02;letter-spacing:-.025em;font-weight:600;max-width:13ch}
.hero h1 .thin{display:block;font-weight:300}
.hero h1 .serif{font-weight:400}
.hero .sub{margin-top:22px;max-width:54ch;color:rgba(255,255,255,.82);font-size:18px}
.cta-row{margin-top:38px;display:flex;align-items:center;gap:20px;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;gap:10px;background:var(--accent);color:#fff;font-weight:600;
  padding:17px 32px;border-radius:99px;font-size:16px;transition:.18s;border:1px solid transparent}
.btn:hover{background:var(--accent-d);transform:translateY(-2px);box-shadow:0 12px 30px -10px var(--accent)}
.btn svg{transition:.18s}
.btn:hover svg{transform:translateX(3px)}
.cta-note{font-size:13px;color:rgba(255,255,255,.65);max-width:24ch}
.copy-block{margin-top:26px;display:inline-flex;align-items:center;gap:0;border:1px solid var(--chip-line);
  background:var(--chip-bg);backdrop-filter:blur(10px);border-radius:99px;padding:6px 6px 6px 20px;max-width:100%}
.copy-block .copy-label{font-size:12px;color:rgba(255,255,255,.65);margin-right:12px;white-space:nowrap}
.copy-block code{font-family:"SF Mono",ui-monospace,Menlo,monospace;font-size:14.5px;color:#fff;letter-spacing:.02em;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:34vw}
.copy-btn{margin-left:14px;flex-shrink:0;background:rgba(255,255,255,.92);color:#111;border:none;border-radius:99px;
  padding:9px 18px;font-size:13px;font-weight:600;cursor:pointer;font-family:inherit;transition:.15s;display:inline-flex;align-items:center;gap:7px}
.copy-btn:hover{background:#fff}
.copy-btn.done{background:#1d9e57;color:#fff}
@media(max-width:640px){.copy-block{width:100%;border-radius:18px;flex-wrap:wrap;row-gap:8px}.copy-block code{max-width:100%}}

/* ---------- stats ---------- */
.stats{background:var(--panel);border-bottom:1px solid var(--line);transition:background .35s}
.stats-in{display:grid;grid-template-columns:repeat(3,1fr)}
.stat{padding:44px 32px;border-left:1px solid var(--line)}
.stat:first-child{border-left:none;padding-left:0}
.stat b{display:block;font-size:clamp(28px,3vw,38px);font-weight:600;letter-spacing:-.02em}
.stat span{font-size:13.5px;color:var(--muted)}
@media(max-width:760px){.stats-in{grid-template-columns:1fr}.stat{border-left:none;border-top:1px solid var(--line);padding:28px 0}.stat:first-child{border-top:none}}

/* ---------- sections ---------- */
section{padding:104px 0}
.label{font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);font-weight:600;margin-bottom:18px}
.label::before{content:"";display:inline-block;width:26px;height:1px;background:var(--accent);vertical-align:middle;margin-right:12px}
h2{font-size:clamp(30px,3.8vw,46px);letter-spacing:-.02em;line-height:1.1;font-weight:600;max-width:24ch}
.section-sub{margin-top:18px;color:var(--muted);max-width:56ch;font-size:17px}

/* steps — editorial numbered rows */
.steps{margin-top:64px;border-top:1px solid var(--line)}
.step{display:grid;grid-template-columns:90px 1fr 1.2fr;gap:32px;padding:38px 0;border-bottom:1px solid var(--line);align-items:baseline;transition:background .2s}
.step:hover{background:var(--panel)}
.step-num{font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-size:30px;color:var(--accent)}
.step h3{font-size:21px;font-weight:600;letter-spacing:-.01em}
.step p{font-size:15px;color:var(--muted)}
@media(max-width:820px){.step{grid-template-columns:56px 1fr}.step p{grid-column:2}}

/* split — image + models */
.split{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center}
.split-img{position:relative}
.split-img img{width:100%;height:560px;object-fit:cover;border-radius:20px;box-shadow:var(--shadow);display:block}
.split-img figcaption{position:absolute;left:20px;bottom:16px;font-size:12px;color:rgba(255,255,255,.85);letter-spacing:.06em}
@media(max-width:900px){.split{grid-template-columns:1fr}.split-img img{height:380px}}

/* models */
.models-list{border-top:1px solid var(--line);margin-top:8px}
.mrow{display:flex;justify-content:space-between;gap:24px;padding:24px 2px;border-bottom:1px solid var(--line);align-items:baseline}
.mrow b{font-size:18px;font-weight:600;white-space:nowrap}
.mrow span{color:var(--muted);font-size:14.5px;text-align:right}
.note{margin-top:26px;font-size:13.5px;color:var(--muted);display:flex;gap:10px;align-items:flex-start;max-width:60ch}
.note svg{flex-shrink:0;margin-top:2px}

/* faq */
.faq-list{margin-top:56px;border-top:1px solid var(--line)}
details{border-bottom:1px solid var(--line)}
summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:20px;
  padding:26px 2px;font-size:18px;font-weight:550;letter-spacing:-.01em;transition:color .15s}
summary::-webkit-details-marker{display:none}
summary:hover{color:var(--accent)}
summary::after{content:"+";font-size:24px;color:var(--muted);font-weight:300;transition:.25s;flex-shrink:0}
details[open] summary::after{transform:rotate(45deg);color:var(--accent)}
details p{padding:0 2px 28px;color:var(--muted);max-width:72ch;font-size:15.5px}

/* final */
.final{position:relative;overflow:hidden;background-image:linear-gradient(to bottom,rgba(0,0,0,.55),rgba(0,0,0,.75)),url("img/hero-night.jpg");
  background-size:cover;background-position:center 40%;text-align:center}
.final h2,.final .section-sub{margin-left:auto;margin-right:auto}
.final h2{color:#fff}
.final .section-sub{color:rgba(255,255,255,.8)}
.final .btn{margin-top:40px}

/* footer */
footer{padding:60px 0 72px;font-size:13px;color:var(--muted)}
.foot-grid{display:flex;justify-content:space-between;gap:32px;flex-wrap:wrap}
.foot-note{max-width:52ch}
.foot-langs b{color:var(--ink);font-weight:600}
.foot-langs a{border-bottom:1px solid transparent}
.foot-langs a:hover{border-color:var(--muted)}
.foot-updated{margin-top:32px;padding-top:24px;border-top:1px solid var(--line);display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
"""

ICONS = {
 "bolt": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h7l-1 8 11-13h-8l1-7z"/></svg>',
 "wordmark": '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M4 13c2.5 0 4-1.6 8-1.6s5.5 1.6 8 1.6c-2.5 0-4-1.6-8-1.6S6.5 13 4 13zm8-9c3.5 0 5.6.6 7.5 1.3C18.6 4 15.9 3 12 3S5.4 4 4.5 5.3C6.4 4.6 8.5 4 12 4zm0 16c-3.5 0-5.6-.6-7.5-1.3C5.4 20 8.1 21 12 21s6.6-1 7.5-2.3C17.6 19.4 15.5 20 12 20z"/></svg>',
 "arrow": '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "info": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></svg>',
 "sun": '<svg class="icon-sun" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.4M12 19.1v2.4M2.5 12h2.4M19.1 12h2.4M5 5l1.7 1.7M17.3 17.3 19 19M19 5l-1.7 1.7M6.7 17.3 5 19"/></svg>',
 "moon": '<svg class="icon-moon" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.6 14.2A8.6 8.6 0 0 1 9.8 3.4a8.6 8.6 0 1 0 10.8 10.8z"/></svg>',
 "copy": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="12" height="12" rx="2.5"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>',
 "check": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5 9.5 18 20 6.5"/></svg>',
}

THEME_BOOT = """
(function(){try{var t=localStorage.getItem('tr-theme');if(!t){t=window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'}document.documentElement.dataset.theme=t}catch(e){document.documentElement.dataset.theme='light'}})();
"""

MAIN_JS = """
(function(){
  // theme toggle
  document.querySelectorAll('.theme-btn').forEach(function(btn){
    btn.addEventListener('click',function(){
      var cur=document.documentElement.dataset.theme==='dark'?'light':'dark';
      document.documentElement.dataset.theme=cur;
      try{localStorage.setItem('tr-theme',cur)}catch(e){}
    });
  });
  // nav background on scroll
  var nav=document.querySelector('nav');
  function onScroll(){nav.classList.toggle('scrolled',window.scrollY>40)}
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();
  // copy link
  document.querySelectorAll('.copy-btn').forEach(function(btn){
    btn.addEventListener('click',function(){
      var code=btn.closest('.copy-block').querySelector('code').textContent.trim();
      var done=function(){
        var label=btn.querySelector('span');
        btn.classList.add('done');
        btn.innerHTML='__CHECK__<span>'+btn.dataset.done+'</span>';
        setTimeout(function(){btn.classList.remove('done');btn.innerHTML='__COPY__<span>'+btn.dataset.label+'</span>'},2200);
      };
      if(navigator.clipboard&&navigator.clipboard.writeText){
        navigator.clipboard.writeText(code).then(done).catch(function(){fallback()});
      }else{fallback()}
      function fallback(){
        var ta=document.createElement('textarea');ta.value=code;document.body.appendChild(ta);ta.select();
        try{document.execCommand('copy')}catch(e){}document.body.removeChild(ta);done();
      }
    });
  });
})();
"""

def page_url(lang):
    d = LANG_DIR[lang]
    return f"{BASE}/{d}" if d else f"{BASE}/"

def render(lang):
    t = T[lang]
    cur = LANG_DIR[lang]
    pre = "../" if cur else ""

    def href(other):
        return pre + (LANG_DIR[other] or "") + "index.html"

    hreflang = "\n".join(
        f'    <link rel="alternate" hreflang="{T[l]["html_lang"]}" href="{page_url(l)}">' for l in LANGS
    ) + f'\n    <link rel="alternate" hreflang="x-default" href="{page_url("en")}">'

    stats_html = "\n".join(f'      <div class="stat"><b>{a}</b><span>{b}</span></div>' for a, b in t["stats"])
    steps_html = "\n".join(f'''      <div class="step">
        <div class="step-num">{i+1:02d}</div>
        <h3>{s[0]}</h3>
        <p>{s[1]}</p>
      </div>''' for i, s in enumerate(t["steps"]))
    models_html = "\n".join(f'      <div class="mrow"><b>{a}</b><span>{b}</span></div>' for a, b in t["models"])
    faq_html = "\n".join(f'''      <details>
        <summary>{q}</summary>
        <p>{a}</p>
      </details>''' for q, a in t["faq"])

    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    site_schema = {"@context": "https://schema.org", "@type": "WebSite",
        "name": "tesla-referral", "url": page_url(lang), "inLanguage": t["html_lang"]}

    lang_links = "".join(
        f'<a href="{href(l)}"{" class=\"on\"" if l == lang else ""}>{l.upper()}</a>' for l in LANGS)
    foot_langs = " · ".join(f'<a href="{href(l)}">{l.upper()}</a>' for l in LANGS)

    js = MAIN_JS.replace("__CHECK__", ICONS["check"]).replace("__COPY__", ICONS["copy"])

    return f"""<!DOCTYPE html>
<html lang="{t["html_lang"]}" data-theme="light">
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
    <meta property="og:image" content="{BASE}/assets/img/hero.jpg">
    <meta property="og:locale" content="{t["html_lang"]}">
    <meta name="theme-color" content="#f7f6f3">
    <script>{THEME_BOOT.strip()}</script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{pre}assets/site.css">
    <script type="application/ld+json">
{json.dumps(site_schema, ensure_ascii=False, indent=2)}
    </script>
    <script type="application/ld+json">
{json.dumps(faq_schema, ensure_ascii=False, indent=2)}
    </script>
</head>
<body>

<nav aria-label="Main">
  <div class="wrap nav-in">
    <a class="brand" href="{pre}index.html">{ICONS["wordmark"]} tesla-referral</a>
    <div class="nav-cta">
      <div class="langs" role="group" aria-label="Language">{lang_links}</div>
      <button class="theme-btn" type="button" aria-label="{t["theme_aria"]}" title="{t["theme_aria"]}">{ICONS["sun"]}{ICONS["moon"]}</button>
    </div>
  </div>
</nav>

<header class="hero">
  <div class="wrap hero-in">
    <div class="eyebrow">{t["eyebrow"]}</div>
    <h1><span class="thin">{t["h1a"]}</span>{t["h1b"]} <span class="serif">{t["h1c"]}</span></h1>
    <p class="sub">{t["sub"]}</p>
    <div class="cta-row">
      <a class="btn" href="{REF_LINK}" rel="sponsored noopener" target="_blank">{t["cta"]} {ICONS["arrow"]}</a>
      <span class="cta-note">{t["cta_note"]}</span>
    </div>
    <div class="copy-block">
      <span class="copy-label">{t["copy_label"]}</span>
      <code>{REF_CODE}</code>
      <button class="copy-btn" type="button" data-label="{t["copy_btn"]}" data-done="{t["copy_done"]}">{ICONS["copy"]}<span>{t["copy_btn"]}</span></button>
    </div>
  </div>
</header>

<main>
  <div class="stats">
    <div class="wrap stats-in">{stats_html}
    </div>
  </div>

  <section id="how" aria-labelledby="how-title">
    <div class="wrap">
      <div class="label">{t["how_label"]}</div>
      <h2 id="how-title">{t["how_title"]}</h2>
      <p class="section-sub">{t["how_sub"]}</p>
      <div class="steps">{steps_html}
      </div>
    </div>
  </section>

  <section aria-labelledby="models-title">
    <div class="wrap split">
      <figure class="split-img">
        <img src="{pre}assets/img/detail.jpg" alt="" loading="lazy">
        <figcaption>SUPERCHARGING</figcaption>
      </figure>
      <div>
        <div class="label">{t["models_label"]}</div>
        <h2 id="models-title">{t["models_title"]}</h2>
        <div class="models-list">{models_html}
        </div>
        <p class="note">{ICONS["info"]}<span>{t["models_note"]}</span></p>
      </div>
    </div>
  </section>

  <section id="faq" aria-labelledby="faq-title">
    <div class="wrap">
      <div class="label">{t["faq_label"]}</div>
      <h2 id="faq-title">{t["faq_title"]}</h2>
      <div class="faq-list">{faq_html}
      </div>
    </div>
  </section>

  <section class="final" aria-labelledby="final-title">
    <div class="wrap">
      <h2 id="final-title">{t["final_title"]}</h2>
      <p class="section-sub">{t["final_sub"]}</p>
      <a class="btn" href="{REF_LINK}" rel="sponsored noopener" target="_blank">{t["final_cta"]} {ICONS["arrow"]}</a>
    </div>
  </section>
</main>

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

<script defer src="{pre}assets/site.js"></script>
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
"""

def main():
    (ROOT / "assets").mkdir(parents=True, exist_ok=True)
    (ROOT / "assets" / "site.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    (ROOT / "assets" / "site.js").write_text(js_text(), encoding="utf-8")
    for lang in LANGS:
        d = LANG_DIR[lang]
        outdir = ROOT / d if d else ROOT
        outdir.mkdir(parents=True, exist_ok=True)
        (outdir / "index.html").write_text(render(lang), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(SITEMAP, encoding="utf-8")
    (ROOT / "robots.txt").write_text(ROBOTS, encoding="utf-8")
    (ROOT / "README.md").write_text(README, encoding="utf-8")
    print("Generated:", ", ".join(LANGS))

def js_text():
    return MAIN_JS.replace("__CHECK__", ICONS["check"]).replace("__COPY__", ICONS["copy"]).strip() + "\n"

if __name__ == "__main__":
    main()
