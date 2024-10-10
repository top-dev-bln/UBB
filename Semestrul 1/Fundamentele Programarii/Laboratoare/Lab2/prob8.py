print("introdu un numar pentru a afisa numarul cel mai mare format din cifrele sale")

n = int(input("===> "))

cifre = []
while n > 0:
    cifre.append(n%10)
    n=n//10

numar_max = 0

cifre.sort()

i=len(cifre)-1
while i>=0:
    numar_max = numar_max*10 + cifre[i]
    i = i - 1
    
    
print(numar_max)