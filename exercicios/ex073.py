serieA = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza',
          'Internacional', 'São Paulo', 'Corinthians', 'Bahia',
          'Cruzeiro', 'Vasco da Gama', 'EC Vitória', 'Atlético-MG',
          'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')
print('-='*15)
print(f'Lista de times do Brasileirão: {serieA}')
print('-='*15)
print(f'Os 4 primeiros são : {serieA[:4]}')
print('-='*15)
print(f'Os 4 últimos são: {serieA[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(serieA)}')
print('-='*15)
print(f'O Cruzeiro está na {serieA.index('Cruzeiro')+1}ª posição.')
