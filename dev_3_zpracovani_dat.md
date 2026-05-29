# Spracovanie dát

> Základné pojmy a principy dátových skladu, datové analytiky a business intelligence. Životný cyklus dátového skladu. Analytika velkých dát, jazyky pre realizaci analytický úloh, analytika na úrovni databáz. Pokročilé techniky Spracovanie dát, výkonnosťní aspekty Spracovanie velkých dát. Príklady z praxe pre všetko vyššie uvedené. (PA036, PA220 || PA212)

1. [Základné pojmy a principy dátových skladu, datové analytiky a business intelligence (1/5)](#základné-pojmy-a-principy-dátových-skladu-datové-analytiky-a-business-intelligence-15)
2. [Životný cyklus dátového skladu (2/5)](#životní-cyklus-dátového-skladu-25)
3. [Analytika velkých dát, jazyky pre realizaci analytických úloh, analytika na úrovni databáz (3/5)](#analytika-velkých-dát-jazyky-pro-realizaci-analytických-úloh-analytika-na-úrovni-databáz-35)
4. [Pokročilé techniky Spracovanie dát, výkonnosťní aspekty Spracovanie velkých dát (4/5)](#pokročilé-techniky-Spracovanie-dát-výkonnosťní-aspekty-Spracovanie-velkých-dát-45)

## Základné pojmy a principy dátových skladu, datové analytiky a business intelligence (1/5)

### Business intelligence

- procesy a nástroje pre zber, analýzu a prezentaci/vizualizaci dát za účelem asistence pri tvorbe informovaných rozhodnutí v podnikovém rízení
- umožňuje transformaci dát do informací
- jádrem je **datový sklad**

### OLTP (online transaction processing)
- spôsob ukladanie dát v db pre transakční Spracovanie
- dáta v databázi se mení, cieľom je zajistit konzistenci a umožnit CRUD
- nutné zamykanie tabulek/rádku pre zabezpečenie konzistencia
- vhodné pre uložení dát v operativním prevádzkau podniku (zaujíma nás, čo máme na sklade, jaká je aktuálné cena produktu...)
- normalizovaná forma (nie je datová redundance, používají se public keys pre prípadné spojovanie dát)
- používané queries známe dopredu

### OLAP (online analytical processing)
- spôsob ukladanie dát pre analytické Spracovanie
- dáta v databázi se nemení
- zamykanie nie je napríklad, dáta se nemodifikují
- pracujeme s mnohem vetším objemem dát
- vhodné pre dlouhodobé uložení dát, reflektuje historii dát z produkční Databázy a ich vývoj v čase
- denormalizovaná forma, hodne indexu, snažíme se minimalizovat nutné joiny, nevadí datová redundance
- **hvezdicové schéma/dimenzionální modelovanie** - stredobodem je vždy nejaký subjekt (obsahující fakta napr. prodej) s **tabulkou faktu** (obsahující konkrétné záznamy meranie), ke ktoré se pomocí referencí (foreign key) vážou **tabulky dimenzí** (často odpovedi na otázky KDO, KDY, KDE, JAK..., zvyčajne detailné (denormalizované) pre snadnou analytiku, redundance nevadí, napr. dátamm delíme na den, mesíc, rok, den v týdnu, kvartál... môžeme mať separé date i time dimenze, zvyčajne 4-15). Čím viac dimenzí máme, tým viac/konkrétneji se môžeme DW dotazovat (dimenze tvorí kontext). Tabulky dimenzí zvyčajne predvyplníme (pre dátamm môžeme použít numerický prepis dáta, napr. 20230621), rozlišujeme dimenze dáta a času. Jako stežejní dáta (to, čo nás zaujíma) bereme fakta, dimenze sú popisná dáta k faktum, popodľa kterých je možné seskupovat. Reference sú jen v tabulce faktu. ID pre tabulky (surrogate keys, int) dimenzí si generujeme sami, abychom neboli limitováni použitými kľúči z OLTP.
  ![](img/20230611150321.png)
- typy faktu:
    - **transakční** - událost spojená s hodnotou (napr. nákup)
    - **snapshot** - zachycující nejakou aktuálné hodnotu (napr. naplnenost skladu)
    - **bez hodnoty** - fakt nemá žádnou numerickou hodnotu, zvyčajne jde o nejakou událost (napr. click na určiťý prvek)
      Za fakty se považujú i odvozená dáta (napr. kumulativní hodnoty za nejaké období), alebo dáta kombinovaná z viac procesu (napr. prodeje a ich predpovedi pre dané období). Ty zvyčajne neukládáme do tabulky faktu (ale muže to mať své opodstatnení, napríklad pre zrychlení dotazu)
- nevadí nám drobná neaktuálnost dát
- query neznáme dopredu, záleží na tom, co chceme zjistit
  ![](img/20230610171630.png)

**Snowflake schema** - star schema, kde dimenze majú hloubku (obsahují reference na další tabulky, napr. obsahující month ID a month name). Zpusobují performance problémy, jde o antipattern.

![](img/20230611150909.png)

**Granularita** popisuje, z jaké úrovne se na fakta díváme (napr. zaujíma nás, kolik se prodalo daného produktu? Za jeden den? V konkrétním obchode?). Nejnižší granularita je jeden fakt (ukládáme opravdu fakty, alebo napríklad jen agregovaná dáta?).

**Meranie/Measure** - aspekt faktu, ktorý nás zaujíma, možno agregovat (napr. cena prodeje). Nektoré hodnoty meranie možno sčítat (napr. tržby), nektoré jen v nekterých dimenzích (napr. zustatek na pokladnách, nemožno sčítat v čase), nektoré vubec (napr. cena za jednotku produktu alebo priemerná cena za období...)

**Conformed (prispôsobivá?) dimension** - dimenze, ktorá má rovnaké hodnoty a význam pre dáta pocházející z viac zdrojov. Napr. čas je zvyčajne conformed dimenze, pobočka nemusí byť (pod jakou pobočku by spadal prodej pres internet?).

### Datový sklad

- OLAP
- oddelení od OLTP, abychom nezatežovali produkční db
- zvyčajne 1 db fungující jako centrálné zdroj pravdy pre analýzu a reporting
- dáta ve skladu se nemení, iba pridávají, je videt vývoj dát v čase
- muže obsahovat dáta z viac zdrojov
- vyžaduje, aby bola zdrojová dáta očištena a konzistentne uložena
- možno využít standardní databázi (napr. postgres), alebo specializovaná riešenie (napr. Google BigQuery, Teradáta)
- jednoduchá reprezentace dát, aby s nimi mohli pracovat analytici a bolo umožneno používat jednoduché analytické dotazy (s minimem joinu)
- cieľom je umožnit a zjednodušit analýzu dát

### Data mart

- malý dáta warehouse, soustredí se na jednu zájmovou jednotku (napr. objednávky)
- cieľom je dekompozice za účelem zvýšení efektivity/obmedzenie prístupu do jednotlivých částí dátového skladu
- mohou byť dve podoby:
    - **Nezávislé dáta marty** - nemáme žádný centrálné zdroj pravdy (DW), dáta do dáta martu jdou prímo ze zdrojov
    - **Logické dáta marty** - dáta marty fungují jako logické pohledy na část dátového skladu, jednoduchší na údržbu

### Data Cube

- obsah DW, umožňuje pohled na dáta z rôznych dimenzí (rozmeru kostky, zvyčajne 4-15)
- skládá se z bunek (cells) - každá je kombinací hodnot dimenzí. No dáta = prázdná buňka.
- **Dense/sparse cube** - hodne/málo neprázdných bunek v dáta cube

Na datový sklad/dáta marty sú zvyčajne napojeny další **vizualizační aplikace** (napr. Grafana, Kibana, PowerBI, alebo napríklad R project)

## Životný cyklus dátového skladu (2/5)

Životný cyklus:

- **Určenie cíle a plánovanie** - co od systémov očekáváme, jaký rozsah dát nás zaujíma, odhad ceny, rizik, prioritizace subjektu (=> dátamartu)
- **Návrh infrastruktury** - voľba vhodných nástrojov a technologií, architektonických riešenie
- **Návrh a vývoj dáta martu** - iterativne tvoríme dáta marty, každý zapojujeme do DW systémov
    - **voľba procesu** - včetne modelovanie procesu (napríklad UML diagramem, alebo BPMN), napr. prodeje
    - **určenie granularity** - napr. prodej jednoho produktu (jedné položky z objednávky) jednomu zákazníkovi, na jedné pobočce v jeden moment
    - **identifikace dimenzí** - vychází z granularity, môžeme dimenze rozšírit o další jevy (napr. den v týdnu, slevové akce...)
    - **identifikace faktu** - všech sloupcu, ktoré budú v tabulce faktu (napr. cena jednotky produktu, prodané množství)
    - čištení dát a ich pridání do DW systémov
- **ETL (Extract, Transform, Load)** - v prubehu života do skladu pribývají dáta, ktoré je vždy napríklad:
    - **extrahovat** z dátových zdrojov (napr. produkční db)
    - **transformovat**
        - odstranit duplicity
        - upravit, aby odpovídala jednotnému stylu v DW, učesat do formátu používaném v DW
        - vyčistit od nekompletních dát/chýb (spelling errors)
        - občas muže byť napríklad rozbít dáta na viac sloupcu (name => first name, last name)
        - možno částečne automatizovat, ale mnohdy sú napríklad manuální zásahy
        - zvyčajne nevkládáme prímo do dw, ale do staging table (muže byť csv ve formátu dw tabulek)
        - je fajn delat po častiach, ať se do toho nezamotáme
    - **naplnit** (load) do DW
        - nejprve aktualizujeme dimenze (abychom meli k dispozici foreign keys), pak fakta
        - upsert (update, insert if not exists) je často drahý -> je fajn detekovat neexistující, pak vložit nové, a pak updatovat
        - je fajn naplňovat po velkých častiach (napr. indexy/materializovaná views prepočítat až po vložení, ne po každém rádku, stejne tak integrity checks)
        - muže pomoct, keď vkládáme predrazená (presorted) dáta
        - paralelizácia (jednotlivé dimenze, tabulky faktu i partitions tabulek faktu možno provádet soubežne)

![](img/20230610173720.png)

### Zmeny dimenzí

Dimenze se mohou v prubehu života DW menit (zmení se napríklad region, pod ktorý spadá pobočka)

Možnosti implementácia zmeny:
- **Prepis** - nahradíme stará dáta novými, je to jednoduché, ale ztrácíme informaci o historii
- **Pridání sloupce s predchozí verzí (a valid from)** - vyreší problém, ale pri další zmene čelíme stejnému problému
- **Verzovanie** - tabulce dimenzí pridáme sloupce `valid from` a `valid to`, pri zmene iba upravíme `valid to` a pridáme rádek pre novou hodnotu dimenze
- **Pridání dimenze** - výber aktuálné verze musíme rešit jen v prípade, že nás daná hodnota zaujíma (napr. mení se prirazení obchodu do regionu, ale ne v každém dotazu nás zaujíma region)

Ak často pracujeme s aktuálné hodnotou, môžeme použít verzovanie, ale držet i aktuálné hodnotu v separátním sloupci.

### Prístupy tvorby dátových skladu

- **top-down** - analogie vodopádu, nejdríve analyzujeme datové zdroje, pak navrhneme a implementujeme sklad, nakonec naplníme daty a vytvoríme dáta marty
- **bottom-up** - iterativne-inkrementálné prístup, postupne pre každý zájmový objekt analyzujeme zdroje, postavíme dáta mart a prípadne rozšíríme (ak nejaký centrálné používáme) datový sklad

## Analytika velkých dát, jazyky pre realizaci analytických úloh, analytika na úrovni databáz (3/5)

### Big dáta

**Big dáta** - jedná se o dáta, ktoré kvuli své rychlé a kontinuálné tvorbe, velkému objemu, či složitosti, vylučují Spracovanie tradičními analytickými spôsoby.

- Rychlý príchod dát vyžaduje kontinuálné Spracovanie. Nepoužíváme batch processing, je ponapríklad stream processing (pre distribuované Spracovanie velkého množství zpráv/predání dát medzi systémy napríklad Apache Kafka).
- Velikost dát možno zvládat pomocí distribuovaných databáz/súborových systémov (zvyčajne NoSQL Databázy, alebo Hadoop Distributed File System)
- pre zvládání složitosti dát (komplexné vztahy, či dáta typu video) je nutné použít specializované nástroje (pre vztahy napríklad grafovou databázi).

### Prístupy ke Spracovanie dát

- **batch** - jednou za čas aktualizujeme náš DW, doplníme nove vzniklá dáta
- **stream** - prubežne vkládáme dáta tak, ako vznikají (duležité je udržovat konzistentní formát dát), snadneji se škáluje

### Jazyky pre realizaci analytických úloh

- Tradične jde o SQL, alebo jeho deriváty, ktoré datoví analytici dobre znají.
- Pre pokročilejší Spracovanie možno využít model MapReduce (a Hadoop), ve kterém je možné specifikovat transformační uzly v jakémkoliv programovacím jazyce
- NoSQL Databázy mohou mať vlastné rozšírení sql, alebo úplne jiný prístup k analytickým dotazum (napr. mongo má knihovny pre rôzne jazyky)

### Druhy sql dotazu specifické pre analytiku

- **Slice** - v rámci jedné dimenze vybíráme konkrétné hodnotu a zobrazujeme iba dáta s touto hodnotou dimenze. V sql pomocí WHERE. Napr. kolik se prodalo laptopu?
- **Dice** - jako slice, akorát pracujeme s intervaly/viac hodnotami jedné dimenze (napr. prodeje od-do, prodeje laptopu a telefonu), alebo hodnot viac dimenzí (prodeje laptopu v ríjnu). V SQL pomocí WHERE a AND/OR/IN/BETWEEN...
- **Roll-up** - provádíme agregaci dát. Dimenzionální - môžeme vynechat nejakou dimenzi (kolik jsme prodali za celý čas? kolik ve všech pobočkách?) alebo hierarchický - môžeme se dívat Z pohľadu vyšší úrovne nejaké dimenze (kolik jsme prodali v jednotlivých regionech, ktoré se skládají z viac poboček?). Oba prístupy možno kombinovat. V sql pomocí agregačních funkcií (GROUP BY a napríklad SUM)
- **Drill-down** - opak roll-upu, jdeme z abstrakce do vetšího detailu. Je nutné, aby nejaká detailnejší dáta existovala. zvyčajne deláme drill-down z nejakého materializovaného pohledu a jdeme na konkrétné dáta.

### Pivoting

- preskládání a agregace dát za účelem vizualizace
- nejjednodušší variantou je **kontingenční tabulka** (cross table), ve ktoré se zamerujeme na dve dimenze:
  ![](img/20230611214059.png)
- v SQL se dríve muselo provádet pomocí sjednocení (union) niekoľkoa príkazu
  ![](img/20230611214616.png)
- nyní je v SQL možné použít (uvádím i príklady, je možné uvést viac sloupcu pre vícedimenzionální kontingenční tabulky):
    - `GROUP BY ROLLUP(year, band)` - vrací *polovinu* kontingenční tabulky (vrátí dáta, agregaci pre každý rok a celkovou agregaci)
      ![](img/20230611215146.png)
    - `GROUP BY CUBE(year, band)` - vrací celou kontingenční tabulku (vrátí dáta, agregaci pre každý rok, agregaci pre každou skupinu a celkovou agregaci)
      ![](img/20230611215253.png)
    - `GROUP BY GROUPING SETS(...)` - umožňuje vetší kontrolu nad agregací dát (možno mimo jiné realizovat príkazy ROLLUP, CUBE)
      ![](img/20230611215834.png)

### Prístupy k implementaci OLAP

- **Relational OLAP (ROLAP)**
    - dáta ukládáme v relačná databázi (napr. postgres), dimenze simulujeme pomocí star schema, pre dotazovanie používáme standardní SQL
    - (+) nie je ponapríklad specializovaný systém
    - (+) dobrá flexibilita
    - (-) response time
    - (-) zabírá 3-4x viac místa, než MOLAP (v prípade dense cubes)
- **Multidimensional OLAP (MOLAP)**
    - dáta ukládáme ve speciálních multidimenzionálních strukturách (napr. in-memory db, alebo multidimenzionální pole/matice kde používáme prímou adresaci na disku)
    - rychlejší queries než ROLAP, zabírá míň místa (nie je ponapríklad ukládat foreign keys)
    - horší flexibilita (pri pridání hodnoty do domény dimenze je nutné pridat velké množství bunek, u ROLAP jde o jeden rádek v tabulce dimenze)
    - je ponapríklad specializovaný systém
    - mnohdy bývá součástí/add-on databázového riešenie (MS SQL Server, Oracle...)
- **Hybrid OLAP (HOLAP)**
    - kombinace MOLAP a ROLAP
    - čistá dáta uložena v ROLAP
    - agregace uloženy v MOLAP
    - => flexibilita, rychlost, ale vyšší složitost systémov

## Pokročilé techniky Spracovanie dát, výkonnosťní aspekty Spracovanie velkých dát (4/5)

Pre zabezpečenie rychlosti dotazu v OLAP se používá redundance v podobe:

- materializovaných pohledu (vkládáme jednou za čas, takže to nie je problém)
- indexu
- denormalizovaného schématu

### Indexy

**Indexy** - umožňují rychlejší získanie dát, ktorá nás zajímajú, pomocí predpočítaných výsledku. Omezují prostor nutný k prohledání pri čítanie dát.

- zvyčajne se používají [B+ stromy](4_dátabaze.md#indexovanie), ty sú však limitovány jen pre 1D dáta, nesú vhodné pre viac dimenzí
- **UB stromy** - multidimenzionální dáta sú linearizovány pomocí Z-krivky a následne indexovány pomocí B* stromu (jako B+, akorát tam sú jiná pravidla pre rebalanc). Linearizace Z-krivkou poskytuje dobrý výkon pre intervalové dotazy a zajišťuje, že dáta, ktorá si bola blízká puvodne si budú blízká i po linearizaci. Indexovat do linearizovaných dát možno pomocí konverze souradnic na binární číslo a následném prokládání bitu souradnic.
  |![](img/20230611224121.png)|![](img/20230611224138.png)|
  |---|---|
  |![](img/20230611224805.png)|![](img/20230611224906.png)|
- **R stromy** - obdélníky, popsány v [otázke 5](4_dátabaze.md#indexovanie), špatne se škálují do mnoha dimenzí
- **Bitmap indexy** - vhodné pre dimenze s málo variantami (napr. pobočky). Pre každou variantu udeláme bitové pole o délce tabulky faktu. Index v poli odpovídá rádku v tabulce faktu. U pole nastavíme 1 pre indexy, ve kterých varianta platí, jinak 0. Výhodou je, že se snadno používají bitové operace (AND, OR) a je možné takto pracovat i s rozdílnými dimenzemi. Pri mazání v tabulce faktu je napríklad buď upravit všechny bitmap indexy, alebo v tabulce faktu použít *tombstone* hodnotu (považujeme za prázdnou).
- **Range-encoded bitmap indexy** - vyžadují, aby mela dimenze serazené hodnoty variant (jinak stejne nemá cenu hledat pomocí intervalu). Opet má každá varianta bitové pole délky tabulky faktu. Ak je varianta pre daný fakt pravdivá, nastavíme ji, a všechny následující varianty v poradie, na hodnotu 1 (jinak 0). (Hodnota neznamená napr. *narodil se v mesíci*, ale *bol už na živu v mesíci*) Pri intervalovém dotazu pak stačí provést `<lower> AND (NOT <upper-exclusive>)`.
  ![](img/20230612104455.png)

### Partitioning

**Partitioning** - delení dát (tabulky) na viac (neprekrývajících se) částí

- prístupy:
    - logické - delíme podľa dáta/organizační jednotky/kategorie... alebo kombinace techto faktoru
    - fyzické - distribúcia dát na rôzne výpočetné uzly, umožnenie paralelního Spracovanie na viac strojích
- muže byť implementováno prímo v databázovém systémov, alebo si ho zajistíme na aplikačné úrovni (náročnejší)
- typy delení:
    - horizontální (sharding)- tabulku delíme na viac tabulek se stejnými sloupci, zvyčajne popodľa intervalu (často časová dimenze, prípadne nejaká, čo sa často nemení), ale je možné i napríklad popodľa hashe
    - vertikální - část sloupcu presuneme do jiné tabulky (a.k.a. row splitting, vztah 1:1), dává smysl keď určiťé sloupce nepoužíváme často.
- dáta používaná společne by mela byť uložena společne
- fajn pre škálovanie, časti možno nezávisle prohledávat na viac strojích
- nevýhodou je vyšší složitost systémov, pri vertikálním delení sú drahé joiny
- doporučuje se delat partitioning, keď má tabulka >100 milionu rádku/je vetší než 2GB

### Optimalizácia JOINu

JOINy sú:
- komutativní (nezáleží na poradie operandu, `A JOIN B = B JOIN A`)
- asociativní (nezáleží na závorkách, keď chceme použít viac operandu, `(A JOIN B) JOIN C = A JOIN (B JOIN C)`)
  => poradie JOINu možno preskládat, abychom získali rychlejší prevedenie SQL dotazu

- zvyčajne optimalizácia provádí databázový systém:
    - počet kombinací poradie joinu je `n!` -> pre jednoduché queries je možné zkoumat všechny možnosti, u složitejších je nutné použít metaheuristiky (napr. genetické algoritmy)
    - používateľ muže poskytnout hinty/vnutit vlastné plán (ak víme, co deláme, môžeme byť snadno lepší)
- ak sú dimenze dost restriktivní (filtrují hodne faktu), muže byť vhodné udelat cross join dimenzí

### Pohledy

- klasický pohled (**view**) pripomíná funkcia v programovacích jazycích - pojmenovaný dotaz. Pri dotazu nad view se automaticky provede selekce dát
- **materializovaný pohled** funguje jako klasický pohled, ale má predpočítaný výsledek, uložený v tabulce (funguje jako cache), takže dotazy na materializovaný pohled sú rychlejší. Pri zmene underlying dát se musí dáta materializovaného pohledu prepočítat/rozšírit (možno odložit, ale pak máme nekonzistenci), což u OLAP nie je zas takový problém, jako u OLTP.
    - vhodné pre často používané a drahé dotazy/časti dotazu

### Databázové technologie pre Big Data

**Sloupcové Databázy** - na rozdíl od rádkových databáz (napr. Postgres), kde sú uloženy vepodľa sebe dáta náležící jednomu rádku ukládají sloupcové Databázy (napr. BigQuery, S4HANA) vepodľa sebe dáta z jednoho sloupce. Vďaka tomu mohou byť sloupcové Databázy rychlejší pre čítanie dát.

**In-memory Databázy** - namísto uložení dát na pevném disku držíme dáta v RAM -> rychlejší prístup, ale mnohem vyšší cena. Napr. S4HANA

**Distribuované Databázy** - umožňují horizontální škálovanie, svou distribuovaností umožňují fault-tolerance (vďaka replikaci dát), napr. Hadoop Distributed File System, Apache Cassandra.

### NoSQL (not only sql)

- **key-value stores** - dáta ukládáme/hledáme pomocí kľúče, snadno se používají jako cache napr. Redis
- **dokumentové Databázy** - dáta ukládají ve forme dokumentu (každý má kľúč, popodľa kterého se referencuje, jinak je to klasická struktura/trída) a kolekcí dokumentu, napr. Mongo, Firebase
- **sloupcové Databázy** (column family, wide-column) - dáta sú organizována do tzv. "rodin sloupcu" (column families), ktoré majú spoločné vlastnosti alebo sú často používány společne, napr. Cassandra
- **grafové Databázy** - snadno modelují entity a vztahy, napr. Neo4j
- zvyčajne nebývají ACID (a nepoužívají joiny), vďaka čemuž mohou byť rychlejší. Vetším problémem je udržení konzistencia dát. Nektoré poskytují distribuci dát na viac výpočetních uzlu out of the box (co vím tak mongo, cassandra)

### Apache Hadoop

**Platforma pre paralelní/distribuované Spracovanie velkých dátasetu**

- batch processing
- vysoká dostupnost zajištena replikací dát
- využívá **Hadoop Distributed File System (HDFS)**
    - distribuovaný súborový systém vhodný pre immutable dáta
    - abstrahuje distribuovanost, používateľ pracuje s dátami jednotným spôsobem
    - high availability vďaka replikaci, dáta rozdelena do bloku (defaultne 128MB), každý je v HDFS replikován (defaultne 3x, každá replikácia na jiném stroji)
    - jeden stroj je **name node** (master), ostatné **dáta nodes**. Master má prehled o mapovanie súborov na bloky a ich lokaci na dáta nodes (tato dáta sú taky replikována). Pre získanie dotazu klient kontaktuje mastera (zjistí, kde má hledat dáta) a následne kontaktuje príslušné dáta nodes.
    - datové bloky sú write-once (vďaka čemuž nemusíme rešit zamykanie a dosahujeme vyšších rychlostí čítanie)
- spolu s HDFS využívá modelov **MapReduce**
    - umožňuje paralelní Spracovanie dát
    - používateľ definuje jen použité map a reduce funkcia (muže jich byť viac)
    - postupne probíhá Map, Grouping a Reduce fázy
    - **Map** - transformace dát (filtrovanie, sorting). Bere vždy jednu položku dát (napr. rádek) a vrací 0-1 key-value pár. Tímto spôsobem zpracuje všechna dáta
    - **Grouping** fázy - deje se automaticky po map fázi, seskupuje dáta se stejným kľúčem (vznikne key-list) a predá dáta se stejným kľúčem jednomu reduceru
    - **Reduce** - agregace dát popodľa kľúče, sumarizace výsledku Map operací. Bere key-list (obsahující všechny hodnoty pre daný kľúč) a vrací key-list (obsahující 0-n výstupních záznamu).
      Napr. word count - map bere rádek a vrací niekoľko (podľa výskytu na rádku) dvojic `(slovo, 1)`. Reduce sečte `1` pre daná slova a vrací `(slovo, součet)`.
      ![img.png](img/mapReduce.png)

### Apache Hive

- distribuovaný dáta warehouse postavený nad Hadoop (a HDFS)
- poskytuje SQL-like (HiveQL) rozhrania pre dotazy, ktoré je prevedeno do MapReduce dotazu (je možné delat i vlastné map reduce skripty)
- umožňuje používanie strukturovaných dát (struktury, seznamy, mapy)
- umožňuje serializaci/deserializaci dát do/z rôznych formátu (xml, csv, json...)
- vhodný pre dlouho bežící ETL jobs
- ak chceme low latency/interactive queries, je vhodnejší použít Apache Impala (SQL query engine nad Hadoopem)

### Stream processing

- nezpracováváme balík dát, ale kontinuálné stream
- Apache Spark (analytický engine pre large-scale dáta processing, umí batch i stream processing)
- Apache Storm (real-time výpočty, skládá se ze zdrojov dát a acyklicky propojených zpracovávajících uzlu)

## Notes

### Príklad architektúry Data Warehouse pre Big Data

![](img/20230612205443.png)

[Go to the next question](dev_4_bezpecny_kod.md)
