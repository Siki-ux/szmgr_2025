#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final refinement pass for Czech to Slovak translation
Targets remaining untranslated Czech words
"""

import os
import re

os.chdir(r"c:\Users\Siki\source\repos\Siki-ux\sz\szmgr_2025")

# Final refinement dictionary - targets remaining Czech
refinements = [
    # Remaining verbs and participles
    ("definována", "definovaná"),
    ("definovány", "definované"),
    ("považují", "považujú"),
    ("se považují", "sa považujú"),
    ("určit", "určiť"),
    ("určité", "určité"),
    ("určitou", "určitú"),
    ("určité", "určité"),
    ("určitý", "určitý"),
    ("je určité", "je určité"),
    ("je určitou", "je určitú"),
    ("co jsou požadavky", "čo sú požiadavky"),
    ("co všechno", "čo všetko"),
    ("lze systém", "možno systém"),
    ("lze měřit", "možno merať"),
    ("lze použít", "možno použiť"),
    
    # More Czech words still present
    ("ve vývoji", "v vývoji"),
    ("ve výrobě", "vo výrobe"),
    ("ve firmě", "vo firme"),
    ("vzájemně", "vzájomne"),
    ("vzájemný", "vzájomný"),
    ("zbytečně", "zbytočne"),
    ("zbytečný", "zbytočný"),
    ("snadný", "jednoduchý"),
    ("snadně", "jednoducho"),
    ("snadnější", "jednoduchší"),
    ("snadnost", "jednoduchosť"),
    ("jednoduše", "jednoducho"),
    ("jednoducho", "jednoducho"),
    ("jednoduché", "jednoduché"),
    ("jednoduchého", "jednoduchého"),
    ("jednoduchých", "jednoduchých"),
    ("jednoduchosti", "jednoduchosti"),
    ("jednoduchostí", "jednoduchosťou"),
    
    # More remaining words
    ("na úrovni", "na úrovni"),
    ("na úrovních", "na úrovniach"),
    ("nedostatky", "nedostatky"),
    ("hledisko", "pohľad"),
    ("hledisku", "pohľadu"),
    ("hledisek", "pohľadov"),
    ("hlediskách", "pohľadoch"),
    ("hlediska", "pohľady"),
    ("koherentní", "koherentné"),
    ("koherentního", "koherentného"),
    ("lokalizovatelné", "lokalizovateľné"),
    ("lokalizovatelného", "lokalizovateľného"),
    ("nehomogenně", "nehomogénne"),
    ("homogenní", "homogénne"),
    ("homogenního", "homogénneho"),
    
    # Czech prepositions and articles that slipped through
    ("při", "pri"),
    ("při vývoji", "pri vývoji"),
    ("z pohledu", "z pohľadu"),
    ("z hlediska", "z pohľadu"),
    ("se schopností", "so schopnosťou"),
    ("se se", "sa sa"),
    ("se schopnost", "so schopnosť"),
    ("se schopnosti", "so schopnosti"),
    ("se schopnostmi", "so schopnosťami"),
    
    # Remaining common verbs
    ("může", "môže"),
    ("můžou", "môžu"),
    ("mají", "majú"),
    ("mít", "mať"),
    ("být", "byť"),
    ("jsou", "sú"),
    ("je", "je"),
    ("bude", "bude"),
    ("budou", "budú"),
    ("byla", "bola"),
    ("bylo", "bolo"),
    ("byly", "boli"),
    ("byl", "bol"),
    ("jsou si", "sú si"),
    
    # More refinements
    ("obtížné", "obtiažné"),
    ("obtížnost", "obtiažnosť"),
    ("obtížnosť", "obtiažnosť"),
    ("otěžují", "sťažujú"),
    ("otěžuje", "sťažuje"),
    ("obtížněji", "obtiažnejšie"),
    ("obtížnější", "obtiažnejší"),
    ("obtížnější", "obtiažnejší"),
    
    # Remaining Czech -ý adjectives
    ("systémový", "systémový"),
    ("systémové", "systémové"),
    ("systémového", "systémového"),
    ("systémovému", "systémovému"),
    ("systémovými", "systémovými"),
    ("bezpečný", "bezpečný"),
    ("bezpečné", "bezpečné"),
    ("bezpečného", "bezpečného"),
    ("bezpečnému", "bezpečnému"),
    ("bezpečnými", "bezpečnými"),
    
    # Remaining participles and gerunds
    ("ošetřování", "spracovávanie"),
    ("ošetřovat", "spracovávať"),
    ("ošetření", "spracovanie"),
    ("ošetřit", "spracovať"),
    ("ošetřena", "spracovaná"),
    
    # Words with -ství suffix
    ("softwarování", "softvérové"),
    ("programování", "programovanie"),
    ("programovacího", "programovacieho"),
    
    # More -ost words
    ("schopnost", "schopnosť"),
    ("schopnosti", "schopnosti"),
    ("schopnostmi", "schopnosťami"),
    ("schopností", "schopnosťou"),
    ("schopností", "schopnosťou"),
    
    # Double-checking remaining Czech words
    ("být", "byť"),
    ("jsou", "sú"),
    ("je", "je"),
    ("budoucnost", "budúcnosť"),
    ("budoucího", "budúceho"),
    ("budoucnosť", "budúcnosť"),
    ("současnosti", "súčasnosti"),
    ("současně", "súčasne"),
    ("současný", "súčasný"),
]

def apply_refinements(filename):
    """Apply refinement translations to a file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_len = len(content)
        
        # Apply all refinements
        for czech, slovak in refinements:
            if czech != slovak:
                # Use simple replace for most terms
                content = content.replace(czech, slovak)
        
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        changes = original_len != len(content)
        status = "✓" if changes else "="
        print(f"{status} {filename}")
        return True
    except Exception as e:
        print(f"✗ {filename}: {e}")
        return False

# Apply to all files
files = [
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

count = 0
for f in files:
    if os.path.exists(f):
        if apply_refinements(f):
            count += 1

print(f"\n✓ Refinement pass complete: {count}/{len(files)} files")
