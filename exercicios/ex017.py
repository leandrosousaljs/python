from math import hypot
a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
c = hypot(a, b)
print(f'A hipotenusa vai medir {(c):.2f}.')
