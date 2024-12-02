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


### Lista Funcționalități

| Funcționalitate               | Descriere                                                              |
| ----------------------------- | ---------------------------------------------------------------------- |
| F1 Adăugare Student           | Adăugarea unui student în lista de studenți.                           |
| F2 Afișare Studenți           | Afișarea listei complete de studenți.                                  |
| F3 Adăugare Laborator         | Adăugarea unui laborator în lista de laboratoare.                      |
| F4 Afișare Laboratoare        | Afișarea listei complete de laboratoare.                               |
| F5 Afișare Detalii Student    | Afișarea detaliilor unui student (după nume sau ID).                   |
| F6 Afișare Detalii Laborator  | Afișarea detaliilor unui laborator (după număr laborator și problemă). |
| F7 Asignare Laborator Student | Asignarea unui laborator unui student.                                 |
| F8 Notare Laborator           | Atribuirea unei note unei rezolvări.                                   |
| F9 Afișare Soluții            | Vizualizarea soluțiilor trimise.                                       |
| F10 Trimitere Soluție         | Adăugarea unei soluții pentru un laborator.                            |
| F11 Ștergere Student          | Ștergerea unui student din lista de studenți.                          |
| F12 Ștergere Laborator        | Ștergerea unui laborator din lista de laboratoare.                     |
| F13 Modificare Student        | Modificarea detaliilor unui student (nume sau grupă).                  |
| F14 Modificare Laborator      | Modificarea detaliilor unui laborator (descriere, deadline).           |
| F15 Afișare Studenți cu Note  | Vizualizarea studenților și a notelor lor pentru un laborator dat.     |
| F16 Afișare Studenți Picați   | Vizualizarea studenților cu media notelor mai mică de 5.               |

##### Plan de iteratii

| Iteratie                 | descriere                                                                                                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Iteratia 1 <br>( Lab 7 ) | - **Gestionare liste de studenti si probleme**<br>     operatii de baza pentru listele de studenti si de probleme<br>     - adaugare<br>     - stergere<br>     - modificare<br><br> |
| Iteratia 2 <br>( Lab 8 ) | - **Cautare**<br>	- Afisare detalii student dupa nume <br>    - Afisare detalii problema dupa id<br><br>- **Asignare** <br>	- Trimitere rezolvari pentru probleme<br>                |
| Iteratia 3<br> ( Lab 9 ) | - **Notare** <br>	- Trimitere note pentru rezolvari<br><br>- **Statistici** <br>	- Afisare studenti si notele la un lab dat (ordonat)<br>    - Afisare stundeti picati<br>           |




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




#### **1. Adăugare Student**

|USER|CONSOLE|DESCRIERE|
|---|---|---|
||_MENIU CONSOLA_|Meniu principal|
|1||Se selectează opțiunea de adăugare|
||Introduceti datele studentului:  <br>ID:|Se cere ID-ul|
|1||Utilizatorul introduce ID-ul 1|
||Nume:|Se cere numele|
|Balan||Utilizatorul introduce numele Balan|
||Grup:|Se cere grupa|
|211||Utilizatorul introduce grupa 211|
||==Student adăugat cu succes!==|Confirmare|

---

#### **2. Afișare Studenți**

|USER|CONSOLE|DESCRIERE|
|---|---|---|
||_MENIU CONSOLA_|Meniu principal|
|2||Se selectează opțiunea de afișare|
||Studenții sunt:  <br>[1] Balan - 211|Lista studenților este afișată|

---

#### **3. Adăugare Laborator**

|USER|CONSOLE|DESCRIERE|
|---|---|---|
||_MENIU CONSOLA_|Meniu principal|
|3||Se selectează opțiunea de adăugare|
||Introduceti datele laboratorului:  <br>Număr laborator:|Se cere numărul laboratorului|
|1||Utilizatorul introduce numărul 1|
||Număr problemă:|Se cere numărul problemei|
|1||Utilizatorul introduce problema 1|
||Descriere:|Se cere o descriere|
|Tema: OOP||Utilizatorul introduce descrierea|
||Introduceti deadline-ul:  <br>Ziua:|Se cere ziua deadline-ului|
|15||Utilizatorul introduce ziua 15|
||Luna:|Se cere luna|
|12||Utilizatorul introduce luna 12|
||Anul:|Se cere anul|
|2024||Utilizatorul introduce anul 2024|
||==Laborator adăugat cu succes!==|Confirmare|

