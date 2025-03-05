from time import sleep
from random import randint
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
i = ('Pedra', 'Papel', 'Tesoura')
c = randint(0,2)
j = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)
print(f'Computador jogou {i[c]}')
print(f'Jogador jogou {i[j]}')
print('-=' * 12)
if c == 0: #PEDRA
  if j == 0:
    print('EMPATE')
  elif j == 1:
    print('JOGADOR VENCE')
  elif j == 2:
    print('COMPUTADOR VENCE')
  else:
    print('JOGADA INVÁLIDA')
elif c == 1: #PAPEL
  if j == 0:
    print('COMPUTADOR VENCE')
  elif j == 1:
    print('EMPATE')
  elif j == 2:
    print('JOGADOR VENCE')
  else:
    print('JOGADA INVÁLIDA')
elif c == 2: #TESOURA
  if j == 0:
    print('JOGADOR VENCE')
  elif j == 1:
    print('COMPUTADOR VENCE')
  elif j == 2:
    print('EMPATE')
  else:
    print('JOGADA INVÁLIDA')
