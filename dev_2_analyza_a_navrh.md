# Analýza a návrh systémov

> Objektové metody návrhu informačních systémov. Špecifikácia a riadenie požiadaviek. Softvérové architektúry, komponentové systémy. Návrhové a architektonické vzory. Rozhrania komponent, kontrakty na úrovni rozhrania, OCL. Modely softvérových systémov, jazyk UML. Príklady z praxe pre všetko vyššie uvedené. (PA103, PV167 || PV258 || PV293)

1. [Objektové metody návrhu informačních systémov (1/6)](#objektové-metody-návrhu-informačních-systémov-16)
2. [Špecifikácia a riadenie požiadaviek (2/6)](#špecifikácia-a-rízení-požiadaviek-26)
3. [Softwarové architektúry, komponentové systémy (3/6)](#softvérové-architektúry-komponentové-systémy-36)
4. [Návrhové a architektonické vzory (4/6)](#návrhové-a-architektonické-vzory-46)
5. [Rozhrania komponent, kontrakty na úrovni rozhrania, OCL (5/6)](#rozhrania-komponent-kontrakty-na-úrovni-rozhrania-ocl-56)
6. [Modely softvérových systémov, jazyk UML (6/6)](#modely-softvérových-systémov-jazyk-uml-66)

## Objektové metody návrhu informačních systémov (1/6)

Prístupy a postupy k návrhu IS založených na objektove orientovaném paradigmatu, kde sú objekty spojením dát a metod nad temito daty.

Pri modelovanie systémov je dobré definovat si jednotný jazyk, ktorý reflektuje skutečnou terminologii pre danou doménu problému. Popodľa toho volíme jména funkcií/tríd, aby bolo pokaždé všem (od doménových expertu po vývojáre) jasné, o čem se mluví. Podstatná jména používaná v jednotném jazyce zvyčajne v kódu reflektují trídy/rozhrania, slovesa zase metody/funkcia.

Objektové paradigma si dobre rozumí s principy abstrakce, což možno aplikovat nejen na úroveň objektu, ale i komponentu - základnéch stavebních jednotek, ze kterých se skládá Architektúra systémov.

Mezi metody se radí:

- modelovanie domény pomocí [UML](#modely-softvérových-systémov-jazyk-uml-66), v rôznych častiach vývoje se zabýváme rôznymi úrovnemi detailu
- dekompozice systémov do menších, koherentnéch částí
- aplikace návrhových a architektonických vzoru, ktoré popisují riešenie na dobre známé a často se opakující problémy v (nejen) objektovém svete.

## Špecifikácia a riadenie požiadaviek (2/6)

Požadavky na systém se delí (zvyčajne je medzi kategoriemi tenká hranice a závisí i na formulaci) na:

- **Funkčné (functional) požadavky** - jaké funkcia zákazník od systémov očekává, jedná se o business logiku, popopoužívateľské požadavky, reší se programove, v implementaci
- **Nefunkčné (non-functional/quality) požadavky** - jaké technické nároky sú na systém, použité technologie, OS, garance dostupnosti (availability), response time, internacionalizace a lokalizace, reší se návrhom, architektúrou i kódem

### Současti riadenie požiadaviek

- **Porozumení doméne problému**
- **zber požiadaviek od stakeholderu** - kľúčem je pýtať se PROČ, ne CO a JAK
- **Analýza a jednání** (hej, toto nie je možné/hej, nestačilo by vám to udelat takto?...)
- **Špecifikácia požiadaviek** - úprava do jednoznačné/formální podoby (use case). Je jasné, v jakém momente môžeme považovat za splnený.
- **Validace požiadaviek** - overenie, že formalizované požadavky odpovídají skutečným potrebám
- **Prioritizace požiadaviek** - umožňuje soustredit se na kritické časti (podľa potreb zákazníka) a blbosti prípadne vynechat, ak nebude čas/rozpočet.

### Vlastnosti dobrého požiadaviek

Dobrý/dobre specifikovaný požadavek:

- reflektuje skutečné potreby zákazníka a je v nem obsaženo PROČ (abychom mohli vybrat nejvhodnejší riešenie, ale muže obsahovat návrhy)
- má jasné kritérium splnení, je meritelný a testovatelný
- má prioritu
- je úplný

Obecne platí, že čím pozdeji se požadavek zmení, tým nákladnejší bude jeho implementácia.

### Modelovanie a formalizace požiadaviek

Požadavky se modelují pomocí **use case diagramu**, uchovávají se v **use case dokumentu** (forma: id, jméno, actor(s), popis, trigger, pre/post conditions, príklad typického flow, priorita, výnimky, častost používanie...). Požadavky sú tiež formalizovány v jednoduché forme pomocí **user stories** - krátké, výstižné popisy (As `role` I want to `akce` So I can `zdôvodnení`), srozumitelní zákazníkovi (+ obsahují akceptačné kritéria, prioritu, story pointy...).

### Určenie priority požiadaviek

Pro **určenie priority požiadaviek** možno použiť napríklad:

- klasické ohodnocení 1-10
- binární strom - požadavky sú uchovávány v uzlech. Vkládaný požadavek srovnáváme s uzly od korene. Ak je vkládaný požadavek prioritnejší, jdeme doprava. Jinak jdeme doleva. Vložený požadavek bude listem stromu.
- MoSCoW - požadavky delíme na Must (kritické), Should (duležité), Could (bolo by fajn mať) a Won't (aktuálne to nemáme v plánu)

Non-functional requirements platí vždy, je napríklad je brát v potaz i s nove príchozími functional požadavky => máme pre ne vyhrazené místo (napr. wiki), kde sú dukladne popsány. Mužeme na konkrétné NFR poukázat v user stories (napr. u FR `jako používateľ chci mať prístup k aktuálním dátamm senzoru` linkneme NFR `systém poskytne odezvu do vteriny` a `dáta ze senzoru se do systémov dostanou nejpozdeji minutu po namerení`).

## Softvérové architektúry, komponentové systémy (3/6)

SW Architektúra určuje, akým spôsobem je systém strukturován, akým spôsobem je delen na komponenty/moduly a ako medzi sebou jednotlivé komponenty/moduly interagují a ako sú jednotlivé časti systémov nasazeny na hw.

SW architektúry (vyšší úroveň abstrakce) a architektonické vzory (nižší úroveň abstrakce) sú obecná riešenie architektur systémov. Uvádím jen seznam, podrobne sú popsány v [časti otázky 1](dev_1_programovani_a_softwarovy_vyvoj.md#základné-koncepty-softvérových-architektur-z-pohledu-implementácia-26)

### Architektonické vzory

- **MVC/MVP/MVVM pattern**
- **Klient-Server**
- **Peer-to-Peer**
- **Layered architecture** - vrstvená Architektúra používá architektonický vzor Repository
- **Microkernel**
- **Pipes and filters**
- **Blackboard** - tabule je sdílená, sú na ní dáta. Výpočetné agenti k tabuli pristupují a spracovávajú dáta podľa svých interních strategií. Klient následne vybere agenta, ktorý prišel s nejlepším riešením, na základe čehož se aktualizují dáta na tabuli. Nedeterministický výpočet. napr. použití rôznych algoritmu u kterých nevíme, jaký je nejlepší.
- **SOA**
- **Microservices**

### Komponentové systémy

komponenty sú spustitelné softvérové jednotky, ktoré majú definované komunikačné rozhrania, do vnitrního fungovanie nevidíme/nezaujíma nás. Komponent by mel poskytovat logicky související funkcionalitu, funguje jako vrstva abstrakce. komponenty mohou byť vyvíjeny nezávisle na jiných komponentách, sú nahraditelné (stačí splnit rozhrania a jeho kontrakt), znovupoužitelné. komponenty mohou mať vnitrní stav, ten však muže delat problém u škálovanie (paralelizací komponentu), mohou byť asynchronní, môžu sa interne skládat z dalších komponentu...

Ak systém vystavuje rozhrania používaná i nekým jiným (klient), je fajn neakým spôsobem verzovat rozhrania. Vďaka tomu se predejde problémum pri pridávanie zmen, nejakou dobu totiž môžeme podporovat viac rozhrania, než se klient aktualizuje na novou verzi.

## Návrhové a architektonické vzory (4/6)

Návrhový vzor je obecné riešenie k často se opakujícímu problému rešenému pri návrhu sw, nie je ponapríklad kompletne vymýšlet vlastné riešenie. Slouží nejen jako obecný návod pre implementaci, ale umožňují snadnejší komunikaci v rámci týmu (napr. tady použijeme Strategy pattern). vzory je napríklad používat s rozvahou, občas mužou byť zbytečne obecné.

*Architektonické vzory sú popsány v [predchozí podotázke](#softvérové-architektúry-komponentové-systémy-36)*.

[Pre pochopení a ukázky kódu](https://refactoring.guru/design-patterns)

### Creational patterns

Řeší tvorbu a inicializaci objektu, poskytují jednoduché rozhrania skrývající zložitú inicializaci.

#### Singleton
Zajišťuje, že daný objekt existuje v systémov jen jednou (globálné stav). V OO jazycích se reší pomocí trídy s private constructorem a se statickou metodou `instance()` poskytující prístup k objektu drženému ve statickém atributu. *Metoda `instance()` se zvyčajne stará i o inicializaci statického atributu*

Singleton je mnohdy považován za antivzor, pretože vytvárí globálné stav (namísto predávanie stavu parametry) - blbe se to testuje, muže byť nutné zamykanie globálneho stavu pre thread safety, narušuje se single responsibility principle (singleton trída ovládá svou tvorbu).

Napr. DB pool

![](img/20230603121311.png)

#### Factory method
Stará se o tvorbu konkrétních instancí objektu podľa instance továrny (tj. máme interfaces VehicleFactory a Vehicle. CarFactory bude delat Car, zatiaľ čo rovnaké volání metody u PlaneFactory vytvorí Plane). Používá se ak potrebujeme flexibilní a rozširitelný spôsob vytvárení objektu, alebo chceme oddelit logiku tvorby objektu od zbytku. Nevýhodou je nutnost tvorby nové Factory trídy a rozhrania.

![](img/20230604152821.png)

#### Abstract factory
Podobná factory method, ale je zodpovedná za viac produktu. Instance této factory zajišťuje tvorbu vzájemne kompatibilních produktu.

![](img/20230605121553.png)

#### Prototype
Doslova trait `Clone`, vytvorí identickou kopii nejakého již existujícího objektu. Hodí se, ak inicializace objektu je náročná, alebo neznáme konkrétné instanci (pracujeme s abstrakcí pres interface).

![](img/20230604183448.png)

#### Builder pattern
Ke konfiguraci objektu pri inicializaci používáme (deklarativním spôsobem) metody príslušného `Builder` objektu, každá se stará o jeden aspekt.

Napr. Inicializace http požiadaviek

```rust
let request = HttpRequest::get("www.mysite.com/content")
    .header("Authorization", "Bearer 8sa96d41a5s3fbwn")
    .queryParam("offset", 42)
    .build();
```

![](img/20230604183525.png)

### Structural patterns

Řeší kompozici objektu do hierarchií, oddelení rozhrania a implementácia.

#### Composite
Umožňuje tvorbu stromových struktur a poskytuje jednotné rozhrania k operaci na podstromu definovaném svým korenem. `Component` je buď list `Leaf`, alebo uzel `Composite` obsahující potenciálne další `Component`y.

Napr. stavební prvky grafických rozhrania

![](img/20230603143753.png)

#### Adapter
A.k.a. Wrapper - zapouzdríme/poskytneme rozhrania nekompatibilní jednotce tak, aby se dala použít v našem systémov.

Napr. integrace knihovny, prípadne môžeme adaptér použít k prevodu medzi formáty (XML - JSON)

Adaptér možno implementovat ve všech populárních jazycích jako wrapper, je možná i implementácia class adaptéru v jazycích podporujících mnohonásobnou dedičnost.

![](img/20230603161229.png)

#### Bridge
Používá se k rozbití tightly coupled jednotek (alebo skupiny jednotek) pomocí abstrakcí (ty mohou mať viac implementací, ale často nám bridge pomuže jen vďaka vytvorení abstrakce).
Abstrakce obsahuje instanci _implementácia_, ktorá je volána v metodách _abstrakce_. Vďaka tomu môžeme snadno menit implementaci, aniž bychom menili _abstrakci_.

![img.png](img/bridge_pattern.png)

[//]: # (![]&#40;img/20230604142514.png&#41;)

#### Decorator
Umožňuje rozšírit trídu, pridat k ní rôzne metody/atributy na základe použitého dekorátoru, dynamicky je pridávat/odebírat. Obdobne jako Adapter muže obalit puvodné komponent, ale nemení rozhrania komponentu.

Napr. BufReader pre bufferované čítanie (ze súborov), BufReader obaluje Reader a pridává buffer.

![](img/20230604142455.png)

#### Proxy
Prostredník medzi objektem a volajícím, transparentne predává zprávu (a muže provádet další operace, hlídat prístup k objektu, provést alokaci objektu on-demand...).

![](img/20230605125209.png)

#### Facade
Poskytuje jednotné (a jednoduché) rozhrania složitejšímu subsystému.

![](img/20230605125311.png)

#### Flyweight
Sdílený objekt použitý na viac místech - sdílený stav je uchováván v objektu, kontextuální stav se dodá skrz parametry volané metody. Slouží k úspore pameti a/alebo výpočtu (ak je inicializace drahá).

Napr. DB pool

![](img/20230605130130.png)

### Behavioral patterns

Řeší chovanie objektu a dynamické interakce medzi objekty.

#### Iterator
Poskytuje jednotné rozhrania k pruchodu prvky kolekcí. Je to samostatný objekt (specifický pre danou strukturu), má metody jako `current()` a `next()` umožňující prístup k prvku, alebo posunutí interního ukazatele iterátoru na další prvek.

Napr. implementácia `for-in/foreach`.

![](img/20230603144800.png)

#### Strategy
Poskytuje rozhrania k výpočtu/operaci, ktoré muže klient použít bez znalosti konkrétné implementácia a jejích detailu. Vďaka tomu je možné konkrétné implementácia pre výpočet snadno menit, alebo jednotne používat funkcionalitu objektu s rozdílnými implementáciami. Klient pristupuje pres `Context`, ktorý se stará o prípadnou volbu strategie. Konkrétné strategie možno menit za behu.

Napr. libovolné použití prístupu pres rozhrania, napríklad výpočet trasy (pre auto, pre cyklistu, pre chodce...)

![](img/20230603153352.png)

#### State
Obdobný jako Strategy, výber implementácia deláme na základe aktuálního stavu, ktorý je možné menit za behu. O konkrétné stav (a výber implementácia) a jeho premeny se stará `Context`, vďaka čemuž izolujeme a môžeme jednoducho kontrolovat prechody stavu v systémov.

Na rozdíl od `Strategy`:
- daná implementácia je vybrána na základe vnitrního stavu
- rešíme prechody stavu, stavy se mužou nahradit jiným stavem (=> stavy mohou mať referenci na kontext)
- nerešíme jeden specifický task, ale poskytujeme implementaci pre vetšinu vecí co `Context` nabízí
- i konkrétné `State` muže vedet o dalších stavech a muže sám spustit prechod do jiného

Napr. Vypínač má dva stavy (concrete state), Vypnutý Vypínač a ZapnutýVypínač. Interface Vypínač má metodu prepni(), čímž se zmení stav (VypnutýVypínač na ZapnutýVypínač a opačne)

![](img/20230603154910.png)

#### Memento
Uchovává predchozí stavy objektu, vďaka čemuž je možné prenést objekt do drívejšího stavu. Používá se pre prípady, kdy prímý prístup do atributu trídy nie je možný (private atributy).

Napr. použití pri implementaci UNDO.

![](img/20230605132549.png)

#### Observer
Umožňuje tvorbu mechanismu pre notifikace. Observery se registrují ke sledovanie Subjektu (ukládáme si reference observeru do vektoru). V momente, kdy se subjekt zmení (a mely by byť observery notifikovány), stačí zavolat metodu notify, ktorá projde observery a každého notifikuje (zvyčajne zavoláním metody).

Používá se pre nahrazení pollingu (opakovane se ptám "už se událost stala?").

![](img/20230605162806.png)

#### Visitor
Poskytuje jednotné rozhrania pre spuštení nejaké shodné akce nad objekty. Každý objekt má implementaci odlišnou, ale signatura pre všetkochny objekty je shodná (napr. serializace rôznych struktur, bere Self, vrací String). Namísto abychom na základe typu struktury volali príslušnou metodu (`if let Vehicle::Car(_) = my_dáta { return serialize_car(my_dáta); }`), implementujeme metodu poskytnutou rozhraniam (jen `serialize(&self)`). V diagramu je to metoda `accept(v: Visitor)`.

Napr. serde

![](img/20230605165644.png)

## Rozhrania komponent, kontrakty na úrovni rozhrania, OCL (5/6)

Aby mohl komponent komunikovat se svým okolím (byť volán a prípadne vracet dáta), potrebuje nejaké verejné rozhrania, kterému se ríká **signatura**. Skladá se z poskytovaných operací (funkcií/metod) a ich vstupních a výstupních parametru.

U rozhrania nás zajímajú i další obmedzenie, ktoré mohou upravovat (správné) používanie rozhrania (*napr. používateľ se muže registrovat jen jednou*). Signature a obmedzenie se souhrnne ríká **kontrakt**. Kontrakt popisuje poskytnutou funkcionalitu za predpokladu, že dodržíme predem stanovené podmínky.

### Současti kontraktu

Součástí kontraktu (v kontextu struktur/objektu) mužou byť:

- **preconditions** - co musí platit pred vyvoláním dané metody, aby metoda probehla správne (napr. máme dost penez na účtu)
- **postconditions** - co musí platit po skončení dané metody, tj. co metoda poskytuje (napr. probehne platba, z účtu se nám odečte príslušná platba)
- **invariants** - co vždy musí platit, váže se zvyčajne k objektum, nejen metodám (napr. na debetním účtu nie je možné ísť do mínusu)

### OCL (Object Constraint Language)

**OCL (Object Constraint Language)** je deklarativní jazyk, ktorý umožňuje popis kontraktu a ich constraintu (obmedzenie domén hodnot), včetne ich zavedení do UML, a muže byť použit i pre ich vynucovanie (napr. generovanie kódu na základe kontraktu popsaného v komentári/anotacích (v Jave `@`)).

Pri definici kontraktu objektu s dedičností nesmíme porušit Liskov substitution principle, dedic muže invarianty a postconditions iba utahovat, ne je rozvolňovat (co platilo pre rodiče, musí platit i pre potomka). Naopak je to u preconditions, kde muže dedic podporovat viac vstupu než predek.

Pre- a postconditions se vztahují k metodám, invarianty k objektum.

`@pre` se používá v postconditions pre odkaz na stav objektu pred voláním metody, `self` se používá pre odkaz na aktuálné instanci objektu.
Preconditions mohou byť ve zdedených trídách rozvolneny, postconditions a invarianty musí byť v dedicích utahovány - Liskov substitution principle.

#### Príklady OCL

Auto (trída Car) nesmí prekročit rychlost 240. `context Car inv: speed < 240` - speed a self.speed (kde self je Car) sú identické


Pred odebráním prvku musí zásobník neco obsahovat, vrací to co bolo na vrchu zásobníku

```ocl
context Stack::pop()
pre neniPrazdny: self.len() > 0
post vraciVrsekZasobniku: result = self@pre.top()
```

Po vložení prvku se zvetší zásobník

```ocl
context Stack::push(element)
post: self.len() = self@pre.len() + 1
```

V OCL možno používat funkcionální prístup ke kolekcím (select, forAll...), rešit existenci (exists), provádet množinové operace (union, intersection...), používat booleovské operátory (or, and, implies...) a spoustu dalšího (promenné, cykly...).

## Modely softvérových systémov, jazyk UML (6/6)

Modely sw systémov popisují systém vždy z nejakého zjednoduchoného pohledu (model je už z definícia abstrakce). Ruzné modely se zabývají rôznymi aspekty/fázymi vývoje systémov. Duležité však je, aby boli modely systémov vzájemne konzistentní. Obecne možno rozlišovat na modely popisující strukturu a modely popisující chovanie.

**UML** je modelovací jazyk umožňující jednotný spôsob vizualizace návrhu systémov. Pre snadné verzovanie je fajn PlantUML (píšeme UML jako deklarativní kód, ze kterého generujeme príslušné diagramy).

Príklad interface

![](img/20230605172409.png)

### Context diagram

Popisuje kontext a prostredia, v jakém systém má fungovat. Jsou zde znázorneny interakce s externími systémy a skupinami používateľu.

![](img/20230607124347.png)

Nerešíme časti, se kterými prímo neinteragujeme. Ty sú videt v [Ecosystem map](#ecosystem-map).

### Use case diagram

Zahrnuje všechny (používateľa i jiné systémy), kterí budú systém používat ve forme actoru. U každého actora vidíme dostupné akce (use case) a prípadne väzby medzi akcemi (<--extend, include-->, spuštení další akce).

| ![](img/20230607130528.png) | ![](img/20230607130605.png) |
|-----------------------------|-----------------------------|

### Conceptual class diagram

Diagram tríd, ale nerešíme datové typy ani metody. Zajímajú nás kľúčové entity (struktury/trídy), ich dáta plynoucí z požiadaviek, a väzby medzi entitami (kontext). Pomáhá ujasňovat terminologii.

### Class diagram

Statická reprezentace systémov ve forme tríd, zobrazuje ich metody, atributy a vzájemnou provázanost. Vztahy majú kardinalitu

**Asociace** - klasická šipka (alebo čára pre oboustranný vztah), popisuje vztah daných tríd
**Agregace** - bílý kosočtverec, popisuje, že trída obsahuje jinou trídu (u ní je kosočtverec)
**Kompozice** - černý kosočtverec, popisuje, že trída (s kosočtvercem) je nedílnou součástí jiné trídy

![](img/20230608120634.png)

![](img/20230608120112.png)

### Object diagram

Zachycuje systém za behu v určiťém čase, zobrazuje konkrétné objekty a ich väzby.

![](img/20230608121047.png)

### Activity diagram

Popisuje workflow systémov/komponentu (podľa úrovne abstrakce), jednoduchý na pochopení i pre zákazníka.

![](img/20230609000854.png)

### Sequence diagram

Popisuje interakce v čase medzi jednotkami (trídami/komponenty/actory) systémov

![](img/20230609001314.png)

### Deployment diagram

Popisuje jednotlivé komponenty systémov a ich komunikačné toky, včetne použitých technologií.

![](img/20230609001416.png)

### Component diagram

Popisuje komponenty a ich kompozici v systémov.

lollipop/Trídní notace

![](img/20230606160621.png)

Komunikačné rozhrania komponentu se nazývají porty, Priame spoje connectors.

![](img/20230606164944.png)

## Notes

**Verifikace vs validace** - validace overuje, že náš model odpovídá požiadaviekm, verifikace overuje, že naše implementácia odpovídá našemu modelov, že je implementácia kvalitní. Napr. u mostu by se validovalo, že je postavený v míste, kde je ponapríklad. Verifikovalo by se, že je postavený správne.

**Motivace objektových metod/návrhových vzoru**

- Systémy bývají zložité, špatne se udržují a je náročné Merať/zajistit kvalitu, často se mení nároky => pomuže dekompozice systémov do menších koherentnéch částí, ktoré se lépe udržují/mení, snadneji se Meria kvalita

Dekompozice popodľa [SOLID](1_kvalita_kodu.md#solid)

- **single responsibility** - každý modul/trída/funkcia by se mely soustredit iba na jednu část funkcionality (a tu zapouzdrovat)
- **open/closed** - každý modul/trída/(funkcia) by mely byť rozširitelné tj. pridání zmen spôsobí minimálné modifikaci kódu, vetšinou rozširujeme pomocí nových tríd/metod
- **liskov substitution** - každý (dedične) nadrazený objekt by mel byť nahraditelný podrazeným objektem, aniž by bol narušen puvodné kontrakt. Napr. nemôžeme vyhodit výjimku, keď to nadrazený nikdy nedelal. Nemôžeme brát u rovnaké metody konkrétnejší argument, než jaký bere nadrazený objekt (je v pohode brát abstraktnejší). Nemôžeme vracet abstraktnejší typ, než jaký vrací nadrazený. Je v pohode pridávat funkcionalitu ve forme dalších metod.
- **interface segregation** - rozbíjíme velká rozhrania na menší, logicky související jednotky. Jen to, co klient opravdu muže potrebovat.
- **dependency inversion** - závisíme na abstrakcích (rozhrania), ne na konkrétních implementacích

**Problém s cyklickou vazbou objektu** - napr. v metode toString() je ponapríklad vhodne rešit, abychom se necyklili. Proto muže byť vhodnejší definovat si pre takéto prípady speciální objekty s jasnou hierarchií a bez cyklu

**Interface Definition Language** - popisuje rozhrania formou, ktorá je nezávislá na použitém programovacím jazyce (napr. OpenAPI Specification pre REST, protocol buffer pre gRPC, Web Services Description Language pre SOAP, CORBA IDL). zvyčajne je možné pomocí IDL schématu vygenerovat v daném programovacím jazyce kód/struktury, ktorý poskytovatel implementuje a používateľ používá. Viac v [otázke 7](6_distribuovane_systemy.md).

**Event list** - seznam všech udalostí, ktoré mohou v systémov nastat

### Ecosystem map

Znázorňuje celý kontext (včetne částí, se kterými prímo nekomunikujeme), ve kterém náš systém funguje.

![](img/20230607124544.png)

### Analytické vzory

Návrhové vzory nabízí riešenie na často rešené problémy v návrzích systémov. Tato riešenie sú místy až príliš sofistikovaná, takže se doporučuje složitejší Návrhové vzory používat s rozvahou, abychom problém *neoverengineeringovali*.

##### Accountability vzory

*Prijdou mi ve slajdech popsány složitejší, než sú, proto popisuju koncepty/zapamatovatelné aspekty, zbytek si človek dokáže odvodit.*

##### Party

Spoločný název (abstrakce) pre osobu či firmu, zvyčajne má kontaktní údaje (adresu, telefon, email...)

![](img/20230602212700.png)

##### Organization Hierarchies

Řešíme problém reprezentace organizace skládající se z často menících se hierarchií organizačních jednotek (napr. Korporace, Region, Pobočka, Oddelení... typy jednotek mohou byť tiež predmetem zmen). Řešením je stavební blok `Organizace`, ktorá má 0..1 rodiče `Organizace` a 0..n potomku `Organizace` (rekurzivní väzba). Jednotlivé typy oddelení pak mohou dedit od `Organizace`.

![](img/20230602212810.png)

##### Organization Structure

To samé co organization hierarchies, ale pridáváme k tomu `TimePeriod` (pre verzovanie v čase), `Typ Organizační Struktury`, ktorý muže mať `Pravidla` zajišťující, že napríklad oddelení nebude nadrízené divizi.

![](img/20230602221810.png)

#### Accountability

Organization Structure, ale Organizaci nahradíme Party (a vztahu ríkáme accountability). Je tam opet `TimePeriod`, ale `Typ Organizační Struktury` se jmenuje `Accountability Type`. `Pravidla` pre väzby zahazujeme.

![](img/20230602223147.png)

##### Accountability Knowledge Level

Accountability, ale `Pravidla` pre väzby medzi jednotlivými `Party`s zase pridáme. `Pravidla` sú definovaná pre jednotlivé `Accountability Type`s, každé definuje povolenou kombinaci `Party Type` potomka a rodiče v hierarchii. Úrovni, kde popisujeme pravidla (a kde tým pádem sú i `Accountability Type`s a `Party Type`s) ríkáme knowledge level, existuje jen pre zabezpečenie správné kompozice (ale nemá moc význam pre day-to-day operace).

Príklad pre aplikaci accountability je ve [slajdech (str 35+)](https://is.muni.cz/auth/el/fi/podzim2021/PA103/um/02-03-Analysis-patterns.pdf#page=35).

![](img/20230602224136.png)

##### Observations & measurements

##### Quantity

Kvantita má hodnotu a jednotku (v Rustu bychom použili Newtype pattern konkrétné jednotky a pomocí traitu implementovali funkcionalitu).

![](img/20230603105247.png)

##### Conversion Ratio

Prevedení jedné jednotky na jinou, samo o sobe funguje jen pre lineární vztahy.

![](img/20230603105928.png)

##### Compound Units

Jednotka muže byť buď `Atomic Unit` (napr. kilometry), alebo `Compound Unit`, ktorá má aspoň jeden `Unit Reference` obsahující mocninu (napr. kilometry za hodinu).

![](img/20230603110857.png)

##### Measurement

Reprezentuje výsledek meranie. Každé meranie bolo nekým vykonáno (`Person`), zkoumalo nejaký merený fenomén (`Phenomenon Type`) a zjistilo nejakou hodnotu, včetne jednotek (`Quantity`).

![](img/20230603111248.png)

#### Observation

Výše popsaný `Measurement` je typ `Observation`, stejne jako `Category Observation` umožňující zaznamenávat nekvantitativní meranie s nejakou kategorickou hodnotou (napr. typ krevní skupiny), kde nás zaujíma konkrétné `Phenomenon` (napr. A+), ktorý je součástí `Phenomenon Type`.

Je možné pridat i spôsob meranie `Protocol`, či sledovať prítomnost/neprítomnost kategorického jevu, ktorý muže mať závislosťi na (pod)jevech modelovaných pomocí `Observation Concept` (napr. diabetik typu 2 je obecne diabetik).

![](img/20230603112121.png)

**Včetne spôsobu meranie a logických vazeb medzi (pod)jevy:**

![](img/20230603112705.png)

[Go to the next question](./dev_3_zpracovani_dat.md)
