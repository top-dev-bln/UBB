Documentația trebuie să conțină: 
- [x] enunțul
- [x] lista de funcționalități
- [x] planul de iterații
- [x] scenarii de rulare
- [x] lista de taskuri

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

| Utilizator     | Program                                                                                | Descriere                                                            |
| -------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
|                | Meniu Principal*                                                                       | se afiseaza meniul principal din care se aleg functionalitatile      |
| 1              |                                                                                        | utilizatorul selecteaza adaugarea                                    |
|                | Meniu Adaugare \*                                                                      | se afiseaza meniul de adaugare                                       |
| 1              |                                                                                        | utilizatorul selecteaza adaugarea pachetului                         |
|                | ==Adaugare pachet nou==<br>Introduceti data de inceput<br>Ziua:<br>                    | mesaj ce confirma procesul de adaugare<br>si se cere ziua de inceput |
| 12             |                                                                                        | se introduce ziua de inceput                                         |
|                | Luna:                                                                                  | se cere luna  de inceput                                             |
| 5              |                                                                                        | se introduce luna de inceput                                         |
|                | Anul:                                                                                  | se cere anul  de inceput                                             |
| 2024           |                                                                                        | se introduce anul de inceput                                         |
|                | Introduceti data de sfarsit<br>Ziua:                                                   | <br>se cere ziua de sfarsit                                          |
| 5              |                                                                                        | se introduce ziua de sfarsit                                         |
|                | Luna:                                                                                  | se cere luna de sfarsit                                              |
| 6              |                                                                                        | se introduce luna de sfarsit                                         |
|                | Anul:                                                                                  | se cere anul  de sfarsit                                             |
| 2024           |                                                                                        | se introduce anul de sfarsit                                         |
|                | Destinatie:                                                                            | se cere destinatia                                                   |
| Grecia, Athena | <br>                                                                                   | se introduce destinatia                                              |
|                | Pret:                                                                                  | se cere pretul                                                       |
| 1280.99        |                                                                                        | se introduce pretul                                                  |
|                | ==Pachet adaugat cu succes==<br>Grecia, Athena (2005-05-12 - 2005-06-05): 1280.99 Euro | mesaj de confirmare a introducerii                                   |
###### Modificare
* continand pasii de la adaugare dupa ce se mai adauga analog mai multe oferte de test

| Utilizator | Program                                                                                                                                                                                                                                                                                                                            | Descriere                                      |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
|            | Meniu Adaugare \*                                                                                                                                                                                                                                                                                                                  | se afiseaza meniul                             |
| 2          |                                                                                                                                                                                                                                                                                                                                    | utilizatorul selecteaza modificarea pachetului |
|            | ==Modificare pachet==<br>Ce pachet doriti sa modificati?<br>Grecia, Athena (2005-05-12 - 2005-06-05): 1280.99 Euro<br>Madagascar (2024-07-02 - 2024-07-12): 87.0 Euro<br>Rwanda (2004-05-12 - 2005-05-12): 420.0 Euro<br>Serbia (2004-05-12 - 2005-05-12): 69.0 Euro<br>Grecia, Athena (2024-05-16 - 2024-06-15): 100.0 Euro<br>=> | afisarea pachetelor disponibile                |
| 1          |                                                                                                                                                                                                                                                                                                                                    |                                                |
|            | Introduceti data de inceput<br>Ziua:                                                                                                                                                                                                                                                                                               | si se cere ziua de inceput                     |
| 15         |                                                                                                                                                                                                                                                                                                                                    | se introduce ziua de inceput                   |
|            | Luna:                                                                                                                                                                                                                                                                                                                              | se cere luna  de inceput                       |
| 7          |                                                                                                                                                                                                                                                                                                                                    | se introduce luna de inceput                   |
|            | Anul:                                                                                                                                                                                                                                                                                                                              | se cere anul  de inceput                       |
| 2024       |                                                                                                                                                                                                                                                                                                                                    | se introduce anul de inceput                   |
|            | Introduceti data de sfarsit<br>Ziua:                                                                                                                                                                                                                                                                                               | <br>se cere ziua de sfarsit                    |
| 15         |                                                                                                                                                                                                                                                                                                                                    | se introduce ziua de sfarsit                   |
|            | Luna:                                                                                                                                                                                                                                                                                                                              | se cere luna de sfarsit                        |
| 8          |                                                                                                                                                                                                                                                                                                                                    | se introduce luna de sfarsit                   |
|            | Anul:                                                                                                                                                                                                                                                                                                                              | se cere anul  de sfarsit                       |
| 2024       |                                                                                                                                                                                                                                                                                                                                    | se introduce anul de sfarsit                   |
|            | Destinatie:                                                                                                                                                                                                                                                                                                                        | se cere destinatia                             |
| Madagascar | <br>                                                                                                                                                                                                                                                                                                                               | se introduce destinatia                        |
|            | Pret:                                                                                                                                                                                                                                                                                                                              | se cere pretul                                 |
| 4200.52    |                                                                                                                                                                                                                                                                                                                                    | se introduce pretul                            |
|            | ==Pachet modificat cu succes==<br>Madagascar (2024-07-15 - 2024-08-15): 4200.52 Euro                                                                                                                                                                                                                                               | mesaj ce confirma modificarea                  |


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


