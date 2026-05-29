# Databázy

> Princípy ukladania údajov, databázy. Architektúra relačných databází, dotazovací jazyk SQL a jeho časti (definícia, manipulácia, transakcie). Jazyk definície datového schémy, DDL. Jazyk manipulácie s údajmi, DML. Relačná algebra, integritné obmedzenia, riadenie transakcií. Indexovanie, hašovanie. Príklady z praxe pre všetko vyššie uvedené. ([PV003](https://is.muni.cz/auth/el/fi/jaro2022/PV003/um/) || [PA152](https://is.muni.cz/auth/el/fi/jaro2025/PA152/um/))

1. [Princípy ukladania údajov, databázy (1/7)](#princípy-ukladania-údajov-databázy-17)
2. [Architektúra relačných databází, dotazovací jazyk SQL a jeho časti (2/7)](#architektúra-relačných-databází-dotazovací-jazyk-sql-a-jeho-časti-27)
3. [Jazyk definície datového schémy, DDL (3/7)](#jazyk-definície-datového-schémy-ddl-37)
4. [Jazyk manipulácie s údajmi, DML (4/7)](#jazyk-manipulácie-s-údajmi-dml-47)
5. [Relačná algebra, integritné obmedzenia, riadenie transakcií (5/7)](#relačná-algebra-integritné-obmedzenia-riadenie-transakcií-57)
6. [Indexovanie, hašovanie (6/7)](#indexovanie-hašovanie-67)
7. [Príklady z praxe pre všetko vyššie uvedené (7/7)](#príklady-z-praxe-pre-všetko-vyššie-uvedené-77)

## Princípy ukladania údajov, databázy (1/7)

Údaje sa v praxi ukladajú priamo do súborového systémov, alebo do databázy (relačný, dokumentový, grafový...).

### Souborový systém

- menšie systémové nároky, jednoduchší
- náročné zabezpečenie konzistentnosti, ponapríklad riešenia uzamykania súborov, problematický transakčný prístup
- náročnejšia správa prístupových práv
- ponapríklad konzistentne riešiť formát údajov
- horšia čitateľnosť & dokumentovateľnosť datového modelov
- operačný systém slúži ako abstrakcia pre aplikácie, umožňuje jednotný prístup k rôznym souborovým systémom

Pre aplikácie sa hodí na ukladanie veľkých súborov (pdf, obrázky, video, statická stránka, pokiaľ teda nepoužijeme CDN), ktoré nie je praktické uchovávať v databáze. Je potrebné dávať pozor, aby sme neposkytli prístup inam ako chceme.

### Databázový systém

- nezávislý od aplikácie, jednotné rozhranie pre všetkých
- ľahké zabezpečenie, konzistentnosť, simultánny prístup
- ľahká čitateľnosť, dokumentovateľnosť
- relačné systémy korelujú s ERD
- deklaratívny prístup
- obtížná implementácia zložitejších štruktúr (závisí však od systémov)
- O relačných databázach platí, že umožňujú ACID [transakcie](#riadenie-transakcií).

## Architektúra relačných databází, dotazovací jazyk SQL a jeho časti (2/7)

*Fun fact: Aká architektúra sa v RDBMS používa? To sa v predmete `Architektúra relačných databází` nedozviete*

### Architektúra relačných databází

Nejaká jednoduchá architektúra by mohla vyzerať takto:

- **databázový server** (napríklad fyzické/virtuálny server, cloudová služba ako AWS RDS, Google Cloud SQL)
  - prijíma, spracováva a odpovídá na požiadavky
- **relačný databázový systém** (napríklad PostgreSQL, MySQL, Oracle Database, Microsoft SQL Server)
  - autentizácia, autorizácia
  - aplikácia pracujúca nad samotnou databázou
  - umožňuje tvorbu tabuľiek/indexov... manipuláciu s údajmi, ich čítanie...
  - zabezpečuje integritu údajov
  - vyhodnocuje a spracováva SQL queries, vykonáva vnútorné optimalizácie
  - môže robiť kešovanie
- **databáza** (napríklad konkrétna databáza `eshop`, `crm`, `test_db` v rámci RDBMS)
  - samotné miesto, kde sú údaje uložené

#### Vnútorné komponenty RDBMS (Čo sa deje pri spracovaní dotazu)
Keď do databázy dorazí SQL dotaz, prechádza špecifickými vnútornými subsystémami RDBMS:

1.  **Parser a Prekladač (Query Parser):** Skontroluje syntaktickú správnosť SQL dotazu a prevede ho do vnútorného stromu reprezentujúceho operácie relačnej algebry.
2.  **Optimalizátor dotazov (Query Optimizer):** **Kľúčová časť.** Na základe štatistík o tabuľkách (počet riadkov, distribúcia hodnôt v indexoch) vygeneruje niekoľko provádzacích plánov (Execution Plans) a vyberie ten s najnižšou odhadovanou cenou (Cost-based optimizer). Rozhoduje, či sa použije Index Scan alebo Sequential Scan.
3.  **Provádzací engine (Execution Engine):** Vykonáva zvolený plán a komunikuje so správcom úložiska.
4.  **Buffer Manager (Správca vyrovnávacej pamäte):** RDBMS nečita údaje priamo z disku po bajtoch, ale v tzv. **Stránkach / Blokoch** (Pages/Blocks, typicky 8 KB). Buffer Manager udržiava najčastejšie používané stránky v RAM. Ak engine potrebuje údaje, Buffer Manager ich vyhľadá v RAM, a až pri minútí (Cache Miss) ich načita z disku.
5.  **Storage Manager (Správca úložiska):** Mapuje logické štruktúry (tabuľky, indexy) na fyzické súbory na disku a alokuje priestor.
6.  **Transaction & Recovery Manager:** Riadi zamykanie údajov (izoláciu) a zápis žurnálu (zabezpečuje trvanlivosť).
RDBMS môže obsahovať techniky pre administráciu prístupových práv (obmedzenie určitých operácií, viditeľnosť údajov až na row/column level...).

Ak sa otázkou myslí *Z akých prvkov sa relačná databáza skladá*, potom by bolo fajn hovoriť o tabuľkách, stĺpcoch, jazyku SQL na ich definíciu (DDL, data definition language) a manipuláciu (DML, data manipulation language), indexoch, (materializovaných) views...

### Dotazovací jazyk SQL a jeho časti

Dotazovací jazyk SQL vychádza z [relačnej algebry](#relačná-algebra).

Obsahuje konštrukty na definíciu datového schémy, na manipuláciu s údajmi a na transakčné spracovanie (pozri ďalšie sekcie).

V niektorých systémoch má prostriedky na procedurálne programovanie, PL/SQL (napríklad Oracle).

SQL môže obsahovať spúšťače, teda dodatočné akcie, ktoré sa majú vykonať pri určitom príkaze (INSERT, UPDATE, DELETE). Používajú sa napríklad na udržiavanie history table, alebo na aktualizáciu `updated_at`, ak to nepodporuje daný RDBMS.

Pri práci s SQL používame prepared statements, aby sme predišli SQL injection.

## Jazyk definície datového schémy, DDL (3/7)

*Poznámka: rôzne RDBMS podporujú rôzne typy. Napríklad TEXT v základe SQL definovaný nie je, ale v praxi je používanie VARCHAR2 s fixnou dĺžkou príliš nepraktické, preto ho tu uvádzam*

Tvorba tabuľky:

```sql
/* Blokový komentár */
-- Inline komentár
CREATE TABLE Products (
          id          INT PRIMARY KEY, --napríklad u pg je možné použiť SERIAL, aby sme si nemuseli robiť sekvencie
          cost        INT NOT NULL,
          ean         INT UNIQUE NOT NULL,
          name        TEXT NOT NULL,
          description TEXT,
          created_by  INT NOT NULL REFERENCES User(id)
            updated_at  DATETIME,
);
```

V praxi je lepšie si vždy generovať primárne kľúče - externé unikátne hodnoty nemusia byť vždy tak unikátne/nemenné. Je lepšie používať čísla, ako stringy (stačí jedna operácia porovnania => rýchlejšie, zvlášť, keď ide o PK). Compound primary key je možný, ale opäť bývá pomalší.

Na generovanie ďalších hodnôt ID sa predtým používali sekvencie, dnes stačí hodiť `SERIAL`, alebo `AUTOINCREMENT`.

Na dátum/čas používame DATETIME. Ak by sme použili INTy & unix timestamp, v roku 2038 by sme mali problém.

U cudzích kľúčov môžeme špecifikovať `ON DELETE` `CASCADE` (so zmazaním popoužívateľa sa zmažú aj ním pridané produkty), `SET NULL` (so zmazaním popoužívateľa sa nastaví `created_by` na NULL, čo ale kvôli našemu constraintu nepôjde). V aktuálnej konštelácii daného popoužívateľa nemôžeme zmazať.

Modifikácia tabuľky:

- pridanie stĺpca, odobranie stĺpca, zahadzovanie tabuľky (zlyháva, ak na ňu sú referencie z iných tabuľiek)

```sql
ALTER TABLE Products ADD picture TEXT;
ALTER TABLE Products DROP COLUMN description;
DROP TABLE Products;
```

Je možné používať `IF EXISTS` a `IF NOT EXISTS`, aby nám skript nepadal pri opakovaných createch/dropoch, ale to sa hodí hlavne na hraní si.

V produkcii používame migračnú schému obsahujúcu UP a DOWN skripty, aby sme mohli prípadne akcie vrátiť.

## Jazyk manipulácie s údajmi, DML (4/7)

### Insert

```sql
INSERT INTO Tabulka(sloupec_a, sloupec_b)
VALUES (hodnota_a, hodnota_b);
```

Kontrolujú sa integritné obmedzenia, v prípade autoincrement/serial kľúča ho nie je potrebné explicitne uvádzať. Zvyčajne príkaz vracia vložené údaje (vrátane vygenerovaných hodnôt).

### Update

```sql
UPDATE Tabulka
SET sloupec_a = hodnota_a
WHERE ... --často kľúč
```

Update bez WHERE môže vykonať update všetkého. Kontrolujú sa integritné obmedzenia postihnutých stĺpcov

### Delete

```sql
DELETE FROM Tabulka WHERE ...
```

Delete bez WHERE môže vykonať zmazanie celého obsahu

### Select

Trocha nabušený select:

```sql
SELECT DISTINCT Tabulka.sloupec, B.sloupec
FROM Tabulka
JOIN TabulkaB AS B ON Tabulka.cizi_id = B.id
WHERE price > 0
ORDER BY sloupec ASC
```

*Join sa dá prepísať pomocou WHERE*

Výsledok selectu sa dá dať do zátvoriek a používať namiesto nejakej tabuľky, údaje majú stále tabuľný štruktúru.

Medzi údajmi s rovnakou štruktúrou sa dajú vykonávať množinové operácie `UNION`, `INTERSECT`, `MINUS`.

U `WHERE` môžeme používať aj príslušnosť v množine hodnôt `IN`, rozsahu `BETWEEN ... AND ...`, logické operátory `AND`, `OR`... U stringov `LIKE` kde `?` zastupuje znak a `%` niekoľko znakov.

### Pohľad/View

- Uložený a pomenovaný select, ktorý sa vykoná s provedením dotazu
- view majú obmedzenú modifikáciu údajov (napríklad nemožno, ak obsahuje agregáciu, distinct, union...) => je lepšie použiť zdrojové tabuľky

### Materializovaný pohľad/view

- View, ktorého výsledok sa počítavopočítaví. Vrátia sa potom hodnoty priamo z novej tabuľky, ale s každou zmenou je potrebné materializovaný view prepočítať (rýchlejšie čítanie, pomalší zápis).

### Agregačné funkcie

Používané s `GROUP BY sloupec/sloupce`

*Ak nepoužijeme `GROUP BY`, počítajú sa agregačné funkcie z SELECTu*

- `COUNT(...)` - počet riadkov, je možné použiť `COUNT(*)`
- `AVG(...)`
- `SUM(...)`
- `MIN(...)`
- `MAX(...)`

Je možné používať `HAVING ...`, čo je `WHERE`, ale s používaním agregačných funkcií.

## Relačná algebra, integritné obmedzenia, riadenie transakcií (5/7)

### Relačná algebra

> *[@thes01](https://github.com/thes01): viac aj na [tomto odkaze (bc štátnice)](https://docs.google.com/document/d/1SVbwwMDDfOCqAdsfTH1RDJex9_fZZ96wb0Vp2fSoUFs/edit)*

**Relácia** je podmnožinou kartézskeho součinu domén. Toto sa premietne do databázy tak, že domény sú dátové typy stĺpcov a tabuľka (zložená zo stĺpcov) obsahuje len tiež kombinácie hodnôt (riadky), akých sú v relácii.

Na relačné operácie používame relačnú algebru skladajúcu sa z:

- **množinových operácií** (ale na zjednotenie, rozdiel a prienik musia byť relácie kompatibilné, tj. mať rovnakú hlavičku)
- **projekcie** - tj. výber stĺpcov
- **selekcie** - tj. WHERE
- **premenovania** - AS
- **spojenie/join/súčin relácií** - JOIN
- **zoskupenia a agregácie** - GROUP BY, AVG(...)...

...jednotlivé operácie teda zodpovedajú dotazovacímu jazyku SQL.

Existujú dotazy, ktoré nie sme schopní vyjadriť relačnou algebrou, napríklad tranzitívny uzáver.

*Tranzitívny uzáver nad relácií získame tak, že sa dívame na prvky množiny v relácii. Ak je `a` v relácii s `b` a `b` v relácii s `c`, potom (aby bolo dosiahnuté tranzitivity) tranzitívny uzáver obsahuje reláciu `a` s `c`.*

### Integritné obmedzenia

Súčasť DDL, jazyka definície údajov. Určitým spôsobom obmedzujú, akých hodnôt môžu polia nadobúdať. Napríklad `NOT NULL`, `UNIQUE`, `FOREIGN KEY .. REFERENCES ..(..)`, `CHECK(price>0)`... Uvádzajú sa na príslušný riadok (ideálne), tabuľky, ako dodatočný riadok tabuľky, alebo ako samostatný výraz `ALTER TABLE .. ADD CONSTRAINT ... NOT NULL (id)`.

### Riadenie transakcií

Transakcie v RDBMS majú ACID vlastnosti:

- **Atomicity** - skupiny príkazov transakcie brané ako jednotka; vykonajú sa všetky, alebo žiadny
- **Consistency** - po vykonaní transakcie je db v konzistentnom stave, nie je porušené žiadne integritné obmedzenie
- **Isolation** - transakcia je izolovaná od ostatných transakcií, je možné nastaviť úrovne transakcie, podľa toho môže transakcia skončiť chybou (ak došlo k modifikácii rovnakého objektu, aký modifikovala iná transakcia), alebo sa využijú uzamykacie mechanizmy
  * **Dirty Read (Špinavé čítanie):** Transakcia T1 čita údaje, ktoré transakcia T2 zmenila, ale ešte nepotvrdila (COMMIT). Ak T2 urobí ROLLBACK, T1 pracovala s neexistujúcimi údajmi.
  * **Non-repeatable Read (Neopakovateľné čítanie):** Transakcia T1 načita riadok. Transakcia T2 tento riadok zmení a potvrdí (COMMIT). Ak T1 načita rovnakú čiaru znovu, dostane iné hodnoty.
  * **Phantom Read (Fantomové čítanie):** Transakcia T1 načita množinu riadkov spĺňajúcich podmienku (napríklad `price > 100`). Transakcia T2 vloží (INSERT) nový riadok spĺňajúci túto podmienku a potvrdí. Ak T1 dotaz zopakuje, objaví sa tam nový „fantomový" riadok.
- **Durability** - údaje sú po vykonaní transakcie trvalo uložené

Transakcie sa potvrdzujú príkazom `COMMIT`, vrátia príkazom `ROLLBACK` na stav pred začatím transakcie, či po poslednom `SAVEPOINT`

#### Ako sa izolácia a trvanlivosť implementuje v praxi:
* **2PL (Two-Phase Locking):** Tradičné pesimistické zamykanie. Transakcia v prvej fázy zámky len získava (zdieľané na čítanie, exkluzívne na zápis) a v druhej fázy po COMMITe ich uvoľňuje. Spôsobuje zablokenie čitateľov písateľom a naopak.
* **MVCC (Multi-Version Concurrency Control):** Moderný optimistický prístup (PostgreSQL). Písatelia neblokujú čitateľov. Pri zmene riadku sa nevytvára prepis, ale nová verzia riadku s informáciou o čase/transakcii (`xmin`, `xmax`). Každá transakcia potom vidí „snímok" (snapshot) údajov zodpovedajúci ho začiatku. Staré verzie čistí na pozadí proces (v PG napríklad `VACUUM`).
* **WAL (Write-Ahead Logging) / Žurnálovanie:** Zabezpečuje **Durability**. Kým sa zmenené údaje (dirty pages) zapíšu z RAM na pomalý disk do samotných tabuliek, zapíše sa sekvenčný záznam o zmene do logu na disku (WAL). Zápis do WAL je extrémne rýchly (iba append). Ak systém spadne, Transaction Manager pri štarte prejde WAL a vykoná operáciu **REDO** (pre potvrdené transakcie) a **UNDO** (pre rozpísané transakcie, ktoré nestihli COMMIT).

## Indexovanie, hašovanie (6/7)

### Indexovanie

Index slúži na zrýchlenie/zefektivnenie často používaných dotazov nad tabuľkou. Dotazy obsahujúce zvolený stĺpec (alebo ich kombináciu) budú rýchlejšie. Štruktúra <kľúč, pointer na záznam>

```sql
CREATE INDEX my_index ON Products (Price)
```

Na indexy sa môžu používať:

- **tradičné indexy** - ako v knihách, odkazy na riadky s danou hodnotou, je možné robiť viacero úrovní indexov, používať rôzne indexové usporiadania...
- **haše** - na získanie jednotlivej hodnoty veľkých údajov, neumožňujú range scans alebo ordering.
- **B+ stromy** - každý uzol obsahuje odkazy na uzly nižšie, alebo hodnoty (ide o listový uzol). Hodnoty sú v listoch vzostupne usporiadané, uzly v sebe majú aj informácie o intervaloch daných odkazov/hodnôt, listy sú provázané. najviac používané.
  ![](img/20230526220652.png)
Špeciálne n-árne vyvážené stromy optimalizované na bloková diskové úložiská. 
    * **Kľúčový rozdiel oproti B-stromom:** Vnútorné uzly (internal nodes) obsahujú **len navigačné kľúče a pointery** na ďalšie uzly, ale neobsahujú samotné údaje riadkov (ani pointery na údaje). Všetky údaje/pointery na reálne riadky sú uložené **výhradne v listových uzloch (leaf nodes)**.
    * **Prečo sú ideálne pre DB:** 
      1. Vnútorné uzly sú vďaka absencii údajov malé $\rightarrow$ do jednej diskovej stránky (8 KB) sa zmestí obrovské množstvo navigačných kľúčov $\rightarrow$ strom má obrovský vetvící faktor (**High Fan-out**) a je veľmi nízky (zvyčajne výška 3 až 4 dokonca pre milióny záznamov). Na nájdenie akéhokoľvek záznamu stačí max 3–4 diskové operácie (I/O).
      2. Všetky listové uzly sú **obojsmerne lineárne provázané** (linked list). Ak DB vykonáva rozsahový dotaz (`WHERE price BETWEEN 10 AND 50`), vyhľadá prvok `10` a potom už len sekvenčne čita susedné listy, nemusí sa vracať nahoru do stromu (tzv. Range Scans sú extrémne rýchle).
- **B stromy** - podobné ako B+, ale uzly môžu obsahovať aj hodnoty, nielen odkazy na ďalšie uzly. Listy nie sú provázané, ale sú na rovnakej úrovni, inak podobné ako B+.
- **R stromy** - podobné ako B+, ale sú viacedimenzionálne, v 2D fungujú ako obdĺžniky. Údaje sú v listových uzloch stromu. Rodič uzla zahrnuje všetkých svojich potomkov (v 2D ide o väčší obdĺžnik, ktorý obsahuje potomkov). Ideálne je, ak zaberajú rodičovské obdĺžniky čo najmenej priestoru - rodič totiž ako index redukuje oblasť potrebnú na prohľadávanie (hovorí *hľadaj vo mne!*). Napríklad pre geodáta.
  ![](img/20230526220927.png)
  ![](img/20230611232516.png)

Ďalšie delenie indexov:

- **dense/hustý** - každý riadok je zaindexovaný, zabiera viac miesta, ale hľadanie je rýchlejšie. môže ukazovať na [kapsu](#kapsy) - skupinu riadkov s rovnakým kľúčom, ktorá sa prechádza lineárne.
- **sparse/riedky** - len niektoré riadky zaindexované, zabiera menej miesta, ale hľadanie pomalšie (je potrebné dohľadať konkrétny riadok)

### Hašovanie

**Cieľom hašovania je previesť vstupné údaje ľubovoľnej dĺžky na výstup jednotnej dĺžky (fixed-length reťazec, alebo číslo), hash.** Z hashe by nemalo byť možné odvodiť vstup (**jednosmernosť**), pre každý vstup by sme mali byť schopní deterministicky (vstupom sú len údaje) určiť jediný hash. Zároveň môže byť (podľa využitia) cieľom minimalizovať riziko kolízie, teda že dva vstupy majú rovnakú hash (nemožno sa tomu ale vyhnúť, pretože musíme byť schopní mapovať nekonečnosť možných vstupov na obmedzenú veľkosť výstupov danú dĺžkou). Podľa využitia môže byť tiež dôležité, aby podobné vstupy mali zásadne rozdielne haše, aby bolo možné ľahko odhaliť drobnú (zámernú či nechcenú) modifikáciu vstupu. Na prolomenie hašov sa používajú rainbow tables, obsahujúce pre daný algoritmus známe vstupy a ich haše.

Hašovanie sa používa na zabezpečenie integrity údajov (certifikáty, checksum), rýchle porovnávanie údajov (HashMap), porovnávanie údajov so znalosťou len hashe (uchovávanie hash hesiel v databáze, Argon2).

#### Bezkoliznosť

- **slabá** - pre vstup A nie sme schopní v rozumnom čase nájsť rozdielny vstup B, ktorý by mal rovnakú hash
- **silná** - nie sme schopní v rozumnom čase nájsť ľubovoľné dva rozdielne vstupy s rovnakou hashou

Na rôzne účely používame rôzne algoritmy, ide o balancia rýchlosti (u hesiel môže byť požadovaná pomalnosť) a bezpečnosti/pravdepodobnosti kolízie.

- **MD5** - relatívne rýchly, nie je bezpečný (možno rýchlo nájsť kolízie aj na bežnom počítači).
- rodina Secure Hashing Algorithm, za bezpečnú sa momentálne považuje **SHA-2** (SHA256, SHA512, SHA-384...)
- **Argon2** - v súčasnosti odporúčaný na hašovanie hesiel
- hashem (hlupavý, ale rýchly) môže byť napríklad aj dĺžka vstupu, modulo, súčet ascii hodnôt znakov... (nazýva sa [Cyclic redundancy check](dev_4_bezpecny_kod.md#notes))

#### Databázové (nekryptografické) vs. Kryptografické hašovanie (Švendov štátnicový chyták)
U zkoušky (dr. Švenda) musiete striktne rozlišovať účel hašovania:
* **Indexové / HashMap hašovanie:** Používa sa na Hash Indexy v DB. Cieľom je **maximálna rýchlosť** výpočtu a rovnomerná distribúcia do pamäťových kapies (buckets). Používajú sa algoritmy ako *MurmurHash* alebo *CityHash*. 
* **Prečo sú tu kryptografické funkcie (SHA-2, SHA-3) nevhodné?** Sú na indexovanie zbytočne výpočetne extrémne drahé (**overkill**). U indexu nepotrebujeme vlastnosti ako jednosmernosť alebo odolnosť proti nájdeniu preimage (nikto sa nesnaží z hashe v indexu zpätne hacknúť hodnotu ID).

#### Riešenie kolízií a typy hašovania v DB
Keď dve rozdielne hodnoty vygenerujú rovnakú kapsu indexu (bucketu), nastáva kolízia. Riešia sa:
1.  **Zretazené hašovanie (Chaining / Kapsy):** Každá kapsa ukazuje na spojový zoznam (kapsu) záznamov. Ak sa zaplní, lineárne sa prechádza alebo sa napojí pretoková kapsa.
2.  **Otvorená adresácia (Open Addressing):** Ak je kapsa obsadená, hľadá sa podľa definovaného pravidla (Linear Probing) ďalšie voľné miesto priamo v hlavnom poli.

Podľa správy veľkosti poľa delíme hašovanie na:
* **Statické hašovanie:** Počet kapies je fixný. Pri zaplnení databázy rýchlo rastie počet kolízií a výkon degraduje (dlhé spojové zoznamy v kapsách).
* **Dynamické hašovanie (Extensible / Linear Hashing):** Veľkosť hašovacej tabuľky sa dynamicky prispôsobuje (rastie/zmenšuje) počtu údajov. Využíva sa bitová reprezentácia hashe. Pri reorganizácii (split bucketu) sa neprepočítava celá tabuľka, ale delí sa vždy len jedna konkrétna kapsa.

## Príklady z praxe pre všetko vyššie uvedené (7/7)

*Poznámka: Praktické príklady sú integrované v jednotlivých sekciách vyššie. Táto sekcia slúži ako prehľad praktických aspektov:*

### Praktické aspekty ukladania údajov
- Výber medzi súborovým systémom a databázou podľa typu a štruktúry údajov
- Používanie CDN na statický obsah a databázy na štruktúrované údaje
- Implementácia migračných skriptov v produkčných prostrediach

### Praktické SQL dotazy a optimalizácia
- Používanie indexov na zrýchlenie časté používaných dotazov
- Prepared statements na prevenciu SQL injection
- Spúšťače na automatizáciu (napríklad aktualizácia `updated_at`)

### Praktické aspekty integrity a transakcií
- Cascading deletes vs. soft deletes v produkčných systémoch
- Používanie transakcií na zabezpečenie konzistentnosti pri zložitých operáciách
- Monitoring a registrovanie databázových operácií

### Praktické aspekty výkonu
- Profiling databázových dotazov
- Sharding a replikácia na škálovanie
- Používanie materializovaných views na zložité analytické dotazy

## Poznámky
### Kapsy
do kapsy sa umiestňujú kolidujúce prípady. kapsa sa prechádza lineárne. na kapsu s vyčerpanou kapacitou možno napojiť pretokovú kapsu, týchto môže byť viac, ale musia sa zretaziť.

[Prejdi na ďalšiu otázku](./5_pocitacove_site.md)
