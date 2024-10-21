Documentația trebuie să conțină: 
- [x] enunțul
- [x] lista de funcționalități
- [x] planul de iterații
- [x] scenarii de rulare
- [ ] lista de taskuri

##### Enunt
Creați o aplicație pentru gestiunea pachetelor de călătorie oferite de o agenție de turism. Aplicația stochează pachete de călătorie oferite clienților după cum urmează: data de început și cea de sfârșit a călătoriei, destinația și prețul.

Aplicația va permite: 
1. Adăugare 
	- Adaugă pachet de călătorie 
	- Modifică pachet de călătorie 
2. Ștergere 
	- Ștergerea tuturor pachetelor de călătorie disponibile pentru o destinație dată 
	- Ștergerea tuturor pachetelor de călătorie care au o durată mai scurtă decât un număr de zile dat 
	- Ștergerea tuturor pachetelor de călătorie care au prețul mai mare decât o sumă dată 
3. Căutare 
	- Tipărirea pachetelor de călătorie care presupun un sejur într-un interval dat (e.g. 10/08/2018 - 24/08/2018 - un pachet valid este cel a cărui dată de început este aceeași sau după de data de început citită și data de sfârșit este înainte sau aceeași cu data de sfârșit introdusă de la tastatură) 
	- Tipărirea pachetelor de călătorie cu o destinație dată și cu preț mai mic decât o sumă dată. 
	- Tipărirea pachetelor de călătorie cu o anumită dată de sfârșit 
4. Rapoarte 
	- Tipărirea numărului de oferte pentru o destinație dată. 
	- Tipărirea tuturor pachetelor disponibile într-o anumită perioadă citită de la tastatură (vezi 3.i.) în ordinea crescătoare a prețului. 
	- Tipărirea mediei de preț pentru o destinație dată 
5. Filtrare 
	- Eliminarea ofertelor care au un preț mai mare decât cel dat și o destinație diferită de cea citită de la tastatură 
	- Eliminarea ofertelor în care sejurul presupune zile dintr-o anumită lună (citită de la tastatură sub forma unui număr natural între 1 și 12) 
6. Undo 
	- Refacerea ultimei operații (lista de oferte revine la ce exista înainte de ultima operație care a modificat lista) – Nu folosiți funcția deepCopy

##### Lista Functionalitati

| Functionalitate | Descriere                                                                          |
| --------------- | ---------------------------------------------------------------------------------- |
| F1  Adăugare    | Adaugă sau modifică pachet de călătorie                                            |
| F2  Ștergere    | Ștergerea pachetelor de călătorie dupa criterii stabilite                          |
| F3  Căutare     | Tipărirea pachetelor de călătorie dupa criterii stabilite                          |
| F4  Rapoarte    | Tipărirea numărului de oferte sau a pachetelor disponibile dupa criterii stabilite |
| F5  Filtrare    | Eliminarea ofertelor dupa criterii stabilite                                       |
| F6  Undo        | Refacerea ultimei operații                                                         |
##### Plan de iteratii

| Iteratie                 | descriere                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Iteratia 0               | - **Adăugare** <br>	- Adaugă pachet de călătorie <br>	- Modifică pachet de călătorie <br>- **Ștergere** <br>	- Ștergerea tuturor pachetelor de călătorie disponibile pentru o destinație dată <br>	- Ștergerea tuturor pachetelor cu o durată mai scurtă decât un număr de zile dat <br>	- Ștergerea tuturor pachetelor cu prețul mai mare decât o sumă dată |
| Iteratia 1 <br>( Lab 4 ) | - **Cautare**<br>     - Tipărirea pachetelor într-un interval<br>     - Tipărirea pachetelor cu o destinație și preț sub o sumă<br>     - Tipărirea pachetelor cu o anumită dată de sfârșit <br>                                                                                                                                                             |
| Iteratia 2 <br>( Lab 5 ) | - **Rapoarte**<br>     - Tipărirea numărului de oferte pentru o destinație dată<br>     - Tipărirea tuturor pachetelor disponibile într-o anumită perioadă<br>     - Tipărirea mediei de preț pentru o destinație dată                                                                                                                                       |
| Iteratia 3<br> ( Lab 6 ) | - **Filtrare** <br>	- Eliminare oferte cu preț mai mare citit și o destinație diferită de cea citită<br>	- Eliminarea ofertelor în care sejurul presupune zile dintr-o anumită lună<br>- **Undo** <br>	- Refacerea ultimei operații                                                                                                                          |

