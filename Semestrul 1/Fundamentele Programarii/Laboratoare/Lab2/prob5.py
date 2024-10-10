
def prim(n):
    if n < 2:
        return False

    if n == 2:
        return True
    
    if n % 2 == 0 and n != 2:
        return False
    
    d=3

    while d * d <= n and n % d != 0:
        d = d + 2

    
    if d * d > n:
        return True
    else:
        return False



print("introdu un numar pentru a cele doua numere prime gemene imediat superioare")

n = int(input("===> "))
while True:
    if prim(n) and prim(n+2):
        print(n, n+2)
        break
    else:
        n = n + 1

