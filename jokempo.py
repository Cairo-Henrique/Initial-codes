from random import choice
from time import sleep
op = ['pedra','papel','tesoura']
while True:
    you = str(input('-----------------\nmão: '))
    print('pedra')
    sleep(0.4)
    print('papel')
    sleep(0.4)
    print('tesoooooou...')
    sleep(0.8)
    print(f'RA\nvocê: {you}\noponente: {choice(op)}')
