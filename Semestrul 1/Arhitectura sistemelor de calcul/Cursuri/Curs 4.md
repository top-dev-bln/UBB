### Complementul fata de 2

> [!NOTE] OBSERVATIE
> Daca as utiliza doar numere intregi pozitive, nu am avea nevoie de nici o metoda sofisticata de reprezentare a unerelor in calculator, iar simpla utilizare a bazelor de numeratie 2 si 10 ar rezolva **TOT**

Numerele interpretate cu semn sunt :
- numere pozitive (+127)
- numere negative(-128)

---
Matematic, ==**REPREZENTAREA**== unu numar **==NEGATIV==** in <u>complement fata de doi </u>
este valoarea 2<sup>n</sup>- V , unde V este valoarea absoluta a numarului reprezentat.



###### Variante complement

VARIANTA 3

Facem swap dupa primul unu de la dreapta la stanga

VARIANTA 4 
Suma valorilor absolute a celor doua valori complementare este cardinalul multimi valorilor reprezentabile pe acea dimensiune


Observatie

Carry flag este NONSENS in reprezentarea cu semn

| Reprezentare | Interpretare | Valoare  |
| ------------ | ------------ | -------- |
| 0xxxx        | Fara semn    | Pozitiva |
| 0xxxx        | Cu semn      | Pozitiva |
| 1xxxx        | Fara semn    | Pozitiva |
| 1xxxx        | Cu semn      | Negativa |

b) reprezentarea binara a valorii - abc  este complementul fata de 2 a configuratiei binare initiale