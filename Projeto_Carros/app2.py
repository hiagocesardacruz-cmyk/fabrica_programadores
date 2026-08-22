import streamlit as st

st.sidebar.image("img/logo.jpg")
st.sidebar.markdown("# JR Locações")

lista_carros = ["eclipse", "evolution", "gt"]

detalhes_carro = {
    "eclipse": {"preço": 50000, "portas": "2 portas", "cor": "preto"},
    "evolution": {"preço": 70000, "portas": "4 portas", "cor": "cinza"},
    "gt": {"preço": 80000, "portas": "2 portas", "cor": "vermelho"},
}

carro_selecionado = st.sidebar.selectbox(
    "Selecione o carro que deseja", lista_carros
)

# Pega os detalhes do carro selecionado
detalhes_selecionado = detalhes_carro[carro_selecionado]

st.title(carro_selecionado.capitalize())
st.image(f"img/{carro_selecionado}.jpg")

st.subheader("Detalhes do Veículo")

col1, col2, col3 = st.columns(3)

col1.metric("Preço Diária", f'R$ {detalhes_selecionado["preço"]}')
col2.metric("Portas", detalhes_selecionado["portas"])
col3.metric("Cor", detalhes_selecionado["cor"].capitalize())

st.divider()

qtd_dias = st.number_input(
    "Quantos dias quer ficar com o carro?", min_value=1, value=1
)

if st.button("Alugar", type="primary"):
  custo_total = qtd_dias * detalhes_selecionado["preço"]
  st.success(f"O aluguel do carro vai custar: **R$ {custo_total}**")