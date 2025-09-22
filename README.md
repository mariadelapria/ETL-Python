## ETL-Python

# O projeto está disponível online
(https://etl-python-e69rabbu7nnqw3w5e6mapx.streamlit.app/).

# Descrição
Este projeto é uma aplicação ETL básica desenvolvida em Python usando Streamlit, Pandas e Pydantic.
O objetivo é permitir que o usuário faça upload de um arquivo CSV e visualize rapidamente informações importantes sobre os dados, além de realizar validações e gerar gráficos.
A aplicação ajuda a entender a estrutura do CSV, detectar problemas como valores em branco ou duplicados e fornecer estatísticas completas das colunas numéricas.

# Funcionalidades

1 - Upload de arquivos CSV
O usuário envia arquivos CSV pelo Streamlit.
O arquivo é lido e processado usando Pandas.

2 - Análise das colunas
Mostra os nomes e tipos de cada coluna, permitindo identificar colunas numéricas e categóricas.
Exibe a quantidade de valores distintos por coluna, ajudando a entender a diversidade de dados.

3 - Detecção de valores em branco e duplicados
Identifica células vazias em qualquer coluna do CSV.
Detecta linhas duplicadas, permitindo que o usuário limpe os dados de forma eficiente.
Estatísticas para colunas numéricas
Calcula o maior e menor valor.
Calcula média, mediana e moda.
Calcula desvio padrão e conta o número de valores únicos.

4 - Gráficos
Gera gráficos para colunas numéricas e categóricas.
Ajuda na análise visual e na identificação de padrões nos dados.
Validação de dados
Percorre todas as linhas do CSV e valida os registros.
Exibe erros encontrados e permite baixar um CSV com os dados validados.

5- Como usar
Executar o projeto com Streamlit.
Fazer upload do arquivo CSV.
Visualizar informações detalhadas sobre os dados, incluindo:

Tipos das colunas

Valores distintos

Valores em branco e duplicados

Estatísticas das colunas numéricas

Gráficos

Conferir erros de validação, se houver, e baixar o CSV validado.

6 - Estrutura do Projeto
app.py → Arquivo principal da aplicação Streamlit
Etl.py → Funções de análise, cálculo de estatísticas e validação de dados
graficos.py → Funções para geração de gráficos
requirements.txt → Lista de dependências necessárias para executar o projeto
