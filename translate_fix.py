#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix and improve Czech to Slovak translations"""

import os
import re

os.chdir(r"c:\Users\Siki\source\repos\Siki-ux\sz\szmgr_2025")

# Additional translations to fix remaining Czech words
more_translations = [
    ("Metriky", "Metriky"),  # Keep as is
    ("Atributy", "Atributy"),  # Keep as is
    ("hledisko", "pohľad"),
    ("Atributu kvality", "Atribútov kvality"),
    ("atributu kvality", "atribútov kvality"),
    ("definována jako", "definovaná ako"),
    ("jak snadno", "ako ľahko"),
    ("Jak snadno", "Ako ľahko"),
    ("lze", "možno"),
    ("Lze", "Možno"),
    ("komentářů", "komentárov"),
    ("řádků", "riadkov"),
    ("zbytečně", "zbytočne"),
    ("následně", "nasledujúce"),
    ("neměřitelné", "nemerateľné"),
    ("netriviální", "netriviálne"),
    ("podstatě", "podstate"),
    ("Podstatě", "Podstate"),
    ("vzájemně", "vzájomne"),
    ("silně", "silne"),
    ("Kromě", "Okrem"),
    ("kromě", "okrem"),
    ("Často", "Často"),
    ("bývají", "býva"),
    ("bývá", "býva"),
    ("bude", "bude"),
    ("mohou", "môžu"),
    ("mají", "majú"),
    ("mít", "mať"),
    ("mohou být", "môžu byť"),
    ("se vlastně", "sa vlastne"),
    ("Dále", "Ďalej"),
    ("dále", "ďalej"),
    ("dále jsou", "ďalej sú"),
    ("Je důležité", "Je dôležité"),
    ("se může", "sa môže"),
    ("Je možné", "Je možné"),
    ("se měří", "sa meria"),
    ("se počítá", "sa počíta"),
]

files_to_fix = [
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

for filename in files_to_fix:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply translations in order (longest first)
        sorted_translations = sorted(more_translations, key=lambda x: len(x[0]), reverse=True)
        
        for czech, slovak in sorted_translations:
            if czech != slovak:
                # Use word boundary matching for more accurate replacements
                pattern = r'\b' + re.escape(czech) + r'\b'
                content = re.sub(pattern, slovak, content, flags=re.IGNORECASE)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Fixed: {filename}")

print("\nTranslation improvements complete!")
