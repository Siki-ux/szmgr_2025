# Kvalita kódu

> Kvalita pri vývoji softvérových systémov, atribúty kvality a softvérové metriky. Taktiky na zabezpečenie kvality na úrovni jednotlivých atribútov kvality. Princípy Clean Code a SOLID, refaktorovanie kódu. Testovanie kódu, jednotkové testy, integračné testy, popoužívateľské a akceptačné testy. Ladenie a testovanie výkonu. Proces riadenia kvality pri vývoji softvérových systémov. Príklady z praxe pre všetko vyššie uvedené. (PV260, PA017, PA103)

1. [Kvalita pri vývoji softvérových systémov, atribúty kvality a softvérové metriky (1/6)](#kvalita-pri-vývoji-softvérových-systémov-atribúty-kvality-a-softvérové-metriky-16)
2. [Taktiky na zabezpečenie kvality na úrovni jednotlivých atribútov kvality (2/6)](#taktiky-na-zabezpečenie-kvality-na-úrovni-jednotlivých-atribútov-kvality-26)
3. [Princípy Clean Code a SOLID, refaktorovanie kódu (3/6)](#princípy-clean-code-a-solid-refaktorovanie-kódu-36)
4. [Testovanie kódu, jednotkové testy, integračné testy, popoužívateľské a akceptačné testy (4/6)](#testovanie-kódu-jednotkové-testy-integračné-testy-popoužívateľské-a-akceptačné-testy-46)
5. [Ladenie a testovanie výkonu (5/6)](#ladenie-a-testovanie-výkonu-56)
6. [Proces riadenia kvality pri vývoji softvérových systémov (6/6)](#proces-riadenia-kvality-pri-vývoji-softvérových-systémov-66)

## Kvalita pri vývoji softvérových systémov, atribúty kvality a softvérové metriky (1/6)

### Kvalita pri vývoji softvérových systémov

- Dôležitý aspekt pri vývoji SW systémov
- Kvalita je často definovaná ako **schopnosť produktu naplniť požiadavky** => je dôležité si určiť, čo sú požiadavky
- Kvalita sa môže líšiť podľa hľadiska:
  - **Popoužívateľské hľadisko** - použiteľnosť, spoľahlivosť, výkon, presnosť, bezpečnosť
  - **Z pohľadu vývojára** - modularita, zložitosť, zrozumiteľnosť, testovateľnosť
  - **Z pohľadu manažéra (dlhodobý)** - schopnosť SW sa prispôsobiť zmenám, znovupoužiteľnosť, udržiavateľnosť, škálovateľnosť
  - **Požiadavky zákazníka** a.k.a. externá kvalita (použiteľnosť, presnosť/správnosť, spoľahlivosť, bezpečnosť, výkon...)
  - Aby sme dosiahli tieto ^, je potrebné, aby sa vývoj vykonával ľahko, aby sa produkt dal jednoducho dlhodobo udržiavať (bolo jednoduché modifikovať/rozšíriť), a aby nebol zbytočne drahý (skrz náklady na prevádzku aj cenu úprav). To dosiahneme dodržiavaním **internej kvality produktu** (modularita, jednoduchosť jednotiek, testovateľnosť, prispôsobiteľnosť zmenám, čitateľnosť kódu, znovupoužiteľnosť, škálovateľnosť, prenositeľnosť, udržiavateľnosť, dodržiavanie noriem...)
- Zlá externá kvalita je často symptómom zlej internej kvality produktu (opravy chýb trvajú dlho, systém je pomalý... ale nemusí to byť vždy pravda, napríklad len máme slabší UI)

### Atribúty kvality

Za najdôležitejšie atribúty kvality kódu sa považujú:

- **Udržiavateľnosť (maintainability)** = jednoduchosť úprav bez technického dlhu
- **Výkonnosť** = čas reakcie systémov (a efektivita využitia zdrojov)
- **Spoľahlivosť** = pravdepodobnosť bezchybného fungovania po určitú dobu
- **Testovateľnosť** = ako ľahko (a čo všetko) možno systém testovať
- **Škálovateľnosť** = schopnosť systémov spracovať väčšie množstvo údajov/popoužívateľov...
- **Bezpečnosť** = ako je systém odolný voči útokom
- **Použiteľnosť** = jednoduchosť používania systémov a jednoduchosť učenia sa práce s ním, správna funkcionalita (zvyčajne samostatný bod)

#### Udržiavateľnosť (maintainability)
- refaktorovanie na koherentné jednotky, aby bolo miesto potrebnej zmeny minimálne a ľahko lokalizovateľné,
- separácia údajov od logiky (aby bolo možné jednotku nahradiť inou),
- decoupling (závislosti na rozhraniach, namiesto na implementáciách)

#### Výkonnosť
- ukladanie do vyrovnávacej pamäte
- paralelizmus
- asynchrónna komunikácia/spracovanie
- detekcia a zmierňovanie úzkych miest
- používať profiler

#### Spoľahlivosť
- detekcia a náprava zdrojov nespoľahlivosti
- kontrolné mechanizmy na zabezpečenie spoľahlivosti
- vhodné spracovanie chýb
- automatické hlásenie neočakávaných chýb
- timeout po požiadavke
- monitorovanie, registrovanie, zbierka udalostí
- pravidelné snímky a rollback v prípade pádu, napríklad pri zlyhání odoslania formulára presmerovať na vopred vyplnený formulár (predchádzať frustrácii popoužívateľa)
- transakcie
- kontrola vstupov na každej úrovni
- odstránenie jediného bodov zlyhania

#### Testovateľnosť
- separácia údajov a logiky
- odstránenie globálneho stavu
- čistý kód, KISS, separácia závislostí

#### Škálovateľnosť
- refaktorovanie na jednoduchšie, nezávisle nasadzované jednotky
- extrakcia údajov na umožnenie paralelizácie jednotiek
- extrakcia a nezávislé nasadenie podsystému
- distribúcia a/alebo replikácia údajov (DB bývá úzke miesto, ostatné veci sa dajú ľahšie paralelizovať)

#### Bezpečnosť
- detekcia a oprava chýb
- použitie šifrovanej komunikácie

#### Použiteľnosť
- zlepšenie UX
- použitie taktík na zlepšenie výkonnosti/škálovateľnosti (keď je to pomalé)


### Softvérové metriky

Merateľné aspekty SW systémov (počet riadkov kódu, pokrytie testami, cyklomatická zložitosť…), ktoré nám dávajú informácie o celkovom obraze, ale môže byť netriviálne ich vhodne interpretovať.

Napríklad 100 % pokrytie testami nemusí znamenať, že v systéme nie sú chyby. Veľký počet malých tried znie dobre, ale triedy môžu byť úplne nelogicky štruktúrované a navzájom silne závislé…

Môžu byť priame (to, čo priamo zmeráme, napríklad počet defektov) alebo odvodené (vypočítané z priamych, napríklad hustota defektov; počet defektov na veľkosť produktu).

Okrem toho je užitočné rozlišovať metriky na **objektívne** a **subjektívne**:
- **Objektívna metrika**: možno ju zmerať priamo číselne nezávisle na vnímání (napríklad LOC – počet riadkov kódu, počet tried, počet funkcií, počet súborov).
- **Subjektívna metrika**: závisí na vnímání či dojme (napríklad čas, ktorý vývojár či používateľ potrebuje na porozumenie novej funkčnosti, alebo „obtiažnosť" porozumenia dátovému modelov).

Klasifikácia metrik:

- **Procesné metriky**: Merajú samotný proces vývoja (napríklad priemerný čas na opravu chyby, počet defektov nájdených pri inšpekcii, produktivita).
- **Produktové metriky**: Merajú vlastnosti samotného softwaru (napríklad cyklomatická zložitosť, veľkosť, výkonnosť, code coverage).
- **Zdrojové (Resource) metriky**: Merajú ľudské alebo hardvérové zdroje (napríklad úsilie v člověkoměsícoch, fluktuácia tímu, vytíženosť servera).

Často nás zaujímajú skôr pomery/odvodené metriky, napríklad pomer komentárov k celkovému počtu riadkov, priemerná veľkosť metódy, odchylky jednotlivých metrik v rámci projektu alebo medzi rôznymi vydaniami, hustota defektov, atď. Metriky sú ale nebezpečné na používanie pri hodnotení výkonu vývojára.

**Konkrétne metriky:**
- **Počet riadkov kódu (LOC)** - môže byť hrubým odhadom úsilia, užitočné na porovnanie medzi vydaniami
- **(Neko)mentované riadky kódu (CLOC)** – riadky obsahujúce komentár vs. bez komentára
- **(LOC vs. CLOC)**: Nestačí len vedieť, čo to je. Ráček sa pýta na výhody a nevýhody. Nevýhodou je silná závislosť od použitého programovacieho jazyka a štýlu programátora.
- **Počet tried**
- **Počet funkcií/metód**
- **Počet balíkov**
- **Počet súborov**
- **Prepojenie tried** – koľko iných tried trieda A volá (tesná väzba), triedy sú závislé, ak metóda A používa metódy triedy B
- **Hĺbka dedičnosti** – počet vrstiev v hierarchii pod dedičnosťou, čím hlbšie je trieda v strome dedičnosti, tým zložitejšia pravdepodobne je
- **Cyklomatická komplexnosť (CC)** – počet nezávislých ciest v skúmanej jednotke (funkcii/metóde), ktoré sa môžu v behu programu prejať. $CC = E - N + 2P$ kde E = počet hrán (vetví), N = počet vrcholov (nevetviť blokov) a P = počet vzájomne neprepojených grafov (zvyčajne P = 1 pre jednu funkciu). Najnižšia hodnota CC je 1 (bez vetvenia). Čím väčšia zložitosť, tým ťažšia testovateľnosť. Kód sa považuje za „zlý" (štandardne sa uvádza $CC > 10$, vtedy už je funkcia príliš zložitá na porozumenie a úplné pokrytie testami)
- **Vážená komplexnosť triedy** - súčet cyklomatických zložitostí metód triedy
- **Reakcia na dotaz** - koľko metód (cudzích alebo svojich tried) bude trieda A volať pri spracovaní požiadavky
- **Nedostatok súdržnosti** - ako súvisia metódy triedy s ho instance premennými

#### **Dátové funkcie (Ukladanie údajov)**
Tohto sú entity alebo tabuľky, s ktorými systém pracuje.

**ILF (Internal Logical File - Interný logický súbor)**: Logická skupina údajov, ktorú tvoj systém udržuje a mení. Sú to údaje, ktoré žijú priamo vo tvojej aplikácii.

**Príklad:** Tabuľka Zákazníci vo tvojej databáze, do ktorej tvoj systém vie pridávať, upravovať a mazať záznamy.

**EIF (External Interface File - Externý súbor rozhrania)**: Logická skupina údajov, ktorú tvoj systém iba čita, ale udržuje ju nejaký iný, externý systém.

**Príklad:** Číselník PSČ alebo aktuálne kurzy mien, ktoré si tvoj e-shop iba sťahuje cez API z webu Slovenskej národnej banky, ale nemôže ich upravovať.

#### **Transakčné funkcie (Spracovanie údajov)**
Tohto sú akcie, ktoré používateľ (alebo iný systém) s aplikáciou vykonáva.

**EI (External Input - Externý vstup)**: Proces, pri ktorom údaje vstupujú do systémov zvonka a upravujú vnútorné údaje (ILF) alebo menia správanie systémov.

**Príklad:** Odoslanie formulára na registráciu nového popoužívateľa (vytvorí sa záznam v ILF).

**EO (External Output - Externý výstup)**: Proces, pri ktorom údaje vystupujú zo systémov von, pričom systém musí vykonať nejaký výpočet, odvodzovanie alebo logickú operáciu.

**Príklad:** Vygenerovanie mesačnej správy o tržbách (systém musí prejsť objednávky, sčítať sumy, vypočítať dane a zobraziť výsledok).

**EQ (External Inquiry - Externý dopyt)**: Proces, pri ktorom údaje vystupujú zo systémov von, ale bez akéhokoľvek výpočtu alebo zmeny údajov. Ide o prosté vytaženie a zobrazenie údajov.

**Príklad:** Zobrazenie detailov profilu popoužívateľa na základe jeho ID (systém len vezme údaje z DB a zobrazí ich, nič nepočítá).

#### **SQALE (Software Quality Assessment Based on Lifecycle Expectations)**
– metóda hodnotenia technického dlhu na základe charakteristík projektu:
1. **Úroveň 1**: základné charakteristiky (znovupoužiteľnosť, udržiavateľnosť, bezpečnosť, efektivita, spoľahlivosť…)
2. **Úroveň 2**: rozvetvenie každej úrovne z Úrovne 1 (napríklad udržiavateľnosť → čitateľnosť kódu, pochopiteľnosť, konzistentnosť názvov, normy)
3. **Úroveň 3**: naviazanie konkrétnych požiadaviek na úrovni kódu (napríklad „žiadne metódy dlhšie ako 30 riadkov", „žiadny viacnásobný dedičný cyklus", „test coverage ≥ 80 %" atď.) – Výstupom je komplexný index technického dlhu, ktorý sa skladá z jednotlivých sub-indexov (napríklad STI – Testability, SRI – Reliability atď.).

## Taktiky na zabezpečenie kvality na úrovni jednotlivých atribútov kvality (2/6)

Problémy s kvalitou a ich spracovanie môžeme rozlišovať na rôznych úrovniach:

**Prevencia:**
- Osvedčené postupy pri programovaní - čistý kód, SOLID, návrhové vzory, párové programovanie, konvencie
- Zabezpečenie kvality procesy - V-model, TDD

**Detekcia:**
- Testovanie požiadaviek (manuálne, automatizované)
- Nefunkčné požiadavky a testy (výkon - perf testing, bezpečnosť - penetračné testovanie)
- Inšpekcia kódu, code reviews
- Statická analýza (SonarQube)

**Náprava:**
- Funkčné požiadavky → oprava chýb
- Spoľahlivosť → odolnosť voči chybám - mechanizmy na odolnosť voči zlyhaniam
- Výkon → paralelizácia, využitie zdrojov, odstránenie „úzkych miest"
- Bezpečnosť → odstránenie jediných bodov zlyhania, známych závislostí s bezpečnostnými nedostatkami
- Udržiavateľnosť → refaktorovanie, návrhové vzory

**Sledovanie:**
- Sledovanie problémov
- Verzovanie, správa vydaní
- Sledovanie technického dlhu, zastaranych komponent

**Poznámka:** Niektoré z uvedených taktík sú konfliktné - nemôžeme mať všetko (napríklad lepšia bezpečnosť môže ohroziť použiteľnosť).


## Princípy Clean Code a SOLID, refaktorovanie kódu (3/6)

### Clean Code

Čitateľný, ľahko zrozumiteľný. Kód bývá oveľa viac čítaný ako písaný, preto je dôležité, aby bol zrozumiteľný, čas vývojárov je drahý. Kľúčové je:

- **Jasné pomenovania** odrážajúce doménu problému, dostatočne výstižné (a nie príliš dlhé či generické, pozri Java). V ideálnom prípade by malo byť sebaopisujúce a komentáre by nemali byť potrebné, ALE aj tak sú komentáre v poriadku. hlavne konzistentnosť v codebase
  - **Triedy**: dodržiavať SRP, pomenovať podľa účelu, vyhnúť sa generickým pomenovaniam → vedie k kompaktným špecifickým triedám
  - **Metódy**:
    - ak vracajú bool, pomenovajú `has*()` alebo `is*()`
    - používať slovesá, dodržiavať konvenciu pre getters/setters, žiadne vedľajšie účinky
    - boolovské parametre metód sú zlá prax (`setAdminStatus(true/false)` → `[grant/revoke]AdminRights()`)
    - nepoužívať synonymá pre rozdielne akcie (add/append → aký je rozdiel? nikto nevie)
    - krátke názvy public metód, dlhé private
  - **Premenné**: veľký rozsah → dlhý názov, malý rozsah → krátky
  - štruktúry sú podstatné mená, metódy začínajú slovesom (alebo ide o getter v ruste)
  - verejné API (public) jednotky by malo byť jasné a jednoduché, interne (private) sa môžu používať dlhšie názvy metód, keď je vďaka tomu jasnější, na čo slúžia
- **Rozumná veľkosť jednotiek** - ideálne krátke funkcie, jednoduché triedy... princíp jedinej zodpovednosti. Obsah jednotky by mal odrážať ho názov
- **Používanie noriem** jazyka/technológie
- dodržiavať osvedčené postupy jazyka/technológie

Ďalej sa riadi princípmi:

#### Princíp Neopakovateľnosti (Don't repeat yourself - DRY)

Každá informácia by mala byť v systéme jednoznačne definovaná na jedinommieste. Platí na všetko, čo môže byť v systéme duplikované (ale aj v procesoch, napríklad opakované manuálne spúšťanie testov => automatizovať)

- Napríklad dokumentáciu generujeme zo zdrojáka, aby sme nemali viac zdrojov pravdy
- Napríklad definujeme schéma (prisma), z ktorej vygenerujeme ako SQL tabuľky, tak štruktúry pre náš jazyk
- Napríklad vytiahneme zdieľanú funkcionalitu do vlastnej funkcie

#### Princíp Jednoduchosti (Keep it simple stupid - KISS)

- Jednoduchosť pred výkonom
- Najlepšie fungovacie systémy sú tie, ktoré sú čo najjednoduchšie
- Nie je dôvod používať zložité techniky na jednoduché problémy

#### Princíp Nebudúcej Potreby (You Ain't Gonna Need It - YAGNI)

- Nezabýváme sa tvorbou niečoho, čo nebudeme potrebovať (napríklad nerobíme príliš abstrakcie na podporu možnej budúcej funkčnosti, ak to nie je potrebné)
- Je lepšie urobiť vec jednoducho a potom ju ľahko upraviť, ako ju urobiť univerzálne, aby sme potom objavili, že nás napadol nejaký edge case a musíme to všetko prepísať. Vývoj prebieha po malých krokoch.

### SOLID

#### Princíp Jedinej Zodpovednosti
- každá trieda by mala mať len jednu zodpovednosť, a.k.a. pre každú triedu by mal byť len jeden dôvod, prečo by sa mala zmeniť (napríklad FileReader by sa mal starať len o čítanie zo súboru, nie o spracovávanie čítaných údajov. Len zmena spôsobu čítania zo súboru môže zapríčiniť, že musíme zmeniť FileReader) => nižšia prepojovateľnosť (závislosti) tried, vyššia kohézia (zameranosť na jednu vec)

#### Princíp Otvorenú/Uzavriatosti
- Otvorené na rozšírenie, zatvorené na zmenu, preferujeme pridávanie novej funkčnosti pred zmenou zdrojového kódu/binárky toho, čo už máme => menšia šanca, že niečo zrobíme, na nových triedach nič nevisí
- používa sa implementácia rozhrania/abstraktnej triedy
- dodržiavanie OCP spôsobuje vyššiu zložitosť, takže je potrebné ho používať obozretne a len tam, kde sa často mení/pridáva funkcionalita

#### Princíp Liskovovej Substitúcie
- inštancie tried by mali byť nahraditeľné ich podtriedami, bez narušenia správania systémov - všetky podtriedy by mali dodržiavať zmluvy nadtried a nemali by odstraňovať správanie nadtried
- potomkovia nesmú:
  - „odstraňovať" alebo obmedziť správanie ich rodičov
  - porušovať základné invarianty triedy - nemeniteľné vlastnosti
  - vyžadovať volanie špecifických funkcií na zistenie, či-li ide o potomka alebo rodiča
  - porušovať akékoľvek vopred stanovené zmluvy ich rodičovskou triedou
- problém je, keď musíme explicitne overovať, o aký podtyp ide (`if instanceOf - then` → maintenance nightmare) - toto by mal riešiť polymorfizmus
- nedodržanie lsp -> narušenie polymorfizmu
- držať sa princípu robustnosti pre typesafe variance:
  - _"buď konzervatívny v tom, čo robíš, buď liberálny v tom, čo akceptuješ od ostatných"_
  - contravariantni parametre metód u podtried: musia prijať typ, ktorý berie nadtrida alebo všeobecnejší
  - covariantni navrátené typy metód u podtried: musia vracať typ, ktorý vracajú nadtrida alebo konkrétnejší
  - nevyhadzovať žiadne nové výnimky v podtriedach, ktoré nie sú v nadtride
  - podrobnejšie video k ty contra/covariance a LSP [tu](https://www.youtube.com/watch?v=7hXi0N1oWFU)

#### Princíp Segregácie Rozhrania
- klienti kódu by nemali byť závislí od metód, ktoré nepoužívajú, a.k.a. robiť malé a jednoduché rozhrania namiesto veľkých
- rozhranie triedy by malo mať len tie metódy, ktoré ho klienti pravdepodobne budú používať v jednotných kontextoch
- pisať malé a súdržné rozhrania
- nedodržanie → klienti používajú len zlomok triedy, pri rozšírení/dedičnosti musia implementovať spúšť „zbytočných" metód
- napríklad v ruste chcem previesť štruktúru na string. Jediné, čo preto musím urobiť, je zabezpečiť implementáciu Display traitu (a nič iného).

#### Princíp Inverzie Závislostí
- moduly by mali závisieť od abstraktnej (rozhrania), nie na konkrétnych implementáciách
- znižuje sa tým prepojovateľnosť modulov, je možné poskytnúť vlastnú implementáciu či mockuvať
- konštruktor by mal prijímať všetko, na čom štruktúra závisí, nie si vytvoriť zdroje sám (napríklad repo si nemá vytvoriť pripojenie do databázy, ale má byť predané v konštruktore) = injektáž závislostí konštruktorom

### Refaktorovanie

Úprava modulu takovým spôsobom, aby sa nezmenilo jeho externe správanie, ale len došlo k zlepšeniu jeho vnútornej štruktúry/modifikovateľnosti...

- Pred refaktoringom je dôležité mať správanie solídne pokryté testami, aby sme nespôsobili nechcenú zmenu
- Počas refaktoringu nerobíme nič iného (žiadna nová funkcionalita)
- **Kedy refaktorovať?** Keď nevyvíjam → oddeliť refactoring od developmentu, súčasť rutiny pri TDD, pri oprave chyby, po zavedení novej funkčnosti, dlhodobé plánované refaktorovanie
- **GRASP** - General Responsibility Assignment Software Principles → princípy na lepší dizajn OOP kódu
- Techniky (niektoré editory ich podporujú, čo zjednodušuje prácu a je pravdepodobne spoľahlivejšie):
  - **Extrakcia funkcie** - kus kódu funguje ako jednotka/potreboval by komentár => vytiahneme ho do funkcie, dáme mu priliehajúci názov, bude možné to použiť na viac miestach
  - **Inline funkcia** - opak vyššie, vhodné pre triviálne situácie ako `isMoreThanFiveEven(x)`
  - **Nahradenie mnohých parametrov funkcie štruktúrou** - fajn, keď funkcia používa ranec premenných => stanú sa fieldami štruktúry
  - **Presunúť metódu/pole** - z jednej do inej štruktúry, ak to dáva zmysel (napríklad doménovo)
  - **Extrakcia/inline triedy** - z triedy obsahujúcej množinu polí, ktoré sú súvisejúce, vytiahneme nový objekt, ktorý bude pôvodná trieda obsahovať/alebo naopak pre inline
  - **Skoré vrátenie** - všeobecne chceme, aby funkcia opisovala správny/bezchybný tok programu. Ak pri spracovaní funkcie objavíme chybu v vstupných údajoch, hodíme tam return. V takých prípadoch nepoužívame `if-else`, ale `if return`
  - **Premenovanie** čokoliv
  - **Zoskupenie mnohých parametrov do štruktúry**
  - **Urobiť finálne parametre metód**
  - **Dlhá zložitá metóda** → vlastný objekt (trieda)
  - **Odstránenie sprostredkovateľa**
  - **Odstránenie magických čísiel**
  - **Zapuzdrenie vlastností**
  - **Guard clauses** → znížiť vnorenie

Kód, ktorý sa dobre čita a udržiava nemusí byť ten najrýchlejší/najefektívnejší (abstrakcie môžu niečo stáť). Zvyčajne nám mierny pokles výkonu za vyššiu čitateľnosť nevadí, ale nemusí to byť vždy pravda.

## Testovanie kódu, jednotkové testy, integračné testy, popoužívateľské a akceptačné testy (4/6)

= proces hodnotenia, či systém spĺňa špecifikované požiadavky (IEEE: "Testing is the process of exercising or evaluating a system or system component by manual or automated means to verify that it satisfies specified requirements.")

**Terminológia:**
- **Defekt (defect)** - nedokonalosť alebo porucha SW, kvôli ktorej produkt nespĺňa požiadavky  
  _Príklad: Funkcia vracia zlý výsledok kvôli chybe v algoritme._
- **Chyba** - ľudská chyba produkujúca nesprávny výsledok  
  _Príklad: Vývojár omylom použije zlý operátor vo výraze._
- **Zlyhanie (failure)** - náhlá neschopnosť produktu vykonávať požadovanú funkciu  
  _Príklad: Aplikácia padá pri pokuse uložiť údaje._
- **Chyba (fault)** - prejav chyby v software  
  _Príklad: Nesprávne inicializovaná premenná spôsobí nesprávne správanie._
- **Chyba (bug)** - synonymum pre defekt  
  _Príklad: Tlačítko v UI nefunguje podľa očakávania._

**Princípy testovania:**
- **Citlivosť** - testy musia odhaliť chybu/nedostatok vždy
- **Zvoliť spoľahlivé kritéria** - zlyhať rýchlo
- **Machine independent** - nezávislé na prostredia
- **Redundancia** - jasne stanoviť zámer
- **Ohraničenie (restriction)** - zjednodušenie problému
- **Rozdeľ a panuj** - zložité testovacie problémy sa dajú zjednodušiť rozdelením priestoru vstupov
- **Viditeľnosť** - schopnosť niečo zmerať, aby sme niečo testovali, musíme vedieť, ako má ideálne dopadnúť
- **Spätná väzba** - ladenie procesu vývoja, poučiť sa z chýb

- V praxi je testovanie z pravidla nekompletné. Testovaním odhaľujeme chyby, ale nedokazujeme bezchybnosť.
- Každý test by mal testovať len jednu vec/vlastnosť/feature, ideálne je množstvo malých testov, vďaka čomu môžeme ľahko identifikovať zdroj problému.
- Ideálne by testovanie mal vykonávať niekto iný, ako autor testovaného kódu
- **Prioritizácia testovania na základe rizík** - nemôžeme otestovať všetko, prioritizácia testovania rizikových funkcionalít (riziko = dopad + pravdepodobnosť)
- Ak narazíme na chybu, pre ktorú nebol test, je dôležitá nielen oprava, ale aj pridanie (ideálne automatizovaného) testu, aby sa chyba už nemohla opakovať

### Typy testovania podľa prístupu

- **Whitebox (štruktúrne)** - vidíme zdrojový kód a môžeme vstupy testov cieliť na spúšťanie kritických miest (off-by-one error, zero division...)
  - napríklad unit, integration, performance tests
- **Blackbox (funkčné)** - nevidíme čo sa deje vnútri systémov, len sledujeme vstupy a výstupy
  - napríklad acceptance tests, system tests

### Všeobecné typy testovania

- **Regresné testovanie** - sledujeme, či zmeny v systéme nepriniesli pády (automatizovaných) testov
- **Smoke testy** - sledujeme, či vybraté kritické funkcie fungujú v novom prostredia. Ak nie, nemá vôbec zmysel nasadzovať a testovať ďalšie veci
- **Sanity testy** - ako smoke, ale spúšťa sa na overenie nápravy chýb/pridania funkčnosti
- **A/B testovanie** - používame dve varianty a sledujeme, ktorá je úspešnejšia (zvyčajne pri testovaní UI)
- :haha: v praxi niektorí experti praktizujú melónové testovanie na zvýšenie test coverage, zvonka zelené, vnútri červené :haha:

- Kvalita testov možno overiť **mutačným testovaním**: do aplikácie zavedieme defekty (mutáciou zdrojového kódu, napríklad negáciou operátora, off-by-one, vynechaním volania) a sledujeme, koľko ich bolo odhalených testami. Ak niečo prešlo, môže ísť o kandidáta na ďalšie testy. Predpoklad je, že testy, ktoré nájdu mutantov, nájdu aj opravdové chyby. Mscore = Mkilled / (Mtotal - Meq), kde Meq sú ekvivalentní mutanti (mutácia voči pôvodnému programu nespôsobí chybu).
- Niektoré situácie sú pre náš produkt riskantnejšie (možno odhadnúť pri analýze), ako ostatné - na tie by sme sa mali zamerať pri testovaní
- Vstupy testov vhodne rozdelujeme na kategórie (napríklad <0, 0, >0), z každej vyberieme pár zástupcov (aby sme nemuseli testovať úplne každú hodnotu)

Testovanie si môžeme zjednodušiť tým, že v systéme modelujeme nevalidné stavy ako nepredstaviteľné (rust enum <3, builder pattern, stavový automat...)

### Pokrytie testami

Môžeme sledovať rôzne kritéria, pokrytie znamená, že danou cestou kódu prešiel aspoň jeden test, metrika je zvyčajne v percentách:

- **Line/statement coverage** - pokryté riadky/výrazy
- **Function coverage** - pokryté funkcie/metódy, ide o to, či bola aspoň raz zavolána
- **Branch coverage** - pokryté logické vetvy programu
- **Condition coverage** - každá boolovská podmienka bola vyhodnotená ako true aj false

Mnohokrát nie je 100% pokrytie možné (ak napríklad niekde niečo redundantne testujeme, lepšie byť bezpečný ako ospravedlňovaný) a zároveň 100% pokrytie neznamenajú bezchybnosť.

Niektoré časti kódu sú oveľa ťažšie pokryť, ako iné.

Môže pomôcť hľadať časti kódu, ktoré sú netestované, ale o kvalite testov sa toho moc nedozviemeúme.

### Jednotkové (unit) testy

Validácia, že sa izolovaná jednotka kódu (funkcia/trieda) správa tak, ako by sme čakali:

- White box
- Testy sú automatizované, rýchle, jednoduché, čitateľné, deterministické, každý testuje jednu jedinou vec
- Izolujeme jednotku od zvyšku systémov pomocou *test doubles*, nafakovaných závislostí:
  - **dummy objekt** - nikdy sa nepoužije, ale je potrebný napríklad ako parameter
  - **fake objekt** - len na účely testov, jednoduchý, ale v praxi nepoužiteľný (napríklad in-memory db)
  - **stub** - vždy vracia rovnakú vec (stubborn, tvrdohlavo vracia vždy rovnakú hodnotu)
  - **spy** - je schopný si zapamätať, ako a s čím bol volaný (napríklad bola volaná metóda odoslania mailu s týmto obsahom)
  - **mock** - vopred naprogramovaný objekt (keď ťa niekto zavolá s parametrom A, urobíš toto, inak niečo iné)
- **AAA** - arrange (príprava), act (vykonanie testovaného správania), assert (overenie) - tri fázy každého testu, act by mal byť čo najkratší
- Napríklad cargo test, jest, junit
- Pokročilejšie techniky zahŕňajúce analýzu zdrojového kódu a následné vygenerovanie vstupných hodnôt (symbolic execution), prípadne formálna verifikácia využívajúca matematických dôkazov, model checking...

### Integrační testy

- Sledujú, či jednotky spolu interagujú tak, ako by sme čakali
- Pomalšie, väčšie a zložitejšie, ako unit testy
- Black/white box
- Na testovanie UI použijeme *Playwright* (predtým sa používal *Selenium*)

### Systémové testy

- Overenie, že systém spĺňa špecifikované požiadavky
- Testujú použiteľnosť, kapacitu, výkon, splnenie funkčnosti, bezpečnosť...
- Benchmarking, penetračné testovanie, popoužívateľské testy...
- Možno automatizovať pomocou programom ovládaného prehliadača (Playwright, predtým Selenium, Puppeteer)
- Black box

### Akceptačné testy

- Overenie, že systém spĺňa obchodné požiadavky a je pripravený na vydanie
- Môže byť vo forme zaškrtávania políčok s požiadavkami na systém, ktoré zákazník vopred určil
- Vykonávajú sa so zákazníkom
- Black box

### Test-driven development (TDD)

Skladá sa z troch fáz, red, green, blue, ktoré iteratívne aplikujeme. V každej časti sa snažíme dosiahnuť len jednej veci (a nič iného, proste počkáme do ďalšej fázy):

- **Red/test** - vytvoríme zlyhávajúci test na čo najmenšiu časť funkčnosti, ktorú chceme implementovať
- **Green/write** - implementujeme funkcionalitu čo najjednoducho tak, aby test prešiel (a zároveň nerozbil iný test)
- **Blue/refactor** - upravíme implementáciu tak, aby zodpovedala štandardom, aby bol kód pekný...

### Behaviour-driven development (BDD)

- So zákazníkom sepíšeme správanie systémov ako jednotlivé scenáre
- Scenáre slúžia vývojárom aj testerom ako jednotky
- Napríklad gherkin, cucumber - konštrukty given, when a then (ako AAA) sa používajú na definíciu scenárov v anglicko-podobnom jazyku zrozumiteľnom zákazníkovi, tieto scenáre sa potom objavujú aj v testoch

## Ladenie a testovanie výkonu (5/6)

Cieľom je identifikácia a riešenie prípadných problémov týkajúcich sa rýchlosti, odozvy a priepustnosti systémov, nájdenie hraníc. Dynamické testovanie SW s cieľom zistenia, ako sa správa pod záťažou, ktoré operácie trvajú najdlhšie, ako by sa dali optimalizovať, čo berie najviac výpočtového výkonu atď.

**Performance testing zahrnuje:**

### Load testing
- záťažové testy, sledujeme ako systém zvláda dlhodobejšiu záťaž
- ako sa bude systém správať s predpokladaným počtom dopytov/popoužívateľov počas určitého časového úseku
- verifikuje schopnosť systémov zvládať očakávanú záťaž

### Stress testing
- sledujeme, ako sa systém vysporiadava s krátkodobými výkyvmi v záťaži (keď najednou príde množstvo požiadaviek)
- aký je horný limit systémov, koľko toho zvládne, kým nezačne odmieta požiadavky atď, pomocou postupného zvyšovania záťaže až po zlyhanie
- hľadáme potenciálne ddos, bezpečnostné problémy, poškodenie údajov
- ako rýchlo sa zvládne systém vrátiť do normálu, identifikácia úzkych miest v HW
- **Spike testing** - testovanie rýchleho krátkodobého nárastu na hraničnú kapacitu

### Soak/endurance testing
- rastúci počet popoužívateľov a požiadaviek počas dlhého časového úseku
- najčastejšie má cieľ odhaliť memory leaky atď

### testovanie škálovateľnosti
- sledovanie rastúceho využitia zdrojov s rastúcim počtom požiadaviek
- mali by sme pozorovať +- priamú úmeru

Bežiaci systém je tiež vhodné dlhodobo monitorovať, aby sme odhalili ďalšie slabé miesta.

Výkon sa možno všeobecne zvýšiť za cenu ďalších atribútov (napríklad maintainability), preto je potrebné zvoliť správny kompromis pre náš prípad.

**Nástroje:** jProfiler, jMeter, Gatling, Siege, LoadRunner, BlazeMeter

## Proces riadenia kvality pri vývoji softvérových systémov (6/6)

**Software Quality Management (SQM)** je kolekcia všetkých procesov, ktoré zabezpečujú, že implementácia produktov, služby a životného cyklu spĺňajú normy kvality organizácie a ostatných zainteresovaných strán.

**Rôzne pohlady na kvalitu:**
- **Kvalita používania** - user experience
- **Externá kvalita** - prejde to všetkými testami a požiadavkami
- **Interná kvalita** - kvalita dizajnu, udržiavateľnosť atď
- **Procesná kvalita** - je pri vývoji správne postupované?

**Proces riadenia SQM zahrnuje:** procesy a ich vlastníci, požiadavky na procesy, metriky procesov, výstupy procesov a spätná väzba.

Skladá sa z:

### Definícia požiadaviek na SW kvalitu a plánovanie (SQP)
- špecifikácia funkčných i nefunkčných požiadaviek, stanovenie hodnotiacich kritérií, rizík, určenie metrik, podrobný popis a rozvrh aktivít na zabezpečenie kvality
- použitie noriem, požiadavky kvality, odhady a plánovanie aktivít, požiadavky, rozsah, zdroje, riziká, časový plán

### Zabezpečenie (assurance) SW kvality (SQA)
- definícia a kontrola procesov, ktoré povedú k zabezpečeniu SW kvality a prevencii defektov (mimo iného nastavenie CI/CD)
- zabezpečuje adekvátnosť a průkaznosť procesov, IEEE normy

### Kontrola SW kvality (SQC)
- kontrola, či produkt/jeho časti spĺňajú požiadavky (vrátane požiadaviek na kvalitu) a ich vývoj sa riadi definovanými procesmi, monitorovanie či sa držíme procesov a vytyčených cieľov
- prechádzanie artefaktov procesov a kontrola, že zodpovedajú norme v najrôznejších rovinách (dizajn, požiadavky, ohraničenia, ...), monitorovanie, plan-do-check-act

### Zlepšenie kvality (SPI)
- snaha zlepšiť procesy, aby sme dosiahli zlepšenie kvality
- spätná väzba, zlepšenie procesov a tým aj ďalších výstupov, zlepšenie efektivnosti, efektívnosti, praktík

## Poznámky

### Capability Maturity Model
Definuje úrovne vyspelosti organizácie v kontexte zabezpečenia kvality:

- **Úroveň 1 Základná (ad hoc)** - chaos, nepredvídateľná cena, plán
- **Úroveň 2 Opakovateľná (doing agile)** - intuitívna, cena a kvalita sú premenlivé, plán je pod vedomeľou kontrolou, neformálne metódy & procedúry
- **Úroveň 3 Definovaná (being agile)** - orientácia na kvalitu, spoľahlivé ceny a plány, stále nepredvídateľný výkon systémov kvality
- **Úroveň 4 Riadená (thinking agile)** - meranie, premyslené a štatisticky riadená kvalita produktu
- **Úroveň 5 Optimalizujúca (agile culture)** - automatizácia a zlepšenie výrobného procesu, prevencia chýb, inováciaechnológie

**Ďalšie modely:**
- **SPICE** (Software Process Improvement and Capability Determination) - 5 kategórií, 24 procesov, 201 praktík
- **CMMI** - pokročilejší model
- **Six Sigma** - dátami založená, eliminácia defektov (definuj, meraj, analyzuj, zlepši, kontroluj)

### Prevencia problémov kvality

- Nasledovanie osvedčených postupov a konvencií, všeobecných (SOLID, clean code) aj pre danú technológiu/jazyk (eslint, cargo fmt)
- Využitie princípov návrhových vzorov
- Techniky ako TDD, párové programovanie, code reviews
- Použitie procesných noriem (ITIL), agilných techník (scrum, kanban)
- Automatizované testovanie, CI
- Komunikácia, jednotný jazyk
- Fail-fast prístup - snažíme sa odhaliť problém vo vstupoch, namiesto aby sme pokojne akceptovali čokoľvek a potom sa divili pri neočakávanom správaní
- Design by contract - naše metódy (zvlášť pri tvorbe) môžu vyžadovať splnenie určitej zmluvy (možno vynútiť asserty), aby mohli poskytnúť záruky o výstupoch. Je možné použiť podmienenú kompiláciu a mať zmluvy napríklad len vo vývojovom prostredia (tým sa ale môžeme pripraviť o presné určenie miesta problému na produkcii)

Nefunkčné problémy kvality sa riešia architektúrou. Na prevencuetiacho problémov je možné vytvoriť model systémov a na ňom si simulačne overiť požiadavky (napríklad schopnosť obsluhovať určitý počet požiadaviek za určitý čas) a prípadne odvodiť nároky na jednotlivé komponenty (napríklad maximálny čas spracovania požiadavky v danej komponente).

Na overenie kvality je tiež možné použiť formálnu verifikáciu (používa sa napríklad na dokazovanie správnosti algoritmov).

### Detekcia problémov kvality

- **Code reviews** (vzájomné medzi vývojármi), **inspections** (formálne, je fajn použiť formulár; ukazuje to prípravu, na nič sa nezabudne a zároveň sa odfiltujú zbytočnosti, nelpíme na štýle, riešíme správnosť, dodržiavanie noriem...)
- **(Automatizované) testovanie** (rust\cargo test)
