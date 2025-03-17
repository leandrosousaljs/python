def fatorial(n, show=False):
  """_summary_
  -> Calcula o fatorial de um número número.
  
  Args:
      n (_int_): O número a ser calculado.
      show (bool, optional): Mostrar ou não a conta. Defaults to False.

  Returns:
      _int_: O fatorial do número.
  """
  f = 1
  for c in range(n, 0, -1):
    if show:
      print(f'{c} x ' if c > 1 else f'{c} = ', end='')
    f *= c
  return f


print(fatorial(5, True))
