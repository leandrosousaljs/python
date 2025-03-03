from random import choice
nomes = input('Digite 4 nomes: ').split()
cho = choice((nomes))
print(f'O aluno escolhido foi {cho}')
