nums = []
pares = []
impares = []
while True:
  n = int(input('Digite um número: '))
  nums.append(n)
  if n % 2 == 0:
    pares.append(n)
  else:
    impares.append(n)
  r = input('Quer continuar? [S/N] ')[0]
  if r in 'Nn':
    break
pares.sort()
impares.sort()
print(f'''A lista completa é {nums}
A lista de pares é {pares}
A lista de impares é {impares}''')
