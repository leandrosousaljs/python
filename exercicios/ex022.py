n = input('Digite seu nome completo: ').strip()
print(f'''Analisando seu nome...
Seu nome em maiúsculas é {n.upper()}
Seu nome em minúsculas é {n.lower()}
Seu nome tem ao todo {len(n) - n.count(' ')}
Seu primeiro nome é {n.split()[0]} e ele tem {len(n.split()[0])} letras''')
