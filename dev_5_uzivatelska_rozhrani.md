# Popopoužívateľské rozhrania

> Principy návrhu a vývoje používateľského rozhrania v moderních softvérových systémech, vč. webových, mobilních. Proces vývoje používateľského rozhrania a zásady kvality. User experience (UX), interaction design, prototypovanie, wireframovanie, používateľský výzkum, testovanie použitelnosti. Technologie a nástroje. Príklady z praxe pre všetko vyššie uvedené. (PV252 || PV247 || PV278 || PV182)

1. [Principy návrhu a vývoje používateľského rozhrania v moderních softvérových systémech, vč. webových, mobilních (1/4)](#principy-návrhu-a-vývoje-používateľského-rozhrania-v-moderních-softvérových-systémech-vč-webových-mobilních-14)
2. [Proces vývoje používateľského rozhrania a zásady kvality (2/4)](#proces-vývoje-používateľského-rozhrania-a-zásady-kvality-24)
3. [User experience (UX), interaction design, prototypovanie, wireframovanie, používateľský výzkum, testovanie použitelnosti (3/4)](#user-experience-ux-interaction-design-prototypovanie-wireframovanie-používateľský-výzkum-testovanie-použitelnosti-34)
4. [Technologie a nástroje (4/4)](#technologie-a-nástroje-44)

*Fun fact: v PV247 se toho o této otázke (vyjma základu Reactu) moc nedozvíte. Ostatné predmety jsem nemel, tak jen z vlastních zkušeností.*

## Principy návrhu a vývoje používateľského rozhrania v moderních softvérových systémech, vč. webových, mobilních (1/4)

Kľúčem k úspechu UI je používateľská prívetivost a snadné použití rozhrania. Nabušený systém s tunou pokročilých funkcionalit bude k ničemu, ak se nedá jednoducho používat koncovými používateľmi. Bežní používateľé zvyčajne dokáží systémum s dobrým UI prominout i nektoré funkcionální nedostatky.

Návrh rozhrania muže ovlivňovat:

- Jedná se o interné, alebo verejný systém? (Musí s ním používateľé pracovat, alebo s ním pracují jen, keď chtejí?)
- Úroveň odbornosti používateľu
- Nutnost možnosti prispôsobení
- Nutnost vícejazyčnosti aplikace (problém mohou delat napríklad odlišné druhy písma)
- Nutnost prístupnosti (accessibility) pre popopoužívateľa s neakým omezením (zrakové alebo sluchové specifické potreby, nutnost používat pre ovládání iba myš alebo iba klávesnici)
- Platforma, na ktoré aplikace beží

UI se zvyčajne vyvíjí jako monolit, ale je možné delat i microfrontendy.

Je fajn brát v potaz

- Používateľskou prívetivost (napr. zložité formuláre je lepší rozdelit na viac částí, pole usporádat top-down namísto v tabulce)
- Bezpečnosť – u aplikací, na ktoré mohou cílit útočníci, je vhodné stránku používateľmi prispôsobit (napr. zobrazit jeho fotku), aby bolo težké stránku napodobit
- Skrývání hesel (zmena viditelnosti textu ve vstupním poli)
- Používanie vhodných vstupních polí (napr. `<input type="email">` pre e-mail, `<input type="tel">` pre telefonní číslo)
- Rozhrania by melo byť jednotné (konzistentní – jednotné barvy, fonty, styl tlačítek apod.)
- Responsivita – fungovanie aplikace na ruzne velkých obrazovkách (desktop, tablet, mobil)

### Specifika pre web

- Řešíme, kdy je stránka renderovaná:
  - Server side rendering (SSR) – stránka je plne renderovaná na serverov, vhodné pre statické aplikace
  - Client side rendering (CSR) – stránka se renderuje na strane klienta, dáta se do aplikace načítají pomocí dotazu na server

- Dríve aplikace fungovaly jako multi-page (prechod na jinou stránku znamenal kompletní nové načtení, napr. v PHP)
- Pozdeji se prešlo na single-page prístup pomocí client side renderingu
- Aktuálne je možné prístupy míchat (initial page load je SSR, následne CSR), což je vhodné pre rychlý počáteční load a SEO (napr. Next.js)

## Proces vývoje používateľského rozhrania a zásady kvality (2/4)

Začneme používateľským výzkumem, abychom pochopili skutečné požadavky na UI. Následuje návrh pomocí wireframu a prototypu, ktoré možno použiť pre zpetnou vazbu a jako predlohu pre vývoj. Na záver je duležité provést popopoužívateľské testovanie s rôznymi typy používateľu, abychom predešli problémum pri nasadenie aplikace.

### Používateľský výzkum, analýza

- Je duležité určiť, kdo sú naši používateľé, ako dosud pracují se stávajícími systémy, co jim vyhovuje a co ne.
- Je napríklad analyzovat požadavky na systém a spôsob, akým se systém používá (napr. minimalizace počtu kliknutí pre dosažení určiťé operace).
- S používateľmi možno pracovat ve **focus groups** (diskusních skupinách).
- Možno použít A/B testovanie – každé skupine používateľu prezentujeme určiťou variantu produktu a sledujeme jej dopad na chovanie.

## User experience (UX), interaction design, prototypovanie, wireframovanie, používateľský výzkum, testovanie použitelnosti (3/4)

### User experience (UX)

UX kombinuje následující aspekty:

- Vizuální estetika (pritažlivý a konzistentní design)
- Použiteľnosť (usability – rozhrania, ktoré umožňuje plnit úkoly i za určiťých obmedzenie)
- Užitnost (utility – rozhrania musí umožňovat provádet požadované úkony)
- Efektivita (efficiency – usnadňuje provádení opakujících se činností)
  - Používateľ by nemel byť nucen zadávat do systémov rovnaké informace vícekrát.
  - Pre časté akce je vhodné umožnit dobre známé klávesové zkratky (napr. Ctrl + S pre uložení).

Celkové popopoužívateľské zkušenosti rozhodují o tom, či budú používateľé produkt aktivne využívat.

### Interaction design

Snažíme se pochopit, akým spôsobem používateľé se systémem interagují, a navrhnout rozhrania tak, aby odpovídalo ich potrebám a zvyklostem. Patrí sem mapovanie používateľských toku, definícia kľúčových scénáru a optimalizácia cest (user flows).

### Wireframovanie

Wireframe je grafický skelet webu alebo aplikace, ktorý slouží jako pruvodce obsahem a koncepty stránek. Funguje podobne jako architektonický plán a pomáhá designérum a klientum diskutovat o detailech budovanie rozhrania.
**Účel:** Získanie konsenzu a zber interné zpetné väzby o tom, ako bude nová funkcionalita fungovat

**Charakteristiky:**
- Low fidelity design (nízká vernost)
- Skladá se z čar, boxu a odstínu šedi
- Nereší se zde barvy a styly, ale iba layout a struktura obsahu
- Slouží ke komunikaci informační struktury, layoutu, obsahu a funkcionality
  

### Mockupy
Mockup je statický návrh používateľského rozhrania, ktorý zobrazuje, ako bude aplikace vypadat. Obsahuje detaily jako barvy, fonty a další vizuální prvky, ale zvyčajne nie je interaktivní.

### Prototypovanie

Krok výše od wireframu s vyšší verností (higher fidelity). Pomocí návrhových nástrojov jako Adobe XD alebo Figma možno vytvorit (částečne i interaktivní) prototyp.

**Charakteristiky:**
- Zahrnuje realisticky vypadající komponenty
- Slouží pre další diskusi se stakeholdery
- Využívá se pre popopoužívateľské testovanie a získanie zpetné väzby
- Validované prototypy sú pripravené k vývoji
### Testovanie použitelnosti

Testovanie použitelnosti muže zahrnovat:

- Pozorovanie používateľu pri provádení úkonu v rámci systémov:
  - Sledujeme ich akce, reakce, potíže.
  - Na základe pozorovanie navrhujeme zlepšenie a úpravy UI.
- Evaluaci experty z oblasti prístupnosti (accessibility). Možno tiež použít automatizované nástroje jako Lighthouse.
- Sledovanie pohybu očí (eye-tracking) používateľa pri používanie produktu:
  - Zjistíme, ktoré časti rozhrania upoutají nejviac pozornosti.
  - Pre eye-tracking je zvyčajne nutný souhlas používateľa.

## Technologie a nástroje (4/4)

V súčasnosti je nejuniverzálnejším spôsobem tvorby UI HTML + CSS + JS. Aktuálne sú populární frontendové JS frameworky (React, Vue, Solid, Svelte, Angular …). Možno je použít v prohlížeči, jako desktopovou aplikaci (Electron – pribalí se k aplikaci Chromium, alebo s využitím nativního WebView, napr. Tauri), pre mobilní aplikace (Progressive Web App, nie je nutné instalovat z App Store), prípadne majú vlastné verze pre nativní mobilní zariadenie (React Native, Svelte Native …). Tyto technologie majú zvyčajne dobre rešené veci jako accessibility či lokalizaci, existují pre ne solidní komponentové knihovny.

Aktuálním trendem s interesantním potenciálem je WebAssembly, ktoré umožňuje použití kompilovaného jazyka (C/C++, Rust …). Výsledná aplikace je spustitelná v prohlížeči a zpravidla rychlejší než čistý JS. WASM podporuje dva režimy – práci s DOM, alebo Priame vykreslovanie na `<canvas>` (používá napríklad Figma).

Alternativou muže byť použití multiplatformního frameworku Flutter (používá jazyk Dart, podporuje Android, iOS, web), ktorý umožňuje vývoj pre viac platforem z jednoho kódu.

Nativními jazyky pre mobilní aplikace sú Swift (iOS) a Java/Kotlin (Android).

Pre desktopové aplikace je možné použít i technologie jako GTK (existují bindingy pre rôzne jazyky) alebo Qt (C++), JavaFX …

[Go back to the first question](1_kvalita_kodu.md)
