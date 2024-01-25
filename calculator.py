import streamlit as st

def calcular_quantidade_novelos(largura_amostra, altura_amostra, peso_amostra, largura_peca, altura_peca, peso_novelo):
    area_amostra = largura_amostra * altura_amostra
    area_peca = largura_peca * altura_peca

    peso_peca = (peso_amostra * area_peca) / area_amostra

    quantidade_novelos = peso_peca / peso_novelo

    quantidade_novelos_arredondado = round(quantidade_novelos * 2) / 2
    
    return area_amostra, area_peca, peso_amostra, peso_peca, quantidade_novelos_arredondado

# Título do app
st.title("Calculadora de Novelos")

# Inputs do usuário
largura_amostra = st.number_input("Largura da amostra (cm):", min_value=1)
altura_amostra = st.number_input("Altura da amostra (cm):", min_value=1)
peso_amostra = st.number_input("Peso da amostra (g):", min_value=1)

largura_peca = st.number_input("Largura da peça (cm):", min_value=1)
altura_peca = st.number_input("Altura da peça (cm):", min_value=1)

peso_novelo = st.number_input("Peso unitário do novelo (g):", min_value=1)

# Botão para calcular
if st.button("Calcular"):
    area_amostra, area_peca, peso_amostra, peso_peca, quantidade_novelos = calcular_quantidade_novelos(largura_amostra, altura_amostra, peso_amostra, largura_peca, altura_peca, peso_novelo)

    # Exibir resultados
    # st.success(f"Área da amostra: {area_amostra:.2f} cm²")
    # st.success(f"Área da peça: {area_peca:.2f} cm²")
    # st.success(f"Peso da amostra: {peso_amostra:.2f} cm²")
    # st.success(f"Peso da peça: {peso_peca:.2f} cm²")
    st.success(f"Quantidade de novelos necessários: {quantidade_novelos:.2f}")
