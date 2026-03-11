import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
# Analisar sequestro
# 1. Comportamento temporal (ano)
# 2. Qual região teve mais sequestro?
# Analisar roubo_celular
# 1. Qual epoca do ano é mais propenso?
# 2. Existem DPs que registram muito mais ocorrencias?

# OBTER DADOS
try:
    dados = pd.read_csv(
        '03.BaseDPEvolucaoMensalCisp.csv',
        sep=';', encoding='iso-8859-1')
    dp = pd.read_csv('08.DP.csv', sep=',', 
                     encoding='utf-8')
    # juntar com codDP
    df_comDP = dados.merge(dp, left_on='cisp',
                           right_on='codDP', how='left')
    df_sequestro = df_comDP[['cisp', 'nome', 'sequestro', 
                             'regiao', 'ano']]
    
except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit(1)

# ANALISE
try:
    df_sequestro_ano = \
    df_sequestro.groupby('ano')['sequestro'].sum().reset_index()
    
    # print(df_sequestro_ano)
    df_sequestro_regiao = \
    df_sequestro.groupby('regiao')['sequestro']. \
    sum().reset_index().sort_values(by='sequestro', 
                                    ascending=False)

except Exception as e:
    print(f'Erro ao analisar os dados: {e}')
    exit(1)

# VISUALIZACAO
try: 
    # Primeiro gráfico: evolução temporal de sequestros
    plt.subplots(2, 2, figsize=(16,9))
    plt.subplot(2, 2, 1)
    plt.plot(df_sequestro_ano['ano'].astype(str), df_sequestro_ano['sequestro'], marker='o', color='tomato', linestyle='--', linewidth=2)
    plt.title('Evolução Temporal de Sequestros')
    plt.xticks(rotation=45)
    plt.xticks(rotation=45)
    # Segundo gráfico: sequestros por região
    plt.subplot(2, 2, 2)
    plt.bar(df_sequestro_regiao['regiao'], df_sequestro_regiao['sequestro'], color='steelblue')
    plt.tight_layout()
    plt.title('Sequestros por Região')
    plt.xticks(rotation=0)
    # terceiro gráfico: Boxplot para sequestros por região
    plt.subplot(2, 2, 3)
    plt.boxplot(df_sequestro['sequestro'], showmeans=True, showfliers=True)
    plt.title('Boxplot de Sequestros por Região')
    # Quarto gráfico: Boxplot sem outliers
    plt.subplot(2, 2, 4)
    plt.boxplot(df_sequestro['sequestro'], showmeans=True, showfliers=False)
    plt.title('Boxplot de Sequestros por Região (sem outliers)')
    plt.show()
except Exception as e:
    print(f'Erro ao visualizar os dados: {e}')
    exit(1)