###### Stergere
- continuand pasii

| Utilizator | Program                                                                  | Descriere                                                                                                                       |
| ---------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
|            | Meniu Adaugare \*                                                        | se afiseaza meniul                                                                                                              |
| 9          |                                                                          | utilizatorul alege sa intre in meniul principal , inchizand sub-meniul                                                          |
|            | Meniu Principal \*                                                       | se afiseaza meniu                                                                                                               |
| 2          |                                                                          | se alege functia de stergere                                                                                                    |
|            | Meniu Stergere \*                                                        | se afiseaza meniu                                                                                                               |
| 1          |                                                                          | se alege stergerea dupa destinatie                                                                                              |
|            | Introduceți destinația de șters:                                         | se cere destinatia                                                                                                              |
| grecia     |                                                                          | se introduce destinatia                                                                                                         |
|            | ai vrut sa spui Grecia, Athena<br>Da sau Nu?  =>                         | se foloseste o functie de fuzzy search pentru a gasi cea mai similara varianta posibila , functia "Did you mean x" de la google |
| Da         |                                                                          | se raspunde                                                                                                                     |
|            | Ofertele cu destinația Grecia, Athena au fost șterse.                    | mesaj de confirmare                                                                                                             |
|            | Meniu Stergere \*                                                        | se afiseaza meniu                                                                                                               |
| 2          |                                                                          | se selecteaza stergerea sub durata                                                                                              |
|            | Introduceți durata de timp ( in zile ):  =>                              | se cere durata                                                                                                                  |
| 15         |                                                                          | se introduce durata                                                                                                             |
|            | Ofertele cu durata de timp mai mică sau egală cu 15 zile au fost șterse. | se sterge pachetul pentru madagascar ce are 10 zile                                                                             |
|            | Meniu Stergere \*                                                        | se afiseaza meniu stergere                                                                                                      |
| 3          |                                                                          | se selecteaza stergerea peste buget                                                                                             |
|            | Introduceți prețul maxim:                                                | se cere pretul maxim                                                                                                            |
| 420        |                                                                          | se introduce pretul maxim                                                                                                       |
|            | Ofertele cu prețul mai mare de 420.0 Euro au fost șterse.                | se sterge pachetul Serbia ce costa 69                                                                                           |

###### Cautare
- se introduc urmatoarele pachete
 1. Pachetul cu destinația Craiova are prețul 100 Euro și este disponibil între 2024-06-16 și 2024-06-20
2. Pachetul cu destinația Timisoara are prețul 87 Euro și este disponibil între 2024-07-02 și 2024-07-12
3. Pachetul cu destinația Cluj-Napoca are prețul 420 Euro și este disponibil între 2024-05-12 și 2024-08-12
4. Pachetul cu destinația Craiova are prețul 69 Euro și este disponibil între 2024-05-12 și 2024-09-12
5. Pachetul cu destinația Grecia, Athena are prețul 420 Euro și este disponibil între 2024-05-12 și 2024-08-12
6. Pachetul cu destinația Grecia, Athena are prețul 69 Euro și este disponibil între 2024-05-04 și 2024-08-12

