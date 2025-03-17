def leiaInt(msg):
  from cores import cores
  ok = False
  valor = 0
  while True:
    n = input(msg).strip()
    if n.isnumeric():
      valor = int(n)
      ok = True
    else:
      print(f'{cores[2]}ERRO! Digite um número inteiro válido.{cores[0]}')
    if ok:
      break
  return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
