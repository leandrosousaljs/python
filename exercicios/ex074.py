from random import randint
nums = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in nums:
  print(n, end=' ')
print(f'\nO maior valor sorteado foi {max(nums)}')
print(f'O menor valor sorteado foi {min(nums)}')