---

#### **4. Afișare Laboratoare**

|USER|CONSOLE|DESCRIERE|
|---|---|---|
||_MENIU CONSOLA_|Meniu principal|
|4||Se selectează opțiunea afișare|
||Laboratoarele sunt:  <br>[1] Laborator 1 - Problema 1: Tema: OOP. Deadline: 2024-12-15|Lista laboratoarelor este afișată|

---

#### **5. Afișare Detalii Student**

|USER|CONSOLE|DESCRIERE|
|---|---|---|
||_MENIU CONSOLA_|Meniu principal|
|5||Se selectează opțiunea de afișare detalii|
||Introduceți numele studentului:|Se cere numele|
|Balan||Utilizatorul introduce numele Balan|
||Detalii student:  <br>[1] Balan - 211|Detaliile studentului sunt afișate|

---

#### **6. Afișare Detalii Laborator**

|USER|CONSOLE|DESCRIERE|
|---|---|---|
||_MENIU CONSOLA_|Meniu principal|
|6||Se selectează opțiunea de afișare detalii|
||Introduceți număr laborator:|Se cere numărul laboratorului|
|1||Utilizatorul introduce numărul 1|
||Număr problemă:|Se cere numărul problemei|
|1||Utilizatorul introduce problema 1|
||Detalii laborator:  <br>[1] Tema: OOP. Deadline: 2024-12-15|Detaliile laboratorului sunt afișate|

---

#### **7. Asignare Laborator Student**

|USER|CONSOLE|DESCRIERE|
|---|---|---|
||_MENIU CONSOLA_|Meniu principal|
|7||Se selectează opțiunea de asignare|
||Introduceți ID student:|Se cere ID-ul studentului|
|1||Utilizatorul introduce ID-ul 1|
||Introduceți număr laborator:|Se cere numărul laboratorului|
|1||Utilizatorul introduce numărul 1|
||Număr problemă:|Se cere numărul problemei|
|1||Utilizatorul introduce problema 1|
||==Laborator asignat cu succes!==|Confirmare|

#### **8. Notare Laborator**

|USER|CONSOLE|DESCRIERE|
|---|---|---|
||_MENIU CONSOLA_|Meniu principal|
|8||Se selectează opțiunea de notare|
||Introduceți ID student:|Se cere ID-ul studentului|
|1||Utilizatorul introduce ID-ul 1|
||Introduceți număr laborator:|Se cere numărul laboratorului|
|1||Utilizatorul introduce numărul 1|
||Introduceți număr problemă:|Se cere numărul problemei|
|1||Utilizatorul introduce problema 1|
||Introduceți nota (0-10):|Se cere nota|
|8.5||Utilizatorul introduce nota 8.5|
||==Rezolvare notată cu succes!==|Confirmare|

**Cazuri suplimentare:**

1. **Notă nevalidă**:
    - Utilizatorul introduce o notă mai mică de 0 sau mai mare de 10.
    - **Mesaj afișat:** `Eroare: Nota trebuie să fie între 0 și 10!`

---

#### **9. Afișare Soluții**

|USER|CONSOLE|DESCRIERE|
|---|---|---|
||_MENIU CONSOLA_|Meniu principal|
|9||Se selectează opțiunea de afișare soluții|
||Introduceți număr laborator (0 pentru toate):|Se cere laboratorul|
|0||Utilizatorul introduce 0 pentru a vedea toate soluțiile|
||Soluții:  <br>- Student ID 1, Lab 1, Problem 1: "Rezolvare OOP"|Se afișează toate soluțiile|

**Cazuri suplimentare:**

