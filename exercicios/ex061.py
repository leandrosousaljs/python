print('Gerador de PA')
print('-=' * 10)
prim = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = prim
i = 1
while i <= 10:
  print(f'{termo} → ', end='')
  termo += razao
  i += 1
print('FIM')
