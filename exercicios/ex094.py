pessoa = {}
galera = []
soma = media = 0
while True:
  pessoa.clear()
  pessoa['nome'] = input('Nome: ')
  while True:
    pessoa['sexo'] = input('Sexo: [M/F] ').upper().strip()[0]
    if pessoa['sexo'] in 'MF':
      break
    print('ERRO! Por favor, digite apenas M ou F. ')
  pessoa['idade'] = int(input('Idade: '))
  soma += pessoa['idade']
  galera.append(pessoa.copy())
  while True:
    r = input('Quer continuar? [S/N] ').upper().strip()[0]
    if r in 'SN':
      break
    print('ERRO! Responda apenas S ou N.')
  if r == 'N':
    break
media = soma / len(galera)
print(f'''Ao todo temos {len(galera)} pessoas cadastradas.
A média de idade é de {media:.1f} anos.''')
print('As mulheres cadastradas foram ', end='')
for p in galera:
  if p['sexo'] == 'F':
    print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média de idade: ')
for p in galera:
  if p['idade'] >= media:
    print('     ', end='')
    for k, v in p.items():
      print(f'{k} = {v}; ', end='')
    print()
