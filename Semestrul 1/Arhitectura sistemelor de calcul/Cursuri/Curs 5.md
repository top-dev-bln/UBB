###### Registri segment introduse original in programarea pe 16 biti
CS - Code Segment
DS - Data Segment
SS - Stack Segment
ES - Extra Segment
###### Registri segment extra adaptati pentru programarea pe 32 biti
FS - 
GS - 
EIP - extended instruction pointer



 **Termenul de segment are doua acceptiuni in familia 8086**
 - Segment fizic , numarul de biti in memoria fizica :
	 - 64Kb pentru procesoarele pe 16 biti
	 - 4 Gigabytes pentru procesoarele pe 32 biti
 - Segment logic, ocupat de codul sau data programului



> [!Warning] 
> Programatorii nu lucreaza niciodata cu adrese fizice efective, ei lucreaza doar cu asa-numitele **specificari de adresa**

| Adr.Segement | Offset  |
| ------------ | ------- |
| 16 biti      | 32 biti |


###### Tabela de index selectori

| index | Selector ( Base ) | Sizeof |
| ----- | ----------------- | ------ |
| 17    | 101382            | ----   |
| 32    | --------          | ----   |
| 1614  | --------          | ----   |
| 2377  | --------          | ----   |
- In coloana de selectori se afla **adresa fizica** 


**Segment logic**
- Inceput (Adr. Baza)
- sizeof (dimensiune)
- Tip( cod, date, stiva, extra)

In totdeauna  combinatia de registrii CS:EIP reprezinta adresa instructiunii curent de executare

###### 3 moduri de specificare a unui operand EXPLICIT
i) modul registru - mov **EAX**, 17
ii) modul imediat - mov EAX, **17**
iii modul <u> adresare la memorie</u>


### Formula de la 2 dimineata


> [!Warning]  Formula de calcul al offset-ului
> Offset = \[Baza] +\[Index \* Scala ] + \[constanta]
- parantezele drepte reprezinta optionalitatea , pot lipsi 1 sau 2 , nu toate 3
- baza -> adresa indirecta
- index -> adresare indexata
- Scala = (1, 2 ,4, 8 pentru byte, word , double , respectiv quad)
- constanta -> adresare directa
- ESP - nu poate registru de index

mov EAX, \[v1]
\[ ] - operatorul de dereferentiere
v1- adresa


Variabila este o zona de memorie etichetata a carui continut este variabil