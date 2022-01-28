from random import randint
cont0 = 0
cont1 = 0
n01 = 0
n = int(input('0 ou 1? '))
players = int(input('Quantos jogadores? ')) - 1
for i in range(players):
    n01 = randint(0,1)
    print(n01)
    if n01 == 0:
        cont0 += 1
    else:
        cont1 += 1
if n == 0:
    cont0 += 1
else:
    cont1 += 1
print(f'Você: {n} \nHouve {cont0} 0s e {cont1} 1s')