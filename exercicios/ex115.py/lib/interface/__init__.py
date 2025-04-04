def leiaInt(msg):
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print(f'\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
      continue
    except (KeyboardInterrupt):
      print(f'\n\033[31mERRO! Usuário preferiu não digitar nenhum número.\033[m')
      return 0
    else:
      return n


def linha(tam=42):
  return '-' * tam

def cabecalho(txt):
  print(linha())
  print(txt.center(42))
  print(linha())


def menu(lst):
  cabecalho('MENU PRINCIPAL')
  c = 1
  for item in lst:
    print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
    c += 1
  print(linha())
  opc = leiaInt('\033[32mSua Opção: \033[m')
  return opc