##### Scenarii de rulare
###### Adaugare

| Utilizator     | Program                                                                                | Descriere                                                       |
| -------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
|                | Meniu Principal*                                                                       | se afiseaza meniul principal din care se aleg functionalitatile |
| 1              |                                                                                        | utilizatorul selecteaza adaugarea                               |
|                | Meniu Adaugare \*                                                                      | se afiseaza meniul                                              |
| 1              |                                                                                        | utilizatorul selecteaza adaugarea pachetului                    |
|                | ==Adaugare pachet nou==<br>Introduceti data de inceput<br>Ziua:<br>                    |                                                                 |
| 12             |                                                                                        |                                                                 |
|                | Luna:                                                                                  |                                                                 |
| 5              |                                                                                        |                                                                 |
|                | Anul:                                                                                  |                                                                 |
| 2024           |                                                                                        |                                                                 |
|                | Introduceti data de sfarsit<br>Ziua:                                                   |                                                                 |
| 5              |                                                                                        |                                                                 |
|                | Luna:                                                                                  |                                                                 |
| 6              |                                                                                        |                                                                 |
|                | Anul:                                                                                  |                                                                 |
| 2024           |                                                                                        |                                                                 |
|                | Destinatie:                                                                            |                                                                 |
| Grecia, Athena | <br>                                                                                   |                                                                 |
|                | Pret:                                                                                  |                                                                 |
| 1280.99        |                                                                                        |                                                                 |
|                | ==Pachet adaugat cu succes==<br>Grecia, Athena (2005-05-12 - 2005-06-05): 1280.99 Euro |                                                                 |
###### Modificare
* continand pasii de la adaugare dupa ce se mai adauga analog mai multe oferte de test

| Utilizator | Program                                                                                                                                                                                                                                                                                                                            | Descriere                                      |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
|            | Meniu Adaugare \*                                                                                                                                                                                                                                                                                                                  | se afiseaza meniul                             |
| 2          |                                                                                                                                                                                                                                                                                                                                    | utilizatorul selecteaza modificarea pachetului |
|            | ==Modificare pachet==<br>Ce pachet doriti sa modificati?<br>Grecia, Athena (2005-05-12 - 2005-06-05): 1280.99 Euro<br>Madagascar (2024-07-02 - 2024-07-12): 87.0 Euro<br>Rwanda (2004-05-12 - 2005-05-12): 420.0 Euro<br>Serbia (2004-05-12 - 2005-05-12): 69.0 Euro<br>Grecia, Athena (2024-05-16 - 2024-06-15): 100.0 Euro<br>=> |                                                |
| 1          |                                                                                                                                                                                                                                                                                                                                    |                                                |
|            | Introduceti data de inceput<br>Ziua:                                                                                                                                                                                                                                                                                               |                                                |
| 15         |                                                                                                                                                                                                                                                                                                                                    |                                                |
|            | Luna:                                                                                                                                                                                                                                                                                                                              |                                                |
| 7          |                                                                                                                                                                                                                                                                                                                                    |                                                |
|            | Anul:                                                                                                                                                                                                                                                                                                                              |                                                |
| 2024       |                                                                                                                                                                                                                                                                                                                                    |                                                |
|            | Introduceti data de sfarsit<br>Ziua:                                                                                                                                                                                                                                                                                               |                                                |
| 15         |                                                                                                                                                                                                                                                                                                                                    |                                                |
|            | Luna:                                                                                                                                                                                                                                                                                                                              |                                                |
| 8          |                                                                                                                                                                                                                                                                                                                                    |                                                |
|            | Anul:                                                                                                                                                                                                                                                                                                                              |                                                |
| 2024       |                                                                                                                                                                                                                                                                                                                                    |                                                |
|            | Destinatie:                                                                                                                                                                                                                                                                                                                        |                                                |
| Madagascar | <br>                                                                                                                                                                                                                                                                                                                               |                                                |
|            | Pret:                                                                                                                                                                                                                                                                                                                              |                                                |
| 4200.52    |                                                                                                                                                                                                                                                                                                                                    |                                                |
|            | ==Pachet modificat cu succes==<br>Madagascar (2024-07-15 - 2024-08-15): 4200.52 Euro                                                                                                                                                                                                                                               |                                                |


###### Undo
- continuand pasii de la modificare

