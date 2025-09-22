import streamlit as st
import pandas as pd 
from Etl import desvio_padrao, maior_valor, valor_medio, menor_valor, valor_moda, \
                 nome_tipo, valor_branco, valor_duplicado, valor_mediana, valor_unico, valores_distintos_string
from graficos import graficos_numericos, graficos_categoricos

st.title("ETL Python")
st.subheader("Insira seu CSV")

uploaded_file = st.file_uploader("Faça o upload de um arquivo CSV", type='csv')

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # --- Valores distintos ---
    st.subheader(" Valores Distintos")
    valores_distintos = valores_distintos_string(data)

    # Transformar em DataFrame para mostrar como tabela
    df_valores_distintos = pd.DataFrame({
        "Coluna": list(valores_distintos.keys()),
        "Quantidade de Valores Distintos": list(valores_distintos.values())
    })
    st.table(df_valores_distintos)

    # --- Tipos das colunas ---
    st.subheader("Tipos de Dados")
    colunas, tipos = nome_tipo(data)
    st.table(pd.DataFrame({"Tipo": tipos}))

    # --- Valores em branco e duplicados ---
    st.subheader("Valores em Branco e Duplicados")
    st.table(pd.DataFrame({
        "Valores em Branco": [valor_branco(data)], 
        "Valores Duplicados": [valor_duplicado(data)]
    }))

    # --- Filtrando apenas colunas numéricas ---
    df_numerico = data.select_dtypes(include='number')

    # --- Maior e Menor Valor ---
    st.subheader("Maior e Menor Valor")
    st.table(pd.DataFrame({
        "Maior Valor": maior_valor(df_numerico),
        "Menor Valor": menor_valor(df_numerico)
    }))

    # --- Média, Mediana e Moda ---
    st.subheader("Média, Mediana e Moda")
    st.table(pd.DataFrame({
        "Média": valor_medio(df_numerico),
        "Mediana": valor_mediana(df_numerico),
        "Moda": valor_moda(df_numerico)
    }))

    # --- Desvio Padrão e Valores Únicos ---
    st.subheader("Desvio Padrão e Valores Únicos")
    st.table(pd.DataFrame({
        "Desvio Padrão": desvio_padrao(df_numerico),
        "Valores Únicos": valor_unico(df_numerico)
    }))

    # --- Gráficos ---
    st.subheader("Gráficos Numéricos")
    graficos_numericos(data)

    st.subheader("Gráficos Categóricos")
    graficos_categoricos(data)

    # --- Validação ---
    erros = []
    dados_validados = []

    for index, row in data.iterrows():
        try:
            user = row.to_dict()  
            dados_validados.append(user)
        except Exception as e:
            erros.append({"linha": index, "erro": str(e)})

    if not erros:
        st.write("Todos os registros são válidos!")
    else:
        st.subheader("Erros de Validação:")
        for erro in erros:
            st.write(erro)

    if dados_validados:
        df_validados = pd.DataFrame(dados_validados)
        st.download_button(
            "Download CSV",
            df_validados.to_csv(index=False),
            "dados_validados.csv",
            "text/csv"
        )
