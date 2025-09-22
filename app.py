import streamlit as st
import pandas as pd 
from Etl import desvio_padrao, maior_valor, media_valor, menor_valor, moda_valor, nome_tipo, valor_branco, valor_duplicado, valor_mediana, valor_medio, valor_moda, valor_unico, valores_distintos_string
from graficos import graficos_numericos, graficos_categoricos

st.title("ETL Python")
st.subheader("Insira seu CSV")

uploaded_file = st.file_uploader("Faça o upload de um arquivo CSV", type='csv',)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("Nomes, Tipos e Valores Duplicados")
    st.write("Valores Distintos:", valores_distintos_string(data))
    st.write(data.dtypes)

    st.subheader("Valores em Branco e Duplicados")
    st.write("Valores em Branco:",valor_branco(data))
    st.write("Valores Duplicados:", valor_duplicado(data))

    st.subheader("Maior e Menor Valor")
    st.write("Maior Valor:", maior_valor(data))
    st.write("Menor Valor:", menor_valor(data))

    st.subheader("Média e Moda")
    st.write("Média:", valor_medio(data))
    st.write("Mediana:", valor_mediana(data))
    st.write("Moda:", valor_moda(data))

    st.subheader("Desvio Padrão e Valores Únicos")
    st.write("Desvio Padrão:", desvio_padrao(data))
    st.write("Valor Único:", valor_unico(data))

#Gráficos

    st.subheader("Gráficos Numéricos")
    graficos_numericos(data)

    st.subheader("Gráficos Categóricos")
    graficos_categoricos(data)

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




