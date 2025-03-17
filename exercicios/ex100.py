from random import randint
from time import sleep


def sorteia(lst):
  print('Sorteando 5 valores da lista: ', end='')
  for c in range(0,5):
    n = randint(1,10)
    lst.append(n)
    print(f'{n} ', end='', flush=True)
    sleep(0.3)
  print('PRONTO!')

def somaPar():
  soma = 0
  for n in nums:
    if n % 2 == 0:
      soma += n
  print(f'Somando os valores pares de {nums}, temos {soma}')


nums = []
sorteia(nums)
somaPar()
