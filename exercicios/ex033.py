n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
maior = n1
menor = n1
if n2 > n1 and n2 > n3:
  maior = n2
if n3 > n1 and n3 > n2:
  maior = n3
if n2 < n1 and n2 < n3:
  menor = n2
if n3 < n1 and n3 < n2:
  menor = n3
print(f'''O menor valor digitado foi {menor}
O maior valor digitado foi {maior}''')
