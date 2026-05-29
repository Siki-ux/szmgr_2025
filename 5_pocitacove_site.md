# Počítačové siete

> Koncepty, principy, architektúry. ISO/OSI a TCP/IP model, IP protokol, transportné protokoly (TCP, UDP). Protokoly na sieťových vrstvách, funkcia IPv4, pokročilé funkcia IPv6. Peer-to-peer (P2P) siete, ad-hoc/senzorové siete, vysokorychlostné siete, Počítačové siete a multimédia. Príklady z praxe pre všetko vyššie uvedené. ([PA159](https://is.muni.cz/auth/el/fi/podzim2022/PA159/um/), PA191)

1. [Koncepty, principy, architektúry (1/5)](#koncepty-principy-architektúry-15)
2. [ISO/OSI a TCP/IP model, IP protokol, transportné protokoly (2/5)](#isoosi-a-tcpip-model-ip-protokol-transportné-protokoly-25)
3. [Protokoly na sieťových vrstvách, funkcia IPv4, pokročilé funkcia IPv6 (3/5)](#protokoly-na-sieťových-vrstvách-funkcia-ipv4-pokročilé-funkcia-ipv6-35)
4. [Peer-to-peer siete, ad-hoc/senzorové siete, vysokorychlostné siete, Počítačové siete a multimédia (4/5)](#peer-to-peer-siete-ad-hocsenzorové-siete-vysokorychlostné-siete-počítačové-siete-a-multimédia-45)
5. [Príklady z praxe pre všetko vyššie uvedené (5/5)](#príklady-z-praxe-pro-vše-výše-uvedené-55)

## Koncepty, principy, architektúry (1/5)

> Počítačová sieť je skupina počítaču a zariadení, prepojená komunikačnými kanálmi, ktorá umožňuje komunikaci používateľu siete a zdieľanie prostriedkov (informací, súborov, dát, sw, hw).

Ideálna sieť je transparentní (používateľ si ani nevšimne, že komunikuje skrz sieť), s neobmedzenou priepustnosťou, bezstratová, bez latence, zachovávajúca poradie paketov. V realite siete takéto problémy a limitace majú.

### Základné typy sietí

- **Connection-oriented (propojované)** - pre komunikaci se stanoví/vyhradí kapacita, ktorá nie je využívaná nikým jiným (napr. drívejší drátový telefon), snadno se zajišťuje kvalita služeb, v QoS tomu odpovídají integrované služby
- **Connection-less (paketové)** - kapacita využívaná všemi komunikujícími, komunikátori své zprávy delí a balí na pakety, težko se reší kvalita služeb (napr. Internet), v QoS tomu odpovídají diferenciované služby

K stanovení jednotných pravidel a spôsobu komunikácia slouží standardizované **protokoly**.

### architektúry

architektúry [peer-to-peer](#peer-to-peer-p2p-siete) vs klient-server (klienti komunikují iba sa sarverem, service discovery konfigurací klientov, klient iniciuje spojení)

### Smerovanie

Smerovanie probíhá pomocí smerovacích tabulek routeru - na základe adresy (a prípadne typu) paketov se popodľa tabulky určí další smer, hop-by-hop princip. Další destinace se určuje na základe nejdelšího CIDR prefixu adresy. Smerovací tabulky sú zvyčajne aktualizovány distribuovanými algoritmy. Na routerech je možné pakety filtrovat (zatoulané, k zabezpečenie QoS) a prípadne klasifikovat (pri modelech pay-as-you-go). Smerovat je možné nejen pomocí nejkratší cesty, ale i s ohledem na aktuálné stav/vytíženost siete.

## ISO/OSI a TCP/IP model, IP protokol, transportné protokoly (2/5)

### ISO/OSI

7 vrstev, každá zodpovedná za určiťou funkcionalitu, vrstva komunikuje iba se svými sousedy, každá vrstva slouží jako abstrakce:

- **Aplikační** - sieťová aplikace
- **Prezentační** - reprezentace dát
- **Relačná (session)** - riešenie používateľských relací (sessions)
- **Transportné** - komunikácia medzi procesy
- **Sieťová** - logické adresovanie v rámci siete, routing
- **Datová (dátalinková)** - fyzické adresovanie (MAC)
- **Fyzická** - drát, bity, signály...

V praxi se ujal model TCP/IP, ktorý jednotlivé vrstvy ISO/OSI slučuje.

*Státnicový chyták: Zkoušející (napr. Rebok, Čeleda) se často ptají: „Co všechno se musí stát na sieťové úrovni, keď ráno prijdete na FI, otevrete notebook a napíšete do prohlížeče is.muni.cz?“ Musiete umet vysvetlit tento postup Z pohľadu protokolu:*

1.  **Fyzické pripojení:** Notebook se pripojí pres Access Point (L1/L2, napr. 802.11 Wi-Fi).
2.  **Získanie sieťové konfigurace (DHCP):** Notebook (pres UDP broadcast) požádá DHCP server o IP adresu, Masku, IP výchozí brány (Gateway) a IP adresu DNS serverov. *Bez tohoto nemuže komunikovat mimo lokálné sieť.*
3.  **Preklad adresy (DNS):** Aplikace (prohlížeč) zná jen jméno `is.muni.cz`. Pres UDP port 53 pošle dotaz na DNS server: "Jaká IP adresa patrí k tomuto jménu?"
4.  **Hľadanie cesty k bráne (ARP):** Aby notebook mohl odeslat HTTP paket ven, musí ho na lokálné sieti doručit výchozí bráne. Zná jej IP (z DHCP), ale potrebuje MAC adresu. Odešle ARP broadcast: "Kdo má IP adresu Gatewaye? Pošli mi MAC." (L2 vrstva).
5.  **Ustavení TCP spojení a TLS Handshake:** Nyní muže na cílovou IP (IS MUNI) odeslat TCP SYN (port 443 pre HTTPS). Po Three-way handshake probehne vyjednávanie kľúču pres TLS (zabezpečení L4/L7).
6.  **HTTP Request / Response:** Až po tomto všem odešle aplikačné dáta (HTTP GET) a server odpoví (HTTP 200 OK + HTML). Po ceste prekládají routery zdrojovou interné IP adresu na verejnou pomocí NATu.

### TCP/IP

4 vrstvy:

#### Aplikační
- poskytuje služby používateľum (web, mail...)
- používají se aplikačné protokoly (HTTP, SMTP, DNS, FTP...), ktoré sú součástí aplikací, každý protokol definuje syntaxi, sémantiku, typy a pravidla výmeny zpráv
- rozlišujeme:
    - peer-to-peer vs klient-server
    - pull (datový prenos iniciuje klient) vs push (datový prenos iniciuje server) model

#### Transportné - TCP, UDP
- bere **dáta**, transformuje je na **segmenty** (TCP) alebo **dátagramy** (UDP)
- zabezpečenie transportu segmentu do cílové aplikace, komunikácia medzi procesy
- adresovanie pomocí portu (16 bitové číslo 0-65535)
- muže poskytovat end-to-end Spoľahlivosť, spojení (segmenty sú číslovány, záleží na poradie, dodání je potvrzeno)
- muže poskytovat kontrolu spojení, quality of service
- logický komunikačné kanál, iluze Priame komunikácia

#### Sieťová (internet layer)
- IP (internet protocol)
- bere **segmenty**, transformuje je na **pakety** (= dátagramy)
- zajišťuje prenos paketov medzi komunikujícími uzly (i napríč rôznymi LAN), čímž de facto vytvárí WAN
- umožňuje adresovanie každého zariadenie na internetu pomocí IP adresy (IPv4 32 bitu, IPv6 128 bitu)
- zajišťuje smerovanie paketov - závisí na vytíženosti siete a jej topologii
    - topologie celého internetu se težko určuje, dynamicky se mení
    - každý router reší doručenie paketov na své nejbližší sousedy ve snaze doručit paket blíže (domnelému) cíli na základe své **smerovací tabulky**
        - upravována manuálne (vhodné pre malé siete), alebo automaticky pomocí distribuovaných algoritmu:
            - **Distance Vector**
                - *vše co vím reknu svým sousedum*
                - protokol **RIP**
                - sousedící routery si periodicky/pri zmene vymeňují smerovací tabulky ve kterých sú informace o vzdálenostech (hop distance) k rôznym cílum (distance vector), princip [Bellman-Ford](https://www.youtube.com/watch?v=obWXjtg0L64) algoritmu
                - používaný pre malé siete, kde nie je redundance
                - dále se používají IGRP, EIGRP
            - **Link State**
                - *všem reknu informaci o svých sousedech*
                - routery si vymeňují informace o stavu svých sousedu, je uchovávána topologie celkové siete, každý si dopočítá svou routovací tabulku, pre cesty se používá [Dijkstra](https://www.youtube.com/watch?v=_lHSawdgXpI).
                - protokol **OSPF**, open shortest path first
                - metrikou (váhou hrany) je cena odvozená od šírky pásma, nižší je lepší
                - robustnejší, pretože si každý počítá routing tabulky sám
                - používaný pre velké siete
                - dále se používá IS-IS
            - **Path Vector**
                - distance vector, ale vymeňují se nejen ceny cest, ale celé ich popisy
                - protokol **BGP (Border Gateway Protocol)**, umožňuje routing pravidla (policies), používá CIDR na zefektivnení routovanie
                - používá se pre smerovanie medzi autonomními systémy
        - je možné použít interné (RIP, OSPF) pre naši doménu (autonomní systém) a externé routing (EGP, BGP-4) pre smerovanie medzi doménami (autonomními systémy)

#### Vrstva sieťového rozhrania (network access layer)
Často se tato vrstva ješte rozlišuje na:
- **datovou (dátalinkovou)**
    - bere **pakety**, transformuje je na **framey** obsahující mimo jiné adresu odesílatele i príjemce (vďaka tomu se m.j. zariadenie dozví, kdo na médiu komunikuje)
    - poskytuje adresovanie pomocí fyzických/MAC adres
    - zajišťuje Spoľahlivosť fyzické vrstvy (detekcia chýb & prípadná korekce, možné vďaka redundanci, napr. paritní bit, Hamminguv kód)
    - flow control
    - reší koordinaci prístupu viac zariadenie ke sdílenému médiu (delením na kanálmi, na základe rezervací, náhodnosti...) - MAC protokol
    - na této úrovni možno zapojovat siete do topologií (bežné topologie bus, hvezda, kruh)
- **fyzickou**
    - poskytuje rozhrania ve forme **framu bitu**
    - poskytuje prístup k prenosovému médiu
    - interne vrstva transformuje bity na signály prenosového média, zajišťuje synchronizaci, multiplexing (skloubení viac signálu/dátových toku do jednoho pre prenos na sdíleném médiu, časový/frekvenční/vlnodélkový multiplexing), demultiplexing...
    - médiem muže byť drátový/optický kabel, vzduch (pre bezdrátový prenos, rádiové/infračervené signály...)

*Státnicový chyták:* Komisi nestačí odpoveď, že na fyzické vrstve "se prenáší signál". Chtejí slyšet, že **logickou** jednotkou prenosu na této vrstve sú **bity (jedničky a nuly)**, ktoré se následne (napr. pomocí modulace či kódovanie) fyzicky reprezentují jako zmeny napetí, svetelné pulzy (optika) alebo elektromagnetické vlnení.
### IP protokol

- Zajišťuje doručenie IP dátagramu (dáta rozrezaná na kousky s obálkou) v rámci internetu host-to-host (i pres prostredníky, a.k.a. routery), sieť je connection-less, paketová
- Best-effort služba, nie je garance o doručenie.

Viac v sekcích [IPv4](#funkcia-ipv4) a [IPv6](#pokročilé-funkcia-ipv6).

### Transportné protokoly (TCP, UDP)

#### UDP (User Datagram Protocol)

- jednoduchý, poskytuje nespojovanou, best-effort službu (Spoľahlivosť si musí prípadne rešit aplikace)
- kľúčová je jednoduchosť => minimálné režie, rychlost
- používá se pre jednoduchou request-reply komunikaci (DNS), real-time prenosy (livestream), multicast

Hlavička obsahuje:
- Zdrojový port
- Cílový port
- Celkovou délku
- Checksum

#### TCP (Transmission Control Protocol)

- poskytuje spolehlivou spojovanou službu, uchovává poradie
- pracuje s byte streamy
- komunikácia musí byť ustanovena 3way handshake (syn, syn&ack, ack)
- komunikácia je rozpoznatelná jen end-to-end, routery nereší, že jde o spojení
- nepodporuje multicast

Hlavička obsahuje:
- zdrojový port
- cílový port
- sekvenční číslo (v rámci toku)
- ack číslo - číslo dalšího očekávaného bajtu, potvrzuje prijetí dát
- délka hlavičky
- príznaky (ack, reset spojení, konec spojení...)
- velikost okna (pre flow control)
- checksum
- options

TCP mení množství poslaných dát v prubehu komunikácia, aby nebol príjemce (Flow Control), alebo sieť (Congestion Control) zahlcen/a, slouží k tomu **velikost okna**.

- **Flow Control** znamená, že príjemce v rámci ACK zprávy pošle, kolik mu zbývá místa v jeho bufferu (napr. 500 bytu), takže sender ví, že viac poslat nemuže. Keď má príjemce plný buffer, tak pošle, že jeho window size je 0 a odesílatel čeká, dokud neprijde nová ACK zpráva od príjemce o tom, že už má volné místo v bufferu.
- **Congestion Control** funguje tak, že pri startu se exponenciálne zvyšuje velikost okna, dokud nedosáhneme určiťé hranice. Od této hranice lineárne zvyšujeme velikost, dokud nedojde ke ztráte paketov. V ten moment snížíme velikost na hraniční hodnotu a pokračujeme v lineárním zvyšovanie rychlosti. Jednotlivé varianty si tuto metodu prispôsobují, napr. Tahoe po ztráte jde na minimálné velikost okna (jako na úplném začátku), Reno praktikuje popsaný postup.
- Výsledný strop pre velikost odeslaných dát je dán minimálné hodnotou techto dvou parametru.

## Protokoly na sieťových vrstvách, funkcia IPv4, pokročilé funkcia IPv6 (3/5)

### Protokoly na sieťových vrstvách

- **Aplikační**
    - **HTTP** - prenos webových stránek, komunikácia medzi webovým prohlížečem a serverem
    - **SMTP** - odesílání e-mailových zpráv
    - **DNS** - preklad doménových jmen na IP adresy
    - **FTP** - prenos súborov medzi počítači

- **Transportné**
    - **TCP** - spolehlivý, spojovaný prenos dát s kontrolou chýb a potvrzováním
    - **UDP** - rychlý, nespojovaný prenos dát bez garantované doručenie

- **Sieťová IP**
    - **IPv4** - internetový protokol verze 4, adresovanie a smerovanie v sieti
        - **ARP** - mapovanie IP adres na MAC adresy
        - **RARP** - mapovanie MAC adres na IP adresy
        - **ICMP** - chybové zprávy a diagnostika siete (ping, traceroute)
        - **IGMP** - správa multicastových skupin
    - **IPv6** - internetový protokol verze 6, nástupce IPv4 s vetším adresním prostorem
        - **ICMPv6** - ICMP pre IPv6

  **Smerovací protokoly:**
    - Distance vector:
        - **RIP** - jednoduchý smerovací protokol pre malé siete
        - **IGRP** - Cisco proprietární protokol, vylepšení RIP
        - **EIGRP** - pokročilý hybridné smerovací protokol od Cisco
    - Link state:
        - **OSPF** - otevrený standard pre smerovanie ve vetších sietích
        - **IS-IS** - smerovací protokol puvodne pre ISO siete

- **Vrstva sieťového rozhrania**
    - **Ethernet** - standard pre kabelové lokálné siete (LAN)
    - **802.11 (Wi-Fi)** - standard pre bezdrátové lokálné siete (WLAN)

### Funkcia IPv4

Protokol umožňující komunikaci host-to-host.

- 32 bitu, 0.0.0.0 - 255.255.255.255
- typy adres:
    - **unicast** - komunikácia 1 na 1
    - **broadcast** - zpráva všem na LAN
    - **multicast** - zpráva tem, kterí se prihlásili k odberu dát na dané multicast adrese

#### Hlavička obsahuje:

- verzi
- délku hlavičky
- type of service (pre zabezpečenie quality of service)
- celkovou délku dátagramu
- identifikaci, flags, offset (používá se pri fragmentaci, rozdelení dátagramu na viac, ak prenosová technologie nezvládá velikost)
- time to live (dekrementován na každém hopu/routeru, pri hodnote 0 je paket zahozen, slouží k eliminaci zatoulaných paketov)
- protokol - špecifikácia protokolu vyšší úrovne, ICMP, IGMP, TCP, UDP, OSPF...
- checksum hlavičky (ne tela, pretože by prepočítávanie trvalo déle, deje se na každém hopu kvuli zmene TTL)
- adresa odesílatele i príjemce
- options - slouží pre testovanie, debugging, volitelná část vďaka poli "délka hlavičky"

#### IPv4 obecne:

- spolupracuje s protokoly:
    - **ICMP** - poskytuje informace o stavu siete (napr. echo request/reply), poskytuje odesílateli informace o chybe doručenie (napr. príjemce nedosažitelný, TTL šlo na nulu)
    - **IGMP** - správa skupin pre multicast, (od)registrace do skupin
    - **ARP, RARP** - preklad IP na MAC a obrácene
- umožňuje multicast

Puvodne se IP adresy delily iba do tríd:

![](img/20230530162603.png)

kvuli nedostatku se začala používat i maska siete (CIDR)

127.0.0.1 je loopback

#### Maska siete, Gateway a NAT (Častá státnicová otázka)
*Otázka komise: „Co vše potrebuji na PC zadat krome IP adresy, aby se správne načetla sieť? K čemu to slouží?“*
* **Maska podsiete (Subnet mask):** Určuje, ktorá část IP adresy je identifikátor siete (network ID) a ktorá část je identifikátor zariadenie (host ID). Používá se k tomu logický AND s IP adresou. Zásadní účel: Počítač popodľa ní pozná, jestli cílový počítač, se kterým chce komunikovat, leží v *jeho* lokálné sieti (pošle mu dáta prímo pres MAC/switch), alebo jestli je v *cizí* sieti (pošle dáta pres router).
* **Výchozí brána (Default Gateway):** IP adresa routeru v naší lokálné sieti. Je to "dverník ven". Ak počítač zjistí (vďaka masce), že cieľ leží mimo jeho sieť, zabalí paket a pošle ho (pres MAC) na bránu, aby ho doručila dál do Internetu.
* **NAT (Network Address Translation):** Riešenie vyčerpání IPv4 adres. Umožňuje desítkám zariadenie v domácnosti mať lokálné (privátní) IP (napr. `192.168.x.x`), ktoré se ven do Internetu vubec nedostanou. Router obsahuje tabulku a jakýkoli požadavek jdoucí zevnitr "prepíše" tak, jako by ho posílal on sám (ze své jedné verejné IP), pričemž zprávu označí specifickým portem (PAT - Port Address Translation), aby vedel, komu v domácnosti má doručit odpoveď.
### Pokročilé funkcia IPv6

- reší problém nedostatku IPv4 adres 128 bitovou délkou
- `0000:0000:0000:0000:0000:0000:0000:0000` - `FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF`
- možnost zkráceného zápisu:
    - vynecháním prefixových nul:
        - `1050:0000:0000:0000:0005:0600:300c:326b` možno prepsat na `1050:0:0:0:5:600:300c:326b`
    - dále vynecháním nejvýše jedné sekvence nul:
        - `1050::5:600:300c:326b`

#### Oproti IPv4:

- IPSec je povinnou součástí
- delší adresa => možnost viac zariadenie v sieti
- jednoduchší hlavička (chybí checksum (úplne odstranen), options, fragmentation) s možností extension headers
- podpora označovanie toku a ich priorit
- podpora bezpečnosťi, šifrovanie, autentizace, integrity dát
- podpora mobility - každé zariadenie je nekde doma, kde má svého *Home Agenta*. Ak je zariadenie mimo domov, posílá informace o své cizí adrese Home Agentovi, ktorý se stará o prípadné preposílání zpráv, alebo spolupracuje pre ustanovení prímého tunelu
- podpora autokonfigurace zariadení
- má i **anycast** - jako multicast, ale stačí, aby se dáta doručila jen jednomu členu skupiny
- odebrána fragmentace pri doručovanie, toto si musí ohlídat odesílatel. Ak je dátagram moc velký, je zahozen a vygeneruje se ICMP zpráva obsahující zprávu o maximálné velikosti na daném linku (procesu určenie správné velikosti se ríká **Path MTU Discovery** - pošli dátagram, keď se nevejde, fragmentuj na hodnotu podľa ICMP zprávy, opakuj proces. MTU = maximum transmission unit)
- odebrání checksumu (reší se na nižší, alebo vyšší vrstve)
- broadcast nahrazen specifickými multicastovými skupinami (napr. skupina routeru na LAN)

#### Hlavička (40B) obsahuje:

- Verzi protokolu
- prioritu (obsahuje i pole, ktoré muže indikovat, či bola po ceste zaznamenáno zpoždení)
- label toku (pakety jednoho toku musí byť zpracovány stejným spôsobem, volbu smerovanie možno kešovat)
- délka dát
- další hlavička - muže byť rozširující hlavička (auth, options...), alebo napríklad TCP hlavička dát
- hop limit
- adresy

#### ICMPv6 a Neighbour Discovery Protocol

Podpurný ICMPv6 rozširuje funkcionalitu i o to co delal IGMP a ARP.

- puvodné ARP nahrazuje **Neighbour Discovery Protocol**, ktorý reší:
    - autokonfiguraci IPv6 adresy (možnost i bez DHCP serverov) na základe sieťového prefixu (info od routeru), MAC adresy/lokálne unikátního ID
    - detekci kolizí adres IPv6 (odešle zprávu na svou adresu, ak nekdo jiný odpoví, máme duplikát)
    - určenie MAC adres uzlu na stejném linku, sledovanie zmen
    - určenie sousedu, kterí mohou preposílat pakety dál
    - sledovanie dostupnosti sousedu
    - funguje vďaka komunikaci pres multicast skupiny

(Pod)sieť definovaná pomocí CIDR notace (všichni v sieti sdílí rovnaký prefix)

#### Prechod z IPv4 na IPv6

- nutnost úpravy legacy systémov
- složitejší spracovávanie IPv6 adresy
- ideálné je dnes delat aplikaci fungující s obojím, alternativne je ponapríklad použít enkapsulaci (tunelovanie) IPv6 do IPv4 paketov, alebo prekládání (NAT)

## Peer-to-peer siete, ad-hoc/senzorové siete, vysokorychlostné siete, Počítačové siete a multimédia (4/5)

### Peer-to-peer (P2P) siete

Systém je tvoren viac identickými (a na rovnaké úrovni) moduly, peery, ktoré vzájemne komunikují. Každý peer funguje jako klient (posílá požadavky) i server (odpovídá na požadavky) současne. U P2P nie je ponapríklad znát topologii celé siete.

#### Oproti Server-Client:

- lepší Škálovateľnosť (ale u C-S možno pomerne solidne obstát s load balancingem) - s počtem klientov roste i výpočetné kapacita
- decentralizace - fajn Z pohľadu dostupnosti (pád 1 peera neznamená pád celého systémov)
    - muže byť problém Z pohľadu konzistencia dát
- vetší promenlivost topologie
- zdieľanie výpočetné kapacity
- sebeorganizace
- C-S je jednoduchší a zavedenejší na vývoj, snadneji se spravuje
- v C-S je server jasnou autoritou, ktorá zajišťuje Bezpečnosť a autenticitu dát, u P2P je to složitejší zajistit

Napr.:
- distribuované výpočty Folding@Home
- filesharing BitTorrent
- Apache Cassandra (db), Gun.js(db)
- blockchain (verejný - kryptomeny, privátní - napr. Hyperledger)

#### Vrstvy:

- **Aplikace**
- **Middleware**
    - abstrakce nad overlay, poskytuje prístup ke službám/zdrojum peeru, kontroluje prístup ke službám/zdrojum, hľadanie a udržovanie zdrojov (skupin peeru) distribuovaných služeb
- **Base overlay**
    - vrstva nad fyzickou sietí (zvyčajne TCP/UDP), kde se peery berou jako hopy (fyzicky vzdálení mohou byť v p2p sieti sousedi a naopak)
    - peer discovery, preposílání zpráv, udržovanie (časti) siete

#### Peer discovery:

- **Static/Manuální** - peer má predkonfigurovaný seznam informací o ostatních možných peerech (ip, port), na ty se zkouší pripojovat. Nevhodné pre dynamické systémy, u vetších systémov možno omezit seznam na pár dlouhodobe bežících stabilnejších peeru.
- **Centralizovaný registr peeru** - udržuje seznam aktivních peeru, používá se pre discovery, následne probíhá komunikácia naprímo. Registr je de facto server, single point of failure. Registr provádí healthcheck (peer muže znenadání spadnout, takže odhlašovanie pri ukončení peera nestačí)

Service discovery možno pomocí záplavy siete dotazy (nestrukturované siete, každý peer zodpovídá za svá dáta/služby, zpráva má TTL pre prevenci zahlcení, je možné použít DFS/BFS/IDS/heuristiky/náhodné procházky... na základe most promising), alebo je nejaký registr (strukturované siete, registr je centrálné, a/alebo dáta sú v distribuované tabulce, skip listu...), prípadne jako registr slouží vybraní peerové (hybridné siete).

#### Vyhledávanie dát v P2P sietích (Strukturované vs. Nestrukturované)
Rozlišujeme dva extrémy, ako P2P siete hledají informace:
* **Nestrukturované (napr. Gnutella, raný BitTorrent s trackery):** Data sú uložena libovolne u uzlu, ktoré si je stáhly. Hľadanie probíhá buď formou centrálního registru (tzv. Trackeru, ktorý spojuje klienty vlastnící hledaný kus), alebo "zaplavováním" (Flooding) – zeptám se 5 sousedu, ti se zeptají dalších 5 sousedu atd. Neefektivní, spôsobuje enormní sieťový prevádzka. Navíc nie je garantováno, že dáta najdu, i keď v sieti existují.
* **Strukturované (napr. Kademlia / DHT):** Založené na distribuovaných hašovacích tabulkách (**DHT**). Topologie overlay siete je prísne kontrolována. Každý uzel dostane vygenerované ID (napr. 160bit hash). I samotná dáta dostanou generované ID (hash súborov). V sieti platí pravidlo, že uzly ukládají ta dáta, jejichž hash je nejblíže ich vlastnímu hashi. Hľadanie je logaritmicky rychlé ($O(log N)$) a deterministické – ak dáta existují, vždy je najdu, pretože presne vím, akým smerem jehledat.
* **Churn:** Fenomén P2P sietí, ktorý označuje neustálou a rychlou zmenu v tom, ako sa uzly (peers) chaoticky pripojují k sieti a okamžite ji opouštejí (napr. stáhnou film a vypnou klienta). Sieť to musí kompenzovat robustní redundancí a neustálou updatovací režií svých stavových informací.
#### Topologie overlay

Topologie overlay (ako sú medzi sebou peerové vzájemne provázaní) určuje celkovou výkonost p2p siete. Snažíme se vyhnout lineárním formacím, splitum.

- **Random mesh** - po discovery peeru se k niekoľkoa z nich pripojím (vybírám popodľa latence, vďaka tomu je vetší šance výberu fyzicky blízkých peeru).
- **Vrstvy** - peeri se organizují do vrstev podľa poskytovaných služeb/pripojení, na nejvyšší úrovni sú ti nejspolehlivejší s kapacitou preposílání zpráv, na každé vrstve je peer spojen s niekoľkoa peery nižších vrstev a preposílá zprávy na vyšší/nižší vrstvy. Struktura je tree-like, ale je napríklad zajistit, aby výpadok jednoho nespôsobil rozdelení siete. Fajn napríklad pre video streaming - peer muže zprávu jdoucí dolu zduplikovat a šetrit tak bandwidth na vyšších vrstvách.
- **Mrížka/Grid** - peeri sú propojeni do mrížky (muže byť vícedimenzionální, i okrajoví mohou byť vzájemne propojení). Problém muže byť pridávanie/odebírání peeru, rádky/sloupce nemusí mať konzistentní počet členu. Koordináty peeru mohou byť použity k adresovanie poskytovaných služeb

### Ad-hoc/senzorové siete

#### Rádiové siete obecne:

- distribuované riadenie ke sdílenému médiu
- možná nutnost riešenie problému odposlechu
- možná velká chybovost, kolize... => používají se spojované protokoly, ktoré mohou mať rezervační, alebo plánovací mechanismy pre zabezpečenie QoS.
- pre signalizaci prenosu (aby bola zajištena prevence kolizí) je nutné použít separátní kanál, alebo tato signalizace musí probehnout pred samotným prenosem
- absence interference u odesílatele neznamená nutne absenci interference u prijímajúcího

#### Ad-hoc

- Siete fungující bez predešlé existující infrastruktury, využívající sieťových schopnosťí jednotlivcu => distribuované
- Každý účastník funguje zároveň jako host
- Na rozdíl od P2P sietí:
    - je mnohem vetší dynamicita topologie, mobilita účastníku
    - účastníci sú sami zodpovedni za prístup k prenosovému médiu (často je to vzduch -> možná vysoká chybovost, interference) => nutnost specializovaných protokolu

Príklady:
- komunikácia medzi autonomními automobily
- vytvorení komunikačné infrastruktury pri nouzových/záchranných situacích
- za mini-ad-hoc sieť by se daly považovat sledovací tagy, ktoré využívají sieťových schopnosťí mobilních telefonu

Smerovanie muže byť:
- **adresové** - každý účastník musí mať prirazenou unikátne adresu, problém je najít ho v sieti. Výhodou je podpora uni/multi/broadcastu
- **dáta-centrické** - zprávy na sobe nemajú cílovou adresu, ale identifikátor dát. Príjemci v sieti avizují, o jaká dáta majú zájem -> ta sú jim preposílána, nie je nutnost rešit unikátne adresy

Další delení smerovanie:
- **proaktivní** (pravidelná výmena informací o stavu siete, udržuje se info o topologii) vs **reaktivní** (nutnost flooding), záleží na kýžené rychlosti a vytížеnosti siete, energetických nárocích...
- smerovanie hop-by-hop vs znalost celé topologie
- flat vs hierarchické (nadriadenie mohou mať pridané zodpovednosti, používají specializované algoritmy...)

#### Senzorové siete

Koncová zariadenie sú zvyčajne zariadenie obsahující:
- procesor a pameť
- komunikačné modul (rádio)
- baterii (muže byť i s hw pre zber energie, napr. solární panel)
- samotný senzor (svetlo, pohyb...)

Specifikem senzorových sietí je:
- duraz na energickou efektivitu, pretože baterka muže byť malá, prísun energie omezený... (toto mohou mať spoločné s ad-hoc sietemi)
- omezená výpočetné/pameťová kapacita
- omezená šírka pásma
- možná nespolehlivost
- nutnost rešit unikátne adresovanie (zvyčajne to v sobe tato zariadenie nemajú porešené)
- možný duraz na sebeorganizaci, multi-hop v rámci siete
- pre šetrení energie se muže používat dočasné uspávanie zariadenie v prípade neaktivity v sieti

Príklady:
- sledovanie prírodních jevu, chovanie/presunu (ohrožených) zvírat
- detekcia požáru, zemetresení, vln
- automatizace zemedelství, detekcia sucha, škudcu...
- riadenie dopravy
- automatizace riadenie teploty v budovách
- meranie kvality vzduchu
- zabezpečení objektu

### Vysokorychlostné siete

- **Vysoká propustnost** - gigabitové až terabitové rychlosti
- **Nízká latence** - kritické pre real-time aplikace (sub-milisekundové odezvy)
- **Vysoká Spoľahlivosť** - redundance, rychlé obnovení pri výpadcích
- **Škálovateľnosť** - schopnosť rustu s rostoucími nároky
- Opticke siete a Ethernet technologie sú nejčasteji používané pre vysokorychlostné siete (napr. 10+ Gigabit Ethernet)
- speciální varianty protokolu - tem bežným by trvalo mega dlouho, než by se dostali na maximálné možnou rychlost.
  - **tsunami** - TCP pre ustanovení spojení, ale pak se prepne na UDP pre rychlý prenos dát
  - high-speed UDP - optimalizované pre vysokou propustnost, minimalizuje overhead
  - reliable UDP
  - RBUDP - reliable blast UDP

#### Aplikace:

- **High Performance Computing (HPC)** - vedecké výpočty, simulace
- **Datacenter interconnects** - propojení dátacenter pre cloud služby
- **Content Delivery Networks (CDN)** - rychlá distribúcia obsahu
- **Real-time trading** - vysokofrekvenční obchodovanie na finančních trzích
- **4K/8K video streaming** - prenos vysokorozlišovacího obsahu

### Počítačové siete a multimédia

**Multimédia** - dáta složená z rôznych typu médií (text, zvuk, video, obrázky...) integrovaných dohromady. Napr. videokonference (video + zvuk), televize/stream (video + zvuk + (text, titulky)). Nektorá média mohou byť analogová, pre prenos je nutná konverze. Je kýžená komprese pre snížení objemu prenášených dát, ale komprese muže znamenat overhead navíc, což nemusí byť prijatelné u realtime prenosu. Dle aplikace nám muže (ne)vadit chybovost.

#### Typy zpoždení

**Delay** - doba prenosu ze zdroje k cíli (človek si všimne latence > 100-200 ms)

- **Processing delay** - časový overhead u odesílatele/príjemce, záleží na rychlosti/vytíženosti komunikujícího systémov
- **Transmission delay** - doba, jakou trvá nacpat všechny bity do prenosového média (záleží na velikosti)
- **Propagation delay** - doba prenosu pres samotné prenosové médium, záleží na technologii a vzdálenosti
- **Routing/queuing delay** - záleží na vytíženosti siete, rychlosti smerovanie

**Jitter** - rozdílná doba prenosu medzi jednotlivými pakety

#### Optimalizácia pre multimédia

Pre minimalizaci overheadu a zabezpečenie maximálné rychlosti (i za cenu chýb, výpadku...) se pre realtime aplikace používá UDP, príjemce muže používat techniky jako odhadovanie chybejících dát, prípadne odesílatel muže použít techniky pre detekci/korekci chýb pomocí redundance (alebo opetovného zaslání).

Je možné použít interleaving - napr. u videa preskládáme sousedící snímky tak, aby nesousedily. Ak vypadne paket, tak bude ovlivneno sice viac částí, ale každá jen trochu, namísto znatelného výpadku jedné časti. Toto ale zvyšuje latenci.

Pre realtime prenosy se používá multicast, namísto spousty unicastu (sieť nie je zahlcená tolik). Ak multicast sieť nepodporuje, môžeme na ní nasadit reflektor - odesílatel posílá jeden datový tok, reflektor prijímá a replikuje príjemcum, každému unicastem.

Média se mohou prenášet diskretizovane (soubor, zpráva), alebo kontinuálne (stream).

#### Typy médií

**Text** - napr. HTTP, SMTP, FTP, vyžaduje relativne málo bandwidth, delay a nároky na chybovost závisí na aplikaci. Komprese napr. pomocí huffman, alebo shannon-fano kódovanie, na webu se používá gzip (obsahuje huffmana), drobné chyby delají problémy

**Audio** - v základu analog, digitalizace pomocí vzorkovanie (hodnota v čase) signálu a kvantitativní (mapovanie napr. na celá čísla). Požadavky na šírku pásma záleží na požadované kvalite a prípadné komprimaci, jsme ochotni tolerovat drobné chyby

**Grafika** - zvyčajne nesú požadavky na rychlost (ak nie je tragická)

**Video** - zvyčajne náročné na šírku pásma, jinak se specifiky podobá audiu

## Príklady z praxe pre všetko vyššie uvedené (5/5)

*Poznámka: Praktické príklady sú integrovány v jednotlivých sekcích výše. Tato sekce slouží jako prehled praktických aspektu:*

### Praktické aplikace sieťových konceptu
- **HTTP/HTTPS komunikácia** - praktické využití TCP/IP stacku pre webové aplikace
- **DNS resolving** - praktický príklad UDP komunikácia s fallbackem na TCP
- **Email systémy** - kombinace SMTP, IMAP/POP3 protokolu

### Praktické smerovanie a protokoly
- **BGP routing medzi ISP** - praktické použití path vector algoritmu
- **OSPF v enterprise sietích** - link state routing v praxi
- **DHCP a IPv6 autokonfigurace** - praktické pridelovanie IP adres

### Praktické P2P aplikace
- **BitTorrent** - distribuované zdieľanie súborov
- **Blockchain siete** - Bitcoin, Ethereum jako príklady P2P konsensu
- **CDN siete** - hybridné prístup kombinující P2P a client-server

### Praktické bezdrátové siete
- **WiFi mesh siete** - ad-hoc siete v domácnostech a kancelárích
- **IoT senzorové siete** - praktické nasadenie v chytrých budovách
- **Vehicle-to-Vehicle komunikácia** - ad-hoc siete v doprave

### Praktické multimediální aplikace
- **Video streaming** - Netflix, YouTube jako príklady optimalizácia pre multimédia
- **VoIP systémy** - Skype, Teams využívající UDP pre real-time komunikaci
- **Online gaming** - nízká latence a jitter management

### Poznámky k implementaci

**Protokol** je sada syntaktických (ako majú jednotlivé zprávy vypadat) a sémantických (jaký je význam jednotlivých zpráv) pravidel pre komunikaci alebo výmenu dát medzi systémy/zariadeními/komunikačnými partnery

**CIDR** - krome IP adresy uchováváme i masku siete (napr. 147.209.5.0/24 hovorí, že relevantních je jen prvních 24 bitu). Umožňuje subneting a efektivnejší smerovanie - ak máme v tabulce adresy se stejným prefixem a stejnou cestou, môžeme ríct, že naší cestou majú chodit pakety pre celý prefix

**Piggybacking** - Ak chceme odesílateli poslat nejaká dáta a zároveň potvrdit príjem dát, môžeme tyto informace spojit do jednoho paketov

**NAT** - (Network Address Translation) Preklad adres na rozhrania siete. Napr. pre naši sieť máme 1 verejnou IP adresu. Aby se zajistilo správné smerovanie všem v sieti, musí se na rozhrania prekládat verejná adresa na interné adresu.

**SSL, TLS** - Kryptografické protokoly (SSL nahrazen TLS) používané medzi transportné a aplikačné vrstvou, zajišťují autenticitu a šifrovanie dát komunikujících stran. Nejprve se účastníci dohodnou na podporovaných algoritmech, pak probehne výmena kľúču (pre symetrické šifrovanie) založená na asymetrickém šifrovanie (certifikát serverov, muže požadovat i certifikát klienta). Pak probíhá komunikácia pomocí symetrického šifrovanie.

Pre zefektivnení smerovanie je možné použít **Multiprotocol Label Switching** - pre predpokládané/známé toky definujeme cesty, každému toku dáme label a smerujeme jen popodľa labelu (rychlejší, je možné nastavit i viac cest, napríklad jako backup, alebo pre distribuci pre load balancing).

**Flow control** se reší pre príjemce, **congestion control** se reší pre sieť

**Autenticita** - dáta sú od správného odesílatele

**Integrita** - dáta nebola cestou zmenena

**Šifrovanie** - dáta nesú čitelná/srozumitelná tretím stranám

[Go to the next question](./6_distribuovane_systemy.md)
