import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Configuração da página para ocupar a tela inteira (Wide) e o novo título na aba
st.set_page_config(page_title="TechSoft Dashboard - Mudanças de Sustentabilidade e ESG", layout="wide")

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

# ----------------- TOPO DO DASHBOARD (TÍTULO ALTERADO AQUI) -----------------
st.markdown("<h1 class='title-dash'>TechSoft Dashboard – Mudanças de Sustentabilidade e ESG</h1>", unsafe_allow_html=True)
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
        <h2 style='color: #16A34A; margin: 0;'>93% <span style='font-size: 14px; color: #64748B;'>Meta >= 90%</span></h2>
        <span style='color: #16A34A; font-size: 12px;'>📈 Tendência: Positiva</span>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ----------------- BLOCO 2: GRÁFICOS E CONFORMIDADE -----------------
col_g1, col_g2, col_g3 = st.columns([4, 4, 3])

with col_g1:
    st.subheader("Tendência Mensal de Emissões e Consumo")
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=meses, y=[2600, 2500, 2450, 2380, 2300, 2150, 2100, 2050, 2000, 1950, 1900, 1850],
                        mode='lines+markers', name='Emissões CO₂ (t)', line=dict(color='#16A34A', width=3)))
    fig_line.add_trace(go.Scatter(x=meses, y=[9500, 9000, 8500, 8200, 8000, 7500, 7100, 6800, 6500, 6200, 6000, 5800],
                        mode='lines+markers', name='Consumo de Água (m³)', yaxis='y2', line=dict(color='#2563EB', width=3)))
    
    fig_line.update_layout(
        yaxis=dict(title='Emissões CO₂ (t)'),
        yaxis2=dict(title='Consumo de Água (m³)', overlaying='y', side='right'),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=40, b=20), height=300
    )
    st.plotly_chart(fig_line, use_container_width=True)

with col_g2:
    st.subheader("Indicadores Operacionais")
    kpis_op = ['Energia', 'Água', 'Resíduos', 'Reciclagem']
    realizado = [14.8, 11, 18, 72]
    meta_op = [12, 10, 15, 70]
    
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(x=kpis_op, y=realizado, name='Realizado', marker_color='#16A34A'))
    fig_bar.add_trace(go.Bar(x=kpis_op, y=meta_op, name='Meta', marker_color='#93C5FD'))
    
    fig_bar.update_layout(
        barmode='group', height=300, margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col_g3:
    st.subheader("Conformidade ESG")
    fig_donut = go.Figure(go.Pie(labels=['Conforme', 'Restante'], values=[88, 12], hole=.7, showlegend=False, marker=dict(colors=['#16A34A', '#E2E8F0'])))
    fig_donut.update_traces(textinfo='none')
    fig_donut.update_layout(
        annotations=[dict(text='88%<br><span style="font-size:12px; color:gray;">Conformidade<br>ESG</span>', x=0.5, y=0.5, font_size=20, showarrow=False, align="center")],
        height=250, margin=dict(l=10, r=10, t=10, b=10)
    )
    st.plotly_chart(fig_donut, use_container_width=True)
    st.success("✅ Acima da meta (>= 80%)")

st.write("")

# ----------------- BLOCO 3: TABELA RESUMO BSC E ARQUITETURA -----------------
col_t1, col_t2 = st.columns([8, 3])

with col_t1:
    st.subheader("Balanced Scorecard ESG – Resumo Estratégico")
    df_bsc = pd.DataFrame({
        'Perspectiva': ['💲 Financeira', '👥 Cliente', '⚙️ Processos', '🎓 Aprendizado'],
        'Objetivo Estratégico': [
            'Reduzir custos operacionais sustentáveis',
            'Elevar a percepção ESG da marca',
            'Reduzir impacto ambiental e aumentar eficiência',
            'Capacitar pessoas e estimular inovação verde'
        ],
        'KPI (indicador)': [
            'Economia de energia',
            'Índice de reputação / satisfação',
            'Emissões CO₂, Consumo de água, Taxa de reciclagem',
            '% colaboradores treinados em ESG'
        ],
        'Meta': ['>= 12%', '>= 75%', '-15%, -10%, >= 70%', '>= 90%']
    })
    st.dataframe(df_bsc, use_container_width=True, hide_index=True)

with col_t2:
    st.subheader("Arquitetura da Solução")
    st.markdown("""
    * 💻 **Front-end:** Streamlit
    * 🌐 **API:** FastAPI
    * 🗄️ **Banco:** SQLite / PostgreSQL
    * 🔌 **Integração:** REST
    """)
