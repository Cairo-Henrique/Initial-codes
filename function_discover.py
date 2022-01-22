print('Teorema da decomposição')
r1 = float(input('Informe a primeira raíz r1: '))
r2 = float(input('Informe a segunda raíz r2: '))
x = float(input('Informe a coordenada x do ponto C: '))
y = float(input('Informe a coordenada y do ponto C: '))
theorem = ((x-r1)*(x-r2))
a = y/theorem
fx1 = (f'({y}/{theorem})x² - ({y*(r2 + r1)}/{theorem})x + {y*r1*r2}/{theorem}')
fx2 = (f'{y/theorem}x² - {(y*(r2 + r1))/theorem}x + {y*r1*r2/theorem}')
print(f'a = {y}/{theorem} = {a}\nf(x) = {fx1}\nf(x) = {fx2}')
#by Cairo Henrique Vaz Cotrim
