print('Gerador de PA')
print('-=' * 10)
prim = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = prim
i = 1
total = 0
mais = 10
while mais != 0:
  total += mais
  while i <= total:
    print(f'{termo} → ', end='')
    termo += razao
    i += 1
  print('PAUSA')
  mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
