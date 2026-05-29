# Databázy

> Principy ukladanie dát, Databázy. Architektúra relačných databáz, dotazovací jazyk SQL a jeho časti (definícia, manipulácia, transakcie). Jazyk definícia dátovej schémy, DDL. Jazyk manipulácia s dátami, DML. Relačná algebra, integritné obmedzenie, riadenie transakcí. Indexovanie, hašovanie. Príklady z praxe pre všetko vyššie uvedené. ([PV003](https://is.muni.cz/auth/el/fi/jaro2022/PV003/um/) || [PA152](https://is.muni.cz/auth/el/fi/jaro2025/PA152/um/))

1. [Principy ukladanie dát, Databázy (1/7)](#principy-ukladanie-dát-Databázy-17)
2. [Architektúra relačných databáz, dotazovací jazyk SQL a jeho časti (2/7)](#Architektúra-relačných-databáz-dotazovací-jazyk-sql-a-jeho-časti-27)
3. [Jazyk definícia dátovej schémy, DDL (3/7)](#jazyk-definícia-dátového-schématu-ddl-37)
4. [Jazyk manipulácia s dátami, DML (4/7)](#jazyk-manipulácia-s-daty-dml-47)
5. [Relačná algebra, integritné obmedzenie, riadenie transakcí (5/7)](#relační-algebra-integritní-obmedzenie-rízení-transakcí-57)
6. [Indexovanie, hašovanie (6/7)](#indexovanie-hašovanie-67)
7. [Príklady z praxe pre všetko vyššie uvedené (7/7)](#príklady-z-praxe-pro-vše-výše-uvedené-77)

## Principy ukladanie dát, Databázy (1/7)

Data se v praxi ukládají prímo do súborového systémov, alebo do Databázy (relační, dokumentové, grafové...).

### Souborový systém

- menší systémové nároky, jednoduchší
- náročné zabezpečenie konzistencia, nutnost riešenie zamykanie súborov, problematický transakční prístup
- náročnejší správa prístupových práv
- nutnost konzistentne rešit formát dát
- horší čitateľnosť & dokumentovatelnost dátového modelov
- operační systém slouží jako abstrakce pre aplikácie, umožňuje jednotný prístup k rôznym súborovým systémum

Pre aplikace se hodí na ukladanie velkých súborov (pdf, obrázky, video, statická stránka, ak teda nepoužijeme CDN), ktoré je nepraktické uchovávat v databázi. Je nutné dávat pozor, abychom neposkytli prístup jinam než chceme.

### Databázový systém

- nezávislý na aplikaci, jednotné rozhrania pre všetkochny
- snadné zabezpečení, konzistencia, soubežný prístup
- snadná čitateľnosť, dokumentovatelnost
- relačná systémy korelují s ERD
- deklarativní prístup
- obtížná implementácia složitejších struktur (záleží však na systémov)
- O relačných databázch platí, že umožňují ACID [transakcie](#rízení-transakcí).

## Architektúra relačných databáz, dotazovací jazyk SQL a jeho časti (2/7)

*Fun fact: Jaká Architektúra se v RDBMS používá? To se v predmetu `Architektúra relačných databáz` nedozvíte*

### Architektúra relačných databáz

Nejaká jednoduchá Architektúra by mohla vypadat takto:

- **databázový server** (napr. fyzické/virtuálné server, cloudová služba jako AWS RDS, Google Cloud SQL)
  - prijímá, zpracovává a odpovídá na požadavky
- **relačná databázový systém** (napr. PostgreSQL, MySQL, Oracle Database, Microsoft SQL Server)
  - autentizace, autorizace
  - aplikace pracující nad samotnou databáz
  - umožňuje tvorbu tabulek/indexu... manipulaci s dátami, ich čítanie...
  - zajišťuje integritu dát
  - vyhodnocuje a zpracovává SQL queries, provádí vnitrní optimalizácia
  - muže delat kešovanie
- **Databázy** (napr. konkrétné Databázy `eshop`, `crm`, `test_db` v rámci RDBMS)
  - samotné místo, kde sú dáta uložena

#### Vnitrní komponenty RDBMS (Co se deje pri Spracovanie dotazu)
Keď do Databázy dorazí SQL dotaz, prochází specifickými vnitrními subsystémy RDBMS:

1.  **Parser a Prekladač (Query Parser):** Zkontroluje syntaktickou správnost SQL dotazu a prevede ho do interního stromu reprezentujícího operace relačná algebry.
2.  **Optimalizátor dotazu (Query Optimizer):** **Kľúčová část.** Na základe statistik o tabulkách (počet rádku, distribúcia hodnot v indexech) vygeneruje niekoľko provádecích plánu (Execution Plans) a vybere ten s nejnižší odhadovanou cenou (Cost-based optimizer). Rozhoduje, či se použije Index Scan alebo Sequential Scan.
3.  **Provádecí engine (Execution Engine):** Vykonává zvolený plán a komunikuje se správcem úložište.
4.  **Buffer Manager (Správce vyrovnávací pameti):** RDBMS nečte dáta prímo z disku po bajtech, ale v tzv. **Stránkách / Blozích** (Pages/Blocks, typicky 8 KB). Buffer Manager udržuje nejčasteji používané stránky v RAM. Ak engine potrebuje dáta, Buffer Manager je vyhledá v RAM, a až pri minoutí (Cache Miss) je načte z disku.
5.  **Storage Manager (Správce úložište):** Mapuje logické struktury (tabulky, indexy) na fyzické soubory na disku a alokuje prostor.
6.  **Transaction & Recovery Manager:** Řídí zamykanie dát (izolaci) a zápis žurnálu (zajišťuje trvanlivost).
RDBMS muže obsahovat techniky pre administraci prístupových práv (obmedzenie určiťých operací, viditelnost dát až na row/column level...).

Ak se otázkou myslí *Z jakých prvku se relačná Databázy skládají*, pak by bolo fajn mluvit o tabulkách, sloupcích, jazyku SQL pre ich definici (DDL, dáta definition language) a manipulaci (DML, dáta manipulation language), indexech, (materializovaných) views...

### Dotazovací jazyk SQL a jeho časti

Dotazovací jazyk SQL vychází z [relačná algebry](#relační-algebra).

Obsahuje konstrukty pre definici dátovej schémy, pre manipulaci s dátami a pre transakční Spracovanie (viz další sekce).

V nekterých systémech má prostredky pre procedurální programovanie, PL/SQL (napríklad Oracle).

SQL muže obsahovat triggery, teda dodatečné akce, ktoré se majú vykonat pri určiťém príkazu (INSERT, UPDATE, DELETE). Používají se napríklad pre udržovanie history table, alebo pre aktualizaci `updated_at`, ak to nepodporuje daný RDBMS.

Pri práci s SQL používáme prepared statements, abychom zabránili SQL injection.

## Jazyk definícia dátovej schémy, DDL (3/7)

*Note: rôzne RDBMS podporují rôzne typy. Treba TEXT v základu SQL definován nie je, ale v praxi je použití VARCHAR2 s fixní délkou príliš nepraktické, proto ho tu uvádím*

Tvorba tabulky:

```sql
/* Blokový komentář */
-- Inline komentář
CREATE TABLE Products (
          id          INT PRIMARY KEY, --napríklad u pg je možné použít SERIAL, abychom si nemuseli dělat sekvence
          cost        INT NOT NULL,
          ean         INT UNIQUE NOT NULL,
          name        TEXT NOT NULL,
          description TEXT,
          created_by  INT NOT NULL REFERENCES User(id)
            updated_at  DATETIME,
);
```

V praxi je lepší si generovat vždycky primárné kľúče - externé unikátne hodnoty nemusí byť vždy zas tak unikátne/nemenné. Je lepší používat čísla, než stringy (stačí jedna operace porovnání => rychlejší, zvlášť, keď jde o PK). Compound primary key je možný, ale opet bývá pomalejší.

Pre generovanie dalších hodnot ID se drív používaly sekvence, dneska stačí hodit `SERIAL`, alebo `AUTOINCREMENT`.

Pre dátamm/čas používáme DATETIME. Ak bychom použili INTy & unix timestamp, v roce 2038 bychom meli problém.

U cizích kľúču môžeme specifikovat `ON DELETE` `CASCADE` (se smazáním používateľa se smažou i jím pridané produkty), `SET NULL` (se smazáním používateľa se nastaví `created_by` na NULL, což ale kvuli našemu constraintu nepujde). V aktuálné konstelaci daného používateľa nemôžeme smazat.

Modifikace tabulky:

- pridání sloupce, odebrání sloupce, zahození tabulky (selže, ak na ni sú reference z jiných tabulek)

```sql
ALTER TABLE Products ADD picture TEXT;
ALTER TABLE Products DROP COLUMN description;
DROP TABLE Products;
```

Je možné použít `IF EXISTS` a `IF NOT EXISTS`, aby nám skript nepadal pri opakovaných createch/dropech, ale to se hodí hlavne pre hraní si.

V produkci použijeme migrační schéma obsahující UP a DOWN skripty, abychom mohli prípadne akce revertovat.

## Jazyk manipulácia s dátami, DML (4/7)

### Insert

```sql
INSERT INTO Tabulka(sloupec_a, sloupec_b)
VALUES (hodnota_a, hodnota_b);
```

Kontrolují se integritné obmedzenie, v prípade autoincrement/serial kľúče ho nie je nutné explicitne uvádet. zvyčajne príkaz vrací vložená dáta (včetne vygenerovaných hodnot).

### Update

```sql
UPDATE Tabulka
SET sloupec_a = hodnota_a
WHERE ... --často klíč
```

Update bez WHERE muže provést update všeho. Kontrolují se integritné obmedzenie ovlivnených sloupcu

### Delete

```sql
DELETE FROM Tabulka WHERE ...
```

Delete bez WHERE muže provést smazání celého obsahu

### Select

Trochu nabušený select:

```sql
SELECT DISTINCT Tabulka.sloupec, B.sloupec
FROM Tabulka
JOIN TabulkaB AS B ON Tabulka.cizi_id = B.id
WHERE price > 0
ORDER BY sloupec ASC
```

*Join jde prepsat pomocí WHERE*

Výsledek selectu možno dát do závorek a použít namísto nejaké tabulky, dáta majú porád tabulární strukturu.

Mezi daty se stejnou strukturou možno provést množinové operace `UNION`, `INTERSECT`, `MINUS`.

U `WHERE` môžeme používat i príslušnost v množine hodnot `IN`, rozsahu `BETWEEN ... AND ...`, logické operátory `AND`, `OR`... U stringu `LIKE` kde `?` zastupuje znak a `%` niekoľko znaku.

### Pohled/View

- Uložený a pojmenovaný select, ktorý se vykoná s provedením dotazu
- view majú omezenou modifikaci dát (napríklad nemožno, ak obsahuje agregaci, distinct, union...) => je lepší použít zdrojové tabulky

### Materializovaný pohled/view

- View, ktorého výsledek se predpočítává. Vrací se pak hodnoty prímo z nové tabulky, ale s každou zmenou je napríklad materializované view prepočítat (rychlejší čítanie, pomalejší zápis).

### Agregační funkcia

Používané s `GROUP BY sloupec/sloupce`

*Ak nepoužijeme `GROUP BY`, počítají se agregační funkcia ze SELECTu*

- `COUNT(...)` - počet rádku, možno použiť `COUNT(*)`
- `AVG(...)`
- `SUM(...)`
- `MIN(...)`
- `MAX(...)`

Možno použít `HAVING ...`, což je `WHERE`, ale s použitím agregačních funkcií.

## Relačná algebra, integritné obmedzenie, riadenie transakcí (5/7)

### Relačná algebra

> *[@thes01](https://github.com/thes01): viac taky na [tomto odkazu (bc státnice)](https://docs.google.com/document/d/1SVbwwMDDfOCqAdsfTH1RDJex9_fZZ96wb0Vp2fSoUFs/edit)*

**Relace** je podmnožinou kartézského součinu domén. Toto se promaťne do Databázy tak, že domény sú datové typy sloupcu a tabulka (složená ze sloupcu) obsahuje iba takéto kombinace hodnot (rádky), jaké sú v relaci.

Pre relačná operace používáme relačná algebru skládající se z:

- **množinových operací** (ale pre sjednocení, rozdíl a prunik musí byť relace kompatibilní, tj. mať stejnou hlavičku)
- **projekce** - tj. výber sloupcu
- **selekce** - tj. WHERE
- **prejmenovanie** - AS
- **spojení/join/součin relací** - JOIN
- **seskupení a agregace** - GROUP BY, AVG(...)...

...jednotlivé operace teda odpovídají dotazovacímu jazyku SQL.

Existují dotazy, ktoré nejsme schopni vyjádrit relačná algebrou, napríklad tranzitivní uzáver.

*Tranzitivní uzáver nad relací získáme tak, že se díváme na prvky množiny v relaci. Ak je `a` v relaci s `b` a `b` v relaci s `c`, pak (aby bolo dosaženo tranzitivity) tranzitivní uzáver obsahuje relaci `a` s `c`.*

### Integritní obmedzenie

Součástí DDL, jazyku definícia dát. Určitým spôsobem omezují, jakých hodnot mohou pole nabývat. Napr. `NOT NULL`, `UNIQUE`, `FOREIGN KEY .. REFERENCES ..(..)`, `CHECK(price>0)`... Uvádí se na príslušný rádek (ideálne), tabulky, jako dodatečný rádek tabulky, alebo jako samostatný výraz `ALTER TABLE .. ADD CONSTRAINT ... NOT NULL (id)`.

### Riadenie transakcí

transakcie v RDBMS majú ACID vlastnosti:

- **Atomicity** - skupina príkazu transakcie brána jako jednotka; provedou se všechny, alebo žádný
- **Consistency** - po vykonání transakcie je db v konzistentním stavu, nie je porušeno žádné integritné obmedzenie
- **Isolation** - transakcie je izolovaná od ostatních transakcí, je možné nastavit úrovne transakcie, podľa toho muže transakcie skončit chybou (ak došlo k modifikaci stejného objektu, jaký modifikovala jiná transakcie), alebo se využijí zamykací mechanismy
  * **Dirty Read (Špinavé čítanie):** transakcie T1 čte dáta, ktorá transakcie T2 zmenila, ale ješte nepotvrdila (COMMIT). Ak T2 udelá rollback, T1 pracovala s neexistujícími daty.
  * **Non-repeatable Read (Neopakovatelné čítanie):** transakcie T1 načte rádek. transakcie T2 tento rádek zmení a potvrdí (COMMIT). Ak T1 načte rovnaký rádek znovu, dostane jiné hodnoty.
  * **Phantom Read (Fantomové čítanie):** transakcie T1 načte množinu rádku splňující podmínku (napr. `price > 100`). transakcie T2 vloží (INSERT) nový rádek splňující tuto podmínku a potvrdí. Ak T1 dotaz zopakuje, objeví se tam nový „fantomový“ rádek.
- **Durability** - dáta sú po vykonání transakcie persistentne uložena

transakcie se potvrzují príkazem `COMMIT`, vrací príkazem `rollback` na stav pred započením transakcie, či po poslední `SAVEPOINT`

#### Ako se izolace a trvanlivost implementuje v praxi:
* **2PL (Two-Phase Locking):** Tradiční pesimistické zamykanie. transakcie v první fázi zámky iba získává (sdílené pre čítanie, exkluzivní pre zápis) a ve druhé fázi po COMMITu je uvolňuje. Zpusobuje zablokovanie čtenáru zapisovateli a naopak.
* **MVCC (Multi-Version Concurrency Control):** Moderní optimistický prístup (PostgreSQL). Zapisovatelé neblokují čtenáre. Pri zmene rádku se nevytvárí prepis, ale nová verze rádku s informací o čase/transakci (`xmin`, `xmax`). Každá transakcie pak vidí „snímek“ (snapshot) dát odpovídající jejímu startu. Staré verze čistí na pozadí proces (v PG napr. `VACUUM`).
* **WAL (Write-Ahead Logging) / Žurnálovanie:** Zajišťuje **Durability**. Než se zmenená dáta (dirty pages) zapíšou z RAM na pomalý disk do samotných tabulek, zapíše sa sakvenční záznam o zmene do logu na disku (WAL). Zápis do WAL je extrémne rychlý (iba append). Ak systém spadne, Transaction Manager pri startu projde WAL a provede operaci **REDO** (pre potvrzené transakcie) a **UNDO** (pre rozepsané transakcie, ktoré nestihly COMMIT).

## Indexovanie, hašovanie (6/7)

### Indexovanie

Index slouží ke zrychlení/zefektivnení častých dotazu nad tabulkou. Dotazy obsahující zvolený sloupec (či ich kombinaci) budú rychlejší. Struktura <kľúč, pointer na záznam>

```sql
CREATE INDEX my_index ON Products (Price)
```

Pre indexy se mohou používat:

- **tradiční indexy** - jako v knihách, odkazy na rádky s danou hodnotou, je možné delat viac úrovniach indexu, používat ruzná indexová usporádání...
- **haše** - pre získanie jednoduché hodnoty velkých dát, neumožňují range scans alebo ordering.
- **B+ stromy** - každý uzel obsahuje odkazy na uzly níže, alebo hodnoty (jedná se o listový uzel). Hodnoty sú v listech vzestupne usporádány, uzly v sobe majú i informace o intervalech daných odkazu/hodnot, listy sú provázané. nejviac používané.
  ![](img/20230526220652.png)
Speciální n-árne vyvážené stromy optimalizované pre bloková disková úložište. 
    * **Kľúčový rozdíl oproti B-stromum:** Vnitrní uzly (internal nodes) obsahují **iba navigační kľúče a pointery** na další uzly, ale neobsahují samotná dáta rádku (ani pointery na dáta). Všechna dáta/pointery na reálné rádky sú uloženy **výhradne v listových uzlech (leaf nodes)**.
    * **Proč sú ideálné pre DB:** 
      1. Vnitrní uzly sú vďaka absenci dát malé $\rightarrow$ do jedné diskové stránky (8 KB) se vejde obrovské množství navigačních kľúču $\rightarrow$ strom má obrovský vetvící faktor (**High Fan-out**) a je velmi nízký (zpravidla výška 3 až 4 i pre miliony záznamu). Na nalezení jakéhokoliv záznamu stačí max 3–4 diskové operace (I/O).
      2. Všechny listové uzly sú **obousmerne lineárne provázané** (linked list). Ak DB provádí rozsahový dotaz (`WHERE price BETWEEN 10 AND 50`), vyhledá prvek `10` a pak už jen sekvenčne čte sousední listy, nemusí se vracet nahoru do stromu (tzv. Range Scans sú extrémne rychlé).
- **B stromy** - podobné jako B+, ale uzly mohou obsahovat i hodnoty, ne iba odkazy na další uzly. liste nesú provázané, ale sú na rovnaké úrovni, jinak podobné jako B+.
- **R stromy** - podobné jako B+, ale sú vícedimenzionální, ve 2D fungují jako obdélníky. Data sú v listových uzlech stromu. Rodič uzlu zahrnuje všechny své potomky (ve 2D jde o vetší obdélník, ktorý obsahuje potomky). Ideálna je, aby zabíraly rodičovské obdélníky co nejméne prostoru - rodič totiž jako index redukuje oblast nutnou k prohledání (ríká *hledej ve mne!*). Treba pre geodáta.
  ![](img/20230526220927.png)
  ![](img/20230611232516.png)

Další delení indexu:

- **dense/hustý** - každý rádek je zaindexovaný, zabírá viac místa, ale hľadanie je rychlejší. muže ukazovat na [kapsu](#kapsy) - skupinu rádku se stejným kľúčem, ktorá se prochází lineárne.
- **sparse/rídký** - iba nektoré rádky zaindexované, zabírá méne místa, ale hľadanie pomalejší (je ponapríklad dohledat konkrétné rádek)

### Hašovanie

**Cieľom hašovanie je prevést vstupní dáta libovolné délky na výstup jednotné délky (fixed-length retezec, alebo číslo), hash.** Z hashe by nemelo byť možné odvodit vstup (**jednosmernost**), pre každý vstup bychom meli byť schopni deterministicky (vstupem sú iba dáta) určiť jediný hash. Zároveň muže byť (podľa použití) cieľom minimalizovat riziko kolize, teda že dva vstupy majú rovnaký hash (nemožno se tomu ale vyhnout, pretože musíme byť schopni mapovat nekonečno možných vstupu na omezený počet výstupu daný délkou). Dle použití muže byť tiež duležité, aby podobné vstupy mely zásadne rozdílné haše, aby bolo možné snadno odhalit drobnou (zámernou či nechtenou) modifikaci vstupu. Pre prolamovanie hašu se používají rainbow tables, obsahující pre daný algoritmus známé vstupy a ich haše.

Hašovanie se používá pre zabezpečenie integrity dát (certifikáty, checksum), rychlé porovnávanie dát (HashMap), porovnávanie dát se znalostí iba hashe (uchovávanie hash hesel v databázi, Argon2).

#### Bezkoliznost

- **slabá** - pre vstup A nejsme schopni v rozumném čase nalézt rozdílný vstup B, ktorý by mel rovnaký hash
- **silná** - nejsme schopni v rozumném čase najít libovolné dva rozdílné vstupy se stejným hashem

Pre rôzne účely používáme rôzne algoritmy, jde o balanc rychlosti (u hesel muže byť kýžená pomalost) a bezpečnosťi/pravdepodobnosti kolize.

- **MD5** - relativne rychlý, nie je bezpečný (možno rychle najít kolize i na bežném počítači).
- rodina Secure Hashing Algorithm, za bezpečnou se aktuálne považuje **SHA-2** (SHA256, SHA512, SHA-384...)
- **Argon2** - v súčasnosti doporučovaný pre hašovanie hesel
- hashem (hloupým, ale rychlým) muže byť napríklad i délka vstupu, modulo, součet ascii hodnot znaku... (nazývá se [Cyclic redundancy check](dev_4_bezpecny_kod.md#notes))

#### Databázové (nekryptografické) vs. Kryptografické hašovanie (Švenduv státnicový chyták)
U zkoušky (dr. Švenda) musiete striktne rozlišovat účel hašovanie:
* **Indexové / HashMap hašovanie:** Používá se pre Hash Indexy v DB. Cieľom je **maximálné rychlost** výpočtu a rovnomerná distribúcia do pameťových kapes (buckets). Používají se algoritmy jako *MurmurHash* alebo *CityHash*. 
* **Proč sú zde kryptografické funkcia (SHA-2, SHA-3) nevhodné?** Jsou pre indexovanie zbytečne výpočetne extrémne drahé (**overkill**). U indexu nepotrebujeme vlastnosti jako jednosmernost alebo odolnost proti nalezení preimage (nikdo se nesnaží z hashe v indexu zpetne hacknout hodnotu ID).

#### Riešenie kolizí a typy hašovanie v DB
Keď dve rôzne hodnoty vygenerují rovnaký index kapsy (bucketu), nastává kolize. Řeší se:
1.  **Zretezené hašovanie (Chaining / Kapsy):** Každý bucket ukazuje na spojový seznam (kapsu) záznamu. Ak se zaplní, lineárne se prochází alebo se napojí pretoková kapsa.
2.  **Otevrená adresace (Open Addressing):** Ak je bucket obsazen, hledá se popodľa definovaného pravidla (Linear Probing) další volné místo prímo v hlavním poli.

Popodľa správy velikosti pole delíme hašovanie na:
* **Statické hašovanie:** Počet bucketu je fixní. Pri zaplnení Databázy rapidne roste počet kolizí a výkon degraduje (dlouhé spojové seznamy v kapsách).
* **Dynamické hašovanie (Extensible / Linear Hashing):** Velikost hašovací tabulky se dynamicky prispôsobuje (roste/zmenšuje se) počtu dát. Využívá se bitová reprezentace hashe. Pri reorganizaci (split bucketu) se neprepočítává celá tabulka, ale rozdeluje se vždy jen jedna konkrétné kapsa.

## Príklady z praxe pre všetko vyššie uvedené (7/7)

*Poznámka: Praktické príklady sú integrovány v jednotlivých sekcích výše. Tato sekce slouží jako prehled praktických aspektu:*

### Praktické aspekty ukladanie dát
- Výber medzi súborovým systémem a databáz popodľa typu a struktury dát
- Použití CDN pre statický obsah a Databázy pre strukturovaná dáta
- Implementácia migračních skriptu v produkčních prostrediach

### Praktické SQL dotazy a optimalizácia
- Použití indexu pre zrychlení častých dotazu
- Prepared statements pre prevenci SQL injection
- Triggery pre automatizaci (napr. aktualizace `updated_at`)

### Praktické aspekty integrity a transakcí
- Cascading deletes vs. soft deletes v produkčních systémech
- Použití transakcí pre zabezpečenie konzistencia pri zložitých operacích
- Monitoring a protokolovanie databázových operací

### Praktické aspekty výkonu
- Profiling databázových dotazu
- Sharding a replikácia pre škálovanie
- Používanie materializovaných views pre zložité analytické dotazy

## Notes
### Kapsy
do kapsy se umísťují kolidující prípady. kapsa se prochází lineárne. na kapsu s vyčerpanou kapacitou možno navázat pretokovou kapsu, tech muže byť viac, ale musí se retezit.

[Go to the next question](./5_pocitacove_site.md)
