n = int(input('Digite um número para ver sua tabuada: '))
print(f'''{'-'*12}
{n} x 1 = {n*1}
{n} x 2 = {n*2}
{n} x 3 = {n*3}
{n} x 4 = {n*4}
{n} x 5 = {n*5}
{n} x 6 = {n*6}
{n} x 7 = {n*7}
{n} x 8 = {n*8}
{n} x 9 = {n*9}
{n} x 10 = {n*10}
{'-'*12}''')
for i in range(1,11):
  print(f'{n} x {i:2} = {n*i}')
print('-'*12)
