
def test():
    assert construire(oricare_doua_consecutive_difera_prin_nr_prim,[1,2,3,6,13,4,21,17,4,2,69,67,86,2,9,11]) == [17,4,2,69,67,86]
    assert construire(oricare_doua_consecutive_difera_prin_semn,[1,2,-3,6,-2,15,-17,3,5,-8]) == [2,-3,6,-2,15,-17,3]
    



def construire(functie,lista):
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
                    secventa=temp
                temp=[]

    return secventa

def oricare_doua_consecutive_difera_prin_nr_prim(a,b):
    return (prim(abs(abs(a)-abs(b))))

def oricare_doua_consecutive_difera_prin_semn(a,b):
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
    while(d*d<n):
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

