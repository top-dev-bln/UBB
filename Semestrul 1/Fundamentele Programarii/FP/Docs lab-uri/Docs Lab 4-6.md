Documentația trebuie să conțină: 
- [x] enunțul
- [x] lista de funcționalități
- [x] planul de iterații
- [ ] scenarii de rulare
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

| Utilizator | Program | Descriere |
| ---------- | ------- | --------- |
|            |         |           |

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
- [ ] scenarii de rulare
- [ ] lista de taskuri

###### Initializare
- [ ] Creare modul principal ( main.py ) ce v-a rula procesul
- [ ] Creare modul de interfata ce creaza instante de pachete
- [ ] Testare modul de interfata
- [ ] Creare modul ( offer.py ) ce contine sablon de pachet 
- [ ] Testare modul de sablon
###### Adăugare
 - [ ] Validare date de intrare, semnalare erori ale utilizatorului
 - [ ] Creare clasa interfata care creaza instante de pachete
 - [ ] Testare interfata
 
 
