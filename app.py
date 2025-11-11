import streamlit as st
import pandas as pd
from faker import Faker
import random

fake = Faker("pt_BR")

st.title("Gerador de Dados")

area = st.selectbox(
    "Selecione a área de dados que deseja gerar:", ['Vendas', 'Saúde', 'RH'])

qtd = st.slider("Quantas linhas deseja gerar?", min_value=10, max_value=8000, step=10)

def gerar_dados(area, qtd):
    dados = []
    if area == 'Vendas':
        for _ in range(qtd):
           dados.append({
               "Data": fake.date_this_year(),
               "Produto": random.choice(['Camisa', 'Calça', 'Tênis', 'Boné', 'Jaqueta']),
               "Valor": round(random.uniform(50,500),2),
               "Pagamento":random.choice(["Cartão", "Dinheiro", "Pix"])
           })
    elif area == 'Saúde':
        for _ in range(qtd):
           dados.append({
               "Data_Consulta": fake.date_this_year(),
               "Paciente": fake.name(),
               "Especialidade": random.choice(["Clínico Geral", "Cardiologia", "Ortopedia"]),
               "Convenio": random.choice(["Particular", "Plano A", "Plano B", "SUS"]),
               "Valor":round(random.uniform(100,500),2)
           })
    elif area == 'RH':
        for _ in range(qtd):
           dados.append({
               "Data": fake.date_this_year(),
               "Produto": random.choice(['Camisa', 'Calça', 'Tênis', 'Boné', 'Jaqueta']),
               "Valor": round(random.uniform(50,500),2),
               "Pagamento":random.choice(["Cartão", "Dinheiro", "Pix"])
           })
