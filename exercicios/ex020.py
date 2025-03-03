from random import shuffle
nomes = input('Digite 4 nomes: ').split()
shuffle(nomes)
print(f'A ordem de apresentação será {nomes}')
