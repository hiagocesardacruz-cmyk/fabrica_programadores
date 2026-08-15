#Autor: Hiago Cesar Da Cruz Caldas
# Projeto: IMC com streamlitpython -m streamlit run imc.web.py

import streamlit as st

st.title('Calculadora de IMC')
peso = st.number_input('Digite seu peso (kg):')
altura = st.number_input('Digite sua altura(m):')

st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #8A00C4;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


#acão do botão
if st.button('Calcular IMC'):
    #verifica se o usuário digitou valor > que zero
   if peso > 0 and altura > 0:
      imc = peso / (altura ** 2)
      st.success(f'Seu imc é: {imc:.2f}')
      if imc <= 18.5:
         st.warning('Abaixo do peso', icon='⚠️')
      elif imc <= 24.9:
       st.success('Peso Normal!', icon ='✅')
      elif imc <= 29.9:
       st.warning('Sobrepeso', icon ='⚠️')
      elif imc <= 34.9:
        st.warning('Obesidade grau I', icon = '⚠️')
      elif imc <= 39.9:
        st.warning ('Obesidade grau II', icon = '⚠️')
      else:
       st.error('Obesidade grau III', icon = '❌')
   else:
     st.warning('Digite um valor válido')

