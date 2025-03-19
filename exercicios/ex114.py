import urllib
import urllib.request
from utils.cores import Cores


try:
  site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
  print(f'{Cores.vermelho}O site Pudim não está acessível no momento. :({Cores.reset}')
else:
  print(f'{Cores.verde}Consegui acessar o site Pudim com sucesso! :D{Cores.reset}')
