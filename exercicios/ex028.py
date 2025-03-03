from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n = int(input('Em que número eu pensei? '))
ns = randint(0,5)
print('PROCESSANDO...')
sleep(2)
print('PARABÉNS! Você conseguiu me vencer' if ns == n else f'GANHEI! Eu pensei no número {ns} e não no {n}')
