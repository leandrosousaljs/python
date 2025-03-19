def leiaDinheiro(msg):
  from ..cores import Cores
  valido = False
  while not valido:
    p = input(msg).replace(',', '.').strip()
    if p.isalpha() or p == '':
      print(f'{Cores.vermelho}ERRO: \"{p}\" é um preço inválido!{Cores.reset}')
    else:
      valido = True
      return float(p)


def leiaInt(msg):
  from utils.cores import Cores
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print(f'{Cores.vermelho}ERRO! Por favor, digite um número inteiro válido.{Cores.reset}')
      continue
    except (KeyboardInterrupt):
      print(f'{Cores.vermelho}ERRO! Usuário preferiu não digitar nenhum número.{Cores.reset}')
      return 0
    else:
      return n


def leiaFloat(msg):
  from utils.cores import Cores
  while True:
    try:
      n = float(input(msg))
    except (ValueError, TypeError):
      print(f'{Cores.vermelho}ERRO! Por favor, digite um número real válido.{Cores.reset}')
      continue
    except (KeyboardInterrupt):
      print(f'{Cores.vermelho}ERRO! Usuário preferiu não digitar nenhum número.{Cores.reset}')
      return 0
    else:
      return n
