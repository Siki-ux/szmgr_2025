#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Czech to Slovak translation with extensive dictionary
"""

import os
import re

os.chdir(r"c:\Users\Siki\source\repos\Siki-ux\sz\szmgr_2025")

# Comprehensive Czech → Slovak translation dictionary
# Organized by category for clarity
translations = [
    # Lifecycle and process terms
    ("Životní cyklus", "Životný cyklus"),
    ("životní cyklus", "životný cyklus"),
    ("vývoje a řízení", "vývoja a riadenia"),
    ("proces vývoje", "proces vývoja"),
    ("Nasazení a provoz", "Nasadenie a prevádzka"),
    ("nasazení a provoz", "nasadenie a prevádzka"),
    ("Údržba", "Údržba"),
    ("údržba", "údržba"),
    ("Životní cyklus SW", "Životný cyklus SW"),
    ("Agilní metodiky", "Agilné metodiky"),
    ("agilní metodiky", "agilné metodiky"),
    ("agilního vývoje", "agilného vývoja"),
    ("METODIKA", "METODIKA"),
    ("Metodika", "Metodika"),
    ("metodika", "metodika"),
    
    # Design and architecture
    ("Návrh", "Návrh"),
    ("návrh", "návrh"),
    ("Návrh systému", "Návrh systému"),
    ("návrhu", "návrhu"),
    ("návrhů", "návrhov"),
    ("návrhy", "návrhy"),
    ("Specifikace", "Špecifikácia"),
    ("specifikace", "špecifikácia"),
    ("Architektura", "Architektúra"),
    ("architektura", "architektúra"),
    ("architektury", "architektúry"),
    ("architektuře", "architektúre"),
    ("Komponenty", "Komponenty"),
    ("komponenty", "komponenty"),
    ("komponent", "komponent"),
    ("komponentu", "komponentu"),
    ("Vzory", "Vzory"),
    ("vzory", "vzory"),
    ("vzor", "vzor"),
    
    # Testing and quality
    ("Testování", "Testovanie"),
    ("testování", "testovanie"),
    ("testuje", "testuje"),
    ("testovací", "testovacie"),
    ("Testy", "Testy"),
    ("testy", "testy"),
    ("test", "test"),
    ("Jednotkové", "Jednotkové"),
    ("jednotkové", "jednotkové"),
    ("Integrační", "Integračné"),
    ("integrační", "integračné"),
    ("Funkční", "Funkčné"),
    ("funkční", "funkčné"),
    ("Akceptační", "Akceptačné"),
    ("akceptační", "akceptačné"),
    ("Regresní", "Regresné"),
    ("regresní", "regresné"),
    
    # Data and database
    ("Databáze", "Databázy"),
    ("databáze", "databázy"),
    ("databází", "databáz"),
    ("datového", "dátového"),
    ("datovém", "dátovom"),
    ("datových", "dátových"),
    ("data", "dáta"),
    ("datu", "dátam"),
    ("Zpracování", "Spracovanie"),
    ("zpracování", "spracovanie"),
    ("Zpracovávání", "Spracovávanie"),
    ("zpracovávání", "spracovávanie"),
    ("Bezpečnost", "Bezpečnosť"),
    ("bezpečnost", "bezpečnosť"),
    ("bezpečnosti", "bezpečnosti"),
    
    # Communication and interfaces
    ("Komunikace", "Komunikácia"),
    ("komunikace", "komunikácia"),
    ("Komunikační", "Komunikačné"),
    ("komunikační", "komunikačné"),
    ("Rozhraní", "Rozhrania"),
    ("rozhraní", "rozhrania"),
    ("rozhraním", "rozhraniami"),
    ("Protokol", "Protokol"),
    ("protokol", "protokol"),
    ("protokoly", "protokoly"),
    ("Protokoly", "Protokoly"),
    
    # Management and organization
    ("Plánování", "Plánovanie"),
    ("plánování", "plánovanie"),
    ("Řízení", "Riadenie"),
    ("řízení", "riadenie"),
    ("Riadenie rizik", "Riadenie rizík"),
    ("řízení rizik", "riadenie rizík"),
    ("rizika", "rizika"),
    ("Rizika", "Rizika"),
    ("riziko", "riziko"),
    ("Riziko", "Riziko"),
    
    # Development methodologies  
    ("Agilita", "Agilita"),
    ("agilita", "agilita"),
    ("SCRUM", "SCRUM"),
    ("Kanban", "Kanban"),
    ("kanban", "kanban"),
    ("Iterační", "Iteračné"),
    ("iterační", "iteračné"),
    ("iteracích", "iteráciach"),
    ("Inkrement", "Inkrement"),
    ("inkrement", "inkrement"),
    ("Sprinty", "Sprinty"),
    ("sprinty", "sprinty"),
    
    # Monitoring and deployment
    ("Monitorování", "Monitorovanie"),
    ("monitorování", "monitorovanie"),
    ("Logování", "Protokolovanie"),
    ("logování", "protokolovanie"),
    ("Nasazení", "Nasadenie"),
    ("nasazení", "nasadenie"),
    ("Selhání", "Zlyhanie"),
    ("selhání", "zlyhanie"),
    ("Výpadek", "Výpadok"),
    ("výpadek", "výpadok"),
    
    # Development tools and environment
    ("Prostředí", "Prostredie"),
    ("prostředí", "prostredie"),
    ("Nástroje", "Nástroje"),
    ("nástroje", "nástroje"),
    ("nástrojů", "nástrojov"),
    ("Editor", "Editor"),
    ("editor", "editor"),
    ("Debugger", "Debugger"),
    ("debugger", "debugger"),
    
    # Network and communication
    ("Sítě", "Siete"),
    ("sítě", "siete"),
    ("síti", "sieti"),
    ("Síť", "Sieť"),
    ("síť", "sieť"),
    ("Protokol", "Protokol"),
    ("protokol", "protokol"),
    ("IP", "IP"),
    ("TCP", "TCP"),
    ("UDP", "UDP"),
    ("HTTP", "HTTP"),
    ("HTTPS", "HTTPS"),
    ("DNS", "DNS"),
    
    # Performance and scalability
    ("Výkon", "Výkon"),
    ("výkon", "výkon"),
    ("Výkonnost", "Výkonnosť"),
    ("výkonnost", "výkonnosť"),
    ("Optimalizace", "Optimalizácia"),
    ("optimalizace", "optimalizácia"),
    ("Škálovatelnost", "Škálovateľnosť"),
    ("škálovatelnost", "škálovateľnosť"),
    ("Škálování", "Škálovanie"),
    ("škálování", "škálovanie"),
    
    # Documentation and comments
    ("Dokumentace", "Dokumentácia"),
    ("dokumentace", "dokumentácia"),
    ("Komentáře", "Komentáre"),
    ("komentáře", "komentáre"),
    ("Poznámka", "Poznámka"),
    ("poznámka", "poznámka"),
    ("Příklady", "Príklady"),
    ("příklady", "príklady"),
    ("Příklad", "Príklad"),
    ("příklad", "príklad"),
    
    # Error handling
    ("Chyba", "Chyba"),
    ("chyba", "chyba"),
    ("Chyby", "Chyby"),
    ("chyby", "chyby"),
    ("Ošetření", "Spracovanie"),
    ("ošetření", "spracovanie"),
    ("Výjimka", "Výnimka"),
    ("výjimka", "výnimka"),
    ("Výjimky", "Výnimky"),
    ("výjimky", "výnimky"),
    
    # Remaining single words and phrases
    ("Důležité", "Dôležité"),
    ("důležité", "dôležité"),
    ("důležitý", "dôležitý"),
    ("Důležitý", "Dôležitý"),
    ("Často", "Často"),
    ("často", "často"),
    ("Obtížnost", "Obtiažnosť"),
    ("obtížnost", "obtiažnosť"),
    ("Povinný", "Povinný"),
    ("povinný", "povinný"),
    ("Volitelný", "Voliteľný"),
    ("volitelný", "voliteľný"),
    ("Jednotnost", "Jednotnosť"),
    ("jednotnost", "jednotnosť"),
    ("Konzistence", "Konzistencia"),
    ("konzistence", "konzistencia"),
    ("Jednoduchá", "Jednoduchá"),
    ("jednoduchá", "jednoduchá"),
    ("Jednoduchý", "Jednoduchý"),
    ("jednoduchý", "jednoduchý"),
    ("Komplexnost", "Komplexnosť"),
    ("komplexnost", "komplexnosť"),
    ("Komplexní", "Komplexné"),
    ("komplexní", "komplexné"),
    
    # Time-related terms
    ("Dobu", "Dobu"),
    ("dobu", "dobu"),
    ("Čas", "Čas"),
    ("čas", "čas"),
    ("Doba", "Doba"),
    ("doba", "doba"),
    ("Dlouhodobě", "Dlhodobo"),
    ("dlouhodobě", "dlhodobo"),
    ("Krátkodobě", "Krátkodobě"),
    ("krátkodobě", "krátkodobě"),
    
    # State and condition
    ("Stav", "Stav"),
    ("stav", "stav"),
    ("Stavy", "Stavy"),
    ("stavy", "stavy"),
    ("Státu", "Stavu"),
    ("státu", "stavu"),
    ("Bezstavový", "Bezstavový"),
    ("bezstavový", "bezstavový"),
    
    # Relationships
    ("Závislost", "Závislosť"),
    ("závislost", "závislosť"),
    ("Závislostí", "Závislostí"),
    ("závislostí", "závislostí"),
    ("Vazby", "Väzby"),
    ("vazby", "väzby"),
    ("Vazba", "Väzba"),
    ("vazba", "väzba"),
    
    # Quality attributes continued
    ("Modularita", "Modularita"),
    ("modularita", "modularita"),
    ("Čitelnost", "Čitateľnosť"),
    ("čitelnost", "čitateľnosť"),
    ("Pochopitelnost", "Pochopiteľnosť"),
    ("pochopitelnost", "pochopiteľnosť"),
    ("Údržitelnost", "Údržateľnosť"),
    ("údržitelnost", "údržateľnosť"),
    ("Rozšiřitelnost", "Rozšíriteľnosť"),
    ("rozšiřitelnost", "rozšíriteľnosť"),
    ("Opakovanost", "Opakovateľnosť"),
    ("opakovanost", "opakovateľnosť"),
    
    # Framework and patterns
    ("Vzory", "Vzory"),
    ("Designové", "Návrhové"),
    ("designové", "návrhové"),
    ("Architektonické", "Architektonické"),
    ("architektonické", "architektonické"),
    ("Model", "Model"),
    ("model", "model"),
    ("MVC", "MVC"),
    ("MVP", "MVP"),
    ("MVVM", "MVVM"),
    
    # Implementation details
    ("Implementace", "Implementácia"),
    ("implementace", "implementácia"),
    ("Implementační", "Implementačné"),
    ("implementační", "implementačné"),
    ("Kód", "Kód"),
    ("kód", "kód"),
    ("Kódů", "Kódov"),
    ("kódů", "kódov"),
    ("Klíč", "Kľúč"),
    ("klíč", "kľúč"),
    ("Klíčové", "Kľúčové"),
    ("klíčové", "kľúčové"),
    
    # Capabilities and features
    ("Možnosti", "Možnosti"),
    ("možnosti", "možnosti"),
    ("Schopnost", "Schopnosť"),
    ("schopnost", "schopnosť"),
    ("Schopnosti", "Schopnosti"),
    ("schopnosti", "schopnosti"),
    ("Funkce", "Funkcia"),
    ("funkce", "funkcia"),
    ("Funkcí", "Funkcií"),
    ("funkcí", "funkcií"),
    ("Funkcionalita", "Funkcionalita"),
    ("funkcionalita", "funkcionalita"),
]

def preserve_special_content(text):
    """Preserve code, URLs, and special content"""
    preserved = {}
    counter = 0
    
    # Preserve code blocks
    def save_code(match):
        nonlocal counter
        placeholder = f"__CODE_{counter}__"
        preserved[placeholder] = match.group(0)
        counter += 1
        return placeholder
    
    text = re.sub(r'```[\s\S]*?```', save_code, text)
    
    # Preserve URLs
    def save_url(match):
        nonlocal counter
        placeholder = f"__URL_{counter}__"
        preserved[placeholder] = match.group(0)
        counter += 1
        return placeholder
    
    text = re.sub(r'https?://[^\s\)]+', save_url, text)
    
    # Preserve math equations
    def save_math(match):
        nonlocal counter
        placeholder = f"__MATH_{counter}__"
        preserved[placeholder] = match.group(0)
        counter += 1
        return placeholder
    
    text = re.sub(r'\$\$[\s\S]*?\$\$', save_math, text)
    text = re.sub(r'\$[^\$]*\$', save_math, text)
    
    return text, preserved

def restore_special_content(text, preserved):
    """Restore preserved content"""
    for placeholder, original in preserved.items():
        text = text.replace(placeholder, original)
    return text

def translate_file(filename):
    """Translate a markdown file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Preserve special content
        content, preserved = preserve_special_content(content)
        
        # Apply translations
        for czech, slovak in translations:
            # Skip if same word
            if czech != slovak:
                content = content.replace(czech, slovak)
        
        # Restore special content
        content = restore_special_content(content, preserved)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ {filename}")
        return True
    except Exception as e:
        print(f"✗ {filename}: {e}")
        return False

# Files to translate
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

success = 0
for f in files:
    if os.path.exists(f):
        if translate_file(f):
            success += 1

print(f"\n✓ Completed: {success}/{len(files)} files")
