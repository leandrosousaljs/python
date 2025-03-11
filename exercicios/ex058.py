from random import randint
nComp = randint(0,10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
tentativas = 0
palpite = 0
while palpite != nComp:
  palpite = int(input('Qual é o seu palpite: '))
  tentativas += 1
  if palpite < nComp:
    print('Mais... Tente mais uma vez.')
  elif palpite > nComp:
    print('Menos... Tente mais uma vez.')
  else:
    print(f'Acertou com {tentativas} tentativas. Parabéns!')
