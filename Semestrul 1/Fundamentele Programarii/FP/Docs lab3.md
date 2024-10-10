

### Scenarii de rulare

| Iteratie | Feature                                                          |
| -------- | ---------------------------------------------------------------- |
| I1       | Introducere lista                                                |
| I2       | gasire secv max in care doua nr. consecutive difera prin nr prim |
| I3       | gasire secv max in care doua nr. consecutive difera prin nr semn |
| I4       | F4. Iesire din program                                           |

### Cazuri de testare
#### Functia ce gaseste secv max unde oricare doua elemente consecutive difera printr-un numar prim

| Date                                      | Rezultat               |
| ----------------------------------------- | ---------------------- |
| \[1,2,3,6,13,4,21,17,4,2,69,67,86,2,9,11] | \[17,4,2,69,67,86]     |
| ----------------------------------------- | ---------------------- |
| \[1,2,3,6,13,4,21,17,4,2,69,67,86,2,9,11] | \[17,4,2,69,67,86]     |

#### Functia ce gaseste secv max unde oricare doua elemente consecutive sunt de semn contrar

| Date                         | Rezultat              |
| ---------------------------- | --------------------- |
| \[1,2,-3,6,-2,15,-17,3,5,-8] | \[2,-3,6,-2,15,-17,3] |
| ---------------------------- | --------------------- |
| \[1,2,-3,6,-2,15,-17,3,5,-8] | \[2,-3,6,-2,15,-17,3] |
