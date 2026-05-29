# Softvérové inžinierstvo

> Životný cyklus SW, proces vývoja a riadenie softvérového vývoja. Metodika (Rational) Unified Process (UP, RUP), agilné metodiky a principy agilného vývoja SW. Nasadenie a prevádzka softvérových systémov. Údržba softvérových systémov, opätovná použiteľnosť. Príklady z praxe pre všetko vyššie uvedené. (PA017)

1. [Životný cyklus sw, proces vývoja a riadenie softvérového vývoja (1/5)](#životní-cyklus-sw-proces-vývoje-a-rízení-softvérového-vývoje-15)
2. [Metodika (Rational) Unified Process (UP, RUP) (2/5)](#metodika-rational-unified-process-up-rup-25)
3. [Agilné metodiky a principy agilného vývoja SW (3/5)](#agilní-metodiky-a-principy-agilního-vývoje-sw-35)
4. [Nasadenie a prevádzka softvérových systémov (4/5)](#nasadenie-a-prevádzka-softvérových-systémov-45)
5. [Údržba softvérových systémov, opätovná použiteľnosť (5/5)](#údržba-softvérových-systémov-opätovná použiteľnosť-55)

## Životný cyklus sw, proces vývoja a riadenie softvérového vývoja (1/5)

Vždy neakým spôsobem obsahuje fázy analýza, návrh, implementácia, testovanie a prevádzka (včetne nasadenie). Rozdiely sú v tom, či a akým spôsobem delíme projekt na uchopiteľnejšie časti. Dôsledkom toho sú i rôzne spôsoby, akým se vývoj rídí.

Existuje niekoľko základnéch modelov:

### Vodopádový model

Skladá se z:
- **Analýza**
    - zber požiadaviek klienta
    - Je duležité rozlišovat medzi tým, co hovorí, že potrebuje, a co skutočne potrebuje. Pre lepšiu predstavu môžeme sledovať, ako koncový používateľ pracuje se súčasným riešením.
    - zaujíma nás **co** a **proč**, často ale klient zmieňuje **jak**. V takých prípadech je duležité se pýtať **proč**. Môže ísť o legitimní dôvod, ale tiež napríklad o nevedomosť. => studie uskutočniteľnosti, dokument požiadaviek...
- **Návrh**
    - návrh architektúry, jednotek, výber technologií, plán testovanie => diagramy (uml), wireframy, prototypy
- **Implementácia**
    - tvorba systémov podľa návrhu
- **Testovanie**
- **Provoz**

tj. nejprve sesbíráme všechny požadavky, pak sw jako celek postupne navrhneme, implementujeme, otestujeme a nasadíme

**Výhody:**
- jednoduchý na rízení
- ak vše jde hladce, je to nejlevnejší spôsob

**Nevýhody:**
- vetšinou všechno nejde hladce
- špatne se reaguje na zmeny (musíme se vracet do predchozích fáz modelov)
- zákazník predem nedokáže presne a úplne definovat, co potrebuje
- v praxi nesú kroky v tomto poradie dodržovány (testovat chceme ideálne počas vývoja, neco chceme ukázat netrpelivému zákazníkovi...)

### Inkrementálné model

- Projekt se rozdelí na inkrementy, časti, ktoré budú vyvíjeny a dodávány postupne, pre každý si udeláme jednoduchou rámcovou analýzu
- Inkrementy se vyvíjí v poradie popodľa priority
- Po nasadenie do systémov máme o inkrementu od zákazníka zpetnou vazbu

**Výhody:**
- Systém je dodáván po častiach, celkové náklady sú distribuovány
- Nie je ponapríklad vytváret velký tým, pretože práce je dodávaná po častiach
- Používateľ vidí systém v raných fázch projektu. Možno rychle reagovat na zpetnou vazbu používateľa
- O nutnosti zmeny se dozvíme dríve a jej zavedení bude levnejší (nie je napríklad vše prekopávat, pridáme zmenový inkrement)

**Nevýhody:**
- Náklady na vývoj sú vysoké kvuli dodávce systémov po častiach
- Model vyžaduje náročné plánovanie k distribuci práce
- Pre pripojení modulu vyvinutých s každou fáz je nezbytné dukladne popsat rozhrania

### Spirála

![](img/20230607122950.png)

- kombinace iterací a vodopádu, duraz na analýzu rizik
- vývoj probíhá v cyklech, každý má niekoľko fáz

**Fáze:**
- **Analýza**
- **Návrh**
- **Implementácia**
- **Testovanie, zpetná väzba a plán dalšího cyklu** - zpetnou vazbu používáme pre práci v dalším cyklu

- oproti inkrementálnímu modelov nemusíme mať po každé iteraci hotovou část nasazeného systémov (inkrement je napríklad ve forme jasných požiadaviek, návrhu systémov, alebo tak).
- cykly aplikujeme i na jednotlivé fázy vodopádu
- lépe pracujeme s nejistotou, ale trvá to déle

### Prototypovanie

- vytvoríme prototyp systémov, abychom porozumeli, akým spôsobem chce zákazník systém používat a co od nej očekává
- po analýze prototypu ho zahodíme a začneme práci na reálném systémov, využijeme vhodný model

### Model výzkumník

- navrhni systém a implementuj ho. Vyhovuje? Super. Nevyhovuje? Zpet k návrhu/implementaci
- nemožno porádne rídit, neexistuje dokumentácia, rešitelé sú obtížne nahraditelní, jde o experimentovanie

### V-model

![](img/vmodel.png)

- ala vodopád, ale zobrazuje i rôzne testy k fázm (jednotkové, integračné, systémové, popopoužívateľské, akceptačné...)

1. Požadavky / Use Casy $\rightarrow$ Validují se pomocí Akceptačnéch testu (overenie se zákazníkem, či systém delá to, co mel).
2. Analýza systémov / Architektúra $\rightarrow$ Verifikuje se pomocí Systémových testu (testuje se systém jako celek, včetne nefunkčnéch požiadaviek jako výkon či Bezpečnosť).
3. Detailné návrh (komponenty a subsystémy) $\rightarrow$ Overuje se pomocí Integračnéch testu (či komponenty pres definovaná rozhrania správne spolupracují).
4. Implementácia (trídy a metody) $\rightarrow$ Pokrývá se pomocí Jednotkových testu (Unit testy prímo nad kódem).

Nezávisle na modelov je duležité nastavit správnou komunikaci, definovat a používat jednotný jazyk. Ak chceme cokoliv rídit, je ponapríklad mať informace o aktuálním stavu, dodržiavanie plánu, očekávaných zmenách, problémech...

Hlavní metodiky riadenie sw projektu sú **prediktivní metodiky (napr. RUP)** a **agilní (napr. SCRUM)**.

## Metodika (Rational) Unified Process (UP, RUP) (2/5)

Pri popisu charakteristického RUP/UP diagramu (tzv. hump chart alebo vlnový diagram) chtejí zkoušející slyšet, že diagram zachycuje dve dimenze vývoje softwaru:

**Sloupečky (Dimenze časová / dynamická)**: Predstavují časovou osu projektu rozdelenou do 4 hlavních fáz (Inception, Elaboration, Construction, Transition), pričemž každá fázy se dál delí na jednotlivé iterace.

**Státnicový chyták:** Fáze nesú totéž čo jedna iterace! Fáze pokrývají celý životný cyklus projektu od začátku do konce a každá z nich se skládá z jedné či viac dílčích iterací.

**Řádky (Dimenze obsahová / statická)**: Predstavují jednotlivé disciplíny / workflows (napr. Business Modeling, Requirements, Analysis & Design, Implementation, Test, Deployment a podpurné disciplíny jako Configuration & Change Management, Project Management, Environment).

**Vlnovky (Humps)**: Výška plochy v daném míste vyjadruje intenzitu úsilí/práce, kterou tým konkrétné disciplíne v dané iteraci venuje. Napríklad v rané fázi Inception je vlnovka u disciplíny Requirements velmi vysoká, zatiaľ čo u Implementation je témer nulová. V prubehu Construction se tento pomer obrací.

- rigidní, duraz na procesy
- vhodná, ak máme jasné a pevné požadavky, variabilní aspekty mohou byť čas a zdroje
- vyžaduje podstatné plánovanie predem
- iterativní a inkrementálné, jednotlivé aktivity (plánovanie, požadavky, modelovanie, návrh, vývoj, testovanie, nasadenie...) se částečne prekrývají
- rízena riziky, use-case požadavky
- Architektúra je stredobodem - existuje architektonický tým, se kterým ostatné týmy konzultují prípadné nejasnosti/problémy, slouží jako centrálné komunikačné uzel (lepší, než kdyby spousta dev týmu komunikovala navzájem)
- umožňuje pevnou kontrolu nad procesy a týmem
- vhodná, ak potrebujeme porádnou dokumentaci (UML diagramy)
- hodí se pre velké a heterogenní produkty, velké týmy...

**Výhody:**
- zákazník nie je počas vývoja ponapríklad, definícia produktu je zakotvena v kontraktu (presne ví, co dostane)

**Nevýhody:**
- pracujeme s fixními deadliny, rozpočtem i funkcionalitou
    - v reálu se deadline a rozpočet muže lehce menit v závislosťi na vývoji
- zmenové požadavky sú problém
- ponapríklad viac času k plánovanie
- složitý kontrakt, je napríklad myslet na všechno (exhaustive kritéria prijetí, penále...)

![](img/20230523215135.png)

### Fáze iterací

Iterace sú seskupovány do fáz:

#### Inception (1 iterace)
- rešíme feasibilitu, zachycujeme kľúčové požadavky, rizika
- popis významných požiadaviek s dopadem na architekturu
- identifikace actoru
- identifikace dalších systémov, se kterými máme komunikovat
- na konci známe cíle, hrubou architekturu
- čo sa používá pre podobné systémy? s čím máme zkušenosti?
- určenie použitých technologií
- určenie orientační ceny, časového plánu a rizik => **Project brief**

#### Elaboration (2 iterace)
- rešíme požadavky, architekturu, hrajeme si s UML diagramy
- na konci máme architekturu, návrh systémov reflektující požadavky

#### Construction (4 iterace)
- tvoríme systém, testujeme, nasazujeme
- na konci máme beta verzi, relativne stabilní a otestovanou, pripravenou k použití

#### Transition (2 iterace)
- hledáme a opravujeme chyby, deláme manuály, poskytujeme konzultace
- testovanie s používateľmi (beta, na základe feedbacku deláme zmenové požadavky), akceptačné testy

### Workflows a UML diagramy

Iterace by nemela prekročit 3 mesíce, prínos iterace je **inkrement**, každá iterace obsahuje workflows, ktoré sú viac či méne prítomné. Pre každé workflow se používají určiťé UML diagramy:

- **Business modelovanie**
    - **activity diagram** - popisuje obchodní procesy, ktoré se majú rešit
- **Požadavky**
    - **use case diagram** - definuje hranice systémov, aktory a ich interakce s funkcionalitou systémov
- **Analýza a návrh**
    - **sequence diagram** - Interakční diagramy, ktoré ukazují, ako si objekty medzi sebou posílají zprávy, aby realizovaly konkrétné scénár z Use Case diagramu.
    - **class diagram** - Zobrazuje kľúčové pojmy z reálného sveta a vztahy medzi nimi (napr. Zákazník, Objednávka, Faktura), bez programátorských detailu.
- **Implementácia**
    - **class diagram** - Už obsahuje konkrétné datové typy, viditelnosti (public/private) a metody, ze kterých možno prímo generovat kód.
    - **component diagrams** - Ukazuje fyzické usporádání kódu – moduly, knihovny (JAR, DLL), zdrojové soubory a ich vzájemné závislosťi.
- **Testovanie**
    - **use case** - Slouží jako prímý podklad pre akceptačné testy (Acceptance Tests) a systémové funkčné testy
    - **class diagram** - Základné stavební kámen pre vývojáre pri psaní jednotkových testu (Unit Tests)
    **activity diagrams** - Vynikající podklad pre tvorbu integračnéch a end-to-end (E2E) testu
- **Deployment**
    - **deployment diagram** - zobrazuje fyzické usporádání systémov – servery, Databázy, sieťové prvky a ako sú medzi sebou propojené

RUP je konkrétné komerční metodika stavející na UP (pridává napríklad jednotlivé role a odpovednosti v týmu, konkrétné postupy...), UP je obecný rámec.

**Iterativní vývoj (Evoluce celku):** Vývoj probíhá v opakovaných cyklech (iteráciach). V každé iteraci se bere v úvahu celý systém (alebo jeho podstatná část) a ten se postupne zahušťuje, vylepšuje a zpresňuje.

**Metafora:** Jako keď malír nejdrív naskicuje celou kompozici uhlem na celé plátno, pak v další iteraci pridá základné barvy všude a v poslednej iteraci vykresluje detaily. V UP to odpovídá napr. fázi Elaboration, kde se definuje a overuje Architektúra celého systémov na základe kľúčových use casu.

**Inkrementálné vývoj (Stavba po kusech):** Systém se vyvíjí a dodává po samostatných, kompletne dokončených častiach – prírustcích (inkrementech).

**Metafora:** Jako keď stavíš dum pokoj po pokoji – nejdríve kompletne postavíš, vymaluješ a vybavíš kuchyň, pak obývák, pak ložnici. V UP to odpovídá fázi Construction, kde se v každé iteraci implementují a dokončují konkrétné sady funkcionalit.

**Propojení v UP:** UP je iterativní i inkrementálné zároveň. Je iterativní, pretože v každé jednotlivé iteraci tým prochází všemi disciplínami (od analýzy pres kódovanie po testovanie) a produkt se evolučne zpresňuje. Je inkrementálné, pretože výstupem každé dokončené iterace musí byť spustitelný, otestovaný a stabilní prírustek kódu (executable architecture/increment), ktorý rozširuje predchozí verzi.

## Agilné metodiky a principy agilného vývoja SW (3/5)

- flexibilní, duraz na lidi
- radši budeme reagovat na zmenu, než se pevne držet plánu
- snažíme se fixovat čas a zdroje, promenlivá muže byť funkcionalita (*Postavili jsme dum a plot, v rozpočtu zbývají zdroje na garáž, alebo bazén. Co z toho chcete?*)
- vhodná, ak se požadavky mení, nie je jasná kýžená výsledná podoba systémov, alebo zákazník požaduje neco hmatatelného relativne brzo => nie je presné dátamm dokončení
- vyžaduje minimálné plánovanie predem
- kľúčová je dobrá komunikácia a spolupráce týmu
- automatizované testovanie
- variabilita funkcionality (vývoj postupuje tak, že keď dojde čas/peníze, tak se ptáme zákazníka, či neco prihodí, alebo či vyškrtneme nejakou část systémov)
- face-to-face komunikácia, rychlé meetingy - rychlejší, získáme lepší porozumení
- jednoduchá dokumentácia - dokumentácia težko udržuje tempo s realitou, proto ji držme co nejjednodušší, ideálne navázanou na kód
- častá setkání se stakeholdery (sprint review), prezentace nové funkcionality (lepší, než jen popis)

### Príklady agilních metodik

#### Extreme programming
- osvedčené postupy tahá do extrému (osvedčují se reviews? => delej reviews co to jde)
- párové programovanie, duraz na testy, refaktorizaci, kód je single source of truth (dokumentaci generujeme z kódu, používáme schéma pre generovanie ostatních vecí...)
- rychlá zpetná väzba, duraz na jednoduchosť, malé inkrementy

### SCRUM

- nejčasteji využívaná agilní metodika
- iterativní, inkrementálné
- jednoduchý, očekává se použití i dalších nástrojov/procesu
- vhodný pre menší týmy (<=15 lidí)
- hodí se, keď máme tým schopný samostatnejší práce, potrebujeme rychle vytvorit aspoň nejaký produkt

#### Role

- **product owner** - reprezentuje stakeholdery, má nejvetší prehled o požadavcích na produkt, spravuje product backlog
- **scrum master** - zodpovedný za dodržiavanie scrumu, reší procesy
- **tým vývojáru** - 3-9 lidí, sobestačný (má lidi na všechno) a sebeorganizující se, spravují sprint backlog, zodpovedný za doručenie produktu

#### Artefakty

##### Product backlog
- obsahuje veškerou zbývající požadovanou funkcionalitu ve forme **user stories**
    - jednotka funkcionality, testovatelná, logický celek
    - každé story má:
        - **story points** reprezentující časovou náročnost odhadnutou pomocí [planning pokeru](#planning-poker)
        - akceptačné kritéria (testovatelná, formulovaná jako Given ... When ... Then ...)
        - muže mať seznam rizik
        - stories majú prioritu (MoSCoW) podľa hodnoty, náročnosti, rizika, prínosu...
            - Must - nezbytné
            - Should - melo by byť
            - Could - bolo by fajn
            - Won't/Wish - zapomeň na to, možná jindy
        - pre testovanie je možné použít Gherkin/Cucumber (As a ... I can ... So that ...)

- tvoren celým scrum týmem, spravuje ho product owner
- v praxi jde o tabuli (reálnou/virtuálné) se sticky notes

##### Sprint backlog
- část product backlogu (množina user stories), ktorá se má provést v daném sprintu
- stories sú rozdeleny na jednotlivé tasky, u každého je určen časový odhad v hodinách
- task má fázy Todo, In progress a Done
- tasky si k práci vybírají vývojári podľa vlastního uvážení, ale žádné (ani user stories) nemohou byť v rámci sprintu pridány/odebrány
    - bolo by nutné zrušit celý sprint product ownerem
- spravován týmem vývojáru

##### Product increment
- všechny predmety product backlogu, ktoré se splní behem sprintu (a.k.a. to, čo sa za sprint stihne/udelá)
- tvoren týmem vývojáru, testován zákazníkem, muže byť released product ownerem
- je nutné, aby bol použiteľný a bol splnen (podľa definícia scrum týmu)

#### Události

##### Project planning
- tvorba [project charteru](3_projektove_rizeni.md#pmi-project-management-body-of-knowledge-pmbok)
- tvorba product backlogu
- výber kľúčových strategií (komunikácia, rizika, riadenie zmen, kvalita...)

##### Sprint planning
- probíhá na začátku sprintu, cca 8 hodin
- účastní se celý scrum tým
- vytyčuje se cieľ nadcházejícího sprintu (a.k.a. co chceme udelat), vybíráme veci z product backlogu a prirazujeme jim tasky

##### Sprint
- iterace soustredená na vývoj funkcionality v sprint backlogu, cieľom je vytvorit použiteľný a potenciálne vydatelný product increment
- pracuje na nem celý scrum team
- product owner reší komunikaci, vývojári vývojárí, scrum master sleduje dodržiavanie procesu
- analýza, návrh, implementácia, testovanie
- max 1 mesíc, všechny sprinty trvají stejnou dobu
- po sprintu sledujeme [team velocity](#team-velocity), popodľa ní máme lepší odhad pre budúcí plány, možno popodľa ní upravit rozsah sprint backlogu

##### Daily scrum (standup)
- 15 minut každý den, účastní se vývojári a možná i scrum master
- co jsem delal včera, co budu delat dneska, narazil jsem na nejaké problémy?

##### Sprint review
- 4 hodiny, účastní se celý scrum team a kľúčoví stakeholderi (napr. zákazník, používateľ)
- probehne predvedení inkrementu
- proberou se prípadné problémy, zmeny, odpovídá se na prípadné otázky stakeholderu
- proberou se prípadné zmeny product backlogu
- prípadne se prepočítá predpokládané dátamm dokončení
- probere se, co by se melo delat dál, upraví se priorita/poradie v product backlogu

##### Sprint retrospective
- 3 hodiny, účastní se scrum team
- reší se procesy - rozložení práce, splnil se cieľ, je napríklad neco upravit?
- reší se vztahy - klapalo to? potrebuje nekdo užší spolupráci?
- reší se nástroje - dobrá komunikácia? dostatečná transparentnost?
- reší se lidi - mel nekdo trable? nekoho pochválíme?
- co nefungovalo, co môžeme zlepšit
- ideálne se vymyslí jedno zlepšenie procesu, ktoré se v príštím sprintu bude používat
- prípadne se upraví kľúčové strategie, rizika

##### Project retrospective
- uzavrení projektu s týmem
- rešíme lessons learned, čo sa povedlo, nepovedlo...
- podekujeme všem

#### Ukončení SCRUM

SCRUM muže skončit, keď:
- product backlog je prázdný (vše hotovo), alebo nepovažujeme (společne se stakeholdery) jeho obsah za duležitý
- dojde čas/peníze
- udelali jsme poslední sprint a je sice co spravovat, ale defekty sú prijatelné
- product owner/stakeholder se rozhodne ukončit projekt

#### Další aspekty SCRUM

- návrh a Architektúra se mohou delat prubežne pre jednotlivé user stories, alebo se do procesu zavádí jako standard (napr. používáme vrstvenou architekturu, používáme tyto technologie...)
- kontrakt se zvyčajne určuje popodľa toho, kolik (a jakých) lidí bude za dané období na projektu pracovat
    - super na flexibilitu, ale težko se určuje výsledná cena/deadline
- zákazník je zatažen do postupu vývoje, muže hned dávat zpetnou vazbu, ale tento overhead vyžaduje extra čas
- balancuje se Čas, Cena a Rozsah funkcionalit

### Burndown chart

Ukazuje kolik práce zbývá a ako si vedeme oproti plánu:

![](img/20230525221317.png)

### Team velocity

Dokončené story pointy za sprint, je videt v Burndown Chartu v dy/dx, alebo jako samostatná krivka:

![](img/20230525221638.png)

### Planning poker

Pre každé story každý z týmu provede odhad, odhady se zverejní najednou. Následuje diskuze, dokud se na bodech za dané story všichni neshodnou (doporučené použité body sú popodľa Fibonacciho posloupnosti).

### SCRUM Board

Viditelný celému týmu, na jednotlivých lístcích tasku je videt i zpracovávající človek:

![](img/20230525224009.png)

## Nasadenie a prevádzka softvérových systémov (4/5)

- pred nasadeniem je duležité systém otestovat v prostredia, ktoré bude co nejbližší tomu produkčnímu
- kľúčové je v prevádzkau protokolovanie udalostí (abychom v prípade chyby vedeli, čo sa v systémov delo), monitoring, systém zpetné väzby
- nasadenie zahrnuje prípravu prostredia (instalace os, databáz...), možno automatizovat/zjednodušit použitím Platform as a Service, prípadne kubernetes
- pred nasadeniem do prevádzkau je fajn projít a zkontrolovat dokumentaci, ktorá muže byť kvuli vývoji neaktuální
- součástí nasadenie je i školení používateľu, abychom predešli neúspechu z dôvodu neochoty/neznalosti používanie
- součástí nasadenie muže byť i customizace systémov pre specifické potreby zákazníka (ak to náš systém umožňuje)

## Údržba softvérových systémov, opätovná použiteľnosť (5/5)

### Analýza projektu

V záveru je fajn si udelat analýzu toho, co (ne)fungovalo, co zlepšit...
- dosažená produktivita a kvalita
- použitý proces, odchylky, dôvody
- plán vs realita a dôvody (čas, peníze, chyby, FP/LOC...)
- rizika (plán vs realita, ako jsme rešili rizika a problémy)
- pracnost (i podľa etap)
- souhrn defektov
- kauzální analýza - analýza odchylek výkonu u použitého procesu (ako a proč)
- použité technologie a ich hodnocení
- popsat v dokumentu tým a jednotlivce, na ktoré je možné se prípadne obrátit (napríklad keď se reší problém v dalším projektu)
- aktiva procesu - co vzniklo a muže byť použito i v jiných projektech (napríklad knihovny, checklisty...)

### Údržba systémov

- údržba se muže delat jako samostatný projekt, mohou na to byť specializované týmy
- reší se oprava (i bezpečnosťních) chýb, aktualizace a vylepšení (ideálne neakým spôsobem automatizované, ale muže byť fajn potvrdenie používateľa), správu zmen (čo sa ako a proč zmenilo)
- opätovná použiteľnosť se zvyčajne reší v rámci jednotlivých služeb/programu/komponent, ale ne znovupoužitím struktur medzi rôznymi projekty (ak nejde o specializovanou knihovnu) - mohli bychom mať problém v prípade zmeny

[Go to the next question](./3_projektove_rizeni.md)
