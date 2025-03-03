v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
  m = (v - 80) * 7
  print(f'''\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h
Você deve pagar uma multa de R${m:.2f}!\033[31m''')
print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')
