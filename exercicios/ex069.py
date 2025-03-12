maiores = homens = mulheres20 = 0
while True:
  idade = int(input('Idade: '))
  sexo = ' '
  while sexo not in 'MF':
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
  op = ' '
  while op not in 'SN':
    op = input('Quer continuar? [S/N]: ').strip().upper()[0]
  if idade > 18:
    maiores += 1
  if sexo == 'M':
    homens += 1
  if sexo == 'F' and idade < 20:
    mulheres20 += 1
  if op in 'N':
    break
print(f'''Total de pessoas com mais de 18 anos: {maiores}
Ao todo temos {homens} homens cadastrados
E temos {mulheres20} mulheres com menos de 20 anos''')
