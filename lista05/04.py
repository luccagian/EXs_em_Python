"""
Foi realizada uma pesquisa de algumas características físicas da população de uma
certa região, a qual coletou os seguintes dados referentes a cada habitante para serem
analisados:
- sexo (masculino e feminino)
- cor dos olhos (azuis, verdes ou castanhos)
- cor dos cabelos ( louros, castanhos, pretos)
- idade
Faça um algoritmo que determine e escreva:
- a maior idade dos habitantes
- a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos inclusive e
que tenham olhos verdes e cabelos louros.
O final do conjunto de habitantes é reconhecido pelo valor -1 entrada como idade
"""

ag = int(input('Idade: '))
agma = 0
qnt = 0

while ag > 0:
    sex = input('Sexo M/F:' )
    cor_o = input('Cor dos olhos (azuis; verdes; castanhos): ')
    cor_c = input('Cor do cabelo (louros; castanhos; pretos): ')

    if ag > agma:
        agma = ag

    if sex == 'F' and ag >= 18 and ag <= 35 and cor_o == 'verdes' and cor_c == 'louros':
        qnt += 1

    ag = int(input('Idade: '))

print('A maior idade dos habitantes:',agma)
print('A quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos inclusive e que tenham olhos verdes e cabelos louros:',qnt)
