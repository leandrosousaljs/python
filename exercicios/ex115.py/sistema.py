from lib.interface import *
from lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if not arqExiste(arq):
  criarArq(arq)

while True:
  resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
  if resp == 1:
    # Opção para listar o conteúdo do arquivo
    lerArq(arq)
  elif resp == 2:
    # Opção para cadastrar uma pessoa
    cabecalho('NOVO CADASTRO')
    nome = input('Nome: ')
    idade = leiaInt('Idade: ')
    cadastrar(arq, nome, idade)
  elif resp == 3:
    # Opção para sair do programa
    cabecalho('Saindo do sistema... Até logo!')
    break
  else:
    # Digitou uma opção errada no menu
    print('\033[31mERRO! Digite uma opção válida!\033[m')
  sleep(1)
