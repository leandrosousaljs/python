from random import randint
v = 0
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
  n = int(input('Diga um valor: '))
  op = (input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
  comp = randint(0,10)
  total = n + comp
  while op not in 'PI':
    op = (input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
  print(f'Você jogou {n} e o computador jogou {comp}. Total de {total} DEU' , 'PAR' if total % 2 == 0 else 'ÍMPAR')
  if op == 'P':
    if total % 2 == 0:
      print('Você VENCEU!')
      v += 1
    else:
      print('Você PERDEU!')
      break
  elif op == 'I':
    if total % 2 != 0:
      print('Você VENCEU!')
      v += 1
    else:
      print('Você PERDEU!')
      break
  print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
