nums = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os valores: {nums}')
print(f'O valor 9 apareceu {nums.count(9)} vezes.')
if 3 in nums:
  print(f'O valor 3 apareceu na {nums.index(3)+1}ª posição.')
else:
  print('O valor 3 não foi digitado.')
print(f'Os valores pares digitados foram: ', end='')
for n in nums:
  if n % 2 == 0:
    print(n, end=' ')
