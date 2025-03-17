from cores import cores
from time import sleep


def ajuda(com):
  titulo(f'Acessando o manual do comando \'{com}\'', 13)
  print(cores[16])
  help(com)
  print(cores[0])
  sleep(2)


def titulo(msg, cor=0):
  tam = len(msg) + 4
  print(cores[cor], end='')
  print('~'*tam)
  print(f'  {msg}')
  print('~'*tam)
  print(cores[0], end='')
  sleep(1)


comando = ''
while True:
  titulo('SISTEMA DE AJUDA PyHELP', 11)
  comando = input('Função ou Biblioteca: (Digite FIM para parar) ').strip()
  if comando.upper() == 'FIM':
    break
  else:
    ajuda(comando)
titulo('ATÉ LOGO', 10)
