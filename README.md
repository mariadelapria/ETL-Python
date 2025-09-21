# ETL-Python

# Descrição
Este projeto é uma aplicação ETL básica desenvolvida em Python usando Streamlit, Pydantic e Pandas.
O objetivo é permitir que o usuário faça upload de um arquivo CSV e visualize rapidamente informações essenciais sobre os dados.

# Como Funciona o Projeto ETL Python

1 - Upload do arquivo
O usuário envia um arquivo CSV pelo Streamlit usando o componente de upload.
O programa lê o arquivo usando Pandas.
Ele aceita arquivos CSV.

2 - Análise básica das colunas
O app verifica e mostra os nomes das colunas do arquivo.
Mostra o tipo de cada coluna (numérico, string, etc.), ajudando a entender a estrutura do CSV.

3 - Detecção de valores em branco
O programa identifica linhas que possuem células vazias.
Mostra quantos valores estão em branco e em quais colunas.

4 - Detecção de duplicatas
O app verifica se existem linhas duplicadas no CSV.
Exibe quantas linhas estão duplicadas, permitindo que o usuário faça limpeza dos dados.

5 - Exibição e download
O app exibe todas essas informações diretamente na página Streamlit.
Se houver dados válidos, o usuário pode baixar o CSV atualizado ou validado.
