#20 cards are faced up or down randomly in a row,
#a move consists of turning a face down to face up and moving it to the right.
#Prove that this sequence of moves must terminate.
from random import randint
print('Face up = 1 \nFace down = 0\n')
l = []
cont = 0
for i in range(20):
    l += [randint(0,1)]
print(l)
try:
    while l.index(0) > -1:
        ind = randint(0,20)
        try:
            if l.index(0) == ind:
                l[ind] = 1
                l[ind], l[ind+1] = l[ind+1], l[ind]
                print(l)
                cont += 1
        except:
            pass
except:
    l[19] = 1
    print(f'\n{l}')
    print(f'Proved with {cont} moves.')