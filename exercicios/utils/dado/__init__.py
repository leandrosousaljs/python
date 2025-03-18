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
  ok = False
  valor = 0
  while True:
    n = input(msg).strip()
    if n.isnumeric():
      valor = int(n)
      ok = True
    else:
      print(f'{Cores.vermelho}ERRO! Digite um número inteiro válido.{Cores.reset}')
    if ok:
      break
  return valor