| Utilizator | Program                                                                                                                                                                                                                                                                                                                                | Descriere                                      |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
|            | Meniu Adaugare \*                                                                                                                                                                                                                                                                                                                      | se afiseaza meniul                             |
| 3          |                                                                                                                                                                                                                                                                                                                                        | utilizatorul selecteaza functia de UNDO        |
|            | ==Undo realizat cu succes==                                                                                                                                                                                                                                                                                                            |                                                |
|            | Meniu Adaugare \*                                                                                                                                                                                                                                                                                                                      | se afiseaza meniul                             |
| 2          | <br>                                                                                                                                                                                                                                                                                                                                   | utilizatorul selecteaza modificarea pachetului |
|            | ==Modificare pachet==<br>Ce pachet doriti sa modificati?<br>Grecia, Athena (2005-05-12 - 2005-06-05): 1280.99 Euro<br>Madagascar (2024-07-02 - 2024-07-12): 87.0 Euro<br>Rwanda (2004-05-12 - 2005-05-12): 420.0 Euro<br>Serbia (2004-05-12 - 2005-05-12): 69.0 Euro<br>Grecia, Athena (2024-05-16 - 2024-06-15): 100.0 Euro<br>=><br> | pachetul a luat valoare precedenta             |
|            |                                                                                                                                                                                                                                                                                                                                        |                                                |

###### Stergere

- continuand pasii

| Utilizator | Program                                                                  | Descriere                                                                                                                       |
| ---------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
|            | Meniu Adaugare \*                                                        | se afiseaza meniul                                                                                                              |
| 9          |                                                                          | utilizatorul alege sa intre in meniul principal , inchizand sub-meniul                                                          |
|            | Meniu Principal \*                                                       |                                                                                                                                 |
| 2          |                                                                          | se alege functia de stergere                                                                                                    |
|            | Meniu Stergere \*                                                        |                                                                                                                                 |
| 1          |                                                                          | se alege stergerea dupa destinatie                                                                                              |
|            | Introduceți destinația de șters:                                         |                                                                                                                                 |
| grecia     |                                                                          |                                                                                                                                 |
|            | ai vrut sa spui Grecia, Athena<br>Da sau Nu?  =>                         | se foloseste o functie de fuzzy search pentru a gasi cea mai similara varianta posibila , functia "Did you mean x" de la google |
| Da         |                                                                          |                                                                                                                                 |
|            | Ofertele cu destinația Grecia, Athena au fost șterse.                    |                                                                                                                                 |
|            | Meniu Stergere \*                                                        |                                                                                                                                 |
| 2          |                                                                          |                                                                                                                                 |
|            | Introduceți durata de timp ( in zile ):  =>                              |                                                                                                                                 |
| 15         |                                                                          |                                                                                                                                 |
|            | Ofertele cu durata de timp mai mică sau egală cu 15 zile au fost șterse. | se sterge pachetul pentru madagascar ce are 10 zile                                                                             |
|            | Meniu Stergere \*                                                        |                                                                                                                                 |
| 3          |                                                                          |                                                                                                                                 |
|            | Introduceți prețul maxim:                                                |                                                                                                                                 |
| 420        |                                                                          |                                                                                                                                 |
|            | Ofertele cu prețul mai mare de 420.0 Euro au fost șterse.                | se sterge pachetul Serbia ce costa 69                                                                                           |

###### Cautare
- se introduc urmatoarele pachete
 1. Pachetul cu destinația Craiova are prețul 100 Euro și este disponibil între 2024-06-16 și 2024-06-20
2. Pachetul cu destinația Timisoara are prețul 87 Euro și este disponibil între 2024-07-02 și 2024-07-12
3. Pachetul cu destinația Cluj-Napoca are prețul 420 Euro și este disponibil între 2024-05-12 și 2024-08-12
4. Pachetul cu destinația Craiova are prețul 69 Euro și este disponibil între 2024-05-12 și 2024-09-12
5. Pachetul cu destinația Grecia, Athena are prețul 420 Euro și este disponibil între 2024-05-12 și 2024-08-12
6. Pachetul cu destinația Grecia, Athena are prețul 69 Euro și este disponibil între 2024-05-04 și 2024-08-12

