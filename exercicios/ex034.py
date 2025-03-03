s = float(input('Qual é o salário do funcionário? R$'))
print(f'Quem ganhava R${s:.2f} passa a ganhar R${s * 1.15 if s <= 1250 else s * 1.10:.2f} agora.')
