from random import choice
from time import sleep
y0 = y1 = y2 = y3 = y4 = y5 = y6 = y7 = y8 = y9 = y10 = ''
cont = 0
while len(y5) < 93:
    l = []
    for i in range(10):
        l += [choice([0,1])]
    x = l.count(1)
    if x == 1:
        y1 += '.'
    if x == 2:
        y2 += '.'
    if x == 3:
        y3 += '.'
    if x == 4:
        y4 += '.'
    if x == 5:
        y5 += '.'
    if x == 6:
        y6 += '.'
    if x == 7:
        y7 += '.'
    if x == 8:
        y8 += '.'
    if x == 9:
        y9 += '.'
    if x == 10:
        y10 += '.'
    cont += 1
    print(f'0{y0}\n1{y1}\n2{y2}\n3{y3}\n4{y4}\n5{y5}\n6{y6}\n7{y7}\n8{y8}\n9{y9}\nX{y10}\n')
    #sleep(0.05)
print(f'{cont} pontinhos no total')
#X is 10 in roman
