n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
  print('''      [ 1 ] somar
      [ 2 ] multiplicar
      [ 3 ] maior
      [ 4 ] novos números
      [ 5 ] sair''')
  op = int(input('>>>>> Qual é a sua opção? '))
  if op == 1:
    print(f'A soma entre {n1} + {n2} é {n1 + n2}')
  elif op == 2:
    print(f'A multiplicação entre {n1} x {n2} é {n1*n2}')
  elif op == 3:
    if n1 > n2:
      print(f'O número {n1} é maior que o número {n2}')
    elif n2 > n1:
      print(f'O número {n2} é maior que o número {n1}')
    else:
      print('Os dois números são iguais')
  elif op == 4:
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
  elif op == 5:
    print('Finalizando...')
  else:
    print('Opção invalida. Tente novamente.')
  print('=-=' * 10)
print('Fim do programa. Volte sempre!')
