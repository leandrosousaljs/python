f = str(input('Digite uma frase: ').strip().upper())
p = f.split()
j = ''.join(p)
r = j[::-1]
print(f'O inverso de {j} é {r}.')
if r == j:
  print('Temos um palíndromo!')
else:
  print('A frase digitada não é um palíndromo.')