1. **Nicio soluție disponibilă**:
    - Dacă nu există soluții, **mesaj afișat:** `Nu există soluții!`

---

#### **10. Trimitere Soluție**

|USER|CONSOLE|DESCRIERE|
|---|---|---|
||_MENIU CONSOLA_|Meniu principal|
|10||Se selectează opțiunea de trimitere soluție|
||Introduceți ID student:|Se cere ID-ul studentului|
|1||Utilizatorul introduce ID-ul 1|
||Introduceți număr laborator:|Se cere numărul laboratorului|
|1||Utilizatorul introduce numărul 1|
||Introduceți număr problemă:|Se cere numărul problemei|
|1||Utilizatorul introduce problema 1|
||Introduceți soluția:|Se cere soluția|
|"Rezolvare OOP"||Utilizatorul introduce soluția|
||==Soluție trimisă cu succes!==|Confirmare|

---

#### **11. Ștergere Student**

|USER|CONSOLE|DESCRIERE|
|---|---|---|
||_MENIU CONSOLA_|Meniu principal|
|11||Se selectează opțiunea de ștergere student|
||Introduceți ID student:|Se cere ID-ul studentului|
|1||Utilizatorul introduce ID-ul 1|
||==Student șters cu succes!==|Confirmare|

**Cazuri suplimentare:**

1. **Student inexistent**:
    - **Mesaj afișat:** `Eroare: Studentul cu ID-ul dat nu există!`

---

#### **12. Ștergere Laborator**

|USER|CONSOLE|DESCRIERE|
|---|---|---|
||_MENIU CONSOLA_|Meniu principal|
|12||Se selectează opțiunea de ștergere laborator|
||Introduceți număr laborator:|Se cere numărul laboratorului|
|1||Utilizatorul introduce numărul 1|
||Introduceți număr problemă:|Se cere numărul problemei|
|1||Utilizatorul introduce problema 1|
||==Laborator șters cu succes!==|Confirmare|

---

#### **13. Modificare Student**

|USER|CONSOLE|DESCRIERE|
|---|---|---|
||_MENIU CONSOLA_|Meniu principal|
|13||Se selectează opțiunea de modificare student|
||Introduceți ID student:|Se cere ID-ul studentului|
|1||Utilizatorul introduce ID-ul 1|
||Introduceți noul nume:|Se cere numele|
|Popescu||Utilizatorul introduce numele Popescu|
||Introduceți noua grupă:|Se cere grupa|
|212||Utilizatorul introduce grupa 212|
||==Student modificat cu succes!==|Confirmare|

---

#### **14. Modificare Laborator**

|USER|CONSOLE|DESCRIERE|
|---|---|---|
||_MENIU CONSOLA_|Meniu principal|
|14||Se selectează opțiunea de modificare laborator|
||Introduceți număr laborator:|Se cere numărul laboratorului|
|1||Utilizatorul introduce numărul 1|
||Introduceți număr problemă:|Se cere numărul problemei|
|1||Utilizatorul introduce problema 1|
||Introduceți noua descriere:|Se cere descrierea|
|"Tema actualizată"||Utilizatorul introduce descrierea|
||Introduceți noul deadline:  <br>Ziua:|Se cere ziua|
|20||Utilizatorul introduce ziua 20|
||Luna:|Se cere luna|
|12||Utilizatorul introduce luna 12|
||Anul:|Se cere anul|
|2024||Utilizatorul introduce anul 2024|
||==Laborator modificat cu succes!==|Confirmare|




#####  \*Meniu Consola
1. Adauga student 
2. Afiseaza studentii 
3. Adauga laborator 
4. Afiseaza laboratoare 
5. Afisare detalii student 
6. Afisare detalii laborator 
7. Asignare laborator student 
8. Notare laborator 
9. Afisare solutii
10. Trimite solutie 
11. Sterge student 
12. Sterge laborator 
13. Modifica student 
14. Modifica laborator 
15. Afisare studenti cu note 
16. Afisare studenti picati x. Iesire