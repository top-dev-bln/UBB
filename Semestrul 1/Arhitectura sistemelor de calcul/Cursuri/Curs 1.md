- **Bitul** este unitatea primara de *reprezentare* a informatiei
- **Octetul** este unitatea primara de *acces* la informatie
***

![[Schema.jpg]]
Partea din stanga a desenului => Sunt registrii generali ai microprocesorului (EAX,  EBX, ECX, EDX, Etc...)


> [!NOTE] Definitie
> Registrii reprezinta capacitati de memorare foarte mici ( 8-16-32-64 bits) si foarte rapide ( ca viteza de acces) utilizate pentru stocarea temporara a unor operanzi. 
> 

Operanzii pot fi :
- date
- coduri de comenzi
- adrese
==Toate sunt **NUMERE**.==

Canalele de transmisie MAGISTRALE (BUS)
- A-BUS
- C-BUS
- D-BUS
Calculator / procesor pe N biti
- viziune software -> N biti = dimensiunea registrilor
- viziunea hardware -> N biti = dimensiunea magistralelor



Explicati de ce numerotarea bitilor in structurile de date manipulabile in calculator incepe de la 0 si nu de la 1 si de ce aceasta numerotare se face de la dreapta la stanga , iar nu de la stanga la dreapta.

În sistemele informatice,r, primul bit reprezintă 2^0, al doilea 2^1, și așa mai departe, ceea ce face numerotarea de la 0 mai naturală.
În reprezentarea binară, biții de la dreapta au valori mai mici (2^0, 2^1, etc.), iar cei din stânga au valori mai mari (2^n). Citirea de la dreapta la stânga permite calcularea valorii totale în timp ce parcurgi biții în ordinea puterilor lui 2.