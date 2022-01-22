from math import cos, radians
alfa = input('informe o angulo oposto ao lado desconhecido (ou x): ')
a = input('lado a = ')
b = input('lado b = ')
c = input('lado c = ')
if a == 'x':
    b = float(b)
    c = float(c)
    alfa = float(alfa)
    a = (b**2 + c**2 - (2 * b * c * (cos(radians(alfa)))))**0.5
    print('a =',a,'\na = √',a**2)
elif b == 'x':
    a = float(a)
    c = float(c)
    if alfa == 'x':
        b = (a**2 - c**2)**0.5
        print('b =',b,'\nb = √',b**2)
    else:
        alfa = float(alfa)
        b = (a**2 + c**2 - (2 * a * c * (cos(radians(alfa)))))**0.5
        print('b =',b,'\nb = √',b**2)
elif c == 'x':
    a = float(a)
    b = float(b)
    if alfa == 'x':
        c = (a**2 - b**2)**0.5
        print('c =',c,'\nc = √',c**2)
    else:
        alfa = float(alfa)
        c = (a**2 + b**2 - (2 * a * b * (cos(radians(alfa)))))**0.5
        print('c =',c,'\nc = √',c**2)