n = cont = soma = maior = menor = 0
op = ''
while op in 'Ss':
  n = int(input('Digite um número: '))
  op = (input('Deseja continuar? [S/N] ')).strip().upper()[0]
  cont += 1
  soma += n
  if cont == 1:
    maior = menor = n
  else:
    if n > maior:
      maior = n
    elif n < menor:
      menor = n
print(f'''Você digitou {cont} números e a média foi de {soma/cont:.2f}.
O maior valor foi {maior} e o menor foi {menor}.''')
