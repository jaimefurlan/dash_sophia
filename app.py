import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from supabase import create_client, Client
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import requests
from google.cloud import monitoring_v3
import numpy as np
import random
from plotly.subplots import make_subplots

# Configuração da página
st.set_page_config(
    page_title="Dashboard SophIA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregar estilos CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do Supabase
@st.cache_resource
def init_supabase():
    try:
        supabase_url = st.secrets["supabase"]["url"]
        supabase_key = st.secrets["supabase"]["key"]
        
        if not supabase_url or not supabase_key:
            st.error("Credenciais do Supabase não encontradas. Verifique as configurações no Streamlit Cloud.")
            return None
            
        return create_client(supabase_url, supabase_key)
    except Exception as e:
        st.error(f"Erro ao inicializar Supabase: {str(e)}")
        return None

supabase = init_supabase()

# Configuração do tema Plotly
plotly_template = dict(
    layout=dict(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="Inter, system-ui, -apple-system, sans-serif",
            color="#1e293b"
        ),
        margin=dict(t=30, l=30, r=30, b=30),
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(226, 232, 240, 0.5)',
            zeroline=False,
            showline=True,
            linecolor='#e2e8f0',
            tickfont=dict(size=12)
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(226, 232, 240, 0.5)',
            zeroline=False,
            showline=True,
            linecolor='#e2e8f0',
            tickfont=dict(size=12)
        ),
        colorway=['#2563eb', '#3b82f6', '#60a5fa', '#93c5fd', '#bfdbfe'],
        hovermode='x unified',
        hoverlabel=dict(
            bgcolor='white',
            font_size=12,
            font_family="Inter, system-ui, -apple-system, sans-serif"
        )
    )
)

# Função para criar indicadores
def create_indicator(value, title, delta=None):
    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode="number+delta" if delta else "number",
        value=value,
        delta=dict(
            reference=delta,
            valueformat=".1%"
        ) if delta else None,
        title=dict(
            text=title,
            font=dict(size=14, color='#64748b')
        ),
        number=dict(
            font=dict(size=24, color='#1e293b'),
            valueformat=".1f"
        )
    ))
    fig.update_layout(
        template=plotly_template,
        height=120,
        margin=dict(t=30, l=30, r=30, b=30)
    )
    return fig

# Função para carregar dados
@st.cache_data(ttl=300)
def load_data():
    try:
        response = supabase.table('sophia_dashboard').select("*").execute()
        df = pd.DataFrame(response.data)
        
        if 'data' in df.columns:
            df['data'] = pd.to_datetime(df['data'])
        
        colunas_numericas = [
            'precisao', 'taxa_erro', 'nps', 'sessoes_chat',
            'velocidade_processamento', 'latencia', 'duracao_sessao',
            'consultas_por_sessao'
        ]
        
        for col in colunas_numericas:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {str(e)}")
        return pd.DataFrame()

# Carregar dados
df = load_data()

# Sidebar com menu
with st.sidebar:
    # Título
    st.markdown("### Dashboard SophIA")
    
    # Menu principal
    selected = option_menu(
        menu_title=None,
        options=["IA", "Cobrança", "Vendas", "SAC", "WhatsApp", "APIs Públicas", "HELP"],
        icons=["robot", "currency-dollar", "cart", "headset", "whatsapp", "globe2", "book"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "transparent",
                "margin": "0!important",
                "box-shadow": "none",
                "border": "none"
            },
            "icon": {
                "color": "var(--primary-color)",
                "font-size": "16px"
            },
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "4px 0",
                "padding": "8px 16px",
                "--hover-color": "var(--hover-bg)",
                "background-color": "transparent",
                "box-shadow": "none",
                "border": "none",
                "border-radius": "8px"
            },
            "nav-link-selected": {
                "background-color": "var(--primary-color)",
                "color": "white",
                "box-shadow": "none",
                "border": "none"
            }
        }
    )

# Filtros na parte superior
st.markdown("### Filtros")
col1, col2, col3, col4 = st.columns([2, 2, 2, 1])

with col1:
    data_inicio = st.date_input(
        "Data Inicial",
        datetime.now() - timedelta(days=7),
        format="DD/MM/YYYY"
    )

with col2:
    data_fim = st.date_input(
        "Data Final",
        datetime.now(),
        format="DD/MM/YYYY"
    )

with col3:
    hora = st.selectbox(
        "Hora",
        range(0, 24),
        format_func=lambda x: f"{x:02d}:00"
    )

with col4:
    campanha = st.text_input("Campanha")

def format_compact_number(n):
    if abs(n) >= 1_000_000_000:
        return f"{n/1_000_000_000:.2f}B"
    elif abs(n) >= 1_000_000:
        return f"{n/1_000_000:.2f}M"
    elif abs(n) >= 1_000:
        return f"{n/1_000:.2f}K"
    else:
        return f"{n:.0f}"

# Conteúdo principal baseado na seleção do menu
if selected == "HELP":
    st.title("📚 Ajuda e Documentação")
    with open("README.txt", "r") as f:
        help_content = f.read()
        st.markdown(help_content)
