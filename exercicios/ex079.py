nums = []
while True:
  n = int(input('Digite um valor: '))
  if n not in nums:
    nums.append(n)
    print('Valor adicionado com sucesso...')
  else:
    print('Valor duplicado não adicionado...')
  r = input('Quer continuar? [S/N] ').strip().upper()[0]
  if r == 'N':
    break
print(f'Você digitou os valores {sorted(nums)}')
