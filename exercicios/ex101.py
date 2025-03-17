def voto():
  from datetime import date
  ano = int(input('Em que ano você nasceu? '))
  idade = date.today().year - ano
  if idade < 16:
    return print(f'Com {idade} anos: NÃO VOTA')
  elif idade == 16 or idade < 18 or idade >= 65:
    return print(f'Com {idade} anos: VOTO OPCIONAL')
  else:
    return print(f'Com {idade} anos: VOTO OBRIGATÓRIO')


voto()
