# Lonear

=============

odpovědi na otázky ze zadání:
(logistic)
1. Otázka: Které sloupce vypadají problematicky?
Odpověď: Sloupce attendance, previous_score a final_score.
2. Otázka: Jaké typy chyb jsi našel?
Odpověď: chybějící hodnoty, neplatné textové hodnoty a chybějící cílová proměnná u studenta s ID 11
3. Otázka: Proč už nepředpovídáme číslo, ale kategorii?
Odpověď: 
4. Otázka: Jaké jsou hlavní rozdíly mezi skupinami?
Odpověď: Úspěšní studenti studovali dvakrát déle, měli výrazně lepší docházku (91 % vs. 71 %) a spali déle
5. Otázka: Jak dobře model funguje a kde dělá chyby?
Odpověď: Model chyby nedělá
6. Otázka: Co znamená pravděpodobnost 0.8 a jak bys rozhodl hranici (threshold)?
Odpověď: Pravděpodobnost 0.8 znamená, že model si je na 80 % jistý úspěchem studenta.
7. Otázka: Co zvyšuje šanci na úspěch, co ji snižuje a dává to smysl?
Odpověď: Podle koeficientů modelu úspěch nejvíc zvyšuje předchozí skóre a docházka, o něco méně pak hodiny studia a spánek. Šanci naopak snižuje konzumace kávy. Výsledky dávají smysl, protože káva zde indikuje stres a učení na poslední chvíli.

(linear)
Otázka 1: Které sloupce vypadají problematicky?
Odpověď: - .. -
Otázka 2: Jaké typy chyb jsi našel?
Odpověď: - .. -
Otázka 3: Co má větší vliv – učení nebo spánek? Je vztah lineární?
Odpověď: Větší vliv má učení. Ano.
Otázka 4: Jak docházka ovlivňuje výkon?
Odpověď: Výrazně.
Otázka 5: Pomáhá káva výkonu, nebo ne?
Odpověď: Statisticky vykazuje káva silnou negativní korelaci. Pravděpodobně se ale nejedná o kauzalitu.
Otázka 6: Překvapilo tě něco na kompletní korelační matici?
Odpověď: Právě teď se na překvapení cítím příliš vyčerpaná, takže bohužel ne.
Otázka 7: Jak přesný je model? Kde dělá chyby?
Odpověď: Model je téměř stoprocentně přesný. 
Otázka 8: Co má největší vliv na výkon z pohledu koeficientů? Dává to smysl?
Odpověď: Největší vliv má hodina studia navíc. Výsledek smysl dává.

=============

lineární regrese: Snaží se daty proložit přímku.

logistická regrese: Namísto přímky používá esovitou křivku.
