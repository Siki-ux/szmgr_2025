# Distribuované systémy

> Základné pojmy, principy. Rozdíl medzi centralizovanou a distribuovanou architektúrou systémov, nevýhody obojího a ich prekonávanie. replikácia, zdieľanie dát. Architektúra orientovaná na služby (SOA), webové služby. Príklady existujících technologií a ich využití. Príklady z praxe pre všetko vyššie uvedené. ([PA053](https://is.muni.cz/auth/el/fi/jaro2023/PA053/um/))

1. [Základné pojmy, principy (1/6)](#základné-pojmy-principy-16)
2. [Rozdíl medzi centralizovanou a distribuovanou architektúrou systémov, nevýhody obojího a ich prekonávanie (2/6)](#rozdíl-mezi-centralizovanou-a-distribuovanou-architektúrou-systémov-nevýhody-obojího-a-ich-prekonávanie-26)
3. [replikácia, zdieľanie dát (3/6)](#replikácia-zdieľanie-dát-36)
4. [Architektúra orientovaná na služby (SOA), webové služby (4/6)](#Architektúra-orientovaná-na-služby-soa-webové-služby-46)
5. [Príklady existujících technologií a ich využití (5/6)](#príklady-existujících-technologií-a-ich-využití-56)
6. [Príklady z praxe pre všetko vyššie uvedené (6/6)](#príklady-z-praxe-pro-vše-výše-uvedené-66)

## Základné pojmy, principy (1/6)

**Distribuovaný systém** se skládá z komponentu (počítaču) propojených komunikačné sietí. Distribuované systémy reší problémy (výpočty/spracovávanie requestu) spoluprací jednotlivých komponentu (každý delá neco). Vďaka tomu se systém snadneji škáluje (posilujeme subsystém, ktorý má problémy).

### Typy architektur

architektúry popsány v [otázke 1](dev_1_programovani_a_softwarovy_vyvoj.md#vícevrstvá-Architektúra-moderních-informačních-systémov-Architektúra-model-view-controller-36), takže jen shrnutí:

#### Monolitická Architektúra
- obsahuje vše, co systém potrebuje, je možné iba vertikální škálovanie, Zlá Spoľahlivosť (pád znamená pád celého systémov)

#### Úrovňová (tiered) Architektúra
- nezameňovat s layered
- jednotlivé úrovne možno distribuovat, paralelizovat, nahradit (komunikácia skrz API)
- Klient muže byť tenký/tlustý podľa poskytnuté funkcionality.
- pr. Client → Server → Database

#### Hexagonal/Microkernel/component-based
- základné aplikace poskytuje minimálné funkcionalitu, zbytek se dodává skrz plug-in komponenty komunikující pres preddefinované api
- komponenty je možné prípadne zapojovat za behu systémov
- další možnost využití komponentu - ak potrebujeme používat legacy systém, ktorý si nemôžeme dovolit prepsat, je možné ho zabalit jako komponent a pristupovat k nemu pres naše kompatibilní rozhrania
- vývoj komponentových systémov je náročnejší (zvlášť problematické je správne určiť rozhrania), ale umožňuje vetší prispôsobiteľnosť/opätovná použiteľnosť komponentu v budúcích projektech
- napr. extensions ve VSCode, component-based architekturu používá Jakarta Enterprise Edition, kde jednotlivé Java Beans sú komponenty

#### Pipeline architecture
- sekvenční Spracovanie, každý komponent se stará o relativne transformaci vstupu na výstup (delej malou vec, ale delej ji dobre)

#### Service-oriented architecture
- popsáno v [samostatné kapitole](#Architektúra-orientovaná-na-služby-soa-webové-služby-46)

#### Microservice architecture
- vysoká koheze, nízká provázanost služeb, systém je tvoren velkým množstvím malých služeb
- duležitá je rychlá komunikácia medzi službami (gRPC)
- služby nesdílí DB

### Komunikačné paradigmata

#### Remote Procedure Call (RPC)
Umožňuje spuštení predem vystavené procedury medzi procesy (i na vzdáleném stroji) tak, jako bychom proceduru volali prímo v kódu. Implementácia procedury muže byť v odlišném programovacím jazyce. Součástí je definícia rozhrania, ze kterého je možné vygenerovat odpovídající volatelné funkcia/struktury použité pre argumenty pre náš jazyk.

- De-facto standardem je dnes **gRPC**
- Pre fullstack typescript aplikace je dnes populární používat **tRPC**
- V PA053 se probírala **CORBA** (primárné focus na Javu, ale podporovala i jiné jazyky, nejde jen o RPC, ale o architekturu pre komunikaci medzi objekty v distribuovaném prostredia), ale ta se v nových systémech prakticky nepoužívá kvuli složitosti/lepším alternativám, nahrazena jednodušším SOAP a REST, alebo RPC riešeními (gRPC, funguje na HTTP/2, zprávy binárne serializuje pomocí protocol bufferu).

#### Doručovací garance zpráv (Delivery Guarantees)
Pri komunikaci pres RPC alebo Message Brokers narážíme na limity nespoľahlivosti siete. Rozlišujeme tri úrovne garancí:
* **At-most-once (Nejvýše jednou):** Zpráva je odeslána, ale odesílatel nečeká na potvrdenie. Ak se paket ztratí, zpráva je ztracena. (Nízká režie, vhodné pre telemetrii, senzory).
* **At-least-once (Alespoň jednou):** Odesílatel posílá zprávu opakovane (Retry), dokud nedostane potvrdenie (ACK). Ak ACK neprijde (napr. kvuli výpadku siete pri návratu), zpráva muže byť doručena a zpracována **duplicitne**.
* **Exactly-once (Práve jednou):** Nejtežší na implementaci. Zpráva je doručena presne jednou bez duplicit. Vyžaduje kombinaci *At-least-once* doručenie a **idempotence** na strane príjemce.

#### Idempotence (Kľúč k odolnosti)
Operace je **idempotentní**, ak jej opakované prevedenie se stejnými parametry vede ke stejnému stavu systémov jako jej první spuštení (napr. `setBalance(100)` je idempotentní, `deductBalance(10)` nie je). V distribuovaných systémech se neidempotentní operace ošetrují pomocí **Idempotency Tokens** (unikátne ID požiadaviek generované klientem, ktoré si server ukládá, a duplicitní tokeny podruhé neprocesuje, iba vrátí puvodné výsledek).

#### Message Queues a Event Brokers
Pre komunikaci se v distribuovaných systémech krome RPC používají **message queues** a **event brokers**, kterí umožňují komunikaci typu publisher-subscriber, alebo Spracovanie jedním z množiny príjemcu, a sú schopny zprávy persistentne uchovávat (hodí se pre transakční Spracovanie, Spoľahlivosť v prípade výpadku).

##### Message Queue (MQ)
Klasická FIFO fronta – každá zpráva má jednoho príjemce. Po prečtení je zpráva odstranena z fronty. Konzument neví, kdo zprávu poslal a odesílatel neví, kdo ji prijme. Ak je fronta plná, dochází k odmaťání/mazání starých zpráv (popodľa konfigurace). [RabbitMQ](https://www.youtube.com/watch?v=NQ3fZtyXji0), Amazon SQS,

##### Event Queue
Primárné nástroj pre event-driven architekturu. Publish-subscribe. Append-only log (zprávy se nemažou ihned po prečtení). Nove pripojená služba muže číst kompletní historii zpráv a rekonstruovat stav systémov. Zprávy sú časove serazené. Použití: Event sourcing, stream processing, audity. [Apache Kafka](https://www.youtube.com/watch?v=uvb00oaa3k8), AWS Kinesis,

##### Message Bus (Event Broker / Pub-Sub Bus)
Rozesílá zprávu viac príjemcum. Publish-subscribe (1:N). Každá zpráva je doručena všem odberatelum daného tématu. Pracuje s topics, na ktoré se jednotlivé služby „prihlašují“ (subscribe). Odesílatel nereší, kolik príjemcu zprávu dostane. Použití: Reakce viac subsystému na stejnou událost, napr. notifikace, cache invalidace. Kafka, Redis Pub/Sub, MQTT brokers

#### Alternativní komunikačné spôsoby
Alternativne se muže pre komunikaci v distribuovaném systémov používat napr. REST, alebo (ak chceme low level kontrolu a výkon) prímá komunikácia medzi sockety.

### Cloudové a distribuované výpočetné paradigmata

#### Cloud Computing
**Cloud** - výhodou je, že môžeme používat platformu/infrastrukturu jako službu, aniž bychom se o ni museli starat/provádet nákladnou iniciální investici. Výpočetné výkon možno (i automaticky) upravit/škálovat na základe aktuálního vytížení. Fyzické zdroje mohou byť sdílené, čímž je možné dosáhnout nižší ceny a je možné distribuovat výpočetné požadavky (peaky rôznych aplikací v rôznych dobách zvládne i jeden stroj). Datová centra možno volit na základe blízkosti k našim zákazníkum.

#### GRID Computing
**GRID computing** - výpočet velmi náročných úloh pomocí velkého množství zdrojov (napr. dobrovolnický Folding@home). Zdroj muže byť CPU, storage, speciální zariadení, ...

#### Batch vs Stream Processing

![](img/20230602104120.png)

U batch processingu môžeme distribuovat pomocí jednotlivých jobs, reší se plánovanie jobs (muže stačit obyčejná fronta)

Stream napr. Apache Kafka

#### MapReduce
**MapReduce** - k transformaci dát používáme operace MAP (transformace dát 1:1) a REDUCE (sumarizace dát N:1). MAPery možno triviálne paralelizovat (rovnaké i rozdílné operace), u REDUCEru je to trochu složitejší, paralelizujeme rozdílné operace. Napr. Apache Hadoop

## Rozdíl medzi centralizovanou a distribuovanou architektúrou systémov, nevýhody obojího a ich prekonávanie (2/6)

Hlavním rozdílem je, že centralizovaná Architektúra shromažďuje dáta a logiku na jednom míste, distribuovaná Architektúra rozptyluje logiku do viac samostatných komponentu (bežících napríklad i na samostatných strojích), ktoré spolu komunikují.

### Nevýhody centralizované architektúry a ich riešenie

**Nevýhody centralizované architektúry:**
- neumožňuje horizontální škálovanie => **riešenie:** škálujeme vertikálne
- zlyhania časti znamená zlyhania celku => **riešenie:** redundance, záložní servery
- nízká flexibilita, vysoká provázanost => **riešenie:** duraz na kvalitu kódu

### Nevýhody distribuované architektúry a ich riešenie

**Nevýhody distribuované architektúry:**
- komplexita celkového systémov, náročnejší správa
- vyžadují viac/složitejší komunikaci, složitejší synchronizace, náchylnost na latenci => **riešenie:** použití message queues, gRPC, eventual consistency

### ACID vs BASE paradigma

Oproti centralizované architektúre Distribuované systémy:

- nebývají požadavky/transakcie ACID, ale **BASE**:
  - **BAsically available** - nefunkčnost časti nespôsobí nefunkčnost celku, zbytek funguje i v prípade nefunkčné časti systémov. napr. na netflixu nemusí fungovat služba hľadanie, ale vše ostatné beží v cajku. Na každý dotaz dostaneme nejakou odpoveď.
  - **Soft state** - zmeny v systémov mohou nastávat i keď neprichází žádné dotazy - systém takto propaguje dáta, aby dosáhl konzistencia
  - **Eventually consistent** - dáta nemusí byť konzistentní okamžite po získanie odpovedi na dotaz, ale až po nejaké chvíli

#### CAP Teorém (Zásadní teoretický pilír)
*Státnicová otázka: „Mužeme mať v distribuovaném systémov siete garantovanou okamžitou konzistenci i 100% dostupnost zároveň?“*

CAP teorém hovorí, že v distribuovaném dátovom úložišti je možné v jeden moment zajistit iba **dve ze trí** následujících vlastností:
* **C (Consistency - Konzistencia):** Každé čítanie vrátí nejnovejší zápis alebo chybu. Všechny uzly vidí rovnaká dáta ve rovnaký čas.
* **A (Availability - Dostupnost):** Každý nezhavarovaný uzel vrátí vždy odpoveď (ne chybu), ale nemusí obsahovat nejnovejší zápis.
* **P (Partition Tolerance - Odolnost proti rozdelení siete):** Systém pokračuje v činnosti i v prípade, že dojde k výpadku komunikácia (rozdelení) medzi uzly.



*Dusledek pre praxi:* Pretože fyzickou sieť (a teda riziko jejího rozdelení - **P**) nemožno v reálném svete 100% garantovat, reálne si vždy vybíráme medzi **CP** (obetujeme dostupnost pre konzistenci - napr. MongoDB, etcd, Redis) a **AP** (obetujeme okamžitou konzistenci pre dostupnost -> eventual consistency, napr. Apache Cassandra, DynamoDB).

#### Klamy distribuovaného počítání (Fallacies of Distributed Computing)
Pri návrhu distribuovaných systémov vývojári často delají 8 chybných predpokladu (definoval L. Peter Deutsch), ktoré vedou k zlyhania architektúry:
1. Sieť je spolehlivá. 2. Latence je nulová. 3. Šírka pásma je nekonečná. 4. Sieť je bezpečná. 5. Topologie se nemení. 6. Je zde jeden administrátor. 7. Transportné náklady sú nulové. 8. Sieť je homogénne.
*(U zkoušky stačí uvést první 3–4 jako argument, proč musíme rešit timeouty, retries a asynchronní komunikaci).*

### Výhody distribuované architektúry

- zlyhania (pád) časti systémov neznamená pád celku
- sú flexibilnejší na modifikace vďaka nízké provázanosti

## replikácia, zdieľanie dát (3/6)

V distribuovaných systémech se používá replikácia dát z rôznych dôvodu. U distribuovaných databáz (Apache Cassandra) /filesystému (Apache Hadoop) to muže byť z dôvodu bezpečnosťi/dostupnosti/prevence výpadku, obecne se tým ale v systémech snažíme zajistit rychlejší odezvy.

### Problém centrálné Databázy

Centrálné Databázy, ve ktoré se sdílí dáta, se muže stát limitujícím bodem -> použijeme buď distribuovanou databázi, ktorá replikaci reší interne, alebo viac databáz, ktoré mohou byť jednoduchší (MongoDB), pretože se distribucí dát vzdáváme ACID a fungujeme s BASE. Určitá replikácia dát vzniká kešováním (Redis). U replikácia je ponapríklad neakým spôsobem rešit invalidaci dát po zmene (timeout, alebo CQRS).

### Content Delivery Networks (CDN)

replikácia je kýžená u content delivery network (CDN), kde se snažíme mať statické zdroje (web, obrázky) co nejblíže používateľmi, aby se dosáhlo rychlého načítání.

### NoSQL Databázy a distribuční strategie

NoSQL Databázy majú zvyčajne mechanismy pre automatickou replikaci/distribuci dát medzi rôznymi uzly:

#### Sharding
Je možné použít **sharding** (rozbijeme dáta, uzel se stará o svou doménu) pre distribuci dát

#### Master-Slave replikácia
**Master-slave replikácia** pre škálovanie (u aplikací s častým čtením) a prevenci výpadku (spadne master? jeden ze slaves je nový master) - master se pri zápisu stará o aktualizaci dát na slaves. Zapisujeme jen na mastera a ten pak zpropaguje na slaves, kteri sú jinak read only a sú pak napríklad bliz uzivatelum.

#### Problém Split-Brain a mechanizmy konsenzu
*Státnicový chyták (Rossi, Pitner): „Pri Master-Slave replikaci se sieť rozdelí na dve poloviny. Slaves v odríznuté polovine si myslí, že Master umrel, a zvolí si nového Mastera. Co se stane a ako tomu zabránit?“*

Ak v clusteru vzniknou dva zapíratelní Masteri (každý v jedné odríznuté časti siete), dojde k fenoménu **Split-Brain** (delený mozek). Obe poloviny začnou nezávisle prijímat zápisy, což nenávratne zkorumpuje konzistenci dát.



**Riešenie:**
1.  **Quorum (Kvorum):** K jakékoli zásadní zmene (napr. zvolení nového Mastera alebo potvrdenie zápisu) je ponapríklad souhlas **nadpoloviční vetšiny** všech uzlu ($Vetšina = \lfloor N/2 \rfloor + 1$). Odríznutá menšina uzlu nikdy nedosáhne kvora, takže se zablokuje pre zápis a split-brain nevznikne. (Proto se distribuované koordinátory staví v lichém počtu uzlu – 3, 5, 7...).
2.  **Konsenzuální algoritmy (Raft, Paxos):** Protokoly, ktoré formálne zajišťují, že se uzly v distribuovaném prostredia bezpečne shodnou na jedné hodnote / jednom lídrovi (Leader Election).
    * **Raft:** Modernejší, srozumitelnejší. Uzly sú ve stavech *Leader*, *Follower*, alebo *Candidate*. Používá ho napr. `etcd` v Kubernetes.
    * **ZAB (ZooKeeper Atomic Broadcast):** Speciální protokol, ktorý interne využívá Apache ZooKeeper pre replikaci stavu.

### Systémy pre zdieľanie dát

Pre zdieľanie dát (udalostí) je možné použít **Apache Kafka**, platformu pre streamovanie dát ukládaných do logu. Pre zdieľanie informací o službách distribuovaného systémov se dá použít **Apache ZooKeeper**.

## Architektúra orientovaná na služby (SOA), webové služby (4/6)

### Architektúra orientovaná na služby (SOA)

Architektonický styl, ktorý rozdeluje systém na volne provázané, vzájemne nezávislé a samostatne nasaditeľné služby, z nichž každá implementuje ucelenou obchodní funkci. Služby komunikují pomocí standardních rozhrania (SOAP, REST, zpráv pres middleware/ESB apod.) a možno je vyvíjet, nasazovat a škálovat nezávisle.

#### Charakteristiky SOA:
- duraz na opätovná použiteľnosť služeb napríč celou organizací
- používá ESB (Enterprise Service Bus) pre komunikaci medzi službami
- standardy jako SOAP, WSDL, UDDI pre definici a objevovanie služeb
- služby sú zvyčajne hrubozrnné (coarse-grained)
- centralizovaná governance a správa služeb
- težší infrastruktura, komplexnejší implementácia
- fajn pre velké enterprise organizace s potrebou zdieľanie služeb
  ![img.png](img/SOA_archi.png)

#### Zásadní rozdíl: SOA vs. Microservices (Smart Endpoints vs. Smart Pipes)
Ačkoli sú mikroslužby evolucí SOA, liší se v kritickém bode zdieľanie logiky a integrace:
* **SOA (Smart Pipes, Dumb Endpoints):** Komunikácia je centralizovaná kolem **ESB (Enterprise Service Bus)**. ESB nie je jen hloupý drát; obsahuje težkou byznys logiku, transformace formátu (napr. XML na JSON), routovanie a orchestraci. Samotné služby sú tak "hloupejší", ale systém závisí na obrím monolitu uprostred (ESB), ktorý se stává single point of failure a bottleneckem.
* **Microservices (Smart Endpoints, Dumb Pipes):** Logika se kompletne presouvá na konce (do samotných mikroslužeb). Komunikačné kanálmi sú maximálne jednoduché a "hloupé" (REST, gRPC, lehká message queue bez logiky). Služby si samy reší transformace dát a stav. Tým se dosahuje skutečného decoupling (rozpojení) služeb.



#### Koordinace služeb: Orchestrace vs. Choreografie
* **Orchestrace (Orchestration):** Centrálné prvek (napr. orchestrátor v ESB alebo dedikovaná služba) rídí tok byznys procesu. Říká službám: "Ty udelej krok A, ty krok B". Vhodné pre komplexné business procesy (Saga pattern rízený orchestrátorem).
* **Choreografie (Choreography):** Decentralizovaný prístup založený na událostech (Event-driven). Služby reagují autonomne na události v Message Busu. Služba A publikuje událost `OrderCreated`, služba B ji zachytí, zpracuje platbu a publikuje `PaymentConfirmed`. Neexistuje centrálné bod, systém je flexibilnejší, ale hure se v nem vizualizuje celkový stav procesu.

### Webové služby

komponenty umožňující komunikaci a interakci prostrednictvím standardizovaných protokolu a formátu. Jsou založeny na Service Oriented Architecture. Web services poskytují abstrakci funkcionalite služby skrz webové API. Skrz definiční jazyk je formálne popsáno schéma/rozhrania dané služby a je možné generovanie klientského kódu pre rôzne programovací jazyky s cieľom usnadnit použití webové služby. Schéma muže byť zároveň generováno prímo ze zdrojového kódu prostrednictvím anotací.

#### Historické technologie (SOAP/XML)

Dríve se používaly web services založené na:
- **SOAP** (simple object access protocol)
- **XML**
- definované pomocí **Web Services Description Language (WSDL)**

*SOAP Request:*
```xml
<?xml version='1.0' ?>
<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <soapenv:Body>
        <ns1:echo
            soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
            xmlns:ns1="http://localhost:8484/services/EchoService">
            <in0 xsi:type="xsd:string">Hello World</in0>
        </ns1:echo>
    </soapenv:Body>
</soapenv:Envelope>
```

##### WSDL (Web Services Description Language)
- **W3C specification** pre popis webových služeb
- **Programmatically generated** from source code annotations
- **Programming language independent** way to specify service interfaces
- **Podobné CORBA IDL**

#### Moderní technologie

Aktuálne se pre tyto účely spíše používá:

##### REST + JSON
- **REST** (representational state transfer, nie je to protokol, ale architektonický styl pre definici rozhrania)
- **JSON** (byť je možné použít i jiné formáty)
- definované pomocí **OpenAPI Specification**

##### GraphQL
- **GraphQL** (a JSON) se svým **GraphQL Schema** a dotazovacím jazykem
- GraphQL používa jeden entrypoint (+1 playground) a umožňuje presne specifikovat kýžená dáta (až na úroveň polí) a rešit tak problém s:
  - **overfetching** (1 dotaz obsahuje zbytečná dáta)
  - **underfetching** (v dotazu nemáme dostatek dát, takže deláme viac rôznych dotazu)

#### Porovnání SOAP vs REST

*SOAP je nezávislý na transportu, REST využívá HTTP. REST je jednoduchší, rychlejší a efektivnejší. SOAP umožňuje jednu zprávu cílit viac príjemcum, prechod zprávy pres prostredníky, kterí mohou zpracovávat hlavičku (telo je určeno jen príjemci). SOAP umožňuje výmenu strukturovaných a typovaných XML dát, SOAP hlavička (nepovinná) muže obsahovat metadáta, QoS, bezpečnosťné informace, SAML dáta, session identifikátor (a.k.a. cookie)..., SOAP obálka je root XML prvek zprávy, obsahuje namespace (určující verzi protokolu), styl kódovanie dát, SOAP telo obsahuje samotný obsah zprávy. REST umožňuje provázanost (vďaka hyperlinkum) a je možné se pomocí nej dostat na úplne jinou stránku mimo náš systém.*

*REST se dívá na web jako na zdroje adresovatelné URL, ktoré vrací reprezentaci dát (HTML, XML, PNG, JSON...). Príjem dát uvede klienta do stavu, ktorý muže byť transformován prístupem na jiný zdroj. Je bezstavový, každá zpráva obsahuje vše, čo je nutné pre jej interpretaci (správne by zpráva nemela obsahovat cookie, ale napríklad JWT), dotazy sú kešovatelné.*

## Príklady existujících technologií a ich využití (5/6)

### Komunikačné technologie

#### RPC frameworky
- **gRPC** - Google's high-performance RPC framework, používá HTTP/2 a Protocol Buffers
- **tRPC** - TypeScript-first RPC framework pre fullstack aplikace

#### Message Brokers
- **Apache Kafka** - distribuovaná streamovací platforma, high-throughput pub/sub messaging
- **RabbitMQ** - message broker s podporou rôznych messaging patterns
- **Redis Pub/Sub** - jednoduchý publish/subscribe messaging

### Databázové technologie

#### Distribuované NoSQL Databázy
- **MongoDB** - document-oriented Databázy s automatickým shardingem
- **Amazon DynamoDB** - fully managed NoSQL Databázy
- **Apache HBase** - column-oriented Databázy postavená na Hadoop

#### In-memory Databázy a cache
- **Redis** - in-memory dáta structure store, používaný jako cache, message broker

### Big Data a Stream Processing

#### Batch Processing
- **Apache Hadoop** - framework pre distribuované ukladanie a Spracovanie big dáta
- **Apache Spark** - unified analytics engine pre large-scale dáta processing

#### Stream Processing
- **Apache Kafka Streams** - stream processing library
- **Apache Storm** - real-time computation system

## Príklady z praxe pre všetko vyššie uvedené (6/6)

#### Netflix
- **Architektúra:** Microservices (600+ služeb)
- **Databázy:** Cassandra pre user dáta, MySQL pre billing
- **Komunikácia:** REST APIs, event-driven architecture
- **CDN:** Vlastné CDN pre video streaming
- **Resilience:** Circuit breakers, bulkheads, timeouts

#### Spotify
- **Event-driven:** Kafka pre user activity tracking
- **Recommendation engine:** Apache Spark pre ML workloads
- **Content delivery:** Multi-CDN strategy
- **Service mesh:** Envoy proxy medzi services

### Event Sourcing a CQRS

#### Event Store
```json
{
  "eventId": "uuid",
  "eventType": "UserRegistered",
  "aggregateId": "user-123",
  "data": {
    "email": "user@example.com",
    "timestamp": "2023-01-01T00:00:00Z"
  }
}
```
### Middleware v praxi

**Middleware** - vrstva softwaru poskytující rozhrania pre interakci s rôznymi službami/systémy, abstrakce k často používané funkcionalite, prípadne vrstva propojující existující systémy.

Príklady middleware:
- **CORBA, Web Services, REST** - komunikačné middleware
- **Message queue systémy, event brokeri** - messaging middleware
- **Apache Camel** - integration framework
- **Spring Boot** - application framework s middleware capabilities

[Go to the next question](./dev_1_programovani_a_softwarovy_vyvoj.md)
