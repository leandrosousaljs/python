import os
import csv
import time
import json
from sys import argv
from random import random
from datetime import datetime

import seaborn as sns
import pandas as pd
import requests

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'

def extracao():

  # Criando a variavel data e hora

  for _ in range(0, 10):
    data_e_hora = datetime.now()
    data = datetime.strftime(data_e_hora, '%d/%m/%Y')
    hora = datetime.strftime(data_e_hora, '%H:%M:%S')
    
    # Captando a taxa CDI
    
    try:
      response = requests.get(URL)
      response.raise_for_status()
    except requests.HTTPError as exc:
      print('Dado não encontrado, continuando...')
      cdi = None
    except Exception as exc:
      print('Erro, parando a execução.')
      raise exc
    else:
      dado = json.loads(response.text)[-1]['valor']
      cdi = float(dado) + (random() - 0.5)
      
    # Verificando se o arquvio "taxa-cdi.csv" existe
    
    if not os.path.exists('./taxa-cdi.csv'):
      with open(file='./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
        fp.write('data,hora,taxa\n')
        
    # Salvando dados no arquivo "taxa-cdi.csv"
    
    with open(file='./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
      fp.write(f'{data},{hora},{cdi}\n')
      
    time.sleep(2 + (random() - 0.5))
  print('Sucesso')
  
def visualizacao():

  # Extraindo as colunas hora e taxa
  
  df = pd.read_csv('./taxa-cdi.csv')
  
  # Salvando no gráfico
  
  grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
  _ = grafico.set_xticklabels(labels=df['hora'], rotation=90)
  grafico.get_figure().savefig(f'{argv[1]}.png' if len(argv) > 1 else 'grafico.png')

def main():
  extracao()
  visualizacao()

if __name__ == '__main__':
  main()
