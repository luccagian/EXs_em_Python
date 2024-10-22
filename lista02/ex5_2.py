"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se
aposentar. As condições para aposentadoria são:
- Ter pelo menos 65 anos,
- Ou ter trabalhado pelo menos 30 anos,
- Ou ter pelo menos 60 anos e ter trabalhado pelo menos 25 anos.
"""

idade = int(input('digite sua idade: '))
temp = int(input('digite os seus anos trabalhados: '))

if idade >= 65 or temp >= 30 or (idade >= 60 and temp >= 25):
    print('pode se aposentar')
else:
    print('não pode se aposentar')
    
