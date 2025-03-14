nums = []
for i in range(0,5):
  n = int(input('Digite um valor: '))
  if i == 0 or n > nums[-1]:
    nums.append(n)
    print('Valor adicionado ao final da lista...')
  else:
    pos = 0
    while pos < len(nums):
      if n <= nums[pos]:
        nums.insert(pos, n)
        print(f'Valor adicionado na posição {pos} da lista...')
        break
      pos += 1
print(f'Os valores digitados em ordem foram {nums}')
