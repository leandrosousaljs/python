s = 0
q = 0
for c in range(1, 501, 2):
  if c % 3 == 0:
    s += c
    q += 1
print(f'A soma de todos os {q} valores solicitados é {s}')
