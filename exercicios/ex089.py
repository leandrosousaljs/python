ficha = []
while True:
  nome = input('Nome: ')
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))
  media = (nota1 + nota2) / 2
  ficha.append([nome, [nota1, nota2], media])
  resp = input('Quer continuar? [S/N] ').strip()
  if resp in 'Nn':
    break
print(f'{'N°':<4}{'NOME':<10}{'MÉDIA':>8}')
for i, a in enumerate(ficha):
  print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
  opc = int(input('Deseja mostrar notas de qual aluno? (999 interrompe): '))
  if opc == 999:
    print('FINALIZANDO...')
    break
  if opc <= len(ficha) - 1:
    print(f'As notas de {ficha[opc][0]} são: {ficha[opc][1]}')
