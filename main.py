# #investimento de marketing

# import numpy  as np
# from sklearn.linear_model import LinearRegression
# # investimento em mkt 1mil
# X = np.array([[1],[2],[4],[5],[3]])
# # vendas 
# y =  np.array([2,8,4,6,5])

# modelo = LinearRegression()

# modelo.fit(X, y)

# print(modelo.predict([[6]]))

# import numpy as np
# from sklearn.tree import DecisionTreeClassifier

# X = np.array([
#     [1,5], 
#     [2,4], 
#     [3,3],
#     [4,1],
#     [5,0], 

# ])

# Y = np.array([1,1,1,0,0])
# modelo = DecisionTreeClassifier()
# modelo.fit(X,Y)

# print(modelo.predict([[10,3]]))


import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header("Previsão de Vendas")

# Dados: [Investimento em Marketing] -> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

# objetivo: previsão de FATURAMENTO baseado nos investimentos

st.bar_chart(dados_vendas, x = 'investimento', y = 'faturamento')

modelo_investimento = LinearRegression() 
modelo_investimento.fit(dados_vendas[['investimento']], dados_vendas['faturamento'])

i_dados_vendas = st.slider('valores investidos', 100,600,300)
valor_final = modelo_investimento.predict([[i_dados_vendas]])
print(valor_final)

st.metric(f'seu valor faturamento seria' ,f'{min(valor_final):.2f}')