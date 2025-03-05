print(f'{' LOJAS GUANABARA ':=^40}')
v = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
o = int(input('Qual é a opção? '))
if o == 1:
  print(f'Sua compra de R${v:.2f} vai custar R${v * 0.9:.2f} no final.')
elif o == 2:
  print(f'Sua compra de R${v:.2f} vai custar R${v * 0.95:.2f} no final.')
elif o == 3:
  print(f'''Sua compra será parcelada em 2x de R${v / 2:.2f} SEM JUROS
Sua compra de R${v:.2f} vai custar R${v:.2f} no final.''')
elif o == 4:
  p = int(input('Quantas parcelas? '))
  print(f'''Sua compra será parcelada em {p}x de R${(v + v * 0.2) / p:.2f} COM JUROS')
Sua compra de R${v:.2f} vai custar R${v * 1.2:.2f} no final.''')
else:
  print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
