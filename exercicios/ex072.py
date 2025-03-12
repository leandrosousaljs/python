numExt = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'catorze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito',
          'dezenove', 'vinte')
while True:
  num = int(input('Digite um número entre 0 e 20 (Digite 999 para parar): '))
  if 0 <= num <= 20:
    print(f'Você digitou o número {numExt[num]}')
  elif num == 999:
    break
  else:
    print('Tente novamente. ', end='')
