p = float(input('Qual é o seu peso? (Kg) '))
a = float(input('Qual é sua altura? (m) '))
imc = p / (a ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
  print('Você está ABAIXO DO PESO normal!')
elif imc < 25:
  print('PARABÉNS, você está na faixa de PESO IDEAL')
elif imc < 30:
  print('Você está em SOBREPESO')
elif imc < 40:
  print('Você está em OBESIDADE')
else:
  print('Você está em OBESIDADE MÓRBIDA, cuidado!')
