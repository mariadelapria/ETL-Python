import streamlit as st
import pandas as pd 
from Etl import nome_tipo

st.title("ETL Python")
st.subheader("Insira seu CSV")

uploaded_file = st.file_uploader("Faça o upload de um arquivo CSV", type='csv',)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("Nomes e Tipos das Colunas")
    st.write(data.dtypes)

    st.subheader("Valores em Branco e Duplicados")
    st.write("Valores em Branco:", data.isnull().sum())
    st.write("Valores Duplicados:", data.duplicated().sum())

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




