f = input('Digite uma frase: ').strip().lower()
print(f'''A letra A aparece {f.count('a')} vezes na frase.
A primeira letra A apareceu na posição {f.find('a')+1}
A última letra A apareceu na posição {f.rfind('a')+1}''')
