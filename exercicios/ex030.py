from cores import cores
n = int(input(f'{cores['roxo']}Me diga um número qualquer:{cores['limpa']} {cores['verde']}'))
print(f'{cores['limpa']}O número {n} é {cores['azul']}PAR{cores['limpa']}' if n % 2 == 0 else f'O número {n} é {cores['azul']}ÍMPAR{cores['limpa']}')
