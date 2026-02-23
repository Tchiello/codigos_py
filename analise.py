# Importação das bibliotecas que vão ser utilizadas
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# Criar uma tabela aleatória
# cria 20 "pedidos" 
import random
produtos = ['computador', 'celular', 'tablet', 'monitor', 'teclado', 'mouse', 'impressora', 'câmera', 'fones de ouvido', 'caixa de som']
# O uso de dicionário é mais eficiente para criar um DataFrame, 
# pois permite criar as colunas diretamente e vai ficar mais parecido com o formato de uma tabela, 
# além de ser mais fácil de ler e entender o código. 
# O uso de listas para criar as colunas pode ser mais trabalhoso e menos eficiente, 
# pois é necessário criar uma lista para cada coluna e depois combiná-las em um DataFrame. 
# O uso de dicionário também permite criar as colunas com nomes específicos, 
# o que torna o código mais legível e fácil de entender.
dados = {
    'Produto': [random.choice(produtos) for _ in range(20)],
    'Preco': [random.randint(200, 7000) for _ in range(20)],
    'Quantidade': [random.randint(1, 10) for _ in range(20)],
    'Data': pd.date_range(start='2026-01-01', periods=20, freq='D')
}
# Como boa prática uma vez criado o dataframe não se deve modificá-lo, 
# para isso é recomendado criar uma cópia do dataframe original e trabalhar com a cópia, 
# isso evita que o dataframe original seja modificado acidentalmente 
# e permite que você tenha uma referência do estado original dos dados 
# caso precise voltar atrás ou comparar os resultados.
df = pd.DataFrame(dados)
# head () é um método do pandas que retorna as primeiras linhas de um DataFrame. 
# tail() é um método do pandas que retorna as últimas linhas de um DataFrame.
# Ele é útil para visualizar rapidamente os dados e verificar se eles foram carregados corretamente. 
# Por padrão, o head() retorna as primeiras 5 linhas, mas você pode especificar o número de linhas que deseja retornar passando um argumento, 
# por exemplo, head(10) retornaria as primeiras 10 linhas do DataFrame.
print ("-"*49)
print(df)
print ("-"*49)
print (df.describe())
print ("-"*49)
print (df.head(10))
print ("-"*49)
print (df.tail())
print ("-"*49)
print (df.shape)
print ("-"*49)
print (df.columns)
# Para exibir mais colunas, usa-se a notação das colunas separadas por vírgulas dentro de colchetes.
# pode-se usar uma estrutura de set para definir o número de colunas a serem exibidas, por exemplo:
# pd.set_option('display.max_columns', 10) # Exibe até 10 colunas
print ("-"*49)
print (df.dtypes)
print ("-"*49)
# O método info() é usado para obter informações sobre o DataFrame, como o número de linhas, colunas, tipos de dados e valores nulos.
print (df.info())
print ("-"*49)
# Filtar o dataframe com base numa coluna específica, por exemplo, para filtrar os produtos com preço maior que 1000:
df_filtrado = df[df['Preco'] > 1000]
print ("-"*49)
print (df_filtrado)
print ("-"*49)
#Inserir uma coluna calculada no DataFrame, 
# Por exemplo, para calcular o preço total de cada pedido multiplicando o preço pelo quantidade:
print ("-"*49)
df['Preco_final'] = df['Preco'] * df['Quantidade']
print ("-"*49)
# O df.dtypes é usado para exibir os tipos de dados de cada coluna do DataFrame.
print ("-"*49)
print(df.dtypes)
print ("-"*49)
df.to_csv('dados.csv', index=False)
print ("Dados exportados para dados.csv")
print ("-"*49)