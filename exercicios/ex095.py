jogador = {}
partidas = []
time = []
while True:
  jogador.clear()
  jogador['nome'] = input('Nome do jogador? ')
  tot = int(input(f'Quantas partidas o {jogador['nome']} jogou? '))
  partidas.clear()
  for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na {c + 1}ª partida? ')))
  jogador['gols'] = partidas[:]
  jogador['total'] = sum(partidas)
  time.append(jogador.copy())
  while True:
    r = input('Quer continuar? ').strip().upper()[0]
    if r in 'SN':
      break
    print('ERRO! Responda apenas S ou N.')
  if r == 'N':
    break
print('-'*40)
print('cod ', end='')
for i in jogador.keys():
  print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
  print(f'{k:>3} ', end='')
  for d in v.values():
    print(f'{str(d):<15}', end='')
  print()
print('-'*40)
while True:
  busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
  if busca == 999:
    break
  if busca >= len(time):
    print(f'ERRO! Não existe jogador com código {busca}!')
  else:
    print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} --')
    for i, g in enumerate(time[busca]['gols']):
      print(f'    No jogo {i +1} fez {g} gols.')
    print('-'*40)
print('<<VOLTE SEMPRE>>')
