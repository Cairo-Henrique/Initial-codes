from os import system
from math import atan,pi
a = float(input('Funcão do 1° ou 2° grau \na = '))
b = float(input('b = '))
c = float(input('c = '))
system('clear')
print(f'f(x) = {a}x² + {b}x + {c}')
if a == 0:
    print(f'Ângulo: {atan(b)*180/pi}°')
else:
    if b != 0:
        print(f'Xv = {-b/(2*a)}')
    else: 
        print(f'Xv = 0')
    print(f'Yv = {-(b**2 - 4*a*c)/(4*a)}')
def f(x):
    return a*x**2 + b*x + c
while True:
    print('-'*10)
    x = float(input('x = '))
    print(f'y = {f(x)}')