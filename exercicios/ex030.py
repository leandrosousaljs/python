from utils.cores import Cores


n = int(input(f'{Cores.roxo}Me diga um número qualquer:{Cores.reset} {Cores.verde}'))
print(f'{Cores.reset}O número {n} é {Cores.azul}PAR{Cores.reset}' if n % 2 == 0 else f'O número {n} é {Cores.azul}ÍMPAR{Cores.reset}')
