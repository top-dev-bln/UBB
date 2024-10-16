

### Scenariu de rulare prop1

| Program                                                                                                                                                                        | Utilizator              | Descriere                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- | -------------------------------------------- |
| meniu\*<br>1. Citire Lista<br>2. oricare doua elemente consecutive difera printr-un numar prim<br>3. are oricare doua elemente consecutive sunt de semne contrare<br>4. Iesire |                         | se afiseaza meniu                            |
|                                                                                                                                                                                | 1                       | utilizatorul introduce 1 pentru citire lista |
| introdu o lista de numere separate prin spatiu                                                                                                                                 |                         | mesaj ce confirma receptarea listei          |
|                                                                                                                                                                                | 3 5 8 10 13 17 22 27 34 | lista introdusa la tastatura de utilizator   |
| meniu*                                                                                                                                                                         |                         | se afiseaza meniu                            |
|                                                                                                                                                                                | 2                       | utilizatorul introduce 2 pentru funct.1      |
| \[3, 5, 8, 10, 13]                                                                                                                                                             |                         | rezultat afisat in consola                   |
| meniu\*                                                                                                                                                                        |                         | se afiseaza meniu                            |
|                                                                                                                                                                                | 1                       | utilizatorul introduce 1 pentru citire lista |
| introdu o lista de numere separate prin spatiu                                                                                                                                 |                         | mesaj ce confirma receptarea listei          |
|                                                                                                                                                                                | 5 11 15 16              | lista introdusa la tastatura de utilizator   |
| meniu\*                                                                                                                                                                        |                         | se afiseaza meniu                            |
|                                                                                                                                                                                | 2                       | utilizatorul introduce 2 pentru funct.1      |
| \[]                                                                                                                                                                            |                         | rezultat afisat in consola                   |
### Scenariu de rulare prop2

| Program                                                                                                                                                                        | Utilizator                | Descriere                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- | -------------------------------------------- |
| meniu\*<br>1. Citire Lista<br>2. oricare doua elemente consecutive difera printr-un numar prim<br>3. are oricare doua elemente consecutive sunt de semne contrare<br>4. Iesire |                           | se afiseaza meniu                            |
|                                                                                                                                                                                | 1                         | utilizatorul introduce 1 pentru citire lista |
| introdu o lista de numere separate prin spatiu                                                                                                                                 |                           | mesaj ce confirma receptarea listei          |
|                                                                                                                                                                                | 1 2 -3 6 -2 15 -17 3 5 -8 | lista introdusa la tastatura de utilizator   |
| meniu\*                                                                                                                                                                        |                           | se afiseaza meniu                            |
|                                                                                                                                                                                | 3                         | utilizatorul introduce 3 pentru funct.2      |
| \[2, -3, 6, -2, 15, -17, 3]                                                                                                                                                    |                           | rezultat afisat in consola                   |
|                                                                                                                                                                                |                           | se afiseaza meniu                            |
|                                                                                                                                                                                | 1                         | utilizatorul introduce 1 pentru citire lista |
| introdu o lista de numere separate prin spatiu                                                                                                                                 |                           | mesaj ce confirma receptarea listei          |
|                                                                                                                                                                                | 0 -1 1 0 -2 2             | lista introdusa la tastatura de utilizator   |
| meniu\*                                                                                                                                                                        |                           | se afiseaza meniu                            |
|                                                                                                                                                                                | 3                         | utilizatorul introduce 3 pentru funct.2      |
| \[-1, 1]                                                                                                                                                                       |                           | rezultat afisat in consola                   |




### Cazuri de testare

#### Funcția ce găsește secv max unde oricare două elemente consecutive diferă printr-un număr prim

| Date                                      | Rezultat               |
| ----------------------------------------- | ---------------------- |
| \[1,2,3,6,13,4,21,17,4,2,69,67,86,2,9,11] | \[17,4,2,69,67,86]     |
| \[6,4,12,7,8,235,12,7,9,16,27]            | \[4,12,7,8]            |
| \[19,2,3,5,7,13,17]                       | \[2,3,5,7,13,17]       |
| \[10,12,14,15,18,23]                      | \[10,12]               |

#### Funcția ce găsește secv max unde oricare două elemente consecutive sunt de semn contrar

| Date                         | Rezultat              |
| ---------------------------- | --------------------- |
| \[1,2,-3,6,-2,15,-17,3,5,-8] | \[2,-3,6,-2,15,-17,3] |
| \[-1,4,-6,8,-10,12,-14]      | \[-1,4,-6,8,-10,12]   |
| \[0,5,-5,10,-10,15,-15]      | \[5,-5,10,-10,15,-15] |
| \[9,-2,3,5,6]                | \[9,-2]               |