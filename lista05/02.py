voto = 7
cand1 = 0 
cand2 = 0
cand3 = 0
cand4 = 0
totn = 0
totb = 0
while voto != 0:


    voto = int(input('Escreva seu voto: '))

    if voto == 1:
        cand1 += 1
        print('Você votou no candidato 1')
    elif voto == 2:
        cand2 += 1
        print('Você votou no candidato 2')
    elif voto == 3:
        cand3 += 1
        print('Você votou no candidato 3')
    elif voto == 4:
        cand4 += 1 
        print('Você votou no candidato 4')
    elif voto == 5:
        totn += 1
        print('Você votou nulo')
    elif voto == 6:
        totb += 1
        print('Você votou em branco')

print('Conjunto de votos finalizado:')
print('Total de votos para candidato 1:',cand1)
print('Total de votos para candidato 2:',cand2)
print('Total de votos para candidato 3:',cand3)
print('Total de votos para candidato 4:',cand4)
print('Total de voto nulo:',totn )
print('Total de votos em branco:',totb )
