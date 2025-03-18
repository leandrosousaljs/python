import utils.moeda as moeda


p = float(input('Digite o preço: R$ '))
print(f'''A metade de R${p:.2f} é R${moeda.metade(p)}.
O dobro de R${p:.2f} é R${moeda.dobro(p)}.
Aumentando 10% temos R${moeda.aumentar(p, 10)}.''')
