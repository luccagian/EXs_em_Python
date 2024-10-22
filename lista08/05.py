"""
Preencha um dicionário com os dados de 5 alunos
- Utilize o RA do aluno como chave e uma lista de três notas como valor.
- Solicite os dados do usuário
- Percorra o dicionário e exiba a média de cada aluno.
Exemplo:
Veja um exemplo da estrutura do dicionário.
{19230490: [10, 8.0, 7.5], 2002441: [6, 5, 7.5], 2001332: [5,8,9.5]}
"""

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
