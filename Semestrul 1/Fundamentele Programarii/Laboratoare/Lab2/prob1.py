##. Găsiți primul număr prim mai mare decât un număr dat.
print("scrie un numar natural n pentru care vrei sa afla primul numar prim mai mare ")
n = int(input("n = "))
n = n+1 #deoarece numarul prim trebuie sa fie strict mai mare decat n
def prim(n):
    if n < 2:
        return False

    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    d=3

    while d * d <= n and n % d != 0:
        d = d + 2

    if d * d > n:
        return True
    return False

        

while(True):
    if prim(n)==True:
        print(n)
        break
    else:
        n = n + 1