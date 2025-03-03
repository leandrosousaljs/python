from datetime import date
a = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if a == 0:
  a = date.today().year
print(f'O ano {a} é BISSEXTO!' if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 else f'O ano {a} não é BISSEXTO!')
