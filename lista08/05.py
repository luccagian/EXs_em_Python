dados_alunos = {}

for i in range(5):
    ra = input('ra do aluno: ')
    n1 = float(input(f'nota 1 do aluno: '))
    n2 = float(input(f'nota 2 do aluno: '))
    n3 = float(input(f'nota 3 do aluno: '))
    dados_alunos[ra] = n1, n2, n3

for chv in dados_alunos:
    media = sum(dados_alunos[chv]) / 3
    print(f'{chv}: {media:.2f}')