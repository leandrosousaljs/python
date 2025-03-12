lista = ('Lápis', 1.75,
        'Borracha', 2,
        'Caderno', 15.9,
        'Estojo', 25,
        'Transferidor', 4.2,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.3,
        'Livro', 34.9)
for pos in range(0, len(lista)):
  if pos % 2 == 0:
    print(f'{lista[pos]:.<30}R${lista[pos + 1]:>6.2f}')
