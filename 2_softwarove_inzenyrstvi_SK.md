# Softvérové inžinierstvo

> Životný cyklus SW, proces vývoja a riadenia softvérového vývoja. Metodika (Rational) Unified Process (UP, RUP), agilné metodiky a princípy agilného vývoja SW. Nasadenie a prevádzka softvérových systémov. Údržba softvérových systémov, znovupoužiteľnosť. Príklady z praxe pre všetko vyššie uvedené. (PA017)

1. [Životný cyklus SW, proces vývoja a riadenia softvérového vývoja (1/5)](#životný-cyklus-sw-proces-vývoja-a-riadenia-softvérového-vývoja-15)
2. [Metodika (Rational) Unified Process (UP, RUP) (2/5)](#metodika-rational-unified-process-up-rup-25)
3. [Agilné metodiky a princípy agilného vývoja SW (3/5)](#agilné-metodiky-a-princípy-agilného-vývoja-sw-35)
4. [Nasadenie a prevádzka softvérových systémov (4/5)](#nasadenie-a-prevádzka-softvérových-systémov-45)
5. [Údržba softvérových systémov, znovupoužiteľnosť (5/5)](#údržba-softvérových-systémov-znovu-použiteľnosť-55)

## Životný cyklus SW, proces vývoja a riadenia softvérového vývoja (1/5)

Vždy neakým spôsobom obsahuje fázy analýza, dizajn, implementácia, testovanie a prevádzka (vrátane nasadenia). Rozdiely sú v tom, či a akým spôsobom delíme projekt na lepšie zvládnuteľné časti. Dôsledkom toho sú aj rôzne spôsoby, ako sa vývoj riadi.

Existuje niekoľko základných modelov:

### Vodopádový model

Skladá sa z:
- **Analýza**
    - zbieranie požiadaviek od klienta
    - Je dôležité rozlišovať medzi tým, čo hovorí že potrebuje, a čo skutočne potrebuje. Pre lepšiu predstavu môžeme sledovať, ako koncový používateľ pracuje s aktuálnym riešením.
    - zaujíma nás **čo** a **prečo**, často ale klient zmieňuje **ako**. V takých prípadoch je dôležité sa pýtať **prečo**. Môže ísť o legitímny dôvod, ale tiež napríklad o nevedomosť. => štúdia uskutočňovateľnosti, dokument požiadaviek...
- **Dizajn**
    - dizajn architektúry, jednotiek, výber technológií, plán testovania => diagramy (uml), wireframy, prototypy
- **Implementácia**
    - tvorba systémov podľa dizajnu
- **Testovanie**
- **Prevádzka**

tj. najprv sesbírame všetky požiadavky, potom SW ako celok postupne navrhujeme, implementujeme, testujeme a nasadzujeme

**Výhody:**
- ľahký na riadenie
- ak všetko ide hladko, je to najlacnejší spôsob

**Nevýhody:**
- väčšinou všetko nejde hladko
- zle sa reaguje na zmeny (musíme sa vrátiť do predchádzajúcich fáz modelov)
- zákazník vopred nevie presne a úplne definovať, čo potrebuje
- v praxi nie sú kroky v tomto poradie dodržiavané (testovať chceme ideálne pri vývoji, niečo chceme ukázať netrpezlivému zákazníkovi...)

### Inkrementálny model

- Projekt sa rozdelí na inkremnety, časti, ktoré budú vyvinuté a dodané postupne, pre každý si urobíme jednoduchú rámcovú analýzu
- Inkremnety sa vyvinú v poradie podľa priority
- Po nasadení do systémov máme o inkremente od zákazníka spätnú väzbu

**Výhody:**
- Systém je dodávaný po častiach, celkové náklady sú distribuované
- Nie je potrebné vytvoriť veľký tým, pretože práca je dodávaná po častiach
- Používateľ vidí systém v raných fázach projektu. Je možné rýchlo reagovať na spätnú väzbu popoužívateľa
- O potrebe zmeny sa dozvieme skôr a ho zavedenie bude lacnejšie (nie je potrebné všetko prekopávať, pridáme zmenu inkrementálne)

**Nevýhody:**
- Náklady na vývoj sú vysoké kvôli dodávke systémov po častiach
- Model vyžaduje náročné plánovanie na distribúciu práce
- Na pripojenie modulov vyvinutých v každej fázy je nevyhnutné detailne opísať rozhrania

### Špirála

![](img/20230607122950.png)

- kombinácia iterácií a vodopádu, dôraz na analýzu rizík
- vývoj prebieha v cykloch, každý má niekoľko fáz

**Fázy:**
- **Analýza**
- **Dizajn**
- **Implementácia**
- **Testovanie, spätná väzba a plán ďalšieho cyklu** - spätnú väzbu používame na prácu v ďalšom cykle

- oproti inkrementálnemu modelov nemusíme mať po každej iterácii hotovú časť nasadeného systémov (inkrementálne je napríklad vo forme jasných požiadaviek, dizajnu systémov, alebo tak).
- cykly aplikujeme aj na jednotlivé fázy vodopádu
- lepšie pracujeme s neistotou, ale trvá to dlhšie

### Prototypovanie

- vytvoríme prototyp systémov, aby sme porozumeli, akým spôsobom chce zákazník systém používať a čo od neho očakáva
- po analýze prototypu ho zahodíme a začneme prácu na reálnom systéme, používame vhodný model

### Výskumný model

- navrhni systém a implementuj ho. Vyhovuje? Super. Nevyhovuje? Späť na dizajn/implementáciu
- nemožno ho poriadne riadiť, neexistuje dokumentácia, riešitelia sú ťažko nahraditeľní, ide o experimentovanie

### V-model

![](img/vmodel.png)

- akoby vodopád, ale zobrazuje aj rôzne testy k fázam (jednotkové, integračné, systémové, popoužívateľské, akceptačné...)

1. Požiadavky / Use Casy $\rightarrow$ Validujú sa pomocou Akceptačných testov (overenie sa zákazníkom, či systém robí to, čo mal).
2. Analýza systémov / Architektúra $\rightarrow$ Verifikuje sa pomocou Systémových testov (testuje sa systém ako celok, vrátane nefunkčných požiadaviek ako výkon či bezpečnosť).
3. Detailný dizajn (komponenty a podsystémy) $\rightarrow$ Overuje sa pomocou Integračných testov (či komponenty cez definované rozhrania správne spolupracujú).
4. Implementácia (triedy a metódy) $\rightarrow$ Pokrýva sa pomocou Jednotkových testov (Unit testy priamo nad kódom).

Nezávisle na modeli je dôležité nastaviť správnu komunikáciu, definovať a používať jednotný jazyk. Ak chceme čokoľvek riadiť, je potrebné mať informácie o aktuálnom stave, dodržiavaní plánu, očakávaných zmenách, problémoch...

Hlavné metodiky riadenia SW projektov sú **prediktívne metodiky (napríklad RUP)** a **agilné (napríklad SCRUM)**.

## Metodika (Rational) Unified Process (UP, RUP) (2/5)

Pri opise charakteristického RUP/UP diagramu (tzv. hump chart alebo vlnový diagram) chcú skúšajúci počuť, že diagram zachytáva dve dimenzie vývoja softwaru:

**Stĺpčeky (Dimenzia časová / dynamická)**: Predstavujú časovú os projektu rozdelenú do 4 hlavných fáz (Inception, Elaboration, Construction, Transition), pričom každá fáza sa ďalej delí na jednotlivé iterácie.

**Štátnicový chyták:** Fázy nie sú totožné s jednou iteráciou! Fázy pokrývajú celý životný cyklus projektu od začiatku do konca a každá z nich sa skladá z jednej alebo viacerých dielčích iterácií.

**Riadky (Dimenzia obsahová / statická)**: Predstavujú jednotlivé disciplíny / workflows (napríklad Business Modeling, Requirements, Analysis & Design, Implementation, Test, Deployment a podporné disciplíny ako Configuration & Change Management, Project Management, Environment).

**Vlnovky (Humps)**: Výška plochy v danom mieste vyjadruje intenzitu úsilia/práce, ktorú tým konkrétnej disciplíne v danej iterácii venuje. Napríklad v rané fázy Inception je vlnovka u disciplíny Requirements veľmi vysoká, zatiaľ čo u Implementation je takmer nulová. Počas Construction sa tento pomer obracia.

- rigidná, dôraz na procesy
- vhodná, ak máme jasné a pevné požiadavky, premenlivé aspekty môžu byť čas a zdroje
- vyžaduje podstatnú prípravu plánu vopred
- iteratívna a inkrementálna, jednotlivé aktivity (plánovanie, požiadavky, modelovanie, dizajn, vývoj, testovanie, nasadenie...) sa čiastočne prekrývajú
- riadená rizikami, use-case požiadavky
- architektúra je stredobodom - existuje architektonický tým, s ktorým ostatné tímy konzultujú prípadné nejasnosti/problémy, slúži ako centrálny komunikačný uzol (lepšie, ako keby spúšť dev tímov komunikovala navzájom)
- umožňuje pevnú kontrolu nad procesmi a tímom
- vhodná, ak potrebujeme poriadnu dokumentáciu (UML diagramy)
- hodí sa pre veľké a heterogénne produkty, veľké tímy...

**Výhody:**
- zákazník nie je pri vývoji potrebný, definícia produktu je zakotvená v zmluve (presne vie, čo dostane)

**Nevýhody:**
- pracujeme s fixnými termínmi, rozpočtom i funkcionalitou
    - v reálnosti sa termín a rozpočet môže ľahko meniť v závislosti od vývoja
- zmeny požiadaviek sú problém
- potrebný viac času na plánovanie
- zložitá zmluva, je potrebné myslieť na všetko (exhaustive kritéria prijatia, pokuty...)

![](img/20230523215135.png)

### Fázy iterácií

Iterácie sú zoskupované do fáz:

#### Inception (1 iterácia)
- riešime uskutočňovateľnosť, zachytávame kľúčové požiadavky, riziká
- opis významných požiadaviek s dopadom na architektúru
- identifikácia actorů
- identifikácia ďalších systémov, s ktorými komunikujeme
- na konci poznáme ciele, hrubú architektúru
- čo sa používa pre podobné systémy? s čím máme skúsenosti?
- určenie použitých technológií
- určenie orientačnej ceny, časového plánu a rizík => **Project brief**

#### Elaboration (2 iterácie)
- riešime požiadavky, architektúru, hráme si s UML diagramami
- na konci máme architektúru, dizajn systémov odrážajúci požiadavky

#### Construction (4 iterácie)
- tvoríme systém, testujeme, nasadzujeme
- na konci máme beta verziu, relatívne stabilnú a otestnovanú, pripraveníu na používanie

#### Transition (2 iterácie)
- hľadáme a opravujeme chyby, robíme manuály, poskytujeme konzultácie
- testovanie so používateľmi (beta, na základe feedbacku robíme zmeny), akceptačné testy

### Workflows a UML diagramy

Iterácia by nemala prekročiť 3 mesiace, prínosom iterácie je **inkrementálny prírastok**, každá iterácia obsahuje workflows, ktoré sú viac alebo menej prítomné. Pre každý workflow sa používajú určité UML diagramy:

- **Business modelovanie**
    - **activity diagram** - opisuje obchodné procesy, ktoré sa majú riešiť
- **Požiadavky**
    - **use case diagram** - definuje hranice systémov, actorů a ich interakcie s funkcionalitou systémov
- **Analýza a dizajn**
    - **sequence diagram** - Interakčné diagramy, ktoré ukazujú, ako si objekty medzi sebou posielajú správy, aby realizovali konkrétny scenár z Use Case diagramu.
    - **class diagram** - Zobrazuje kľúčové pojmy z reálneho sveta a vzťahy medzi nimi (napríklad Zákazník, Objednávka, Faktúra), bez programátorských detailov.
- **Implementácia**
    - **class diagram** - Už obsahuje konkrétne dátové typy, viditeľnosti (public/private) a metódy, zo ktorých je možné priamo generovať kód.
    - **component diagrams** - Ukazuje fyzické usporiadanie kódu – moduly, knižnice (JAR, DLL), zdrojové súbory a ich vzájomné závislosti.
- **Testovanie**
    - **use case** - Slúži ako priamy podklad pre akceptačné testy (Acceptance Tests) a systémové funkčné testy
    - **class diagram** - Základný stavebný kameň pre vývojárov pri písaní jednotkových testov (Unit Tests)
    **activity diagrams** - Výborný podklad na tvorbu integračných a end-to-end (E2E) testov
- **Deployment**
    - **deployment diagram** - zobrazuje fyzické usporiadanie systémov – servery, databázy, sieťové prvky a ako sú medzi sebou prepojené

RUP je konkrétna komerčná metodika stavajúca sa na UP (pridáva napríklad jednotlivé role a odpovědnosti v tíme, konkrétne postupy...), UP je všeobecný rámec.

**Iteratívny vývoj (Evolúcia celku):** Vývoj prebieha v opakovaných cykloch (iteráciách). V každej iterácii sa berie v úvahu celý systém (alebo jeho podstatná časť) a ten sa postupne zahusťuje, vylepšuje a spresňuje.

**Metafora:** Ako keď maliar najprv načrtne celú kompozíciu uhlom na celé plátno, potom v ďalšej iterácii pridá základné farby všade a v poslednej iterácii vykresľuje detaily. V UP to zodpovedá napríklad fázy Elaboration, kde sa definuje a overuje architektúra celého systémov na základe kľúčových use casov.

**Inkrementálny vývoj (Stavba po kúskoch):** Systém sa vyvíja a dodáva po samostatných, úplne dokončených častiach – prírastkov (inkrementov).

**Metafora:** Ako keď staviš dom po miestnosti – najprv úplne postavíš, namaluješ a vybavíš kuchyňu, potom obývačku, potom spálňu. V UP to zodpovedá fázy Construction, kde sa v každej iterácii implementujú a dokončujú konkrétne sady funkcionalít.

**Prepojenie v UP:** UP je iteratívny aj inkrementálny zároveň. Je iteratívny, pretože v každej jednotlivej iterácii tým prechádza všetkými disciplínami (od analýzy cez kódovanie až po testovanie) a produkt sa evoluične spresňuje. Je inkrementálny, pretože výstupom každej dokončenej iterácie musí byť spustiteľný, otestovaný a stabilný prírastok kódu (executable architecture/increment), ktorý rozširuje predchádzajúcu verziu.

## Agilné metodiky a princípy agilného vývoja SW (3/5)

- flexibilná, dôraz na ľudí
- radšej budeme reagovať na zmenu, ako sa pevne držať plánu
- snažíme sa fixovať čas a zdroje, premenlivá môže byť funkcionalita (*Postavili sme dom a plot, v rozpočte nám zvyšujú zdroje na garáž, alebo bazen. Čo z toho chcete?*)
- vhodná, ak sa požiadavky menia, nie je jasná požadovaná výsledná podoba systémov, alebo zákazník požaduje niečo hmatateľné relatívne skoro => nie je presný termín ukončenia
- vyžaduje minimálne plánovanie vopred
- kľúčová je dobrá komunikácia a spolupráca tímu
- automatizované testovanie
- variabilita funkčnosti (vývoj prebieha tak, že keď dôjde čas/peniaze, pýtame sa zákazníka, či niečo pridáme, alebo či vynecháme nejakú časť systémov)
- face-to-face komunikácia, rýchle stretnutia - rýchlejšie, získame lepšie porozumenie
- jednoduchá dokumentácia - dokumentácia ťažko udržiava tempo s realitou, preto ju držme čo najjednoducho, ideálne napojenú na kód
- časté stretnutia so stakeholdermi (sprint review), prezentácia novej funkčnosti (lepšie, ako len opis)

### Príklady agilných metodik

#### Extreme programming
- osvedčené postupy ťahá do extrému (osvedčujú sa reviews? => robiť reviews čo to ide)
- párové programovanie, dôraz na testy, refaktorovanie, kód je single source of truth (dokumentáciu generujeme z kódu, používame schéma na generovanie ostatných vecí...)
- rýchla spätná väzba, dôraz na jednoduchosť, malé prírastky

### SCRUM

- najčastejšie využívaná agilná metodika
- iteratívna, inkrementálna
- jednoduchá, očakáva sa použitie aj ďalších nástrojov/procesov
- vhodný pre menšie tímy (<=15 ľudí)
- hodí sa, keď máme tým schopný samostatnejšej práce, potrebujeme rýchlo vytvoriť aspoň nejaký produkt

#### Role

- **product owner** - reprezentuje stakeholderov, má najväčší prehľad o požiadavkách na produkt, spravuje product backlog
- **scrum master** - zodpovedný za dodržiavanie scrumu, riešinies procesy
- **tým vývojárov** - 3-9 ľudí, sebeobslužný (má ľudí na všetko) a samo organizovaný, spravujú sprint backlog, zodpovední za doručenie produktu

#### Artefakty

##### Product backlog
- obsahuje všetku zvyšnú požadovanú funkcionalitu vo forme **user stories**
    - jednotka funkčnosti, testovateľná, logický celok
    - každý príbeh má:
        - **story points** reprezentujúce časovú náročnosť odhadnutú pomocou [planning pokeru](#planning-poker)
        - akceptačné kritéria (testovateľné, formulované ako Given ... When ... Then ...)
        - môže mať zoznam rizík
        - príbehy majú prioritu (MoSCoW) podľa hodnoty, náročnosti, rizika, prínosu...
            - Must - nevyhnutné
            - Should - malo by byť
            - Could - bolo by fajn
            - Won't/Wish - zabudni na to, možno neskôr
        - na testovanie je možné použiť Gherkin/Cucumber (As a ... I can ... So that ...)

- tvorený celým scrum tímom, spravuje ho product owner
- v praxi ide o tabuľu (skutočnú/virtuálnu) s lepiacimi poznámkami

##### Sprint backlog
- časť product backlogu (množstvo user stories), ktorá sa má vykonať v danom sprinte
- príbehy sú rozdelené na jednotlivé tasky, u každého je určený časový odhad v hodinách
- úloha má fázy Todo, In progress a Done
- úlohy si k práci vyberajú vývojári podľa vlastného uváženia, ale žiadne (ani príbehy) nemôžu byť v rámci sprintu pridané/odobraté
    - bolo by potrebné zrušiť celý sprint product ownerom
- spravovaný tímom vývojárov

##### Product increment
- všetky položky product backlogu, ktoré sa spĺňajú počas sprintu (a.k.a. to, čo sa za sprint stihne/urobí)
- tvorený tímom vývojárov, testovaný zákazníkom, môže byť vydaný product ownerom
- je potrebné, aby bol použiteľný a bol splnený (podľa definície scrum tímu)

#### Udalosti

##### Project planning
- tvorba [project charteru](3_projektove_riadenie.md#pmi-project-management-body-of-knowledge-pmbok)
- tvorba product backlogu
- výber kľúčových stratégií (komunikácia, riziká, kvalita, zmeny...)

##### Sprint planning
- prebieha na začiatku sprintu, približne 8 hodín
- účastní sa celý scrum tým
- vytyčuje sa cieľ nadchádzajúceho sprintu (a.k.a. čo chceme urobiť), vyberáme veci z product backlogu a priradúváme im úlohy

##### Sprint
- iterácia zameraná na vývoj funkčnosti v sprint backlogu, cieľom je vytvoriť použiteľný a potenciálne vydateľný product increment
- pracuje naň celý scrum team
- product owner riešinies komunikáciu, vývojári vyvíjajú, scrum master sleduje dodržiavanie procesov
- analýza, dizajn, implementácia, testovanie
- max 1 mesiac, všetky sprinty trvajú rovnaký čas
- po sprinte sledujeme [team velocity](#team-velocity), podľa nej máme lepší odhad na budúce plány, je možné podľa nej upraviť rozsah sprint backlogu

##### Daily scrum (standup)
- 15 minút každý deň, účastní sa vývojári a možno aj scrum master
- čo som robil včera, čo budem robiť dnes, narážam na nejaké problémy?

##### Sprint review
- 4 hodiny, účastní sa celý scrum team a kľúčoví stakeholdeři (napríklad zákazník, používateľ)
- prebehnú prevedenie inkrementu
- preberoú sa prípadné problémy, zmeny, odpovedá sa na prípadné otázky stakeholderov
- preberoú sa prípadné zmeny product backlogu
- prípadne sa prepočítá predpokladaný termín dokončenia
- preberie sa, čo by sa malo ďalej robiť, upravia sa priorita/poradie v product backlogu

##### Sprint retrospective
- 3 hodiny, účastní sa scrum team
- riešia sa procesy - rozdelenie práce, splnil sa cieľ, je potrebné niečo upraviť?
- riešia sa vzťahy - klapalo to? potrebuje niekto užšiu spoluprácu?
- riešia sa nástroje - dobrá komunikácia? dostatočná transparentnosť?
- riešia sa ľudia - mal niekto problémy? niekoho pochválime?
- čo nefungovalo, čo môžeme zlepšiť
- ideálne sa vymyslí jedno zlepšenie procesov, ktoré sa v ďalšom sprinte bude používať
- prípadne sa upravia kľúčové stratégie, riziká

##### Project retrospective
- uzavretie projektu s tímom
- riešíme poučenia, čo sa podarilo, nepodarilo...
- poďakujeme všetkým

#### Ukončenie SCRUM

SCRUM môže skončiť, keď:
- product backlog je prázdny (všetko hotovo), alebo neuvádzame (spoločne so stakeholdermi) jeho obsah za dôležitý
- dôjde čas/peniaze
- urobili sme posledný sprint a hoci je čo opravovať, defekty sú prijateľné
- product owner/stakeholder sa rozhodne ukončiť projekt

#### Ďalšie aspekty SCRUM

- dizajn a architektúra sa môžu robiť kontinuálne pre jednotlivé príbehy, alebo sa do procesu zavádza ako štandard (napríklad používame vrstvovú architektúru, používame tieto technológie...)
- zmluva sa zvyčajne určuje podľa toho, koľko (a akých) ľudí bude za dané obdobie na projekte pracovať
    - super na flexibilitu, ale ťažko sa určuje výsledná cena/termín
- zákazník je zatažený do postupu vývoja, môže hneď dávať spätnú väzbu, ale tento overhead vyžaduje extra čas
- balancuje sa Čas, Cena a Rozsah funkcionalít

### Burndown chart

Ukazuje koľko práce zvyšuje a ako si vedieme oproti plánu:

![](img/20230525221317.png)

### Team velocity

Dokončené príbehy bodov za sprint, je vidieť v Burndown Chartu v dy/dx, alebo ako samostatná krivka:

![](img/20230525221638.png)

### Planning poker

Pre každý príbeh každý z tímu vykonáúa odhad, odhady sa zverejnia najednou. Nasleduje diskusia, kým sa na bodoch za daný príbeh všetci neshodnou (odporúčané použité body sú podľa Fibonacciho sekvencie).

### SCRUM Board

Viditeľný celému tímu, na jednotlivých listoch úloh je vidieť aj spracovávajúca osoba:

![](img/20230525224009.png)

## Nasadenie a prevádzka softvérových systémov (4/5)

- pred nasadením je dôležité systém otestovať v prostredia, ktoré bude čo najblížšie tomu produkčnému
- kľúčové je v prevádzke zaznamenávanie udalostí (aby sme v prípade chyby vedeli, čo sa v systéme dialo), monitorovanie, systém spätnej väzby
- nasadenie zahrnuje prípravu prostredia (inštalácia os, databáz...), je možné automatizovať/zjednodušiť použitím Platform as a Service, prípadne kubernetes
- pred nasadením do prevádzky je fajn prejsť a skontrolovať dokumentáciu, ktorá môže byť kvôli vývoju zastaraná
- súčasťou nasadenia je aj školenie popoužívateľov, aby sme predišli neúspechu z dôvodu neochoty/neznalosti používania
- súčasťou nasadenia môže byť aj customizácia systémov pre špecifické potreby zákazníka (ak to náš systém umožňuje)

## Údržba softvérových systémov, znovupoužiteľnosť (5/5)

### Analýza projektu

Na konci je fajn si urobiť analýzu toho, čo (ne)fungovalo, čo zlepšiť...
- dosiahnutá produktivita a kvalita
- použitý proces, odchylky, dôvody
- plán vs realita a dôvody (čas, peniaze, chyby, FP/LOC...)
- riziká (plán vs realita, ako sme riešili riziká a problémy)
- pracnosti (aj podľa etáp)
- zhrnutie defektov
- kauzálna analýza - analýza odchýlok výkonu u použitého procesu (ako a prečo)
- použité technológie a ich hodnotenie
- popísať v dokumente tým a jednotlivcov, na ktorých je možné sa prípadne obrátiť (napríklad keď sa riešinies problém v ďalšom projekte)
- aktíva procesu - čo vzniklo a môže byť použité aj v iných projektoch (napríklad knižnice, checklisty...)

### Údržba systémov

- údržba sa môže robiť ako samostatný projekt, môžu na to byť špecializované tímy
- riešia sa opravy (aj bezpečnostných) chýb, aktualizácie a vylepšenia (ideálne neakým spôsobom automatizované, ale môže byť fajn potvrdenie popoužívateľa), správu zmien (čo sa ako a prečo zmenilo)
- znovupoužiteľnosť sa zvyčajne riešinies v rámci jednotlivých služieb/programov/komponent, ale nie opakovaným používaním štruktúr medzi rôznymi projektami (pokiaľ nejde o špecializovanú knižnicu) - mohli by sme mať problém v prípade zmeny

[Prejdi na ďalšiu otázku](./3_projektove_riadenie.md)
