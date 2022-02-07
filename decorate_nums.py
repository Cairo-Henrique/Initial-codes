from random import randint
from time import sleep
from os import system
cont = 0
while True:
    system('clear')
    num = randint(1000,10000)
    print(num)
    sleep(0.4)
    system('clear')
    if input('Qual era o número? ') == str(num):
        print('Acertou!')
        cont += 1
        if cont > 1:
            print(f'{cont} acertos seguidos!')
        sleep(0.5)
    else:
        print(f'Errou. Era {num}')
        cont = 0
        input('Aperte para continuar ')