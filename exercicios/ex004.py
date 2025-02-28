smt = input('Digite algo:')
print(f'''O tipo primitivo desse valor é {type(smt)}
Só tem espaços? {smt.isspace()}
É um número? {smt.isnumeric()}
É alfabético? {smt.isalpha()}
É alfanumérico? {smt.isalnum()}
Está em maiúsculas? {smt.isupper()}
Está em minúsculas? {smt.islower()}
Está capitalizada? {smt.istitle()}''')
