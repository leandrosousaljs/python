total = totMil = menorPreco = cont = 0
barato = ''
while True:
  produto = input('Nome do Produto: ')
  preco = float(input('Preço: R$'))
  resp = ' '
  total += preco
  cont += 1
  if cont == 1 or preco < menorPreco:
    menorPreco = preco
    barato = produto
  if preco > 1000:
    totMil += 1
  while resp not in 'SN':
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
  if resp == 'N':
    break
print(f'''O total da compra foi R${total:.2f}
Temos {totMil} produtos custando mais de R$1000,00
O produto mais barato foi {barato} que custa R${menorPreco:.2f}''')
