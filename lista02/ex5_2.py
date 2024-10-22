idade = int(input('digite sua idade: '))
temp = int(input('digite os seus anos trabalhados: '))

if idade >= 65 or temp >= 30 or (idade >= 60 and temp >= 25):
    print('pode se aposentar')
else:
    print('não pode se aposentar')
    
