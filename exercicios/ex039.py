from datetime import date
a = int(input('Ano de nascimento: '))
d = date.today().year
i = d - a
print(f'Quem nasceu em {a} tem {i} anos em {d}.')
if i < 18:
  print(f'''Ainda faltam {18 - i} anos para o alistamento.
Seu alistamento será em {a + 18}''')
elif i == 18:
  print('Você tem que se alistar IMEDIATAMENTE!')
else:
  print(f'''Você já deveria ter se alistado há {i - 18} anos.
Seu alistamento foi em {a + 18}''')
