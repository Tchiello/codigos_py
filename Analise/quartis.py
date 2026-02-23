import pandas as pd
import numpy as np


#1. Criar um DataFrame de exemplo de dados fictícios a respeito de prazo de entrega de produtos
dados = np.array([10,25,27,56,8,13,85,49,27,1,99,55,60])
q1 = np.percentile(dados, 25) #calcula o primeiro quartil (Q1) usando a função np.percentile, que retorna o valor abaixo do qual 25% dos dados estão localizados.
q2 = np.percentile(dados, 50) #calcula o segundo quartil (Q2) ou mediana, que é o valor abaixo do qual 50% dos dados estão localizados.
q3 = np.percentile(dados, 75) #calcula o terceiro quartil (Q3), que é o valor abaixo do qual 75% dos dados estão localizados.
print(f'Primeiro Quartil (Q1 - Mais rápidos) Q1: {q1}')
print(f'Segundo Quartil (Q2 - Mediana/Padrão) Q2: {q2}')
print(f'Terceiro Quartil (Q3 - Mais lentos) Q3: {q3}')

media = np.mean(dados) #calcula a média dos dados usando a função np.mean, que retorna o valor médio dos dados.
delta_media_mediana = media - q2 #calcula a diferença entre a média e a mediana (Q2) para avaliar a assimetria dos dados.

print(f'Média: {media}')
print(f'diferença entre média e mediana: {delta_media_mediana:.2f}')