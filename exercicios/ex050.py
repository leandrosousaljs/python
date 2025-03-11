s = 0
c = 0
for i in range (1,7):
  n = int(input(f'Digite o {i}° valor: '))
  if n % 2 == 0:
    s += n
    c += 1
print(f'Você informou {c} valores PARES e a soma foi {s}')
