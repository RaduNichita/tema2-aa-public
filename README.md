## Analiza Algoritmilor 2023 - Tema2

### Structură arhivă
```bash
student@aa:$ tree -L 1
.
├── check
├── check_utils
├── install.sh
├── Makefile.example_cpp
├── Makefile.exampleJava
├── README.md
├── sat_oracle.py
├── task.h
├── Task.java
└── tasks
```
### Structură cod

Pentru rezolvarea task-urilor `trial` și `rise`, recomandăm modularizare în următoarele funcții:

1. o funcție care citește de la `stdin` datele de intrare.
1. o funcție care formulează clauzele către oracol.
1. o funcție care apelează oracolul (deja implementată).
1. o funcție care descifrează (prelucrează) răspunsul oracolului.
1. o funcție care afișează rezultatul la `stdout`.

Pentru fiecare din limbajele `C++` și `Java` există o clasă
ce conține cele 5 metode menționate anterior, din care puteți moșteni câte o clasă pentru fiecare problemă in parte (e.g: puteți avea clasele Task1, Task2, Task3 care moștenesc clasa abstractă Task).

Trebuiesc implementate doar metodele 1, 2, 4, 5. Apelarea oracolului este deja realizată de funcția `ask_oracle` (`askOracle`). Va trebui **doar** să o apelați după ce formulați clauzele SAT corespunzătoare fiecărei probleme.

Pentru rezolvarea task-ului `redemption` se poate folosi orice abordare.

### Makefile

Pentru fiecare problemă, va trebui să fie o regulă corespunzătoare în Makefile run_`<nume_problema`> (e.g: `run_rise`)

Există câte un exemplu pentru fiecare din limbajele `C++` și `Java`. **Nu este permisă folosirea flag-urilor de optimizare.**

### Rulare checker

Pentru a rula checker-ul, folosiți comanda `./check`

Pentru a rula un anumit task, folosiți comanda `./check --task {nume_task}`. (exemplu: `./check --task rise`).

Testele pentru fiecare problemă se găsesc în folder-ul `tasks/<nume_problema>/tests`. (exemplu: testele pentru problema rise se găsesc în folder-ul `tasks/rise/tasks`).

După rularea checker-ului, pentru fiecare test este generat un fișier de output în folderul (`tasks/<nume_problemă>/tests/<XY-nume_problemă>/<XY-nume_problemă.out>`), unde XY este numărul testului
(exemplu: **după** rularea checker-ului, rezultatul testului 00 pentru problema `rise`, output-ul se va găsi la ` tasks/rise/tests/00-rise/00-rise.out`).

### Mod de testare

* `trial` : fișierele de referință conțin doar `True` sau `False`, reprezentând dacă fișierul de input are sau nu soluție.
Dacă răspunsul este `True`, checker-ul va verifica că indicii afisați formează un set cover valid.

* `rise` : fișierele de referință conține numărul minim de pachețele achiziționate. Checker-ul va verifica că indicii pachețelelor afisațe conțin cărțile dorite.

* `redemption` : fișierele de referință conține numărul minim de pachețele achiziționate. Checker-ul va verifica că indicii pachețelelor afisațe conțin cărțile dorite.

Pentru a măsura performanța algoritmului vom folosi următoarea formulă:

```python
factor1 = (min(given_elems, expected_elems) / expected_elems)

factor2 = 1 - ((abs(given_sets - expected_sets)) / expected_sets)

return 0.5 * factor1 + 0.5 * factor2
```

unde

* given_sets = numărul de pachețele date în soluția voastră
* expected_sets-uri = numărul de pachețele din soluția optimă
* given_elems = cărțile necesare date în soluția voastră
* expected_elems = cărțile necesare

Punctarea se va face astfel:

* un scor `<= 0.6` va fi punctat cu 0p
* un scor `>= 0.9` va fi punctat cu 3p, punctajul maxim pe test.
* un scor s între 0.6 și 0.9 va fi punctat liniar după formula:
```
    punctaj = (s - 0.6) / (0.9 - 0.6) * 3p
```

Exemplu:

1. un scor de `0.75` va obține `1.5p / 3p`
1. un scor de `0.8` va fi punctat cu `2p / 3p`
