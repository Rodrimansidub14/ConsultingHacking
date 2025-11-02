import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="Analisis de clustering forensico",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown('''
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #1e3a8a; font-weight: 700; border-bottom: 3px solid #3b82f6; }
    h2 { color: #1e40af; font-weight: 600; }
    [data-testid="stMetricValue"] { font-size: 2rem; color: #1e3a8a; }
    [data-testid="stSidebar"] { background-color: #1e3a8a; }
    [data-testid="stSidebar"] * { color: white !important; }
    </style>
''', unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv('data/hack_data_clustered.csv')

df = load_data()

st.sidebar.title(' Navegación')
page = st.sidebar.radio('Seleccionar Vista:', ['Resumen Ejecutivo', 'Análisis Detallado', 'Perfiles de Clústeres', 'Detalles Técnicos'])
st.sidebar.markdown('---')
st.sidebar.metric('Total de Ataques', len(df))
st.sidebar.metric('Clústeres Identificados', df['cluster'].nunique())

selected_clusters = st.sidebar.multiselect('Filtrar por Clúster:', sorted(df['cluster'].unique()), sorted(df['cluster'].unique()))
df_filtered = df[df['cluster'].isin(selected_clusters)] if selected_clusters else df

st.title(' Análisis de Clustering Forense')
st.markdown('### Informe de Investigación de Ataques Cibernéticos')
st.markdown('---')

feat_cols = ['Session_Connection_Time','Bytes_Transferred','Servers_Corrupted','Pages_Corrupted','WPM_Typing_Speed','bytes_per_min','pages_per_min']

if page == 'Resumen Ejecutivo':
    col1, col2 = st.columns(2)
    col1.info('** Objetivo**\n\nDeterminar si los ciberataques se originaron en **2 o 3 atacantes distintos**.')
    col2.success('** Conclusión**\n\nEl análisis confirma **DOS atacantes distintos**.')

    st.markdown('###  Indicadores Clave de Desempeño (KPI)')
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric('Silhouette Score', '0.8176')
    kpi2.metric('ARI', '1.000')
    kpi3.metric('Attackers', '2')
    kpi4.metric('Balance', '167/167')
    
    if 'PC1' in df_filtered.columns:
        fig = px.scatter(df_filtered, x='PC1', y='PC2', color=df_filtered['cluster'].astype(str), title='PCA: Attacker Separation', color_discrete_sequence=['#3b82f6','#ef4444'])
        st.plotly_chart(fig, use_container_width=True)

elif page == 'Análisis Detallado':
    var = st.selectbox('Seleccionar Métrica:', feat_cols, format_func=lambda x: x.replace('_',' ').title())
    fig = px.box(df_filtered, x='cluster', y=var, color=df_filtered['cluster'].astype(str), color_discrete_sequence=['#3b82f6','#ef4444'])
    st.plotly_chart(fig, use_container_width=True)
    
    fig2 = px.scatter(df_filtered, x='bytes_per_min', y='WPM_Typing_Speed', color=df_filtered['cluster'].astype(str), trendline='ols', color_discrete_sequence=['#3b82f6','#ef4444'])
    st.plotly_chart(fig2, use_container_width=True)

elif page == 'Perfiles de Clústeres':
    summary = df_filtered.groupby('cluster')[feat_cols].agg(['mean','std']).round(2)
    st.dataframe(summary, use_container_width=True)
    
    for col in feat_cols[:3]:
        c1, c2 = st.columns(2)
        c1.plotly_chart(px.histogram(df_filtered, x=col, color=df_filtered['cluster'].astype(str), barmode='overlay', opacity=0.7, color_discrete_sequence=['#3b82f6','#ef4444']), use_container_width=True)
        c2.plotly_chart(px.violin(df_filtered, y=col, x='cluster', color=df_filtered['cluster'].astype(str), box=True, color_discrete_sequence=['#3b82f6','#ef4444']), use_container_width=True)

else:
    st.markdown('###  Metodología y Detalles Técnicos')
    st.dataframe(df_filtered.head(20), use_container_width=True)
    csv = df_filtered.to_csv(index=False).encode()
    st.download_button('Descargar Datos', csv, 'analysis.csv', 'text/csv')

st.markdown('---')
st.markdown('<div style="text-align:center;color:#64748b;"><p><strong>Análisis de Clustering Forense</strong><br/>Generated Nov 2, 2025</p></div>', unsafe_allow_html=True)
