from random import randint,choice
from time import sleep
mao = bot = carta = cont11 = money = aposta = 0
escolbot = [1,1]
print('Bem-vindo ao Blackjack!')
money = float(input('Qual é o seu patrimônio? '))
print('-'*32)
while True:
    while aposta == 0 and money > 0:
        aposta = float(input('Quanto quer apostar? '))
        if aposta > money:
            print('Caloteiro!')
            aposta = 0
    escol = str(input('Quer sacar uma carta (s/n)? '))
    if escol == 's':
        if cont11 == 1:
            carta = randint(1,10)
        else:
            carta = randint(1,11)
        if carta == 11:
            cont11 = 1
        mao += carta
        print(f'Você ganhou {carta} e agora tem {mao}')
        if mao > 21:
            money -= aposta
            print(f'Você perdeu. \nAgora você tem ${money}\n',('-'*32))
            mao = bot = carta = cont11 = aposta = 0
            escolbot = [1,1]
            continue
    if bot > 10:
        del escolbot[0]
        escolbot += [0]
    if (choice(escolbot) == 1 or mao > bot) and bot < 21:
        sleep(0.5)
        if cont11 == 1:
            carta = randint(1,10)
        else:
            carta = randint(1,11)
        if carta == 11:
            cont11 = 1
        bot += carta
        print(f'Oponente ganhou {carta} e agora tem {bot}')
        if bot > 21:
            money += aposta
            print(f'Você ganhou! \nAgora você tem ${money}\n',('-'*32))
            mao = bot = carta = cont11 = aposta = 0
            escolbot = [1,1]
    elif escol != 's':
        print(f'Você tem {mao} e oponente tem {bot}')
        if mao > bot:
            money += aposta
            print(f'Você ganhou! \nAgora você tem ${money}')
        elif bot > mao:
            money -= aposta
            print(f'Você perdeu. \nAgora você tem ${money}')
        else:
            print('Empate! Nínguem ganhou ou perdeu dinheiro.')
        print('-'*32)
        mao = bot = carta = cont11 = aposta = 0
        escolbot = [1,1]
