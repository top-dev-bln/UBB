import sys

current_limit = sys.getrecursionlimit()
sys.setrecursionlimit(30000)
new_limit = sys.getrecursionlimit()


def pi_blana(iter=1, stop=29900):
    if iter==stop:
        return 1
    return 6+((2*iter+1)*(2*iter+1))/pi_blana(iter+1,stop)
    
pi = 3+1/pi_blana()
print(pi)

