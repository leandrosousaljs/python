n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
o = int(input(f'Sua opção para converter o número {n}: '))
if o == 1:
  print(f'O número {n} em BINÁRIO é {bin(n)[2:]}')
elif o == 2:
  print(f'O número {n} em OCTAL é {oct(n)[2:]}')
elif o == 3:
  print(f'O número {n} em HEXADECIMAL é {hex(n)[2:]}')
else:
  print('Opção inválida. Tente novamente.')
