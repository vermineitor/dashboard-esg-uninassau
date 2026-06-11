import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Configuração da página para ocupar a tela inteira (Wide)
st.set_page_config(page_title="Dashboard de Governança - ESG", layout="wide")

# Estilização CSS para imitar as cores e bordas da imagem
st.markdown("""
    <style>
    .metric-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-top: 5px solid #1E3A8A;
        margin-bottom: 15px;
    }
    .title-dash {
        color: #0F172A;
        font-weight: bold;
        margin-bottom: 0px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR (MENU LATERAL) -----------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3248/3248149.png", width=70)
    st.subheader("ESG INDÚSTRIA")
    st.markdown("---")
    st.button("🏠 Visão Geral", use_container_width=True)
    st.button("🎯 BSC ESG", use_container_width=True)
    st.button("📊 KPIs", use_container_width=True)
    st.button("🔌 API REST", use_container_width=True)
    st.button("🗄️ Banco de Dados", use_container_width=True)
    st.button("📄 Relatórios", use_container_width=True)
    st.markdown("---")
    st.info("🌱 **Compromisso ESG**\nGerando valor sustentável para negócios, pessoas e o planeta.")

# ----------------- TOPO DO DASHBOARD -----------------
st.markdown("<h1 class='title-dash'>Dashboard de Governança – Exemplo 3: Sustentabilidade e ESG na Indústria</h1>", unsafe_allow_html=True)
st.caption("Monitoramento estratégico com Balanced Scorecard (BSC) e indicadores ESG")

# Filtros superiores
c_filt1, c_filt2, c_filt3, c_filt4 = st.columns([2, 2, 2, 1])
with c_filt1:
    st.selectbox("Período", ["01/01/2024 – 31/12/2024"])
with c_filt2:
    st.selectbox("Unidade Industrial", ["Todas as Unidades"])
with c_filt3:
    st.selectbox("Status", ["Todos"])
with c_filt4:
    st.write("")
    st.write("")
    st.button("🔄 Atualizar", use_container_width=True)

st.markdown("---")

# ----------------- BLOCO 1: CARDS DO BSC (4 COLUNAS) -----------------
card1, card2, card3, card4 = st.columns(4)

with card1:
    st.markdown("""
    <div style='background-color: #F0FDF4; padding: 15px; border-radius: 10px; border-left: 5px solid #16A34A;'>
        <span style='color: #16A34A; font-weight: bold;'>💲 Financeira</span><br>
        <small style='color: #64748B;'>Objetivo: Reduzir custos operacionais sustentáveis</small><br><br>
        <small>KPI: Economia de energia</small>
        <h2 style='color: #16A34A; margin: 0;'>14.8% <span style='font-size: 14px; color: #64748B;'>Meta >= 12%</span></h2>
        <span style='color: #16A34A; font-size: 12px;'>📈 Tendência: Positiva</span>
    </div>
    """, unsafe_allow_html=True)

with card2:
    st.markdown("""
    <div style='background-color: #EFF6FF; padding: 15px; border-radius: 10px; border-left: 5px solid #2563EB;'>
        <span style='color: #2563EB; font-weight: bold;'>👥 Cliente</span><br>
        <small style='color: #64748B;'>Objetivo: Elevar a perception ESG da marca</small><br><br>
        <small>KPI: Índice de reputação / satisfação</small>
        <h2 style='color: #2563EB; margin: 0;'>81% <span style='font-size: 14px; color: #64748B;'>Meta >= 75%</span></h2>
        <span style='color: #2563EB; font-size: 12px;'>📈 Tendência: Positiva</span>
    </div>
    """, unsafe_allow_html=True)

with card3:
    st.markdown("""
    <div style='background-color: #F5F3FF; padding: 15px; border-radius: 10px; border-left: 5px solid #7C3AED;'>
        <span style='color: #7C3AED; font-weight: bold;'>⚙️ Processos</span><br>
        <small style='color: #64748B;'>Objetivo: Reduzir impacto ambiental e aumentar eficiência</small><br>
        <small style='font-size: 11px;'>KPIs: Emissões CO₂ (-18%) | Água (-11%) | Reciclagem (72%)</small>
        <p style='color: #7C3AED; margin: 5px 0 0 0; font-size: 12px; font-weight: bold;'>Metas: -15%, -10%, >= 70%</p>
        <span style='color: #7C3AED; font-size: 12px;'>📈 Tendência: Positiva</span>
    </div>
    """, unsafe_allow_html=True)

with card4:
    st.markdown("""
    <div style='background-color: #F0FDF4; padding: 15px; border-radius: 10px; border-left: 5px solid #16A34A;'>
        <span style='color: #16A34A; font-weight: bold;'>🎓 Aprendizado</span><br>
        <small style='color: #64748B;'>Objetivo: Capacitar pessoas e estimular inovação verde</small><br><br>
        <small>KPI: % colaboradores treinados em ESG</small>
        <h2 style='color: #16A34A; margin: 0;'>93% <span style='font-size: 14px; color: #64748B;'>Meta >= 90%