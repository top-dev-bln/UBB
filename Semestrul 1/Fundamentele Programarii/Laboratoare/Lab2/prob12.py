print("introdu numarul n pentru a determina elementul sirului")
n=int(input("n="))
n=n-1
i=0
nr=0

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
    

       




       


while(i<n):
    nr=nr+1
    if prim(nr):
        i=i+1
        if(i==n):
            print(nr,' ')
    else:
        d = 2
        numar = nr
        while(d<=numar):
            if(numar%d==0):
                
                i=i+1
                if(i==n):
                    print(d,' ')
                    break
                while(numar%d==0):
                    numar=numar//d
            d=d+1