somaIdade = 0
cMulheres = 0
maiorIdade = 0
velhoNome = ''
for i in range(1, 5):
  print(f'----- {i}ª PESSOA -----')
  nome = input('Nome: ').strip()
  idade = int(input('Idade: '))
  sexo = input('Sexo [M/F]: ').strip()
  somaIdade += idade
  if sexo in 'Mm':
    maiorIdade = idade
    velhoNome = nome
  elif sexo in 'Ff' and idade < 20:
    cMulheres += 1
  elif sexo not in 'MmFf':
    print('Sexo inválido. Por favor, digite M ou F.')
print(f'''A média de idade do grupo é de {somaIdade/4:.1f} anos.
O homem mais velho tem {maiorIdade} anos e se chama {velhoNome}.
Ao todo são {cMulheres} mulheres com menos de 20 anos.''')
