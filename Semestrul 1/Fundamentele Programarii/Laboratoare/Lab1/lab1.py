#suma a n numere naturale

sum=0

n=int(input("cate numere doresti sa introduci  => "))

while n>0:
    x=int(input("numar => "))
    sum=sum+x
    n=n-1


print("suma este => ",sum)



#verificati daca un numar citit de la tastatura este prim

n = int(input("Introdu un numar pentru a verifica primalitatea => "))

for d in range(2, n):
    if n % d == 0:
        print(n, " nu este prim")
        break
else:
    print(n, " este prim")



#calculati cel mai mare divizor comun

print("introdu doua numere pentru cmmdc")
a=int(input("primul numar =>"))
b=int(input("al doilea numar =>"))

while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print("cmmdc = ",a)

