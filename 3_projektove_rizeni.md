# **Projektové riadenie** (PA179)

> Plánovanie, riadenie rizik, role modelov v projektovém rízení. Ganttovy diagramy, sieťová analýza, metoda kritické cesty (CPM), Program Evaluation and Review Technique (PERT). Mezinárodní standardy a metodiky projektového riadenie (PMI Project Management Body of Knowledge, PRINCE 2). Príklady z praxe pre všetko vyššie uvedené. [PA179](https://is.muni.cz/auth/el/fi/jaro2022/PA179/um/)

1. [Plánovanie, riadenie rizik, role modelov v projektovém rízení](#plánovanie-rízení-rizik-role-modelov-v-projektovém-rízení-14)
2. [Ganttovy diagramy, sieťová analýza, metoda kritické cesty (CPM), Program Evaluation and Review Technique (PERT)](#ganttovy-diagramy-sieťová-analýza-metoda-kritické-cesty-cpm-program-evaluation-and-review-technique-pert-24)
3. [Mezinárodní standardy a metodiky projektového riadenie (PMI Project Management Body of Knowledge, PRINCE 2)](#mezinárodní-standardy-a-metodiky-projektového-rízení-pmi-project-management-body-of-knowledge-prince-2-34)
4. [Príklady z praxe pre všetko vyššie uvedené](#príklady-z-praxe-pro-vše-výše-uvedené-44)

## Plánovanie, riadenie rizik, role modelov v projektovém riadenie (1/4)

### Plánovanie

Je napríklad rozlišovat mezi:

- **Projekty**
    - dočasné - majú start i konec, typické fázy (príprava, prevedenie, uzavrení, prípadne fázy sw životního cyklu)
    - prinášející zmenu, dodávají hodnotu stakeholderum (všem zúčastneným; používateľum, zákazníkum i dodavatelum produktu...)
    - unikátne - každý má svá specifika (požadavky, zákazníky, tým...), nejedná se o každodenní rutinnou práci firmy
    - plánované
    - opakovatelné prvky projektu (či celé projekty) sú **procesy** - rízené událostmi, bývají dobre definované (ako postupovat), vizualizované flow chartem
      > proces je opakovatelná série aktivit s definovanými vstupy, výstupy, nástroji, technikami...
    - bývají spojené s rizikem - spojené s unikátností (nikdy jsme to nedelali), deadliny, deláme nejakou zmenu
    - **rízení**
        - balanc medzi časem, cenou a rozsahem/kvalitou
        - začneme užíváním standardu (PRINCE2, PMBOK, IPMA), abychom efektivneji komunikovali, koordinovali, zvýšili duveru stakeholderu, transparentnost, abychom znovu neobjevovali vymyšlené
- **Programy** - skupina dočasných, vzájemne provázaných projektu rízená jako skupina abychom dosáhli cílu, ktoré projekty sdílí
    - **rízení**
        - správa rizik
        - odstraňovanie obmedzenie a konfliktu z projektu
        - v projektech se premýšlí a plánuje i s ohledem na jiné projekty programu
- **Portfolio** - skupina projektu a programu, rízená k dosažení dlouhodobých strategických cílu
    - a.k.a. co dlouhodobe nabízíme
    - **rízení**
        - monitoringem výkonu firmy
        - výberem a prioritizací programu a projektu

Pre konkrétné projekt je ponapríklad si zvolit vhodný prístup **prediktivní** alebo **agilní** [viz otázka 2](2_softwarove_inzenyrstvi.md).

#### Agilní plánovanie

Dále je ponapríklad u plánovanie projektu sepsat Project Charter popisující základné informace o projektu (proč, co, kdo, kdy, jak, za kolik...), sepsat podrobnosti kľúčových strategií (komunikácia, rizika, kvalita, zmeny) a neakým spôsobem začít plánovat práci (product backlog, riešenie architektúry...).

#### Prediktivní plánovanie

Sepisuje se **Project Initiation Documentation** obsahující detailné Business Case, veškeré informace o projektu (proč, co, kdo, kdy, jak, za kolik), definují se kľúčové strategie (komunikácia, rizika, kvalita, zmeny), vše se dokumentuje, vytvárí se príslušné registry, vše se schvaluje product boardem (zástupci exekutivy, inženýru a zákazníku). Do PID se pak zapisují i zmeny a prubeh, aby bolo možné porovnat plán a realitu, je dostupný všem v rámci projektu.

Delá se detailné analýza požiadaviek, spousta Use case diagramu, detailné rozsah sloužící jako základ pre ocenení, design mockupy. Tvorí se **specifikační dokument** produktu - obsahuje požadavky, rozbití systémov na komponenty (včetne detailního popisu až po pole vstupních formuláru), očekávanou kvalitu, akceptačné kritéria.

Delá se **projektový plán** (proč, co, kdo, kdy, jak, za kolik...) - **Work Breakdown Structure** tvorená ze specifikačního dokumentu, počítá se čas a cena jednotlivých **Work Packages** (součást WBS, nejnižší jednotka) napríklad pomocí [PERT](#program-evaluation-and-review-technique-pert), ich závislosťi, tvoríme rozvrh (gantt/network diagram), prirazujeme odpovednosti (melo by ísť snadno najít aktivity človeka i všechny spojené s aktivitou). 

**Pozor na rozdíl Človekoden (Man-Day / MD) vs. Kalendární čas:** MD je jednotka **úsilí (pracnosti)**, nikoliv času. Úkol o velikosti 10 MD znamená, že zabere 10 dní *jednomu* človeku. Ak na nej nasadíme 5 lidí, muže teoreticky trvat jen 2 kalendární dny. Do kritické cesty (CPM) se vždy dosazuje kalendární *délka trvání*, ne absolutní úsilí. (Pozor na *Brooksuv zákon*: Pridání lidí do zpoždeného SW projektu ho zvyčajne ješte viac zpozdí kvuli režii na komunikaci).

#### Chronologický postup prediktivního plánovanie (Státnicový chyták)
Zkoušející často nachytají studenty na otázke: „Co udeláte pri plánovanie jako první? Gantt, alebo sieťový graf?“ Správná odpoveď je **WBS**. Postup musí ísť striktne v tomto poradie:
1.  **Dekompozice rozsahu (WBS):** Rozbití celého systémov na nejmenší riditelné celky (**Work Packages**). Bez toho nemožno plánovat dál.
2.  **Odhad pracnosti a zdrojov:** Každému Work Package priradíme potrebné úsilí (napr. pomocí PERT) a určíme, kdo ho bude delat.
3.  **Sestavení sieťového grafu:** Definujeme logické závislosťi medzi úkoly (co na co navazuje).
4.  **Výpočet kritické cesty (CPM):** Zjistíme matematické trvání projektu a kritické úkoly.
5.  **Vykreslení do časové osy (Ganttuv diagram):** Teprve na základe všech predchozích krokom/krokov vzniká Gantt jako vizuální kalendární plán.

*WBS*

![](img/20230526000518.png)

### Riadenie rizík

Postup:

1. **Identifikace rizik**
    - čerpáme z predchozích zkušeností, lessons learned... co a proč se stalo?
2. **Ohodnocení rizik**
    - každé riziko spôsobí náklady, môžeme pre nej odhadnout cenu
    - každému priradíme pravdepodobnosť a kritičnost dopadu, určíme následky
      ![](img/20230525214112.png)
3. **Určenie odezev na rizika**, možnosti:
    - **akceptuj** - no tak se to stane, no, nevadí, náklady na prevenci by boli vyšší než samotné riziko
    - **vyhni se** - nastavení plánu, aby problém nemohl nastat (napr. použití jiné technologie, ktorá tento problém nemá)
    - **presuň** (napríklad na nekoho jiného) - napr. tento komponent outsourcujeme se solidním SLA, alebo se pojistíme
    - **zmenši** - sniž pravdepodobnosť/míru dopadu rizika, napríklad dukladnejším systémem reviews
4. **Stanovení monitoringu rizik**
    - stanovení odpovednosti za monitoring rizik
    - určenie, kde budú rizika definovaná, kdy budú revidována a upravována
5. **Vytvorení registru rizik**

Možné zdroje rizik (nejčastejší tučne):

- **používateľ** - **nemožnost/neochota zapojit se**, odpor ke zmenám
- **požadavky** - **špatne pochopené**, blbe definované, nejasné či neadekvátní, **prijdou zmeny** (mnohdy až v momente, kdy mohou zásadne narušit vyvíjený systém)
- **složitost projektu** - komplexné doména, použití nové/nezavedené technologie
- **management** - **neefektivní rízení**, špatne zvolená/použitá metodika/standard, **špatný odhad nákladu/zdrojov/času**, špatne určená komunikácia, **nezkušený manažer**
- **tým** - nezkušenost, **málo lidí**, osobní konflikty
- **firemní prostredia** - nestabilní, zmena vedení...
- **subdodavatelé** - opoždení, nedostatečná kvalita, komunikácia...

#### Specifika prevence u agilního riadenie rizik

Prevence:

- **Transparence a zpetná väzba**, abychom predešli nedorozumení v týmu
- **Používanie user stories** - sú snadno pochopitelné pre zákazníka, dají se dobre overovat
- **Jasná definícia, co znamená "hotovo"**
- **Krátké iterace** - brzo zjistíme, čo je prípadne blbe

### Role modelov v projektovém rízení
V softvérovém projektovém riadenie slouží modely predevším k **odhadovanie pracnosti (effort), času a ceny** projektu na základe historických dát a metrik. Zkoušející chtejí slyšet tyto dva hlavní prístupy:

* **Metoda funkčnéch bodov (Function Points - FP):** Odhaduje velikost SW Z pohľadu používateľa (počet vstupu, výstupu, dotazu, interních súborov). Je nezávislá na technologii.
* **Model COCOMO (Constructive Cost Model) a COCOMO II:** Algoritmetický model, ktorý odhaduje pracnost v človekomesících (Person-Months) a kalendární čas na základe velikosti kódu (KLOC - tisíce rádku kódu) a produktivních faktoru (zkušenost týmu, složitost platformy).

COCOMO rozlišuje **3 vývojové módy (kontexty projektu)**, na ktoré se doc. Ráček velmi často ptá:
1.  **Organic (Organický):** Malé projekty, známé prostredia, malý a zkušený tým, flexibilní požadavky (napr. interné firemní nástroj). Nízká režie rízení.
2.  **Semi-detached (Polorozdelený):** Strední projekty, smíšený tým (zkušení i nezkušení), část požiadaviek je striktní, část volnejší. Vyšší nároky na koordinaci.
3.  **Embedded (Vestavený / Integrovaný):** Komplexné projekty s extrémne prísnými obmedzeniami (napr. riadenie letového prevádzkau, bankovní jádro, embedded medicínský software). Požadavky sú pevné, procesy rigidní, obrovská režie na testovanie a dokumentaci.

Dále sem spadají **matematické modely rízení** (sieťové grafy CPM/PERT), ktoré modelují projekt jako matematický graf a hledají v nem kritická místa (úzká hrdla).

## Ganttovy diagramy, sieťová analýza, metoda kritické cesty (CPM), Program Evaluation and Review Technique (PERT) (2/4)

### Ganttovy diagramy

- nástroj pre plánovanie (nejen) projektu

V základu toto:

![](img/20230525192847.png)

ale možno rozšírit...

- y osa obsahuje úlohy (prípadne zdroje)
- x osa zobrazuje čas
- úloha jako uzel/obdélník (šírka udává časovou náročnost), prípadná hrana značí vztah
- je možné pridat:
    - milestones
    - progress
    - zdroje (kdo co delá, dávají se místo udalostí na osu y), pak rešíme problém plánovanie job-shopu
    - obmedzenie, precedenční podmínky (úloha musí byť započata až po dokončení jiné úlohy, nečo je možné paralelizovat...)
- zvyčajne minimalizujeme makespan (čas dokončení poslední úlohy a teda i celého projektu)

![](img/20230525195955.png)

### Sieťová analýza

Metody pre modelovanie súborov činností vedoucích k dosažení nejakého cíle (tj. projektu).

Cieľom je projekt naplánovat, minimalizovat prostoje a náklady, určiť termíny, celkovou dobu trvání projektu, identifikovat kritické úlohy v projektu.

Používá se pre to sieťový graf hranove/uzlove orientovaný - úlohy sú na hranách/uzlech. Uzlove orientovaný umožňuje snadno modelovat precedenční podmínky, možno snadno použít pre metodu kritické cesty.

* **AON (Activity-on-Node / Uzlove orientovaný):** * **Uzly** predstavují samotné aktivity (činnosti, napr. "Programovanie backendu").
    * **Hrany (šipky)** predstavují logické závislosťi medzi nimi.
    * *Využití:* Mnohem častejší v moderním softwaru (Jira, MS Project), pretože se v nem snadno modelují složitejší závislosťi (napr. SS, FF).
* **AOA (Activity-on-Arrow / Hranove orientovaný):**
    * **Hrany (šipky)** predstavují samotné aktivity, ktoré spotrebovávají čas a zdroje.
    * **Uzly** predstavují **události / milníky (milestones)** – okamžik, kdy jedna činnost končí a druhá začíná (majú nulové trvání).
    * *Využití / Výhoda:* Zkoušející chtejí slyšet, že AOA se skvele hodí pre prirozené zobrazení milníku prímo v grafech. Nekdy vyžaduje zavedení "fiktivních hran" (dummy activities) s nulovým časem pre zachovanie logiky grafu.

### Metoda kritické cesty (CPM)

Metoda pre identifikaci vzájemne závislých aktivit, ktoré majú vliv (sú kritické) na dobu dokončení projektu a nemohou byť opoždeny bez prodloužení dokončení projektu.

#### 4 typy precedenčních závislosťí (Chyták na tabuli)
Pri výpočtu CPM na tabuli vám zkoušející nemusí dát jen klasickou následnost. Musiete znát všechny čtyri typy vazeb:
* **FS (Finish-to-Start / Konec-Start):** Nejbežnejší. Úloha B muže začít až poté, co úloha A skončí (napr. Testovanie začne až po dokončení Implementácia).
* **SS (Start-to-Start / Start-Start):** Úloha B muže začít hned, jakmile začne úloha A. Mohou bežet paralelne (napr. S programovaniem frontendu se muže začít hned, ako sa začne programovat backend).
* **FF (Finish-to-Finish / Konec-Konec):** Úloha B muže skončit až tehdi, kdy skončí úloha A (napr. Dokumentácia celého systémov muže byť hotová/skončená až v momente, kdy skončí implementácia poslední komponenty).
* **SF (Start-to-Finish / Start-Konec):** Velmi vzácná. Úloha B muže skončit až poté, co úloha A začne.

[Postup](https://www.youtube.com/watch?v=4oDLMs11Exs):

- udeláme si graf závislosťí, určíme si dobu trvání aktivit
- v prvním pruchodu jdeme start => konec, rešíme earliest start/completion time. Keď vedou 2 do 1, bereme maximum tech 2.
- v druhém pruchodu jdeme konec => start, rešíme latest completion/start time. Keď vedou 2 z 1, bereme minimum tech 2.
- kritická cesta obsahuje aktivity, ktoré majú earliest & latest finish time identický
- slack/float udává, o kolik môžeme danou aktivitu opozdit, aniž by došlo ke zpoždení projektu (`latest completion time - earliest completion time`)

![](img/20230526101347.png)

### Program Evaluation and Review Technique (PERT)

Technika k odhadu času k dokončení tasku. Bereme **optimistický** odhad, **pesimistický** odhad a **nejpravdepodobnejší** odhad:

`očekávaný = (optimistický + 4 * nejpravdepodobnejší + pesimistický) / 6`

Ak máme informace o úrovni platu implementátoru tasku, môžeme dopočítat odhadovanou cenu.

## Mezinárodní standardy a metodiky projektového riadenie (PMI Project Management Body of Knowledge, PRINCE 2) (3/4)

- standardy projektového riadenie PRINCE2, PMBOK, IPMA ICB popisují obecnejší spôsob rízení
- metodiky sw vývoje (RUP, SCRUM) reší riadenie v rámci vývojového týmu, sú specifické pre vývoj SW

![](img/20230525184623.png)

### PMI Project Management Body of Knowledge (PMBOK)

- **procesne orientovaný** standard, podrobne popsaná sada good practices
- snadno se používá jako handbook pre vhodné znalostní oblasti a nástroje/techniky pri životním cyklu projektu
- vhodný, keď:
    - manažer potrebuje tipy na nástroje a techniky, jaké by mel použít, ale aspoň trochu tuší co a jak

49 procesu (série aktivit s definovanými vstupy, výstupy, nástroji a technikami) delených do:

- **5 procesních skupin** - logické delení procesu popodľa fáz (inicializace, plánovanie, prevedenie, monitoring a rízení, uzavírání)
- **10 vedomostních oblastí/disciplín** projektového managementu, každá má vlastné procesy:
    - **Integrace**
        - tvorba **Project Charter**u:
            - **Business case (proč)** - cíle projektu, hrubá cena, rozpočet, rizika
            - **Project outcome (co)** - popis, hlavní cíle a požadavky
            - **Stakeholders (kdo)** - externé i interné, rešíme ich role, potreby, zapojení a odpovednosti
            - **Management approach (jak)** - popis použitých standardu, nástrojov, metodik, životního cyklu projektu...
            - **Schedule (kdy)** - hrubý plán projektu, fázy, milestones, Ganttuv diagram...
    - **Rozsah (scope)** - sesbírání požiadaviek, definícia, validace a riadenie rozsahu funkcionalit systémov, tvorba Work Breakdown Structure
    - **Plán** - definícia a určenie poradie aktivit, odhady času aktivit, tvorba a riadenie plánu
    - **Cena** - odhad cen a rozpočtu aktivit alebo jednotek práce pomocí Work Breakdown Structure, riadenie ceny a rozpočtu
    - **Kvalita** - plánovanie, riadenie a kontrola kvality
    - **Zdroje** - odhad nepenežních a lidských zdrojov, ich získávanie a rízení, tvorba a správa týmu
    - **Komunikácia** - plán, správa a kontrola komunikácia a informací o projektu
    - **Riziko** - identifikace, kvalitativní (míra dopadu) a kvantitativní (pravdepodobnosť) analýza rizik, ich monitoring, plán a procesy reagující na rizika
    - **Dodavatelé** - produkty a služby pocházející mimo náš tým, kontrakty, objednávky, SLAčka, výber dodavatelu, monitoring výkonu dodavatelu
    - **Stakeholderi** - zúčastnené osoby; ich identifikace, plánovanie a správa zapojení stakeholderu do projektu

### PRINCE 2 (PRojects IN Controlled Environment)

- standard pre riadenie obecného projektu
- predepsaný postup, krok za krokom (spousta formuláru na vyplňovanie, checklisty)
- součástí nie je správa požiadaviek, rozpočtovanie
- vhodný pro:
    - nutnost velkého reportovanie
    - nutnost kompletní projektové dokumentácia
    - tým vyžaduje rád a kontrolu
    - manažery s málo zkušenostmi, hodí se mu podrobný popis postupu

#### Fáze

(hrube odpovídá UP inception, elaboration, construction a transition):

![img.png](img.png)

- **Starting up**
    - tvorba **Project brief**:
        - rešíme feasibilitu, zachycujeme kľúčové požadavky, rizika
        - popis významných požiadaviek s dopadem na architekturu
        - identifikace actoru
        - identifikace dalších systémov, se kterými máme komunikovat
        - na konci známe cíle, hrubou architekturu
        - čo sa používá pre podobné systémy? s čím máme zkušenosti?
        - určenie použitých technologií
        - určenie orientační ceny, časového plánu a rizik
    - plán další fázy:
        - **Work Breakdown Structure**
        - identifikace aktivit, dependencí
        - odhad trvání aktivit, stanovení milestones
        - definícia rolí a odpovedností
        - tvorba rozvrhu (Gantt/sieťový diagram)
- **Initiation**
    - tvorba **Project Initiation Documentation** (dokument/viac dokumentu):
        - obsahuje súčasný stav projektu, plány, Kdo, Co, Kdy, Jak, Proč, Za Kolik...
        - slouží k definici projektu, určenie rámce...
        - schvaluje product board
        - detailné Business Case (dôvody projektu, očekávanie, cost-benefit analýzu, časovou škálu, ceny, rizika)
        - popis struktury managementu, rolí týmu
        - popis prístupu ke kvalite, zmenám, riziku, komunikaci
        - plán projektu
    - plán další fázy
- **Delivery**
    - zvyčajne má viac částí (iterací), každá max 3 mesíce, každá má definované meritelné a overitelné milestones
    - produktový manažer se stará o udržení ceny, termínu, rozsahu a kvality specifikované v PID
    - produktový manažer autorizuje, provádí reviews work packages, reportuje (pravidelne) status, zmeny, problémy a kvalitu výš, spravuje rizika a problémy
    - týmový manažer provádí týmové plánovanie (jednotlivých work packages), demonstruje kvalitu produktu, zajišťuje dodání work packages
    - medzi fázymi se hodnotí končící fázy a plánuje (zase WBS, gantt) další, aktualizuje se PID
- **Close**
    - predání produktu (samozrejme opet spousta protokolu), nasadenie, uzavrení všech dokumentu, PID, dokumentácia, tvorba end report a lessons learned
    - prípadné predání projektu ops a maintenance týmu
    - tvorba SLA

#### 7 principu

(vše máme nejak zdokumentované):

- **Kontinuálné odôvodnení projektu** - proč to deláme?
- **učenia sa ze zkušeností** - co (ne)fungovalo
- **Role a odpovednosti** - presne specifikovaná struktura týmu, vymezené práva a odpovednosti
- **Riadenie po fázch** - po každé fázi deláme review Project brief, provádíme reporting vyššímu managementu
- **Manage by exception** - riadenie soustreďujeme na časti, ktoré se nejak (negativne) vymykají. Nezasahujeme do toho, co funguje. Vytyčíme cíle a tolerovatelné odchylky v kvalite, času, cene a rozsahu, určíme zodpovednosti za neprekračovanie
- **Duraz na produkt** - primárné cieľ je produkt, ne práce
- **Prispôsobení metodiky projektu** - nie je nutné PRINCE používat úplne doslovne, rádek po rádku. Ne všechny formuláre sú vždy úplne relevantní

#### 7 témat

- **Business case** - obsahuje očekávané prínosy, rizika, časový a cenový rozsah, dôvody projektu... Mel by byť neustále aktualizován a držen validní po celou dobu projektu
- **Organizace** - definícia rolí a odpovedností, typy stakeholderu (dodavatel, business/zákazník, používateľ), 3 úrovne managementu (project board pre smerovanie projektu (obsahuje exekutivu, senior suppliera, senior popoužívateľa), project manager pre riadenie projektu, team manager pre dodávanie produktu), manage by exception
- **Kvalita** - monitoring, akceptačné kritéria, určíme si strategii riadenie kvality (nástroje, procesy), rešíme kvalitu produktu i manažerských výtvoru (plány, reporty)
- **Plány** - plánujeme projekt i jednotlivé fázy, Gantt diagram, Work Breakdown Structure je základem plánovanie
- **Rizika** - identifikace možných rizik, určujeme spôsob reakce na dané riziko na základe ceny prevence, pravdepodobnosti a dopadu, uchováváme registr rizik
- **Zmeny** - u požiadaviek na zmenu rešíme prioritu, dopad, kritičnost, zkoumáme možnosti riešenie, podľa zmeny upravujeme záznamy a plán
- **Postup projektu** - porovnáváme realitu s plány (čas, cena, kvalita, rozsah, rizika...), sledujeme či stále projekt splňuje business case

#### 7 procesu

![](img/20230525115631.png)

- **Úplný začátek projektu** - nastínení business case, prirazení kľúčových vedoucích osob, studovanie "lessons learned" predchozích podobných projektu, získanie autorizace product boardu
- **Inicializace projektu** - príprava strategií riadenie (rizik, kvality, komunikácia, konfigurace), projektového plánu, konkretizace business case, založení dokumentácia
- **Riadenie fázy** - reší produktový manažer, monitoring, reportovanie významných udalostí, rídíme exceptions, revidujeme a schvalujeme práci/nové časti produktu
- **Riadenie dodání produktu** - to samé co riadenie fázy, ale reší to týmový manažer
- **Smerovanie projektu** - vysokoúrovňová rozhodnutí, funguje po celou dobu projektu, plán nadcházející fázy, na konci projektu autorizujeme uzavrení
- **Riadenie medzi fázymi (managing a stage boundary)** - plán nadcházející fázy, reší produktový manažer, aktualizace business case a projektového plánu, report predchozí fázy
- **Uzavrení projektu** - reší projektový manažer, evaluace, predání produktu, návrh board na ukončení

### IPMA ICB

*V otázke nie je, ale nie je na škodu znát*

- obecný standard pre vedení projektu
- na rozdíl od vetšiny ostatních obsahuje podrobnou sekci o soft skills
- vhodný, keď:
    - projekt vyžaduje dobré soft-skills (komunikácia, leadership, riešenie konfliktu)
    - manažer je zkušený, zná procesy
    - nie je nutná spousta reportingu
- vhodné pre použití jako handbook pre rôzne manažerské kompetence
- kompetenční prístup, pre každou ICB popisuje požadované dovednosti a schopnosťi, popis a Metriky indikátoru kompetence
  > kompetence je aplikace znalostí (knowledge, informace & zkušenosti), dovedností (skill, schopnosť aplikovat znalosti) a schopnosťí (ability, použití dovedností efektivne, ve správný čas a na správném míste) k dosažení kýženého výsledku
    - kompetence perspektivy - metody a techniky pre interakci jedincu s prostrediam
    - lidské kompetence - techniky pre jednání s jedinci/skupinami
    - praktické kompetence - metody a techniky pre úspech projektu

### Metodiky

Popsány v [otázke 3](2_softwarove_inzenyrstvi.md) (metodiky sw vývoje jako RUP, SCRUM)

## Príklady z praxe pre všetko vyššie uvedené (4/4)

### Specifika IT projektu

v porovnání s vetšinou prumyslových odvetví:

- nepresné/neznámé, časté a menící se požadavky
- vetší nutnost prispôsobení produktu
- velká složitost
- náročné testovanie
- neustálý a rapidní vývoj technologií
- možnost globálné spolupráce
- projekty mohou v rámci portfolia ovlivnit ostatné projekty (zvlášť pri zlyhania)
- nutnost riadenie rizik
- dokončené projekty je často napríklad servisovat/poskytovat podporu

### IT Infrastructure Library (ITIL)

Best practices pro **riadenie IT služeb**:

**Fáze:**
- **Service strategy** - požadavky, strategie pre zabezpečenie kýženého, finance, co vlastne budeme delat
- **Service design** - Service Level Agreement, riešenie rizik, security & business compliance
- **Service transition** - ako meníme stávající služby, riešenie deploymentu, uložení získaných znalostí pre budúcí projekty
- **Service operation** - dokumentácia pre popopoužívateľa/helpdesk, riešenie incidentu/zmenových požiadaviek/problému, riešenie identit a prístupu k systémov
- **Continual service improvement** - monitoring, protokolovanie, aktualizace bežící služby

### Praktické príklady aplikace

#### Príklad použití CPM v praxi

**Situace:** Vývoj webové aplikace pre e-commerce

**Aktivity a závislosťi:**
- A: Analýza požiadaviek (5 dní)
- B: Design Databázy (3 dní, po A)
- C: Design UI/UX (4 dny, po A)
- D: Implementácia backend (8 dní, po B)
- E: Implementácia frontend (6 dní, po C)
- F: Integrace (3 dny, po D a E)
- G: Testovanie (4 dny, po F)

**Kritická cesta:** A → B → D → F → G (23 dní)
**Slack:** C a E majú 2 dny slack

#### Príklad PERT odhadu

**Task:** Implementácia platebního systémov

- **Optimistický odhad:** 8 dní (vše jde hladce)
- **Nejpravdepodobnejší:** 12 dní (standardní prubeh)
- **Pesimistický:** 20 dní (komplikace s API, Bezpečnosť)

**PERT odhad:** (8 + 4×12 + 20) / 6 = 76/6 ≈ 12,7 dní

[Go to the next question](./4_dátabaze.md)
