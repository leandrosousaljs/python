aluno = {}
aluno['nome'] = input('Nome: ')
aluno['média'] = float(input('Média: '))
if aluno['média'] < 5:
  aluno['situação'] = 'Reprovado'
elif 5 <= aluno['média'] <= 6.9:
  aluno['situação'] = 'Recuperação'
else:
  aluno['situação'] = 'Aprovado'
print()
for k, v in aluno.items():
  print(f'{k}: {v}')
