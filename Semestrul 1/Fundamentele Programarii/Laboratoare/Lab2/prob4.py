##ipoteza Goldbach : orice numar natural mai mare ca 2 este suma a doua numere prime


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
    else:
        return False



print("introdu un numar pentru a cele doua numere prime ce adunate dau numarul")

n = int(input("===> "))
for i in range(2, n):
    if prim(i) and prim(n - i):
        print(i, n - i)
        break
