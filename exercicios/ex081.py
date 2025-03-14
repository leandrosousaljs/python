nums = []
while True:
  nums.append(int(input('Digite um valor: ')))
  r = input('Quer continuar? [S/N] ')[0]
  if r in 'Nn':
    break
nums.sort(reverse=True)
print(f'''Você digitou {len(nums)} elementos.
Os valores em ordem decrescente são {nums}
{'O valor 5 faz parte da lista!' if 5 in nums else 'O valor 5 não foi encontrado!'}''')
