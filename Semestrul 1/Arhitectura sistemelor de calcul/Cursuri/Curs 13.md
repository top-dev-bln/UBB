
Resurse volatile, EAX ,ECX ,EDX, eFLAGS

COD apel:

a) slavare res volatile
b)transpmitere parametro
c) efectuando los apelando con salvando de la adresa revenindos

cod intrare
a)configurare cadru stiva ( push EBP, mov EBP, ESP)
b)rezervando spatiu eventuale var locale
c)salvare resurse nevolatile ( daca e )


cod iesire
a) restaurare resurse nevolatile (daca e)
b) eliberare variabile locale (daca e)
c) dezafectarea cadru stiva


| Apelant | Apelat | Cod apel                     | Cod intrare                                                       | cod iesire          |
| ------- | ------ | ---------------------------- | ----------------------------------------------------------------- | ------------------- |
| C       | C      | compilator                   | compilator                                                        | compilator          |
| C       | ASM    | compilator                   | programator                                                       | programator         |
| ASM     | C      | programator                  | compilator                                                        | compilator          |
| ASM     | ASM    | call ( cu salvare revenire ) | nimic obligatoriu, <br>totul ramane la<br>latitudinea programator | ret (recuperareadr) |
|         |        |                              |                                                                   |                     |



