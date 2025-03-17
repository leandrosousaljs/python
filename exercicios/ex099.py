from time import sleep


def maior(*nums):
  print('-='*40)
  print('Analisando os valores passados...')
  if len(nums) == 0:
    print('Nenhum valor foi informado')
  else:
    for n in nums:
      print(f'{n} ', end='', flush=True)
      sleep(0.3)
    print(f'Foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor informado foi {max(nums)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
