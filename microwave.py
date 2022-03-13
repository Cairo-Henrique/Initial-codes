from os import system
from time import sleep
system('clear')
pos1 = input()
system('clear')
pos2 = input(f'{pos1}:')
system('clear')
pos3 = input(f'{pos1}:{pos2}')
stringtime = f'{pos1}:{pos2}{pos3}'
t = int(pos1+pos2+pos3)
t += int(stringtime[0])*(-40)
#t - stringtime[0]*100 + stringtime[0]*60
pos1,pos2,pos3 = int(pos1),int(pos2),int(pos3)
for i in range(t):
    system('clear')
    pos3 -= 1
    if pos3 < 0:
        pos2 -= 1
        pos3 = 9
    if pos2 < 0:
        pos1 -= 1
        pos2 = 5
    stringtime = f'{pos1}:{pos2}{pos3}'
    print(stringtime)
    sleep(1)
    system('clear')
print('bipe')