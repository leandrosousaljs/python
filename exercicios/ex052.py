n = int(input('Digite um número: '))
t = 0
for i in range(1,n + 1):
  if n % i  == 0:
    print('\033[33m', end='')
    t += 1
  else:
    print('\033[31m', end='')
  print(f'{i} ', end='')
print(f'\n\033[mO número {n} foi divisível {t} vezes')
if t == 2:
  print(f'E por isso ele É PRIMO!')
else:
  print(f'E por isso ele NÃO É PRIMO!')
