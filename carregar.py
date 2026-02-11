import pandas as pd
try :
    df = pd.read_csv('base.csv')
    print('-' * 49)
    print(df.head())
    print('-' * 49)
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")
print('-' * 49)
print(df.info())
print('-' * 49)