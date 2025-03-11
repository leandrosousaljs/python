from datetime import date
ca = 0
cj = 0
d = date.today().year
for i in range(1,8):
  a = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
  if a <= d - 21:
    ca += 1
  else:
    cj += 1
print(f'''Ao todo tivemos {ca} pessoas maiores de idade
E também tivemos {cj} pessoas menores de idade''')