| Utilizator | Program                                                                                                                                                          | Descriere                                                                                                       |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
|            | Meniu Principal*                                                                                                                                                 | se afiseaza meniul                                                                                              |
| 3          |                                                                                                                                                                  | se alege meniul de cautare                                                                                      |
|            | Meniu Cautare \*                                                                                                                                                 | se afiseaza meniul de cautare                                                                                   |
| 1          |                                                                                                                                                                  | se alege cautare pe interval                                                                                    |
|            | Cautare pachete in functie de un interval de timp dat<br>Introduceti data de inceput<br>Ziua: <br>                                                               | se confirma alegerea si se cere ziua de inceput                                                                 |
| 6          |                                                                                                                                                                  | se introduce ziua de inceput                                                                                    |
|            | Luna:                                                                                                                                                            | se cere luna  de inceput                                                                                        |
| 6          |                                                                                                                                                                  | se introduce luna de inceput                                                                                    |
|            | Anul:                                                                                                                                                            | se cere anul  de inceput                                                                                        |
| 2024       |                                                                                                                                                                  | se introduce anul de inceput                                                                                    |
|            | Introduceti data de sfarsit<br>Ziua:                                                                                                                             | <br>se cere ziua de sfarsit                                                                                     |
| 12         |                                                                                                                                                                  | se introduce ziua de sfarsit                                                                                    |
|            | Luna:                                                                                                                                                            | se cere luna de sfarsit                                                                                         |
| 7          |                                                                                                                                                                  | se introduce luna de sfarsit                                                                                    |
|            | Anul:                                                                                                                                                            | se cere anul  de sfarsit                                                                                        |
| 2024       |                                                                                                                                                                  | se introduce anul de sfarsit                                                                                    |
|            | Craiova (2024-06-16 - 2024-06-20): 100.0 Euro<br><br>Timisoara (2024-07-02 - 2024-07-12): 87.0 Euro                                                              | se afiseaza ofertele ce se incadreaza                                                                           |
|            | Meniu Cautare \*                                                                                                                                                 | se afiseaza meniul de cautare                                                                                   |
| 2          |                                                                                                                                                                  | se alege varianta de cautare pe destinatie si pret maxim                                                        |
|            | Cautare pachete in functie de destinatie si pret maxim<br>Introduceti pretul maxim:                                                                              | mesaj de confirmare a inceputului de cautare si se cere pretul maxim                                            |
| 100        |                                                                                                                                                                  | se introduce pretul maxim                                                                                       |
|            | Introduceți destinația:                                                                                                                                          | se cere destinatia                                                                                              |
| grecia     |                                                                                                                                                                  | se introduce destinatia (eronat)                                                                                |
|            | ai vrut sa spui Grecia, Athena<br>Da sau Nu?  =>                                                                                                                 | fuctia fuzzy detecteaza similaritatea cu varianta corecta si se intreaba daca intr-adevar este varianta corecta |
| Da         |                                                                                                                                                                  | se raspunde la intrebare                                                                                        |
|            | Grecia, Athena (2024-05-04 - 2024-08-12): 69.0 Euro                                                                                                              | se afiseaza ofertele ce se incadreaza in parametrii                                                             |
|            | Meniu Cautare \*                                                                                                                                                 | se afiseaza meniul de cautare                                                                                   |
| 3          |                                                                                                                                                                  | se selecteaza cautarea in functie de data de sfarsit                                                            |
|            | Cautare pachete in functie de data de sfarsit<br>Introduceti data de sfarsit<br>Ziua:                                                                            | <br>se cere ziua de sfarsit                                                                                     |
| 12         |                                                                                                                                                                  | se introduce ziua de sfarsit                                                                                    |
|            | Luna:                                                                                                                                                            | se cere luna de sfarsit                                                                                         |
| 8          |                                                                                                                                                                  | se introduce luna de sfarsit                                                                                    |
|            | Anul:                                                                                                                                                            | se cere anul  de sfarsit                                                                                        |
| 2024       |                                                                                                                                                                  | se introduce anul de sfarsit                                                                                    |
|            | Cluj-Napoca (2024-05-12 - 2024-08-12): 420.0 Euro<br>Grecia, Athena (2024-05-12 - 2024-08-12): 420.0 Euro<br>Grecia, Athena (2024-05-04 - 2024-08-12): 69.0 Euro | se afiseaza ofertele ce au data de final aceeasi cu cea introdusa                                               |
###### Rapoarte
| Utilizator     | Program                                                                                              | Descriere                                                        |
| -------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
|                | Meniu Principal*                                                                                     | se afiseaza meniul                                               |
| 4              |                                                                                                      | se selectiaza optiunea de rapoarte                               |
|                | Meniu Rapoarte \*                                                                                    | se afiseaza meniul de rapoarte                                   |
| 1              |                                                                                                      | se selecteaza afisarea numarului de oferte pentru o destinatie   |
|                | ==Afisare numar de oferte pentru o destinatie==<br>Introduceti o destinatie:                         | se cere destinatia                                               |
| Craiova        |                                                                                                      | se introduce destinatia                                          |
|                | Exista 2 oferte pentru destinatia Craiova.                                                           | se afiseaza rezultatul                                           |
|                | Meniu Rapoarte \*                                                                                    | se afiseaza meniul de rapoarte                                   |
| 2              |                                                                                                      | se selecteaza afisarea pachetelor disponibile intr-un interval   |
|                | ==Afisare pachete disponibile intr-un interval de timp==<br>Introduceti data de inceput<br>Ziua:<br> | se confirma alegerea si se cere ziua de inceput                  |
| 6              |                                                                                                      | se introduce ziua de inceput                                     |
|                | Luna:                                                                                                | se cere luna  de inceput                                         |
| 6              |                                                                                                      | se introduce luna de inceput                                     |
|                | Anul:                                                                                                | se cere anul  de inceput                                         |
| 2024           |                                                                                                      | se introduce anul de inceput                                     |
|                | Introduceti data de sfarsit<br>Ziua:                                                                 | <br>se cere ziua de sfarsit                                      |
| 12             |                                                                                                      | se introduce ziua de sfarsit                                     |
|                | Luna:                                                                                                | se cere luna de sfarsit                                          |
| 7              |                                                                                                      | se introduce luna de sfarsit                                     |
|                | Anul:                                                                                                | se cere anul  de sfarsit                                         |
| 2024           |                                                                                                      | se introduce anul de sfarsit                                     |
|                | Timisoara (2024-07-02 - 2024-07-12): 87.0 Euro <br><br>Craiova (2024-06-16 - 2024-06-20): 100.0 Euro | se afiseaza rezultate sortate dupa pret in mod crescator         |
|                | Meniu Rapoarte \*                                                                                    | se afieaza meniul de rapoarte                                    |
| 3              |                                                                                                      | se alege varianta de pret mediu pentru o destinatie              |
|                | Afisare pret mediu pentru o destinatie<br>Introduceti destinatia:                                    | se confirma alegerea si se cere destinatia                       |
| Grecia, Athena |                                                                                                      | se introduce destinatia                                          |
|                | Pretul mediu pentru destinatia Grecia, Athena este 244.50 Euro.                                      | se afiseaza media pretului pentru ofertele ce au acea destinatie |

