from cores import cores


n = int(input(f'{cores[6]}Me diga um número qualquer:{cores[0]} {cores[3]}'))
print(f'{cores[0]}O número {n} é {cores[5]}PAR{cores[0]}' if n % 2 == 0 else f'O número {n} é {cores[5]}ÍMPAR{cores[0]}')
