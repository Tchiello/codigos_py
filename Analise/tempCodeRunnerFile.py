import pandas as pd
import numpy as np

#1. Criar um DataFrame de exemplo de dados fictícios
dados = np.array([10,25,27,56,8,13,85,49,27,1,99,55,60])
q1 = np.percentile(dados, 25) #calcula o primeiro quartil (Q1) usando a função np.percentile, que retorna o valor abaixo do qual 25% dos dados estão localizados.
q2 = np.percentile(dados, 50) #calcula o segundo quartil (Q2) ou mediana, que é o valor abaixo do qual 50% dos dados estão localizados.
q3 = np.percentile(dados, 75) #calcula o terceiro quartil (Q3), que é o valor abaixo do qual 75% dos dados estão localizados.
print(f'Primeiro Quartil (Q1 - Mais rápidos) Q1: {q1}')
print(f'Segundo Quartil (Q2 - Mediana/Padrão) Q2: {q2}')
print(f'Terceiro Quartil (Q3 - Mais lentos) Q3: {q3}')