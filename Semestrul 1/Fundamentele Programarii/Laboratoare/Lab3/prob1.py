def test():
    # Tests for oricare_doua_consecutive_difera_prin_nr_prim
    assert construire(oricare_doua_consecutive_difera_prin_nr_prim, [1, 2, 3, 6, 13, 4, 21, 17, 4, 2, 69, 67, 86, 2, 9, 11]) == [17, 4, 2, 69, 67, 86]
    assert construire(oricare_doua_consecutive_difera_prin_nr_prim, [5, 11, 15, 16]) == []  # fara diferente prime
    assert construire(oricare_doua_consecutive_difera_prin_nr_prim, []) == []  # lista goala
    assert construire(oricare_doua_consecutive_difera_prin_nr_prim, [7]) == []  # un singur element
    assert construire(oricare_doua_consecutive_difera_prin_nr_prim, [2, 5, 8, 13, 18, 23, 28]) == [2, 5, 8, 13, 18, 23, 28]  # Toata lista are proprietatea
    assert construire(oricare_doua_consecutive_difera_prin_nr_prim, [10, 12, 15, 20, 25, 30]) == [10, 12, 15, 20, 25, 30]  
    assert construire(oricare_doua_consecutive_difera_prin_nr_prim, [3, 5, 8, 10, 13, 17, 22, 27, 34]) == [3, 5, 8, 10, 13]
    
    # Tests for oricare_doua_consecutive_difera_prin_semn
    assert construire(oricare_doua_consecutive_difera_prin_semn, [1, 2, -3, 6, -2, 15, -17, 3, 5, -8]) == [2, -3, 6, -2, 15, -17, 3]
    assert construire(oricare_doua_consecutive_difera_prin_semn, []) == []  # lista goala
    assert construire(oricare_doua_consecutive_difera_prin_semn, [5]) == []  # un singur element
    assert construire(oricare_doua_consecutive_difera_prin_semn, [1, 2, 3, 4, 5]) == []  # Toate pozitive
    assert construire(oricare_doua_consecutive_difera_prin_semn, [-1, -2, -3, -4]) == []  # Toate negative
    assert construire(oricare_doua_consecutive_difera_prin_semn, [1, -1, 1, -1, 1, -1]) == [1, -1, 1, -1, 1, -1]  # Toata lista are proprietatea
    assert construire(oricare_doua_consecutive_difera_prin_semn, [0, -1, 1, 0, -2, 2]) == [-1, 1]  # Include 0
    assert construire(oricare_doua_consecutive_difera_prin_semn, [10, -10, 20, -20, 30, -30, 40]) == [10, -10, 20, -20, 30, -30, 40]
 
    print("All tests passed successfully!")



def construire(functie,lista):

    if len(lista) < 2: 
        return []

    secventa = []
    temp=[]
    max=0
    for i in range(0,len(lista)-1):
        if (functie(lista[i],lista[i+1])==True):
            if temp==[]:
                temp.append(lista[i])
            temp.append(lista[i+1])
        else:
            if temp!=[]:
                if len(temp)>max:
                    max=len(temp)
                    secventa = temp.copy()
                temp=[]

    if temp and len(temp) > max:
      secventa = temp.copy()

    return secventa

def oricare_doua_consecutive_difera_prin_nr_prim(a,b):
    return (prim(abs(abs(a)-abs(b))))

def oricare_doua_consecutive_difera_prin_semn(a,b):
    if a==0 or b==0:
        return False
    return (a*b<0)


    
def meniu():
    print("-------------------------------------------------------------------")
    print("1. Citire Lista")
    print("---------Secventa de lungime maxima cu proprietatea----------------")
    print("2. oricare doua elemente consecutive difera printr-un numar prim")
    print("3. are oricare doua elemente consecutive sunt de semne contrare")
    print("-------------------------------------------------------------------")
    print("4. Iesire")
    while True:
        try:
            optiune = int(input("Alegeti o optiune: "))
            if optiune > 0 and optiune < 5:
                return optiune
            else:
                print("Optiune invalida!")
        except ValueError:
            print("Optiune invalida!")


def prim(n):
    if(n<2):
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    d=3
    while(d*d<=n):
        if n%d==0:
            return False
        d=d+2
    return True


def citire():
    print("introdu o lista de numere separate prin spatiu")
    lista=[]
    x=input()
    x=x.split()
    x=[int(i) for i in x]
    lista = x
    return lista




test()

while True:
    option = meniu()
    if(option==1):
        lista=citire()
    if(option==2):
        print(construire(oricare_doua_consecutive_difera_prin_nr_prim,lista))
    if(option==3):
        print(construire(oricare_doua_consecutive_difera_prin_semn,lista))
    if(option==4):
        break

