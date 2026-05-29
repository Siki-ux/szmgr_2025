#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Czech to Slovak translation script for markdown files
Preserves code blocks, links, and special formatting
"""

import re
import os

# Comprehensive Czech → Slovak translation dictionary (as list of tuples for order preservation)
TRANSLATIONS = [
    # File titles and main headers
    "Kvalita kódu": "Kvalita kódu",
    "Softwarové inženýrství": "Softvérové inžinierstvo",
    "Projektové řízení": "Projektové riadenie",
    "Databáze": "Databázy",
    "Počítačové sítě": "Počítačové siete",
    "Distribuované systémy": "Distribuované systémy",
    "Programování a softwarový vývoj": "Programovanie a softvérový vývoj",
    "Analýza a návrh systémů": "Analýza a návrh systémov",
    "Zpracování dat": "Spracovanie dát",
    "Bezpečný kód": "Bezpečný kód",
    "Uživatelská rozhraní": "Používateľské rozhrania",
    
    # Common terms - must be careful with word boundaries
    "Kvalita ve vývoji": "Kvalita v vývoji",
    "softwarových systémů": "softvérových systémov",
    "softwarové metriky": "softvérové metriky",
    "softwarového vývoje": "softvérového vývoja",
    "Taktiky pro zajištění": "Taktiky na zaistenie",
    "Principy Clean Code": "Princípy Clean Code",
    "refaktoring kódu": "refaktorovanie kódu",
    "Testování kódu": "Testovanie kódu",
    "jednotkové testy": "jednotkové testy",
    "integrační testy": "integračné testy",
    "uživatelské": "používateľské",
    "akceptační testy": "akceptačné testy",
    "Ladění a testování": "Ladenie a testovanie",
    "Proces řízení kvality": "Proces riadenia kvality",
    "Příklady z praxe": "Príklady z praxe",
    "Atributy kvality": "Atributy kvality",
    "Udržitelnost": "Udržateľnosť",
    "maintainability": "maintainability",
    "snadnost úprav": "ľahkosť úprav",
    "Výkonnost": "Výkonnosť",
    "reakční doba": "doba odozvy",
    "Spolehlivost": "Spoľahlivosť",
    "pravděpodobnost": "pravdepodobnosť",
    "bezchybného fungování": "bezchybného fungovania",
    "Testovatelnost": "Testovateľnosť",
    "Škálovatelnost": "Škálovateľnosť",
    "zpracovat větší množství": "spracovať väčšie množstvo",
    "Bezpečnost": "Bezpečnosť",
    "odolný vůči útokům": "odolný voči útokom",
    "Použitelnost": "Použiteľnosť",
    "snadnost používání": "ľahkosť používania",
    "učení se": "učenia sa",
    "správná funkcionalita": "správna funkcionalita",
    "obvykle": "zvyčajne",
    "Důležitý aspekt": "Dôležitý aspekt",
    "při vývoji": "počas vývoja",
    "se může lišit": "sa môže líšiť",
    "podle hlediska": "podľa pohľadu",
    "Z pohledu": "Z pohľadu",
    "Z pohledu vývojáře": "Z pohľadu vývojára",
    "Z pohledu managera": "Z pohľadu manažéra",
    "Zákaznické požadavky": "Požiadavky zákazníka",
    "externí kvalita": "vonkajšia kvalita",
    "aby šel vývoj snadno": "aby bol vývoj jednoduchý",
    "dlouhodobě udržovat": "dlhodobo udržiavať",
    "modifikovat/rozšířit": "modifikovať/rozšíriť",
    "interní kvalitu": "vnútornú kvalitu",
    "modularita": "modularita",
    "jednoduchost": "jednoduchosť",
    "testovatelnost": "testovateľnosť",
    "přizpůsobitelnost": "prispôsobiteľnosť",
    "čitelnost kódu": "čitateľnosť kódu",
    "znovupoužitelnost": "opätovná použiteľnosť",
    "přenositelnost": "prenositeľnosť",
    "dodržování": "dodržiavanie",
    "Špatná": "Zlá",
    "špatné": "zlej",
    "symptomem": "symptómom",
    "opravy chyb": "opravy chýb",
    "nemusí to být": "nemusí to byť",
    
    # Specific technical terms
    "Cyklomatická složitost": "Cyklomatická zložitosť",
    "pokrytí testy": "pokrytí testami",
    "pokrytí testů": "pokrytí testov",
    "počet řádků kódu": "počet riadkov kódu",
    "Měřitelné aspekty": "Merateľné aspekty",
    "Měřit": "Merať",
    "Měří": "Meria",
    "Měřením": "Meraním",
    "změřit": "zmerať",
    "změříme": "zmeráme",
    "změřitpřímo": "zmerať priamo",
    "Přímé": "Priame",
    "Odvozené": "Odvodené",
    "vypočítané": "vypočítané",
    "hustota defektů": "hustota defektov",
    "defektů": "defektov",
    "defekt": "defekt",
    "defekty": "defekty",
    "počet defektů": "počet defektov",
    
    # Processes and methodologies
    "Procesní metriky": "Procesné metriky",
    "Produktové metriky": "Produktové metriky",
    "Zdrojové metriky": "Zdrojové metriky",
    "průměrný čas": "priemerný čas",
    "průměrná": "priemerná",
    "produktivita": "produktivita",
    "vlastnosti softwaru": "vlastnosti softvéru",
    "vlastnosti samotného": "vlastnosti samého",
    "výkonnost": "výkonnosť",
    "poměry": "pomery",
    "poměr komentářů": "pomer komentárov",
    "Metriky": "Metriky",
    "nebezpečné": "nebezpečné",
    "hodnocení výkonu": "hodnotenie výkonu",
    
    # Quality-related verbs and phrases
    "kešování": "kešovanie",
    "paralelismus": "paralelizmus",
    "asynchronní komunikace": "asynchronná komunikácia",
    "detekce": "detekcia",
    "mitigace": "zmiernenie",
    "bottlenecků": "bottleneckov",
    "profiler": "profiler",
    "náprava": "náprava",
    "zdrojů": "zdrojov",
    "nespolehlivosti": "nespoľahlivosti",
    "kontrolní mechanismy": "kontrolné mechanizmy",
    "ošetření": "spracovanie",
    "chyb": "chýb",
    "automatický reporting": "automatické hlásenie",
    "neočekávaných": "neočakávaných",
    "timeout": "timeout",
    "requestu": "požiadavky",
    "monitorování": "monitorovanie",
    "logování": "protokolovanie",
    "sběr": "zber",
    "událostí": "udalostí",
    "snapshoty": "snímky",
    "rollback": "rollback",
    "pádu": "pádu",
    "selhání": "zlyhania",
    "odeslání": "odoslania",
    "formuláře": "formuláre",
    "přesměrovat": "presmerovaťna",
    "předvyplněný": "predvyplnený",
    "frustraci": "frustráciu",
    "usera": "užívateľa",
    "transakce": "transakcie",
    "kontrol vstupů": "kontrola vstupov",
    "úrovní": "úrovniach",
    "odstranění": "odstránenie",
    "single point of failure": "single point of failure",
    
    # Architectural terms
    "separace dat": "separácia dát",
    "globálního stavu": "globálneho stavu",
    "dependency separation": "dependency separation",
    "refaktoring": "refaktorovanie",
    "jednodušší": "jednoduchší",
    "jednotky": "jednotky",
    "nasaditelné": "nasaditeľné",
    "extrakce": "extrakcia",
    "umožnění": "umožnenie",
    "paralelizace": "paralelizácia",
    "subsystému": "subsystému",
    "distribuce": "distribúcia",
    "replikace": "replikácia",
    "šifrované komunikace": "šifrovanej komunikácie",
    
    # UX/Interface terms
    "zlepšení UX": "zlepšenie UX",
    "taktiky pro zlepšení": "taktiky na zlepšenie",
    "pomalé": "pomalé",
    
    # Architecture and design patterns
    "Architektura": "Architektúra",
    "architektury": "architektúry",
    "architektuře": "architektúre",
    "architekturou": "architektúrou",
    "architekturě": "architektúre",
    "Komponenty": "Komponenty",
    "komponenty": "komponenty",
    "Návrhové vzory": "Návrhové vzory",
    "vzory": "vzory",
    "vzor": "vzor",
    
    # Processing and data
    "Zpracování": "Spracovanie",
    "zpracovávají": "spracovávajú",
    "zpracování": "spracovanie",
    "zpracovávání": "spracovávanie",
    "zpracovat": "spracovať",
    
    # Common Czech → Slovak conversions
    "ů": "u",
    "ě": "e",
    "ř": "r",
    "č": "č",
    "š": "š",
    "ž": "ž",
    "ý": "ý",
    "á": "á",
    "é": "é",
    "í": "í",
    "ó": "ó",
    "ú": "ú",
    
    # Specific phrases with context
    "Klasifikace metrik": "Klasifikácia metrík",
    "Často nás zajímají": "Často nás zaujímajú",
    "Metriky je ale nebezpečné": "Metriky je ale nebezpečné",
}

def preserve_code_blocks(content):
    """Extract and preserve code blocks to avoid translation"""
    code_blocks = {}
    counter = 0
    
    # Find code blocks
    def replace_code(match):
        nonlocal counter
        placeholder = f"__CODE_BLOCK_{counter}__"
        code_blocks[placeholder] = match.group(0)
        counter += 1
        return placeholder
    
    # Match triple backticks code blocks
    content = re.sub(r'```[\s\S]*?```', replace_code, content)
    
    return content, code_blocks

def restore_code_blocks(content, code_blocks):
    """Restore preserved code blocks"""
    for placeholder, code in code_blocks.items():
        content = content.replace(placeholder, code)
    return content

def translate_text(text):
    """Translate text using the dictionary while preserving special elements"""
    # Preserve code blocks
    text, code_blocks = preserve_code_blocks(text)
    
    # Apply translations (order matters - longer strings first to avoid partial replacements)
    sorted_translations = sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)
    
    for czech, slovak in sorted_translations:
        # Use word boundaries for most translations to avoid partial replacements
        if len(czech) > 3:  # Only use word boundaries for longer phrases
            pattern = r'\b' + re.escape(czech) + r'\b'
            text = re.sub(pattern, slovak, text, flags=re.IGNORECASE | re.MULTILINE)
        else:
            text = text.replace(czech, slovak)
    
    # Restore code blocks
    text = restore_code_blocks(text, code_blocks)
    
    return text

def translate_file(input_path, output_path=None):
    """Translate a single markdown file"""
    if output_path is None:
        output_path = input_path
    
    # Read the file
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Translate
    translated = translate_text(content)
    
    # Write the file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(translated)
    
    print(f"Translated: {input_path} -> {output_path}")

def main():
    files_to_translate = [
        "1_kvalita_kodu.md",
        "2_softwarove_inzenyrstvi.md",
        "3_projektove_rizeni.md",
        "4_databaze.md",
        "5_pocitacove_site.md",
        "6_distribuovane_systemy.md",
        "dev_1_programovani_a_softwarovy_vyvoj.md",
        "dev_2_analyza_a_navrh.md",
        "dev_3_zpracovani_dat.md",
        "dev_4_bezpecny_kod.md",
        "dev_5_uzivatelska_rozhrani.md",
    ]
    
    for filename in files_to_translate:
        filepath = os.path.join(os.getcwd(), filename)
        if os.path.exists(filepath):
            translate_file(filepath)
        else:
            print(f"File not found: {filepath}")

if __name__ == "__main__":
    main()
