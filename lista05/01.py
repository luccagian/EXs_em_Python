neg = 0
numbma = 0
for n in range(10):
    numb = int(input(''))

    if numb < 0:
        neg += 1

    if numb > numbma:
        numbma = numb

print(numbma)
print(neg)
