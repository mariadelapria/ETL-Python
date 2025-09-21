import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('data.csv', sep=';',)

profile = ProfileReport(df, title='Data Profiling Report')
profile.to_file("data_profiling.html")

# Nome e Tipo das Colunas

def nome_tipo(df):
    return df.columns.tolist(), df.dtypes
colunas, tipos = nome_tipo(df)
print("Colunas:", colunas)
print("\nTipos:")
print(tipos)

# Valores vazios 

def valor_branco(df):
    return df.isnull().any(axis=1).sum()
linhas_branco = valor_branco(df)
print("Quantidade de linhas com valores em branco:", linhas_branco)

vazio = df.isnull()
linhas_colunas_vazias = vazio.stack()[vazio.stack() == True].index.tolist()
print("Detalhe das células vazias (linha, coluna):")
print(linhas_colunas_vazias)

# Valores duplicados

def valor_duplicado(df):
    return df.duplicated().sum()
linhas_duplicadas = valor_duplicado(df)
print("Quantidade de linhas duplicadas:", linhas_duplicadas)











