import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

def graficos_numericos(df, max_graficos=1):
    for col in df.select_dtypes(include="number").columns:
        plt.figure(figsize=(6,4))
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribuição de {col}")
        st.pyplot(plt.gcf()) 
        plt.show()

def graficos_categoricos(df, max_graficos=1):
    for col in df.select_dtypes(include="object").columns:
        plt.figure(figsize=(6,4))
        df[col].value_counts().plot(kind="bar")
        plt.title(f"Frequência de {col}")
        st.pyplot(plt.gcf()) 
        st.pyplot(plt)  
