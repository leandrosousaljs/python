for i in range(1,6):
  p = float(input(f'Peso da {i}ª pessoa: '))
  if i == 1:
    maior = p
    menor = p
  else:
    if p > maior:
      maior = p
    if p < menor:
      menor = p
print(f'''O maior peso lido foi de {maior:.1f}Kg
O menor peso lido foi de {menor:.1f}Kg''')
