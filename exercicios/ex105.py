def notas(*n, sit=False):
  """_summary_

  Args:
      *n, _int_: Recebe uma ou mais notas dos alunos.
      sit (bool, optional): Adicona ou não a situação do aluno. Defaults to False.

  Returns:
      _dict_: Retorna um dicionário com as notas, a média e a situação do aluno.
  """
  r = {}
  r['total'] = len(n)
  r['maior'] = max(n)
  r['menor'] = min(n)
  r['media'] = sum(n) / len(n)
  if sit:
    if r['media'] >= 7:
      r['situação'] = 'BOA'
    elif r['media'] <= 5:
      r['situação'] = 'RUIM'
    else:
      r['situação'] = 'RAZOAVEL'
  return r


resp = notas(5.5, 0.5, 2, 8.5, sit=True)
print(resp)
help(notas)
