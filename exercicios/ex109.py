import utils.moeda as moeda


p = float(input('Digite o preço: R$ '))
print(f'''A metade de {moeda.moeda(p)} é {moeda.metade(p)}.
O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}.
Aumentando 10% temos {moeda.aumentar(p, 10)}.
Diminuindo 13% temos {moeda.diminuir(p, 13)}.''')
