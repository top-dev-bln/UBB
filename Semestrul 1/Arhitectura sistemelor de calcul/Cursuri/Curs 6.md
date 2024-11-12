

##### Operatii cu pointer
- Adunarea a 2 pointeri  ==OPERATIE INTERZISA IN INFORMATICA==
- Adunarea a unei constante la un pointer (ex: localizarea unui element in memorie de la un loc stabilit)
- Scaderea a doi pointer ( ex: determinarea lungimii unui sir)
- Scadarea unei constante la un pointer  (ex: localizarea unui element in memorie de la un loc stabilit)


\<expresie calcul de adresa> := \<val, expr aritmetica>
mov \[EBX +EDX\*4 +v-7], a+2

###### C++ Reference variable ( & )
1. int & j = i; //j devine **ALIAS** pt i
2. transmitere prin referinta // float f (int &x, y)
3. returnarea de L-valori print intermediul functiilor 
```cpp
int f(x,i){
....
return v[i]
}

q=f(a,79)
q=v[79]

int F(x,i){
....
return &v[i]
}

F(a,79) = 13193 // v[79] = 14193



```