###### Filtrare

| Utilizator     | Program                                                                                         | Descriere                                                              |
| -------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
|                | Meniu Principal*                                                                                | se afiseaza meniul                                                     |
| 5              |                                                                                                 | se alege meniul de filtrare                                            |
|                | Meniu Filtrare \*                                                                               | se afiseaza meniul de filtrare                                         |
| 1              |                                                                                                 | se alege eliminarea pachetelor in functie de destinatie si buget       |
|                | Cautare pachete in functie de destinatie si pret maxim<br>Introduceti pretul maxim:             | se afiseaza mesajul de confirmare a alegerii si se cere pretul maxim   |
| 100            |                                                                                                 | se introduce pretul maxim                                              |
|                | Introduceți destinația:                                                                         | se cere destinatia                                                     |
| Grecia, Athena |                                                                                                 | se introduce destinatia                                                |
|                | Grecia, Athena (2024-05-04 - 2024-08-12): 69.0 Euro                                             | se afiseaza rezultatul                                                 |
|                | Meniu Filtrare\*                                                                                | se afiseaza meniul de filtrare                                         |
| 2              |                                                                                                 | se alege eliminare ofertelor ce presupun zile dintr-o anumita luna     |
|                | Cautare pachete fara o anumita luna<br>Introduceti luna:                                        | se afiseaza mesajul de confirmare si se cere luna respectiva           |
| 5              |                                                                                                 | se introduce luna                                                      |
|                | Craiova (2024-06-16 - 2024-06-20): 100.0 Euro<br>Timisoara (2024-07-02 - 2024-07-12): 87.0 Euro | se afiseaza ofertele valabile ce nu presupun zile dintr-o anumita luna |






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
- [x] lista de taskuri
	- [x] adaugare
	- [x] Ștergere
	- [x] Căutare
	- [x] Rapoarte
	- [x] Filtrare
	- [x] Undo

###### Initializare
- [x] Creare modul principal ( main.py ) ce v-a rula procesul
- [x] Creare modul de interfata ce creaza instante de pachete
- [x] Creare modul ( offer.py ) ce contine sablon de pachet 
###### Adăugare
 - [x] Scris teste
 - [x] Validare date de intrare, semnalare erori ale utilizatorului
 - [x] Creare clasa interfata care creaza instante de pachete

###### Ștergere
- [x] Scris teste
- [x] sterge pachete pentru o destinatie
- [x] sterge pachete cu o durata mai scurta
- [x] sterge pachete cu pret mai mare decat o suma
###### Căutare
- [x] Scris teste
- [x] Tipărirea pachetelor într-un interval
- [x] Tipărirea pachetelor cu o destinație și preț sub o sumă
- [x] Tipărirea pachetelor cu o anumită dată de sfârșit 


###### Rapoarte
- [x] Scris teste
- [x] Tipărirea numărului de oferte pentru o destinație dată
- [x] Tipărirea tuturor pachetelor disponibile într-o anumită perioadă
- [x] Tipărirea mediei de preț pentru o destinație dată


###### Filtrare
- [x] Scris teste
- [x] Eliminare oferte cu preț mai mare citit și o destinație diferită de cea citită
- [x] Eliminarea ofertelor în care sejurul presupune zile dintr-o anumită lună


###### Undo
- [x] refacerea ultimei operatii