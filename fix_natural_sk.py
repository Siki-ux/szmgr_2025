import glob
import re

adjectives_ne = [
    "konkrétní", "interní", "externí", "aktuální", "centrální", "kontinuální",
    "minimální", "maximální", "detailní", "inkrementální", "puvodní", "lokální",
    "fyzicko-virtuální", "hybridní", "logiční", "statní", "fyzický", "fyzické",
    "primární", "sekundární", "finální", "globální", "ideální", "komunikační",
    "transportní", "vysokorychlostní", "bezpečnosťní", "penetrační", "výpočetní",
    "certifikační", "virtuální"
]

exact_matches = {
    "není": "nie je",
    "rešení": "riešenie",
    "řešení": "riešenie",
    "zajištení": "zabezpečenie",
    "zajištění": "zabezpečenie",
    "omezení": "obmedzenie",
    "omezeními": "obmedzeniami",
    "chování": "správanie",
    "používání": "používanie",
    "určení": "určenie",
    "čtení": "čítanie",
    "merení": "meranie",
    "zlepšení": "zlepšenie",
    "doručení": "doručenie",
    "potvrzení": "potvrdenie",
    "získání": "získanie",
    "overení": "overenie",
    "ukládání": "ukladanie",
    "modelování": "modelovanie",
    "hledání": "hľadanie",
    "zamykání": "zamykanie",
    "provedení": "prevedenie",
    "ostatní": "ostatné",
    "vlastní": "vlastné",
    "unikátní": "unikátne",
    "víc": "viac",
    "více": "viac",
    "Víc": "Viac",
    "Více": "Viac",
    "pouze": "iba",
    "při ": "pri ",
    "pro ": "pre ",
    "zda ": "či ",
    "jejich": "ich",
    "svoje": "svoje",
    "svojí": "svojou",
    "jak ": "ako ",
    "krokem": "krokom",
    "kroku": "krokom/krokov",
    "návrhem": "návrhom",
    "chyb": "chýb",
    "způsob": "spôsob",
    "způsobu": "spôsobu",
    "způsobem": "spôsobom",
    "způsoby": "spôsoby",
    "tím": "tým",
    "zcela": "úplne",
    "přístup": "prístup",
    "přístupu": "prístupu",
    "přístupem": "prístupom",
    "často": "často",
    "nástroju": "nástrojov",
    "uživatelu": "používateľov",
    "uživateli": "používateľmi",
    "cílem": "cieľom",
    "cíl": "cieľ",
    "díky": "vďaka",
    "kvůli": "kvôli",
    "např.": "napr.",
    "tj.": "t. j.",
    "tzv.": "tzv.",
    "atd.": "atď.",
    "vč.": "vrátane",
    "třeba": "napríklad",
    "lze": "možno",
    "nelze": "nemožno",
    "jej": "ho",
    "její": "jej",
    "jehož": "ktorého",
    "protože": "pretože",
    "aby": "aby",
    "pokud": "ak",
    "zda-li": "či",
    "zda": "či",
    "nebo": "alebo",
    "ale": "ale",
    "však": "však",
    "když": "keď",
    "tedy": "teda",
    "tudíž": "teda",
    "stejný": "rovnaký",
    "stejná": "rovnaká",
    "stejné": "rovnaké",
    "společný": "spoločný",
    "společná": "spoločná",
    "společné": "spoločné",
    "různý": "rôzny",
    "různá": "rôzna",
    "různé": "rôzne",
    "použitelný": "použiteľný",
    "bezpečnostní": "bezpečnostné",
    "síť": "sieť",
    "sítě": "siete",
    "síti": "sieti",
    "sítí": "sietí",
    "zařízení": "zariadenie",
    "článku": "článkov",
    "bodu": "bodov",
    "systému": "systémov", # in genitive plural mostly
    "serveru": "serverov",
    "klientu": "klientov",
    "souboru": "súborov",
    "uživatelů": "používateľov",
    "modelu": "modelov",
    "případů": "prípadov",
    "dat": "dát",
    "části": "časti",
    "kroků": "krokov",
    "testů": "testov",
    "chyb": "chýb", # repeated ok
    "změn": "zmien",
    "nákladů": "nákladov",
    "zdrojů": "zdrojov",
    "vlastností": "vlastností",
}

def replace_with_case(match, new_word):
    orig = match.group(0)
    if orig.isupper():
        return new_word.upper()
    elif orig[0].isupper():
        return new_word.capitalize()
    return new_word

def fix_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content
    
    # regex for gerunds
    content = re.sub(r'([a-zA-ZáčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]+)ování\b', lambda m: m.group(1) + 'ovanie', content)
    content = re.sub(r'([a-zA-ZáčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]+)ávání\b', lambda m: m.group(1) + 'ávanie', content)
    content = re.sub(r'([a-zA-ZáčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]+)inování\b', lambda m: m.group(1) + 'inovanie', content)
    content = re.sub(r'([a-zA-ZáčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]+)nění\b', lambda m: m.group(1) + 'nenie', content)
    
    # Exact word replacements
    for cz, sk in exact_matches.items():
        # Case insensitive exact word match
        pattern = re.compile(r'\b' + re.escape(cz) + r'\b', re.IGNORECASE)
        content = pattern.sub(lambda m: replace_with_case(m, sk), content)

    # Adjectives replacing 'í' with 'é'
    for adj in adjectives_ne:
        pattern = re.compile(r'\b' + re.escape(adj) + r'\b', re.IGNORECASE)
        # Slovak equivalent ends with 'é' for adjectives to be neutral/plural which is a safe default here
        sk_adj = adj[:-1] + 'é'
        content = pattern.sub(lambda m: replace_with_case(m, sk_adj), content)

    # Some targeted post-processing
    content = content.replace("systémovv", "systémov")
    content = content.replace("môžeovanie", "modelovanie") # fallback if regex broke it
    
    if content != orig_content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

if __name__ == "__main__":
    count = 0
    for file in glob.glob("*.md"):
        if fix_file(file):
            print(f"Fixed {file}")
            count += 1
    print(f"Total files fully naturalized: {count}")
