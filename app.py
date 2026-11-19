import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

path="acidentes.xlsx"
bruto = pd.read_excel(path, header=0)   

formatacao_total = bruto.iloc[0:3339, 3:4].copy()
formatacao_total = formatacao_total.reset_index(drop=True)
formatacao_total.columns = [
    "dia_semana"
]

formatacao_dias = (
    bruto.groupby(["dia_semana"], as_index=False)
    .agg(
        total_acidentes=("dia_semana", "count")
    )
)
formatacao_dias = formatacao_dias.sort_values(by="total_acidentes", ascending=False)
formatacao_dias = formatacao_dias.reset_index(drop=True)

st.title("Prova Final 3A2")
st.header("Acidentes em BH por dias da semana")
st.sidebar.title("Filtros de Análise")
add_selectbox = st.sidebar.selectbox(
    "Qual estilo deseja visualizar?",
    ("Tabela", "Gráfico")
)

if add_selectbox == "Tabela":
    st.subheader("Visualização por tabela")
    st.write(formatacao_dias)
elif add_selectbox == "Gráfico":
    st.subheader("Visualização por gráfico")
    fig = px.bar(
        formatacao_dias, 
        x='dia_semana', y='total_acidentes', 
        color='total_acidentes',
        barmode='group',
        orientation='v',
        color_continuous_scale='Viridis',
        title="Quantidades de acidente por dia da semana"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.subheader("Nenhuma opção selecionada")