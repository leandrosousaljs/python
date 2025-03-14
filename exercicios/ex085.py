num = [[], []]
valor = 0
for i in range(1, 8):
  valor = int(input(f'Digite o {i}° valor: '))
  if valor % 2 == 0:
    num[0].append(valor)
  else:
    num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'''Os valores pares digitados foram: {num[0]}
Os valores impares digitados foram: {num[1]}''')
