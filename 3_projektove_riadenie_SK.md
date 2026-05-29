# **Projektové riadenie** (PA179)

> Plánovanie, riadenie rizík, úloha modelov v projektovom riadení. Ganttove diagramy, sieťová analýza, metóda kritickej cesty (CPM), Program Evaluation and Review Technique (PERT). Medzinárodné normy a metodiky projektového riadenia (PMI Project Management Body of Knowledge, PRINCE 2). Príklady z praxe pre všetko vyššie uvedené. [PA179](https://is.muni.cz/auth/el/fi/jaro2022/PA179/um/)

1. [Plánovanie, riadenie rizík, úloha modelov v projektovom riadení](#plánovanie-riadenie-rizík-úloha-modelov-v-projektovom-riadení-14)
2. [Ganttove diagramy, sieťová analýza, metóda kritickej cesty (CPM), Program Evaluation and Review Technique (PERT)](#ganttove-diagramy-sieťová-analýza-metóda-kritickej-cesty-cpm-program-evaluation-and-review-technique-pert-24)
3. [Medzinárodné normy a metodiky projektového riadenia (PMI Project Management Body of Knowledge, PRINCE 2)](#medzinárodné-normy-a-metodiky-projektového-riadenia-pmi-project-management-body-of-knowledge-prince-2-34)
4. [Príklady z praxe pre všetko vyššie uvedené](#príklady-z-praxe-pre-všetko-vyššie-uvedené-44)

## Plánovanie, riadenie rizík, úloha modelov v projektovom riadení (1/4)

### Plánovanie

Je potrebné rozlišovať medzi:

- **Projekty**
    - dočasné - majú začiatok aj koniec, typické fázy (príprava, vykonanie, uzavretie, prípadne fázy SW životného cyklu)
    - prinášajúce zmenu, dodávajúce hodnotu zainteresovaným stranám (všetkým zúčastneným; popoužívateľom, zákazníkom aj dodávateľom produktu...)
    - unikátne - každý má svoje špecifiká (požiadavky, zákazníkov, tým...), nie je to o každodennej rutinnej práci firmy
    - plánované
    - opakovateľné prvky projektu (alebo celé projekty) sú **procesy** - riadené udalosťami, bývajú dobre definované (ako postupovať), vizualizované flow chartom
      > proces je opakovateľný rad aktivít s definovanými vstupmi, výstupmi, nástrojmi, technikami...
    - zvyčajne sú spojené s rizikom - spojené s unikátnosťou (nikdy sme to nerobili), termínmi, robíme nejakú zmenu
    - **riadenie**
        - balancia medzi časom, cenou a rozsahom/kvalitou
        - začneme používaním noriem (PRINCE2, PMBOK, IPMA), aby sme efektívnejšie komunikovali, koordinovali, zvýšili dôveru zainteresovaných strán, transparentnosť, aby sme nanovo neobjavovali vymyslené
- **Programy** - skupiny dočasných, vzájomne prepojených projektov riadené ako skupina aby sme dosiahli ciele, ktoré projekty zdieľajú
    - **riadenie**
        - správa rizík
        - odstránenie obmedzení a konfliktov z projektov
        - v projektoch sa premýšľa a plánuje aj s ohľadom na iné projekty programu
- **Portfolio** - skupiny projektov a programov, riadené na dosiahnutie dlhodobých strategických cieľov
    - a.k.a. čo dlhodobo ponúkame
    - **riadenie**
        - monitoringom výkonu firmy
        - výberom a prioritizáciou programov a projektov

Pre konkrétny projekt je potrebné si zvoliť vhodný prístup **prediktívny** alebo **agilný** [pozri otázka 2](2_softwarove_inzenyrstvi.md).

#### Agilné plánovanie

Ďalej je potrebné u plánovania projektov sepísať Project Charter popisujúci základné informácie o projekte (prečo, čo, kto, kedy, ako, za koľko...), sepísať podrobnosti kľúčových stratégií (komunikácia, riziká, kvalita, zmeny) a neakým spôsobom začať plánovať prácu (product backlog, riešenie architektúry...).

#### Prediktívne plánovanie

Sepíše sa **Project Initiation Documentation** obsahujúce detailný Business Case, všetky informácie o projekte (prečo, čo, kto, kedy, ako, za koľko), definujú sa kľúčové stratégie (komunikácia, riziká, kvalita, zmeny), všetko sa dokumentuje, tvoria sa príslušné registry, všetko sa schvaľuje product boardom (zástupcovia exekutívy, inžinierov a zákazníkov). Do PID sa potom zapisujú aj zmeny a priebeh, aby bolo možné porovnať plán a realitu, je dostupný všetkým v rámci projektu.

Robí sa detailná analýza požiadaviek, spúšť Use case diagramov, detailný rozsah slúžiaci ako základ na oceňovanie, design mockupy. Tvoria sa **špecifikačný dokument** produktu - obsahuje požiadavky, rozdelenie systémov na komponenty (vrátane detailného popisu až po polia vstupných formulárov), očakávanú kvalitu, akceptačné kritéria.

Robí sa **projektový plán** (prečo, čo, kto, kedy, ako, za koľko...) - **Work Breakdown Structure** tvorená zo špecifikačného dokumentu, počítajú sa časy a ceny jednotlivých **Work Packages** (súčasť WBS, najnižšia jednotka) napríklad pomocou [PERT](#program-evaluation-and-review-technique-pert), ich závislosti, tvoria sa rozvrhy (gantt/sieťový diagram), priradútvajú sa zodpovednosti (malo by ísť ľahko nájsť aktivity človeka aj všetky spojené s aktivitou). 

**Pozor na rozdiel Člověkoden (Man-Day / MD) vs. Kalendárny čas:** MD je jednotka **úsilia (pracnosti)**, nielen času. Úloha o veľkosti 10 MD znamená, že zabere 10 dní *jednému* človekovi. Ak na ňu nasadíme 5 ľudí, môže teoreticky trvať len 2 kalendárne dni. Do kritickej cesty (CPM) sa vždy dosadzuje kalendárna *dĺžka trvania*, nie absolútne úsilie. (Pozor na *Brooksov zákon*: Pridanie ľudí do opozdného SW projektu ho zvyčajne ešte viac opozdí kvôli režii na komunikáciu).

#### Chronologický postup prediktívneho plánovania (Štátnicový chyták)
Skúšajúci často nachytajú študentov na otázke: „Čo urobíte pri plánovaní ako prvé? Gantt, alebo sieťový graf?" Správna odpoveď je **WBS**. Postup musí ísť striktne v tomto poradie:
1.  **Dekompozícia rozsahu (WBS):** Rozdelenie celého systémov na najmenšie riaditeľné celky (**Work Packages**). Bez toho nemožno plánovať ďalej.
2.  **Odhad pracnosti a zdrojov:** Každému Work Package priradíme potrebné úsilie (napríklad pomocou PERT) a určíme, kto ho bude robiť.
3.  **Zostavenie sieťového grafu:** Definujeme logické závislosti medzi úlohami (čo na čo nadväzuje).
4.  **Výpočet kritickej cesty (CPM):** Zistíme matematické trvanie projektu a kritické úlohy.
5.  **Vykreslenie do časovej osy (Ganttov diagram):** Teraz na základe všetkých predchádzajúcich krokov vzniká Gantt ako vizuálny kalendárny plán.

*WBS*

![](img/20230526000518.png)

### Riadenie rizík

Postup:

1. **Identifikácia rizík**
    - čerpáme z predchádzajúcich skúseností, poučení z minulosti... čo a prečo sa stalo?
2. **Hodnotenie rizík**
    - každé riziko spôsobí náklady, môžeme preň odhadnúť cenu
    - každému priradíme pravdepodobnosť a kritičnosť dopadu, určíme dôsledky
      ![](img/20230525214112.png)
3. **Určenie odpovedí na riziká**, možnosti:
    - **akceptuj** - no tak sa to stane, no, nevadí, náklady na prevenciu by boli vyššie ako samotné riziko
    - **vyhni sa** - nastavenie plánu, aby problém nemohol nastať (napríklad použitie inej technológie, ktorá tento problém nemá)
    - **presuň** (napríklad na niekoho iného) - napríklad tento komponent outsourcujeme so solídnym SLA, alebo sa poistíme
    - **znížim** - skráťte pravdepodobnosť/mieru dopadu rizika, napríklad dôkladnejším systémom reviews
4. **Stanovenie monitoringu rizík**
    - stanovenie zodpovednosti za monitoring rizík
    - určenie, kde budú riziká definované, kedy budú revidované a upravované
5. **Vytvorenie registra rizík**

Možné zdroje rizík (najčastejšie tučne):

- **používateľ** - **neschopnosť/neochota zapojiť sa**, odpor voči zmenám
- **požiadavky** - **zle pochopené**, zle definované, nejasné či neadekvátne, **prídu zmeny** (mnohokrát až v momente, keď môžu zásadne narušiť vyvíjaný systém)
- **zložitosť projektu** - komplexná doména, použitie novej/nezavádzkej technológie
- **management** - **neefektívne riadenie**, zle zvolená/použitá metodika/norma, **zlý odhad nákladov/zdrojov/času**, zle určená komunikácia, **nezkušený manažér**
- **tým** - nezkušenosť, **málo ľudí**, osobné konflikty
- **firemné prostredie** - nestabilné, zmena vedenia...
- **subdodávatelia** - opoždenie, nedostatočná kvalita, komunikácia...

#### Špecifiká prevence u agilného riadenia rizík

Prevencia:

- **Transparentnosť a spätná väzba**, aby sme predišli nedorozumeniam v tíme
- **Používanie príbehov popoužívateľa** - sú ľahko zrozumiteľné pre zákazníka, dajú sa dobre overiť
- **Jasná definícia, čo znamená "hotovo"**
- **Krátke iterácie** - skoro zistíme, čo je prípadne zle

### Úloha modelov v projektovom riadení
V softvérovom projektovom riadení slúžia modely primárne na **odhadovanie pracnosti (effort), času a ceny** projektu na základe historických údajov a metrik. Skúšajúci chcú počuť tieto dva hlavné prístupy:

* **Metóda funkčných bodov (Function Points - FP):** Odhaduje veľkosť SW z pohľadu popoužívateľa (počet vstupov, výstupov, dopytov, interných súborov). Je nezávislá na technológii.
* **Model COCOMO (Constructive Cost Model) a COCOMO II:** Algoritmický model, ktorý odhaduje pracnosť v person-mesiacoch (Person-Months) a kalendárny čas na základe veľkosti kódu (KLOC - tisíc riadkov kódu) a produktívnych faktorov (skúsenosť tímu, komplexnosť platformy).

COCOMO rozlišuje **3 vývojové módy (kontexty projektu)**, na ktoré sa doc. Ráček veľmi často pýta:
1.  **Organický (Organický):** Malé projekty, známe prostredie, malý a skúsený tým, flexibilné požiadavky (napríklad interný firemný nástroj). Nízka režia riadenia.
2.  **Polorozdelený (Semi-detached):** Strední projekty, zmiešaný tým (skúsení aj neskúsení), časť požiadaviek je striktná, časť voľnejšia. Vyššie nároky na koordináciu.
3.  **Vestavěný / Integrovaný (Embedded):** Komplexné projekty s extrémne prísnymi obmedzeniami (napríklad riadenie letového premávku, bankové jadro, vstavané medicínsky software). Požiadavky sú pevné, procesy rigidné, obrovská režia na testovanie a dokumentáciu.

Ďalej sem patria **matematické modely riadenia** (sieťové grafy CPM/PERT), ktoré modelujú projekt ako matematický graf a hľadajú v ňom kritické miesta (úzke hrdlá).

## Ganttove diagramy, sieťová analýza, metóda kritickej cesty (CPM), Program Evaluation and Review Technique (PERT) (2/4)

### Ganttove diagramy

- nástroj na plánovanie (nielen) projektov

V základe toto:

![](img/20230525192847.png)

ale je možné rozšíriť...

- os y obsahuje úlohy (prípadne zdroje)
- os x zobrazuje čas
- úloha ako uzel/obdĺžnik (šírka udáva časovú náročnosť), prípadne hrana značí vzťah
- je možné pridať:
    - milníky
    - pokrok
    - zdroje (kto čo robí, dávajú sa miesto udalostí na os y), potom riešíme problém plánovania job-shopu
    - ohraničenia, precedenčné podmienky (úloha musí byť spustená až po dokončení inej úlohy, niečo je možné paralelizovať...)
- zvyčajne minimalizujeme makespan (čas dokončenia poslednej úlohy a teda aj celého projektu)

![](img/20230525195955.png)

### Sieťová analýza

Metódy na modelovanie súboru činností vedúcich k dosahu nejakého cieľa (tj. projektov).

Cieľom je projekt naplánovať, minimalizovať prostoje a náklady, určiť termíny, celkovú dobu trvania projektov, identifikovať kritické úlohy v projekte.

Používa sa na to sieťový graf hranovo/uzlovo orientovaný - úlohy sú na hranách/uzloch. Uzlovo orientovaný umožňuje ľahko modelovať precedenčné podmienky, je možné ľahko použiť na metódu kritickej cesty.

* **AON (Activity-on-Node / Uzlovo orientovaný):** * **Uzly** predstavujú samotné aktivity (činnosti, napríklad "Programovanie backendu").
    * **Hrany (šípky)** predstavujú logické závislosti medzi nimi.
    * *Využitie:* Oveľa častejšie v modernom softvéri (Jira, MS Project), pretože sa v ňom ľahko modelujú zložitejšie závislosti (napríklad SS, FF).
* **AOA (Activity-on-Arrow / Hranovo orientovaný):**
    * **Hrany (šípky)** predstavujú samotné aktivity, ktoré spotrebúvajú čas a zdroje.
    * **Uzly** predstavujú **udalosti / milníky (milestones)** – okamžik, keď jedna činnosť končí a druhá začína (majú nulové trvanie).
    * *Využitie / Výhoda:* Skúšajúci chcú počuť, že AOA sa vynikajúco hodí na prirodzené zobrazenie milníkov priamo v grafoch. Niekedy vyžaduje zavedenie "fiktívnych hrán" (dummy activities) s nulovým časom na zachovanie logiky grafu.

### Metóda kritickej cesty (CPM)

Metóda na identifikáciu vzájomne závislých aktivít, ktoré majú vplyv (sú kritické) na dobu dokončenia projektu a nemôžu byť opozdené bez predĺženia dokončenia projektu.

#### 4 typy precedenčných závislostí (Chyták na tabuli)
Pri výpočte CPM na tabuli vám skúšajúci nemusí dať len klasickú nasledujúcu úlohu. Musiete poznať všetky štyri typy väzieb:
* **FS (Finish-to-Start / Koniec-Začiatok):** Najčastejší. Úloha B môže začať až po dokončení úlohy A (napríklad Testovanie začne až po dokončení Implementácie).
* **SS (Start-to-Start / Začiatok-Začiatok):** Úloha B môže začať hneď, keď začne úloha A. Môžu bežať paralelne (napríklad S programovaním frontendu sa môže začať hneď, ako sa začne programovať backend).
* **FF (Finish-to-Finish / Koniec-Koniec):** Úloha B môže skončiť až vtedy, keď skončí úloha A (napríklad Dokumentácia celého systémov môže byť hotová/skončená až v momente, keď skončí implementácia poslednej komponenty).
* **SF (Start-to-Finish / Začiatok-Koniec):** Veľmi vzácna. Úloha B môže skončiť až po tom, ako úloha A začne.

[Postup](https://www.youtube.com/watch?v=4oDLMs11Exs):

- urobíme si graf závislostí, určíme si dobu trvania aktivít
- v prvom prechode ideme štart => koniec, riešíme earliest start/completion time. Keď vedú 2 do 1, berieme maximum tých 2.
- v druhom prechode ideme koniec => štart, riešíme latest completion/start time. Keď vedú 2 z 1, berieme minimum tých 2.
- kritická cesta obsahuje aktivity, ktoré majú earliest & latest finish time identické
- slack/float udáva, o koľko môžeme danú aktivitu opozdúť, bez toho aby došlo k opozdeniu projektu (`latest completion time - earliest completion time`)

![](img/20230526101347.png)

### Program Evaluation and Review Technique (PERT)

Technika na odhad času na dokončenie úlohy. Berieme **optimistický** odhad, **pesimistický** odhad a **najpravdepodobnejší** odhad:

`očakávaný = (optimistický + 4 * najpravdepodobnejší + pesimistický) / 6`

Ak máme informácie o úrovni platov implementátorov úloh, môžeme dopočítať odhadovanú cenu.

## Medzinárodné normy a metodiky projektového riadenia (PMI Project Management Body of Knowledge, PRINCE 2) (3/4)

- normy projektového riadenia PRINCE2, PMBOK, IPMA ICB opisujú všeobecnejší spôsob riadenia
- metodiky SW vývoja (RUP, SCRUM) riešia riadenie v rámci vývojového tímu, sú špecifické pre vývoj SW

![](img/20230525184623.png)

### PMI Project Management Body of Knowledge (PMBOK)

- **procesne orientovaná** norma, podrobne opísaná sada osvedčených postupov
- ľahko sa používa ako príručka na vhodné vedomostné oblasti a nástroje/techniky pri životnom cykle projektu
- vhodný, keď:
    - manažér potrebuje tipy na nástroje a techniky, ktoré by mal používať, ale aspoň trochu si myslí čo a ako

49 procesov (rad aktivít s definovanými vstupmi, výstupmi, nástrojmi a technikami) rozdelených do:

- **5 procesných skupín** - logické rozdelenie procesov podľa fáz (inicializácia, plánovanie, vykonávanie, monitoring a riadenie, uzavretie)
- **10 vedomostných oblastí/disciplín** projektového manažmentu, každá má svoje procesy:
    - **Integrácia**
        - tvorba **Project Charteru**:
            - **Business case (prečo)** - ciele projektu, hrubá cena, rozpočet, riziká
            - **Project outcome (čo)** - opis, hlavné ciele a požiadavky
            - **Stakeholders (kto)** - externé aj interné, riešíme ich role, potreby, zapojenie a zodpovednosti
            - **Management approach (ako)** - popis použitých noriem, nástrojov, metodik, životného cyklu projektu...
            - **Schedule (kedy)** - hrubý plán projektu, fázy, milníky, Ganttov diagram...
    - **Rozsah (scope)** - zbieranie požiadaviek, definícia, validácia a riadenie rozsahu funkcionalít systémov, tvorba Work Breakdown Structure
    - **Plán** - definícia a určenie poradia aktivít, odhady časov aktivít, tvorba a riadenie plánu
    - **Cena** - odhad cien a rozpočtu aktivít alebo jednotiek práce pomocou Work Breakdown Structure, riadenie ceny a rozpočtu
    - **Kvalita** - plánovanie, riadenie a kontrola kvality
    - **Zdroje** - odhad nepeňažných a ľudských zdrojov, ich získavanie a riadenie, tvorba a správa tímov
    - **Komunikácia** - plán, správa a kontrola komunikácie a informácií o projekte
    - **Riziko** - identifikácia, kvalitatívna (miara dopadu) a kvantitatívna (pravdepodobnosť) analýza rizík, ich monitoring, plán a procesy reagujúce na riziká
    - **Dodávatelia** - produkty a služby pochádzajúce mimo nášho tímu, zmluvy, objednávky, SLA, výber dodávateľov, monitoring výkonu dodávateľov
    - **Stakeholdeři** - zainteresované osoby; ich identifikácia, plánovanie a správa zapojenia stakeholderov do projektu

### PRINCE 2 (PRojects IN Controlled Environment)

- norma na riadenie všeobecného projektu
- predpísaný postup, krok za krokom (spúšť formulárov na vyplňovanie, checklisty)
- súčasťou nie je správa požiadaviek, rozpočtovanie
- vhodný pre:
    - potrebu veľkého reportingu
    - potrebu úplnej projektovej dokumentácie
    - tým vyžaduje poriadok a kontrolu
    - manažérov s malými skúsenosťami, hodí sa im podrobný opis postupu

#### Fázy

(grubó zodpovedá UP inception, elaboration, construction a transition):

![img.png](img.png)

- **Starting up**
    - tvorba **Project brief**:
        - riešíme uskutočňovateľnosť, zachytávame kľúčové požiadavky, riziká
        - opis významných požiadaviek s dopadom na architektúru
        - identifikácia actorů
        - identifikácia ďalších systémov, s ktorými komunikujeme
        - na konci poznáme ciele, hrubú architektúru
        - čo sa používa pre podobné systémy? s čím máme skúsenosti?
        - určenie použitých technológií
        - určenie orientačnej ceny, časového plánu a rizík
    - plán nasledujúcej fázy:
        - **Work Breakdown Structure**
        - identifikácia aktivít, závislostí
        - odhad trvania aktivít, stanovenie milníkov
        - definícia rolí a zodpovedností
        - tvorba rozvrhu (Gantt/sieťový diagram)
- **Initiation**
    - tvorba **Project Initiation Documentation** (dokument/viacero dokumentov):
        - obsahuje aktuálny stav projektu, plány, Kto, Čo, Kedy, Ako, Prečo, Za Koľko...
        - slúži na definíciu projektu, určenie rámca...
        - schvaľuje product board
        - detailný Business Case (dôvody projektu, očakávania, cost-benefit analýzu, časovú škálu, ceny, riziká)
        - opis štruktúry managementu, rolí tímu
        - opis prístupu ku kvalite, zmenám, riziku, komunikácii
        - plán projektu
    - plán nasledujúcej fázy
- **Delivery**
    - zvyčajne má viacero časti (iterácií), každá max 3 mesiace, každá má definované merateľné a overiteľné milníky
    - produktový manažér sa stará o udržanie ceny, termínov, rozsahu a kvality špecifikovanej v PID
    - produktový manažér autorizuje, vykonáva reviews work packages, hlási (pravidelne) stav, zmeny, problémy a kvalitu vyššie, spravuje riziká a problémy
    - tímový manažér vykonáva tímové plánovanie (jednotlivých work packages), demonštruje kvalitu produktu, zabezpečuje dodanie work packages
    - medzi fázami sa hodnotí končiaca fáza a plánuje (zasa WBS, gantt) nasledujúca, aktualizuje sa PID
- **Close**
    - predanie produktu (samozrejme opäť spúšť protokolov), nasadenie, uzavretie všetkých dokumentov, PID, dokumentácia, tvorba end report a poučení
    - prípadne predanie projektu ops a maintenance tímu
    - tvorba SLA

#### 7 princípov

(všetko máme neakým spôsobom zdokumentované):

- **Kontinuálne odôvodnenie projektu** - prečo to robíme?
- **Učenie sa zo skúseností** - čo (ne)fungovalo
- **Role a zodpovednosti** - presne špecifikovaná štruktúra tímu, vymedzené práva a zodpovednosti
- **Riadenie po fázach** - po každej fázy robíme review Project brief, vykonávame reporting vyššímu managementu
- **Manage by exception** - riadenie sústredíme na časti, ktoré sa nejako (negatívne) vymykajú. Nezasahujeme do toho, čo funguje. Vytyčíme ciele a tolerovateľné odchylky v kvalite, čase, cene a rozsahu, určíme zodpovednosti za neprekročenie
- **Dôraz na produkt** - primárny cieľ je produkt, nie práca
- **Prispôsobenie metodiky projektu** - nie je potrebné PRINCE používať úplne doslova, riadok po riadku. Nie všetky formuláre sú vždy úplne relevantné

#### 7 tém

- **Business case** - obsahuje očakávané prínosy, riziká, časový a cenový rozsah, dôvody projektu... Mal by byť neustále aktualizovaný a držaný validný počas celej doby projektu
- **Organizácia** - definícia rolí a zodpovedností, typy stakeholderov (dodávateľ, business/zákazník, používateľ), 3 úrovne managementu (project board na nasmerovanie projektu (obsahuje exekutívu, senior suppliera, senior usera), project manager na riadenie projektu, team manager na dodávanie produktu), manage by exception
- **Kvalita** - monitoring, akceptačné kritéria, určíme si stratégiu riadenia kvality (nástroje, procesy), riešíme kvalitu produktu i manažerských výtvorov (plány, reporty)
- **Plány** - plánujeme projekt aj jednotlivé fázy, Ganttov diagram, Work Breakdown Structure je základom plánovania
- **Riziká** - identifikácia možných rizík, určujeme spôsob reakcie na dané riziko na základe ceny prevenciálnych opatrení, pravdepodobnosti a dopadu, uchováváme register rizík
- **Zmeny** - u požiadaviek na zmenu riešíme prioritu, dopad, kritičnosť, zkoumáme možnosti riešenia, podľa zmeny upravujeme záznamy a plán
- **Priebeh projektu** - porovnávame realitu s plánmi (čas, cena, kvalita, rozsah, riziká...), sledujeme či stále projekt spĺňa business case

#### 7 procesov

![](img/20230525115631.png)

- **Úplný začiatok projektu** - nastínenie business case, priradenie kľúčových vedúcich osôb, študovanie "poučení" predchádzajúcich podobných projektov, získanie autorizácie product boardu
- **Inicializácia projektu** - príprava stratégií riadenia (rizík, kvality, komunikácie, konfigurácie), projektového plánu, konkretizácia business case, založenie dokumentácie
- **Riadenie fázy** - rieší produktový manažér, monitoring, hlásenie významných udalostí, riadime exceptions, revidujeme a schvaľujeme prácu/nové časti produktu
- **Riadenie dodania produktu** - to isté čo riadenie fázy, ale rieší to tímový manažér
- **Nasmerovanie projektu** - vysokoúrovňové rozhodnutia, funguje počas celej doby projektu, plán nasledujúcej fázy, na konci projektu autorizujeme uzavretie
- **Riadenie medzi fázami (managing a stage boundary)** - plán nasledujúcej fázy, rieší produktový manažér, aktualizácia business case a projektového plánu, report predchádzajúcej fázy
- **Uzavretie projektu** - rieší projektový manažér, evaluácia, predanie produktu, návrh board na ukončenie

### IPMA ICB

*V otázke nie je, ale nie je na škodu vedieť*

- všeobecná norma na vedenie projektu
- na rozdiel od väčšiny ostatných obsahuje podrobný sekciu o soft skills
- vhodný, keď:
    - projekt vyžaduje dobré soft-skills (komunikácia, vedenie, riešenie konfliktov)
    - manažér je skúsený, pozná procesy
    - nie je potrebný spúšť reportingu
- vhodný na používanie ako príručka na rôzne manažérske kompetencie
- kompetentnostný prístup, pre každú ICB opisuje požadované zručnosti a schopnosti, opis a metriky indikátorov kompetencie
  > kompetencie je aplikácia vedomostí (knowledge, informácie & skúsenosti), zručností (skill, schopnosť aplikovať vedomosti) a schopností (ability, používanie zručností efektívne, v správny čas a na správnom mieste) na dosiahnutie žiadaného výsledku
    - kompetencie perspektívy - metódy a techniky na interakciu jedincov s prostrediam
    - ľudské kompetencie - techniky na narábanie s jedincami/skupinami
    - praktické kompetencie - metódy a techniky na úspech projektu

### Metodiky

Opísané v [otázka 3](2_softwarove_inzenyrstvi.md) (metodiky SW vývoja ako RUP, SCRUM)

## Príklady z praxe pre všetko vyššie uvedené (4/4)

### Špecifiká IT projektov

v porovnaní s väčšinou priemyselných odvetví:

- nepresné/neznáme, časté a meniace sa požiadavky
- väčšia ponapríklad prispôsobenia produktu
- veľká zložitosť
- náročné testovanie
- neustály a rýchly vývoj technológií
- možnosť globálnej spolupráce
- projekty môžu v rámci portfólia ovplyvniť ostatné projekty (zvlášť pri zlyhaní)
- ponapríklad riadenia rizík
- dokončené projekty je často potrebné servisovať/poskytovať podporu

### IT Infrastructure Library (ITIL)

Osvedčené postupy na **riadenie IT služieb**:

**Fázy:**
- **Service strategy** - požiadavky, stratégia na zabezpečenie požadovaného, financie, čo vlastne budeme robiť
- **Service design** - Service Level Agreement, riešenie rizík, bezpečnosť & business compliance
- **Service transition** - ako meníme existujúce služby, riešenie deploymentu, uloženie získaných vedomostí na budúce projekty
- **Service operation** - dokumentácia pre popoužívateľov/helpdesk, riešenie incidentov/zmeny požiadaviek/problémov, riešenie identít a prístupu k systémov
- **Continual service improvement** - monitoring, registrovanie, aktualizácia bežiacej služby

### Praktické príklady aplikácie

#### Príklad použitia CPM v praxi

**Situácia:** Vývoj webovej aplikácie pre e-commerce

**Aktivity a závislosti:**
- A: Analýza požiadaviek (5 dní)
- B: Dizajn databázy (3 dni, po A)
- C: Dizajn UI/UX (4 dni, po A)
- D: Implementácia backend (8 dní, po B)
- E: Implementácia frontend (6 dní, po C)
- F: Integrácia (3 dni, po D a E)
- G: Testovanie (4 dni, po F)

**Kritická cesta:** A → B → D → F → G (23 dní)
**Slack:** C a E majú 2 dni slack

#### Príklad PERT odhadu

**Úloha:** Implementácia platobného systémov

- **Optimistický odhad:** 8 dní (všetko ide hladko)
- **Najpravdepodobnejší:** 12 dní (štandardný priebeh)
- **Pesimistický:** 20 dní (komplikácie s API, bezpečnosť)

**PERT odhad:** (8 + 4×12 + 20) / 6 = 76/6 ≈ 12,7 dní

[Prejdi na ďalšiu otázku](./4_databaze.md)
