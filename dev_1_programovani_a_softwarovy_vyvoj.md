# Programovanie a softvérový vývoj

> Nástroje a prostredia pre softvérový vývoj rozsiahlych systémov. Základné koncepty softvérových architektur Z pohľadu implementácia. Viacvrstvová Architektúra moderních informačních systémov, Architektúra model-view-controller. Technologie a jazyky vhodné pre frontend a backend vývoj. Persistence, ORM. Príklady z praxe pre všetko vyššie uvedené. (PA165 || PV179, voľba Programovanie, SA200)

1. [Nástroje a prostredia pre softvérový vývoj rozsiahlych systémov (1/6)](#nástroje-a-prostredia-pro-softvérový-vývoj-rozsiahlych-systémov-16)
2. [Základné koncepty softvérových architektur Z pohľadu implementácia (2/6)](#základné-koncepty-softvérových-architektur-z-pohledu-implementácia-26)
3. [Viacvrstvová Architektúra moderních informačních systémov, Architektúra model-view-controller (3/6)](#vícevrstvá-Architektúra-moderních-informačních-systémov-Architektúra-model-view-controller-36)
4. [Technologie a jazyky vhodné pre frontend a backend vývoj (4/6)](#technologie-a-jazyky-vhodné-pro-frontend-a-backend-vývoj-46)
5. [Persistence, ORM (5/6)](#persistence-orm-56)
6. [Príklady z praxe pre všetko vyššie uvedené (6/6)](#príklady-z-praxe-pro-vše-výše-uvedené-66)

## Nástroje a prostredia pre softvérový vývoj rozsiahlych systémov (1/6)

Vývoj sw riešenie se zvyčajne skládá z krokom/krokov: Analýza, Návrh, Implementácia, Testovanie, Nasadenie. Viac v otázke [Softvérové inžinierstvo](2_softwarove_inzenyrstvi.md)

- **Komunikácia a ubiquitous language** - kľúčové je zajistit pravidelnou a dobre definovanou komunikaci medzi stakeholdery (nejen na začátku, ale i v prubehu vývoje), definovat ubiquitous language (univerzální jazyk domény) a vynucovat jeho používanie, aby v rámci úzce spolupracujících skupin nedocházelo k vytvárení vlastních výrazu a následnému neporozumení medzi skupinami.

- **Kontinuálné integrace a nasadenie (CI/CD)** - počas vývoja se často používá kontinuálné integrace a nasadenie (CI/CD), čímž se mohou vynucovat standardy (dobré pre Udržateľnosť kódu) a spouštet se automatizované testy. Bývá součástí verzovanie kódu.

- **Dekompozice a abstrakce** - kľúčovou součástí analýzy a návrhu bývá dekompozice (a abstrakce) na komponenty, pri ktoré delíme komplexné systém na jednoduchší nezávislé časti, abychom nemuseli neustále držet v hlave kontext celého systémov. Cieľom je minimalizovat závislosť medzi komponenty a dodržovat SOLID principy. [Viac v Kvalita kódu](1_kvalita_kodu.md).

- **Kontrakty komponentu** - komponenty systémov majú dobre definovaný kontrakt, nezávisí na konkrétních implementacích, ale na abstrakcích (napr. parametr metody je typu interface, ne konkrétné struktura)

Pre vývoj rozsiahlych systémov se používají následující typy nástrojov:

- **Editory a vývojová prostredia** - v ideálním prípade (ak jazyk podporuje Language Server Protocol) závisí na preferencích vývojáre. Je možné použít od jednoduchých editoru až po plne integrovaná vývojová prostredia (vim/neovim, vscode, jetbrains produkty).
- **Verzovací systémy** - umožňují správu verzí zdrojového kódu a spolupráci vývojáru (git, SVN). zvyčajne beží na platforme, ktorá muže byť hostovaná (github, gitlab), alebo kterou si hostujeme sami na vlastních serverech (gitlab). Platformy zvyčajne nabízí viac, než jen správu zdrojového kódu (CI/CD, issue tracking...)
- **Nástroje pre správu projektu** - slouží pre správu úkolu, sledovanie chýb a komunikaci v týmu (Clickup, Jira, ale i napríklad Github).
- **Nástroje pre testovanie** - umožňují vytváret a spouštet testy, simulovat popopoužívateľské interakce, overovat funkčnost systémov (Jest, cargo test, Insomnia, Postman)
- **Nástroje pre kontinuálné integraci a nasadenie** - automatizují spouštení testu a sestavení výsledného produktu (github workflows, gitlab CI/CD, circle ci, Travis CI, Jenkins).
- **Monitoring a protokolovanie** - slouží pre sledovanie výkonu systémov a analýzu chýb a problému (Grafana)
- **Dokumentační nástroje** - popisující fungovanie systémov a jeho částí. Dokumentaci zdrojového kódu je vhodné z nej generovat, aby se minimalizoval problém neaktuálnosti (cargo doc, OpenAPI (machine-readable JSON/YAML formát, je možné ho generovat z anotací, alebo z nej generovat príklady, dokumentaci), pre jednoduchý formátovaný text Markdown). Dokumentácia je duležitá zvlášť pre vystavovaná API
- **Kontejnerová prostredia** - slouží pre minimalizaci rozdílu medzi prostrediami, usnadňují reprodukovatelnost prostredia, ve kterých aplikace beží (vývojové, testovacie, produkční) (Docker, Podman).
- **Nástroje pre analýzu kódu** - kontrolují dodržiavanie standardu, zajišťují určiťou kvalitu kódu, hledají potenciální chyby/slabá místa (cargo clippy, ESLint, SonarQube).

## Základné koncepty softvérových architektur Z pohľadu implementácia (2/6)

### Specifika implementácia webových informačních systémov

Webové informační systémy se zvyčajne skládají z niekoľkoa částí:

- **popopoužívateľské rozhrania/frontend/klient** je zprístupneno používateľmi skrz prohlížeč. Základnémi stavebními kameny sú HTML, CSS a JavaScript/Web Assembly. Tradične šlo o **multipage aplikace** renderované na serverov (šablonovací systémy jako python\jinja, rust\askama, php má šablonovanie prímo v sobe), po každém požiadaviek probehlo prekreslení. Nedávno bol trend **singlepage** aplikací renderovaných na klientovi (založeny na JS frameworkcích jako React, Vue, Svelte, Solid, alebo WASM (aktuálne defaultne) rust\yew), kde po iniciálním načtení aplikace putovala medzi klientem a serverem jen dáta. Aktuálné trend je používat fullstack/meta frameworky (NextJS, SvelteKit, rust\leptos...), kde prvotní vykreslení je na serverov a následne se web chová jako SPA (ale umožňuje vícero módu fungovanie, napríklad plne static-site generation). Toto platí zvlášť pre menší projekty, pretože fullstack framework umožňuje vývoj frontendu i backendu na jednom míste.

- **Aplikační server/backend** slouží k vykonávanie aplikačné logiky, zpracovává požadavky klienta a odpovídá na ne, zajišťuje autentizaci a autorizaci. Stav systémov propisuje do Databázy, zvyčajne je server bezstavový. Používají se general-purpose programovací jazyky (Rust, JS/TS, Go, C#, Python, Java).

- **Databázy** uchovává stav systémov. Tradične se používá relačná Databázy (Postgres, MySQL, Oracle), ale muže byť vhodnejší použít dokumentovou (MongoDB) či grafovou (Neo4j).

Webové informační systémy majú tato specifika:

- **Snadnost aktualizací klienta** - na rozdíl od desktop aplikací nie je ponapríklad ze strany používateľa nic explicitne stahovat a instalovat
- Nutnost **responzivního a prístupného používateľského rozhrania**, ke kterému používateľé mohou pristupovat i z mobilních zariadení, prohlížeče usnadňují implementaci prístupnosti (vada zraku, prístup iba pomocí klávesnice...)
- Vetšinou **tenký klient** - aplikačné logika se provádí z pravidla na serverov
- Webové systémy bývají (ak nie je rešeno jinak) prístupné z celého internetu, proto je duležité vhodne rešit **autentizaci a autorizaci**, a ich **zabezpečení proti útokum** (napríklad SQL injection, XSS, CSRF, viac níže)
- Mohou byť používané vetším množstvím používateľu, proto je vhodné napríklad rešit škálovanie (vertikální vetším výkonem nemusí stačit, horizontální viac stroji nemusí byť vždy aplikovatelné). Aplikační servery je možné vďaka ich bezstavovosti škálovat horizontálne, Databázy se zvyčajne reší vertikálne, či použitím distribuovaných databáz (Cassandra). Základem zvyšovanie výkonu systémov je kešovanie (Redis).
- zvyčajne se používá model klient-server

### Útoky

- **SQL injection** - do vstupního pole vložíme specifický string, ktorý dokáže spôsobit akci v databázi (napr. vstup `ahoj; DROP TABLE Users; --`)
  - obrana pomocí prepared statements
- **Session hijacking** - útočník se zmocní cookie/tokenu, ktorý se používá pre prokázání identity. Tokeny ukládáme jako cookie (nejbezpečnejší, pre mobilní aplikace je v pohode local storage)
  - obrana pomocí nastavení cookie jako "Secure" (možno poslat jen skrz https) a "HttpOnly" (nemožno číst/upravit pomocí JS)
- **Cross site scripting (XSS)** - útočník vloží na web obsah, ktorý je validní html/js a obeti se zobrazí/spustí pri načtení stránky
  - obrana pomocí sanitizace vstupu
- **Cross site request forgery (CSRF)** - útočník pripraví a pošle klientovi URL odkaz (alebo vytvorí na svém webu formulár) vyvolávající akci na našem serverov
  - obrana pomocí CSRF náhodných tokenu (jednorázove vydaný s požadavkem dávající používateľmi prístup k akci). Token vložíme do formuláre (aby ho používateľ mohl odeslat) a zároveň si ho buď uložíme, alebo ho nastavíme jako cookie. Pri Spracovanie požiadaviek zkontrolujeme, či se tokeny shodují.
  - obrana pomocí cookie atributu "SameSite", ktorý modifikuje, kdy se cookie posílá pri cross-site požadavcích. `Strict` neposílá cookie nikdy pri cross site požadavcích, `Lax` jen pri GET požadavcích - ty by stejne nemely vyvolávat akci, takže by to nemelo vadit. Problém však pretrvává u starých prohlížeču, alebo ak se útočníkovi podarí umístit vlastné formulár na naši doménu či subdoménu.
  - obrana pomocí explicitního potvrdenie (alebo MFA) u duležitých akcí
- **Clickjacking** - útočník na svém webu zobrazí pruhledný iframe nad svou stránkou. Používateľ si myslí, že kliká na tlačítko útočníkova webu, ale ve skutečnosti kliká na web v iframe, čímž muže vyvolat nechtenou akci
  - obrana pomocí `X-Frame-Options` hlavičky
- **Phishing** - útočník vytvorí vizuálne identický web, na kterém chce po používateľích prihlášení
  - obrana pomocí kontroly domény používateľam, nutný trénink používateľu
  - pomoct muže prispôsobení webu - ak je používateľ zvyklý vídat u kritických akcí svou fotku a všimne si, že na útočníkove webu chybí, muže pojmout podezrení

### Auth

Viac v [Bezpečný kód](dev_4_bezpecny_kod.md)

#### Autentizace

- Overenie identity
- **Session based** - používateľ poskytne údaje, server vydá cookie, kterou si udržuje (db/pameť). Používateľ následne s každým požadavkem zasílá cookie, popodľa ktoré server overí a rozpozná používateľa
- **Token based** - používateľ overí svou identitu, server zapouzdrí údaje o používateľmi do tokenu, ktorý podepíše, čímž zajistí, že je možné detekovat modifikaci. Používateľ následne zasílá token, kterým prokazuje svou totožnost, mohou zde byť i informace o právech. Na rozdíl od sessions nemusí vďaka certifikátum servery nic držet v pameti, jde o riešenie vhodné pre použití s viac servery/systémy, alebo keď se uchovávají sessions v databázi a Databázy začíná byť bottleneck. Tokeny se nedají revokovat ze strany serverov => dává se časove omezená platnost
- Ak nám nevadí používat autorizaci poskytnutou tretí stranou, bývá nejbezpečnejší a nejjednodušší riešenie použít federalizovanou identitu. Ak opravdu chceme ukládat používateľská hesla, ukládáme heše (se solí) získané aktuálne doporučovaným Argon2 (muže se zmenit).

#### Autorizace

- Overenie práv k určiťé akci

### Používané technologie

- **HTTP basic** - http header `Authorization: Basic <dáta>`, kde `<dáta>` sú `<jméno>:<heslo>` v base64
  - `-` hlavička je viditelná (=> použij aspoň https), údaje se zasílají s každým požadavkem
- **TLS certifikáty** - server musí poskytnout certifikát, klient muže poskytnout certifikát, čímž se autentizuje
- **OAuth2** - protokol pre poskytnutí autorizace tretím stranám, funguje na principu vydávanie tokenu (Refresh token, Access token). Access token má omezenou dobu platnosti a obsahuje autorizační dáta (majitel tokenu je oprávnen k akci) používateľa podepsaná soukromým kľúčem autorizačního serverov. Refresh token muže mať delší dobu platnosti, je uložený u používateľa a je možné ho použít k získanie dalšího access tokenu bez nutnosti autentizace (provedou se ale kontroly ohledne práv používateľa).
- **OpenID Connect** - nadstavba nad OAuth2, pridává autentizaci a informace o identite používateľa. Používá se pre federalizovanou správu identity (single sign-on). *Klient* je aplikace, ktorá potrebuje autentizovat používateľa. *Autorizační server* autentizuje používateľa, vydává token autorizující držitele k prístupu ke *scopes* obsahující *claims* (napr. scope profil pre claimy id, email, name, picture, locale...) umístených na *resource serverov*. Resource server slouží jako endpoint pre poskytovanie claimu na základe scopes v tokenu (JWT)
- **SAML** - xml protokol pre výmenu autentizačních a autorizačních dát, starší než oauth/oidc
- **Kerberos** - na rozdíl od oauth2 a openid connect používá v základu symetrickou kryptografii (napr. používateľovo heslo je na autorizačním serverov, používateľ posílá iba svou identitu a server vrací prístupová dáta šifrovaná heslem používateľa)

## Viacvrstvová Architektúra moderních informačních systémov, Architektúra model-view-controller (3/6)

architektúry popsány v [otázke 1](dev_1_programovani_a_softwarovy_vyvoj.md#základné-koncepty-softvérových-architektur-z-pohledu-implementácia-26), takže jen shrnutí:

- **MVC pattern - model, view, controller** - oddeluje systém na model, view a controller. Model obsahuje dáta a business logiku. View je zobrazením techto dát a controller slouží k manipulaci nad modelem. Jde o cyklický vztah: `USER (uses)> CONTROLLER (manipulates)> MODEL (updates)> VIEW (shown to)> USER`
  - oddelení logiky zvyšuje modulárnost kódu, ktorý je pak snadnejší upravovat, testovat, udržovat
  - napr. multipage web
- **MVP pattern - model, view, presenter** - presenter je prostredník medzi modelem a view, jde pres nej veškerá komunikácia. Používateľ používá iba view, akce používateľa view predává presenteru, ktorý aktualizuje model a zasílá view nová dáta. Napr. SPA. Vztah Presenter - View je imperativní. Presenter naslouchá událostem vyvolaným View a popodľa toho s ním manipuluje.
- **MVVM pattern - model, view, viewmodel** - používateľ interaguje iba pres view, veškerá komunikácia jde pres viewmodel, ktoré provádí dáta, propisuje je do modelov. Rozdíl oproti mvp je, že viewmodel muže byť použit pre viac views, zmeny se sledují pomocí observeru. Napr. android aplikace. Vztah View - ViewModel je deklarativní. ViewModel neinteraguje s View prímo, ale pozoruje deklarované vlastnosti prostrednictvím speciální vrstvy dátových vazeb.
- **Klient-Server** - klient slouží jako popopoužívateľské rozhrania. Server zpracovává požadavky zasílané klientem a odpovídá na ne. Server podľa požiadaviek klienta provádí aplikačné logiku, pristupuje k databázi... Komunikácia je vždy iniciována klientem, server iba odpovídá. Možno delit na úrovne (2 tier, 3 tier i s databáz, další úrovne mužou byť servisní vrstvy...)

- **Peer-to-Peer** - každý klient je současne i serverem, klienti spolu komunikují naprímo. Klienti takto sdílí výpočetné výkon, distribuují dáta... napr. BitTorrent

- **Vrstvená Architektúra (layered, prípadne clean)** - Delí monolitický systém na vrstvy, každá je zodpovedná za určiťou část aplikace. Vrstva využívá služeb vrstvy pod ní. Každá vrstva muže byť otevrená/uzavrená, otevrené vrstvy je možné preskočit.
  - **Presentation** - closed, UI, klient
  - **Business** - closed, zpracovává business logiku
  - **Service** - open, obsahuje sdílené komponenty business vrstvy (autentizace, protokolovanie)
  - **Persistence** - closed, slouží k prístupu do Databázy, repository pattern
  - **Database** - closed, čiste databázová vrstva

  - jednoduchá na vývoj (porád je to monolit), levná, vhodná pre projekty s velmi omezeným časem/rozpočtem, vhodná ak si nejsme jistí co použít
  - oproti klasickému monolitu je vetší overhead s predáváním dát medzi vrstvami
  - nie je odolná vuči chybám, pád časti = pád celého systémov, relativne dlouhý startup
  - vrstvu je možné nasadit samostatne a zlepšit tak Škálovateľnosť systémov
  - napr. eshop

- **Pipeline Architektúra/Pipes and Filters** - monolitická, skládá se z:
  - **pipe** - point-to-point komunikácia
  - **filter** - komponenty transformující dáta, bezstavové, ale mohou zapisovat do db. Filter se má soustredit čiste na jednu úlohu. Jsou typy:
    - **Producer/source** - zdroj, iniciátor akce
    - **Transformer (map)** - transformuje vstup na výstup
    - **Tester (reduce)** - testuje kritérium a potenciálne vyprodukuje (mimo predání dát bez modifikace dál) výstup, ktorý muže vyvolat akci (zápis do Databázy)
    - **Consumer/sink** - ukončuje akci
    - aktivní filter aktivne tahá dáta (pulling) a predává je dalšímu filtru. pasivní filter jen pasivne čeká na dáta a ako prijdou, zpracuje je, následující aktivní filter si je z nej sám tahá
  - filtry je možné snadno používat znovu (reuse)
  - vede k batch processingu, což nie je fajn pre rychlou odezvu systémov
  - napr. unix terminal, compiler, RxJS, Dart streamy
    ![](img/20230518144835.png)

- **Microkernel/Hexagonal/Component-based architecture** - monolitická, delí systém na jádro (core) a (ideálne) plug-in komponenty, aplikačné logika je v techto komponentech. Jednoduchá rozširitelnost, adaptabilita, customizace
  - Jádro obsahuje minimálné nutnou funkcionalitu, ktorá se rozširuje skrz pluginy
  - Pluginy by mely byť nezávislé, pripojitelné za behu, mohou mať vlastné db, mohou byť vzdálené a komunikovat s jádrem pres napr. REST.
  - Pluginy sú zvyčajne dostupné z nejakého registru, kde sú dáta jako název, kontrakt, detaily pre pripojení pluginu.
  - Duležité je dobre definovat standardizované kontrakty, ktoré musí pluginy splňovat
  - Pre využití komponenty je nutné rešit discovery pomocí nejakého registru (muže stačit hashmapa), musíme znát identitu (ktorá by se nemela menit) chteného komponentu, ktorý v systémov nemusí byť
  - napr. VS Code - jádro je textový editor, pluginy sú extensions

- **Servisne orientovaná Architektúra ([SOA](https://www.youtube.com/watch?v=9fn4vGEKFs8))** - tradiční enterprise prístup
  - duraz na opätovná použiteľnosť služeb napríč celou organizací
  - používá ESB (Enterprise Service Bus) pre komunikaci medzi službami
  - standardy jako SOAP, WSDL, UDDI pre definici a objevovanie služeb
  - služby sú zvyčajne hrubozrnné (coarse-grained)
  - centralizovaná governance a správa služeb
  - težší infrastruktura, komplexnejší implementácia
  - fajn pre velké enterprise organizace s potrebou zdieľanie služeb
![img.png](img/SOA_archi.png)

- **Servisne založená Architektúra ([Service-Based Architecture](https://www.youtube.com/watch?v=LK0tC1-mlFA))** - hybrid medzi monolitem a microservices
  - separátní UI (muže jich byť viac), separátne nasazené služby (zvyčajne 4-12), každá se soustredí na jednu úlohu (alebo část systémov), sdílená db, služby sú interne tvoreny vrstvenou architektúrou/deleny podľa domény
  - Ak služba využívá část Databázy, kterou žádná jiná služba nevyužívá, je možné tuto část oddelit do vlastné Databázy.
  - ak chceme jednotné API, používá se vrstva fasády, ktorá preposílá komunikaci jednotlivým službám
  - ACID transakcie (microservices majú BASE - basically available, soft state, eventually consistent, tj. duplikace dát, konzistencia muže chvíli trvat...), fajn pre konzistenci a integritu, ale úprava znamená nutnost testu celého systémov
  - fajn pre domain driven design bez prílišné složitosti
  - fajn keď potrebujeme ACID
  - modernejší, jednoduchší prístup než tradiční SOA
![img_1.png](img/service_based_archi.png)

- **Microservices**
  - cieľom je vysoká nezávislosť jednotlivých služeb, mohou byť implementovány v rôznych programovacích jazycích
  - každá služba se stará o nutné minimum, služby fungují nezávisle
  - nesdílí se DB
  - duplikace je akceptovatelná, keď se sníží provázanost

## Technologie a jazyky vhodné pre frontend a backend vývoj (4/6)

### Frontend technologie

#### Základné webové technologie
- **HTML** - struktura obsahu webových stránek
- **CSS** - stylovanie a layout webových stránek
- **JavaScript** - interaktivita a dynamické chovanie
- **WebAssembly (WASM)** - vysokooptimalizované aplikace v prohlížeči

#### JavaScript frameworky a knihovny
- **React** - component-based, virtual DOM, unidirectional dáta flow, velký ekosystém
- **Vue.js** - progressive framework, template-based syntax, snadné učení
- **Svelte/SvelteKit** - compile-time optimized, bez virtual DOM, menší bunpodľa size
- **Angular** - full-featured framework, TypeScript-first, velké enterprise aplikace

#### Meta/Fullstack frameworky
- **Next.js** (React-based) - SSR, SSG, API routes, automatic code splitting
- **Nuxt.js** (Vue-based) - universal applications, automatic routing
- **SvelteKit** - SSR, SPA, SSG mode support

#### CSS frameworky a nástroje
- **Tailwind CSS** - utility classes pre rapid prototyping
- **Bootstrap** - responsive grid system, pre-built components
- **Styled Components** - CSS v React komponentech

#### Build nástroje
- **Webpack** - konfigurovatelný bundler, široká podpora
- **Vite** - rychlý development server, založený na ES modules
- **esbuild** - extrémne rychlý Go-based bundler

### Backend technologie

#### Programovací jazyky
- **JavaScript/Node.js** - shared language s frontendem, velký ekosystém (Express.js, Fastify, NestJS)
- **Python** - čitateľnosť kódu, rozsáhlé knihovny (Django, Flask, FastAPI)
- **Java** - enterprise standard, type safety, JVM ekosystém (Spring Boot, Jakarta EE)
- **C#/.NET** - strong typing, performance, Microsoft ekosystém (ASP.NET Core)
- **Go** - performance, jednoduchosť, built-in concurrency (Gin, Echo)
- **Rust** - memory safety, performance, zero-cost abstractions (Actix-web, Axum)
- **PHP** - široké prijetí, hosting support (Laravel, Symfony)

#### Databázové technologie
- **Relačná Databázy** - PostgreSQL, MySQL, SQLite, SQL Server, Oracle
- **NoSQL Databázy** - MongoDB (document), Redis (key-value), Cassandra (wide-column)
- **Graph Databázy** - Neo4j, Amazon Neptune

#### API technologie
- **REST** - HTTP-based, resource-oriented, OpenAPI/Swagger dokumentácia
- **GraphQL** - single endpoint, efficient dáta fetching, flexibilní API
- **gRPC** - high performance, type safety, microservices communication

#### Messaging a queue systémy
- **RabbitMQ** - traditional message broker
- **Apache Kafka** - distributed streaming platform
- **Redis Pub/Sub** - simple messaging

### Cloud a DevOps technologie

#### Kontejnerizace a orchestrace
- **Docker** - containerization platform
- **Kubernetes** - container orchestration
- **Podman** - daemonless container engine

#### Cloud platformy
- **AWS** - nejvetší cloud provider (EC2, S3, RDS, Lambda)
- **Google Cloud Platform** - strong v AI/ML services
- **Microsoft Azure** - integration s Microsoft stack
- **Heroku** - jednoduchá PaaS platforma

#### CI/CD nástroje
- **GitHub Actions** - integrated s GitHub
- **GitLab CI/CD** - integrated s GitLab
- **Jenkins** - open-source automation server

## Persistence, ORM (5/6)

Zabývá se uchováním dát medzi jednotlivými behy aplikace/restarty systémov/požadavky klienta:

- **Relačná Databázy** - nejbežnejší spôsob uchovávanie dát v sw systémech. Data sú strukturována do tabulek obsahujících sloupce, rádek tabulky = datový záznam. Vztahy medzi daty se reší relacemi, odkazy na primárné kľúč jiné tabulky. Pre manipulaci nad daty se využívá SQL (structured query language). (Postgres, MySQL, SQLite). Jsou široce podporovány v programovacích jazycích, je ponapríklad dávat pozor na sql injection (rust/sqlx). Pri použití SQL v aplikacích se doporučuje použít Repository/DAO pattern, prípadne CQRS.

- **Objektove relačná mapovanie (ORM)** - umožňuje mapovanie objektového modelov aplikace na relačná databázi. Výhodou je, že nie je nutné psát Priame SQL dotazy a kód je (mel by byť) agnostický k použité databázi, muže však vzniknout problém s nedostatečnou kontrolou nad dotazem/nutností tvorby specializovaných struktur/tríd. Složitejší dotazy mohou byť ve výsledku podobne komplikované, jako vlastné sql dotaz. Problém muže pusobit i výkon (js\prisma, rust\diesel, java\hibernate)

- **Souborový systém** - dáta je možné ukládat prímo do súborového systémov. Toto je vhodné napríklad pre obrázky/pdf, ale je ponapríklad ošetrit, abychom neposkytli prístup k jiným částem systémov, než k akým chceme.

- **NoSQL** - alternativa k relačním db, umožňují ukladanie a manipulaci s nestrukturovanými daty. Oproti relačním databázm poskytují lepší Škálovateľnosť a flexibilitu, problém muže byť konzistencia (často se používá duplikace pre vyšší rychlost) (mongodb, cassandra)

- **Cachovanie** - dočasné ukladanie často používaných dát/výsledku operací. Možno provádet na úrovni RAM, pred databáz, pred serverem... (redis, nginx)

## Príklady z praxe pre všetko vyššie uvedené (6/6)

### Reálné architektúry

- **Netflix** - microservices Architektúra s 600+ službami, circuit breaker pattern (Hystrix), service discovery (Eureka), API Gateway (Zuul), distributed caching (EVCache)
- **Spotify** - microservices s event-driven architektúrou, Kafka pre user activity tracking, Apache Spark pre ML workloads
- **Uber** - 1000+ mikroservic, Kafka pre location updates, Schemaless (MySQL wrapper) + Cassandra

### Nástroje v praxi

#### CI/CD implementácia
- **GitHub Actions** - YAML konfigurace pre build, test, deploy pipeline
- **GitLab CI/CD** - integrované s GitLab repository

#### Kontejnerizace
- **Docker** - standardní kontejnerizace aplikací
- **Kubernetes** - orchestrace kontejneru v produkci s auto-scaling

#### Monitoring a observability
- **Prometheus + Grafana** - Metriky a dashboardy
- **Jaeger, Zipkin** - distributed tracing napríč mikroservicemi

### Frontend implementácia v praxi

- **React aplikace** - component-based Architektúra s hooks pre state management
- **Next.js** - SSR/SSG s API routes pre fullstack aplikace
- **Tailwind CSS** - utility-first styling pre rychlý vývoj
- **Redux/Zustand** - state management pre complex aplikace

### Backend implementácia v praxi

- **Express.js API** - REST endpoints s middleware pre auth, validation, logging
- **Spring Boot** - enterprise Java aplikace s dependency injection
- **ASP.NET Core** - .NET aplikace s built-in dependency injection

### Databázové implementácia

- **PostgreSQL** - relačná Databázy s JSON support a advanced features
- **MongoDB** - document dátabase pre flexible schema
- **Redis** - in-memory cache a session store
- **Prisma/TypeORM** - type-safe ORM s automatickou migrací

### Security implementácia

- **JWT tokens** - stateless authentication s claims
- **OAuth2/OpenID Connect** - federalized identity management
- **API rate limiting** - ochrana proti abuse
- **HTTPS everywhere** - TLS certifikáty pre všetkochnu komunikaci

### DevOps workflow

- **Git workflow** - feature branches, pull requests, code review
- **Automated testing** - unit, integration, e2e testy v CI pipeline
- **Blue-green deployment** - zero-downtime nasadenie
- **Infrastructure as Code** - Terraform, CloudFormation pre reproducible infrastructure

## Notes

**Validace** - systém delá to, čo sa od nej čeká (v rámci požiadaviek)

**Verifikace** - systém delá veci správne interne

**DAO** - dáta access object, abstrahuje prístup k databázi/persistenčnímu mechanismu

- umožňuje výmenu persistenční technologie, aniž by bolo napríklad zasahovat do jiných vrstev
- usnadňuje testovanie business logiky
- zvyčajne jeden na entitu, CRUD

**DTO a.k.a. Value Object** - dáta transfer object, zapouzdruje dáta pre komunikaci medzi vrstvami

**Inversion of Control** - struktura má pole (napríklad connection pool), ktoré používá pre své fungovanie (závisí na nem). Nemá si pole tvorit sama, naplnit ho z parametru konstruktoru/jiným spôsobem.

**Dependency Injection** - existují frameworky, ktoré asistují s IoC pomocí injekce závislosťí prímo do polí struktur "automaticky" (rust\di, java\spring)

**Aspect Oriented Programming** - technika, kde se definuje aspekt, ktorý je volán pokaždé pri definované akci. Napr. pre protokolovanie - aspekt je definován jednou a je rečeno, že se má provádet pre všetkochny metody. Nie je nutné upravit každou metodu, aby explicitne logovala.

**Software as a service**, **Platform as a service** (staráme se jen o vývoj, vše ostatné zajišťuje služba, napr. Heroku), **Infrastructure as a service** (pronajímáme si infrastrukturu, napr. klasický cloud, AWS, azure, gcp...)

**CORS** - zabraňuje, aby skript z prohlížeče komunikoval sa sarverem odjinud, než z webové aplikace. Napr. ak z klienta SPA myweb.com chci poslat asynchronní dotaz (pomocí fetch API) na other.com, tak ak other.com explicitne nepovolí prístup, prohlížeč muj požadavek neodešle.

**Message queue** - namísto synchronního Spracovanie je možné použít message queue (používá se často interne v distribuovaných systémech, nie je nutné okamžité Spracovanie, usnadňuje load balancing, je možný broadcast, zprávy mohou byť persisted, ...) FIFO, na kazdym konci queue je jeden konzument, RabbitMQ

**Message bus** = dokaze zpravu poslat na vic zarizeni (ne jen jedno jako mq), pub/sub pattern, mam tam topics, ktery odebiram, kafka, redis

**Event queue** - primarne pre event driven systemy, komunikujeme, ze neco probehlo, vetsinou append only log, napr pre big dáta analyzu. Kafka

**Continuous integration** - pravidelne sestavujeme výsledný systém (deláme malé a relativne jednoduché zmeny), automaticky testujeme výsledek

**Continuous delivery** - pravidelne sestavujeme výsledný systém tak, že by mohl byť okamžite vydán, automaticky testujeme výsledek

**Continuous deployment** - pravidelne dodáváme, automaticky testujeme výsledek

**Regresné testy** - provádí se po zmenách, abychom detekovali nechtené efekty

#### REST (Representational State Transfer)

- nejpoužívanejší styl/spôsob tvorby rozhrania webových aplikací (ne protokol), vychází z HTTP, požadavek má syntax `<metoda> <uri>`
- zdroje identifikovány URI, mohou mať ruznou podobu (JSON, XML, HTML, PNG...)
- užívá HTTP metod:
  - **GET** - pre získanie dát
  - **HEAD** - pre získanie metadat - hlavička je totožná s GET, ale v odpovedi nie je prítomno telo
  - **POST** - požadavek, aby cílový zdroj zpracoval dáta obsažená v tele. zvyčajne se používá pre akce/pridání nového prvku do kolekce (login, pridání príspevku...). V prípade tvorby prvku bývá pravidlem vrátit nove vytvorené ID v odpovedi
  - **PUT** - jako post, ale součástí požiadaviek je ID. Prvek s tímto ID má byť upraven novými daty (v tele), alebo vytvoren práve s tímto ID
  - **PATCH** - jako put, ale v tele nemusí byť všechna pole upravovaného prvku - zmenit se majú jen ta pole, ktorá sú prítomná
  - **DELETE** - požadavek k odstránenie dát
  - dále existují **CONNECT**, **OPTIONS** a **TRACE**

*Safe* metody nemení stav na serverov (get, head, options, trace)

*Idempotentní* metody splňují vlastnost, že viac identických požiadaviek má rovnaký efekt, jako jediný požadavek (všechny, krome POST, PATCH (nie je úplne standardizované chovanie) a CONNECT)

RESTové služby sú bezstavové (pre vyhodnocení požiadaviek by nemelo byť nutné znát nic, co nie je v požiadaviek obsaženo, napr. namísto `GET /nextPage` se použije `GET /pages/2`)

Nektoré REST metody sú kešovatelné, v komunikaci mohou byť prostredníci (napríklad cache, proxy, load balancer...), o kterých klient neví

**Best practices**

- konzistentní pojmenovávanie zdrojov
- vztahy rešíme pomocí URI (napr. `GET /users/1/orders` vrací objednávky používateľa 1)
- je v cajku udelat alias (napr. `/me`, `/trends`)
- používanie správných metod, premýšlíme v rámci CRUD operací
- filtrovanie a razení rešíme pomocí query parametru (`/users?active=true&sort=name`)
- verzovanie API
- metody, ktoré vytvárejí/upravují zdroje by mely vracet výslednou podobu zdroje
- aktuálne je preference pracovat s JSON
- používanie správných HTTP návratových hodnot

#### Richardson Maturity Model - úrovne REST API

- **Level 0 (Swamp of POX - Plain Old XML)**
  - jeden endpoint pre celé API (napr. `POST /api/service`)
  - vetšinou jen POST metoda pre všetkochny operace
  - akce určována obsahem payload `{"action": "getUser", "userId": 1}`

- **Level 1 (Resources)**
  - rozdelené zdroje s vlastními URI (`/api/users`, `/api/orders`)
  - stále prevážne POST operace pre všetkochny akce `POST /api/users`with payload `{"action": "getUser", "userId": 1 }`
  - začíná resource-based design, ale nerespektuje HTTP metody

- **Level 2 (HTTP Verbs)**
  - správné využití HTTP metod pre rôzne operace s resources
  - `GET /api/users/1` (získanie), `POST /api/users` (vytvorení), `PUT /api/users/1` (aktualizace), `DELETE /api/users/1` (smazání)
  - HTTP se používá jako aplikačné protokol, ne jen transport
  - intuitivní a snadno pochopitelné API

- **Level 3 (Hypermedia/HATEOAS - Hypermedia As The Engine Of Application State)**
  - odpovedi obsahují odkazy na související akce a možné stavy
  - klient muže dynamicky objevovat možnosti API bez hard-coded URL
  - decoupling klienta od serverov, API možno menit bez breaking changes, klienti u sebe nepotrebují uchovávat dané URI
  - nejzralejší forma REST API

```json5
{
  // Příklad HATEOAS odpovědi
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "links": {
    "self": "/api/users/1",
    "update": "/api/users/1",
    "delete": "/api/users/1",
    "orders": "/api/users/1/orders"
  }
}
```
#### WSDL (web services description language)

- standardizovaný spôsob popisu rozhrania webových služeb (jméno, lokaci, podporované protokoly, operace, formát zpráv...), používá sa sa SOAP

#### SOAP (simple object access protocol)

- komunikačné protokol pre web services, umožňuje výmenu dát, vzdálená volání funkcií
- slouží jako jednotná vrstva medzi službami (aktuálne se používá spíš gRPC)

[Go to the next question](./dev_2_analyza_a_navrh.md)
