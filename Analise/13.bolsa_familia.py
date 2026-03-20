import polars as pl
import pandas as pd
import datetime as dt
# Para ler arquivos dentro de uma pasta no windows:
import os
# Para limpar resíduos -> garbage collector
import gc
ENDERECO_DADOS = r"C:/Users/marcelo.mmoreira/Documents/MarceloMM/UC1/codigos_py/Pasta Base BF/"
try:
    print('obtendo_arquivos')
    hora_inicio = dt.datetime.now()

    # lista de arquivos
    arquivos = os.listdir(ENDERECO_DADOS)
    for arquivo in arquivos:
        print(f'Lendo_arquivo: {arquivo}')

        #df = pd.read_csv(ENDERECO_DADOS  + arquivo, sep =';', encoding ='iso-8859-1')
        df = pl.read_csv(ENDERECO_DADOS  + arquivo, separator =';', encoding ='iso-8859-1')
        if 'df_bf' in locals():
            # Para utilizar o polars temos que substituir pd.concat por pl.concat e vice versa
            # Ou seja para rodar o Pandas temos que substituir pl.concat por pd.concat
            df_bf = pl.concat([df_bf, df])
        else: df_bf = df

        del df
    df_bf = df_bf.with_columns(
        pl.col("VALOR PARCELA").str.replace_all(",", ".").cast(pl.Float64)  
        # Substitua "VALOR PARCELA" e "Float64" pelos valores corretos
    )
    df_bf.write_parquet('C:/Users/marcelo.mmoreira/Documents/MarceloMM/UC1/codigos_py/Analise/dados_bronze/df_bf.parquet')
    gc.collect()
    hora_fim = dt.datetime.now()
    print(f'Tempo total: {hora_fim - hora_inicio}')

except Exception as e:
    print(f'Erro ao obter dados: {e}')