| Utilizator | Program                                                                                                                                                          | Descriere          |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
|            | Meniu Principal*                                                                                                                                                 | se afiseaza meniul |
| 3          |                                                                                                                                                                  |                    |
|            | Meniu Cautare \*                                                                                                                                                 |                    |
| 1          |                                                                                                                                                                  |                    |
|            | Cautare pachete in functie de un interval de timp dat<br>Introduceti data de inceput<br>Ziua: <br>                                                               |                    |
| 6          |                                                                                                                                                                  |                    |
|            | Luna:                                                                                                                                                            |                    |
| 6          |                                                                                                                                                                  |                    |
|            | Anul:                                                                                                                                                            |                    |
| 2024       |                                                                                                                                                                  |                    |
|            | Introduceti data de sfarsit<br>Ziua:                                                                                                                             |                    |
| 12         |                                                                                                                                                                  |                    |
|            | Luna:                                                                                                                                                            |                    |
| 7          |                                                                                                                                                                  |                    |
|            | Anul:                                                                                                                                                            |                    |
| 2024       |                                                                                                                                                                  |                    |
|            | Craiova (2024-06-16 - 2024-06-20): 100.0 Euro<br><br>Timisoara (2024-07-02 - 2024-07-12): 87.0 Euro                                                              |                    |
|            | Meniu Cautare \*                                                                                                                                                 |                    |
| 2          |                                                                                                                                                                  |                    |
|            | Cautare pachete in functie de destinatie si pret maxim<br>Introduceti pretul maxim:                                                                              |                    |
| 100        |                                                                                                                                                                  |                    |
|            | Introduceți destinația:                                                                                                                                          |                    |
| grecia     |                                                                                                                                                                  |                    |
|            | ai vrut sa spui Grecia, Athena<br>Da sau Nu?  =>                                                                                                                 |                    |
| Da         |                                                                                                                                                                  |                    |
|            | Grecia, Athena (2024-05-04 - 2024-08-12): 69.0 Euro                                                                                                              |                    |
|            | Meniu Cautare \*                                                                                                                                                 |                    |
| 3          |                                                                                                                                                                  |                    |
|            | Cautare pachete in functie de data de sfarsit<br>Introduceti data de sfarsit<br>Ziua:                                                                            |                    |
| 12         |                                                                                                                                                                  |                    |
|            | Luna:                                                                                                                                                            |                    |
| 8          |                                                                                                                                                                  |                    |
|            | Anul:                                                                                                                                                            |                    |
| 2024       |                                                                                                                                                                  |                    |
|            | Cluj-Napoca (2024-05-12 - 2024-08-12): 420.0 Euro<br>Grecia, Athena (2024-05-12 - 2024-08-12): 420.0 Euro<br>Grecia, Athena (2024-05-04 - 2024-08-12): 69.0 Euro |                    |
###### Rapoarte
| Utilizator     | Program                                                                                              | Descriere          |
| -------------- | ---------------------------------------------------------------------------------------------------- | ------------------ |
|                | Meniu Principal*                                                                                     | se afiseaza meniul |
| 4              |                                                                                                      |                    |
|                | Meniu Rapoarte \*                                                                                    |                    |
| 1              |                                                                                                      |                    |
|                | ==Afisare numar de oferte pentru o destinatie==<br>Introduceti o destinatie:                         |                    |
| Craiova        |                                                                                                      |                    |
|                | Exista 2 oferte pentru destinatia Craiova.                                                           |                    |
|                | Meniu Rapoarte \*                                                                                    |                    |
| 2              |                                                                                                      |                    |
|                | ==Afisare pachete disponibile intr-un interval de timp==<br>Introduceti data de inceput<br>Ziua:<br> |                    |
| 6              |                                                                                                      |                    |
|                | Luna:                                                                                                |                    |
| 6              |                                                                                                      |                    |
|                | Anul:                                                                                                |                    |
| 2024           |                                                                                                      |                    |
|                | Introduceti data de sfarsit<br>Ziua:                                                                 |                    |
| 12             |                                                                                                      |                    |
|                | Luna:                                                                                                |                    |
| 7              |                                                                                                      |                    |
|                | Anul:                                                                                                |                    |
| 2024           |                                                                                                      |                    |
|                | Timisoara (2024-07-02 - 2024-07-12): 87.0 Euro <br><br>Craiova (2024-06-16 - 2024-06-20): 100.0 Euro |                    |
|                | Meniu Rapoarte \*                                                                                    |                    |
| 3              |                                                                                                      |                    |
|                | Afisare pret mediu pentru o destinatie<br>Introduceti destinatia:                                    |                    |
| Grecia, Athena |                                                                                                      |                    |
|                | Pretul mediu pentru destinatia Grecia, Athena este 244.50 Euro.                                      |                    |

