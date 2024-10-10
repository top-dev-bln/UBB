

### Scenarii de rulare

| Iteratie | Feature                                                          |
| -------- | ---------------------------------------------------------------- |
| I1       | Introducere lista                                                |
| I2       | gasire secv max in care doua nr. consecutive difera prin nr prim |
| I3       | gasire secv max in care doua nr. consecutive difera prin nr semn |
| I4       | F4. Iesire din program                                           |

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