from os import system
from random import randint
from time import sleep
hpmaxbot = 300
hp = hp0 = 300
hpbot = hpbot0 = hpmaxbot
while True:
    print(f'Seu pkm tem {hp}hp \no pkm do adversário tem {hpbot}hp\n')
    hpbot0 = hpbot
    hp0 = hp
    choice = input('1 - 75 de dano garantido \n2 - 50 a 150 de dano \n3 - Capturar \n')
    if choice == '1':
        hpbot -= 75
        print('O adversário tomou 75 de dano')
    if choice == '2':
        hpbot -= randint(50,150)
        print(f'O adversário tomou {hpbot0-hpbot} de dano')
    if hpbot <= 0:
        print('Game over')
        break
    if choice == '3':
        for i in range(3):
            print('🌟')
            sleep(0.5)
        if (randint(1,100)) <= ((3*hpmaxbot-2*hpbot)*75/(3*hpmaxbot)):
            print('Capturado!')
            break
        else:
            print('Escapou!')
    hp -= randint(50,100)
    print(f'Você tomou {hp0-hp} de dano')
    if hp <= 0:
        print('Game over')
        break
    input('↓')
    system('clear')