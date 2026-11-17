import streamlit as st
from consumidor_api import obter_dados_meteorologicos

st.set_page_config(
    page_title="Monitoramento Meteorológico",
    page_icon="🌦️",
    layout="wide"
)

st.title("🌦️ Monitoramento Meteorológico")
st.caption("Estação meteorológica — Jaraguá do Sul/SC")

st.divider()

if st.button("🔄 Atualizar dados"):
    st.rerun()

try:
    with st.spinner("Consultando a API meteorológica..."):
        dados = obter_dados_meteorologicos()

    st.success("Dados meteorológicos carregados.")

    st.subheader("Condições atuais")

    col1, col2 = st.columns(2)

    col1.metric(
        "Latitude",
        f"{dados['latitude']:.3f} °C"
    )

    col2.metric(
        "Longitude",
        f"{dados['longitude']:.3f} %"
    )

    
    st.divider()
    
except Exception as erro:
    st.error(f"Não foi possível consultar os dados: {erro}")
