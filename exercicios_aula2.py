# calculadora


import streamlit as st




st.title('Calculadora')


numero1 = st.number_input('numero1 ') 
numero2 = st.number_input('numero2 ', step=0.1)


if st.button('+'):
    soma = numero1 +  numero2
    st.success(soma)

if st.button('-'):
    soma = numero1 -  numero2
    st.success(soma)

if st.button('*'):
    soma = numero1 *  numero2
    st.success(soma)

if st.button('/'):
    soma = numero1 /  numero2
    st.success(soma)


# ----------------------------------------


# calculadora de imc



st.title('Calculo do imc')


peso = st.number_input('PESO')
altura = st.number_input('Altura')


if st.button('Calcular IMC'):
    calculo = round(peso / (altura ** 2), 2)
    st.success(calculo)

# ----------------------------------------


# 9. Média de Notas

st.title('9. Média de Notas')


nota1 = st.number_input('Nota1 ') 
nota2 = st.number_input('Nota2 ')


if st.button('Calcular Média'):
    media = (nota1 + nota2) / 2
    st.success(media)

# ----------------------------------------


# 8. Verificador de Número Par ou Ímpar

st.title('8. Verificador de Número Par ou Ímpar')

num = st.number_input('Digite um numero: ') 

if st.button('Verificar'):
    if (num % 2) == 0:
        st.success(f"O número $ {int(num)} $ é **PAR**!")
    else :
        st.success(f"O número $ {int(num)} $ é **ÍMPAR**!")  
