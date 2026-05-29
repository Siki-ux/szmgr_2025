#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob

# Spelling, grammar, and remaining Czechism fixes
fixes = {
    # Užívateľ vs Používateľ (sk grammar)
    "užívateľské": "používateľské",
    "užívateľský": "používateľský",
    "užívateľského": "používateľského",
    "užívateľa": "používateľa",
    "užívateľov": "používateľov",
    "užívatelia": "používatelia",
    "Užívateľské": "Používateľské",
    "Užívatelia": "Používatelia",
    "užívateľ": "používateľ",
    "Užívateľ": "Používateľ",
    "užívateľom": "používateľom",
    "Užívateľom": "Používateľom",

    # Common grammar and stylistics
    "znovu použiteľnosť": "znovupoužiteľnosť",
    "Znovu použiteľnosť": "Znovupoužiteľnosť",
    " zložitosť ": " komplexnosť ", # in technical context
    "počas určitú dobu": "po určitú dobu",
    "Toho dosiahneme": "To dosiahneme",
    "dostáť požiadavkám": "naplniť požiadavky",
    "aby sa vývoj vykonávali": "aby sa vývoj vykonával",

    # Pre-existing Czechisms in the final pass
    "síte": "siete",
    "Síte": "Siete",
    "sítí": "sietí",
    "integrační": "integračné",
    "relačních": "relačných",
    "dátabáz": "databáz",
    "dátabáza": "databáza",
    "dátabázy": "databázy",
    "Dátabáz": "Databáz",
    "Dátabáza": "Databáza",
    "Dátabázy": "Databázy",
    "definice": "definícia",
    "Definice": "Definícia",
    "manipulace": "manipulácia",
    "Manipulace": "Manipulácia",
    "dátového schématu": "dátovej schémy",
    "Relační ": "Relačná ",
    "relační ": "relačná ",
    "s daty": "s dátami",
    "s datami": "s dátami", # proper is dátami
    "integritní ": "integritné ",
    "rízení ": "riadenie ",
    "Rízení ": "Riadenie ",
    "hašování": "hašovanie",
    "výše uvedené": "vyššie uvedené",
    "pro vše vyššie": "pre všetko vyššie",
    "pro vše": "pre všetko",
    "príklady z praxe pro": "príklady z praxe pre",
    "všetko výše uvedené": "všetko vyššie uvedené",

    "propojená": "prepojená",
    "komunikačnémi": "komunikačnými",
    "kanály": "kanálmi",
    "která ": "ktorá ",
    "které ": "ktoré ",
    "který ": "ktorý ",
    "sdílení": "zdieľanie",
    "prostredku": "prostriedkov",
    "souboru": "súborov",
    "Ideální ": "Ideálna ",
    "neomezenou": "neobmedzenou",
    "propustností": "priepustnosťou",
    "bezztrátová": "bezstratová",
    "zachovávající": "zachovávajúca",
    "poradí": "poradie",
    "paketu": "paketov",
    "V reálu": "V realite",
    "takové": "takéto",
    "zpusob": "spôsob",
    "zpusoby": "spôsoby",
    "zpusobem": "spôsobom",
    "fáze": "fázy",
    "fází": "fáz",
    "provoz": "prevádzka",
    "provozu": "prevádzky",
    "Rozdíly": "Rozdiely",
    "rozdíly": "rozdiely",
    " zda ": " či ",
    "jakým": "akým",
    "uchopitelnejší": "uchopiteľnejšie",
    "Dusledkem": "Dôsledkom",
    "ruzný": "rôzny",
    "ruznými": "rôznymi",
    "ruzných": "rôznych",
    "ruzným": "rôznym",
    "ruzné": "rôzne",
    "nekolik": "niekoľko",
    "Skládá": "Skladá",
    "požadavku": "požiadaviek",
    "požiadavku": "požiadaviek", # usually means plural when taking from CZ
    " mezi ": " medzi ",
    " tím, ": " tým, ", # but carefully
    " ríká, ": " hovorí, ",
    "skutečne": "skutočne",
    "potrebuje": "potrebuje",
    "Pro lepší": "Pre lepšiu",
    "mužeme": "môžeme",
    "sledovat": "sledovať",
    "súčasným": "súčasným",
    "rešením": "riešením",
    "zajímá": "zaujíma",
    "zmiňuje": "zmieňuje",
    "V takových": "V takých",
    "případech": "prípadoch",
    " ptát": " pýtať",
    "Muže ": "Môže ",
    " jít ": " ísť ",
    "duvod": "dôvod",
    " také ": " tiež ",
    "treba": "napríklad",
    "nevedomost": "nevedomosť",
    "proveditelnosti": "uskutočniteľnosti",
    "dle návrhu": "podľa návrhu",
    "dle ": "podľa ",
    "tvorba": "tvorba",
    "zarízení": "zariadení",
    "uživatele": "používateľa",
    "uživatelem": "používateľom",
    "uživateli": "používateľmi",
    " Uživatele": " Používateľa",
    "uživatel": "používateľ",
    "Uživatel": "Používateľ",
    "vlastností": "vlastností",

    " softwarových": " softvérových",
    " softwarové": " softvérové",
    " softwarový": " softvérový",
    " Softwarové": " Softvérové",

    # other typos
    "úrovnich": "úrovniach",
    "částech": "častiach",
    "části": "časti",
    "otázce": "otázke",
    "volba": "voľba",
    "prostredí": "prostredia",
    "rozsáhlých": "rozsiahlych",
    "Víc ": "Viac ",
    "více ": "viac ",
    "Více ": "Viac ",
    "základní": "základné",
    "Základní": "Základné",
    "Vícevrstvá": "Viacvrstvová",
    "Vhodné": "Vhodné",
    "vhodné": "vhodné",
}

def fix_silesian(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

    old_content = content
    for word_cz, word_sk in fixes.items():
        content = content.replace(word_cz, word_sk)
    
    # targeted fixes
    content = content.replace("požiadavku klienta", "požiadaviek klienta")
    content = content.replace("tím, čo", "tým, čo")
    content = content.replace("ríká že", "hovorí, že")
    content = content.replace("treba o", "napríklad o")
    content = content.replace("na úrovni jednotlivých", "na úrovni jednotlivých")

    if content != old_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

if __name__ == "__main__":
    files = glob.glob("*.md")
    count = 0
    for file in files:
        if fix_silesian(file):
            print(f"Fixed spelling/grammar in {file}")
            count += 1
    print(f"Total files updated: {count}")
