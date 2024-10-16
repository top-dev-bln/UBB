

> [!NOTE] Ce inseamna calculator pe n bits ?
> Intrebarea poate fii vazuta din doua perspective
> - din perspectiva inginereasca reprezinta dimensiunea magistralelor de adrese ( b-bus , c-bus , d-bus)
> - din perspectiva software reprezinta capacitatea registrelor de pe procesor

- Byte-ul este cea mai mica cantitate ADRESABILA din memorie

- Dispozitivul ALU mai are si task-ul de a seta in mod corespunzator flag-urile dupa executia unei instructiuni
***

- **CF** = Carry Flag
- **CF** are rol doar pentru adunare si scadere, nu este implicat de loc in operatia de impartire si este implicat doar partial in operatia de inmultire

***
- Calculatoarele lucreaza cu reprezentari in baza 2
- Noi lucram cu 2 interpretari valide in baza 10

***
##### Exista doua tipuri de flag-uri
###### flaguri care sunt setate ca efect al UOE
- ==CF==
- PF
- AF
- ZF
- SF
- OF
###### flaguri care sunt setate de **NOI**
- ==CF== 
	- CLC = 0
	- STC = 1
	- CMC = complement
- DF
	- CLD = 0
	- STD = 1
- IF
	- CLI = 0
	- STI = 1
- TF

Nu exista metoda de access la TF in mod direct
***
##### Legenda:
UOE - Ultima operatie efectuata

