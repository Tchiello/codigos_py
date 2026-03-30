
import polars as pl
from sqlalchemy import create_engine

# Configuração
PARQUET_PATH = r'dados_bronze/df_bf.parquet'
TABELA = 'bolsa_familia'
BATCH_SIZE = 10000
ENGINE_URL = (
    'mysql+pymysql://root:@localhost:3306/bolsa_familia'
)

# Conexão
engine = create_engine(ENGINE_URL)

# Leitura
print ('Lendo arquivo parquet')
df = pl.read_parquet(PARQUET_PATH)

# Escrita am batch (lote) no banco
total = df.shape[0]
linhas = 0

for i, batch in enumerate(df.iter_slices(n_rows=BATCH_SIZE)):
    batch_PD =  batch.to_pandas()

    modo = 'replace' if i == 0 else 'append'
    # se fosse usar o método if teria que fazer um código com varias linhas do tipo:
    # if i == 0:
    #     modo = 'replace'
    # else:
    #     modo = 'append'

    batch_PD.to_sql(
        name=TABELA, 
        con=engine, 
        if_exists=modo, 
        index=False
    )
    linhas += batch_PD.shape[0]
    percent = (linhas / total) * 100
    print(f"Progresso {i + 1} | : {percent:.2f}%")
    
