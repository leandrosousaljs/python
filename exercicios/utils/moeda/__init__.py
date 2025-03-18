def metade(p=0, formato=True):
  res = p / 2
  return res if not formato else moeda(res)


def dobro(p=0, formato=True):
  res = p * 2
  return res if not formato else moeda(res)


def aumentar(p=0, t=0, formato=True):
  res = p + (p * t / 100)
  return res if not formato else moeda(res)


def diminuir(p=0, t=0, formato=True):
  res = p - (p * t / 100)
  return res if not formato else moeda(res)


def moeda(p=0, m='R$'):
  return f'{m}{p:.2f}'.replace('.', ',')


def resumo(p=0, a=10, r=10):
  print(f'''{'-'*30}
{'RESUMO DO VALOR'.center(30)}
{'-'*30}
Preço analisado: \t{moeda(p)}
Dobro do preço: \t{dobro(p)}
Metade do preço: \t{metade(p)}
{a}% de aumento: \t{aumentar(p, a)}
{r}% de redução: \t{diminuir(p, r)}
{'-'*30}''')