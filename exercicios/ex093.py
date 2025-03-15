jogador = {}
partidas = []
jogador['nome'] = input('Nome do jogador? ')
tot = int(input(f'Quantas partidas o {jogador['nome']} jogou? '))
for c in range(0, tot):
  partidas.append(int(input(f'Quantos gols na {c + 1}ª partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
for k, v in jogador.items():
  print(f'O campo {k} tem o valor {v}')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
  print(f'  → Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
