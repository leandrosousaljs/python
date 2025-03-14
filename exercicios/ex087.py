matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sPar = mai = sCol = 0
for l in range(0, 3):
  for c in range(0, 3):
    matriz[l][c] = int(input(f'Digite o valor para a posição [{l},{c}]: '))
for l in range(0, 3):
  sCol += matriz[l][2]
  for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
      mai = matriz[1][c]
    print(f'[{matriz[l][c]:^5}]', end='')
    if matriz[l][c] % 2 == 0:
      sPar += matriz[l][c]
  print()
print(f'''A soma dos valores pares é {sPar}.
A soma dos valores da terceira coluna é {sCol}.
O maior valor da segunda linha é {mai}.''')
