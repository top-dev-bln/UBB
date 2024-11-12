Documentația trebuie să conțină: 
- [x] enunțul
- [x] lista de funcționalități
- [x] planul de iterații
- [ ] scenarii de rulare
# P2. Gestiune laboratoare studenți
##### Enunt
Scrieți o aplicație pentru gestiunea notelor și a problemelor de laborator pentru o disciplină. 

Aplicația gestionează: 
- studenți
- problemă laborator

Creați o aplicație care permite: 
- gestiunea listei de studenți și probleme de laborator.
- adaugă, șterge, modifică, lista de studenți, listă de probleme
- căutare student, căutare problemă
- Asignare laborator/Notare laborator 
- Creare statistici: 
	- lista de studenți și notele lor la o problema de laborator dat, ordonat: alfabetic după nume, după notă. 
	- Toți studenții cu media notelor de laborator mai mic decât 5. (nume student și notă)


##### Lista Functionalitati

| Functionalitate                                  | Descriere                                                                                                                             |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| F1  Adăugare Student                             | Adaugarea student in lista de studenti                                                                                                |
| F2  Ștergere Student                             | Ștergerea student din lista de studenti                                                                                               |
| F3  Adăugare Problema                            | Adaugarea problema in lista de probleme de laborator                                                                                  |
| F4  Ștergere Problema                            | Ștergerea problema din lista de probleme de laborator                                                                                 |
| F5 Modificare Student                            | Modificarea detaliilor unui student ( nume sau grupa)                                                                                 |
| F6 Modificare Problema                           | Modificarea detaliilor unei probleme de laborator ( numar laborator _ numar problema, descriere, deadline )                           |
| F7  Căutare Student                              | Tipărirea detaliilor unui student dupa id sau dupa nume                                                                               |
| F8  Căutare Problema                             | Tipărirea detaliilor unei probleme dupa id                                                                                            |
| F9 Asignare laborator unui student               | Unui student i se atribuie un laborator                                                                                               |
| F10 Notarea                                      | Unei rezolvari i se da o nota                                                                                                         |
| F11 Statistici laborator -lista studenti cu nota | Afisare studenti carora le-a fost atribuita o anumita problema si notele corespunzatoarea acestora in ordine alfabetica sau dupa nota |
| F12 Statistica laborator - lista studenti picati | Afisare studenti carora le-a fost atribuita o anumita problema si notele sunt sub valoare 5                                           |


##### Plan de iteratii

| Iteratie                 | descriere                                                                                                                                                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Iteratia 1 <br>( Lab 7 ) | - **Gestionare liste de studenti si probleme**<br>     - operatii de baza pentru listele de studenti si de probleme<br>     - adaugare<br>     - stergere<br>     - modificare<br>- **Meniu POV**<br><br>                |
| Iteratia 2 <br>( Lab 8 ) | - **Cautare**<br>	- Afisare detalii student dupa nume <br>    - Afisare detalii problema dupa id<br><br>- **Asignare** <br>	- Trimitere rezolvari pentru probleme<br>- **Notare** <br>	- Trimitere note pentru rezolvari |
| Iteratia 3<br> ( Lab 9 ) | - **Statistici** <br>	- Afisare studenti si notele la un lab dat (ordonat)<br>    - Afisare stundeti picati<br>                                                                                                          |



##### Scenarii de rulare

| F1  Adăugare Student                             |
| ------------------------------------------------ |
| F2  Ștergere Student                             |
| F3  Adăugare Problema                            |
| F4  Ștergere Problema                            |
| F5 Modificare Student                            |
| F6 Modificare Problema                           |
| F7  Căutare Student                              |
| F8  Căutare Problema                             |
| F9 Asignare laborator unui student               |
| F10 Notarea                                      |
| F11 Statistici laborator -lista studenti cu nota |
| F12 Statistica laborator - lista studenti picati |
