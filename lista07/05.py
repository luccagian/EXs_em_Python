n = int(input())

def prim(n):
    for i in range(2,n):
        if n % i == 0:
            a = False
        elif n % i != 0:
            a = True
        return a
    
primo = prim(n)

print(primo)