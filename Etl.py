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

# Função para pegar apenas colunas do tipo string
def somente_strings(df):
    return df.select_dtypes(include='object')

# Função para mostrar valores distintos de cada coluna string
def valores_distintos_string(df):
    df_string = somente_strings(df)
    resultado = {}
    for col in df_string.columns:
        resultado[col] = df_string[col].dropna().unique().tolist()
    return resultado
valores_distintos = valores_distintos_string(df)
print("Valores distintos das colunas string:")
for coluna, valores in valores_distintos.items():
    print(f"{coluna}: {valores}")

#Função para cálculos númericos

def somente_numericas(df):
    return df.select_dtypes(include='number',)
df_numerico = somente_numericas(df)

#Menor Valor encontrado

def menor_valor(df_numerico):
    return df_numerico.min()
menores_valores = menor_valor(df_numerico)
print("Menores Valores:", menores_valores)

#Maior Valor encontrado

def maior_valor(df_numerico):
    return df_numerico.max()
maiores_valores = maior_valor(df_numerico)
print("Maiores Valores:", maiores_valores)

#Valor Médio encontrado

def valor_medio(df_numerico):
    return df_numerico.mean()
media_valor = valor_medio(df_numerico)
print("Média de Valores:", media_valor)

#Valor Mediano encontrado

def valor_mediana(df_numerico):
    return df_numerico.median()
mediano_valor = valor_mediana(df_numerico)
print("Mediana:", mediano_valor)

#Valor Moda encontrado

def valor_moda(df_numerico):
    return df_numerico.mode()[0]
moda_valor = valor_moda(df_numerico)
print("Valores Frequentes:", moda_valor)

#Desvio Padrão encontrado

def desvio_padrao(df_numerico):
    return df_numerico.std()
padrao_desvio = desvio_padrao(df_numerico)
print("Desvio Padrão:", padrao_desvio)

#Contagem de Valores Únicos

def valor_unico(df_numerico):
    return df_numerico.nunique()
unic_valor = valor_unico(df)
print("Valores Únicos:", unic_valor)










