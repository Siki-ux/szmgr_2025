# Bezpečný kód

> Metody autentizace a riadenie prístupu. Biometrické metody autentizace, ich dopady a problémy. Elektronický podpis a jeho použití. Autentizace stroju a aplikací. Zásady a principy bezpečného kódu. Typické bezpečnosťné chyby na úrovni kódu, soubežnost, spracovanie vstupu. detekcia bezpečnosťních zranitelností, penetračné testovanie. Príklady z praxe pre všetko vyššie uvedené. (PV157, PV286 || PV017 || PV276)

1. [Metody autentizace a riadenie prístupu (1/7)](#metody-autentizace-a-rízení-prístupu-17)
2. [Biometrické metody autentizace, ich dopady a problémy (2/7)](#biometrické-metody-autentizace-ich-dopady-a-problémy-27)
3. [Elektronický podpis a jeho použití (3/7)](#elektronický-podpis-a-jeho-použití-37)
4. [Autentizace stroju a aplikací (4/7)](#autentizace-stroju-a-aplikací-47)
5. [Zásady a principy bezpečného kódu (5/7)](#zásady-a-principy-bezpečného-kódu-57)
6. [Typické bezpečnosťné chyby na úrovni kódu, soubežnost, spracovanie vstupu (6/7)](#typické-bezpečnosťné-chyby-na-úrovni-kódu-soubežnost-spracovanie-vstupu-67)
7. [detekcia bezpečnosťních zranitelností, penetračné testovanie (7/7)](#detekcia-bezpečnosťních-zranitelností-penetračné-testovanie-77)

## Metody autentizace a riadenie prístupu (1/7)

**Kľúčové pojmy**

- **Autentizace/verifikace identity** - verifikace/overenie identity - kombinace identity (napr. jména) a dukazu (napr. hesla)
- **Identifikace** - rozpoznání - rozpoznání entity v dané množine entit, subjekt nepredkládá identitu, ale systém se mu ji snaží priradit z Databázy známých identit, napr. otisk prstu na vstupních dverích
- **Autorizace** - udelení práv k vykonání určiťých akcí (napr. autorizace terminálu k platbe vložením karty a pinu, zároveň se používateľ autentizoval pinem vuči karte)

**Metody autentizace**

- na základe znalosti (pin/heslo)
- na základe vlastnictví fyzického tokenu (kľúč/čipová karta, reší se i cena padelání, zvyčajne velká za kus, ale funguje economies of scale, fungují legislativní postihy)
- na základe biometrie (otisk prstu, ktorý nikdo jiný nemá)
- na základe fyzické/virtuálné lokace (rychlá zmena fyzické lokace muže byť varovný signál, prihlášení z určiťého počítače s certifikátem muže stačit k autentizaci)

Autentizaci môžeme vyžadovat jednostranne (napr. webový server, potrebujeme vedet, že se nejedná o nekoho jiného. Serverov je jedno, komu odpovídá, ak jen vrací verejnou webovou stránku), alebo oboustranne (pre duležité akce potrebuje server ujištení, že akci provádí opravdu používateľ).

Autentizace muže probehnout na základe výzvy, alebo klidne z iniciativy subjektu.

**Zero-knowledge protokoly** - umožňují demonstraci znalosti tajemství, aniž bychom odhalili jakoukoliv informaci vedoucí k získanie tajemství

- vlastnosti
  - **úplnost/completeness** - poctiví vždy dosáhnou úspešného výsledku
  - **korektnost/soundness** - mizivá šance na úspech nepoctivce

### Autentizace tajnými informacemi

**Tajné informace**

- cieľom je autentizace používateľa
- v ideálním prípade autorizovaným používateľum nekomplikují fungovanie, ale co nejviac znesnadňují zneužití útočníky
- reší se
  - ukladanie
  - Bezpečnosť (kvalita/složitost) vs zapamatovatelnost
  - ako bude probíhat kontrola
  - postup v prípade kompromitace (zmena hesla)
- je nutné dodržet
  - informace by mela byť opravdu tajná, nemela by byť odvoditelná (napr. ne rodné jméno matky)
  - informace by mela byť vybrána z velkého prostoru hodnot (napr. vynucení čísel, speciálních symbolu, mixed case...)
  - informaci pri autentizaci nepredáváme v čisté podobe (možno odposlechnout). Máme možnosti:
    - šifrujeme, v ideálním prípade je šifrovaná celá komunikácia
    - posíláme jen hash. Ten možno sice použít pre podvodnou autentizaci, ale nemožno z nej odvodit heslo
    - používáme challenge-response, pomocí kterého se tajné informace nešírí
- muže ísť o pin/heslo/passphrase/identifikaci obrazové informace/spojení bodov v určiťém poradie...

**Hesla**

- možnosti
  - skupinová (viac používateľu sdílí heslo) - mizivá Bezpečnosť
  - unikátne pre osobu, pomocí hesla se zároveň používateľ identifikuje
  - kombinace s používateľským jménem
  - jednorázová - jdou oddeleným kanálem, zvyčajne součástí vícefaktorové autentizace, prokazujeme vlastnictví dalšího tokenu
- ukládají se [hashovaná](4_dátabaze.md#hašovanie) (ak nepotrebujeme získat puvodné heslo), ideálne včetne soli a pepre, alebo šifrovaná (problém je, že teď musíme chránit místo hesla šifrovací kľúč), nikdy ne v plaintextu
  - **salt** - náhodne vygenerovaná dáta, ktorá se ukládají zároveň s hashem a pri hashovanie se pridávají k heslu, efektivne prodlužuje délku hesla a znemožní detekci stejných hesel podľa shody hashu
  - **pepper** - dáta, ktorá se pri hashovanie pridávají ke vstupu, sú však utajená (neukládáme je vepodľa hashe)
- nucená expirace hesla muže mať za následek používanie obecne slabších hesel
- dobrý kompromis medzi bezpečnosťí a zapamatovatelností sú hesla založená na frázích (se zakomponováním speciálních znaku/číslic), alebo lokálním duveryhodným správcem hesel

**Útoky na hesla**

- cílený (snažíme se zjistit heslo konkrétního používateľa) vs plošný (snažíme se zjistit heslo kohokoliv ze skupiny používateľu)
- online (možno omezit počet pokusu) vs offline (kdy jsme se zmocnili súborov s hashi/šifrovanými daty)
- odpozorovanie (vizuálne, phishing, alebo zachycení komunikácia, sniffing)
- slovníkový (máme slovník často používaných hesel)
- hrubou silou
- zneužití mechanismu na obnovu hesla (mnohdy snadnejší, než prolomení hesla)
- analýza zdrojového kódu alebo súborov verzovacího systémov (často tam hesla nechávají vývojári)
- použití iniciálního hesla z manuálu (napr. často u routeru)
- krádež Databázy/Databázy, získanie obsahu pameti/cache
- použití rainbow tables (predpočítané hodnoty a ich hashe), nástroje na prolomení heslem chránených súborov (john the ripper)

**Jednorázová hesla**

- buď náhodne generovaná a zaslaná separátním kanálem (multifactor authentication)
- alebo **(Lamportuv) retezec hashu**
  - na začátku si používateľ lokálne uloží heslo, ktoré 1000× prožene hash funkcií, výsledek dá serverov
  - pri každé autentizaci používateľ pošle predchozí hash (číslo 999, 998...). Server prožene tento predaný hash 1× hash funkcií a porovná s posledním uloženým hashem. Ak výsledek sedí, uloží si predaný hash jako poslední uložený a považuje používateľa za autentizovaného. Útočník nemuže použít odposlechnutý hash, pretože potrebuje predchozí hodnotu (a originál nezná).
- alebo prístroj (autentizační kalkulátor) generující náhodná hesla na základe času, princip generovanie je znám službe, ktorá autentizuje. Je nutná synchronizace hodin/povolení niekoľkoa hesel kolem predpokládaného okamžiku. (to už je spíš autentizace tokenem). Prípadne má autentizační kalkulátor klávesnici a používáme ho pre challenge-response

**PINy**

- zvyčajne velmi krátké → omezujeme počet pokusu

#### Autentizace pomocí symetrické kryptografie

Ako overit, že komunikuji s tým, kdo se mnou sdílí kľúč?

- pošlu náhodné číslo (a napríklad sekvenční číslo/timestamp pre prevenci útoku), ktoré mi má druhý vrátit zašifrované
- možno i oboustranne, druhý komunikující ve své odpovedi zahrne zašifrovaný challenge pre me

Alternativne možno provést výpočetne jednoduchší variantu - nepredáváme si šifrovaná dáta, ale hashe (pre jejichž vytvorení bol zahrnut kľúč), jinak je to principiálne rovnaké.

- ak chceme oboustrannou autentizaci, musí mi druhý poslat challenge i v nehashované podobe, ať ho mužu použít taky

Do zpráv je možné pridat identitu challengera, abychom predešli man in the midpodľa útokum.

`r` je náhodné číslo, `E` znamená encrypted, `h` znamená hashed, `K` je sdílený kľúč

| s šifrováním                | s hashováním                 |
|-----------------------------|-----------------------------|
| ![](img/20230613181843.png) | ![](img/20230613181909.png) |

#### Autentizace pomocí asymetrické kryptografie

Pomocí šifrovanie: Zašifruju zprávu verejným kľúčem. Jestli jsi majitel soukromého kľúče, dešifruj a pošli výsledek zpet.

Alternativne možno pomocí podpisu: Tady máš náhodné číslo, podepiš mi ho (hash a šifrovanie soukromým kľúčem). Server do dát prihodí své náhodné číslo (aby predešel zneužití, kdy útočník chce od serverov získat svá podepsaná dáta), celé to podepíše a vrátí.

Možno samozrejme provádet oboustranne.

Do zpráv je možné pridat identitu challengera, abychom predešli man in the midpodľa útokum.

### Protokoly pre správu kľúču

**Aktualizace kľúče**

- Nový kľúč možno predat zašifrovaný. Možno opatrit časovým razítkem, alebo spojit s náhodným číslem od parťáka, abychom predešli útoku prehráním.
- Tady máš náhodné číslo. Náš nový kľúč je toto číslo zašifrované starým kľúčem (je fajn si poslat kontrolní zprávu s informací šifrovanou novým kľúčem)

**Ustanovení kľúče bez predchozího sdíleného tajemství**

- **Shamiruv protokol**
  - Vyžaduje komutativní šifru, kde platí `E_a( E_b( X ) ) = E_b( E_a( X ) )`
    1. vygeneruju nový kľúč X. Ten zašifruju svým kľúčem a. `E_a(X)` pošlu kamarádovi
    2. kamarád výsledek zašifruje svým kľúčem b a pošle mi `E_b( E_a( X ) )`
    3. odstraním svuj kľúč a, pošlu kamarádovi výsledek `E_b( X )`. Kamarád odstraní kľúč b a zjistí nový kľúč X, kterým môžeme šifrovat
- **Diffie Hellman protokol**
  - spolu s kamarádem se dohodneme na společném základu (malé prvočíslo `g` a velké číslo `n`) a každý pridáme svou tajnou ingredienci, já `a`, kamarád `b`, `1 <= a, b <= n` (`x_a = g^a mod n` a `x_b = g^b mod n`)
  - výsledek si vymeníme
  - pridáme opet svou tajnou ingredienci a využijeme ekvivalence a kongruence modulo n (`(g^a mod n)^b mod n = g^ab mod n = (g^b mod n)^a mod n`)
  - výsledek `g^ab mod n` používáme pre šifrovanie

### Riadenie prístupu

Bezpečnosťné mechanismus pre umožnenie používateľum vykonávat v systémov nejaké akce.

Pojmy

- vlastník dát - zodpovedný za určiťá dáta
- správce dát - zodpovedný za Bezpečnosť určiťých dát
- používateľ - muže vykonávat operace s dátami podľa svých prístupových práv

Politiky riadenie prístupu

- voliteľný prístup/decentralizovaná správa riadenie - vlastník dát/objektu rozhoduje (malá režie, o správu se starají vlastníci/správci, zlej vynucovanie/koordinace celosystémových pravidel, možnost problému, kdy nekdo v súborovém systémov tajný soubor zkopíruje a zverejní ho omylem všem)
- povinný prístup/centralizovaná správa riadenie - o prístupu rozhoduje systémová politika
- povinný a voliteľný prístup možno kombinovat, systém je pak flexibilnejší, ale stále zaručuje Bezpečnosť u kritických objektu

Základné typy práv (zvyčajne specifikovatelná pre každou jednotku dát, napr. soubory, alebo napríklad buňky v tabulkách)

- read (muže i kopírovat a zrádný člen skupiny tak udelat verejnou kopii)
- write (modifikace)
- execute (spouštení programu)
- pokročilejší príznaky mohou byť napríklad append only soubor

Práva mohou byť specifikována v matici (jedna osa soubory, druhá používateľé, uprostred práva), ale muže byť neprehledná → práva možno ukládat v metadatech daného objektu - **Access Control List (ACL)** (ale težko se zas hledá, k čemu všemu má daný používateľ prístup).

Prístup k objektu

- muže byť omezený časem, místem, intervalem hodnot, typem služby...
- na základe identity používateľa, jeho role/skupiny, alebo napríklad jen hesla

V unixových systémech bývá zvyčajne nejaký superadmin/root, ktorý má prístup ke všemu. Dobrou politikou je snaha o obmedzenie práv tohoto používateľa a vytvorení skupin pre príslušné skupiny dát/objektu - ak se hacker dostane k rootu, je vše v pytli. Moderní unixové systémy (zvyčajne komerční verze) nabízí jemnejší granularitu nad skupinami, právy používateľu...

Good practices riadenie prístupu

- separace oprávnení - potvrdenie duležité operace viac aktéry
- obmedzenie práv jednotlivce - každý má prístup jen k tomu, co nutne potrebuje = _princip nejnižších privilegií_
- defaultní akce je zamaťnutí - práva pridelujeme explicitním povolením, abychom nepovolili nečo jen proto, že jsme zapomneli vzít v potaz určiťý scénár, defaultne zamaťneme vše a používáme whitelisty (napr. firewall)

**Multi-level systems (MLS)**

- do systémov majú prístup všichni používateľé, dáta jim zobrazujeme/umožňujeme používat objekty podľa ich úrovne (nižším úrovním skrýváme to, co mohou videt vyšší úrovne)
- role sú hierarchické
- problémem muže byť **skrytý kanál**
  - mechanismus, ktorý nie je určen ke komunikaci je využit pre získanie informací
  - napr. zátež procesoru, zaplnení disku, čas posledního prístupu k súborov
  - napr. nemožnost vytvorit soubor (indikuje, že soubor se stejným jménem už existuje, jen je nám skrytý)/vložit hodnotu do Databázy ⇒ máme automatizované schéma pre pojmenovávanie

**Role-based access control (RBAC)**

- používateľum prirazujeme role (i viac)
- na role navazujeme oprávnení
- napr. role v databázch

## Biometrické metody autentizace, ich dopady a problémy (2/7)

> Automatizované metody identifikace alebo overenie identity na základe meritelných fyziologických alebo behaviorálních (založených na chovanie) vlastností človeka

Biometrická dáta je nejdríve napríklad nasnímat (včetne kontroly kvality, extrakcia charakteristik) a uložit, potom je možné je používat k autentizaci/identifikaci (pomocí srovnání charakteristik).

Na rozdíl od ostatních metod autentizace **musíme rešit variabilitu** uložených dát a nasnímaného vzorku, dáta nesú nikdy úplne identická.

- velmi často závisí na merících podmínkách, na samotném zariadení, stavu mereného, schopnosťi/motivaci mereného provést si meranie správne...
- 100% shoda muže znamenat problém - útočník se dostal k uloženým dátamm
- reší se balance medzi **false acceptance** (bezpečnosťné problém) a **false rejection** (nepohodlí používateľu)

Biometriky sú vhodné jako doplňkové metody, pre prístup k tajnému kľúči, autentizaci používateľa (ne dát/počítače)... ne pre použití jako samotný kľúč

**Problémy biometrické autentizace**

- nikdy nesú úplne bezchybné
- Failure to enroll - nie je možné získat biometrickou charakteristiku pri registraci (napr. nekdo nemá prst, ktorý chceme snímat)
- Failure to acquire/capture - nie je možné získat charakteristiku pri autentizaci
- False positive identification - prijali jsme chybne (bezpečnosťné riziko)
- False negative identification - zamaťli jsme chybne (naštvanejší používateľé)
- fenotypické charakteristiky (napr. geometrie ruky) se mohou v čase menit
- genotypické charakteristiky (napr. DNA) je zase obtiažné rychle vyhodnotit
- meranie nie je dokonalé (prostredia, jiný merák, nezkušenost/nespolupráce mereného)
- meranie muže byť nepríjemné
- metody majú rôzne charakteristiky rychlosti, spolehlivosti, príjemnosti, výpočetné náročnosti, míru vlivu prostredia...
- musíme rešit živost - jde skutočne o človeka, alebo napríklad o umelý prst? je daný človek naživu?
- jedna charakteristika muže byť použita ve viac systémech, zverejnení nesmí ohrozit soukromí
- biometriky nesú tajné
- ochrana soukromí, legislativní obmedzenie
- kvuli nepresnostem/možným zmenám/netajnosti nie je vhodné z biometrik generovat kvalitní kryptografické kľúče

**Kontinuálné autentizace** - subjekt kontinuálne sledujeme a snažíme se detekovat možné odchylky v chovanie, ktoré by naznačovaly, že se jedná o útočníka, napr. dynamika psaní na klávesnici

Forenzní systémy pre biometrickou autentizaci sú presnejší, spolehlivejší, dražší, mohou byť pomalejší, vyžadují odborníky.

napr. otisk prstu (tam sledujeme markanty), geometrie ruky, sken duhovky, sken sítnice, rozpoznání obličeje, rozpoznání hlasu, rozpoznání stylu interakce se zariadením (napr. tempo psaní na klávesnici, dynamika podpisu), DNA

## Elektronický podpis a jeho použití (3/7)

- zajišťuje **autentizaci** (že zpráva pochází od daného autora) a **integritu** (že zprávu nikdo nepozmenil) **podepisovaných dát**
- musí byť overitelný tretí stranou
- nezajišťuje duvernost dát
- mel by obsahovat i dátamm/čas
- algoritmy **RSA, DSA**

Nektoré algoritmy umožňují obnovu dát na základe podpisu (v podpisu sú neakým spôsobem dáta obsažena).

**Prubeh podepisovanie**

1. vytvorím asymetrické kľúče (verejný, soukromý), verejný kľúč zaregistruju/vystavím, aby mohl byť pozdeji použit k overenie
2. (pre každý podepisovaný dokument) - vytvorím hash (napr. pomocí SHA-2) podepisovaného dokumentu, ktorý šifruju soukromým kľúčem (asymetrické algoritmy bývají pomalé, takže nešifruju celý dokument)
3. podepsané dokumenty je možné overit pomocí mého vystaveného verejného kľúče

**Certifikát**

- spojuje verejný kľúč a informace o subjektu, ktorý verejný kľúč poskytuje ⇒ potvrdenie identity
- společne s informacemi o certifikačné autorite je podepsán pomocí soukromého kľúče **certifikačné autority**
  - vytvárí se retezec duvery - ak veríš autorite, mužeš verit i mne
- certifikačné autorita
  - zajišťuje, že daný subjekt opravdu vlastné soukromý kľúč
  - autentizuje subjekt vystavující verejný kľúč (zajišťuje, že daný subjekt je tým, za čo sa vydává)
  - potvrzuje platnost verejného kľúče daného subjektu svým podpisem
- bývá časove omezen

**Použití podpisu**

- autentizace dát (podpis zprávy, ktorý si mohou ostatné overit)
- autentizace počítaču/tokenu vďaka mechanismu **výzva-odpoveď (challenge-response)**
  - jestli jsi opravdu vlastníkem soukromého kľúče, tak podepiš tato vzorová dáta
- autentizace osob pomocí schopnosťi spustit aplikaci na počítači/tokenu
- digitální podpis neprovádí človek, ale počítač
- ak potrebujeme šifrovat, nejprve podepisujeme, potom šifrujeme

**Soukromý kľúč je ponapríklad chránit**, v prípade vyzrazení se za nás muže nekdo vydávat.

- soukromý kľúč bývá ideálne šifrovaný/blokovaný (napr. vyžaduje zadání prístupového hesla/pinu)

**Verejný kľúč musí mať zajištenou integritu** - ak bychom používali nesprávný verejný kľúč, mohli bychom dojít k nesprávným výsledkum ⇒ vystavuje se certifikát, ktorý spojuje kľúč s naší identitou pomocí podpisu certifikačné autoritou

**Infrastruktura pre správu verejných kľúču (PKI)**

- **Certifikačné autorita** - poskytuje certifikačné služby, vydává certifikáty a prípadne je zneplatňuje
- **Registrační autorita** - registruje žadatele o vydání certifikátu, proveruje ich identitu (muže byť zároveň CA)
- **Adresárová služba** - uchovává a distribuuje platné kľúče (a seznam zneplatnených certifikátu)
- certifikačné autoritu zvyčajne certifikuje nadrazená certifikačné autorita, čímž se tvorí retezec duvery

**Vystavení certifikátu**

- generovanie kľúčových dát (napr. key-pair pre asymetrickou kryptografii)
- doložení a overenie identifikačních informací (napr. pre web predáme údaje o identite a instalujeme *Certbot*, alebo nahrajeme určiťý soubor, abychom dokázali, že máme nad serverem kontrolu)
- vydání certifikátu žadateli (včetne zverejnení v adresárové službe)

## Autentizace stroju a aplikací (4/7)

**Autentizace počítaču**

- na základe adresy (IP, MAC fyzická adresa)
  - MAC fyzická adresa - svázáním portu switch prepínače s určiťou MAC adresou, alebo svázání IP adresy s MAC adresou
  - IP - riadenie prístupu k webovým službám na základe IP adresy
  - problém muže byť, že MAC i IP adresy možno zmenit, nesú tajné, je možné uvést cizí IP adresu
- na základe tajné informace (symetrická/asymetrická kryptografie)
  - heslo/tajný symetrický kľúč/soukromý asymetrický kľúč
  - vhodné ukládat zašifrované a pri startu zadat heslo (pak to budeme držet v pameti), alebo použít napr. HashiCorp Vault (secret manager)

**TLS/SSL** - protokol vyšší úrovne

- SSL je predchudce TLS
- autentizuje strany pomocí certifikátu a challenge-response (defaultne povinná pre server, volitelná pre klienta)
- zajišťuje integritu a autenticitu dát (pomocí Message Authentication Code, MAC, k dátamm pridáme tajný kľúč a celé to hashujeme (na rozdíl od podpisu neprovádíme šifrovanie hashe dát tajným kľúčem))
- zajišťuje duvernost
- Nejprve probehne iniciální handshake (autentizace pomocí asymetrické kryptografie). Následne se stanoví symetrický kryptografický kľúč, kterým je šifrována celá komunikácia.
- je medzi TCP a aplikací, TLS nevidí do prenášených dát

**IPSec** - na sieťové vrstve, pridán do IPv4, v IPv6 už je defaultne

- pre každý IP dátagram
  - zajišťuje autentizaci odesilatele (IP hlavičky (vyjma menených dát, napr. TTL) a dáta, pridá tajný kľúč, hash uloží do autentizační hlavičky)
  - zajišťuje integritu dát (nezmenená dáta, ^^^)
  - zajišťuje duvernost dát (symetrický šifrovací kľúč známý obema stranám, dáta sú šifrována)
  - zajišťuje ochranu pred útokem prehráním (MAC v kombinaci sa sakvenčním číslem)
  - AH - Authentication Header - zajišťuje autentizaci a integritu dát, ale nešifruje
  - ESP - Encapsulating Security Payload - zajišťuje privacy
- umožňuje transportné (end to end, nepodporuje NAT), alebo tunelovací režim (celý dátagram beru jako dáta, prilepím tomu novou IP hlavičku)
![img_1.png](img_1.png)
**Secure Shell Host (SSH)**

- slouží k vzdálenému prihlášení k serverov
- oproti telnetu je komunikácia šifrovaná (symetrickou šifrou, kľúč se stanoví po handshake)
- probíhá autentizace serverov i klienta (určiťe jste si nekdy generovali key pair pomocí `ssh-keygen`, tak to bolo ono)
- používá se pre to napríklad RSA, DSA (asymetrická kryptografie)

**Security Assertion Markup Language (SAML)**

- standard pre popis a výmenu autentizačních dát
- založený na XML, používaný pre webové aplikace
- umožňuje oddelení poskytovatele identity a poskytovatele služeb, jinými slovy umožňuje Single Sign-On (SSO)
- SAML token obsahuje
  - subject (kdo je držitel tokenu, napr. user id)
  - auth statement (spôsob a čas provedené autentizace)
  - príslušnost ke skupinám, rolím, povolené operace

## Zásady a principy bezpečného kódu (5/7)

**Defensive programming**

- kód by mel byť psán tak, aby bol systém pripraven pracovat v prostredia, kde mohou nastávat (nechtené) chyby
  - duraz na overovanie vstupních dát
  - spracovanie i tech situací, ktoré *prece nemužou nastat*
  - príprava systémov na jednoduché testovanie (dekompozice, závislosťi na abstrakcích) a diagnostiku chýb (protokolovanie, explicitní spracovanie chýb)
  - protokolovanie udalostí (abychom dokázali detekovat, čo sa v systémov delo)

Pre zabezpečenie bezpečnosťi kódu možno postupovat rôznymi spôsoby, prístupy se nevylučují (víceúrovňová ochrana rozhodne nie je na škodu)

- použití bezpečnejšího jazyka, ktorý nektoré chyby neumožňuje, alebo je aspoň delá težší na prevedenie napr. Rust
  - prípadne použití striktnejšího módu prekladače
- spouštení aplikace v sandbox prostredia, napríklad kontejneru, aby prípadný útočník nezískal kontrolu nad celým strojem
- dukladné testovanie, statická a dynamická analýza, code reviews...
- pre kritické veci (kryptografie) je dobré použít osvedčené knihovny
- závislosťi (knihovny) je dobré pravidelne sledovať ohledne výskytu bezpečnosťních slabin (napr. automatizovane pomocí dependabot)
- použití bezpečných verzí funkcií (u C/C++ napríklad strncpy místo strcpy), nepoužívání funkcií označených *obsolete*
- kontinuálné integrace - automatizované spouštení testu, statické (prípadne i dynamické) analýzy
- je kľúčové dobre znát použitý jazyk a jeho typické slabiny
- ak si môžeme vybrat, je lepší používat whitelisting než blacklisting (deny by default)

počas vývoja kódu je dobré zajistit, aby boli chybové stavy nereprezentovatelné (napríklad pomocí builder patternu a rôznych builder tríd).

## Typické bezpečnosťné chyby na úrovni kódu, soubežnost, spracovanie vstupu (6/7)

Seznamy bežných chýb

- Common Weakness Enumeration (CWE) - obecne časté bezpečnosťné chyby v programovacích jazycích
- OWASP top 10 - nejčastejší bezpečnosťné díry ve webových aplikacích (ale OWASP majú i jiné zajímavé projekty zamerené na Bezpečnosť)

Typické chyby

- **Injection** - vložení vlastních instrukcí do dát, ktorá sú bez dostatečné kontroly vyhodnocována interpretem
  - napr. SQL injection
- absence protokolovanie/monitorovanie
- **Race condition** - simultánní zápisy (alebo zápis a čítanie) do sdílené pameti (ze stejného pameťového místa, ale i napríklad ze dvou rôznych logicky závislých míst) - riešením je sekvenční Spracovanie alebo zamykanie
- **Buffer overflow** - v pameti máme pole a za ním dáta. Ak provedeme zápis do pole a zapisovaná dáta sú delší než pole (a neohlídáme si délku), mohou nám zapisovaná dáta prepsat i dáta za polem. Ovlivňuje hlavne C/C++.
- **Buffer overread** - jako buffer overflow, ale se čtením - jsme schopni číst i dáta za polem
- použití neinicializované pameti (po malloc), alebo uvolneného ukazatele (po free)
- **Stack exhaustion** - vyplýtvání místa na zásobníku, typicky kvuli velké rekurzi
- **Heap exhaustion** - vyplýtvání místa na halde, nie je možné alokovat další pameť (muže byť spôsobeno memory leaky, alebo velkou pameťovou náročností programu)
- **Type overflow** - pretečení hodnoty. Napr. int overflow; spôsobeno `i64::MAX + 1`, výsledek je 0 ⇒ kontrola hodnot, alebo speciální operace (napr. hodí výjimku pri pretečení)
- **Floating point reprezentace** - `0.1 + 0.2 == 0.3000000001` ⇒ použít decimal/bigdecimal, což sú inty s fixed-point desetinnou čárkou
- **Off-by-one error**

**Soubežnost** a.k.a. race condition

- zlej načasovanie operací (alebo ich poradie) spôsobí nečekané stavy systémov
- napr. máme současne bežící programy, každý chce prečíst hodnotu ze sdílené pameti a zvýšit ji o 1.

```
Procesy A a B chtějí inkrementovat sdílený čítač, každý o 1
A čte hodnotu 5
B čte hodnotu 5
A inkrementuje načtenou hodnotu 5+1=6
B inkrementuje načtenou hodnotu 5+1=6
A zapíše 6
B zapíše 6
Oba procesy inkrementovaly čítač, ktorý se reálně zvedl iba o 1
```

- riešením je vyznačení problematické časti jako kritické sekce. Pre kritickou sekci se musí vynutit prístupová pravidla čtenáru a písaru:
  - ak existuje písar, musí byť jediný a nesmí existovat žádní čtenári
  - ak neexistuje písar, muže existovat libovolný počet čtenáru
- striktnejším riešením je uzamčení celé kritické sekce, aby k nim mel prístup vždy jen 1 proces
- ak máme viac kritických sekcí a používáme zámky, je napríklad dávat pozor na uváznutí (deadlock). Ten nastane, keď každý proces z množiny procesu vlastné nejaký zdroj a pre dokončení své práce (a uvolnení vlastneného zdroje) vyžaduje zdroj vlastnený jiným procesem. Všichni tak čekají

Nektoré chyby bývají specifické pre určiťé programovací jazyky (buffer overflow pre C/C++)

*Zero-day exploit* - využití bezpečnosťné chyby, ktorá ješte nie je obecne známá/neexistuje proti ní obrana

Zdrojový kód se muže od výsledné binárky značne lišit (optimalizácia, debug-only sekce kódu). počas vývoja se hodí mať dodatečné informace pre debugging (umožňující napríklad detailné stack trace). V release verzi však tyto informace mohou pomoct útočníkovi.

Pre explicitní riadenie prechodu medzi stavy programu možno použiť **automata-based modelling**.

- Stavy a prechody programu modelujeme jako stavový automat; pomocí dát reprezentujeme stav a na základe nej môžeme explicitne definovat validní prechody (napr. switch/match statement, prípadne transformace objektu (pokročilejší builder pattern)). Minimalizujeme tak místa, ve kterých se mení stav, vďaka čemuž je kód prehlednejší a bezpečnejší.

Pro **ošetrovanie vstupu** je vhodné použít fail-fast prístup. Jakmile zjistíme, že pracujeme s chybnými daty, meli bychom prerušit standardní pruchod funkcií a spracovať chybu. Koncovému používateľmi sdelujeme jen nutné minimum nutné pre identifikaci dôvodu chyby (nadbytečné informace, jako napríklad názvy tríd, by mu mohly odhalit interné strukturu aplikace, což by mohlo byť bezpečnosťné riziko).

- pre jednoduchší overovanie je vhodné omezit počet validních vstupu (napr. jen čísla)
- vstupní dáta mapujeme na interné dáta (napr. používáme enumy)
- maximálné délku vstupu je duležité brát v potaz zvlášť u Spracovanie súborov (navíc je dobré použít bufferované čítanie a zpracovávat soubor po rádcích)
- problém muže delat napríklad UTF-8 retezce, kde jeden znak muže mať ruznou délku
- pre spracovanie vstupu je navíc fajn používat validační knihovny (napr. zod pre js, clap pre rust)
- Pre pruzkum toho, čo všetko v našem systémov závisí na používateľském vstupu, je možné použít **taint analýzu**
- jednotky systémov mohou používat [kontrakty](dev_2_analyza_a_navrh.md#rozhrania-komponent-kontrakty-na-úrovni-rozhrania-ocl-56) (preconditions, postconditions, invariants) jako pojistku v prípade nedostatečného spracovanie vstupu
- Pre kontrolu dostatečného spracovanie vstupu je možné použít **fuzzing** (viz další sekce)
- Pre jednoduché Spracovanie sekvence vstupu (príkazu) je vhodné použít **automata-based modelling**
  - v ideálním prípade se chceme nutnosti udržovat stav medzi príkazy vyhnout, bezstavová komunikácia je méne náchylná na chyby a je možné systém jednoduššeji škálovat
- duležité je samozrejme nikdy neverit používateľským vstupum

## detekcia bezpečnosťních zranitelností, penetračné testovanie (7/7)

Pre detekci (nejen) bezpečnosťních zranitelností je možné použít viac prístupu (nesú exkluzivní)

- statická analýza
- dynamická analýza
- fuzzing
- penetračné testovanie
- security review

Pre detekci buffer overflow možno pomocí prekladače použít tzv. canary - dáta za každým polem. Ak dojde k pretečení pole, bude canary prepsán, což je signál problému. Problém pretrvá, ak útočník zná hodnotu canary. Alternativne (režijne náročnejší) možno kontrolovat délku pole a zapisovaných dát.

Prevencí zmeny návratové adresy funkcia útočníkem (dusledek buffer overflow) je randomizace adres funkcií v kódu.

Prevencí code injection muže byť dáta execution prevention - pameť delíme na datovou a spustitelnou, nie je možné spouštet kód z datové časti. SQL injection (zprávy sú zvyčajne interpretované) se reší pomocí prepared statements, čímž efektivne delíme časti príkazu na datovou a príkazovou.

**Statická analýza**

- analýza kódu programu, aniž by bol program spušten
- možno analyzovat zdrojový kód (jednoduchší, je k tomu viac kontextu), ale i binárku
- možno aplikovat i na nedokončený kód
- možno využít i pre vynucení jednotného stylu kódu
- duležitou (ale špatne automatizovatelnou a škálovatelnou) variantou je code review
- statickou analýzu provádí i samotný prekladač (type checking) - ten si ale nemuže dovolit považovat za chybu neco, co chybou ve skutečnosti nie je
- možno využít automatizované nástroje, kterým stačí zdrojový kód (napr. cargo check, cargo clippy, pre viac jazyku napríklad sonarqube)
- bežne bývá součástí CI - duraz na rychlost
- snadno odhalí i časté chyby jako ponechání hardcoded api kľúče

**Dynamická analýza**

- program je spušten, poskytujeme rôzne vstupy
- je možné použít virtualizovaný procesor/interpret, môžeme sledovať pameť
- možno vynutit omezené prostredia (málo pameti, omezená práva, obmedzenie v súborovém systémov)
- možno sledovať dáta a ich zmeny v programu
- možno vložit logovací instrukce
- napr. Valgrind (nahrazuje standardní alokátor a poskytuje vlastné, což mu umožňuje sledovať dení v pameti), miri (interpret pre rust, používá se pre detekci undefined behavior pri práci s unsafe kódem)
- **Fuzzing** - program spouštíme s *náhodnými* generovanými vstupy a sledujeme výstupy
  - vhodné pre blackbox
  - vstupy mohou byť úplne náhodné, v praxi chceme poskytnout niekoľko vhodných vstupu (jako základ), ktoré fuzzer modifikuje rôznymi spôsoby (úplne náhodne, alebo pomocí nejaké inteligentní strategie)
  - kľúčové je, aby vstupu bolo velké množství, proces je možné snadno automatizovat a opakovat
  - behem fuzzingu sledujeme chovanie aplikace (zamrzla? beží v cajku?)
  - po skončení fuzzingu máme množinu problematických vstupu, jejichž ošetrovanie se môžeme venovat
  - zvyčajne se takto najdou jen pomerne jednoduché chyby, alebo chyby validace (ale záleží na programu)
  - nektoré fuzzery generují vstupy ze zdrojového kódu, cieľom je vysoká code coverage (napr. American Fuzzy Lop)
  - napr. MiniFuzz (input file fuzzer)
- **Taint analýza** - dáta, ktoré neakým spôsobem závisí na neduveryhodném vstupu, sú označena. Ak se označení dostane i ke kritickým částem kódu, vyskočí nám upozornení

**Security review**

- provádí se top-down, bottom up (vhodnejší pri nejasné architektúre, ale náročnejší na prevedenie) či hybridne
- začíná u architektúry a dokumentácia, snaha o detekci návrhových chýb, stanovují se možná rizika a zranitelnosti
- u kódu se sleduje, ako dobre implementuje architekturu (často existují rozdiely), hledají se možné zranitelnosti v high-level logice, pak i v samotném kódu
- hodnotí se dodržiavanie bezpečnosťních standardu
- prakticky se testuje zabezpečení (penetračné testovanie, DDoS útoky, statická analýza)
- sleduje se vliv neduveryhodných dát (taint analýza)
- možno analyzovat prímo kód (rádek po rádku, alebo popodľa poradie volaných funkcií), prípadne si môžeme udelat seznam potenciálních slabin a na ty se zamerit
- analyzuje se kontrola prístupu a správa oprávnení
- hodnotí se bezpečnosťné opatrení, monitoring
- hodnotí se ochrana dát, správa kľúču, šifrovanie
- výsledkem je zpráva popisující súčasný stav a doporučení do budúcna

**Penetračné testovanie**

- obecné penetračné testovanie je náročné, zvyčajne je dobré si vytipovat/doporučit slabá místa, zamerit útoky jen na nektoré časti systémov
- interne - týmem v rámci organizace
  - možno využít znalosti zdrojového kódu
  - vyžaduje udržovanie specializovaného odborného týmu
- externe - jinou, specializovanou společností
  - nabízí pohled z venku, ktorý muže brát v potaz problémy, ktoré sami nevidíme
  - muže byť součástí compliance
  - poskytovat kód externe muže byť problém
  - muže byť fajn použít viac společností, aby se vzájemne vychytala slabá místa
- možno provádet whitebox/blackbox (graybox je, keď dáme k dispozici dokumentaci, ale ne zdrojový kód)
- dobrou praxí je mať systém odmen za hlášení bezpečnosťních chýb (bug bounty)

## Notes

**Brainstorm**

- používanie neaktuálních/nepodporovaných verzí systémov
- odesílání používateľmi zbytečne detailních informací, ktoré mohou byť zneužity
  - napr. verze používaného dobre známého systémov (napríklad nginx), útočník muže cílit na slabosti této konkrétné verze
  - napr. *Cannot insert new record into table Users, unique constraint on column Email has been violated*
- xss

**Základné pojmy**

- [hashovanie](4_dátabaze.md#hašovanie)
- **kľúče** - rozsáhlé retezce bitu, náhodná čísla, prvočísla...
- **šifrovanie** - zajišťuje duvernost (transformace zprávy za účelem skrytí jejího obsahu pred nepovolanými aktéry)
- kódovanie nie je šifrovanie (napr. zakódované heslo v base64 možno snadno prevést do puvodního tvaru bez jakéhokoliv kľúče)
- základném principem kryptografie je **verejný algoritmus** (dobre otestovaný, vytvorený bezpečnosťními experty) a zabezpečenie bezpečnosťi pomocí **tajného kľúče**. Spoléhat na Bezpečnosť algoritmu jen jeho (algoritmu) utajením nie je dobrý nápad.
- **symetrická kryptografie** - komunikující strany sdílí identický kľúč, kterým se šifruje i dešifruje. Je to rychlejší, než asymetrická kryptografie, ale hure se využívají, keď vyžadujeme autentizaci (napr. server by si musel bezpečne uchovávat kľúč u každého klienta, zároveň je ponapríklad se na kľúči nejak dohodnout, což muže byť odposloucháváno)
  - napr. **AES** (advanced encryption standard), **DES** (dáta encryption standard)
- **asymetrická kryptografie** - existují 2 druhy kľúču, verejný (pre šifrovanie/overenie podpisu) a soukromý (pre dešifrovanie/tvorbu podpisu). Ak chtejí 2 strany plne komunikovat (full duplex), pak každá potrebuje znát svuj soukromý kľúč a verejný kľúč druhé strany. Ak nekomu prozradím svuj soukromý kľúč, muže se vydávat za me.
  - napr. **RSA, DSA**
  - pre šifrovanie a podepisovanie používáme rozdílné páry kľúču, abychom nemuseli čelit problémum, kdy zamestnanec odejde z firmy (a stále zná soukromý kľúč)
- **šifrovanie v praxi** - kombinace symetrické a asymetrické kryptografie
  - pre komunikaci probehne ustanovení symetrického kľúče náhodným vygenerováním, kľúč se bezpečne predá pomocí asymetrické kryptografie. Následne probíhá komunikácia šifrovaná symetricky.

**SHA**

- secure hashing algorithm
- SHA-0 a SHA-1 sú zastaralé a nepovažujú se za bezpečné
- rodina hashovacích funkcií SHA-2, zahrnuje SHA-224, SHA-256, SHA-384 a SHA-512 (jména popodľa ich délky v bitech)

**RSA** - asymetrická kryptografie, funguje na principu faktorizace velkých čísel (a modulo) - faktorizace je lehká na výpočet, težká na reverzní výpočet

**Bloková šifra** - symetrická, vstupní dáta sú rozdelena na bloky fixní délky, ktoré sú šifrovány stejným spôsobem. Pre vetší Bezpečnosť se nešifrují všechny bloky stejne, ale muže se použít napr. Cipher Block Chaining (CBC), kdy je medzi bloky vytvorena závislosť (každý další blok je xorován zašifrovaným predchozím blokem). Zmena bitu zašifrovaných dát znemožní dešifrovanie zprávy. Napr. AES, DES

**Proudová šifra** - symetrická, z kľúče vygenerujeme posloupnost a na jejím základe šifrujeme jednotlivé bity dát (⇒ každý jinak). Vďaka tomu nie je nutné dešifrovat všechno (jako u blokových šifer v režimu Cipher Block Chaining), ale môžeme ísť *od prostredka*. Fungují rychle (napríklad pomocí XOR dát s kľúčem). Zmena bitu zašifrované zprávy pozmení puvodné zprávu ⇒ je vhodné pridat nejakou formu hashovanie. [https://www.youtube.com/watch?v=wlSG3pEiQdc&t=1s](https://www.youtube.com/watch?v=wlSG3pEiQdc&t=1s)

**Cyclic Redundancy Check (CRC)**

- kontrolní součet, umožňuje detekci neúmyslných chýb pri prenosu/uložení
- je snadné vytvorit vstup odpovídající součtu, takže neposkytuje ochranu pred úmyslnou zmenou
- napr. xor, modulo

Pre zabezpečenie duvernosti dát bez šifrovanie možno použiť **Chaffing and winnowing** - dáta rozdelíme na bity (možno i vetší časti). Pre každý bit budeme v náhodném poradie posílat dve zprávy, jednu s validním MAC a jednu (obsahující inverzi bitu) s nevalidním MAC.

**Čipové karty**

- součástí je pameť (RAM, ROM, EEPROM), procesor
- dáta se na karte ukládají ve forme súborov, každému možno nastavit prístupová práva (volný prístup/prístup jen s pinem/zakázaný prístup)
- karta je schopná pracovat s kryptografickými algoritmy/protokoly
- možno provádet
  - fyzické útoky (preparace čipu, čítanie pameti, využití zárení/elektromagnetických polí), zvyčajne zanechávají viditelné známky útoku
  - logické útoky, vyžadují detailné znalosti o strukture karty
    - časová analýza - sledujeme odezvu podľa vstupu,
      - jako prevenci se snažíme odstranit závislosť délky Spracovanie na vstupu (napr. vložíme fejkové instrukce)
    - výkonová analýza - odberová, memory operace sú levnejší, než výpočty
    - indukce chýb - pomocí náhlých zmen podmínek (napetí, teplota...) se snažíme zmenit operační podmínky
    - útoky pres api - snažíme se využít možné chyby programátora
      - napr. počítadlo pokusu by melo nejdrív snížit počet pokusu, pak overit pin a v prípade úspechu resetovat počítadlo pokusu... jinak možno po zadání pinu a detekci neúspechu rychle odpojit zdroj

**Honeypotting** - pre útočníka pripravíme izolovaný subsystém, do kterého ho pustíme a sledujeme jeho chovanie, čímž se učíme o jeho spôsobu práce

[Go to the next question](dev_5_uzivatelska_rozhrani.md)
