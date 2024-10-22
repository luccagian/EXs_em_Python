n = int(input())
a = 0

for i in range(2,n):
    if n % i == 0:
        print('não é primo')
        a += 1 
        break
if a == 0:
    print('é primo')