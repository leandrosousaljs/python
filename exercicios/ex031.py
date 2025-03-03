n = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {n}Km.')
p = n * 0.5 if n <= 200 else n * 0.45
print(f'E o preço da sua passagem será de R${p:.2f}.')
