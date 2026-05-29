# Kvalita kódu

> Kvalita v vývoji softvérových systémov, Atributy kvality a softvérové Metriky. Taktiky na zaistenie kvality na úrovni jednotlivých atributu kvality. Princípy Clean Code a SOLID, refaktorovanie kódu. Testovanie kódu, jednotkové testy, integračné testy, popopoužívateľské a akceptačné testy. Ladenie a testovanie výkonu. Proces riadenia kvality v vývoji softvérových systémov. Príklady z praxe pre všetko vyššie uvedené. (PV260, PA017, PA103)

1. [Kvalita v vývoji softvérových systémov, Atributy kvality a softvérové Metriky (1/6)](#kvalita-ve-vývoji-softvérových-systémov-atributy-kvality-a-softvérové-Metriky-16)
2. [Taktiky na zaistenie kvality na úrovni jednotlivých atributu kvality (2/6)](#taktiky-pro-zabezpečenie-kvality-na-úrovni-jednotlivých-atributu-kvality-26)
3. [Princípy Clean Code a SOLID, refaktorovanie kódu (3/6)](#principy-clean-code-a-solid-refaktorovanie-kódu-36)
4. [Testovanie kódu, jednotkové testy, integračné testy, popopoužívateľské a akceptačné testy (4/6)](#testovanie-kódu-jednotkové-testy-integračné-testy-popopoužívateľské-a-akceptačné-testy-46)
5. [Ladenie a testovanie výkonu (5/6)](#ladení-a-testovanie-výkonu-56)
6. [Proces riadenia kvality v vývoji softvérových systémov (6/6)](#proces-rízení-kvality-ve-vývoji-softvérových-systémov-66)

## Kvalita v vývoji softvérových systémov, Atributy kvality a softvérové Metriky (1/6)

### Kvalita v vývoji softvérových systémov

- Dôležitý aspekt počas vývoja sw systémov
- Kvalita je často definovaná jako **schopnosť produktu dostát požiadaviekm** => je duležité si určiť, čo sú požiadavky
- Kvalita sa môže líšiť podľa pohľadu:
  - **popopoužívateľské pohľad** - Použiteľnosť, Spoľahlivosť, výkon, presnost, Bezpečnosť
  - **Z pohľadu vývojára** - modularita, komplexita, pochopiteľnosť, Testovateľnosť
  - **Z pohľadu manažéra (long term)** - schopnosť sw se adaptovat na zmeny, opätovná použiteľnosť, Udržateľnosť, Škálovateľnosť
  - **Požiadavky zákazníka** a.k.a. vonkajšia kvalita (Použiteľnosť, presnost/správnost, Spoľahlivosť, Bezpečnosť, výkon...)
  - Abychom dostáli temto ^, je napríklad, aby bol vývoj jednoduchý, aby se produkt dal jednoducho dlhodobo udržiavať (bol jednoduchý modifikovať/rozšíriť), a aby nebol zbytečne drahý (skrz náklady na prevádzka i cenu úprav). Toho docílíme dodržováním **interné kvality produktu** (modularita, jednoduchosť jednotek, Testovateľnosť, prispôsobiteľnosť zmenám, čitateľnosť kódu, opätovná použiteľnosť, Škálovateľnosť, prenositeľnosť, Udržateľnosť, dodržiavanie standardu...)
- Zlá vonkajšia kvalita je často symptómom zlej interné kvality produktu (opravy chýb trvají dlouho, systém je pomalý... ale nemusí to byť vždy pravda, napríklad jen máme slabší UI)

### Atributy kvality

Za nejduležitejší Atributy kvality kódu se považujú:

- **Udržateľnosť (maintainability)** = ľahkosť úprav bez technického dluhu
- **Výkonnosť** = doba odozvy systémov (a efektivita využití zdrojov)
- **Spoľahlivosť** = pravdepodobnosť bezchybného fungovania po určiťou dobu
- **Testovateľnosť** = ako ľahko (a čo všetko) možno systém testovat
- **Škálovateľnosť** = schopnosť systémov spracovať väčšie množstvo dát/používateľu...
- **Bezpečnosť** = ako je systém odolný voči útokom
- **Použiteľnosť** = ľahkosť používania systémov a jednoduchosť učenia sa práce s ním, správna funkcionalita (zvyčajne samostatný bod)

#### Udržateľnosť (maintainability)
- refaktorovanie na koherentné jednotky, aby bolo místo nutné zmeny minimálné a snadno lokalizovateľné,
- separácia dát od logiky (aby bolo možné jednotku nahradit jinou),
- decoupling (závislosťi na rozhraniach, namísto na implementacích)

#### Výkonnosť
- kešovanie
- paralelizmus
- asynchronná komunikácia/Spracovanie
- detekcia a zmiernenie bottleneckov
- používat profiler

#### Spoľahlivosť
- detekcia a náprava zdrojov nespoľahlivosti
- kontrolné mechanizmy pre zabezpečenie spolehlivosti
- vhodné spracovanie chýb
- automatické hlásenie neočakávaných chýb
- timeout po požiadavky
- monitorovanie, protokolovanie, zber udalostí
- pravidelné snímky a rollback v prípade pádu, napr. pri zlyhania odoslania formuláre presmerovaťna na predvyplnený formulár (predcházet frustráciu popoužívateľa)
- transakcie
- kontrola vstupu na každé úrovni
- odstránenie single point of failure

#### Testovateľnosť
- separácia dát a logiky
- odstránenie globálneho stavu
- clean kod, KISS, dependency separation

#### Škálovateľnosť
- refaktorovanie na jednoduchší, samostatne nasaditeľné jednotky
- extrakcia dát pre umožnenie paralelizácia jednotek
- extrakcia a samostatné nasadenie subsystému
- distribúcia a/alebo replikácia dát (db bývá bottleneck, ostatné veci možno snadneji paralelizovat)

#### Bezpečnosť
- detekcia a oprava chýb
- použití šifrovanej komunikácie

#### Použiteľnosť
- zlepšenie UX
- použití taktik pre zlepšenie výkonnosťi/škálovateľnosťi (keď je to pomalé)


### softvérové Metriky

Merateľné aspekty sw systémov (počet riadkov kódu, pokrytí testami, Cyklomatická zložitosť…), ktoré nám dávají informace o celkovém obrazu, ale muže byť netriviální je vhodne interpretovat.

Napr. 100 % pokrytí testami nemusí znamenat, že v systémov nesú chyby. Velký počet malých tríd zní dobre, ale trídy mohou byť naprosto nelogicky strukturované a vzájemne silne závislé…

Mohou byť Priame (to, co prímo zmeráme, napr. počet defektov) alebo Odvodené (vypočítané z prímých, napr. hustota defektov; počet defektov na velikost produktu).

Krome toho je užitečné rozlišit Metriky na **objektivní** a **subjektivní**:
- **Objektivní metrika**: možno ji zmerať prímo číselne nezávisle na vnímání (napr. LOC – počet riadkov kódu, počet tríd, počet funkcií, počet súborov).
- **Subjektivní metrika**: závisí na vnímání či dojmu (napr. čas, ktorý vývojár či používateľ potrebuje k porozumení nové funkcionalite, alebo „obtiažnosť" pochopení dátového modelov).

Klasifikácia metrík:

- **Procesné Metriky**: Meria samotný proces vývoja (napr. priemerný čas na opravu chyby, počet defektov nalezených pri inspekci, produktivita).
- **Produktové Metriky**: Meria vlastnosti samého softwaru (napr. Cyklomatická zložitosť, velikost, Výkonnosť, code coverage).
- **Zdrojové (Resource) Metriky**: Meria lidské alebo hardwarové zdroje (napr. úsilí v človekomesících, fluktuace týmu, vytíženost serverov).

Často nás zaujímajú spíš pomery/Odvodené Metriky, napr. pomer komentárov k celkovému počtu rádku, priemerná velikost metody, odchylky jednotlivých metrik v rámci projektu alebo medzi rôznymi releasy, hustota defektov, atd. Metriky je ale nebezpečné používat k hodnotenie výkonu vývojáre.

**Konkrétné Metriky:**
- **Lines of Code (LOC)** - muže byť hrubým odhadem úsilí, užitečné pre porovnání napríč releasy
- **(Non)Commented lines of code (CLOC)** – rádky obsahující komentár vs. bez komentáre
- **(LOC vs. CLOC)**: Nestačí jen vedet, co to je. Ráček se ptá na výhody a nevýhody. Nevýhodou je silná závislosť na použitém programovacím jazyce a stylu programátora.
- **Počet tríd**
- **Počet funkcií/metod**
- **Počet packages**
- **Počet súborov**
- **Provázanost tríd** – kolik jiných tríd trída A volá (tight coupling), trídy sú závislé, ak metoda A používá metody trídy B
- **Hloubka dedičnosti** – počet vrstev v hierarchii pod dedičností, čím hloubeji je trída ve stromu dedičnosti, tým komplexnejší nejspíše je
- **Cyklomatická komplexnosť (CC)** – počet nezávislých cest ve zkoumané jednotce (funkcia/metode), ktoré se mohou v behu programu projevit. $CC = E - N + 2P$ kde E = počet hran (vetví), N = počet vrcholu (nevetvených bloku) a P = počet vzájemne nepropojených grafu (zvyčajne P = 1 pre jednu funkci). Nejnižší hodnota CC je 1 (bez vetvení). Čím vetší komplexita, tým obtížnejší Testovateľnosť. Kód považuje za "špatný" (standardne se uvádí $CC > 10$, tehdy už je funkcia príliš složitá na pochopení a plné pokrytí testami)
- **Váhovaná komplexita trídy** - součet cyklomatických zložitosťou metod trídy
- **Reakce na dotaz** - kolik metod (cizích alebo svých tríd) bude trída A volat pri Spracovanie požiadavky
- **Nedostatek soudržnosti** - ako souvisí metody trídy s jejíma instančníma promennýma

**Datové funkcia (Ukladanie dát)**
Tohle sú entity alebo tabulky, se kterými systém pracuje.

**ILF (Internal Logical File - Interné logický soubor)**: Logická skupina dát, kterou tvuj systém udržuje a mení. Jsou to dáta, ktorá žijí prímo ve tvé aplikaci.

**Príklad:** Tabulka Zákazníci ve tvé databázi, kam tvuj systém umí pridávat, upravovat a mazat záznamy.

**EIF (External Interface File - Externé soubor rozhrania)**: Logická skupina dát, kterou tvuj systém iba čte, ale udržuje ji nejaký jiný, externé systém.

**Príklad:** Číselník PSČ alebo aktuálné kurzy men, ktoré si tvuj e-shop iba stahuje pres API z webu České národní banky, ale nemuže je upravovat.

**Transakční funkcia (Spracovanie dát)**
Tohle sú akce, ktoré používateľ (alebo jiný systém) s aplikací provádí.

**EI (External Input - Externé vstup)**: Proces, pri kterém dáta vstupují do systémov zvenčí a upravují vnitrní dáta (ILF) alebo mení chovanie systémov.

**Príklad:** odoslania formuláre pre registraci nového používateľa (vytvorí se záznam v ILF).

**EO (External Output - Externé výstup)**: Proces, pri kterém dáta vystupují ze systémov ven, pričemž systém musí provést nejaký výpočet, odvození alebo logickou operaci.

**Príklad:** Vygenerovanie mesíčního reportu tržeb (systém musí projít objednávky, sečíst částky, vypočítat dane a výsledek zobrazit).

**EQ (External Inquiry - Externé dotaz)**: Proces, pri kterém dáta vystupují ze systémov ven, ale bez jakéhokoliv výpočtu alebo zmeny dát. Jde o prosté vytažení a zobrazení dát.

**Príklad:** Zobrazení detailu profilu používateľa na základe jeho ID (systém jen vezme dáta z DB a zobrazí je, nic nepočítá).

#### **SQALE (Software Quality Assessment Based on Lifecycle Expectations)**
– metoda hodnocení technického dluhu na základe charakteristik projektu:
1. **Level 1**: základné charakteristiky (opätovná použiteľnosť, Udržateľnosť, Bezpečnosť, efektivita, Spoľahlivosť…)
2. **Level 2**: rozvetvení každé úrovne z Level 1 (napr. Udržateľnosť → čitateľnosť kódu, pochopiteľnosť, konzistencia názvu, standardy)
3. **Level 3**: navázání konkrétních požiadaviek na úrovni kódu (napr. „žádné metody delší než 30 rádku", „žádný vícenásobný dedický cyklus", „test coverage ≥ 80 %" atp.) – Výstupem je komplexné index technického dluhu, ktorý se skládá z jednotlivých sub-indexu (napr. STI – Testability, SRI – Reliability atd.).

## Taktiky na zaistenie kvality na úrovni jednotlivých atributu kvality (2/6)

Problémy s kvalitou a ich Spracovanie môžeme rozlišit na rôznych úrovních:

**Prevence:**
- Best practices pre programovanie - clean code, SOLID, Návrhové vzory, párové programovanie, konvence
- Zabezpečenie kvality procesy - V-model, TDD

**detekcia:**
- Testovanie požiadaviek (manual, automatic)
- Nefunkčné požadavky a testy (výkon - perf testing, Bezpečnosť - penetračné testing)
- Inspekce kódu, code reviews
- Statická analýza (SonarQube)

**náprava:**
- Funkčné požadavky → bug fixing
- Spoľahlivosť → fault-tolerance - mechanismy pre odolnost proti zlyhania
- Výkon → paralelizácia, využití zdrojov, odstránenie "bottleneckov"
- Bezpečnosť → odstránenie jediných bodov zlyhania, známých závislosťí s bezpečnosťními nedostatky
- Udržateľnosť → refaktorovanie, Návrhové vzory

**Trackovanie:**
- Trackovanie problému
- Verzovanie, release management
- Sledovanie technického dluhu, zastaralých komponent

**Poznámka:** Nektoré z uvedených taktik sú konfliktní - nemôžeme mať všechno (napr. lepší Bezpečnosť muže ohrozit Použiteľnosť).


## Princípy Clean Code a SOLID, refaktorovanie kódu (3/6)

### Clean Code

Čitelný, snadno pochopitelný. Kód bývá mnohem viac čten než psán, proto je duležité, aby bol srozumitelný, čas vývojáru je drahý. Kľúčové je:

- **Jasné pojmenovávanie** reflektující doménu problému, dostatečne výstižné (a ne príliš dlouhé či generické, viz Java). V ideálním prípade by melo byť sebevysvetlující a komentáre by nemely byť ponapríklad, ALE i tak sú komentáre fajn. hlavne konzistencia v codebase
  - **Trídy**: dodržovat SRP, pojmenovat podľa účelu, vyhnout se generickým pojmenováním → vede ke kompaktním specifickým trídám
  - **Metody**:
    - ak vrací bool, pojmenuj to `has*()` alebo `is*()`
    - používat slovesa, dodržet konvenci pre getters/setters, žádné side-effects
    - boolean parametry metod sú bad practice (`setAdminStatus(true/false)` → `[grant/revoke]AdminRights()`)
    - nepoužívat synonyma pre rozdílné akce (add/append → jaký je rozdíl? nikdo neví)
    - krátké názvy public metod, dlouhé private
  - **Promenné**: velký scope → dlouhé jméno, malý scope → krátké
  - struktury sú podstatná jména, metody začínají slovesem (alebo se jedná o getter v rustu)
  - verejné API (public) jednotky by melo byť jasné a jednoduché, interne (private) se mohou používat delší názvy metod, keď je vďaka tomu jasnejší, k čemu slouží
- **Rozumná velikost jednotek** - ideálne krátké funkcia, jednoduché trídy... single responsibility principle. Obsah jednotky by mel reflektovat jej název
- **Užívání standardu** jazyka/technologie
- dodržovat best practices jazyka/technologie

Dále se rídí principy:

#### Don't repeat yourself (DRY) princip

Každá informace by mela byť v systémov jednoznačne definovaná na jediném míste. Platí na vše, co muže byť v systémov duplikováno (ale i v procesech, napríklad opakované manuální spouštení testu => automatizovat)

- Napr. dokumentaci generujeme ze zdrojáku, abychom nemeli viac sources of truth
- Napr. definujeme schéma (prisma), ze kterého vygenerujeme ako SQL tabulky, tak struktury pre náš jazyk
- Napr. vytáhneme sdílenou funkcionalitu do vlastné funkcia

#### Keep it simple stupid (KISS) princip

- jednoduchosť pred výkonem
- Nejlépe fungují systémy, ktoré sú co nejjednodušší
- Nie je dôvod používat zložité techniky na jednoduché problémy

#### You Ain't Gonna Need It (YAGNI)

- Nezabýváme se tvorbou nečeho, co nebudeme potrebovat (napr. nedeláme prílišné abstrakce pre podporu možné budúcí funkcionality, ak to nie je nutné)
- Je lepší vec udelat jednoducho a pak ji snadno upravit, než ji udelat univerzálne, abychom pak zjistili, že nás nenapadl nejaký edge case a musíme to stejne celé prepsat. Vývoj postupuje po malých kručcích.

### SOLID

#### Single responsibility
- každá trída by mela mať iba jednu zodpovednost, a.k.a. pre každou trídu by mel byť iba jeden dôvod, proč by se mela zmenit (napr. FileReader by se mel starat iba o čítanie ze súborov, ne o spracovávanie čtených dát. Iba zmena spôsobu čítanie ze súborov muže zapríčinit, že musíme menit FileReader) => nižší provázanost (závislosťi) tríd, vyšší koheze (zamerenost na jednu vec)

#### Open/closed principle
- Otevreno pre rozšírení, uzavreno pre modifikaci, preferujeme pridávanie nové funkcionality pred zmenou zdrojového kódu/binárky toho, co už máme => menší šance, že neco rozbijeme, na nových trídách nic nezávisí
- používá se implementácia rozhrania/abstraktní trídy
- dodržiavanie OCP spôsobuje vyšší komplexitu, takže je ponapríklad ho používat obezretne a jen tam, kde se často mení/pridává funkcionalita

#### Liskov substitution principle
- instance tríd by mely byť nahraditelné ich podtrídami, aniž by došlo k narušení chovanie systémov - všechny podtrídy by mely dodržovat kontrakty nadtríd a nemely by odstraňovat chovanie nadtríd
- potomci nesmejí:
  - "odstraňovat" alebo omezovat chovanie ich rodiču
  - porušovat základné invarianty trídy - nemenné vlastnosti
  - požadovat volání specifických funkcií pre zjištení, či se jedná o potomka alebo rodiče
  - porušovat jakékoliv predem stanovené kontrakty ich rodičovskou trídou
- problém je, keď musíme explicitne overovat, o jaký podtyp se jedná (`if instanceOf - then` → maintenance nightmare) - toto by mel rešit polymorfismus
- nedodržení lsp -> narušení polymorfysmu
- držet se robustness principu pre typesafe variance:
  - _"be conservative in what you do, be liberal in what you accept from others"_
  - contravariantni parametry metod u podtrid: musi prijmat typ, ktere bere nadtrida alebo obecnejší
  - covariantni navratove typy metod u podtrid: musi vracet typ, ktery vraci nadtrida alebo konkrétnejší
  - nevyhazovat zadne nove vyjimky v podtridach, ktere nesú v nadtride
  - detailnejší video k ty contra/covariance a LSP [here](https://www.youtube.com/watch?v=7hXi0N1oWFU)

#### Interface segregation principle
- klienti kódu by nemeli byť závislí na metodách, ktoré nepoužívají, a.k.a. delej malá a jednoduchá rozhrania namísto velkých
- rozhrania trídy by melo mať jen ty metody, ktoré jej klienti nejspíš budú používat v jednotných kontextech
- psát malé a soudržné rozhrania
- nedodržení → klienti používají jen zlomek trídy, pri rozšírení/dedení musí implementovat spoustu "zbytočných" metod
- napr. chci v rustu prevést strukturu na string. Jediné co proto musím udelat je zajistit implementaci Display traitu (a ničeho jiného).

#### Dependency inversion
- moduly by mely záviset na abstrakcích (rozhrania), ne na konkrétních implementacích
- snižuje se tým provázanost modulu, je možné poskytnout vlastné implementaci či mockovat
- konstruktor by mel prijímat vše, na čem struktura závisí, ne si vytváret zdroje sám (napr. repo si nemá tvorit pripojení do Databázy, ale má byť predáno v konstruktoru) = dependency injection konstruktorem

### refaktorovanie

Úprava modulu takovým spôsobem, aby se nezmenilo jeho externé chovanie, ale iba došlo ke zlepšenie jeho interné struktury/modifikovatelnosti...

- Pred refaktoringem je duležité mať chovanie solidne pokryto testy, abychom nespôsobili nechtenou zmenu
- Behem refaktoringu nedeláme nic jiného (žádná nová funkcionalita)
- **Kdy refaktorovat?** Keď nevyvíjím → oddelit refactoring od developmentu, součást rutiny pri TDD, pri oprave bugu, po zavedené nové funkcionality, dlouhodobé plánované refaktorovanie
- **GRASP** - General Responsibility Assignment Software Principles → principy pre lepší design OOP kódu
- Techniky (nektoré editory je podporují, což usnadňuje práci a je pravdepodobne spolehlivejší):
  - **extrakcia funkcia** - kus kódu funguje jako jednotka/potreboval by komentár => vytáhni ho do funkcia, dej tomu priléhající jméno, bude možné to použít na viac místech
  - **Inline funkcia** - opak výše, vhodné pre triviální situace jako `isMoreThanFiveEven(x)`
  - **Nahrazení mnoha parametru funkcia strukturou** - fajn, keď funkcia používá ranec promenných => stanou se fieldy struktury
  - **Move method/field** - z jedné do jiné struktury, ak to dává smysl (napríklad doménove)
  - **extrakcia/inline trídy** - z trídy obsahující množinu polí, ktorá sú related, vytáhneme nový objekt, ktorý bude puvodné trída obsahovat/alebo naopak pre inline
  - **Early return** - obecne chceme, aby funkcia popisovala správný/bezchybný tok programu. Ak pri Spracovanie funkcia objevíme chybu ve vstupních datech, hodíme tam return. V takých prípadech nepoužíváme `if-else`, ale `if return`
  - **Rename** cokoliv
  - **Seskupení mnoha parametru do struktury**
  - **Udelat final parametry metod**
  - **Dlouhá složitá metoda** → vlastné objekt (trída)
  - **odstránenie prostredníka**
  - **Odstranit magické čísla**
  - **Zapouzdrení vlastností**
  - **Guard clauses** → redukovat nesting

Kód, ktorý se dobre čte a udržuje nemusí byť ten nejrychlejší/nejefektivnejší (abstrakce mohou neco stát). zvyčajne nám mírné snížení výkonu za vyšší čitateľnosť nevadí, ale nemusí to byť vždy pravda.

## Testovanie kódu, jednotkové testy, integračné testy, popopoužívateľské a akceptačné testy (4/6)

= proces evaluace, či systém splňuje specifikované požadavky (IEEE: "Testing is the process of exercising or evaluating a system or system component by manual or automated means to verify that it satisfies specified requirements.")

**Terminologie:**
- **defekt (defect)** - nedokonalost alebo porucha sw, kvuli ktoré produkt nesplňuje požadavky  
  _Príklad: Funkcia vrací špatný výsledek kvuli chybe v algoritmu._
- **Error** - lidská chyba produkující nesprávný výsledek  
  _Príklad: Vývojár omylem použije špatný operátor ve výrazu._
- **zlyhania (failure)** - náhlá neschopnosť produktu provádet požadovanou funkci  
  _Príklad: Aplikace spadne pri pokusu uložit dáta._
- **Chyba (fault)** - projev erroru v software  
  _Príklad: Nesprávne inicializovaná promenná spôsobí nesprávné chovanie._
- **Bug** - synonymum pre defekt  
  _Príklad: Tlačítko v UI nefunguje popodľa očekávanie._

**Principy testovanie:**
- **Sensitivita** - testy musí odhalit chybu/nedostatek vždy
- **Zvolit spolehlivá kritéria** - fail fast
- **Machine independent** - nezávislé na prostredia
- **Redundance** - jasne stanovit zámer
- **Obmedzenie (restriction)** - usnadnení problému
- **Rozdel a panuj** - zložité testovacie problémy jdou usnadnit rozdelením prostoru vstupu
- **Viditelnost** - schopnosť neco zmerať, abychom neco testovali, musíme vedet, ako to má ideálne dopadnout
- **Zpetná väzba** - ladení procesu vývoje, poučit se z chýb

- V praxi je testovanie z pravidla nekompletní. Testovaniem odhalujeme chyby, ale nedokazujeme bezchybnost.
- Každý test by mel testovat iba jednu vec/vlastnost/feature, ideálné je spousta malých testu, vďaka čemuž môžeme snadno identifikovat zdroj problému.
- Ideálne by mel testovanie provádet nekdo jiný, než autor testovaného kódu
- **Prioritizace testovanie na základe rizik** - nemôžeme otestovat všechno, prioritizace testovanie rizikových funkcionalit (risk = dopad + pravdepodobnosť)
- Ak narazíme na chybu, pre kterou nebol test, je duležitá nejen oprava, ale i pridání (ideálne automatizovaného) testu, aby se chyba už nemohla opakovat

### Typy testovanie popodľa prístupu

- **Whitebox (strukturální)** - vidíme zdrojový kód a môžeme vstupy testu cílit na spouštení kritických míst (off-by-one error, zero division...)
  - napr. unit, integration, performance tests
- **Blackbox (funkcionální)** - nevidíme čo sa deje uvnitr systémov, iba sledujeme vstupy a výstupy
  - napr. acceptance tests, system tests

### Obecné typy testovanie

- **Regresné testovanie** - sledujeme, či zmeny v systémov neprinesly pády (automatizovaných) testu
- **Smoke testy** - sledujeme, či vybrané kritické funkcia fungují v novém prostredia. Ak ne, nemá vubec cenu nasazovat a testovat další veci
- **Sanity testy** - jako smoke, ale spouští se pre overenie nápravy chýb/pridání funkcionality
- **A/B testovanie** - používáme dve varianty a sledujeme, ktorá je úspešnejší (zvyčajne pri testovanie UI)
- :haha: v praxi nekterí experti praktikují melounové testovanie pre zvýšení test coverage, zvenku zelené, uvnitr červené :haha:

- Kvalita testu možno overit **mutačním testovaniem**: do aplikace zavedeme defekty (mutací zdrojového kódu, napr. negací operátoru, off-by-one, vynechání volání) a sledujeme, kolik jich bolo odhaleno testy. Ak neco prošlo, muže ísť o kandidáta na další testy. Predpoklad je, že testy, ktoré najdou mutanty, najdou i opravdové chyby. Mscore = Mkilled / (Mtotal - Meq), kde Meq sú ekvivalentní mutanti (mutace oproti puvodnímu programu nespôsobí chybu).
- Nektoré situace sú pre náš produkt rizikovejší (možno odhadnout pri analýze), než ostatné - na ty bychom se meli zamerit pri testovanie
- Vstupy testu vhodne rozdelujeme na kategorie (napr. <0, 0, >0), z každé vybereme pár reprezentantu (abychom nemuseli testovat úplne každou hodnotu)

Testovanie si môžeme usnadnit tým, že v systémov modelujeme nevalidní stavy jako nereprezentovatelné (rust enum <3, builder pattern, stavový automat...)

### pokrytí testami

Mužeme sledovať ruzná kritéria, pokrytí znamená, že danou cestou kódu prošel aspoň jeden test, metrika je zvyčajne v procentech:

- **Line/statement coverage** - pokryté rádky/výrazy
- **Function coverage** - pokryté funkcia/metody, jde o to, či bola aspoň jednou zavolána
- **Branch coverage** - pokryté logické vetve programu
- **Condition coverage** - každá boolean podmínka bola vyhodnocena jako true i false

Mnohdy nie je 100% pokrytí možné (ak napríklad nekde neco redundantne testujeme, better be safe than sorry) a zároveň 100% pokrytí neznamená bezchybnost.

Nektoré časti kódu je mnohem težší pokrýt, než jiné.

Môže pomoct hledat časti kódu, ktoré sú neotestované, ale o kvalite testu se toho moc nedozvíme.

### Jednotkové (unit) testy

Validace, že se izolovaná jednotka kódu (funkcia/trída) chová tak, ako bychom očekávali:

- White box
- Testy sú automatizované, rychlé, jednoduché, čitelné, deterministické, každý testuje jednu jedinou vec
- Izolujeme jednotku od zbytku systémov pomocí *test doubles*, nafejkovaných závislosťí:
  - **dummy objekt** - nikdy se nepoužije, ale je ponapríklad napríklad jako parametr
  - **fake objekt** - jen pre účely testu, jednoduchý, ale v praxi nepoužitelný (napr. in-memory db)
  - **stub** - vrací vždy stejnou vec (stubborn, tvrdohlave vraci vzdy stejnou hodnotu)
  - **spy** - je schopen si zapamatovat, ako a s čím bol volán (napr. volala se metoda odoslania mailu s tímto obsahem)
  - **mock** - predprogramovaný objekt (keď te nekdo zavolá s parametrem A, udeláš toto, jinak neco jiného)
- **AAA** - arrange (príprava), act (prevedenie testovaného chovanie), assert (overenie) - tri fázy každého testu, act by mel byť co nejkratší
- Napr. cargo test, jest, junit
- Pokročilejší techniky zahrnující analýzu zdrojového kódu a následné vygenerovanie vstupních hodnot (symbolic execution), prípadne formální verifikace využívající matematických dukazu, model checking...

### integračné testy

- Sledují, či spolu jednotky interagují tak, ako bychom očekávali
- Pomalejší, vetší a složitejší, než unit testy
- Black/white box
- Pre testovanie UI použijeme *Playwright* (drív se používalo *Selenium*)

### Systémové testy

- Overenie, že systém splňuje specifikované požadavky
- Testují Použiteľnosť, kapacitu, výkon, splnení funkcionality, Bezpečnosť...
- Benchmarking, penetračné testovanie, popopoužívateľské testy...
- Možno automatizovat pomocí programem ovládaným prohlížečem (Playwright, dríve Selenium, Puppeteer)
- Black box

### akceptačné testy

- Overenie, že systém splňuje business požadavky a je pripraven k vydání
- Môže byť ve forme odškrtávanie políček s požadavky na systém, ktoré zákazník predem určil
- Provádeny se zákazníkem
- Black box

### Test-driven development (TDD)

Skladá se z trí fáz, red, green, blue, ktoré iterativne aplikujeme. V každé časti se snažíme docílit iba jedné veci (a ničeho jiného, holt počkáme do další fázy):

- **Red/test** - vytvoríme failující test pre co nejmenší část funkcionality, kterou chceme implementovat
- **Green/write** - implementujeme funkcionalitu co nejjednoduchoji tak, aby test prošel (a zároveň nerozbil jiný test)
- **Blue/refactor** - upravíme implementaci tak, aby odpovídala standardum, aby bol kód hezký...

### Behaviour-driven development (BDD)

- Se zákazníkem sepíšeme chovanie systémov jako jednotlivé scénáre
- Scénáre slouží vývojárum i testerum jako jednotky
- Napr. gherkin, cucumber - konstrukty given, when a then (jako AAA) se používají pre definici scénáru v english-like jazyce srozumitelném zákazníkovi, tyto scénáre se pak objevují i v testech

## Ladenie a testovanie výkonu (5/6)

Cieľom je identifikace a riešenie prípadných problému týkajících se rychlosti, odezvy a propustnosti systémov, nalezení hranic. Dynamické testovanie sw za cieľom zjištení, ako sa chová pod záteží, jaké operace trvají nejdéle, ako by je šlo optimalizovat, co bere nejviac výpočetního výkonu atp.

**Performance testing zahrnuje:**

### Load testing
- zátežové testy, sledujeme ako systém zvládá dlouhodobejší zátež
- ako sa bude systém chovat s predpokládaným počtem dotazu/používateľu behem určiťého časového úseku
- verifikuje schopnosť systémov zvládat očekávanou zátež

### Stress testing
- sledujeme, ako sa systém vyporádává s krátkodobými výkyvy v záteži (keď najednou prijde spousta požiadaviek)
- jaký je horní limit systémov, kolik toho zvládne, než začne odmaťat požadavky atp, pomocí postupného zvyšovanie záteže až po zlyhania
- hledáme potentiální ddos, security issues, korupci dát
- ako rychle se zvládne systém vrátit do normálu, identifikace bottleneckov v hw
- **Spike testing** - testovanie rychlého krátkého nárustu na limitní kapacitu

### Soak/endurance testing
- narustající počet používateľu a požiadaviek v prubehu dlouhého časového úseku
- nejčasteji má za cieľ odhalit memory leaks atp

### testing škálovateľnosťi
- sledovanie narustajícího využití resources s narustajícím počtem požiadaviek
- meli bychom pozorovat +- prímou úmeru

Bežící systém je tiež vhodné dlouhodobe monitorovat, abychom odhalili další slabá místa.

Výkon možno obecne zvýšit za cenu dalších atributu (napríklad maintainability), proto je nutné volit správný kompromis pre náš prípad.

**Nástroje:** jProfiler, jMeter, Gatling, Siege, LoadRunner, BlazeMeter

## Proces riadenia kvality v vývoji softvérových systémov (6/6)

**Software Quality Management (SQM)** je kolekce všech procesu, ktoré zajišťují, že implementácia produktu, služby a životního cyklu splňuje standardy kvality organizace a ostatních zúčastnených stran.

**Ruzné pohledy na kvalitu:**
- **Kvalita použití** - user experience
- **vonkajšia kvalita** - projde to všemi testy a požadavky
- **Interné kvalita** - kvalita návrhu, udržovatelnost atp
- **Procesní kvalita** - je počas vývoja správne postupováno?

**Proces riadenie SQM zahrnuje:** procesy a ich vlastníky, požadavky na procesy, Metriky procesu, výstupy procesu a zpetná väzba.

Skladá se z:

### Definícia požiadaviek na sw kvalitu a plánovanie (SQP)
- špecifikácia funkčnéch i nefunkčnéch požiadaviek, stanovení hodnotících kritérií, rizik, určenie metrik, podrobný popis a rozvržení aktivit k zabezpečenie kvality
- použití standardu, požadavky kvality, odhady a plánovanie aktivit, požadavky, scope, zdroje, risky, časový plán

### Zabezpečenie (assurance) sw kvality (SQA)
- definícia a kontrola procesu, ktoré povedou k zabezpečenie sw kvality a prevenci defektov (mimo jiné nastavení CI/CD)
- zajišťuje adekvátnost a prukaznost procesu, IEEE standardy

### Kontrola sw kvality (SQC)
- kontrola, či produkt/jeho časti splňují požadavky (včetne požiadaviek na kvalitu) a ich vývoj se rídí definovanými procesy, monitoring či se držíme procesu a vytyčených cílu
- procházení artefaktu procesu a kontrola, že odpovídají standardu v nejruznejších rovinách (design, požadavky, obmedzenie, ...), monitorovanie, plan-do-check-act

### Zlepšenie kvality (SPI)
- snaha zlepšit procesy, abychom docílili zlepšenie kvality
- zpetná väzba, zlepšenie procesu a tým i dalších výstupu, zlepšit efektivitu, efektivnost, praktiky

## Notes

### Capability Maturity Model
Definuje úrovne vyspelosti organizace v kontextu zabezpečenie kvality:

- **Level 1 Výchozí (ad hoc)** - chaos, nepredvídatelná cena, plán
- **Level 2 Opakovatelný (doing agile)** - intuitivní, cena a kvalita sú promenlivé, plán je pod vedomou kontrolou, neformální metody & procedury
- **Level 3 Definovaný (being agile)** - orientace na kvalitu, spolehlivé ceny a plány, stále nepredvídatelný výkon systémov kvality
- **Level 4 Řízený (thinking agile)** - meranie, promyšlená a statisticky rízená kvalita produktu
- **Level 5 Optimalizující (agile culture)** - automatizace a zlepšenie výrobního procesu, prevence chýb, inovace technologie

**Další modely:**
- **SPICE** (Software Process Improvement and Capability Determination) - 5 kategorií, 24 procesu, 201 praktik
- **CMMI** - pokročilejší model
- **Six Sigma** - dáta based, eliminace defektov (definuj, mer, analyzuj, zlepši, kontroluj)

### Prevence problému kvality

- Následovanie best practices a konvencí, obecných (SOLID, clean code) i pre danou technologii/jazyk (eslint, cargo fmt)
- Využití principu návrhových vzoru
- Techniky jako TDD, párové programovanie, code reviews
- Použití procesních standardu (ITIL), agilních technik (scrum, kanban)
- Automatizované testovanie, CI
- Komunikácia, jednotný jazyk
- Fail-fast prístup - snažíme se detekovat problém ve vstupech, namísto abychom klidne akceptovali cokoliv a pak se divili pri neočekávaném chovanie
- Design by contract - naše metody (zvlášť pri tvorbe) mohou vyžadovat splnení určiťého kontraktu (možno vynutit asserty), aby mohly poskytnout garance o výstupech. Je možné použít podmínenou kompilaci a mať kontrakty napríklad jen ve vývojovém prostredia (tým se ale môžeme pripravit o presné určenie místa problému na produkci)

Nefunkčné problémy kvality se reší architektúrou. Pre prevenci techto problému je možné vytvorit model systémov a na nem si simulačne overovat požadavky (napr. schopnosť obsloužit určiťý počet požiadaviek za určiťý čas) a prípadne odvodit nároky na jednotlivé komponenty (napríklad maximálné dobu Spracovanie požiadaviek v daném komponentu).

Pre overenie kvality je tiež možné použít formální verifikaci (používá se napríklad pre dokazovanie správnosti algoritmu).

### detekcia problému kvality

- **Code reviews** (vzájemné medzi vývojári), **inspections** (formální, je fajn použít formulár; ukazuje to prípravu, na nic se nezapomene a zároveň se odfiltrují zbytečnosti, nelpíme na stylu, rešíme správnost, dodržiavanie standardu...)
- **(Automatizované) testovanie** (rust\cargo test)
- **Statická analýza** (rust\cargo clippy, borrow checker, sonarqube) - nespouštíme kód

### Špatný kód

- Pomíchané úrovne abstrakce
- Nízká koheze (megatrídy, dlouhé funkcia...)
- Kruhové závislosťi (je pak závislosť na implementaci, blbe se sleduje flow a vztahy, blbe se to testuje, udržuje a škáluje)
- Duplikace kódu
- Spousta parametru
- Blbé názvy
- Delání vecí príliš "chytre", keď to nie je nutné
- Nedodržovanie standardu/vhodných konstruktu jazyka
- Magické konstanty

#### Code smells a riešenie

!Jednotlivé taktiky mohou byť vzájemne v rozporu, je ponapríklad si určiť, čeho chceme docílit! (napr. Udržateľnosť vs výkon)

##### Udržateľnosť
- príliš brzké optimalizácia => nejdrív profiluj, pak prípadne optimalizuj
- prílišná flexibilita => snaž se o jednoduchosť, pak prípadne rozširuj
- snaha o moc chytré riešenie => stavební základy by mely byť co nejjednodušší
- nepoužívání standardu, principu návrhových vzoru
- nízká modularizace

##### Výkonnosť
- redundantní práce => kešovanie, memoizace, bottom-up approach dynamického programovanie
- sekvenční Spracovanie/hľadanie => binární hľadanie, chytrejší algoritmy, práce sa sarazenými kolekcemi, paralelizácia go brrrrrr
- dlouhé kritické sekce (ve vícevláknových programech) => minimalizujeme kritickou sekci, muže byť lepší použít viac zámku
- aktivní čekání => async Spracovanie, necháme se notifikovat až operace skončí...

##### Spoľahlivosť
- nevalidujeme vstupní dáta, slepá duvera
- špatný error/exception handling
- nepredpokládáme, že by funkcia mohl nekdo zavolat v jiném poradie
- prílišný hypetrain, používáme technologie, kterým úplne nerozumíme
- absence protokolovanie => loguj, je fajn vedet, čo sa v systémov delo pred pádem
- jednoduchý pád celého systémov kvuli jedné časti => nasaď viac služeb, implementuj restart/recover, automatické prepnutí se na jinou, funkčné službu

##### Testovateľnosť
- globálné stav, promenné
- schovávanie závislosťí; je lepší provést dependency injection, než sázet na predchozí volání `init()` funkcia pracující s globálním stavem
- komunikácia medzi jednotkami, ktoré by nemely komunikovat => SOLID
- nutnost hacky solutions, abychom vubec mohli testovat => SOLID
- nedeterminismus (závislosť na čase, náhodnosti, globálním stavu, databázi... napr. bacha na iteraci pres rust std::collections::HashMap, elementy sú náhodne serazené)
- neoddelujeme inicializační a aplikačné logiku

##### Škálovateľnosť
- monolitická aplikace, distribúcia muže zvýšit výkon/kapacitu, ale bacha na nutný režijní overhead, težší testovanie, nasazovanie, Bezpečnosť...

### Sledovanie problému kvality

- Issue tracking
- Správa technického dluhu (tracking, vyhrazení času na jeho nápravu)

[Go to the next question](./2_softwarove_inzenyrstvi.md)
