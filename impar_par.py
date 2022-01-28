from random import randint
while True:
    bot = randint(0,10)
    print('-'*23)
    tipo = input('Ímpar (i) ou par (p)? ')
    num = int(input('Número: '))
    nums = num+bot
    print(f'{num}+{bot} = {nums}')
    if tipo == 'p':
        if nums/2 == int(nums/2):
            print('Você ganhou!')
        else:
            print('Você perdeu')
    elif tipo == 'i':
        if nums/2 == int(nums/2):
            print('Você perdeu')
        else:
            print('Você ganhou!')