elif selected == "IA":
    st.title("Dashboard de IA")
    st.write("Indicadores técnicos, de uso, qualidade, linguagem e negócio da IA.")

    # MOCK: Dados fictícios para visualização
    dias = pd.date_range(end=datetime.now(), periods=14)
    mock_ia = pd.DataFrame({
        "data": dias,
        "taxa_acerto": np.random.uniform(0.8, 0.95, len(dias)),
        "satisfacao": np.random.uniform(0.85, 0.98, len(dias)),
        "eficiencia": np.random.uniform(0.75, 0.9, len(dias)),
        "disponibilidade": np.random.uniform(0.9, 0.99, len(dias)),
        "tokens_sessao": np.random.randint(100, 1000, len(dias)),
        "latencia": np.random.uniform(200, 800, len(dias)),
        "respostas_corretas": np.random.uniform(0.8, 0.95, len(dias)),
        "fallback": np.random.uniform(0.01, 0.2, len(dias)),
        "score_empatia": np.random.uniform(3, 5, len(dias)),
        "csat": np.random.uniform(3, 5, len(dias)),
        "nps": np.random.randint(-100, 100, len(dias)),
        "elogios": np.random.uniform(0, 0.1, len(dias)),
        "tempo_sessao": np.random.uniform(2, 20, len(dias)),
        "sessoes_dia": np.random.randint(50, 200, len(dias)),
        "custo_ia": np.random.uniform(100, 500, len(dias)),
        "horas_ativas": np.random.uniform(8, 24, len(dias)),
    })

    # 1. Métricas de Performance e Qualidade
    st.header("Métricas de Performance e Qualidade")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.metric("Taxa de Acerto (%)", f"{100*mock_ia['taxa_acerto'].mean():.1f}%")
    with col2:
        st.metric("Satisfação (%)", f"{100*mock_ia['satisfacao'].mean():.1f}%")
    with col3:
        st.metric("Eficiência (%)", f"{100*mock_ia['eficiencia'].mean():.1f}%")
    with col4:
        st.metric("Disponibilidade (%)", f"{100*mock_ia['disponibilidade'].mean():.1f}%")
    with col5:
        st.metric("Tokens/sessão", format_compact_number(mock_ia['tokens_sessao'].mean()))
    with col6:
        st.metric("Latência (ms)", f"{mock_ia['latencia'].mean():.0f}")
    st.plotly_chart(px.line(mock_ia, x="data", y="taxa_acerto", title="Taxa de Acerto (%)"), use_container_width=True)

    # 2. Métricas de Qualidade da Resposta
    st.header("Métricas de Qualidade da Resposta")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Respostas Corretas (%)", f"{100*mock_ia['respostas_corretas'].mean():.1f}%")
    with col2:
        st.metric("Fallback (%)", f"{100*mock_ia['fallback'].mean():.1f}%")
    with col3:
        st.metric("Empatia/Naturalidade", f"{mock_ia['score_empatia'].mean():.2f}")
    with col4:
        st.metric("CSAT", f"{mock_ia['csat'].mean():.2f}")
    with col5:
        st.metric("NPS", int(mock_ia["nps"].mean()))
    st.plotly_chart(px.line(mock_ia, x="data", y="respostas_corretas", title="Taxa de Respostas Corretas (%)"), use_container_width=True)

    # 3. Métricas de Engajamento
    st.header("Métricas de Engajamento")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Elogios (%)", f"{100*mock_ia['elogios'].mean():.2f}%")
    with col2:
        st.metric("Tempo Médio Sessão", f"{mock_ia['tempo_sessao'].mean():.1f}")
    with col3:
        st.metric("Sessões/Dia", format_compact_number(mock_ia['sessoes_dia'].mean()))
    with col4:
        st.metric("Horas Ativas", f"{mock_ia['horas_ativas'].mean():.1f}")
    st.plotly_chart(px.line(mock_ia, x="data", y="sessoes_dia", title="Total de Sessões por Dia"), use_container_width=True)

    # KPIs executivos
    st.header("KPIs Executivos")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        custo_sessao = mock_ia["custo_ia"].sum() / max(1, mock_ia["sessoes_dia"].sum())
        st.metric(label="Custo por Sessão (R$)", value=format_compact_number(custo_sessao))
    with col2:
        st.metric("CSAT Médio", f"{mock_ia['csat'].mean():.2f}")
    with col3:
        st.metric("NPS", int(mock_ia["nps"].mean()))
    with col4:
        st.metric("Disponibilidade (%)", f"{100*mock_ia['disponibilidade'].mean():.1f}%")
    with col5:
        st.metric("Eficiência (%)", f"{100*mock_ia['eficiencia'].mean():.1f}%")

    # Mapa de distribuição geográfica
    st.header("Distribuição Geográfica dos Usuários")
    
    # Dados mockados de DDDs e estados
    ddd_data = {
        'DDD': [11, 21, 31, 41, 51, 61, 71, 81, 91, 27, 47, 19, 85, 83, 63],
        'Estado': ['SP', 'RJ', 'MG', 'PR', 'RS', 'DF', 'BA', 'PE', 'PA', 'ES', 'SC', 'SP', 'CE', 'PB', 'TO'],
        'Usuários': np.random.randint(100, 1000, 15),
        'Latitude': [-23.5505, -22.9068, -19.9167, -25.4289, -30.0346, -15.7801, -12.9714, -8.0476, -1.4557, -20.2976, -27.5969, -22.9071, -3.7319, -7.1150, -10.1674],
        'Longitude': [-46.6333, -43.1729, -43.9345, -49.2671, -51.2177, -47.9292, -38.5014, -34.8770, -48.4902, -40.2958, -48.5495, -43.0632, -38.5267, -34.8631, -48.3317]
    }
    
    df_ddd = pd.DataFrame(ddd_data)
    
    # Criar o mapa
    fig = px.scatter_mapbox(
        df_ddd,
        lat='Latitude',
        lon='Longitude',
        size='Usuários',
        color='Usuários',
        hover_name='Estado',
        hover_data={
            'DDD': True,
            'Usuários': True,
            'Latitude': False,
            'Longitude': False
        },
        color_continuous_scale=px.colors.sequential.Blues,
        size_max=30,
        zoom=3,
        center=dict(lat=-15.7801, lon=-47.9292),  # Centro do Brasil
        mapbox_style="carto-positron",
        title="Distribuição de Usuários por DDD"
    )
    
    fig.update_layout(
        margin=dict(l=0, r=0, t=30, b=0),
        height=600,
        mapbox=dict(
            center=dict(lat=-15.7801, lon=-47.9292),
            zoom=3
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabela com dados detalhados
    st.subheader("Detalhamento por DDD")
    df_ddd_display = df_ddd.sort_values('Usuários', ascending=False)
    df_ddd_display = df_ddd_display[['DDD', 'Estado', 'Usuários']]
    df_ddd_display['Usuários'] = df_ddd_display['Usuários'].apply(lambda x: format_compact_number(x))
    st.dataframe(df_ddd_display, use_container_width=True)

elif selected == "Cobrança":
    st.title("Dashboard de Cobrança - IA")
    st.write("Indicadores financeiros, de engajamento, qualidade, custo e recorrência do canal automatizado.")

    # MOCK: Dados fictícios para visualização
    dias = pd.date_range(end=datetime.now(), periods=14)
    mock_cobranca = pd.DataFrame({
        "data": dias,
        "valor_negociado": np.random.uniform(10000, 50000, len(dias)),
        "acordos_fechados": np.random.randint(10, 100, len(dias)),
        "ticket_medio": np.random.uniform(500, 2000, len(dias)),
        "acordos_pagos": np.random.randint(5, 80, len(dias)),
        "carteira_acionada": np.random.uniform(50000, 200000, len(dias)),
        "valor_recuperado_sessao": np.random.uniform(50, 500, len(dias)),
        "abertura_primeiro_contato": np.random.uniform(0.5, 0.95, len(dias)),
        "resposta_primeiro_contato": np.random.uniform(0.3, 0.8, len(dias)),
        "entrada_negociacao": np.random.uniform(0.2, 0.7, len(dias)),
        "conclusao_negociacao": np.random.uniform(0.1, 0.6, len(dias)),
        "abandono_fluxo": np.random.uniform(0.05, 0.3, len(dias)),
        "tempo_decisao": np.random.uniform(2, 30, len(dias)),
        "acerto_proposta": np.random.uniform(0.7, 1.0, len(dias)),
        "sem_intervencao": np.random.uniform(0.7, 1.0, len(dias)),
        "nps": np.random.randint(-100, 100, len(dias)),
        "taxa_erros": np.random.uniform(0, 0.05, len(dias)),
        "comprimento_sessao": np.random.uniform(5, 30, len(dias)),
        "custo_sessao": np.random.uniform(0.5, 2.0, len(dias)),
        "custo_acordo": np.random.uniform(10, 50, len(dias)),
        "custo_callcenter": np.random.uniform(30, 80, len(dias)),
        "retentativa": np.random.randint(0, 10, len(dias)),
        "reengajamento": np.random.randint(0, 15, len(dias)),
        "renegociacoes": np.random.randint(0, 8, len(dias)),
        "sessoes_iniciadas": np.random.randint(50, 200, len(dias)),
        "custo_ia": np.random.uniform(100, 500, len(dias)),
    })

    # 1. Métricas de Conversão e Resultado Financeiro
    st.header("Métricas de Conversão e Resultado Financeiro")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.metric(label="Valor negociado total (R$)", value=format_compact_number(mock_cobranca['valor_negociado'].sum()))
    with col2:
        st.metric(label="Acordos fechados", value=format_compact_number(mock_cobranca["acordos_fechados"].sum()))
    with col3:
        st.metric(label="Ticket médio (R$)", value=format_compact_number(mock_cobranca['ticket_medio'].mean()))
    with col4:
        pct_pagos = 100 * mock_cobranca["acordos_pagos"].sum() / max(1, mock_cobranca["acordos_fechados"].sum())
        st.metric("% acordos pagos", f"{pct_pagos:.1f}%")
    with col5:
        pct_recup = 100 * mock_cobranca["valor_negociado"].sum() / max(1, mock_cobranca["carteira_acionada"].sum())
        st.metric("% recuperação carteira", f"{pct_recup:.1f}%")
    with col6:
        st.metric(label="Valor recup./sessão (R$)", value=format_compact_number(mock_cobranca['valor_recuperado_sessao'].mean()))
    st.plotly_chart(px.line(mock_cobranca, x="data", y="valor_negociado", title="Valor negociado total (R$)"), use_container_width=True)

    # 2. Métricas de Engajamento e Funil de Conversão
    st.header("Métricas de Engajamento e Funil de Conversão")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.metric("Abertura 1º contato (%)", f"{100*mock_cobranca['abertura_primeiro_contato'].mean():.1f}%")
    with col2:
        st.metric("Resp. 1º contato (%)", f"{100*mock_cobranca['resposta_primeiro_contato'].mean():.1f}%")
    with col3:
        st.metric("Entrada negociação (%)", f"{100*mock_cobranca['entrada_negociacao'].mean():.1f}%")
    with col4:
        st.metric("Conclusão negociação (%)", f"{100*mock_cobranca['conclusao_negociacao'].mean():.1f}%")
    with col5:
        st.metric("Abandono fluxo (%)", f"{100*mock_cobranca['abandono_fluxo'].mean():.1f}%")
    with col6:
        st.metric("Tempo até decisão (min)", f"{mock_cobranca['tempo_decisao'].mean():.1f}")
    st.plotly_chart(px.line(mock_cobranca, x="data", y="abertura_primeiro_contato", title="Taxa de abertura do 1º contato"), use_container_width=True)

    # 3. Métricas de Qualidade da IA e Conversação
    st.header("Métricas de Qualidade da IA e Conversação")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Acerto proposta (%)", f"{100*mock_cobranca['acerto_proposta'].mean():.1f}%")
    with col2:
        st.metric("% sem intervenção humana", f"{100*mock_cobranca['sem_intervencao'].mean():.1f}%")
    with col3:
        st.metric("NPS/CSAT", int(mock_cobranca["nps"].mean()))
    with col4:
        st.metric("Taxa erros conversa (%)", f"{100*mock_cobranca['taxa_erros'].mean():.2f}%")
    with col5:
        st.metric("Comp. média sessão", f"{mock_cobranca['comprimento_sessao'].mean():.1f}")
    st.plotly_chart(px.line(mock_cobranca, x="data", y="acerto_proposta", title="Taxa de acerto na proposta"), use_container_width=True)

    # 4. Métricas Operacionais e de Custo
    st.header("Métricas Operacionais e de Custo")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Custo por sessão (R$)", value=format_compact_number(mock_cobranca['custo_sessao'].mean()))
    with col2:
        st.metric(label="CAC (R$)", value=format_compact_number(mock_cobranca['custo_acordo'].mean()))
    with col3:
        st.metric(label="Call center (R$/acordo)", value=format_compact_number(mock_cobranca['custo_callcenter'].mean()))
    st.plotly_chart(px.line(mock_cobranca, x="data", y="custo_sessao", title="Custo por sessão (R$)"), use_container_width=True)

    # 5. Métricas de Recorrência e Pós-Venda
    st.header("Métricas de Recorrência e Pós-Venda")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Retentativa clientes", int(mock_cobranca["retentativa"].sum()))
    with col2:
        st.metric("Reengajamento pós-lembrete", int(mock_cobranca["reengajamento"].sum()))
    with col3:
        st.metric("Renegociações IA", int(mock_cobranca["renegociacoes"].sum()))
    st.plotly_chart(px.line(mock_cobranca, x="data", y="renegociacoes", title="Renegociações por dia"), use_container_width=True)

    # KPIs executivos
    st.header("KPIs Executivos")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        conv_bruta = 100 * mock_cobranca["acordos_fechados"].sum() / max(1, mock_cobranca["sessoes_iniciadas"].sum())
        st.metric("Conversão bruta (%)", f"{conv_bruta:.1f}%")
    with col2:
        conv_liquida = 100 * mock_cobranca["acordos_pagos"].sum() / max(1, mock_cobranca["sessoes_iniciadas"].sum())
        st.metric("Conversão líquida (%)", f"{conv_liquida:.1f}%")
    with col3:
        roi = 100 * (mock_cobranca["valor_negociado"].sum() - mock_cobranca["custo_ia"].sum()) / max(1, mock_cobranca["custo_ia"].sum())
        st.metric("ROI canal IA (%)", f"{roi:.1f}%")
    with col4:
        tempo_conv = mock_cobranca["tempo_decisao"].sum() / max(1, mock_cobranca["acordos_fechados"].sum())
        st.metric("Tempo médio conversão (min)", f"{tempo_conv:.1f}")
    with col5:
        st.metric("NPS", int(mock_cobranca["nps"].mean()))

elif selected == "Vendas":
    st.title("Dashboard de Vendas - IA")
    st.write("Indicadores comerciais, funil, performance, satisfação, recorrência e KPIs executivos do chatbot de vendas.")

    # MOCK: Dados fictícios para visualização
    dias = pd.date_range(end=datetime.now(), periods=14)
    mock_vendas = pd.DataFrame({
        "data": dias,
        "vendas_realizadas": np.random.randint(5, 50, len(dias)),
        "valor_total_vendas": np.random.uniform(5000, 30000, len(dias)),
        "ticket_medio": np.random.uniform(200, 1500, len(dias)),
        "conversao_sessao": np.random.uniform(0.05, 0.4, len(dias)),
        "conversao_lead": np.random.uniform(0.01, 0.2, len(dias)),
        "cac": np.random.uniform(10, 80, len(dias)),
        "tempo_fechamento": np.random.uniform(2, 30, len(dias)),
        "qualif_leads": np.random.uniform(0.2, 0.8, len(dias)),
        "abandono_funil": np.random.uniform(0.05, 0.3, len(dias)),
        "agendamento_reuniao": np.random.uniform(0.01, 0.2, len(dias)),
        "cliques_oferta": np.random.uniform(0.05, 0.5, len(dias)),
        "leads_retorno": np.random.uniform(0.01, 0.2, len(dias)),
        "latencia_resposta": np.random.uniform(200, 800, len(dias)),
        "interacoes_sessao": np.random.randint(2, 20, len(dias)),
        "finalizacao_auto": np.random.uniform(0.5, 1.0, len(dias)),
        "fallback": np.random.uniform(0.01, 0.2, len(dias)),
        "score_empatia": np.random.uniform(3, 5, len(dias)),
        "csat": np.random.uniform(3, 5, len(dias)),
        "nps": np.random.randint(-100, 100, len(dias)),
        "elogios": np.random.uniform(0, 0.1, len(dias)),
        "tempo_sessao": np.random.uniform(2, 20, len(dias)),
        "retorno_nova_compra": np.random.uniform(0.01, 0.2, len(dias)),
        "upsell_cross": np.random.uniform(0.01, 0.2, len(dias)),
        "recompra_mes": np.random.uniform(0.01, 0.2, len(dias)),
        "leads_totais": np.random.randint(20, 100, len(dias)),
        "custo_ia": np.random.uniform(100, 500, len(dias)),
        "vendas_sem_humano": np.random.uniform(0.5, 1.0, len(dias)),
        "horas_ativas": np.random.uniform(8, 24, len(dias)),
    })

    # 1. Métricas de Conversão e Resultado Comercial
    st.header("Métricas de Conversão e Resultado Comercial")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col1:
        st.metric(label="Vendas realizadas", value=format_compact_number(mock_vendas["vendas_realizadas"].sum()))
    with col2:
        st.metric(label="Valor total vendas (R$)", value=format_compact_number(mock_vendas['valor_total_vendas'].sum()))
    with col3:
        st.metric(label="Ticket médio (R$)", value=format_compact_number(mock_vendas['ticket_medio'].mean()))
    with col4:
        taxa_conv_sessao = 100 * mock_vendas["conversao_sessao"].mean()
        st.metric("Conversão/sessão (%)", f"{taxa_conv_sessao:.1f}%")
    with col5:
        taxa_conv_lead = 100 * mock_vendas["conversao_lead"].mean()
        st.metric("Conversão/lead (%)", f"{taxa_conv_lead:.1f}%")
    with col6:
        st.metric(label="CAC (R$)", value=format_compact_number(mock_vendas['cac'].mean()))
    with col7:
        st.metric("Tempo médio fechamento (min)", f"{mock_vendas['tempo_fechamento'].mean():.1f}")
    st.plotly_chart(px.line(mock_vendas, x="data", y="valor_total_vendas", title="Valor total em vendas (R$)"), use_container_width=True)

    # 2. Métricas de Funil de Vendas
    st.header("Métricas de Funil de Vendas (pipeline)")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.metric("Qualif. leads (%)", f"{100*mock_vendas['qualif_leads'].mean():.1f}%")
    with col2:
        st.metric("Abandono funil (%)", f"{100*mock_vendas['abandono_funil'].mean():.1f}%")
    with col3:
        st.metric("Agend. reunião (%)", f"{100*mock_vendas['agendamento_reuniao'].mean():.1f}%")
    with col4:
        st.metric("Cliques oferta (%)", f"{100*mock_vendas['cliques_oferta'].mean():.1f}%")
    with col5:
        st.metric("Leads 2ª sessão (%)", f"{100*mock_vendas['leads_retorno'].mean():.1f}%")
    with col6:
        st.metric("Leads totais", int(mock_vendas["leads_totais"].sum()))
    st.plotly_chart(px.line(mock_vendas, x="data", y="qualif_leads", title="Taxa de qualificação de leads (%)"), use_container_width=True)

    # 3. Métricas de Performance do Chatbot
    st.header("Métricas de Performance do Chatbot")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Latência resp. (ms)", f"{mock_vendas['latencia_resposta'].mean():.0f}")
    with col2:
        st.metric("Interações/sessão", int(mock_vendas["interacoes_sessao"].mean()))
    with col3:
        st.metric("Finalização auto. (%)", f"{100*mock_vendas['finalizacao_auto'].mean():.1f}%")
    with col4:
        st.metric("Fallback (%)", f"{100*mock_vendas['fallback'].mean():.1f}%")
    with col5:
        st.metric("Empatia/naturalidade", f"{mock_vendas['score_empatia'].mean():.2f}")
    st.plotly_chart(px.line(mock_vendas, x="data", y="latencia_resposta", title="Latência média de resposta (ms)"), use_container_width=True)

    # 4. Métricas de Qualidade e Satisfação do Cliente
    st.header("Métricas de Qualidade e Satisfação do Cliente")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("CSAT", f"{mock_vendas['csat'].mean():.2f}")
    with col2:
        st.metric("NPS IA", int(mock_vendas["nps"].mean()))
    with col3:
        st.metric("Elogios (%)", f"{100*mock_vendas['elogios'].mean():.2f}%")
    with col4:
        st.metric("Tempo médio sessão", f"{mock_vendas['tempo_sessao'].mean():.1f}")
    st.plotly_chart(px.line(mock_vendas, x="data", y="csat", title="CSAT (Customer Satisfaction Score)"), use_container_width=True)

    # 5. Métricas de Retenção e Recorrência
    st.header("Métricas de Retenção e Recorrência")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Retorno nova compra (%)", f"{100*mock_vendas['retorno_nova_compra'].mean():.1f}%")
    with col2:
        st.metric("Up-sell/cross-sell (%)", f"{100*mock_vendas['upsell_cross'].mean():.1f}%")
    with col3:
        st.metric("Recompra no mês (%)", f"{100*mock_vendas['recompra_mes'].mean():.1f}%")
    st.plotly_chart(px.line(mock_vendas, x="data", y="retorno_nova_compra", title="Taxa de retorno para nova compra (%)"), use_container_width=True)

    # KPIs executivos
    st.header("KPIs Executivos")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        conv_lead = 100 * mock_vendas["vendas_realizadas"].sum() / max(1, mock_vendas["leads_totais"].sum())
        st.metric("Conversão por lead (%)", f"{conv_lead:.1f}%")
    with col2:
        cac_ia = (mock_vendas["custo_ia"].sum()) / max(1, mock_vendas["vendas_realizadas"].sum())
        st.metric(label="CAC via IA (R$)", value=format_compact_number(cac_ia))
    with col3:
        vendas_hora = mock_vendas["vendas_realizadas"].sum() / max(1, mock_vendas["horas_ativas"].sum())
        st.metric("Vendas por hora", f"{vendas_hora:.2f}")
    with col4:
        vendas_sem_humano = 100 * mock_vendas["vendas_sem_humano"].mean()
        st.metric("Vendas sem humano (%)", f"{vendas_sem_humano:.1f}%")
    with col5:
        st.metric("NPS IA", int(mock_vendas["nps"].mean()))

elif selected == "SAC":
    st.title("Dashboard SAC - Atendimento Automatizado")
    st.write("Indicadores de resolução, qualidade, operação, satisfação e volume do chatbot de atendimento.")

    # MOCK: Dados fictícios para visualização
    dias = pd.date_range(end=datetime.now(), periods=14)
    mock_sac = pd.DataFrame({
        "data": dias,
        "resolucao_primeira": np.random.uniform(0.5, 0.95, len(dias)),
        "resolucao_sem_transfer": np.random.uniform(0.4, 0.9, len(dias)),
        "transfer_humano": np.random.uniform(0.05, 0.3, len(dias)),
        "reabertura": np.random.uniform(0.01, 0.15, len(dias)),
        "chamados_resolvidos": np.random.randint(10, 100, len(dias)),
        "score_relevancia": np.random.uniform(3, 5, len(dias)),
        "respostas_incorretas": np.random.uniform(0, 0.05, len(dias)),
        "loops": np.random.uniform(0, 0.03, len(dias)),
        "score_clareza": np.random.uniform(3, 5, len(dias)),
        "latencia": np.random.uniform(200, 800, len(dias)),
        "falhas_tecnicas": np.random.uniform(0, 0.02, len(dias)),
        "tempo_atendimento": np.random.uniform(2, 15, len(dias)),
        "tokens_sessao": np.random.randint(100, 1000, len(dias)),
        "tokens_resposta": np.random.randint(10, 100, len(dias)),
        "csat": np.random.uniform(3, 5, len(dias)),
        "nps": np.random.randint(-100, 100, len(dias)),
        "feedback_positivo": np.random.uniform(0.5, 0.95, len(dias)),
        "reclamacoes": np.random.uniform(0, 0.05, len(dias)),
        "sessoes_dia": np.random.randint(50, 200, len(dias)),
        "sessoes_mes": np.random.randint(1000, 5000, len(dias)),
        "sessoes_simultaneas": np.random.randint(1, 20, len(dias)),
        "hora": [d.hour for d in dias],
        "sessoes_whatsapp": np.random.randint(10, 100, len(dias)),
        "sessoes_web": np.random.randint(10, 100, len(dias)),
        "sla": np.random.uniform(0.7, 0.99, len(dias)),
        "economia": np.random.uniform(1000, 10000, len(dias)),
    })

    # 1. Métricas de Resolução e Efetividade
    st.header("Métricas de Resolução e Efetividade")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Resolução 1ª interação (%)", f"{100*mock_sac['resolucao_primeira'].mean():.1f}%")
    with col2:
        st.metric("Resolução sem transferência (%)", f"{100*mock_sac['resolucao_sem_transfer'].mean():.1f}%")
    with col3:
        st.metric("Transferências para humano (%)", f"{100*mock_sac['transfer_humano'].mean():.1f}%")
    with col4:
        st.metric("Reabertura chamado (%)", f"{100*mock_sac['reabertura'].mean():.1f}%")
    with col5:
        st.metric("Chamados resolvidos/dia", format_compact_number(mock_sac['chamados_resolvidos'].mean()))
    st.plotly_chart(px.line(mock_sac, x="data", y="resolucao_primeira", title="Taxa de resolução na primeira interação (%)"), use_container_width=True)

    # 2. Métricas de Qualidade da Resposta
    st.header("Métricas de Qualidade da Resposta")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Score relevância", f"{mock_sac['score_relevancia'].mean():.2f}")
    with col2:
        st.metric("Respostas incorretas (%)", f"{100*mock_sac['respostas_incorretas'].mean():.2f}%")
    with col3:
        st.metric("Loops (%)", f"{100*mock_sac['loops'].mean():.2f}%")
    with col4:
        st.metric("Score clareza (1-5)", f"{mock_sac['score_clareza'].mean():.2f}")
    st.plotly_chart(px.line(mock_sac, x="data", y="score_relevancia", title="Score de relevância da resposta"), use_container_width=True)

    # 3. Métricas Técnicas e Operacionais
    st.header("Métricas Técnicas e Operacionais")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Latência média (ms)", f"{mock_sac['latencia'].mean():.0f}")
    with col2:
        st.metric("Falhas técnicas (%)", f"{100*mock_sac['falhas_tecnicas'].mean():.2f}%")
    with col3:
        st.metric("Tempo médio atendimento (min)", f"{mock_sac['tempo_atendimento'].mean():.1f}")
    with col4:
        st.metric("Tokens/sessão", format_compact_number(mock_sac['tokens_sessao'].mean()))
    st.plotly_chart(px.line(mock_sac, x="data", y="latencia", title="Latência média (ms)"), use_container_width=True)

    # 4. Métricas de Satisfação do Cliente (CX)
    st.header("Métricas de Satisfação do Cliente (CX)")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("CSAT", f"{mock_sac['csat'].mean():.2f}")
    with col2:
        st.metric("NPS IA", int(mock_sac['nps'].mean()))
    with col3:
        st.metric("Feedback positivo (%)", f"{100*mock_sac['feedback_positivo'].mean():.1f}%")
    with col4:
        st.metric("Reclamações pós (%)", f"{100*mock_sac['reclamacoes'].mean():.2f}%")
    st.plotly_chart(px.line(mock_sac, x="data", y="csat", title="CSAT (Customer Satisfaction Score)"), use_container_width=True)

    # 5. Métricas de Volume e Capacidade
    st.header("Métricas de Volume e Capacidade")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Sessões/dia", format_compact_number(mock_sac['sessoes_dia'].mean()))
    with col2:
        st.metric("Sessões/mês", format_compact_number(mock_sac['sessoes_mes'].mean()))
    with col3:
        st.metric("Simultâneas máx.", format_compact_number(mock_sac['sessoes_simultaneas'].max()))
    with col4:
        st.metric("Sessões WhatsApp/Web", f"{format_compact_number(mock_sac['sessoes_whatsapp'].mean())} / {format_compact_number(mock_sac['sessoes_web'].mean())}")
    st.plotly_chart(px.line(mock_sac, x="data", y="sessoes_dia", title="Total de sessões por dia"), use_container_width=True)

    # KPIs executivos
    st.header("KPIs Executivos")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("SLA resposta (%)", f"{100*mock_sac['sla'].mean():.1f}%")
    with col2:
        st.metric("Resolução sem humano (%)", f"{100*mock_sac['resolucao_sem_transfer'].mean():.1f}%")
    with col3:
        st.metric("CSAT médio", f"{mock_sac['csat'].mean():.2f}")
    with col4:
        st.metric("Reaberturas (%)", f"{100*mock_sac['reabertura'].mean():.1f}%")
    with col5:
        st.metric("Economia estimada (R$)", format_compact_number(mock_sac['economia'].sum()))

elif selected == "WhatsApp":
    st.title("Dashboard WhatsApp - Campanhas e Performance")
    st.write("Indicadores de performance, custo, status e templates de campanhas WhatsApp.")

    # MOCK: Dados fictícios para visualização
    dias = pd.date_range(end=datetime.now(), periods=14)
    mock_wpp = pd.DataFrame({
        "data": dias,
        "enviadas": np.random.randint(5000, 20000, len(dias)),
        "entregues": np.random.randint(4000, 19000, len(dias)),
        "lidas": np.random.randint(3000, 18000, len(dias)),
        "respostas": np.random.randint(500, 5000, len(dias)),
        "cliques": np.random.randint(200, 3000, len(dias)),
        "conversoes": np.random.randint(50, 1000, len(dias)),
        "custo_meta": np.random.uniform(100, 1000, len(dias)),
        "custo_gupshup": np.random.uniform(10, 100, len(dias)),
        "receita": np.random.uniform(1000, 10000, len(dias)),
        "custo_total": np.random.uniform(120, 1100, len(dias)),
    })

    # 1. Indicadores de Performance da Campanha
    st.header("Indicadores de Performance da Campanha")
    
    # Primeira linha de métricas
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Mensagens Enviadas", format_compact_number(mock_wpp["enviadas"].sum()))
    with col2:
        pct_entregues = 100 * mock_wpp["entregues"].sum() / max(1, mock_wpp["enviadas"].sum())
        st.metric("Taxa de Entrega", f"{pct_entregues:.1f}%")
    with col3:
        pct_lidas = 100 * mock_wpp["lidas"].sum() / max(1, mock_wpp["entregues"].sum())
        st.metric("Taxa de Leitura", f"{pct_lidas:.1f}%")
    with col4:
        pct_resposta = 100 * mock_wpp["respostas"].sum() / max(1, mock_wpp["entregues"].sum())
        st.metric("Taxa de Resposta", f"{pct_resposta:.1f}%")

    # Segunda linha de métricas
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        pct_clique = 100 * mock_wpp["cliques"].sum() / max(1, mock_wpp["entregues"].sum())
        st.metric("Taxa de Clique", f"{pct_clique:.1f}%")
    with col2:
        st.metric("Conversões", format_compact_number(mock_wpp["conversoes"].sum()))
    with col3:
        cpm = mock_wpp["conversoes"].sum() / max(1, mock_wpp["enviadas"].sum()/1000)
        st.metric("Conversões/1K msgs", f"{cpm:.2f}")
    with col4:
        roi = 100 * (mock_wpp["receita"].sum() - mock_wpp["custo_total"].sum()) / max(1, mock_wpp["custo_total"].sum())
        st.metric("ROI", f"{roi:.1f}%")

    # Gráfico de mensagens enviadas
    st.plotly_chart(px.line(mock_wpp, x="data", y="enviadas", title="Mensagens enviadas por dia"), use_container_width=True)

    # 2. Indicadores por Template e Campanha
    st.header("Indicadores por Template e Campanha")
    
    # Dados de custo por tipo de template
    custos_template = {
        "Marketing": {"meta": 0.0625, "gupshup": 0.001},
        "Marketing (Lite)": {"meta": 0.05625, "gupshup": 0.001},
        "Utility": {"meta": 0.008, "gupshup": 0.001},
        "Authentication": {"meta": 0.0315, "gupshup": 0.001},
        "Service": {"meta": 0.0, "gupshup": 0.001},
        "Ads Click to WhatsApp": {"meta": 0.0, "gupshup": 0.001},
        "Sessão (resposta)": {"meta": None, "gupshup": 0.001}
    }

    # Dados das campanhas com custos calculados
    campanhas = [
        {
            "Campanha": "Dia das Mães",
            "Tipo": "Marketing",
            "Enviadas": 10000,
            "Entregues": 9100,
            "Lidas": 7500,
            "Respostas": 2800,
            "CTR (%)": 18,
            "Conversões": 400,
            "Custo Meta (USD)": 10000 * 0.0625,
            "Custo Gupshup (USD)": 10000 * 0.001,
            "Custo Total (USD)": (10000 * 0.0625) + (10000 * 0.001),
            "ROI (%)": 260
        },
        {
            "Campanha": "Boletos",
            "Tipo": "Utility",
            "Enviadas": 5000,
            "Entregues": 4980,
            "Lidas": 4950,
            "Respostas": 150,
            "CTR (%)": 3,
            "Conversões": 70,
            "Custo Meta (USD)": 5000 * 0.008,
            "Custo Gupshup (USD)": 5000 * 0.001,
            "Custo Total (USD)": (5000 * 0.008) + (5000 * 0.001),
            "ROI (%)": 170
        }
    ]

    df_painel = pd.DataFrame(campanhas)
    st.dataframe(df_painel, use_container_width=True)

    # Resumo de custos
    st.subheader("Resumo de Custos")
    col1, col2, col3 = st.columns(3)
    with col1:
        custo_meta_total = sum(c["Custo Meta (USD)"] for c in campanhas)
        st.metric("Custo Total Meta (USD)", f"${custo_meta_total:.2f}")
    with col2:
        custo_gupshup_total = sum(c["Custo Gupshup (USD)"] for c in campanhas)
        st.metric("Custo Total Gupshup (USD)", f"${custo_gupshup_total:.2f}")
    with col3:
        custo_total = sum(c["Custo Total (USD)"] for c in campanhas)
        st.metric("Custo Total Geral (USD)", f"${custo_total:.2f}")

elif selected == "APIs Públicas":
    st.title("Teste de APIs Públicas")
    st.write("Aqui você pode testar algumas APIs públicas enquanto aguardamos os endpoints do projeto.")

    api_escolhida = st.selectbox(
        "Escolha uma API para testar:",
        ["ViaCEP (CEP)", "JSONPlaceholder (Posts)", "CoinGecko (Criptomoedas)", "Métricas Gemini (Vertex AI)"]
    )

    if api_escolhida == "ViaCEP (CEP)":
        cep = st.text_input("Digite um CEP (ex: 01001000)")
        if st.button("Consultar CEP") and cep:
            url = f"https://viacep.com.br/ws/{cep}/json/"
            try:
                resp = requests.get(url, timeout=5)
                if resp.status_code == 200:
                    st.json(resp.json())
                else:
                    st.error(f"Erro ao consultar: {resp.status_code}")
            except Exception as e:
                st.error(f"Erro: {e}")

    elif api_escolhida == "JSONPlaceholder (Posts)":
        post_id = st.number_input("Digite o ID do post (1-100)", min_value=1, max_value=100, value=1)
        if st.button("Buscar Post"):
            url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
            try:
                resp = requests.get(url, timeout=5)
                if resp.status_code == 200:
                    st.json(resp.json())
                else:
                    st.error(f"Erro ao consultar: {resp.status_code}")
            except Exception as e:
                st.error(f"Erro: {e}")

    elif api_escolhida == "CoinGecko (Criptomoedas)":
        st.subheader("Consulta de Preço de Criptoativos - CoinGecko")
        moedas = {
            "Bitcoin": "bitcoin",
            "Ethereum": "ethereum",
            "Solana": "solana",
            "BNB": "binancecoin",
            "Cardano": "cardano",
            "Dogecoin": "dogecoin",
            "Polygon": "matic-network",
            "XRP": "ripple"
        }
        moeda_nome = st.selectbox("Escolha a moeda:", list(moedas.keys()))
        moeda_id = moedas[moeda_nome]
        dias = st.slider("Quantos dias de histórico?", 1, 30, 7)
        if st.button("Buscar Histórico de Preço"):
            url = f"https://api.coingecko.com/api/v3/coins/{moeda_id}/market_chart?vs_currency=usd&days={dias}"
            try:
                resp = requests.get(url, timeout=10)
                if resp.status_code == 200:
                    data = resp.json()
                    prices = data["prices"]
                    df_crypto = pd.DataFrame(prices, columns=["timestamp", "price"])
                    df_crypto["timestamp"] = pd.to_datetime(df_crypto["timestamp"], unit="ms")
                    fig = px.line(df_crypto, x="timestamp", y="price", title=f"Preço do {moeda_nome} (USD) - Últimos {dias} dias")
                    fig.update_layout(xaxis_title="Data", yaxis_title="Preço (USD)")
                    st.plotly_chart(fig, use_container_width=True)
                    st.dataframe(df_crypto.tail(10), use_container_width=True)
                else:
                    st.error(f"Erro ao consultar: {resp.status_code}")
            except Exception as e:
                st.error(f"Erro: {e}")

    elif api_escolhida == "Métricas Gemini (Vertex AI)":
        st.subheader("Métricas do Gemini (Vertex AI) via Cloud Monitoring")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "global_ia.json"
        client = monitoring_v3.MetricServiceClient()
        project_id = "globalinteligenciaartificial"
        project_name = f"projects/{project_id}"

        # Período: últimos 7 dias
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(days=7)
        interval = monitoring_v3.TimeInterval({
            "end_time": {"seconds": int(end_time.timestamp())},
            "start_time": {"seconds": int(start_time.timestamp())}
        })

        metric_types = {
            "Request count": "aiplatform.googleapis.com/prediction/online_prediction_count",
            "Request latencies": "aiplatform.googleapis.com/prediction/online_prediction_latency",
            "Request sizes": "aiplatform.googleapis.com/prediction/online_prediction_request_bytes",
            "Response sizes": "aiplatform.googleapis.com/prediction/online_prediction_response_bytes"
        }

        for nome, metric_type in metric_types.items():
            st.markdown(f"#### {nome}")
            results = client.list_time_series(
                request={
                    "name": project_name,
                    "filter": f'metric.type = "{metric_type}"',
                    "interval": interval,
                    "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
                }
            )
            data = []
            for result in results:
                for point in result.points:
                    # Para métricas de distribuição (latência, tamanhos), pegar o valor médio
                    if hasattr(point.value, "distribution_value"):
                        mean = point.value.distribution_value.mean
                        valor = mean
                    else:
                        valor = getattr(point.value, "int64_value", None) or getattr(point.value, "double_value", None)
                    data.append({
                        "timestamp": point.interval.end_time.ToDatetime(),
                        "value": valor
                    })
            if data:
                df = pd.DataFrame(data)
                df = df.sort_values("timestamp")
                st.line_chart(df.set_index("timestamp")["value"])
                st.dataframe(df.tail(10), use_container_width=True)
            else:
                st.info("Sem dados para esta métrica no período.") 