###### Filtrare

| Utilizator     | Program                                                                                         | Descriere          |
| -------------- | ----------------------------------------------------------------------------------------------- | ------------------ |
|                | Meniu Principal*                                                                                | se afiseaza meniul |
| 5              |                                                                                                 |                    |
|                | Meniu Filtrare \*                                                                               |                    |
| 1              |                                                                                                 |                    |
|                | Cautare pachete in functie de destinatie si pret maxim<br>Introduceti pretul maxim:             |                    |
| 100            |                                                                                                 |                    |
|                | Introduceți destinația:                                                                         |                    |
| Grecia, Athena |                                                                                                 |                    |
|                | Grecia, Athena (2024-05-04 - 2024-08-12): 69.0 Euro                                             |                    |
|                | Meniu Filtrare\*                                                                                |                    |
| 2              |                                                                                                 |                    |
|                | Cautare pachete fara o anumita luna<br>Introduceti luna:                                        |                    |
| 5              |                                                                                                 |                    |
|                | Craiova (2024-06-16 - 2024-06-20): 100.0 Euro<br>Timisoara (2024-07-02 - 2024-07-12): 87.0 Euro |                    |






Meniu Principal \*
```python
'''
1. Adaugare
2. Stergere
3. Cautare
4. Rapoarte
5. Filtrare
6. Undo

9. Exit
'''
```

Meniu Adaugare \*
```python
'''
1. Adaugare pachet
2. Modificare pachet existent
3. Undo


9. Back
'''
```

Meniu Stergere \*
```python
'''
1. Stergere pachete dupa destinatie
2. Stergere pachete dupa durata
3. Stergere pachete dupa pret
4. Undo

9. Back
'''
```

Meniu Cautare \*
```python
'''
1. Afisare pachete intr-un interval
2. Afisare pachete cu destinatie si pret sub stabilit
3. Afisare pachete dupa data de sfarsit


9. Back
'''
```

Meniu Rapoarte \*
```python
'''
1. Afisare numarul de oferte pentru o destinatie
2. Afisare tuturor pachetelor disponibile intr-un interval (crescator dupa pret)
3. Afisare mediei de pret pentru o destinatie


9. Back
'''
```

Meniu Filtrare \*
```python
'''
1. Eliminare oferte peste buget sau destinatie diferita
2. Eliminare oferte ce presupun zile dintr-o anumita luna


9. Back
'''
```



##### Lista de task-uri

###### Documentatie
- [x] enunțul
- [x] lista de funcționalități
- [x] planul de iterații
- [x] scenarii de rulare
	- [x] adaugare
	- [x] Ștergere
	- [x] Căutare
	- [x] Rapoarte
	- [x] Filtrare
	- [x] Undo
- [ ] lista de taskuri
	- [x] adaugare
	- [ ] Ștergere
	- [ ] Căutare
	- [ ] Rapoarte
	- [ ] Filtrare
	- [x] Undo

###### Initializare
- [x] Creare modul principal ( main.py ) ce v-a rula procesul
- [x] Creare modul de interfata ce creaza instante de pachete
- [x] Creare modul ( offer.py ) ce contine sablon de pachet 
###### Adăugare
 - [x] Validare date de intrare, semnalare erori ale utilizatorului
 - [x] Creare clasa interfata care creaza instante de pachete

###### Ștergere
- [x] sterge pachete pentru o destinatie
- [x] sterge pachete cu o durata mai scurta
- [x] sterge pachete cu pret mai mare decat o suma
- [ ] testare

###### Căutare
- [x] Tipărirea pachetelor într-un interval
- [x] Tipărirea pachetelor cu o destinație și preț sub o sumă
- [x] Tipărirea pachetelor cu o anumită dată de sfârșit 
- [ ] refactorizare
- [ ] testare

###### Rapoarte
- [x] Tipărirea numărului de oferte pentru o destinație dată
- [x] Tipărirea tuturor pachetelor disponibile într-o anumită perioadă
- [x] Tipărirea mediei de preț pentru o destinație dată
- [ ] refactorizare
- [ ] testare
###### Filtrare
- [x] Eliminare oferte cu preț mai mare citit și o destinație diferită de cea citită
- [x] Eliminarea ofertelor în care sejurul presupune zile dintr-o anumită lună
- [ ] refactorizare
- [ ] testare

###### Undo
- [x] refacerea ultimei operatii