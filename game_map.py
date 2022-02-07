from os import system
from random import randint
from datetime import datetime
score = minu = seg = 0
l =['x'] + [''] * 35
l[randint(1,35)] = 'O'
print(l,'\n(wasd)')
while True:
    pos = l.index('x')
    time = datetime.now()
    minu0 = time.minute
    seg0 = time.second
    mov = input()
    system('clear')
    try:
        if 'w' in mov and pos >= 12:
            l[pos-12] = 'x'
            l[pos] = ''
            pos = l.index('x')
        if 'a' in mov and pos >= 1 and pos != 12 and pos != 24:
            l[pos-1] = 'x'
            l[pos] = ''
            pos = l.index('x')
        if 's' in mov:
            l[pos+12] = 'x'
            l[pos] = ''
            pos = l.index('x')
        if 'd' in mov and pos != 11 and pos != 23:
            l[pos+1] = 'x'
            l[pos] = ''
            pos = l.index('x')
    except:
        pass
    while not 'O' in l:
        l[randint(0,35)] = 'O'
        score += 1
        if l.index('O') == pos:
            l[l.index('O')] = 'x'
            score -= 1
    time = datetime.now()
    minu += time.minute-minu0
    seg += time.second-seg0
    if seg < 0:
        seg += 60
        minu -= 1
    if minu < 0:
        minu += 60
    while seg > 59:
        minu += 1
        seg -= 60
    print(f'score: {score} | {minu}:{seg} \n{l}')