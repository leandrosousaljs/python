from utils.cores import Cores
from time import sleep


def ajuda(com):
  titulo(f'Acessando o manual do comando \'{com}\'', 'fAzul')
  print(Cores.fBranco)
  help(com)
  print(Cores.reset)
  sleep(2)


def titulo(msg, cor=''):
  tam = len(msg) + 4
  corS = getattr(Cores, cor, Cores.reset)
  print(corS, end='')
  print('~'*tam)
  print(f'  {msg}')
  print('~'*tam)
  print(Cores.reset, end='')
  sleep(1)


comando = ''
while True:
  titulo('SISTEMA DE AJUDA PyHELP', 'fVerde')
  comando = input('Função ou Biblioteca: (Digite FIM para parar) ').strip()
  if comando.upper() == 'FIM':
    break
  else:
    ajuda(comando)
titulo('ATÉ LOGO', 'fVermelho')
